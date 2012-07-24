#!/usr/bin/env python
# encoding: utf-8

name = "Diels_alder_addition/PrIMe"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 60,
    label = "r00016478",
    reactant1 = 
"""
1 *1 C 0 {2,D} {3,S}
2 *2 C 0 {1,D}
3    C 0 {1,S} {4,D}
4    O 0 {3,D}
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3 *3 C 0 {1,S} {5,D}
4 *6 C 0 {2,S} {6,D}
5 *4 C 0 {3,D} {6,S}
6 *5 C 0 {4,D} {5,S}
""",
    product1 = 
"""
1  *3 C 0 {2,S} {5,S} {7,S}
2  *1 C 0 {1,S} {4,S} {9,S}
3  *6 C 0 {4,S} {6,S} {8,S}
4  *2 C 0 {2,S} {3,S}
5     C 0 {1,S} {6,S}
6     C 0 {3,S} {5,S}
7  *4 C 0 {1,S} {8,D}
8  *5 C 0 {3,S} {7,D}
9     C 0 {2,S} {10,D}
10    O 0 {9,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (603,"cm^3/(mol*s)"),
        n = 0,
        Ea = (87302,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Van Mele, B.", "Tybaert, C.", "Huybrechts, G."],
        title = u'Kinetics, mechanism, and stereochemistry of Diels-Alder reactions of carbonyl-substituted ethenes with cyclohexa-1,3-diene in the gas phase',
        journal = "Int. J. Chem. Kinet.",
        volume = "19",
        pages = """1063""",
        year = "1987",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016478/rk00000003.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016478/rk00000003.xml
""",
    history = [
        ("Tue May 17 14:35:47 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016478/rk00000003.xml"""),
    ],
)

