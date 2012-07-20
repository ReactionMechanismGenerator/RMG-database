#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_Endocyclic/PrIMe"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 10,
    label = "r00017190",
    reactant1 = 
"""
1 *3 C 0 {2,S} {4,S}
2 *1 C 0 {1,S} {3,B} {5,B}
3 *4 C 0 {2,B} {4,S} {6,B}
4 *2 C 1 {1,S} {3,S}
5    C 0 {2,B} {8,B}
6    C 0 {3,B} {7,B}
7    C 0 {6,B} {8,B}
8    C 0 {5,B} {7,B}
""",
    product1 = 
"""
1 *4 C 0 {2,B} {4,S} {8,B}
2    C 0 {1,B} {3,B}
3    C 0 {2,B} {5,B}
4 *2 C 0 {1,S} {7,D}
5    C 0 {3,B} {6,B}
6    C 0 {5,B} {8,B}
7 *3 C 0 {4,D}
8 *1 C 1 {1,B} {6,B}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.91e+12,"s^-1"),
        n = 0.26,
        Ea = (624.223,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Tokmakov, I.V.", "Lin, M.C."],
        title = u'Reaction of phenyl radicals with acetylene: Quantum chemical investigation of the mechanism and master equation analysis of the kinetics',
        journal = "J. Am. Chem. Soc.",
        volume = "125",
        pages = """11397-11408""",
        year = "2003",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00017190/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00017190/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:36:12 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00017190/rk00000001.xml"""),
    ],
)

