#!/usr/bin/env python
# encoding: utf-8

name = "H_Abstraction/PrIMe"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 17,
    label = "r00001370",
    reactant1 = 
"""
1 *1 C 0 {2,D} {3,S}
2    O 0 {1,D}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *2 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 1 {2,D}
2    O 0 {1,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1e+08,"cm^3/(mol*s)"),
        n = 0,
        Ea = (167360,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00001370/rk00000007.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00001370/rk00000007.xml
""",
    history = [
        ("Tue May 17 14:33:30 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00001370/rk00000007.xml"""),
        ("Tue May 17 18:03:57 2011","Josh Allen <jwallen@mit.edu>","action","""Fixed reversed reactants and products."""),
    ],
)

entry(
    index = 81,
    label = "r00001950",
    reactant1 = 
"""
1 *1 C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 C 1
""",
    product1 = 
"""
1 *1 C 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (6.14,"cm^3/(mol*s)"),
        n = 1.74,
        Ea = (43722.8,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00001950/rk00000003.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00001950/rk00000003.xml
""",
    history = [
        ("Tue May 17 14:33:32 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00001950/rk00000003.xml"""),
    ],
)

entry(
    index = 99,
    label = "r00001957",
    reactant1 = 
"""
1    C 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    reactant2 = 
"""
1 *3 C 1
""",
    product1 = 
"""
1 *1 C 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10,"cm^3/(mol*s)"),
        n = 1.5,
        Ea = (41589,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00001957/rk00000006.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00001957/rk00000006.xml
""",
    history = [
        ("Tue May 17 14:33:32 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00001957/rk00000006.xml"""),
    ],
)

entry(
    index = 110,
    label = "r00001965",
    reactant1 = 
"""
1 *1 C 0 {2,S} {3,S}
2    O 0 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 C 1
""",
    product1 = 
"""
1 *1 C 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 1 {2,S}
2    O 0 {1,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (30,"cm^3/(mol*s)"),
        n = 1.5,
        Ea = (41589,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00001965/rk00000003.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00001965/rk00000003.xml
""",
    history = [
        ("Tue May 17 14:33:32 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00001965/rk00000003.xml"""),
    ],
)

entry(
    index = 115,
    label = "r00001966",
    reactant1 = 
"""
1 *1 C 0 {2,D} {3,S}
2    O 0 {1,D}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 C 1
""",
    product1 = 
"""
1 *1 C 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 1 {2,D}
2    O 0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (0.00332,"cm^3/(mol*s)"),
        n = 2.81,
        Ea = (24518.2,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00001966/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00001966/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:33:32 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00001966/rk00000002.xml"""),
    ],
)

entry(
    index = 130,
    label = "r00001968",
    reactant1 = 
"""
1 *1 C 0 {2,D} {3,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 C 1
""",
    product1 = 
"""
1 *1 C 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,D}
2 *3 C 1 {1,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (0.227,"cm^3/(mol*s)"),
        n = 2,
        Ea = (38492.8,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00001968/rk00000004.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00001968/rk00000004.xml
""",
    history = [
        ("Tue May 17 14:33:32 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00001968/rk00000004.xml"""),
    ],
)

entry(
    index = 142,
    label = "r00001973",
    reactant1 = 
"""
1 *3 C 1
""",
    reactant2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S}
3 *2 H 0 {1,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (0.0245,"cm^3/(mol*s)"),
        n = 2.47,
        Ea = (21673.1,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00001973/rk00000004.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00001973/rk00000004.xml
""",
    history = [
        ("Tue May 17 14:33:32 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00001973/rk00000004.xml"""),
    ],
)

entry(
    index = 149,
    label = "r00002003",
    reactant1 = 
"""
1 *3 C 1
""",
    reactant2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *2 H 0 {1,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+06,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00002003/rk00000008.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00002003/rk00000008.xml
""",
    history = [
        ("Tue May 17 14:33:32 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00002003/rk00000008.xml"""),
    ],
)

entry(
    index = 187,
    label = "r00002017",
    reactant1 = 
"""
1 *1 C 0 {2,S}
2 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 H 1
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (660,"cm^3/(mol*s)"),
        n = 1.62,
        Ea = (45354.6,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00002017/rk00000056.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00002017/rk00000056.xml
""",
    history = [
        ("Tue May 17 14:33:33 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00002017/rk00000056.xml"""),
    ],
)

entry(
    index = 252,
    label = "r00002499",
    reactant1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,T}
2 *3 C 1 {1,T}
""",
    product1 = 
"""
1    C 0 {2,T}
2 *1 C 0 {1,T} {3,S}
3 *2 H 0 {2,S}
""",
    product2 = 
"""
1 *3 H 1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (56800,"cm^3/(mol*s)"),
        n = 0.9,
        Ea = (8338.71,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00002499/rk00000010.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00002499/rk00000010.xml
""",
    history = [
        ("Tue May 17 14:33:35 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00002499/rk00000010.xml"""),
    ],
)

