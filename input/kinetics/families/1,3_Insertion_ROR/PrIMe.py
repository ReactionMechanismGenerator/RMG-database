#!/usr/bin/env python
# encoding: utf-8

name = "1,3_Insertion_ROR/PrIMe"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 24,
    label = "r00007088",
    reactant1 = 
"""
1    C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 C 0 {1,S} {6,S} {7,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    C 0 {1,S}
6 *1 C 0 {2,S} {8,S}
7 *4 O 0 {2,S}
8 *3 H 0 {6,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4    C 0 {1,S}
5 *2 C 0 {1,S} {6,D}
6 *1 C 0 {5,D}
""",
    product2 = 
"""
1 *4 O 0 {2,S}
2 *3 H 0 {1,S}
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (1e+14,"s^-1"),
        n = (0.0,""),
        Ea = (284355.0,"J/mol"),
        T0 = (1.0,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Thermal Stability of Alcohols',
        journal = "Int. J. Chem. Kinet.",
        volume = "8",
        pages = """173""",
        year = "1976",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00007088/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007088/rk00000001.xml
""",
    history = [('Tue May 17 14:34:02 2011', 'Josh Allen <jwallen@mit.edu>', 'action', 'Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00007088/rk00000001.xml')],
)
