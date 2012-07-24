#!/usr/bin/env python
# encoding: utf-8

name = "2+2_cycloaddition_Cd/PrIMe"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 56,
    label = "r00016232",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S}
2 *4 C 0 {1,S} {5,S} {6,S}
3 *1 C 0 {1,S} {6,S}
4    C 0 {1,S}
5    C 0 {2,S}
6 *3 O 0 {2,S} {3,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,D}
3 *1 C 0 {2,D}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *4 C 0 {1,S} {3,D}
3 *3 O 0 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.13e+15,"s^-1"),
        n = 0,
        Ea = (270220,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Holbrook, K.A.", "Scott, R.A."],
        title = u'Gas-phase Unimolecular Pyrolyses of cis- and trans-2,3-Dimethyloxetan',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "70",
        pages = """43""",
        year = "1974",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016232/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016232/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:40 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016232/rk00000001.xml"""),
    ],
)

entry(
    index = 58,
    label = "r00016298",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S}
2 *4 C 0 {1,S} {5,S} {6,S}
3 *1 C 0 {1,S} {6,S}
4    C 0 {1,S}
5    C 0 {2,S}
6 *3 O 0 {2,S} {3,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,D}
3 *1 C 0 {2,D}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *4 C 0 {1,S} {3,D}
3 *3 O 0 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.01e+15,"s^-1"),
        n = 0,
        Ea = (264400,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Holbrook, K.A.", "Scott, R.A."],
        title = u'Gas-phase Unimolecular Pyrolyses of cis- and trans-2,3-Dimethyloxetan',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "70",
        pages = """43""",
        year = "1974",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016298/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016298/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:42 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016298/rk00000001.xml"""),
    ],
)

entry(
    index = 60,
    label = "r00016300",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S} {5,S} {6,S}
2 *4 C 0 {1,S} {4,S} {7,S}
3 *1 C 0 {1,S} {4,S}
4 *3 C 0 {2,S} {3,S}
5    C 0 {1,S}
6    C 0 {1,S}
7    C 0 {2,S}
""",
    product1 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *2 C 0 {1,S} {2,S} {4,D}
4 *1 C 0 {3,D}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *4 C 0 {1,S} {3,D}
3 *3 C 0 {2,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (5.62e+15,"s^-1"),
        n = 0,
        Ea = (251929,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Cocks, A.T.", "Frey, H.M."],
        title = u'The Thermal Unimolecular Decomposition of 1,1,2-Trimethylcyclobutane',
        journal = "J. Phys. Chem.",
        volume = "75",
        pages = """1437""",
        year = "1971",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016300/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016300/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:42 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016300/rk00000001.xml"""),
    ],
)

entry(
    index = 62,
    label = "r00016567",
    reactant1 = 
"""
1 *2 C 0 {2,S} {4,S} {5,S} {8,S}
2 *1 C 0 {1,S} {3,S} {6,S}
3 *3 C 0 {2,S} {7,S} {8,S}
4    C 0 {1,S}
5    C 0 {1,S}
6    C 0 {2,S}
7    C 0 {3,S}
8 *4 O 0 {1,S} {3,S}
""",
    product1 = 
"""
1    C 0 {4,S}
2    C 0 {4,S}
3    C 0 {5,S}
4 *2 C 0 {1,S} {2,S} {5,D}
5 *1 C 0 {3,S} {4,D}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 0 {1,S} {3,D}
3 *4 O 0 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e+14,"s^-1"),
        n = 0,
        Ea = (236962,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Hammonds, P.", "Holbrook, K.A.", "Carless, H.A.J."],
        title = u'Thermolyses of cis- and trans-2,2,3,4-tetramethyloxetane',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "80",
        pages = """691""",
        year = "1984",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016567/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016567/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:49 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016567/rk00000001.xml"""),
    ],
)

entry(
    index = 63,
    label = "r00016568",
    reactant1 = 
"""
1 *2 C 0 {2,S} {4,S} {5,S} {8,S}
2 *1 C 0 {1,S} {3,S} {6,S}
3 *3 C 0 {2,S} {7,S} {8,S}
4    C 0 {1,S}
5    C 0 {1,S}
6    C 0 {2,S}
7    C 0 {3,S}
8 *4 O 0 {1,S} {3,S}
""",
    product1 = 
"""
1    C 0 {4,S}
2    C 0 {4,S}
3    C 0 {5,S}
4 *2 C 0 {1,S} {2,S} {5,D}
5 *1 C 0 {3,S} {4,D}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 0 {1,S} {3,D}
3 *4 O 0 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.94e+13,"s^-1"),
        n = 0,
        Ea = (228648,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Hammonds, P.", "Holbrook, K.A.", "Carless, H.A.J."],
        title = u'Thermolyses of cis- and trans-2,2,3,4-tetramethyloxetane',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "80",
        pages = """691""",
        year = "1984",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016568/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016568/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:50 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016568/rk00000001.xml"""),
    ],
)

entry(
    index = 64,
    label = "r00016669",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S} {6,S}
2 *1 C 0 {1,S} {4,S} {8,S}
3 *4 C 0 {1,S} {5,S} {8,S}
4    C 0 {2,S}
5    C 0 {3,S}
6    C 0 {1,S} {7,D}
7    C 0 {6,D}
8 *3 O 0 {2,S} {3,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,D}
3 *2 C 0 {2,D} {4,S}
4    C 0 {3,S} {5,D}
5    C 0 {4,D}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *4 C 0 {1,S} {3,D}
3 *3 O 0 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.63e+13,"s^-1"),
        n = 0,
        Ea = (200379,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Carless, H.A.J.", "Maitra, A.K.", "Pottinger, R.", "Frey, H.M."],
        title = u'Thermal decomposition of cis-2,4-dimethyl-trans-3-vinyloxetan',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "76",
        pages = """1849""",
        year = "1980",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016669/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016669/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:52 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016669/rk00000001.xml"""),
    ],
)