entry(
    index = 627,
    label = "r00006096",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {4,S} {5,S}
3    C 0 {1,S}
4    C 0 {2,S} {6,D}
5 *2 H 0 {2,S}
6    O 0 {4,D}
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *3 C 1 {1,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {4,S}
3    C 0 {1,S}
4 *2 H 0 {2,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *3 C 1 {1,S} {4,S}
4    C 0 {3,S} {5,D}
5    O 0 {4,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (39800,"cm^3/(mol*s)"),
        n = 0,
        Ea = (40990.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Forgeteg, S.", "Berces, T.", "Dobe, S."],
        title = u'The kinetics and mechanism of n-butyraldehyde photolysis in the vapor phase at 313 nm',
        journal = "Int. J. Chem. Kinet.",
        volume = "11",
        pages = """219""",
        year = "1979",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00006096/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00006096/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:33:57 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00006096/rk00000002.xml"""),
    ],
)

entry(
    index = 629,
    label = "r00006129",
    reactant1 = 
"""
1     C 0 {3,S} {7,S}
2     C 0 {4,S} {8,S}
3     C 0 {1,S} {5,S}
4     C 0 {2,S} {6,S}
5     C 0 {3,S} {6,S}
6     C 0 {4,S} {5,S}
7     C 0 {1,S} {9,S}
8     C 0 {2,S} {10,S}
9  *1 C 0 {7,S} {11,S}
10    C 0 {8,S}
11 *2 H 0 {9,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1     C 0 {3,S} {7,S}
2     C 0 {4,S} {6,S}
3     C 0 {1,S} {5,S}
4     C 0 {2,S} {5,S}
5     C 0 {3,S} {4,S}
6     C 0 {2,S} {8,S}
7     C 0 {1,S} {9,S}
8     C 0 {6,S} {10,S}
9     C 0 {7,S}
10 *3 C 1 {8,S}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (14.1109,"cm^3/(mol*s)"),
        n = 1.8,
        Ea = (4074.09,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Cohen, N."],
        title = u'Are reaction rate coefficients additive? Revised transition state theory calculations for OH + alkane reactions',
        journal = "Int. J. Chem. Kinet.",
        volume = "23",
        pages = """397-417""",
        year = "1991",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00006129/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00006129/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:33:57 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00006129/rk00000001.xml"""),
    ],
)

entry(
    index = 630,
    label = "r00006130",
    reactant1 = 
"""
1     C 0 {3,S} {7,S}
2     C 0 {4,S} {8,S}
3     C 0 {1,S} {5,S}
4     C 0 {2,S} {6,S}
5     C 0 {3,S} {6,S}
6     C 0 {4,S} {5,S}
7  *1 C 0 {1,S} {9,S} {11,S}
8     C 0 {2,S} {10,S}
9     C 0 {7,S}
10    C 0 {8,S}
11 *2 H 0 {7,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1     C 0 {2,S} {6,S}
2     C 0 {1,S} {4,S}
3     C 0 {4,S} {5,S}
4     C 0 {2,S} {3,S}
5     C 0 {3,S} {7,S}
6     C 0 {1,S} {8,S}
7     C 0 {5,S} {10,S}
8     C 0 {6,S}
9     C 0 {10,S}
10 *3 C 1 {7,S} {9,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.99315,"cm^3/(mol*s)"),
        n = 2,
        Ea = (-2494.34,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Cohen, N."],
        title = u'Are reaction rate coefficients additive? Revised transition state theory calculations for OH + alkane reactions',
        journal = "Int. J. Chem. Kinet.",
        volume = "23",
        pages = """397-417""",
        year = "1991",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00006130/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00006130/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:33:57 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00006130/rk00000001.xml"""),
    ],
)

entry(
    index = 631,
    label = "r00006131",
    reactant1 = 
"""
1  *1 C 0 {3,S} {7,S} {11,S}
2     C 0 {4,S} {8,S}
3     C 0 {1,S} {5,S}
4     C 0 {2,S} {6,S}
5     C 0 {3,S} {6,S}
6     C 0 {4,S} {5,S}
7     C 0 {1,S} {9,S}
8     C 0 {2,S} {10,S}
9     C 0 {7,S}
10    C 0 {8,S}
11 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1     C 0 {2,S} {5,S}
2     C 0 {1,S} {3,S}
3     C 0 {2,S} {4,S}
4     C 0 {3,S} {6,S}
5     C 0 {1,S} {8,S}
6     C 0 {4,S} {10,S}
7     C 0 {9,S} {10,S}
8     C 0 {5,S}
9     C 0 {7,S}
10 *3 C 1 {6,S} {7,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (6.75645,"cm^3/(mol*s)"),
        n = 2,
        Ea = (-5820.13,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Cohen, N."],
        title = u'Are reaction rate coefficients additive? Revised transition state theory calculations for OH + alkane reactions',
        journal = "Int. J. Chem. Kinet.",
        volume = "23",
        pages = """397-417""",
        year = "1991",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00006131/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00006131/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:33:57 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00006131/rk00000001.xml"""),
    ],
)

entry(
    index = 632,
    label = "r00006132",
    reactant1 = 
"""
1     C 0 {3,S} {7,S}
2     C 0 {4,S} {8,S}
3     C 0 {1,S} {5,S}
4     C 0 {2,S} {6,S}
5  *1 C 0 {3,S} {6,S} {11,S}
6     C 0 {4,S} {5,S}
7     C 0 {1,S} {9,S}
8     C 0 {2,S} {10,S}
9     C 0 {7,S}
10    C 0 {8,S}
11 *2 H 0 {5,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1     C 0 {3,S} {5,S}
2     C 0 {4,S} {6,S}
3     C 0 {1,S} {7,S}
4     C 0 {2,S} {8,S}
5     C 0 {1,S} {9,S}
6     C 0 {2,S} {10,S}
7     C 0 {3,S} {10,S}
8     C 0 {4,S}
9     C 0 {5,S}
10 *3 C 1 {6,S} {7,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (6.79023,"cm^3/(mol*s)"),
        n = 2,
        Ea = (-5820.13,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Cohen, N."],
        title = u'Are reaction rate coefficients additive? Revised transition state theory calculations for OH + alkane reactions',
        journal = "Int. J. Chem. Kinet.",
        volume = "23",
        pages = """397-417""",
        year = "1991",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00006132/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00006132/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:33:57 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00006132/rk00000001.xml"""),
    ],
)

entry(
    index = 635,
    label = "r00006332",
    reactant1 = 
"""
1 *1 C 0 {3,S} {4,S} {8,S}
2    C 0 {3,S} {5,S}
3    C 0 {1,S} {2,S}
4    C 0 {1,S} {6,S}
5    C 0 {2,S} {7,S}
6    C 0 {4,S}
7    C 0 {5,S}
8 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {5,S}
3    C 0 {1,S} {7,S}
4    C 0 {6,S} {7,S}
5    C 0 {2,S}
6    C 0 {4,S}
7 *3 C 1 {3,S} {4,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (4.36917,"cm^3/(mol*s)"),
        n = 2,
        Ea = (-5487.55,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Cohen, N."],
        title = u'Are reaction rate coefficients additive? Revised transition state theory calculations for OH + alkane reactions',
        journal = "Int. J. Chem. Kinet.",
        volume = "23",
        pages = """397-417""",
        year = "1991",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00006332/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00006332/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:33:58 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00006332/rk00000001.xml"""),
    ],
)

entry(
    index = 636,
    label = "r00006333",
    reactant1 = 
"""
1    C 0 {3,S} {4,S}
2    C 0 {3,S} {5,S}
3 *1 C 0 {1,S} {2,S} {8,S}
4    C 0 {1,S} {6,S}
5    C 0 {2,S} {7,S}
6    C 0 {4,S}
7    C 0 {5,S}
8 *2 H 0 {3,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {3,S} {5,S}
2    C 0 {4,S} {6,S}
3    C 0 {1,S} {7,S}
4    C 0 {2,S} {7,S}
5    C 0 {1,S}
6    C 0 {2,S}
7 *3 C 1 {3,S} {4,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.36917,"cm^3/(mol*s)"),
        n = 2,
        Ea = (-5487.55,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Cohen, N."],
        title = u'Are reaction rate coefficients additive? Revised transition state theory calculations for OH + alkane reactions',
        journal = "Int. J. Chem. Kinet.",
        volume = "23",
        pages = """397-417""",
        year = "1991",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00006333/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00006333/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:33:58 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00006333/rk00000001.xml"""),
    ],
)

entry(
    index = 645,
    label = "r00006483",
    reactant1 = 
"""
1 *1 C 0 {2,S} {3,S} {6,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S} {5,S}
4    C 0 {2,S} {5,S}
5    C 0 {3,S} {4,S}
6 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,B} {3,B}
2    C 0 {1,B} {4,B}
3    C 0 {1,B} {5,B}
4    C 0 {2,B} {6,B}
5    C 0 {3,B} {6,B}
6 *3 C 1 {4,B} {5,B}
""",
    product1 = 
"""
1    C 0 {2,B} {3,B}
2    C 0 {1,B} {4,B}
3 *1 C 0 {1,B} {5,B} {7,S}
4    C 0 {2,B} {6,B}
5    C 0 {3,B} {6,B}
6    C 0 {4,B} {5,B}
7 *2 H 0 {3,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S} {5,S}
4    C 0 {2,S} {5,S}
5 *3 C 1 {3,S} {4,S}
""",
    degeneracy = 10,
    kinetics = Arrhenius(
        A = (2.69e+06,"cm^3/(mol*s)"),
        n = 0,
        Ea = (16961.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Yu, T.", "Lin, M.C."],
        title = u'Kinetics of phenyl radical reactions with selected cycloalkanes and carbon tetrachloride',
        journal = "J. Phys. Chem.",
        volume = "99",
        pages = """8599-8603""",
        year = "1995",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00006483/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00006483/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:34:01 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00006483/rk00000002.xml"""),
    ],
)

entry(
    index = 659,
    label = "r00007011",
    reactant1 = 
"""
1 *1 C 0 {2,D} {3,S}
2    C 0 {1,D} {4,D}
3 *2 H 0 {1,S}
4    O 0 {2,D}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 1 {2,D}
2    C 0 {1,D} {3,D}
3    O 0 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.5e+06,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8368,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00007011/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007011/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:34:02 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007011/rk00000002.xml"""),
    ],
)

entry(
    index = 685,
    label = "r00007083",
    reactant1 = 
"""
1    C 0 {2,S} {3,S} {4,S} {5,S}
2 *1 C 0 {1,S} {6,S} {7,S} {8,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    C 0 {1,S}
6    C 0 {2,S}
7    C 0 {2,S}
8 *2 H 0 {2,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {4,S} {7,S}
2    C 0 {1,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    C 0 {7,S}
6    C 0 {7,S}
7 *3 C 1 {1,S} {5,S} {6,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.26e+06,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-798.189,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Greiner, N.R."],
        title = u'Hydroxyl radical kinetics by kinetic spectroscopy. VI. Reactions with alkanes in the range 300-500K',
        journal = "J. Chem. Phys.",
        volume = "53",
        pages = """1070""",
        year = "1970",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00007083/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007083/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:34:02 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007083/rk00000001.xml"""),
    ],
)

entry(
    index = 686,
    label = "r00007083",
    reactant1 = 
"""
1    C 0 {2,S} {3,S} {4,S} {5,S}
2 *1 C 0 {1,S} {6,S} {7,S} {8,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    C 0 {1,S}
6    C 0 {2,S}
7    C 0 {2,S}
8 *2 H 0 {2,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {4,S} {7,S}
2    C 0 {1,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    C 0 {7,S}
6    C 0 {7,S}
7 *3 C 1 {1,S} {5,S} {6,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.09e+06,"cm^3/(mol*s)"),
        n = 0,
        Ea = (457.296,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Baldwin, R.R.", "Walker, R.W.", "Walker, R.W."],
        title = u'Addition of 2,2,3-Trimethylbutane to Slowly Reacting Mixtures of Hydrogen and Oxygen at 480^oC',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "77",
        pages = """2157""",
        year = "1981",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00007083/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007083/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:34:02 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007083/rk00000002.xml"""),
    ],
)

entry(
    index = 687,
    label = "r00007083",
    reactant1 = 
"""
1    C 0 {2,S} {3,S} {4,S} {5,S}
2 *1 C 0 {1,S} {6,S} {7,S} {8,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    C 0 {1,S}
6    C 0 {2,S}
7    C 0 {2,S}
8 *2 H 0 {2,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {4,S} {7,S}
2    C 0 {1,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    C 0 {7,S}
6    C 0 {7,S}
7 *3 C 1 {1,S} {5,S} {6,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+06,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-956.164,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Baldwin, R.R.", "Walker, R.W.", "Walker, R.W."],
        title = u'Addition of 2,2,3-Trimethylbutane to Slowly Reacting Mixtures of Hydrogen and Oxygen at 480^oC',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "77",
        pages = """2157""",
        year = "1981",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00007083/rk00000003.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007083/rk00000003.xml
""",
    history = [
        ("Tue May 17 14:34:02 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007083/rk00000003.xml"""),
    ],
)

entry(
    index = 688,
    label = "r00007083",
    reactant1 = 
"""
1    C 0 {2,S} {3,S} {4,S} {5,S}
2 *1 C 0 {1,S} {6,S} {7,S} {8,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    C 0 {1,S}
6    C 0 {2,S}
7    C 0 {2,S}
8 *2 H 0 {2,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {4,S} {7,S}
2    C 0 {1,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    C 0 {7,S}
6    C 0 {7,S}
7 *3 C 1 {1,S} {5,S} {6,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2197.99,"cm^3/(mol*s)"),
        n = 1,
        Ea = (-2743.78,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Walker, R.W."],
        title = u'Temperature coefficients for reactions of OH radicals with alkanes between 300 and 1000 K',
        journal = "Int. J. Chem. Kinet.",
        volume = "17",
        pages = """573""",
        year = "1985",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00007083/rk00000004.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007083/rk00000004.xml
""",
    history = [
        ("Tue May 17 14:34:02 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007083/rk00000004.xml"""),
    ],
)

entry(
    index = 689,
    label = "r00007083",
    reactant1 = 
"""
1    C 0 {2,S} {3,S} {4,S} {5,S}
2 *1 C 0 {1,S} {6,S} {7,S} {8,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    C 0 {1,S}
6    C 0 {2,S}
7    C 0 {2,S}
8 *2 H 0 {2,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {4,S} {7,S}
2    C 0 {1,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    C 0 {7,S}
6    C 0 {7,S}
7 *3 C 1 {1,S} {5,S} {6,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.13734,"cm^3/(mol*s)"),
        n = 2,
        Ea = (-6543.49,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Atkinson, R."],
        title = u'Estimations of OH radical rate constants from H-atom abstraction from C-H and O-H bonds over the temperature range 250-1000K',
        journal = "Int. J. Chem. Kinet.",
        volume = "18",
        pages = """555""",
        year = "1986",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00007083/rk00000005.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007083/rk00000005.xml
""",
    history = [
        ("Tue May 17 14:34:02 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007083/rk00000005.xml"""),
    ],
)

entry(
    index = 690,
    label = "r00007083",
    reactant1 = 
"""
1    C 0 {2,S} {3,S} {4,S} {5,S}
2 *1 C 0 {1,S} {6,S} {7,S} {8,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    C 0 {1,S}
6    C 0 {2,S}
7    C 0 {2,S}
8 *2 H 0 {2,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {4,S} {7,S}
2    C 0 {1,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    C 0 {7,S}
6    C 0 {7,S}
7 *3 C 1 {1,S} {5,S} {6,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.93239,"cm^3/(mol*s)"),
        n = 2,
        Ea = (-7898.75,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Cohen, N."],
        title = u'Are reaction rate coefficients additive? Revised transition state theory calculations for OH + alkane reactions',
        journal = "Int. J. Chem. Kinet.",
        volume = "23",
        pages = """397-417""",
        year = "1991",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00007083/rk00000006.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007083/rk00000006.xml
""",
    history = [
        ("Tue May 17 14:34:02 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007083/rk00000006.xml"""),
    ],
)

entry(
    index = 691,
    label = "r00007084",
    reactant1 = 
"""
1    C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S} {6,S} {7,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    C 0 {1,S}
6 *1 C 0 {2,S} {8,S}
7    C 0 {2,S}
8 *2 H 0 {6,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S} {6,S} {7,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    C 0 {1,S}
6    C 0 {2,S}
7 *3 C 1 {2,S}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (3.69e+06,"cm^3/(mol*s)"),
        n = 0,
        Ea = (6842.81,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Greiner, N.R."],
        title = u'Hydroxyl radical kinetics by kinetic spectroscopy. VI. Reactions with alkanes in the range 300-500K',
        journal = "J. Chem. Phys.",
        volume = "53",
        pages = """1070""",
        year = "1970",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00007084/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007084/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:34:02 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007084/rk00000001.xml"""),
    ],
)

entry(
    index = 692,
    label = "r00007084",
    reactant1 = 
"""
1    C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S} {6,S} {7,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    C 0 {1,S}
6 *1 C 0 {2,S} {8,S}
7    C 0 {2,S}
8 *2 H 0 {6,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S} {6,S} {7,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    C 0 {1,S}
6    C 0 {2,S}
7 *3 C 1 {2,S}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (5.3939,"cm^3/(mol*s)"),
        n = 2,
        Ea = (1887.39,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Atkinson, R."],
        title = u'Estimations of OH radical rate constants from H-atom abstraction from C-H and O-H bonds over the temperature range 250-1000K',
        journal = "Int. J. Chem. Kinet.",
        volume = "18",
        pages = """555""",
        year = "1986",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00007084/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007084/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:34:02 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007084/rk00000002.xml"""),
    ],
)

entry(
    index = 693,
    label = "r00007084",
    reactant1 = 
"""
1    C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S} {6,S} {7,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    C 0 {1,S}
6 *1 C 0 {2,S} {8,S}
7    C 0 {2,S}
8 *2 H 0 {6,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S} {6,S} {7,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    C 0 {1,S}
6    C 0 {2,S}
7 *3 C 1 {2,S}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (20.0227,"cm^3/(mol*s)"),
        n = 1.8,
        Ea = (6069.56,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Cohen, N."],
        title = u'Are reaction rate coefficients additive? Revised transition state theory calculations for OH + alkane reactions',
        journal = "Int. J. Chem. Kinet.",
        volume = "23",
        pages = """397-417""",
        year = "1991",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00007084/rk00000003.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007084/rk00000003.xml
""",
    history = [
        ("Tue May 17 14:34:02 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007084/rk00000003.xml"""),
    ],
)

entry(
    index = 695,
    label = "r00007395",
    reactant1 = 
"""
1    C 0 {3,S} {4,S} {5,S} {6,S}
2 *1 C 0 {3,S} {7,S} {8,S} {9,S}
3    C 0 {1,S} {2,S}
4    C 0 {1,S}
5    C 0 {1,S}
6    C 0 {1,S}
7    C 0 {2,S}
8    C 0 {2,S}
9 *2 H 0 {2,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S} {8,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    C 0 {1,S}
6    C 0 {8,S}
7    C 0 {8,S}
8 *3 C 1 {2,S} {6,S} {7,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.13734,"cm^3/(mol*s)"),
        n = 2,
        Ea = (-6543.49,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Atkinson, R."],
        title = u'Estimations of OH radical rate constants from H-atom abstraction from C-H and O-H bonds over the temperature range 250-1000K',
        journal = "Int. J. Chem. Kinet.",
        volume = "18",
        pages = """555""",
        year = "1986",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00007395/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007395/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:34:07 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007395/rk00000001.xml"""),
    ],
)

entry(
    index = 696,
    label = "r00007395",
    reactant1 = 
"""
1    C 0 {3,S} {4,S} {5,S} {6,S}
2 *1 C 0 {3,S} {7,S} {8,S} {9,S}
3    C 0 {1,S} {2,S}
4    C 0 {1,S}
5    C 0 {1,S}
6    C 0 {1,S}
7    C 0 {2,S}
8    C 0 {2,S}
9 *2 H 0 {2,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S} {8,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    C 0 {1,S}
6    C 0 {8,S}
7    C 0 {8,S}
8 *3 C 1 {2,S} {6,S} {7,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.698,"cm^3/(mol*s)"),
        n = 1.9,
        Ea = (-6069.56,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Cohen, N."],
        title = u'Are reaction rate coefficients additive? Revised transition state theory calculations for OH + alkane reactions',
        journal = "Int. J. Chem. Kinet.",
        volume = "23",
        pages = """397-417""",
        year = "1991",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00007395/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007395/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:34:07 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007395/rk00000002.xml"""),
    ],
)

