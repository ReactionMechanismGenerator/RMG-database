#!/usr/bin/env python
# encoding: utf-8

name = "R_Recombination/PrIMe"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 539,
    label = "r00011821",
    reactant1 = 
"""
1 * O 1 {2,S}
2   O 1 {1,S}
""",
    reactant2 = 
"""
1 * H 1
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *2 H 0 {1,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (4.34e+13,"cm^3/(mol*s)"),
        n = -1.4,
        Ea = (0,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Davis, S.G.", "Joshi, A.V.", "Wang, H.", "Egolfopoulos, F."],
        title = u'An optimized kinetic model of H2/CO Combustion',
        journal = "Proc. Combust. Inst.",
        volume = "30",
        pages = """1283-1292""",
        year = "2005",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011821/rk00000026.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011821/rk00000026.xml
""",
    history = [
        ("Tue May 17 14:34:50 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011821/rk00000026.xml"""),
    ],
)

entry(
    index = 540,
    label = "r00011821",
    reactant1 = 
"""
1 * O 1 {2,S}
2   O 1 {1,S}
""",
    reactant2 = 
"""
1 * H 1
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *2 H 0 {1,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.07e+13,"cm^3/(mol*s)"),
        n = -1.4,
        Ea = (0,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Davis, S.G.", "Joshi, A.V.", "Wang, H.", "Egolfopoulos, F."],
        title = u'An optimized kinetic model of H2/CO Combustion',
        journal = "Proc. Combust. Inst.",
        volume = "30",
        pages = """1283-1292""",
        year = "2005",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011821/rk00000027.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011821/rk00000027.xml
""",
    history = [
        ("Tue May 17 14:34:50 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011821/rk00000027.xml"""),
    ],
)

entry(
    index = 541,
    label = "r00011821",
    reactant1 = 
"""
1 * O 1 {2,S}
2   O 1 {1,S}
""",
    reactant2 = 
"""
1 * H 1
""",
    product1 = 
"""
1 *1 O 0 {2,S} {3,S}
2    O 1 {1,S}
3 *2 H 0 {1,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (6.95e+14,"cm^3/(mol*s)"),
        n = -1.4,
        Ea = (0,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Davis, S.G.", "Joshi, A.V.", "Wang, H.", "Egolfopoulos, F."],
        title = u'An optimized kinetic model of H2/CO Combustion',
        journal = "Proc. Combust. Inst.",
        volume = "30",
        pages = """1283-1292""",
        year = "2005",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011821/rk00000028.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011821/rk00000028.xml
""",
    history = [
        ("Tue May 17 14:34:50 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011821/rk00000028.xml"""),
    ],
)

entry(
    index = 584,
    label = "r00014912",
    reactant1 = 
"""
1     C 0 {3,S} {5,S} {6,S} {11,S}
2     C 0 {4,S} {7,S} {8,S} {12,S}
3     C 0 {1,S} {9,S}
4     C 0 {2,S} {10,S}
5     C 0 {1,S}
6     C 0 {1,S}
7     C 0 {2,S}
8     C 0 {2,S}
9     C 0 {3,S}
10    C 0 {4,S}
11 *1 O 0 {1,S} {12,S}
12 *2 O 0 {2,S} {11,S}
""",
    product1 = 
"""
1   C 0 {2,S} {3,S} {4,S} {6,S}
2   C 0 {1,S} {5,S}
3   C 0 {1,S}
4   C 0 {1,S}
5   C 0 {2,S}
6 * O 1 {1,S}
""",
    product2 = 
"""
1   C 0 {2,S} {3,S} {4,S} {6,S}
2   C 0 {1,S} {5,S}
3   C 0 {1,S}
4   C 0 {1,S}
5   C 0 {2,S}
6 * O 1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.31e+15,"s^-1"),
        n = 0,
        Ea = (152155,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Perona, M.J.", "Golden, D.M."],
        title = u'Very Low-Pressure Pyrolysis. VIII. The Decomposition of Di-t-Amyl Peroxide',
        journal = "Int. J. Chem. Kinet.",
        volume = "5",
        pages = """55""",
        year = "1973",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00014912/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00014912/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:17 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00014912/rk00000001.xml"""),
    ],
)

