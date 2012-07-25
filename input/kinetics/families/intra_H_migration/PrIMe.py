#!/usr/bin/env python
# encoding: utf-8

name = "intra_H_migration/PrIMe"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 55,
    label = "r00017124",
    reactant1 = 
"""
1 *4 C 0 {2,B} {4,S} {8,B}
2    C 0 {1,B} {3,B}
3    C 0 {2,B} {5,B}
4 *5 C 0 {1,S} {7,D}
5    C 0 {3,B} {6,B}
6    C 0 {5,B} {8,B}
7 *2 C 0 {4,D} {9,S}
8 *1 C 1 {1,B} {6,B}
9 *3 H 0 {7,S}
""",
    product1 = 
"""
1 *5 C 0 {2,B} {3,B} {7,S}
2    C 0 {1,B} {4,B}
3 *2 C 0 {1,B} {6,B} {9,S}
4    C 0 {2,B} {5,B}
5    C 0 {4,B} {6,B}
6    C 0 {3,B} {5,B}
7 *4 C 0 {1,S} {8,D}
8 *1 C 1 {7,D}
9 *3 H 0 {3,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.57e+09,"s^-1"),
        n = 0.81,
        Ea = (434.048,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Tokmakov, I.V.", "Lin, M.C."],
        title = u'Reaction of phenyl radicals with acetylene: Quantum chemical investigation of the mechanism and master equation analysis of the kinetics',
        journal = "J. Am. Chem. Soc.",
        volume = "125",
        pages = """11397-11408""",
        year = "2003",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00017124/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00017124/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:36:12 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00017124/rk00000001.xml"""),
    ],
)

entry(
    index = 56,
    label = "r00017124",
    reactant1 = 
"""
1 *5 C 0 {2,B} {3,B} {7,S}
2 *2 C 0 {1,B} {5,B} {9,S}
3    C 0 {1,B} {6,B}
4    C 0 {5,B} {6,B}
5    C 0 {2,B} {4,B}
6    C 0 {3,B} {4,B}
7 *4 C 0 {1,S} {8,D}
8 *1 C 1 {7,D}
9 *3 H 0 {2,S}
""",
    product1 = 
"""
1 *4 C 0 {2,B} {5,S} {8,B}
2    C 0 {1,B} {3,B}
3    C 0 {2,B} {4,B}
4    C 0 {3,B} {6,B}
5 *5 C 0 {1,S} {7,D}
6    C 0 {4,B} {8,B}
7 *2 C 0 {5,D} {9,S}
8 *1 C 1 {1,B} {6,B}
9 *3 H 0 {7,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.04e+10,"s^-1"),
        n = 0.7,
        Ea = (454.371,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Tokmakov, I.V.", "Lin, M.C."],
        title = u'Reaction of phenyl radicals with acetylene: Quantum chemical investigation of the mechanism and master equation analysis of the kinetics',
        journal = "J. Am. Chem. Soc.",
        volume = "125",
        pages = """11397-11408""",
        year = "2003",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00017124/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00017124/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:36:12 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00017124/rk00000002.xml"""),
    ],
)