entry(
    index = 697,
    label = "r00007396",
    reactant1 = 
"""
1    C 0 {3,S} {4,S} {5,S} {6,S}
2    C 0 {3,S} {7,S} {8,S}
3    C 0 {1,S} {2,S}
4    C 0 {1,S}
5    C 0 {1,S}
6    C 0 {1,S}
7 *1 C 0 {2,S} {9,S}
8    C 0 {2,S}
9 *2 H 0 {7,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {3,S} {4,S} {5,S} {6,S}
2    C 0 {3,S} {7,S} {8,S}
3    C 0 {1,S} {2,S}
4    C 0 {1,S}
5    C 0 {1,S}
6    C 0 {1,S}
7    C 0 {2,S}
8 *3 C 1 {2,S}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (5.3939,"cm^3/(mol*s)"),
        n = 2,
        Ea = (1887.39,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Atkinson, R."],
        title = u'Estimations of OH radical rate constants from H-atom abstraction from C-H and O-H bonds over the temperature range 250-1000K',
        journal = "Int. J. Chem. Kinet.",
        volume = "18",
        pages = """555""",
        year = "1986",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00007396/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007396/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:34:07 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007396/rk00000001.xml"""),
    ],
)

entry(
    index = 698,
    label = "r00007396",
    reactant1 = 
"""
1    C 0 {3,S} {4,S} {5,S} {6,S}
2    C 0 {3,S} {7,S} {8,S}
3    C 0 {1,S} {2,S}
4    C 0 {1,S}
5    C 0 {1,S}
6    C 0 {1,S}
7 *1 C 0 {2,S} {9,S}
8    C 0 {2,S}
9 *2 H 0 {7,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {3,S} {4,S} {5,S} {6,S}
2    C 0 {3,S} {7,S} {8,S}
3    C 0 {1,S} {2,S}
4    C 0 {1,S}
5    C 0 {1,S}
6    C 0 {1,S}
7    C 0 {2,S}
8 *3 C 1 {2,S}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (17.8058,"cm^3/(mol*s)"),
        n = 1.8,
        Ea = (5986.42,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Cohen, N."],
        title = u'Are reaction rate coefficients additive? Revised transition state theory calculations for OH + alkane reactions',
        journal = "Int. J. Chem. Kinet.",
        volume = "23",
        pages = """397-417""",
        year = "1991",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00007396/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007396/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:34:07 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007396/rk00000002.xml"""),
    ],
)

