#!/usr/bin/env python
# encoding: utf-8

name = "Disproportionation/PrIMe"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 2,
    label = "r00001361",
    reactant1 = 
"""
1 *3 C 1 {2,S}
2 *2 O 0 {1,S} {3,S}
3 *4 H 0 {2,S}
""",
    reactant2 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 0 {2,D}
2 *2 O 0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.8e+07,"cm^3/(mol*s)"),
        n = 0,
        Ea = (3765.6,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00001361/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00001361/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:33:30 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00001361/rk00000002.xml"""),
    ],
)

entry(
    index = 9,
    label = "r00002190",
    reactant1 = 
"""
1 *1 H 1
""",
    reactant2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *3 C 1 {1,S}
3 *4 H 0 {1,S}
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *4 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 0 {2,D}
2 *2 C 0 {1,D}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2e+06,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00002190/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00002190/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:33:34 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00002190/rk00000002.xml"""),
    ],
)

entry(
    index = 49,
    label = "r00010580",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *3 O 1 {1,S}
3 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1 *1 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *4 H 0 {1,S}
""",
    product2 = 
"""
1 *2 C 0 {2,D}
2 *3 O 0 {1,D}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (5e+06,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00010580/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010580/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010580/rk00000002.xml"""),
    ],
)

entry(
    index = 70,
    label = "r00010588",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *3 O 1 {1,S}
3 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product2 = 
"""
1 *2 C 0 {2,D}
2 *3 O 0 {1,D}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (4.28e-19,"cm^3/(mol*s)"),
        n = 7.6,
        Ea = (-14769.5,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00010588/rk00000038.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010588/rk00000038.xml
""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010588/rk00000038.xml"""),
    ],
)

entry(
    index = 71,
    label = "r00010601",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *3 O 1 {1,S}
3 *4 H 0 {1,S}
""",
    reactant2 = 
"""
1 *1 H 1
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *4 H 0 {1,S}
""",
    product2 = 
"""
1 *2 C 0 {2,D}
2 *3 O 0 {1,D}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2e+07,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00010601/rk00000007.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010601/rk00000007.xml
""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010601/rk00000007.xml"""),
    ],
)

entry(
    index = 83,
    label = "r00011296",
    reactant1 = 
"""
1 *3 C 1 {2,S}
2 *2 O 0 {1,S} {3,S}
3 *4 H 0 {2,S}
""",
    reactant2 = 
"""
1 *1 O 1
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *4 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 0 {2,D}
2 *2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+06,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011296/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011296/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:34:46 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011296/rk00000002.xml"""),
    ],
)

entry(
    index = 84,
    label = "r00011312",
    reactant1 = 
"""
1 *3 C 1 {2,S}
2 *2 O 0 {1,S} {3,S}
3 *4 H 0 {2,S}
""",
    reactant2 = 
"""
1 *1 H 1
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *4 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 0 {2,D}
2 *2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+07,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011312/rk00000004.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011312/rk00000004.xml
""",
    history = [
        ("Tue May 17 14:34:46 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011312/rk00000004.xml"""),
    ],
)

entry(
    index = 104,
    label = "r00013871",
    reactant1 = 
"""
1 *2 C 0 {2,D}
2 *3 C 0 {1,D}
""",
    reactant2 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *4 H 0 {1,S}
""",
    product1 = 
"""
1 *1 O 1 {2,S}
2    O 1 {1,S}
""",
    product2 = 
"""
1 *2 C 0 {2,S} {3,S}
2 *3 C 1 {1,S}
3 *4 H 0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.67e-20,"cm^3/(mol*s)"),
        n = -0.772,
        Ea = (38.4976,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Clifford, E.P.", "Farrell, J.T.", "DeSain, J.D.", "Taatjes, C.A."],
        title = u'Infrared Frequency-Modulation Probing of Product Formation in Alkyl + O_2 Reactions: I. The Reaction of C_2H_5 with O_2 between 295 and 698 K',
        journal = "J. Phys. Chem. A",
        volume = "104",
        pages = """11549-11560""",
        year = "2000",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00013871/rk00000032.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013871/rk00000032.xml
""",
    history = [
        ("Tue May 17 14:35:14 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013871/rk00000032.xml"""),
    ],
)

entry(
    index = 116,
    label = "r00017290",
    reactant1 = 
"""
1 *1 H 1
""",
    reactant2 = 
"""
1    C 0 {2,D}
2 *2 C 0 {1,D} {3,S} {4,S}
3 *3 O 1 {2,S}
4 *4 H 0 {2,S}
""",
    product1 = 
"""
1 *4 H 0 {2,S}
2 *1 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,D}
2 *2 C 0 {1,D} {3,D}
3 *3 O 0 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.1e+07,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00017290/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00017290/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:36:14 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00017290/rk00000001.xml"""),
    ],
)

