#!/usr/bin/env python
# encoding: utf-8

name = "1,3_Insertion_CO2/PrIMe"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 20,
    label = "r00014891",
    reactant1 = 
"""
1 *3 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4    C 0 {1,S} {6,D}
5 *1 C 0 {1,S} {7,S} {8,D}
6    C 0 {4,D}
7 *2 O 0 {5,S} {9,S}
8    O 0 {5,D}
9 *4 H 0 {7,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,D}
2 *2 O 0 {1,D}
3    O 0 {1,D}
""",
    product2 = 
"""
1 *3 C 0 {2,S} {3,S} {4,S} {6,S}
2    C 0 {1,S}
3    C 0 {1,S}
4    C 0 {1,S} {5,D}
5    C 0 {4,D}
6 *4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.03e+11,"s^-1"),
        n = 0,
        Ea = (154649,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Al-Borno, A.", "Bigley, D.B."],
        title = u'Studies in Decarboxylation. Par t 15. The Effects of 3-Substitution on the Rate of Decarboxylation of \u03b2\u03b2\u03c0\u03b2-Unsaturated Acids',
        journal = "J. Chem. Soc. Perkin Trans. 2",
        pages = """15""",
        year = "1982",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00014891/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00014891/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:35:16 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00014891/rk00000002.xml"""),
    ],
)

entry(
    index = 22,
    label = "r00015736",
    reactant1 = 
"""
1  *3 C 0 {3,S} {4,S} {7,S} {9,S}
2     C 0 {5,S} {7,S}
3     C 0 {1,S}
4     C 0 {1,S}
5     C 0 {2,S}
6     C 0 {8,S}
7     C 0 {1,S} {2,S} {8,D}
8     C 0 {6,S} {7,D}
9  *1 C 0 {1,S} {10,S} {11,D}
10 *2 O 0 {9,S} {12,S}
11    O 0 {9,D}
12 *4 H 0 {10,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,D}
2 *2 O 0 {1,D}
3    O 0 {1,D}
""",
    product2 = 
"""
1 *3 C 0 {3,S} {4,S} {7,S} {9,S}
2    C 0 {5,S} {7,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    C 0 {2,S}
6    C 0 {8,S}
7    C 0 {1,S} {2,S} {8,D}
8    C 0 {6,S} {7,D}
9 *4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.07e+11,"s^-1"),
        n = 0,
        Ea = (146335,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Bigley, D.B.", "May, R.W."],
        title = u'Studies in decarboxylation. Part IV. The effect of alkyl substituents on the rate of gas-phase decarboxylation of some \u03b2\u03b3-unsaturated acids',
        journal = "J. Chem. Soc. B",
        pages = """557-559""",
        year = "1967",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00015736/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015736/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:27 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015736/rk00000001.xml"""),
    ],
)