entry(
    index = 707,
    label = "r00007720",
    reactant1 = 
"""
1 *1 C 0 {3,S} {5,S}
2    C 0 {4,S}
3    C 0 {1,S} {4,D}
4    C 0 {2,S} {3,D}
5 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 C 1
""",
    product1 = 
"""
1 *1 C 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D} {4,S}
4 *3 C 1 {3,S}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (16000,"cm^3/(mol*s)"),
        n = 0,
        Ea = (30514.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Yokoyama, N.", "Brinton, R.K."],
        title = u'Reaction of methyl radicals with cis-butene-2',
        journal = "Can. J. Chem.",
        volume = "47",
        pages = """2987""",
        year = "1969",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00007720/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007720/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:34:09 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007720/rk00000001.xml"""),
    ],
)

entry(
    index = 708,
    label = "r00007720",
    reactant1 = 
"""
1 *1 C 0 {3,S} {5,S}
2    C 0 {4,S}
3    C 0 {1,S} {4,D}
4    C 0 {2,S} {3,D}
5 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 C 1
""",
    product1 = 
"""
1 *1 C 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D} {4,S}
4 *3 C 1 {3,S}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (180000,"cm^3/(mol*s)"),
        n = 0,
        Ea = (33923,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Warnatz, J."],
        year = "1984",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00007720/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007720/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:34:09 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007720/rk00000002.xml"""),
    ],
)

entry(
    index = 709,
    label = "r00007720",
    reactant1 = 
"""
1 *1 C 0 {3,S} {5,S}
2    C 0 {4,S}
3    C 0 {1,S} {4,D}
4    C 0 {2,S} {3,D}
5 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 C 1
""",
    product1 = 
"""
1 *1 C 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D} {4,S}
4 *3 C 1 {3,S}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (309000,"cm^3/(mol*s)"),
        n = 0,
        Ea = (34920.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Sway, M.I."],
        title = u'Arrhenius parameters for reactions of methyl radicals with alkenes',
        journal = "Ber. Bunsenges. Phys. Chem.",
        volume = "29",
        pages = """900""",
        year = "1990",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00007720/rk00000004.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007720/rk00000004.xml
""",
    history = [
        ("Tue May 17 14:34:09 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007720/rk00000004.xml"""),
    ],
)

entry(
    index = 710,
    label = "r00007723",
    reactant1 = 
"""
1    C 0 {3,S}
2    C 0 {4,S}
3 *1 C 0 {1,S} {4,D} {5,S}
4    C 0 {2,S} {3,D}
5 *2 H 0 {3,S}
""",
    reactant2 = 
"""
1    C 0 {2,S} {4,S}
2    C 0 {1,S}
3    C 0 {4,S}
4 *3 C 1 {1,S} {3,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S} {3,S} {5,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S}
4    C 0 {2,S}
5 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {3,S}
2    C 0 {4,S}
3    C 0 {1,S} {4,D}
4 *3 C 1 {2,S} {3,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (251000,"cm^3/(mol*s)"),
        n = 0,
        Ea = (33507.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Collongues, C.", "Richard, C.", "Martin, R."],
        title = u'Thermal reaction of hydrogen-butene-2-cis mixtures at 500C: Hydrogenation, hydrogenolysis, and thermal reaction of the olefin',
        journal = "Int. J. Chem. Kinet.",
        volume = "15",
        pages = """5""",
        year = "1983",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00007723/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007723/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:34:09 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007723/rk00000001.xml"""),
    ],
)

entry(
    index = 711,
    label = "r00007724",
    reactant1 = 
"""
1 *1 C 0 {3,S} {5,S}
2    C 0 {4,S}
3    C 0 {1,S} {4,D}
4    C 0 {2,S} {3,D}
5 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4    C 0 {1,S}
5 *3 O 1 {1,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4    C 0 {1,S}
5 *1 O 0 {1,S} {6,S}
6 *2 H 0 {5,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D} {4,S}
4 *3 C 1 {3,S}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (1.17e+07,"cm^3/(mol*s)"),
        n = 0,
        Ea = (25026.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Sway, M.I.", "Waddington, D.J."],
        title = u'Reactons of oxygenated radicals in the gas phase. Part 13. Reactions of t-Butoxyl radicals with alkanes and alkenes',
        journal = "J. Chem. Soc. Perkin Trans. 2",
        pages = """63""",
        year = "1984",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00007724/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007724/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:34:09 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007724/rk00000001.xml"""),
    ],
)

entry(
    index = 712,
    label = "r00007758",
    reactant1 = 
"""
1 *1 C 0 {3,S} {5,S}
2    C 0 {4,S}
3    C 0 {1,S} {4,D}
4    C 0 {2,S} {3,D}
5 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S} {3,S}
3    C 0 {2,S} {4,D}
4    C 0 {3,D}
""",
    product1 = 
"""
1 *1 C 0 {2,S} {3,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S} {4,D}
4    C 0 {3,D}
5 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D} {4,S}
4 *3 C 1 {3,S}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (3.98e+07,"cm^3/(mol*s)"),
        n = 0,
        Ea = (66100.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Richard, C.", "Boiveaut, A.", "Martin, R."],
        title = u'H_2S-Promoted Therm al Isomerization of Butene-2 cis to Butene-1 or Butene-2 trans around 500^oC',
        journal = "Int. J. Chem. Kinet.",
        volume = "12",
        pages = """921""",
        year = "1980",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00007758/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007758/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:34:09 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007758/rk00000001.xml"""),
    ],
)

entry(
    index = 731,
    label = "r00008211",
    reactant1 = 
"""
1 *1 C 0 {3,S} {5,S}
2    C 0 {4,S}
3    C 0 {1,S} {4,D}
4    C 0 {2,S} {3,D}
5 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 C 1
""",
    product1 = 
"""
1 *1 C 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D} {4,S}
4 *3 C 1 {3,S}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (1e+06,"cm^3/(mol*s)"),
        n = 0,
        Ea = (40242,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Warnatz, J."],
        year = "1984",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00008211/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00008211/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:34:14 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00008211/rk00000002.xml"""),
    ],
)

entry(
    index = 732,
    label = "r00008214",
    reactant1 = 
"""
1 *1 C 0 {3,S} {5,S}
2    C 0 {4,S}
3    C 0 {1,S} {4,D}
4    C 0 {2,S} {3,D}
5 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4    C 0 {1,S}
5 *3 O 1 {1,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4    C 0 {1,S}
5 *1 O 0 {1,S} {6,S}
6 *2 H 0 {5,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D} {4,S}
4 *3 C 1 {3,S}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (1.95e+07,"cm^3/(mol*s)"),
        n = 0,
        Ea = (26523.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Sway, M.I.", "Waddington, D.J."],
        title = u'Reactons of oxygenated radicals in the gas phase. Part 13. Reactions of t-Butoxyl radicals with alkanes and alkenes',
        journal = "J. Chem. Soc. Perkin Trans. 2",
        pages = """63""",
        year = "1984",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00008214/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00008214/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:34:14 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00008214/rk00000001.xml"""),
    ],
)

entry(
    index = 756,
    label = "r00009460",
    reactant1 = 
"""
1 *1 C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 H 1
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (115,"cm^3/(mol*s)"),
        n = 1.9,
        Ea = (31505.5,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00009460/rk00000016.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00009460/rk00000016.xml
""",
    history = [
        ("Tue May 17 14:34:25 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00009460/rk00000016.xml"""),
    ],
)

