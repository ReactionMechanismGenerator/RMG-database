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