entry(
    index = 785,
    label = "r00009467",
    reactant1 = 
"""
1    C 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    reactant2 = 
"""
1 *3 H 1
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.2,"cm^3/(mol*s)"),
        n = 2.1,
        Ea = (20376.1,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00009467/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00009467/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:34:25 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00009467/rk00000002.xml"""),
    ],
)

entry(
    index = 795,
    label = "r00009476",
    reactant1 = 
"""
1 *1 C 0 {2,S} {3,S}
2    O 0 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 H 1
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 1 {2,S}
2    O 0 {1,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (17,"cm^3/(mol*s)"),
        n = 2.1,
        Ea = (20376.1,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00009476/rk00000003.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00009476/rk00000003.xml
""",
    history = [
        ("Tue May 17 14:34:25 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00009476/rk00000003.xml"""),
    ],
)

entry(
    index = 800,
    label = "r00009476",
    reactant1 = 
"""
1 *1 C 0 {2,S} {3,S}
2    O 0 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 H 1
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 1 {2,S}
2    O 0 {1,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (16.4407,"cm^3/(mol*s)"),
        n = 2,
        Ea = (18873.9,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Li, S.C.", "Williams, F.A."],
        title = u'Experimental and numerical studies of two-stage methanol flames',
        journal = "Symp. Int. Combust. Proc.",
        volume = "26",
        pages = """1017-1024""",
        year = "1996",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00009476/rk00000008.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00009476/rk00000008.xml
""",
    history = [
        ("Tue May 17 14:34:25 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00009476/rk00000008.xml"""),
    ],
)

entry(
    index = 803,
    label = "r00009477",
    reactant1 = 
"""
1 *1 C 0 {2,D} {3,S}
2    O 0 {1,D}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 H 1
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 1 {2,D}
2    O 0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (57.4,"cm^3/(mol*s)"),
        n = 1.9,
        Ea = (11472.5,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00009477/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00009477/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:34:25 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00009477/rk00000002.xml"""),
    ],
)

entry(
    index = 831,
    label = "r00009480",
    reactant1 = 
"""
1 *1 C 0 {2,D} {3,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 H 1
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,D}
2 *3 C 1 {1,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.325,"cm^3/(mol*s)"),
        n = 2.53,
        Ea = (51212.2,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00009480/rk00000013.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00009480/rk00000013.xml
""",
    history = [
        ("Tue May 17 14:34:25 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00009480/rk00000013.xml"""),
    ],
)

entry(
    index = 856,
    label = "r00009484",
    reactant1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 H 1
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (12.1,"cm^3/(mol*s)"),
        n = 2,
        Ea = (21756.8,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00009484/rk00000008.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00009484/rk00000008.xml
""",
    history = [
        ("Tue May 17 14:34:26 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00009484/rk00000008.xml"""),
    ],
)

entry(
    index = 871,
    label = "r00009509",
    reactant1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 H 1
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.48e+07,"cm^3/(mol*s)"),
        n = 0,
        Ea = (4468.51,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00009509/rk00000007.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00009509/rk00000007.xml
""",
    history = [
        ("Tue May 17 14:34:26 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00009509/rk00000007.xml"""),
    ],
)

entry(
    index = 881,
    label = "r00009579",
    reactant1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {3,S}
2    C 0 {4,S}
3    C 0 {1,S} {4,D}
4 *3 C 1 {2,S} {3,D}
""",
    product1 = 
"""
1    C 0 {3,S}
2    C 0 {4,S}
3    C 0 {1,S} {4,D}
4 *1 C 0 {2,S} {3,D} {5,S}
5 *2 H 0 {4,S}
""",
    product2 = 
"""
1 *3 H 1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.26e+07,"cm^3/(mol*s)"),
        n = 0,
        Ea = (101437,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Collongues, C.", "Richard, C.", "Martin, R."],
        title = u'Thermal reaction of hydrogen-butene-2-cis mixtures at 500C: Hydrogenation, hydrogenolysis, and thermal reaction of the olefin',
        journal = "Int. J. Chem. Kinet.",
        volume = "15",
        pages = """5""",
        year = "1983",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00009579/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00009579/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:34:26 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00009579/rk00000001.xml"""),
    ],
)

entry(
    index = 893,
    label = "r00010403",
    reactant1 = 
"""
1    C 0 {2,T}
2 *3 C 1 {1,T}
""",
    reactant2 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product1 = 
"""
1    C 0 {2,T}
2 *1 C 0 {1,T} {3,S}
3 *2 H 0 {2,S}
""",
    product2 = 
"""
1 *3 O 1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.26465e+06,"cm^3/(molecule*s)"),
        n = 0,
        Ea = (-18225.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Ding, Y.", "Zhang, X.", "Li, Z.", "Huang, X.", "Sun, C."],
        title = u'Is the C_2H + H_2O Reaction Anomalous?',
        journal = "J. Phys. Chem. A",
        volume = "105",
        pages = """8206-8215""",
        year = "2001",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00010403/rk00000003.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010403/rk00000003.xml
""",
    history = [
        ("Tue May 17 14:34:34 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010403/rk00000003.xml"""),
        ("Tue May 17 16:45:41 2011","Josh Allen <jwallen@mit.edu>","action","""Fixed a typo in the units of the preexponential factor."""),
    ],
)

entry(
    index = 894,
    label = "r00010403",
    reactant1 = 
"""
1 *1 C 0 {2,T} {3,S}
2    C 0 {1,T}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,T}
2 *3 C 1 {1,T}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (33.7,"cm^3/(mol*s)"),
        n = 2,
        Ea = (58576,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00010403/rk00000004.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010403/rk00000004.xml
""",
    history = [
        ("Tue May 17 14:34:34 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010403/rk00000004.xml"""),
    ],
)

entry(
    index = 917,
    label = "r00010587",
    reactant1 = 
"""
1    C 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.3,"cm^3/(mol*s)"),
        n = 2,
        Ea = (6276,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00010587/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010587/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010587/rk00000002.xml"""),
    ],
)

entry(
    index = 930,
    label = "r00010849",
    reactant1 = 
"""
1 *3 C 1
""",
    reactant2 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1 *3 O 1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.39058e-06,"cm^3/(mol*s)"),
        n = 3.31,
        Ea = (52547.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Ma, S.", "Liu, R."],
        title = u'Theoretical studies on the reaction path and dynamics of the reaction CH_3+H_2O \u2192 CH_4+OH',
        journal = "Sci. China Ser. B",
        volume = "39",
        pages = """37-44""",
        year = "1996",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00010849/rk00000004.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010849/rk00000004.xml
""",
    history = [
        ("Tue May 17 14:34:41 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010849/rk00000004.xml"""),
    ],
)

entry(
    index = 931,
    label = "r00010849",
    reactant1 = 
"""
1 *1 C 0 {2,S}
2 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 1
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (100,"cm^3/(mol*s)"),
        n = 1.6,
        Ea = (13054.1,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00010849/rk00000005.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010849/rk00000005.xml
""",
    history = [
        ("Tue May 17 14:34:41 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010849/rk00000005.xml"""),
    ],
)

entry(
    index = 987,
    label = "r00011158",
    reactant1 = 
"""
1    C 0 {2,B} {3,B}
2    C 0 {1,B} {4,B}
3    C 0 {1,B} {5,B}
4    C 0 {2,B} {6,B}
5    C 0 {3,B} {6,B}
6 *3 C 1 {4,B} {5,B}
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {3,D} {4,S}
3    C 0 {1,S} {2,D}
4 *2 H 0 {2,S}
""",
    product1 = 
"""
1    C 0 {2,B} {3,B}
2    C 0 {1,B} {4,B}
3    C 0 {1,B} {5,B}
4    C 0 {2,B} {6,B}
5    C 0 {3,B} {6,B}
6 *1 C 0 {4,B} {5,B} {7,S}
7 *2 H 0 {6,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {3,D}
3 *3 C 1 {1,S} {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (0.000594385,"cm^3/(molecule*s)"),
        n = 3.13,
        Ea = (493.694,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Vereecken, L.", "Peeters, J."],
        title = u'Reactions of chemically activated C9H9 species II: The reaction of phenyl radicals with allene and cyclopropene, and of benzyl radicals with acetylene',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "5",
        pages = """2807-2817""",
        year = "2003",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011158/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011158/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:34:45 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011158/rk00000001.xml"""),
        ("Tue May 17 16:45:41 2011","Josh Allen <jwallen@mit.edu>","action","""Fixed a typo in the units of the preexponential factor."""),
    ],
)

entry(
    index = 1000,
    label = "r00011303",
    reactant1 = 
"""
1 *1 C 0 {2,S} {3,S}
2    O 0 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 1 {2,S}
2    O 0 {1,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.44,"cm^3/(mol*s)"),
        n = 2,
        Ea = (-3514.56,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011303/rk00000003.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011303/rk00000003.xml
""",
    history = [
        ("Tue May 17 14:34:46 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011303/rk00000003.xml"""),
    ],
)

entry(
    index = 1005,
    label = "r00011303",
    reactant1 = 
"""
1 *1 C 0 {2,S} {3,S}
2    O 0 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 1 {2,S}
2    O 0 {1,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.44138,"cm^3/(mol*s)"),
        n = 2,
        Ea = (-3517.02,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Li, S.C.", "Williams, F.A."],
        title = u'Experimental and numerical studies of two-stage methanol flames',
        journal = "Symp. Int. Combust. Proc.",
        volume = "26",
        pages = """1017-1024""",
        year = "1996",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011303/rk00000010.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011303/rk00000010.xml
""",
    history = [
        ("Tue May 17 14:34:46 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011303/rk00000010.xml"""),
    ],
)

entry(
    index = 1009,
    label = "r00011339",
    reactant1 = 
"""
1 *1 C 0 {2,D} {3,S}
2    O 0 {1,D}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    product2 = 
"""
1 *3 C 1 {2,D}
2    O 0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.6,"cm^3/(mol*s)"),
        n = 2,
        Ea = (50208,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011339/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011339/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:34:46 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011339/rk00000002.xml"""),
    ],
)

entry(
    index = 1020,
    label = "r00011341",
    reactant1 = 
"""
1 *1 C 0 {2,D} {3,S}
2    O 0 {1,D}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 1 {2,D}
2    O 0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3430,"cm^3/(mol*s)"),
        n = 1.18,
        Ea = (-1870.25,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011341/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011341/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:34:47 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011341/rk00000002.xml"""),
    ],
)

entry(
    index = 1021,
    label = "r00011341",
    reactant1 = 
"""
1 *1 C 0 {2,D} {3,S}
2    O 0 {1,D}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 1 {2,D}
2    O 0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.94,"cm^3/(mol*s)"),
        n = 2.11,
        Ea = (-7058.99,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Xu, S.C.", "Zhu, R.S.", "Lin, M.C."],
        title = u'Ab initio study of the OH+CH(2)Oreaction: The effect of the OHOCH2 complex on the H-abstraction kinetics ',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """322-326""",
        year = "2006",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011341/rk00000003.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011341/rk00000003.xml
""",
    history = [
        ("Tue May 17 14:34:47 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011341/rk00000003.xml"""),
    ],
)

entry(
    index = 1032,
    label = "r00011341",
    reactant1 = 
"""
1 *1 C 0 {2,D} {3,S}
2    O 0 {1,D}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 1 {2,D}
2    O 0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3430,"cm^3/(mol*s)"),
        n = 1.18,
        Ea = (-1870.25,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011341/rk00000022.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011341/rk00000022.xml
""",
    history = [
        ("Tue May 17 14:34:47 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011341/rk00000022.xml"""),
    ],
)

entry(
    index = 1033,
    label = "r00011341",
    reactant1 = 
"""
1 *1 C 0 {2,D} {3,S}
2    O 0 {1,D}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 1 {2,D}
2    O 0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3430,"cm^3/(mol*s)"),
        n = 1.18,
        Ea = (-1870.25,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011341/rk00000025.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011341/rk00000025.xml
""",
    history = [
        ("Tue May 17 14:34:47 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011341/rk00000025.xml"""),
    ],
)

entry(
    index = 1038,
    label = "r00011341",
    reactant1 = 
"""
1 *1 C 0 {2,D} {3,S}
2    O 0 {1,D}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 1 {2,D}
2    O 0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (93.3,"cm^3/(mol*s)"),
        n = 1.85,
        Ea = (3849.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Li, H.Y.", "Pu, M.", "Ji, Y.Q.", "Xu, Z.F.", "Feng, W.L."],
        title = u'Theoretical study on the reaction path and rate constants of the hydrogen atom abstraction reaction of CH_2O with CH_3/OH',
        journal = "Chem. Phys.",
        volume = "307",
        pages = """35-43""",
        year = "2004",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011341/rk00000033.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011341/rk00000033.xml
""",
    history = [
        ("Tue May 17 14:34:47 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011341/rk00000033.xml"""),
    ],
)

entry(
    index = 1040,
    label = "r00011341",
    reactant1 = 
"""
1 *1 C 0 {2,D} {3,S}
2    O 0 {1,D}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 1 {2,D}
2    O 0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (0.00148,"cm^3/(mol*s)"),
        n = 2.98,
        Ea = (-14550.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Xu, S.C.", "Zhu, R.S.", "Lin, M.C."],
        title = u'Ab initio study of the OH+CH(2)Oreaction: The effect of the OHOCH2 complex on the H-abstraction kinetics ',
        journal = "Int. J. Chem. Kinet.",
        volume = "38",
        pages = """322-326""",
        year = "2006",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011341/rk00000035.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011341/rk00000035.xml
""",
    history = [
        ("Tue May 17 14:34:47 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011341/rk00000035.xml"""),
    ],
)

entry(
    index = 1041,
    label = "r00011341",
    reactant1 = 
"""
1 *1 C 0 {2,D} {3,S}
2    O 0 {1,D}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 1 {2,D}
2    O 0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.39e+07,"cm^3/(mol*s)"),
        n = 0,
        Ea = (2527.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Baulch, D. L.", "Bowman, C. T.", "Cobos, C. J.", "Cox, R. A.", "Just, T.", "Kerr, J. A.", "Pilling, M. J.", "Stocker, D.", "Troe, J.", "Tsang, W.", "Walker, R. W.", "Warnatz, J."],
        title = u'Evaluated kinetic data for combustion modeling: supplement II',
        journal = "Journal of Physical and Chemical Reference Data",
        volume = "34",
        pages = """757""",
        year = "2005",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011341/rk00000036.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011341/rk00000036.xml
""",
    history = [
        ("Tue May 17 14:34:47 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011341/rk00000036.xml"""),
    ],
)

entry(
    index = 1047,
    label = "r00011431",
    reactant1 = 
"""
1 *1 C 0 {2,D} {3,S}
2    C 0 {1,D}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,D}
2 *3 C 1 {1,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.6,"cm^3/(mol*s)"),
        n = 2,
        Ea = (10460,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011431/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011431/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:34:47 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011431/rk00000002.xml"""),
    ],
)

entry(
    index = 1060,
    label = "r00011639",
    reactant1 = 
"""
1 *1 C 0 {2,S} {4,S}
2    O 0 {1,S} {3,S}
3    O 0 {2,S}
4 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 1 {2,S}
2    O 0 {1,S} {3,S}
3    O 0 {2,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.08e+06,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1829.18,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Esser, C.", "Frank, P.", "Just, Th.", "Kerr, J.A.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."],
        title = u'Evaluated kinetic data for combustion modelling',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "21",
        pages = """411-429""",
        year = "1992",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011639/rk00000006.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011639/rk00000006.xml
""",
    history = [
        ("Tue May 17 14:34:49 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011639/rk00000006.xml"""),
    ],
)

entry(
    index = 1061,
    label = "r00011639",
    reactant1 = 
"""
1 *1 C 0 {2,S} {4,S}
2    O 0 {1,S} {3,S}
3    O 0 {2,S}
4 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 1 {2,S}
2    O 0 {1,S} {3,S}
3    O 0 {2,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (603000,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1579.75,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Hampson, R.F., Jr.", "Kerr, J.A.", "Rossi, M.J.", "Troe, J."],
        title = u'Evaluated kinetic, photochemical and heterogeneous data for atmospheric chemistry: supplement V, IUPAC subcommittee on gas kinetic data evaluation for atmospheric chemistry',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "26",
        pages = """521-1011""",
        year = "1997",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011639/rk00000007.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011639/rk00000007.xml
""",
    history = [
        ("Tue May 17 14:34:49 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011639/rk00000007.xml"""),
    ],
)

entry(
    index = 1062,
    label = "r00011639",
    reactant1 = 
"""
1 *1 C 0 {2,S} {4,S}
2    O 0 {1,S} {3,S}
3    O 0 {2,S}
4 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 1 {2,S}
2    O 0 {1,S} {3,S}
3    O 0 {2,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (602214,"cm^3/(molecule*s)"),
        n = 0,
        Ea = (-1579.75,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Crowley, J.N.", "Hampson, R.F, Jr.", "Kerr, J.A.", "Rossi, M.J.", "Troe, J."],
        title = u'Summary of Evaluated Kinetic and Photochemical Data for Atmospheric Chemistry',
        journal = "Not in System",
        pages = """1-56""",
        year = "2001",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011639/rk00000008.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011639/rk00000008.xml
""",
    history = [
        ("Tue May 17 14:34:49 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011639/rk00000008.xml"""),
        ("Tue May 17 16:45:41 2011","Josh Allen <jwallen@mit.edu>","action","""Fixed a typo in the units of the preexponential factor."""),
    ],
)

entry(
    index = 1075,
    label = "r00011842",
    reactant1 = 
"""
1 *3 O 1
""",
    reactant2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S}
3 *2 H 0 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+06,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1786.57,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011842/rk00000003.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011842/rk00000003.xml
""",
    history = [
        ("Tue May 17 14:34:50 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011842/rk00000003.xml"""),
    ],
)

entry(
    index = 1076,
    label = "r00011842",
    reactant1 = 
"""
1 *3 O 1
""",
    reactant2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S}
3 *2 H 0 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (123051,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011842/rk00000004.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011842/rk00000004.xml
""",
    history = [
        ("Tue May 17 14:34:50 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011842/rk00000004.xml"""),
    ],
)

entry(
    index = 1101,
    label = "r00011842",
    reactant1 = 
"""
1 *3 O 1
""",
    reactant2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S}
3 *2 H 0 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.7378e+06,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1330.32,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Hong, Zekai", "Cook, Robert D.", "Davidson, David F.", "Hanson, Ronald K."],
        title = u'A Shock Tube Study of OH + H2O2 -> H2O + HO2 and H2O2 + M -> 2OH + M using Laser Absorption of H2O and OH',
        journal = "The Journal of Physical Chemistry A",
        volume = "114",
        pages = """5718-5727""",
        year = "2010",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011842/rk00000044.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011842/rk00000044.xml
""",
    history = [
        ("Tue May 17 14:34:50 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011842/rk00000044.xml"""),
    ],
)

entry(
    index = 1102,
    label = "r00011842",
    reactant1 = 
"""
1 *3 O 1
""",
    reactant2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 0 {1,S}
3 *2 H 0 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.5858e+07,"cm^3/(mol*s)"),
        n = 0,
        Ea = (30431,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Hong, Zekai", "Cook, Robert D.", "Davidson, David F.", "Hanson, Ronald K."],
        title = u'A Shock Tube Study of OH + H2O2 -> H2O + HO2 and H2O2 + M -> 2OH + M using Laser Absorption of H2O and OH',
        journal = "The Journal of Physical Chemistry A",
        volume = "114",
        pages = """5718-5727""",
        year = "2010",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011842/rk00000045.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011842/rk00000045.xml
""",
    history = [
        ("Tue May 17 14:34:50 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011842/rk00000045.xml"""),
    ],
)

entry(
    index = 1108,
    label = "r00011918",
    reactant1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S} {6,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    O 0 {1,S}
6    O 0 {2,S} {7,S}
7 *3 O 1 {6,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S} {4,S} {6,S}
2    C 0 {1,S} {5,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    O 0 {2,S} {7,S}
6    O 0 {1,S}
7 *1 O 0 {5,S} {8,S}
8 *2 H 0 {7,S}
""",
    product2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (33700,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-13718.9,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Boyd, A.A.", "Lesclaux, R.", "Jenkin, M.E.", "Wallington, T.J."],
        title = u'A spectroscopic, kinetic, and product study of the (CH_3)_2C(OH)CH_2O_2 radical self reaction and reaction with HO_2',
        journal = "J. Phys. Chem.",
        volume = "100",
        pages = """6594-6603""",
        year = "1996",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011918/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011918/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:34:51 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011918/rk00000001.xml"""),
    ],
)

entry(
    index = 1120,
    label = "r00013692",
    reactant1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    product2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (130000,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-6819.92,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:35:13 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000002.xml"""),
    ],
)

entry(
    index = 1121,
    label = "r00013692",
    reactant1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    product2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.2e+08,"cm^3/(mol*s)"),
        n = 0,
        Ea = (50208,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000003.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000003.xml
""",
    history = [
        ("Tue May 17 14:35:13 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000003.xml"""),
    ],
)

entry(
    index = 1122,
    label = "r00013692",
    reactant1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    product2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+07,"cm^3/(mol*s)"),
        n = 0,
        Ea = (4182.18,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Lloyd, A.C."],
        title = u'Evaluated and estimated kinetic data for phase reactions of the hydroperoxyl radical',
        journal = "Int. J. Chem. Kinet.",
        volume = "6",
        pages = """169-228""",
        year = "1974",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000006.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000006.xml
""",
    history = [
        ("Tue May 17 14:35:13 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000006.xml"""),
    ],
)

entry(
    index = 1123,
    label = "r00013692",
    reactant1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    product2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (22900,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-10393.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Cox, R.A.", "Burrows, J.P."],
        title = u'Kinetics and Mechanism of the Disproportionation of HO_2 in the Gas Phase',
        journal = "J. Phys. Chem.",
        volume = "83",
        pages = """2560""",
        year = "1979",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000010.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000010.xml
""",
    history = [
        ("Tue May 17 14:35:13 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000010.xml"""),
    ],
)

entry(
    index = 1124,
    label = "r00013692",
    reactant1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    product2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (68700,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-8813.34,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Lii, R.-R.", "Gorse, R.A., Jr.", "Sauer, M.C., Jr.", "Gordon, S."],
        title = u'Negative Activation Energy for the Self-Reaction of HO_2 in the Gas Phase. Dimerization ofHO_2',
        journal = "J. Phys. Chem.",
        volume = "83",
        pages = """1803""",
        year = "1979",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000012.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000012.xml
""",
    history = [
        ("Tue May 17 14:35:13 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000012.xml"""),
    ],
)

entry(
    index = 1125,
    label = "r00013692",
    reactant1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    product2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (53600,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-8813.34,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Lii, R.-R.", "Gorse, R.A., Jr.", "Sauer, M.C., Jr.", "Gordon, S."],
        title = u'Temperature Dependence of the Gas-Phase Self-Reaction of HO_2 in the Presence of NH_3',
        journal = "J. Phys. Chem.",
        volume = "84",
        pages = """813""",
        year = "1980",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000018.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000018.xml
""",
    history = [
        ("Tue May 17 14:35:13 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000018.xml"""),
    ],
)

entry(
    index = 1126,
    label = "r00013692",
    reactant1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    product2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (46300,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-8480.76,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Burrows, J.P.", "Cox, R.a.", "Derwent, R.G."],
        title = u'Modulated Photolysis of the Ozone-Water Vapour System: Kinetics of the Reaction of OH with HO_2',
        journal = "J. Photochem.",
        volume = "16",
        pages = """147""",
        year = "1981",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000019.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000019.xml
""",
    history = [
        ("Tue May 17 14:35:13 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000019.xml"""),
    ],
)

entry(
    index = 1127,
    label = "r00013692",
    reactant1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    product2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (55500,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-8813.34,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Lii, R.-R.", "Sauer, M.C., Jr.", "Gordon, S."],
        title = u'Temperature Dependence of the Gas-Phase Self-Reaction of HO_2 in the Presence of H_2O',
        journal = "J. Phys. Chem.",
        volume = "85",
        pages = """2833""",
        year = "1981",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000020.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000020.xml
""",
    history = [
        ("Tue May 17 14:35:13 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000020.xml"""),
    ],
)

entry(
    index = 1128,
    label = "r00013692",
    reactant1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    product2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (249000,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-5238.12,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Patrick, R.", "Pilling, M.J."],
        title = u'The Temperature Dependence of the HO_2 + HO_2 Reaction',
        journal = "Chem. Phys. Lett.",
        volume = "91",
        pages = """343""",
        year = "1982",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000021.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000021.xml
""",
    history = [
        ("Tue May 17 14:35:13 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000021.xml"""),
    ],
)

entry(
    index = 1129,
    label = "r00013692",
    reactant1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    product2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (145000,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-4656.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Thrush, B.A.", "Tyndall, G.S."],
        title = u'The Rate of Reaction between HO_2 Radicals at Low Pressures',
        journal = "Chem. Phys. Lett.",
        volume = "92",
        pages = """232""",
        year = "1982",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000023.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000023.xml
""",
    history = [
        ("Tue May 17 14:35:13 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000023.xml"""),
    ],
)

entry(
    index = 1130,
    label = "r00013692",
    reactant1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    product2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3770,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-18707.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Mozurkewich, M.", "Benson, S.W."],
        title = u'Self-reaction of HO_2 and DO_2: Negative temperature dependence and pressure effects',
        journal = "Int. J. Chem. Kinet.",
        volume = "17",
        pages = """787""",
        year = "1985",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000028.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000028.xml
""",
    history = [
        ("Tue May 17 14:35:13 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000028.xml"""),
    ],
)

entry(
    index = 1131,
    label = "r00013692",
    reactant1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    product2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+07,"cm^3/(mol*s)"),
        n = 0,
        Ea = (4182.18,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Pitz, W.J.", "Westbrook, C.K."],
        title = u'Chemical kinetics of the high pressure oxidation of n-butane and its relation to engine knock',
        journal = "Combust. Flame",
        volume = "63",
        pages = """113-133""",
        year = "1986",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000030.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000030.xml
""",
    history = [
        ("Tue May 17 14:35:13 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000030.xml"""),
    ],
)

entry(
    index = 1132,
    label = "r00013692",
    reactant1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    product2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (121000,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-4947.11,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Takacs, G.A.", "Howard, C.J."],
        title = u'Temperature dependence of the reaction HO_2 + HO_2 at low pressures',
        journal = "J. Phys. Chem.",
        volume = "90",
        pages = """687""",
        year = "1986",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000031.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000031.xml
""",
    history = [
        ("Tue May 17 14:35:13 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000031.xml"""),
    ],
)

entry(
    index = 1133,
    label = "r00013692",
    reactant1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    product2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5550,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-14134.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Andersson, B.Y.", "Cox, R.A.", "Jenkin, M.E."],
        title = u'The effect of methanol on the self reaction of HO_2 radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "20",
        pages = """283""",
        year = "1988",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000034.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000034.xml
""",
    history = [
        ("Tue May 17 14:35:13 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000034.xml"""),
    ],
)

entry(
    index = 1134,
    label = "r00013692",
    reactant1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    product2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.87e+06,"cm^3/(mol*s)"),
        n = 0,
        Ea = (6443.72,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Esser, C.", "Frank, P.", "Just, Th.", "Kerr, J.A.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."],
        title = u'Evaluated kinetic data for combustion modelling',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "21",
        pages = """411-429""",
        year = "1992",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000038.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000038.xml
""",
    history = [
        ("Tue May 17 14:35:13 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000038.xml"""),
    ],
)

entry(
    index = 1135,
    label = "r00013692",
    reactant1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    product2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (271000,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-4323.53,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Dobis, O.", "Benson, S.W."],
        title = u'Reaction of the ethyl radical with oxygen at millitorr pressures at 243-368 K and a study of the Cl + HO_2, ethyl + HO_2, and HO_2 + HO_2 reactions',
        journal = "J. Am. Chem. Soc.",
        volume = "115",
        pages = """8798-8809""",
        year = "1993",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000039.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000039.xml
""",
    history = [
        ("Tue May 17 14:35:13 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000039.xml"""),
    ],
)

entry(
    index = 1136,
    label = "r00013692",
    reactant1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    product2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.22e+08,"cm^3/(mol*s)"),
        n = 0,
        Ea = (50136.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Frank, P.", "Hayman, G.", "Just, Th.", "Kerr, J.A.", "Murrells, T.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."],
        title = u'Evaluated kinetic data for combusion modelling. Supplement I',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "23",
        pages = """847-1033""",
        year = "1994",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000040.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000040.xml
""",
    history = [
        ("Tue May 17 14:35:13 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000040.xml"""),
    ],
)

entry(
    index = 1137,
    label = "r00013692",
    reactant1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    product2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (169000,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-4938.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Maricq, M.M.", "Szente, J.J."],
        title = u'A kinetic study of the reaction between ethylperoxy radicals and HO_2',
        journal = "J. Phys. Chem.",
        volume = "98",
        pages = """2078-2082""",
        year = "1994",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000041.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000041.xml
""",
    history = [
        ("Tue May 17 14:35:13 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000041.xml"""),
    ],
)

entry(
    index = 1138,
    label = "r00013692",
    reactant1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    product2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (132000,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-4988.68,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Hampson, R.F., Jr.", "Kerr, J.A.", "Rossi, M.J.", "Troe, J."],
        title = u'Evaluated kinetic and photochemical data for atmospheric chemistry: supplement VI. IUPAC subcommittee on gas kinetic data evaluation for atmospheric chemistry',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "26",
        pages = """1329-1499""",
        year = "1997",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000042.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000042.xml
""",
    history = [
        ("Tue May 17 14:35:13 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000042.xml"""),
    ],
)

entry(
    index = 1139,
    label = "r00013692",
    reactant1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    product2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (139000,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-4988.68,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["DeMore, W.B.", "Sander, S.P.", "Golden, D.M.", "Hampson, R.F.", "Kurylo, M.J.", "Howard, C.J.", "Ravishankara, A.R.", "Kolb, C.E.", "Molina, M.J."],
        title = u'Chemical kinetics and photochemical data for use in stratospheric modeling. Evaluation number 12',
        journal = "JPL Publication 97-4",
        pages = """1-266""",
        year = "1997",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000043.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000043.xml
""",
    history = [
        ("Tue May 17 14:35:13 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000043.xml"""),
    ],
)

entry(
    index = 1140,
    label = "r00013692",
    reactant1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    product2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (132487,"cm^3/(molecule*s)"),
        n = 0,
        Ea = (-4988.68,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Crowley, J.N.", "Hampson, R.F, Jr.", "Kerr, J.A.", "Rossi, M.J.", "Troe, J."],
        title = u'Summary of Evaluated Kinetic and Photochemical Data for Atmospheric Chemistry',
        journal = "Not in System",
        pages = """1-56""",
        year = "2001",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000045.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000045.xml
""",
    history = [
        ("Tue May 17 14:35:13 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000045.xml"""),
        ("Tue May 17 16:45:41 2011","Josh Allen <jwallen@mit.edu>","action","""Fixed a typo in the units of the preexponential factor."""),
    ],
)

entry(
    index = 1141,
    label = "r00013692",
    reactant1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    product2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (132487,"cm^3/(molecule*s)"),
        n = 0,
        Ea = (-4988.68,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Crowley, J.N.", "Hampson, R.F.", "Hynes, R.G.", "Jenkin, M.E.", "Rossi, M.J.", "Troe, J."],
        title = u'Evaluated kinetic and photochemical data for atmospheric chemistry: Volume I - gas phase reactions of Ox, HOx, NOx and SOx species',
        journal = "Atmos. Chem. Phys.",
        volume = "4",
        pages = """1461-1738""",
        year = "2004",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000046.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000046.xml
""",
    history = [
        ("Tue May 17 14:35:13 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013692/rk00000046.xml"""),
        ("Tue May 17 16:45:41 2011","Josh Allen <jwallen@mit.edu>","action","""Fixed a typo in the units of the preexponential factor."""),
    ],
)

entry(
    index = 1144,
    label = "r00013765",
    reactant1 = 
"""
1 *1 C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (3.54,"cm^3/(mol*s)"),
        n = 2.12,
        Ea = (3640.08,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00013765/rk00000003.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013765/rk00000003.xml
""",
    history = [
        ("Tue May 17 14:35:13 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013765/rk00000003.xml"""),
    ],
)

entry(
    index = 1145,
    label = "r00013765",
    reactant1 = 
"""
1 *1 C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (4.78e+06,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8563.91,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Clarke, J.S.", "Kroll, J.H.", "Donahue, N.M.", "Anderson, J.G."],
        title = u'Testing frontier orbital control: kinetics of OH with ethane, propane, and cyclopropane from 180 to 360K',
        journal = "J. Phys. Chem. A",
        volume = "102",
        pages = """9847-9857""",
        year = "1998",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00013765/rk00000004.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013765/rk00000004.xml
""",
    history = [
        ("Tue May 17 14:35:13 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013765/rk00000004.xml"""),
    ],
)

entry(
    index = 1180,
    label = "r00013767",
    reactant1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.45e+07,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-2092,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00013767/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013767/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:35:13 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013767/rk00000002.xml"""),
    ],
)

entry(
    index = 1181,
    label = "r00013767",
    reactant1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1 *3 O 1 {2,S}
2    O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+09,"cm^3/(mol*s)"),
        n = 0,
        Ea = (72508.7,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00013767/rk00000003.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013767/rk00000003.xml
""",
    history = [
        ("Tue May 17 14:35:13 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013767/rk00000003.xml"""),
    ],
)

entry(
    index = 1204,
    label = "r00013781",
    reactant1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1 *3 H 1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (216,"cm^3/(mol*s)"),
        n = 1.51,
        Ea = (14351.1,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00013781/rk00000015.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013781/rk00000015.xml
""",
    history = [
        ("Tue May 17 14:35:13 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013781/rk00000015.xml"""),
    ],
)

entry(
    index = 1251,
    label = "r00017220",
    reactant1 = 
"""
1 *3 H 1
""",
    reactant2 = 
"""
1 *1 C 0 {2,D} {3,S}
2    C 0 {1,D} {4,D}
3 *2 H 0 {1,S}
4    O 0 {2,D}
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,D} {3,D}
2 *3 C 1 {1,D}
3    O 0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5e+07,"cm^3/(mol*s)"),
        n = 0,
        Ea = (33472,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00017220/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00017220/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:36:14 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00017220/rk00000001.xml"""),
    ],
)

entry(
    index = 1252,
    label = "r00017282",
    reactant1 = 
"""
1 *3 H 1
""",
    reactant2 = 
"""
1 *1 C 0 {2,S} {3,S}
2    C 0 {1,S} {4,D}
3 *2 H 0 {1,S}
4    O 0 {2,D}
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,D}
2 *3 C 1 {1,S}
3    O 0 {1,D}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2050,"cm^3/(mol*s)"),
        n = 1.16,
        Ea = (10062.5,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00017282/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00017282/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:36:14 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00017282/rk00000001.xml"""),
    ],
)

