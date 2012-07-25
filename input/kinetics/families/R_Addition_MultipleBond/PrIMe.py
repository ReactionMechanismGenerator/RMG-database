#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_MultipleBond/PrIMe"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 105,
    label = "r00010238",
    reactant1 = 
"""
1 *1 C 0 {2,D}
2 *2 C 0 {1,D}
""",
    reactant2 = 
"""
1 *3 H 1
""",
    product1 = 
"""
1 *1 C 0 {2,S} {3,S}
2 *2 C 1 {1,S}
3 *3 H 0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (540000,"cm^3/(mol*s)"),
        n = 0.454,
        Ea = (7614.88,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00010238/rk00000040.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010238/rk00000040.xml
""",
    history = [
        ("Tue May 17 14:34:34 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010238/rk00000040.xml"""),
    ],
)

entry(
    index = 143,
    label = "r00010564",
    reactant1 = 
"""
1 *1 C 0 {2,D}
2 *2 O 0 {1,D}
""",
    reactant2 = 
"""
1 *3 H 1
""",
    product1 = 
"""
1 *1 C 0 {2,S} {3,S}
2 *2 O 1 {1,S}
3 *3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (540000,"cm^3/(mol*s)"),
        n = 0.454,
        Ea = (10878.4,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00010564/rk00000030.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010564/rk00000030.xml
""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010564/rk00000030.xml"""),
    ],
)

entry(
    index = 148,
    label = "r00010632",
    reactant1 = 
"""
1 *3 C 0 {2,S}
2 *1 C 0 {1,S} {3,S}
3 *2 O 1 {2,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D}
2 *2 O 0 {1,D}
""",
    product2 = 
"""
1 *3 C 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.98e+13,"s^-1"),
        n = 0,
        Ea = (83976.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Choo, K.Y.", "Benson, S.W."],
        title = u'Arrhenius Parameters for the Alkoxy Radical Decomposition Reactions',
        journal = "Int. J. Chem. Kinet.",
        volume = "13",
        pages = """833""",
        year = "1981",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00010632/rk00000005.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010632/rk00000005.xml
""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010632/rk00000005.xml"""),
    ],
)

entry(
    index = 149,
    label = "r00010632",
    reactant1 = 
"""
1 *3 C 0 {2,S}
2 *1 C 0 {1,S} {3,S}
3 *2 O 1 {2,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D}
2 *2 O 0 {1,D}
""",
    product2 = 
"""
1 *3 C 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+15,"s^-1"),
        n = 0,
        Ea = (90627.7,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Heicklen, J."],
        title = u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals',
        journal = "Adv. Photochem.",
        volume = "14",
        pages = """177""",
        year = "1988",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00010632/rk00000006.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010632/rk00000006.xml
""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010632/rk00000006.xml"""),
    ],
)

entry(
    index = 150,
    label = "r00010632",
    reactant1 = 
"""
1 *3 C 0 {2,S}
2 *1 C 0 {1,S} {3,S}
3 *2 O 1 {2,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D}
2 *2 O 0 {1,D}
""",
    product2 = 
"""
1 *3 C 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+13,"s^-1"),
        n = 0,
        Ea = (89796.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Esser, C.", "Frank, P.", "Just, Th.", "Kerr, J.A.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."],
        title = u'Evaluated kinetic data for combustion modelling',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "21",
        pages = """411-429""",
        year = "1992",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00010632/rk00000007.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010632/rk00000007.xml
""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010632/rk00000007.xml"""),
    ],
)

entry(
    index = 151,
    label = "r00010632",
    reactant1 = 
"""
1 *3 C 0 {2,S}
2 *1 C 0 {1,S} {3,S}
3 *2 O 1 {2,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D}
2 *2 O 0 {1,D}
""",
    product2 = 
"""
1 *3 C 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.98e+13,"s^-1"),
        n = 0,
        Ea = (70400,"kJ/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."],
        title = u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds',
        journal = "Can. J. Chem.",
        volume = "81",
        pages = """431-442""",
        year = "2003",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00010632/rk00000010.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010632/rk00000010.xml
""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010632/rk00000010.xml"""),
        ("Fri Jun  3 17:09:42 2011","Josh Allen <jwallen@mit.edu>","action","""Fixed incorrect value of activation energy."""),
    ],
)

entry(
    index = 156,
    label = "r00010633",
    reactant1 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,S} {4,S}
3 *2 O 1 {2,S}
4 *3 H 0 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,D}
3 *2 O 0 {2,D}
""",
    product2 = 
"""
1 *3 H 1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.46e+13,"s^-1"),
        n = 0,
        Ea = (87600,"kJ/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."],
        title = u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds',
        journal = "Can. J. Chem.",
        volume = "81",
        pages = """431-442""",
        year = "2003",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00010633/rk00000006.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010633/rk00000006.xml
""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010633/rk00000006.xml"""),
        ("Fri Jun  3 17:09:42 2011","Josh Allen <jwallen@mit.edu>","action","""Fixed incorrect value of activation energy."""),
    ],
)

entry(
    index = 158,
    label = "r00010737",
    reactant1 = 
"""
1 *3 C 0 {2,S} {5,S}
2    C 0 {1,S}
3    C 0 {4,S}
4 *2 C 1 {3,S} {5,S}
5 *1 O 0 {1,S} {4,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,D}
3 *1 O 0 {2,D}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+13,"s^-1"),
        n = 0,
        Ea = (73250.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["East, R.L.", "Phillips, L."],
        title = u'Pressure-dependence of the gas-phase pyrolysis of the s-butoxyl radical at 150-190',
        journal = "J. Chem. Soc. A",
        pages = """1939""",
        year = "1967",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00010737/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010737/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:34:40 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010737/rk00000001.xml"""),
    ],
)

entry(
    index = 159,
    label = "r00010737",
    reactant1 = 
"""
1 *3 C 0 {2,S} {5,S}
2    C 0 {1,S}
3    C 0 {4,S}
4 *2 C 1 {3,S} {5,S}
5 *1 O 0 {1,S} {4,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,D}
3 *1 O 0 {2,D}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.01e+09,"s^-1"),
        n = 0,
        Ea = (66931.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Hohlein, G.", "Freeman, G.R."],
        title = u'Radiation-sensitized pyrolysis of diethyl ether. Free-radical reaction rate parameters',
        journal = "J. Am. Chem. Soc.",
        volume = "92",
        pages = """6118""",
        year = "1970",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00010737/rk00000003.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010737/rk00000003.xml
""",
    history = [
        ("Tue May 17 14:34:40 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010737/rk00000003.xml"""),
    ],
)

entry(
    index = 164,
    label = "r00011106",
    reactant1 = 
"""
1 *1 C 0 {2,S} {4,S}
2 *3 C 0 {1,S}
3    C 0 {4,S}
4 *2 C 1 {1,S} {3,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,D}
3 *1 C 0 {2,D}
""",
    product2 = 
"""
1 *3 C 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.5e+11,"s^-1"),
        n = 0,
        Ea = (100605,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Gruver, J.T.", "Calvert, J.C."],
        title = u'The vapor phase photolysis of 2-methylbutanal at wave length 3130 A',
        journal = "J. Am. Chem. Soc.",
        volume = "78",
        pages = """5208""",
        year = "1956",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011106/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011106/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:34:43 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011106/rk00000001.xml"""),
    ],
)

entry(
    index = 177,
    label = "r00011107",
    reactant1 = 
"""
1 *1 C 0 {2,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {4,S}
4 *2 C 1 {1,S} {3,S}
5 *3 H 0 {1,S}
""",
    product1 = 
"""
1    C 0 {3,S}
2    C 0 {4,S}
3 *2 C 0 {1,S} {4,D}
4 *1 C 0 {2,S} {3,D}
""",
    product2 = 
"""
1 *3 H 1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.17e+12,"s^-1"),
        n = 0,
        Ea = (145503,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'The stability of alkyl radicals',
        journal = "J. Am. Chem. Soc.",
        volume = "107",
        pages = """2872""",
        year = "1985",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011107/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011107/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:34:43 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011107/rk00000001.xml"""),
    ],
)

entry(
    index = 178,
    label = "r00011107",
    reactant1 = 
"""
1    C 0 {3,S}
2    C 0 {4,S}
3 *1 C 0 {1,S} {4,D}
4 *2 C 0 {2,S} {3,D}
""",
    reactant2 = 
"""
1 *3 H 1
""",
    product1 = 
"""
1 *1 C 0 {2,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {4,S}
4 *2 C 1 {1,S} {3,S}
5 *3 H 0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.61e+07,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8023.47,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Kyogoku, T.", "Watanabe, T.", "Tsunashima, S.", "Sato, S."],
        title = u'Arrhenius parameters for the reactions of hydrogen and deuterium atoms with four butenes',
        journal = "Bull. Chem. Soc. Jpn.",
        volume = "56",
        pages = """19""",
        year = "1983",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011107/rk00000007.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011107/rk00000007.xml
""",
    history = [
        ("Tue May 17 14:34:43 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011107/rk00000007.xml"""),
    ],
)

entry(
    index = 179,
    label = "r00011108",
    reactant1 = 
"""
1 *1 C 0 {2,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {4,S}
4 *2 C 1 {1,S} {3,S}
5 *3 H 0 {1,S}
""",
    product1 = 
"""
1    C 0 {3,S}
2    C 0 {4,S}
3 *2 C 0 {1,S} {4,D}
4 *1 C 0 {2,S} {3,D}
""",
    product2 = 
"""
1 *3 H 1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.57e+12,"s^-1"),
        n = 0,
        Ea = (142177,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'The stability of alkyl radicals',
        journal = "J. Am. Chem. Soc.",
        volume = "107",
        pages = """2872""",
        year = "1985",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011108/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011108/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:34:43 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011108/rk00000001.xml"""),
    ],
)

entry(
    index = 180,
    label = "r00011108",
    reactant1 = 
"""
1    C 0 {3,S}
2    C 0 {4,S}
3 *1 C 0 {1,S} {4,D}
4 *2 C 0 {2,S} {3,D}
""",
    reactant2 = 
"""
1 *3 H 1
""",
    product1 = 
"""
1 *1 C 0 {2,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {4,S}
4 *2 C 1 {1,S} {3,S}
5 *3 H 0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.08e+07,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8647.05,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Harris, G.W.", "Pitts, J.N., Jr."],
        title = u'Absolute Rate Constants and Temperature Dependences for the Gas Phase Reactions of H Atoms with Propene and the Butenes in the Temperature Range 298 to 445 K',
        journal = "J. Chem. Phys.",
        volume = "77",
        pages = """3994""",
        year = "1982",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011108/rk00000013.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011108/rk00000013.xml
""",
    history = [
        ("Tue May 17 14:34:43 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011108/rk00000013.xml"""),
    ],
)

entry(
    index = 181,
    label = "r00011108",
    reactant1 = 
"""
1    C 0 {3,S}
2    C 0 {4,S}
3 *1 C 0 {1,S} {4,D}
4 *2 C 0 {2,S} {3,D}
""",
    reactant2 = 
"""
1 *3 H 1
""",
    product1 = 
"""
1 *1 C 0 {2,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {4,S}
4 *2 C 1 {1,S} {3,S}
5 *3 H 0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.39e+07,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8813.34,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Kyogoku, T.", "Watanabe, T.", "Tsunashima, S.", "Sato, S."],
        title = u'Arrhenius parameters for the reactions of hydrogen and deuterium atoms with four butenes',
        journal = "Bull. Chem. Soc. Jpn.",
        volume = "56",
        pages = """19""",
        year = "1983",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011108/rk00000014.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011108/rk00000014.xml
""",
    history = [
        ("Tue May 17 14:34:43 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011108/rk00000014.xml"""),
    ],
)

entry(
    index = 182,
    label = "r00011148",
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
1 *2 C 0 {2,S} {3,D}
2    C 0 {1,S} {4,D}
3 *1 C 0 {1,D}
4    C 0 {2,D}
""",
    product1 = 
"""
1  *1 C 0 {2,S} {3,S}
2  *3 C 0 {1,S} {4,B} {5,B}
3  *2 C 1 {1,S} {9,S}
4     C 0 {2,B} {7,B}
5     C 0 {2,B} {8,B}
6     C 0 {7,B} {8,B}
7     C 0 {4,B} {6,B}
8     C 0 {5,B} {6,B}
9     C 0 {3,S} {10,D}
10    C 0 {9,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.01e+40,"cm^3/(mol*s)"),
        n = -10.2,
        Ea = (69069.5,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Fascella, S.", "Cavallotti, C.", "Rota, R.", "Carra, S."],
        title = u'Quantum chemistry investigation of key reactions involved in the formation of naphthalene and indene',
        journal = "J. Phys. Chem. A",
        volume = "108",
        pages = """3829-3843""",
        year = "2004",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011148/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011148/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:34:44 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011148/rk00000001.xml"""),
        ("Fri Jun  3 16:02:18 2011","Josh Allen <jwallen@mit.edu>","action","""Fixed incorrect value for activation energy."""),
    ],
)

entry(
    index = 184,
    label = "r00011148",
    reactant1 = 
"""
1  *1 C 0 {2,S} {3,S}
2  *3 C 0 {1,S} {4,B} {5,B}
3  *2 C 1 {1,S} {9,S}
4     C 0 {2,B} {7,B}
5     C 0 {2,B} {8,B}
6     C 0 {7,B} {8,B}
7     C 0 {4,B} {6,B}
8     C 0 {5,B} {6,B}
9     C 0 {3,S} {10,D}
10    C 0 {9,D}
""",
    product1 = 
"""
1    C 0 {2,S} {3,D}
2 *2 C 0 {1,S} {4,D}
3    C 0 {1,D}
4 *1 C 0 {2,D}
""",
    product2 = 
"""
1    C 0 {2,B} {3,B}
2    C 0 {1,B} {4,B}
3    C 0 {1,B} {5,B}
4    C 0 {2,B} {6,B}
5    C 0 {3,B} {6,B}
6 *3 C 1 {4,B} {5,B}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.3e+17,"s^-1"),
        n = -1,
        Ea = (204598,"kcal/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Fascella, S.", "Cavallotti, C.", "Rota, R.", "Carra, S."],
        title = u'Quantum chemistry investigation of key reactions involved in the formation of naphthalene and indene',
        journal = "J. Phys. Chem. A",
        volume = "108",
        pages = """3829-3843""",
        year = "2004",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011148/rk00000004.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011148/rk00000004.xml
""",
    history = [
        ("Tue May 17 14:34:44 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011148/rk00000004.xml"""),
        ("Fri Jun  3 16:02:18 2011","Josh Allen <jwallen@mit.edu>","action","""Fixed incorrect value for activation energy."""),
    ],
)

entry(
    index = 200,
    label = "r00011210",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *1 C 0 {1,S} {4,D}
4 *2 C 0 {3,D}
""",
    reactant2 = 
"""
1 *3 H 1
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {4,S} {5,S}
3    C 0 {1,S}
4 *2 C 1 {2,S}
5 *3 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.49e+07,"cm^3/(mol*s)"),
        n = 0,
        Ea = (6244.17,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Kyogoku, T.", "Watanabe, T.", "Tsunashima, S.", "Sato, S."],
        title = u'Arrhenius parameters for the reactions of hydrogen and deuterium atoms with four butenes',
        journal = "Bull. Chem. Soc. Jpn.",
        volume = "56",
        pages = """19""",
        year = "1983",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011210/rk00000004.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011210/rk00000004.xml
""",
    history = [
        ("Tue May 17 14:34:46 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011210/rk00000004.xml"""),
    ],
)

entry(
    index = 214,
    label = "r00011282",
    reactant1 = 
"""
1 *2 C 0 {2,D}
2 *1 O 0 {1,D}
""",
    reactant2 = 
"""
1 *3 H 1
""",
    product1 = 
"""
1 *2 C 1 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *3 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (540000,"cm^3/(mol*s)"),
        n = 0.454,
        Ea = (15062.4,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011282/rk00000017.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011282/rk00000017.xml
""",
    history = [
        ("Tue May 17 14:34:46 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011282/rk00000017.xml"""),
    ],
)

entry(
    index = 232,
    label = "r00011402",
    reactant1 = 
"""
1 *1 C 0 {2,T}
2 *2 C 0 {1,T}
""",
    reactant2 = 
"""
1 *3 H 1
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,S}
2 *2 C 1 {1,D}
3 *3 H 0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.6e+06,"cm^3/(mol*s)"),
        n = 0,
        Ea = (10041.6,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011402/rk00000027.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011402/rk00000027.xml
""",
    history = [
        ("Tue May 17 14:34:47 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011402/rk00000027.xml"""),
    ],
)

entry(
    index = 240,
    label = "r00011527",
    reactant1 = 
"""
1 *1 C 0 {2,S} {3,D} {5,S}
2    C 0 {1,S} {4,T}
3 *2 C 1 {1,D}
4    C 0 {2,T}
5 *3 H 0 {1,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,T}
2 *1 C 0 {1,S} {4,T}
3    C 0 {1,T}
4 *2 C 0 {2,T}
""",
    product2 = 
"""
1 *3 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14,"s^-1"),
        n = 0,
        Ea = (167121,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Back, M.H."],
        title = u'Mechanism of the pyrolysis of acetylene',
        journal = "Can. J. Chem.",
        volume = "49",
        pages = """2199""",
        year = "1971",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011527/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011527/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:34:48 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011527/rk00000001.xml"""),
    ],
)

entry(
    index = 241,
    label = "r00011527",
    reactant1 = 
"""
1 *1 C 0 {2,S} {3,D} {5,S}
2    C 0 {1,S} {4,T}
3 *2 C 1 {1,D}
4    C 0 {2,T}
5 *3 H 0 {1,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,T}
2 *1 C 0 {1,S} {4,T}
3    C 0 {1,T}
4 *2 C 0 {2,T}
""",
    product2 = 
"""
1 *3 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14,"s^-1"),
        n = 0,
        Ea = (170447,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Weissman, M.", "Benson, S.W."],
        title = u'Pyrolysis of methyl chloride, a pathway in the chlorine-catalyzed polymerization of methane',
        journal = "Int. J. Chem. Kinet.",
        volume = "16",
        pages = """307""",
        year = "1984",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011527/rk00000003.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011527/rk00000003.xml
""",
    history = [
        ("Tue May 17 14:34:48 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011527/rk00000003.xml"""),
    ],
)

entry(
    index = 242,
    label = "r00011527",
    reactant1 = 
"""
1 *1 C 0 {2,S} {3,D} {5,S}
2    C 0 {1,S} {4,T}
3 *2 C 1 {1,D}
4    C 0 {2,T}
5 *3 H 0 {1,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,T}
2 *1 C 0 {1,S} {4,T}
3    C 0 {1,T}
4 *2 C 0 {2,T}
""",
    product2 = 
"""
1 *3 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.16228e+61,"s^-1"),
        n = -13.9,
        Ea = (256898,"kcal/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Braun-Unkhoff, M.", "Frank, P.", "Just, Th."],
        title = u'A shock tube study on the thermal decomposition of toluene and of the phenyl radical at high temperatures',
        journal = "Symp. Int. Combust. Proc.",
        volume = "22",
        pages = """1053""",
        year = "1989",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011527/rk00000005.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011527/rk00000005.xml
""",
    history = [
        ("Tue May 17 14:34:48 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011527/rk00000005.xml"""),
        ("Fri Jun  3 14:55:12 2011","Josh Allen <jwallen@mit.edu>","action","""Fixed incorrect values of the kinetic parameters."""),
    ],
)

entry(
    index = 260,
    label = "r00011689",
    reactant1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 0 {1,S}
3    C 0 {1,S}
4    C 0 {1,S}
5 *2 O 1 {1,S}
""",
    product1 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *1 C 0 {1,S} {2,S} {4,D}
4 *2 O 0 {3,D}
""",
    product2 = 
"""
1 *3 C 1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.15e+14,"s^-1"),
        n = 0,
        Ea = (56900,"kJ/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."],
        title = u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds',
        journal = "Can. J. Chem.",
        volume = "81",
        pages = """431-442""",
        year = "2003",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011689/rk00000023.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011689/rk00000023.xml
""",
    history = [
        ("Tue May 17 14:34:50 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011689/rk00000023.xml"""),
        ("Fri Jun  3 17:09:42 2011","Josh Allen <jwallen@mit.edu>","action","""Fixed incorrect value of activation energy."""),
    ],
)

entry(
    index = 263,
    label = "r00011862",
    reactant1 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    reactant2 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *1 C 0 {1,S} {2,S} {4,D}
4 *2 C 0 {3,D}
""",
    product1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *2 C 1 {1,S}
5 *3 O 0 {1,S} {6,S}
6    O 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0131,"cm^3/(mol*s)"),
        n = 2.10058,
        Ea = (31547.4,"kcal/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Chen, C.-J.", "Bozzelli, J.W."],
        title = u'Analysis of Tertiary Butyl Radical + O_2, Isobutene + HO_2, Isobutene + OH, and Isobutene-OH Adducts + O_2: A Detailed Tertiary Butyl Oxidation Mechanism',
        journal = "J. Phys. Chem. A",
        volume = "103",
        pages = """9731-9769""",
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011862/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011862/rk00000001.xml
Table 9 rate k1 in doi:10.1021/jp991227n
Fitting with two parameter modified Arrhenius equation; A estimated using TST- and MP2-determined entropies, Ea evaluated from CBS-q//MP2(full)/6-31G* calculation.
""",
    history = [
        ("Tue May 17 14:34:51 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011862/rk00000001.xml"""),
        ("Wed Jun 15 13:08:15 2011","Josh Allen <jwallen@mit.edu>","action","""Fixed incorrect values of preexponential and activation energy."""),
        ("2011-06-20","Richard West <rwest@mit.edu>","action","""Fixed typo in A and added detail to longDesc."""),
    ],
)

entry(
    index = 277,
    label = "r00012570",
    reactant1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *2 O 1 {1,S}
5 *3 H 0 {1,S}
""",
    product1 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *1 C 0 {1,S} {2,S} {4,D}
4 *2 O 0 {3,D}
""",
    product2 = 
"""
1 *3 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.58e+13,"s^-1"),
        n = 0,
        Ea = (76600,"kJ/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."],
        title = u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds',
        journal = "Can. J. Chem.",
        volume = "81",
        pages = """431-442""",
        year = "2003",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00012570/rk00000004.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00012570/rk00000004.xml
""",
    history = [
        ("Tue May 17 14:34:54 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00012570/rk00000004.xml"""),
        ("Fri Jun  3 17:09:42 2011","Josh Allen <jwallen@mit.edu>","action","""Fixed incorrect value of activation energy."""),
    ],
)

entry(
    index = 286,
    label = "r00012571",
    reactant1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S}
2 *3 C 0 {1,S}
3    C 0 {1,S}
4 *2 O 1 {1,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,D}
3 *2 O 0 {2,D}
""",
    product2 = 
"""
1 *3 C 1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (9.12e+13,"s^-1"),
        n = 0,
        Ea = (60100,"kJ/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."],
        title = u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds',
        journal = "Can. J. Chem.",
        volume = "81",
        pages = """431-442""",
        year = "2003",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00012571/rk00000015.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00012571/rk00000015.xml
""",
    history = [
        ("Tue May 17 14:34:54 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00012571/rk00000015.xml"""),
        ("Fri Jun  3 17:09:42 2011","Josh Allen <jwallen@mit.edu>","action","""Fixed incorrect value of activation energy."""),
    ],
)

entry(
    index = 296,
    label = "r00012710",
    reactant1 = 
"""
1 *2 C 0 {2,D}
2 *1 C 0 {1,D} {3,D}
3    O 0 {2,D}
""",
    reactant2 = 
"""
1 *3 H 1
""",
    product1 = 
"""
1 *2 C 1 {2,S}
2 *1 C 0 {1,S} {3,D} {4,S}
3    O 0 {2,D}
4 *3 H 0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (486500,"cm^3/(mol*s)"),
        n = 0.422,
        Ea = (-7342.92,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00012710/rk00000010.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00012710/rk00000010.xml
""",
    history = [
        ("Tue May 17 14:34:57 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00012710/rk00000010.xml"""),
    ],
)

entry(
    index = 315,
    label = "r00012935",
    reactant1 = 
"""
1 *3 C 0 {2,S}
2 *1 C 0 {1,S} {3,D}
3 *2 C 1 {2,D}
""",
    product1 = 
"""
1 *2 C 0 {2,T}
2 *1 C 0 {1,T}
""",
    product2 = 
"""
1 *3 C 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.26e+13,"s^-1"),
        n = 0,
        Ea = (139683,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Dean, A.M."],
        title = u'Predictions of pressure and temperature effects upon radical addition and recombination reactions',
        journal = "J. Phys. Chem.",
        volume = "89",
        pages = """4600""",
        year = "1985",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00012935/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00012935/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:04 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00012935/rk00000001.xml"""),
    ],
)

entry(
    index = 316,
    label = "r00012935",
    reactant1 = 
"""
1 *3 C 0 {2,S}
2 *1 C 0 {1,S} {3,D}
3 *2 C 1 {2,D}
""",
    product1 = 
"""
1 *2 C 0 {2,T}
2 *1 C 0 {1,T}
""",
    product2 = 
"""
1 *3 C 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.77e+12,"s^-1"),
        n = 0,
        Ea = (180424,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Naroznik, M.", "Niedzielski, J."],
        title = u'Propylene photolysis at 6.7 eV: Calculation of the quantum yields for the secondary processes',
        journal = "J. Photochem.",
        volume = "32",
        pages = """281""",
        year = "1986",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00012935/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00012935/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:35:04 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00012935/rk00000002.xml"""),
    ],
)

entry(
    index = 317,
    label = "r00012935",
    reactant1 = 
"""
1 *1 C 0 {2,T}
2 *2 C 0 {1,T}
""",
    reactant2 = 
"""
1 *3 C 1
""",
    product1 = 
"""
1 *3 C 0 {2,S}
2 *1 C 0 {1,S} {3,D}
3 *2 C 1 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (251000,"cm^3/(mol*s)"),
        n = 0,
        Ea = (32177,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Garcia Dominguez, J.A.", "Trotman-Dickenson, A.F."],
        title = u'The reactions of alkyl radicals. Part IX. The addition of methyl, ethyl, isopropyl, and t-butyl radicals to acetylene and the isomerization of alkenyl radicals',
        journal = "J. Chem. Soc.",
        pages = """940-944""",
        year = "1962",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00012935/rk00000003.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00012935/rk00000003.xml
""",
    history = [
        ("Tue May 17 14:35:04 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00012935/rk00000003.xml"""),
    ],
)

entry(
    index = 318,
    label = "r00012935",
    reactant1 = 
"""
1 *1 C 0 {2,T}
2 *2 C 0 {1,T}
""",
    reactant2 = 
"""
1 *3 C 1
""",
    product1 = 
"""
1 *3 C 0 {2,S}
2 *1 C 0 {1,S} {3,D}
3 *2 C 1 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.61048e+34,"cm^3/(mol*s)"),
        n = -8.58,
        Ea = (84807.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Dean, A.M.", "Westmoreland, P.R."],
        title = u'Bimolecular QRRK analyss of methyl radical reactions',
        journal = "Int. J. Chem. Kinet.",
        volume = "19",
        pages = """207""",
        year = "1987",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00012935/rk00000004.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00012935/rk00000004.xml
""",
    history = [
        ("Tue May 17 14:35:04 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00012935/rk00000004.xml"""),
    ],
)

entry(
    index = 319,
    label = "r00012935",
    reactant1 = 
"""
1 *1 C 0 {2,T}
2 *2 C 0 {1,T}
""",
    reactant2 = 
"""
1 *3 C 1
""",
    product1 = 
"""
1 *3 C 0 {2,S}
2 *1 C 0 {1,S} {3,D}
3 *2 C 1 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (603000,"cm^3/(mol*s)"),
        n = 0,
        Ea = (32426.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Esser, C.", "Frank, P.", "Just, Th.", "Kerr, J.A.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."],
        title = u'Evaluated kinetic data for combustion modelling',
        journal = "J. Phys. Chem. Ref. Data",
        volume = "21",
        pages = """411-429""",
        year = "1992",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00012935/rk00000005.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00012935/rk00000005.xml
""",
    history = [
        ("Tue May 17 14:35:04 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00012935/rk00000005.xml"""),
    ],
)

entry(
    index = 320,
    label = "r00012935",
    reactant1 = 
"""
1 *1 C 0 {2,T}
2 *2 C 0 {1,T}
""",
    reactant2 = 
"""
1 *3 C 1
""",
    product1 = 
"""
1 *3 C 0 {2,S}
2 *1 C 0 {1,S} {3,D}
3 *2 C 1 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.56501e+50,"cm^3/(mol*s)"),
        n = -13.7,
        Ea = (116403,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Diau, E.W.", "Lin, M.C."],
        title = u'A theoretical study of the CH_3 + C_2H_2 reaction',
        journal = "J. Chem. Phys.",
        volume = "101",
        pages = """3923-3927""",
        year = "1994",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00012935/rk00000006.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00012935/rk00000006.xml
""",
    history = [
        ("Tue May 17 14:35:04 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00012935/rk00000006.xml"""),
    ],
)

entry(
    index = 321,
    label = "r00012935",
    reactant1 = 
"""
1 *1 C 0 {2,T}
2 *2 C 0 {1,T}
""",
    reactant2 = 
"""
1 *3 C 1
""",
    product1 = 
"""
1 *3 C 0 {2,S}
2 *1 C 0 {1,S} {3,D}
3 *2 C 1 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.2934e+24,"cm^3/(mol*s)"),
        n = -5.98,
        Ea = (55790.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Diau, E.W.", "Lin, M.C."],
        title = u'A theoretical study of the CH_3 + C_2H_2 reaction',
        journal = "J. Chem. Phys.",
        volume = "101",
        pages = """3923-3927""",
        year = "1994",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00012935/rk00000007.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00012935/rk00000007.xml
""",
    history = [
        ("Tue May 17 14:35:04 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00012935/rk00000007.xml"""),
    ],
)

entry(
    index = 322,
    label = "r00012935",
    reactant1 = 
"""
1 *1 C 0 {2,T}
2 *2 C 0 {1,T}
""",
    reactant2 = 
"""
1 *3 C 1
""",
    product1 = 
"""
1 *3 C 0 {2,S}
2 *1 C 0 {1,S} {3,D}
3 *2 C 1 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (375000,"cm^3/(mol*s)"),
        n = 0,
        Ea = (32509.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Diau, E.W.", "Lin, M.C."],
        title = u'Kinetic modeling of the CH_3 + C_2H_2 reaction data with sensitivity analyses',
        journal = "Int. J. Chem. Kinet.",
        volume = "27",
        pages = """855-866""",
        year = "1995",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00012935/rk00000008.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00012935/rk00000008.xml
""",
    history = [
        ("Tue May 17 14:35:04 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00012935/rk00000008.xml"""),
    ],
)

entry(
    index = 324,
    label = "r00013096",
    reactant1 = 
"""
1 *3 C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {4,S}
3    C 0 {1,S} {5,D}
4 *2 C 1 {2,S}
5    C 0 {3,D}
""",
    product1 = 
"""
1 *1 C 0 {2,D}
2 *2 C 0 {1,D}
""",
    product2 = 
"""
1    C 0 {2,D} {3,S}
2    C 0 {1,D}
3 *3 C 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.31e+13,"s^-1"),
        n = 0,
        Ea = (93953.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Gierczak, T.", "Gawlowski, J.", "Niedzielski, J."],
        title = u'Mutual isomerization of cyclopentyl and 1-penten-5-yl radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "18",
        pages = """623-637""",
        year = "1986",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00013096/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013096/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:12 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00013096/rk00000001.xml"""),
    ],
)

entry(
    index = 325,
    label = "r00015135",
    reactant1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {6,S}
2 *3 C 0 {1,S} {5,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    C 0 {2,S}
6 *2 O 1 {1,S}
""",
    product1 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *1 C 0 {1,S} {2,S} {4,D}
4 *2 O 0 {3,D}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.01e+14,"s^-1"),
        n = 0,
        Ea = (59864.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Batt, L.", "Islam, T.S.A.", "Rattray, G.N."],
        title = u'The Gas-Phase Pyrolysis of Alkyl Nitrites. VI. t-Amyl Nitrite',
        journal = "Int. J. Chem. Kinet.",
        volume = "10",
        pages = """931""",
        year = "1978",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00015135/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015135/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:17 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015135/rk00000001.xml"""),
    ],
)

entry(
    index = 326,
    label = "r00015135",
    reactant1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {6,S}
2 *3 C 0 {1,S} {5,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    C 0 {2,S}
6 *2 O 1 {1,S}
""",
    product1 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *1 C 0 {1,S} {2,S} {4,D}
4 *2 O 0 {3,D}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.31e+14,"s^-1"),
        n = 0,
        Ea = (57702.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Batt, L."],
        title = u'The Gas-Phase Decomposition of Alkoxy Radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "11",
        pages = """977""",
        year = "1979",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00015135/rk00000003.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015135/rk00000003.xml
""",
    history = [
        ("Tue May 17 14:35:17 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015135/rk00000003.xml"""),
    ],
)

entry(
    index = 327,
    label = "r00015135",
    reactant1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {6,S}
2 *3 C 0 {1,S} {5,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    C 0 {2,S}
6 *2 O 1 {1,S}
""",
    product1 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *1 C 0 {1,S} {2,S} {4,D}
4 *2 O 0 {3,D}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.98e+13,"s^-1"),
        n = 0,
        Ea = (51882.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Choo, K.Y.", "Benson, S.W."],
        title = u'Arrhenius Parameters for the Alkoxy Radical Decomposition Reactions',
        journal = "Int. J. Chem. Kinet.",
        volume = "13",
        pages = """833""",
        year = "1981",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00015135/rk00000004.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015135/rk00000004.xml
""",
    history = [
        ("Tue May 17 14:35:17 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015135/rk00000004.xml"""),
    ],
)

entry(
    index = 328,
    label = "r00015135",
    reactant1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {6,S}
2 *3 C 0 {1,S} {5,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    C 0 {2,S}
6 *2 O 1 {1,S}
""",
    product1 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *1 C 0 {1,S} {2,S} {4,D}
4 *2 O 0 {3,D}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+15,"s^-1"),
        n = 0,
        Ea = (64021.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Heicklen, J."],
        title = u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals',
        journal = "Adv. Photochem.",
        volume = "14",
        pages = """177""",
        year = "1988",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00015135/rk00000005.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015135/rk00000005.xml
""",
    history = [
        ("Tue May 17 14:35:17 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015135/rk00000005.xml"""),
    ],
)

entry(
    index = 329,
    label = "r00015136",
    reactant1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {6,S}
2    C 0 {1,S} {5,S}
3 *3 C 0 {1,S}
4    C 0 {1,S}
5    C 0 {2,S}
6 *2 O 1 {1,S}
""",
    product1 = 
"""
1    C 0 {2,S} {4,S}
2    C 0 {1,S}
3    C 0 {4,S}
4 *1 C 0 {1,S} {3,S} {5,D}
5 *2 O 0 {4,D}
""",
    product2 = 
"""
1 *3 C 1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+15,"s^-1"),
        n = 0,
        Ea = (78239.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Batt, L.", "Islam, T.S.A.", "Rattray, G.N."],
        title = u'The Gas-Phase Pyrolysis of Alkyl Nitrites. VI. t-Amyl Nitrite',
        journal = "Int. J. Chem. Kinet.",
        volume = "10",
        pages = """931""",
        year = "1978",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00015136/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015136/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:17 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015136/rk00000001.xml"""),
    ],
)

entry(
    index = 330,
    label = "r00015136",
    reactant1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {6,S}
2    C 0 {1,S} {5,S}
3 *3 C 0 {1,S}
4    C 0 {1,S}
5    C 0 {2,S}
6 *2 O 1 {1,S}
""",
    product1 = 
"""
1    C 0 {2,S} {4,S}
2    C 0 {1,S}
3    C 0 {4,S}
4 *1 C 0 {1,S} {3,S} {5,D}
5 *2 O 0 {4,D}
""",
    product2 = 
"""
1 *3 C 1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.31e+13,"s^-1"),
        n = 0,
        Ea = (67347.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Choo, K.Y.", "Benson, S.W."],
        title = u'Arrhenius Parameters for the Alkoxy Radical Decomposition Reactions',
        journal = "Int. J. Chem. Kinet.",
        volume = "13",
        pages = """833""",
        year = "1981",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00015136/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015136/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:35:17 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015136/rk00000002.xml"""),
    ],
)

entry(
    index = 331,
    label = "r00015136",
    reactant1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {6,S}
2    C 0 {1,S} {5,S}
3 *3 C 0 {1,S}
4    C 0 {1,S}
5    C 0 {2,S}
6 *2 O 1 {1,S}
""",
    product1 = 
"""
1    C 0 {2,S} {4,S}
2    C 0 {1,S}
3    C 0 {4,S}
4 *1 C 0 {1,S} {3,S} {5,D}
5 *2 O 0 {4,D}
""",
    product2 = 
"""
1 *3 C 1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+15,"s^-1"),
        n = 0,
        Ea = (78239.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Heicklen, J."],
        title = u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals',
        journal = "Adv. Photochem.",
        volume = "14",
        pages = """177""",
        year = "1988",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00015136/rk00000003.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015136/rk00000003.xml
""",
    history = [
        ("Tue May 17 14:35:17 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015136/rk00000003.xml"""),
    ],
)

entry(
    index = 334,
    label = "r00015628",
    reactant1 = 
"""
1    C 0 {3,S}
2 *1 C 0 {3,D} {4,S}
3 *2 C 1 {1,S} {2,D}
4 *3 H 0 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,T}
3 *1 C 0 {2,T}
""",
    product2 = 
"""
1 *3 H 1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (9.55e+12,"s^-1"),
        n = 0,
        Ea = (192896,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Naroznik, M.", "Niedzielski, J."],
        title = u'Propylene photolysis at 6.7 eV: Calculation of the quantum yields for the secondary processes',
        journal = "J. Photochem.",
        volume = "32",
        pages = """281""",
        year = "1986",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00015628/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015628/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:25 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015628/rk00000001.xml"""),
    ],
)

entry(
    index = 335,
    label = "r00015628",
    reactant1 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,T}
3 *1 C 0 {2,T}
""",
    reactant2 = 
"""
1 *3 H 1
""",
    product1 = 
"""
1    C 0 {3,S}
2 *1 C 0 {3,D} {4,S}
3 *2 C 1 {1,S} {2,D}
4 *3 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.5e+06,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8397.62,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Wagner, H.Gg.", "Zellner, R."],
        title = u'Reaktionen von Wasserstoffatomen mit ungesaettigten C_3-Kohlenwasserstoffen. II. Die Reaktion von H-Atomen mit Methylacetylen',
        journal = "Ber. Bunsenges. Phys. Chem.",
        volume = "76",
        pages = """518""",
        year = "1972",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00015628/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015628/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:35:25 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015628/rk00000002.xml"""),
    ],
)

entry(
    index = 336,
    label = "r00015629",
    reactant1 = 
"""
1 *1 C 0 {3,S} {4,S}
2    C 0 {3,D}
3 *2 C 1 {1,S} {2,D}
4 *3 H 0 {1,S}
""",
    product1 = 
"""
1    C 0 {3,D}
2 *1 C 0 {3,D}
3 *2 C 0 {1,D} {2,D}
""",
    product2 = 
"""
1 *3 H 1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.32e+13,"s^-1"),
        n = 0,
        Ea = (199547,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Naroznik, M.", "Niedzielski, J."],
        title = u'Propylene photolysis at 6.7 eV: Calculation of the quantum yields for the secondary processes',
        journal = "J. Photochem.",
        volume = "32",
        pages = """281""",
        year = "1986",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00015629/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015629/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:25 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015629/rk00000001.xml"""),
    ],
)

entry(
    index = 337,
    label = "r00015629",
    reactant1 = 
"""
1 *1 C 0 {3,D}
2    C 0 {3,D}
3 *2 C 0 {1,D} {2,D}
""",
    reactant2 = 
"""
1 *3 H 1
""",
    product1 = 
"""
1 *1 C 0 {3,S} {4,S}
2    C 0 {3,D}
3 *2 C 1 {1,S} {2,D}
4 *3 H 0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.49e+06,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8397.62,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Wagner, H.Gg.", "Zellner, R."],
        title = u'Reaktionen von Wasserstoffatomen mit ungesaettigten C_3-Kohlenwasserstoffen. III. Die Reaktion von H-Atomen mit Allen',
        journal = "Ber. Bunsenges. Phys. Chem.",
        volume = "76",
        pages = """667""",
        year = "1972",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00015629/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015629/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:35:25 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015629/rk00000002.xml"""),
    ],
)

entry(
    index = 341,
    label = "r00015702",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *1 C 0 {1,S} {4,S} {5,S}
4 *2 O 1 {3,S}
5 *3 H 0 {3,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *1 C 0 {1,S} {4,D}
4 *2 O 0 {3,D}
""",
    product2 = 
"""
1 *3 H 1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.7e+13,"s^-1"),
        n = 0,
        Ea = (85800,"kJ/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."],
        title = u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds',
        journal = "Can. J. Chem.",
        volume = "81",
        pages = """431-442""",
        year = "2003",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00015702/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015702/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:26 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015702/rk00000001.xml"""),
        ("Fri Jun  3 17:09:42 2011","Josh Allen <jwallen@mit.edu>","action","""Fixed incorrect value of activation energy."""),
    ],
)

entry(
    index = 342,
    label = "r00015704",
    reactant1 = 
"""
1 *1 C 0 {2,D} {3,S} {4,S}
2    O 0 {1,D}
3 *2 O 1 {1,S}
4 *3 H 0 {1,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,D}
2    O 0 {1,D}
3 *2 O 0 {1,D}
""",
    product2 = 
"""
1 *3 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"s^-1"),
        n = 0.307,
        Ea = (138020,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Larson, c.W.", "Stewart, P.H.", "Golden, D.M."],
        title = u'Pressure and temperature dependence of reactions proceeding via a bound complex. An approach for combustion and atmospheric chemistry modelers. Application to HO + CO \u2192 [HOCO] \u2192 H + CO_2',
        journal = "Int. J. Chem. Kinet.",
        volume = "20",
        pages = """27""",
        year = "1988",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00015704/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015704/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:26 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015704/rk00000001.xml"""),
    ],
)

entry(
    index = 345,
    label = "r00015716",
    reactant1 = 
"""
1 *3 C 0 {3,S}
2 *2 C 1 {3,S}
3 *1 O 0 {1,S} {2,S}
""",
    product1 = 
"""
1 *2 C 0 {2,D}
2 *1 O 0 {1,D}
""",
    product2 = 
"""
1 *3 C 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.45e+14,"s^-1"),
        n = -0.22,
        Ea = (113908,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Li, Q.S.", "Zhang, Y.", "Zhang, S.W."],
        title = u'Dual level direct ab initio and density-functional theory dynamics study on the unimolecular decomposition of CH_3OCH_2 radical',
        journal = "J. Phys. Chem. A:",
        volume = "108",
        pages = """2014-2019""",
        year = "2004",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00015716/rk00000005.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015716/rk00000005.xml
""",
    history = [
        ("Tue May 17 14:35:26 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015716/rk00000005.xml"""),
    ],
)

entry(
    index = 346,
    label = "r00015756",
    reactant1 = 
"""
1     C 0 {2,S} {3,B} {4,B}
2  *1 C 0 {1,S} {5,D}
3     C 0 {1,B} {7,B}
4     C 0 {1,B} {8,B}
5  *2 C 0 {2,D} {9,S}
6     C 0 {7,B} {8,B}
7     C 0 {3,B} {6,B}
8     C 0 {4,B} {6,B}
9     C 0 {5,S} {10,D}
10    C 0 {9,D}
""",
    reactant2 = 
"""
1 *3 H 1
""",
    product1 = 
"""
1  *1 C 0 {2,S} {3,S} {11,S}
2     C 0 {1,S} {4,B} {5,B}
3  *2 C 1 {1,S} {9,S}
4     C 0 {2,B} {7,B}
5     C 0 {2,B} {8,B}
6     C 0 {7,B} {8,B}
7     C 0 {4,B} {6,B}
8     C 0 {5,B} {6,B}
9     C 0 {3,S} {10,D}
10    C 0 {9,D}
11 *3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.2e+06,"cm^3/(mol*s)"),
        n = 0,
        Ea = (36819.2,"kcal/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Fascella, S.", "Cavallotti, C.", "Rota, R.", "Carra, S."],
        title = u'Quantum chemistry investigation of key reactions involved in the formation of naphthalene and indene',
        journal = "J. Phys. Chem. A",
        volume = "108",
        pages = """3829-3843""",
        year = "2004",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00015756/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015756/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:28 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015756/rk00000001.xml"""),
        ("Fri Jun  3 16:02:18 2011","Josh Allen <jwallen@mit.edu>","action","""Fixed incorrect value for activation energy."""),
    ],
)

entry(
    index = 347,
    label = "r00015756",
    reactant1 = 
"""
1  *1 C 0 {2,S} {3,S} {11,S}
2     C 0 {1,S} {4,B} {5,B}
3  *2 C 1 {1,S} {9,S}
4     C 0 {2,B} {7,B}
5     C 0 {2,B} {8,B}
6     C 0 {7,B} {8,B}
7     C 0 {4,B} {6,B}
8     C 0 {5,B} {6,B}
9     C 0 {3,S} {10,D}
10    C 0 {9,D}
11 *3 H 0 {1,S}
""",
    product1 = 
"""
1     C 0 {2,S} {3,B} {4,B}
2  *1 C 0 {1,S} {5,D}
3     C 0 {1,B} {6,B}
4     C 0 {1,B} {7,B}
5  *2 C 0 {2,D} {9,S}
6     C 0 {3,B} {8,B}
7     C 0 {4,B} {8,B}
8     C 0 {6,B} {7,B}
9     C 0 {5,S} {10,D}
10    C 0 {9,D}
""",
    product2 = 
"""
1 *3 H 1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.4e+12,"s^-1"),
        n = 0,
        Ea = (195811,"kcal/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Fascella, S.", "Cavallotti, C.", "Rota, R.", "Carra, S."],
        title = u'Quantum chemistry investigation of key reactions involved in the formation of naphthalene and indene',
        journal = "J. Phys. Chem. A",
        volume = "108",
        pages = """3829-3843""",
        year = "2004",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00015756/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015756/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:35:28 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015756/rk00000002.xml"""),
        ("Fri Jun  3 16:02:18 2011","Josh Allen <jwallen@mit.edu>","action","""Fixed incorrect value for activation energy."""),
    ],
)

entry(
    index = 350,
    label = "r00016108",
    reactant1 = 
"""
1    C 0 {2,B} {3,B} {7,S}
2    C 0 {1,B} {5,B}
3    C 0 {1,B} {6,B}
4    C 0 {5,B} {6,B}
5    C 0 {2,B} {4,B}
6    C 0 {3,B} {4,B}
7 *1 C 0 {1,S} {8,D} {9,S}
8 *2 C 1 {7,D}
9 *3 H 0 {7,S}
""",
    product1 = 
"""
1    C 0 {2,B} {3,B} {7,S}
2    C 0 {1,B} {4,B}
3    C 0 {1,B} {5,B}
4    C 0 {2,B} {6,B}
5    C 0 {3,B} {6,B}
6    C 0 {4,B} {5,B}
7 *1 C 0 {1,S} {8,T}
8 *2 C 0 {7,T}
""",
    product2 = 
"""
1 *3 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.8e+11,"s^-1"),
        n = 0.82,
        Ea = (162799,"kcal/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Tokmakov, I.V.", "Lin, M.C."],
        title = u'Reaction of phenyl radicals with acetylene: Quantum chemical investigation of the mechanism and master equation analysis of the kinetics',
        journal = "J. Am. Chem. Soc.",
        volume = "125",
        pages = """11397-11408""",
        year = "2003",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016108/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016108/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:37 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016108/rk00000001.xml"""),
    ],
)

entry(
    index = 355,
    label = "r00016184",
    reactant1 = 
"""
1 *1 C 0 {2,S} {4,S}
2 *3 C 0 {1,S} {3,D}
3    C 0 {2,D}
4 *2 O 1 {1,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D}
2 *2 O 0 {1,D}
""",
    product2 = 
"""
1    C 0 {2,D}
2 *3 C 1 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.39e+14,"s^-1"),
        n = 0,
        Ea = (94800,"kJ/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."],
        title = u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds',
        journal = "Can. J. Chem.",
        volume = "81",
        pages = """431-442""",
        year = "2003",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016184/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016184/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:38 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016184/rk00000001.xml"""),
        ("Fri Jun  3 17:09:42 2011","Josh Allen <jwallen@mit.edu>","action","""Fixed incorrect value of activation energy."""),
    ],
)

entry(
    index = 356,
    label = "r00016185",
    reactant1 = 
"""
1 *1 C 0 {2,S} {4,S} {5,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D}
4 *2 O 1 {1,S}
5 *3 H 0 {1,S}
""",
    product1 = 
"""
1    C 0 {2,D} {3,S}
2    C 0 {1,D}
3 *1 C 0 {1,S} {4,D}
4 *2 O 0 {3,D}
""",
    product2 = 
"""
1 *3 H 1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.1e+13,"s^-1"),
        n = 0,
        Ea = (77200,"kJ/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."],
        title = u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds',
        journal = "Can. J. Chem.",
        volume = "81",
        pages = """431-442""",
        year = "2003",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016185/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016185/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:38 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016185/rk00000001.xml"""),
        ("Fri Jun  3 17:09:42 2011","Josh Allen <jwallen@mit.edu>","action","""Fixed incorrect value of activation energy."""),
    ],
)

entry(
    index = 358,
    label = "r00016187",
    reactant1 = 
"""
1 *1 C 0 {2,S} {8,S} {9,S}
2    C 0 {1,S} {3,B} {4,B}
3    C 0 {2,B} {6,B}
4    C 0 {2,B} {7,B}
5    C 0 {6,B} {7,B}
6    C 0 {3,B} {5,B}
7    C 0 {4,B} {5,B}
8 *2 O 1 {1,S}
9 *3 H 0 {1,S}
""",
    product1 = 
"""
1    C 0 {2,B} {3,B} {7,S}
2    C 0 {1,B} {4,B}
3    C 0 {1,B} {6,B}
4    C 0 {2,B} {5,B}
5    C 0 {4,B} {6,B}
6    C 0 {3,B} {5,B}
7 *1 C 0 {1,S} {8,D}
8 *2 O 0 {7,D}
""",
    product2 = 
"""
1 *3 H 1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.27e+14,"s^-1"),
        n = 0,
        Ea = (4614.53,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Brezinsky, K.", "Litzinger, T.A.", "Glassman, I."],
        title = u'The high temperature oxidation of the methyl side chain of toluene',
        journal = "Int. J. Chem. Kinet.",
        volume = "16",
        pages = """1053""",
        year = "1984",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016187/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016187/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:39 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016187/rk00000001.xml"""),
    ],
)

entry(
    index = 359,
    label = "r00016188",
    reactant1 = 
"""
1 *3 C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {4,S} {5,S}
3    C 0 {1,S}
4    C 0 {2,S}
5 *2 O 1 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,D}
3 *2 O 0 {2,D}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+16,"s^-1"),
        n = 0,
        Ea = (73250.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Batt, L.", "McCulloch, R.D.", "Milne, R.T."],
        title = u'Thermochemical and Kinetic Studies of Alkyl Nitrites (RONO)-D(RO-NO), The Reactions between RO. and NO, and the Decomposition RO.',
        journal = "Proc. Symp. Chem. Kinet. Data Upper Lower Atmos. 1974",
        pages = """441""",
        year = "1975",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:39 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000001.xml"""),
    ],
)

entry(
    index = 360,
    label = "r00016188",
    reactant1 = 
"""
1 *3 C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {4,S} {5,S}
3    C 0 {1,S}
4    C 0 {2,S}
5 *2 O 1 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,D}
3 *2 O 0 {2,D}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.31e+14,"s^-1"),
        n = 0,
        Ea = (64021.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Batt, L.", "McCulloch, R.D."],
        title = u'The Gas-Phase Pyrolysis of Alkyl Nitrites. II. s-Butyl Nitrite',
        journal = "Int. J. Chem. Kinet.",
        volume = "8",
        pages = """911""",
        year = "1976",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:35:39 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000002.xml"""),
    ],
)

entry(
    index = 361,
    label = "r00016188",
    reactant1 = 
"""
1 *3 C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {4,S} {5,S}
3    C 0 {1,S}
4    C 0 {2,S}
5 *2 O 1 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,D}
3 *2 O 0 {2,D}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.76e+14,"s^-1"),
        n = 0,
        Ea = (61111.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Baldwin, A.C.", "Barker, J.R.", "Golden, D.M.", "Hendry, D.G."],
        title = u'Photochemical smog. Rate parameter estimates and computer simulations',
        journal = "J. Phys. Chem.",
        volume = "81",
        pages = """2483""",
        year = "1977",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000003.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000003.xml
""",
    history = [
        ("Tue May 17 14:35:39 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000003.xml"""),
    ],
)

entry(
    index = 362,
    label = "r00016188",
    reactant1 = 
"""
1 *3 C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {4,S} {5,S}
3    C 0 {1,S}
4    C 0 {2,S}
5 *2 O 1 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,D}
3 *2 O 0 {2,D}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.94e+14,"s^-1"),
        n = 0,
        Ea = (64021.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Batt, L."],
        title = u'The Gas-Phase Decomposition of Alkoxy Radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "11",
        pages = """977""",
        year = "1979",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000004.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000004.xml
""",
    history = [
        ("Tue May 17 14:35:39 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000004.xml"""),
    ],
)

entry(
    index = 363,
    label = "r00016188",
    reactant1 = 
"""
1 *3 C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {4,S} {5,S}
3    C 0 {1,S}
4    C 0 {2,S}
5 *2 O 1 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,D}
3 *2 O 0 {2,D}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.98e+13,"s^-1"),
        n = 0,
        Ea = (56455.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Choo, K.Y.", "Benson, S.W."],
        title = u'Arrhenius Parameters for the Alkoxy Radical Decomposition Reactions',
        journal = "Int. J. Chem. Kinet.",
        volume = "13",
        pages = """833""",
        year = "1981",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000005.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000005.xml
""",
    history = [
        ("Tue May 17 14:35:39 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000005.xml"""),
    ],
)

entry(
    index = 364,
    label = "r00016188",
    reactant1 = 
"""
1 *3 C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {4,S} {5,S}
3    C 0 {1,S}
4    C 0 {2,S}
5 *2 O 1 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,D}
3 *2 O 0 {2,D}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+15,"s^-1"),
        n = 0,
        Ea = (64437.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Heicklen, J."],
        title = u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals',
        journal = "Adv. Photochem.",
        volume = "14",
        pages = """177""",
        year = "1988",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000007.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000007.xml
""",
    history = [
        ("Tue May 17 14:35:39 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000007.xml"""),
    ],
)

entry(
    index = 365,
    label = "r00016188",
    reactant1 = 
"""
1 *3 C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {4,S} {5,S}
3    C 0 {1,S}
4    C 0 {2,S}
5 *2 O 1 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,D}
3 *2 O 0 {2,D}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.35e+13,"s^-1"),
        n = 0,
        Ea = (62774.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Heiss, A.", "Tardieu de Maleissye, J.", "Viossat, V.", "Sahetchian, K.A."],
        title = u'Reactions of primary and secondary butoxy radicals in oxygen at atmospheric pressure',
        journal = "Int. J. Chem. Kinet.",
        volume = "23",
        pages = """607-622""",
        year = "1991",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000008.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000008.xml
""",
    history = [
        ("Tue May 17 14:35:39 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000008.xml"""),
    ],
)

entry(
    index = 366,
    label = "r00016188",
    reactant1 = 
"""
1 *3 C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {4,S} {5,S}
3    C 0 {1,S}
4    C 0 {2,S}
5 *2 O 1 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,D}
3 *2 O 0 {2,D}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.25e+13,"s^-1"),
        n = 0,
        Ea = (48900,"kJ/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."],
        title = u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds',
        journal = "Can. J. Chem.",
        volume = "81",
        pages = """431-442""",
        year = "2003",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000009.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000009.xml
""",
    history = [
        ("Tue May 17 14:35:39 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000009.xml"""),
        ("Fri Jun  3 17:09:42 2011","Josh Allen <jwallen@mit.edu>","action","""Fixed incorrect value of activation energy."""),
    ],
)

entry(
    index = 367,
    label = "r00016189",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {4,S} {5,S} {6,S}
3    C 0 {1,S}
4    C 0 {2,S}
5 *2 O 1 {2,S}
6 *3 H 0 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S} {4,S}
2    C 0 {1,S}
3    C 0 {4,S}
4 *1 C 0 {1,S} {3,S} {5,D}
5 *2 O 0 {4,D}
""",
    product2 = 
"""
1 *3 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.51e+13,"s^-1"),
        n = 0,
        Ea = (75600,"kJ/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."],
        title = u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds',
        journal = "Can. J. Chem.",
        volume = "81",
        pages = """431-442""",
        year = "2003",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016189/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016189/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:39 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016189/rk00000001.xml"""),
        ("Fri Jun  3 17:09:42 2011","Josh Allen <jwallen@mit.edu>","action","""Fixed incorrect value of activation energy."""),
    ],
)

entry(
    index = 368,
    label = "r00016190",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {4,S} {5,S}
3    C 0 {1,S}
4 *3 C 0 {2,S}
5 *2 O 1 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *1 C 0 {1,S} {4,D}
4 *2 O 0 {3,D}
""",
    product2 = 
"""
1 *3 C 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.94e+14,"s^-1"),
        n = 0,
        Ea = (79486.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Batt, L."],
        title = u'The Gas-Phase Decomposition of Alkoxy Radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "11",
        pages = """977""",
        year = "1979",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016190/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016190/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:39 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016190/rk00000001.xml"""),
    ],
)

entry(
    index = 369,
    label = "r00016190",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {4,S} {5,S}
3    C 0 {1,S}
4 *3 C 0 {2,S}
5 *2 O 1 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *1 C 0 {1,S} {4,D}
4 *2 O 0 {3,D}
""",
    product2 = 
"""
1 *3 C 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+15,"s^-1"),
        n = 0,
        Ea = (79902.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Heicklen, J."],
        title = u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals',
        journal = "Adv. Photochem.",
        volume = "14",
        pages = """177""",
        year = "1988",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016190/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016190/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:35:39 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016190/rk00000002.xml"""),
    ],
)

entry(
    index = 370,
    label = "r00016190",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {4,S} {5,S}
3    C 0 {1,S}
4 *3 C 0 {2,S}
5 *2 O 1 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *1 C 0 {1,S} {4,D}
4 *2 O 0 {3,D}
""",
    product2 = 
"""
1 *3 C 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.78e+13,"s^-1"),
        n = 0,
        Ea = (62300,"kJ/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."],
        title = u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds',
        journal = "Can. J. Chem.",
        volume = "81",
        pages = """431-442""",
        year = "2003",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016190/rk00000003.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016190/rk00000003.xml
""",
    history = [
        ("Tue May 17 14:35:39 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016190/rk00000003.xml"""),
        ("Fri Jun  3 17:09:42 2011","Josh Allen <jwallen@mit.edu>","action","""Fixed incorrect value of activation energy."""),
    ],
)

entry(
    index = 373,
    label = "r00016656",
    reactant1 = 
"""
1 *3 C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3 *1 C 0 {1,S} {5,S} {6,S}
4    C 0 {2,S}
5    C 0 {3,S}
6 *2 O 1 {3,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,D}
3 *2 O 0 {2,D}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *3 C 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.58e+14,"s^-1"),
        n = 0,
        Ea = (57702.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Dobe, S.", "Berces, T.", "Marta, F."],
        title = u'Gas phase decomposition and isomerization reactions of 2-pentoxy radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "18",
        pages = """329""",
        year = "1986",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016656/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016656/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:51 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016656/rk00000001.xml"""),
    ],
)

entry(
    index = 374,
    label = "r00016656",
    reactant1 = 
"""
1 *3 C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3 *1 C 0 {1,S} {5,S} {6,S}
4    C 0 {2,S}
5    C 0 {3,S}
6 *2 O 1 {3,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,D}
3 *2 O 0 {2,D}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *3 C 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+15,"s^-1"),
        n = 0,
        Ea = (64437.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Heicklen, J."],
        title = u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals',
        journal = "Adv. Photochem.",
        volume = "14",
        pages = """177""",
        year = "1988",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016656/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016656/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:35:51 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016656/rk00000002.xml"""),
    ],
)

entry(
    index = 375,
    label = "r00016657",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3 *1 C 0 {1,S} {5,S} {6,S}
4    C 0 {2,S}
5 *3 C 0 {3,S}
6 *2 O 1 {3,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S}
4 *1 C 0 {2,S} {5,D}
5 *2 O 0 {4,D}
""",
    product2 = 
"""
1 *3 C 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.58e+14,"s^-1"),
        n = 0,
        Ea = (72834.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Dobe, S.", "Berces, T.", "Marta, F."],
        title = u'Gas phase decomposition and isomerization reactions of 2-pentoxy radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "18",
        pages = """329""",
        year = "1986",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016657/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016657/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:52 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016657/rk00000001.xml"""),
    ],
)

entry(
    index = 376,
    label = "r00016678",
    reactant1 = 
"""
1 *1 C 0 {2,D} {5,S}
2 *2 C 1 {1,D} {3,S}
3    C 0 {2,S} {4,T}
4    C 0 {3,T}
5 *3 H 0 {1,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,T}
2 *2 C 0 {1,S} {4,T}
3    C 0 {1,T}
4 *1 C 0 {2,T}
""",
    product2 = 
"""
1 *3 H 1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+14,"s^-1"),
        n = 0,
        Ea = (216176,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Ghibaudi, E.", "Colussi, A.J."],
        title = u'Kinetics and thermochemistry of the equilibrium 2 (acetylene) = vinylacetylene. Direct evidence against a chain mechanism',
        journal = "J. Phys. Chem.",
        volume = "92",
        pages = """5839""",
        year = "1988",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016678/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016678/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:35:53 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016678/rk00000002.xml"""),
    ],
)

entry(
    index = 377,
    label = "r00016678",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,T}
2    C 0 {1,S} {4,T}
3 *1 C 0 {1,T}
4    C 0 {2,T}
""",
    reactant2 = 
"""
1 *3 H 1
""",
    product1 = 
"""
1 *1 C 0 {2,D} {5,S}
2 *2 C 1 {1,D} {3,S}
3    C 0 {2,S} {4,T}
4    C 0 {3,T}
5 *3 H 0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.3e+24,"cm^3/(mol*s)"),
        n = -4.92,
        Ea = (45189.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Eiteneer, B.", "Frenklach, M."],
        title = u'Experimental and Modeling Study of Shock-Tube Oxidation of Acetylene',
        journal = "Int J. Chem. Kinet.",
        volume = "35",
        pages = """391-414""",
        year = "2003",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016678/rk00000003.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016678/rk00000003.xml
""",
    history = [
        ("Tue May 17 14:35:53 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016678/rk00000003.xml"""),
    ],
)

entry(
    index = 378,
    label = "r00016682",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2 *3 C 0 {1,S} {4,S}
3    C 0 {1,S} {5,S}
4 *1 C 0 {2,S} {6,S}
5    O 0 {3,S}
6 *2 O 1 {4,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D}
2 *2 O 0 {1,D}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3 *3 C 1 {1,S}
4    O 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13,"s^-1"),
        n = 0,
        Ea = (79486.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Baldwin, A.C.", "Barker, J.R.", "Golden, D.M.", "Hendry, D.G."],
        title = u'Photochemical smog. Rate parameter estimates and computer simulations',
        journal = "J. Phys. Chem.",
        volume = "81",
        pages = """2483""",
        year = "1977",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016682/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016682/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:53 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016682/rk00000001.xml"""),
    ],
)

entry(
    index = 381,
    label = "r00016804",
    reactant1 = 
"""
1 *3 C 0 {3,S}
2    C 0 {4,S}
3 *1 C 0 {1,S} {4,D}
4 *2 C 1 {2,S} {3,D}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,T}
3 *1 C 0 {2,T}
""",
    product2 = 
"""
1 *3 C 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.01e+13,"s^-1"),
        n = 0,
        Ea = (131369,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Dean, A.M."],
        title = u'Predictions of pressure and temperature effects upon radical addition and recombination reactions',
        journal = "J. Phys. Chem.",
        volume = "89",
        pages = """4600""",
        year = "1985",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016804/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016804/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:36:00 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016804/rk00000001.xml"""),
    ],
)

entry(
    index = 382,
    label = "r00016804",
    reactant1 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,T}
3 *1 C 0 {2,T}
""",
    reactant2 = 
"""
1 *3 C 1
""",
    product1 = 
"""
1 *3 C 0 {3,S}
2    C 0 {4,S}
3 *1 C 0 {1,S} {4,D}
4 *2 C 1 {2,S} {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (501000,"cm^3/(mol*s)"),
        n = 0,
        Ea = (36833.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Getty, R.R.", "Kerr, J.A.", "Trotman-Dickenson, A.F."],
        title = u'The reactions of alkyl radicals. Part XIII. The additions of methyl, isopropyl, and t-butyl radicals to propyne and the isomerisation of alkenyl radicals',
        journal = "J. Chem. Soc. A",
        pages = """1360""",
        year = "1967",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016804/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016804/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:36:00 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016804/rk00000002.xml"""),
    ],
)

entry(
    index = 394,
    label = "r00016901",
    reactant1 = 
"""
1    C 0 {2,S} {3,D}
2 *1 C 0 {1,S} {4,D} {5,S}
3    C 0 {1,D}
4 *2 C 1 {2,D}
5 *3 H 0 {2,S}
""",
    product1 = 
"""
1    C 0 {2,D} {3,S}
2    C 0 {1,D}
3 *1 C 0 {1,S} {4,T}
4 *2 C 0 {3,T}
""",
    product2 = 
"""
1 *3 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14,"s^-1"),
        n = 0,
        Ea = (172941,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Weissman, M.", "Benson, S.W."],
        title = u'Pyrolysis of methyl chloride, a pathway in the chlorine-catalyzed polymerization of methane',
        journal = "Int. J. Chem. Kinet.",
        volume = "16",
        pages = """307""",
        year = "1984",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016901/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016901/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:36:03 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016901/rk00000001.xml"""),
    ],
)

entry(
    index = 395,
    label = "r00016901",
    reactant1 = 
"""
1    C 0 {2,S} {3,D}
2 *1 C 0 {1,S} {4,D} {5,S}
3    C 0 {1,D}
4 *2 C 1 {2,D}
5 *3 H 0 {2,S}
""",
    product1 = 
"""
1    C 0 {2,D} {3,S}
2    C 0 {1,D}
3 *1 C 0 {1,S} {4,T}
4 *2 C 0 {3,T}
""",
    product2 = 
"""
1 *3 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+14,"s^-1"),
        n = 0,
        Ea = (172941,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Colket, M.B., III", "Seery, D.J.", "Palmer, H.B."],
        title = u'The pyrolysis of acetylene initiated by acetone',
        journal = "Combust. Flame",
        volume = "75",
        pages = """343-366""",
        year = "1989",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016901/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016901/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:36:03 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016901/rk00000002.xml"""),
    ],
)

entry(
    index = 403,
    label = "r00017011",
    reactant1 = 
"""
1 *3 C 0 {2,D} {3,S}
2    C 0 {1,D} {4,S}
3 *1 C 0 {1,S} {5,D}
4    C 0 {2,S} {6,T}
5 *2 C 1 {3,D}
6    C 0 {4,T}
""",
    product1 = 
"""
1 *1 C 0 {2,T}
2 *2 C 0 {1,T}
""",
    product2 = 
"""
1    C 0 {2,S} {3,D}
2    C 0 {1,S} {4,T}
3 *3 C 1 {1,D}
4    C 0 {2,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.98107e+62,"s^-1"),
        n = -14.7,
        Ea = (240580,"kcal/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Braun-Unkhoff, M.", "Frank, P.", "Just, Th."],
        title = u'A shock tube study on the thermal decomposition of toluene and of the phenyl radical at high temperatures',
        journal = "Symp. Int. Combust. Proc.",
        volume = "22",
        pages = """1053""",
        year = "1989",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00017011/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00017011/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:36:10 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00017011/rk00000001.xml"""),
        ("Fri Jun  3 14:55:12 2011","Josh Allen <jwallen@mit.edu>","action","""Fixed incorrect values of the kinetic parameters."""),
    ],
)

entry(
    index = 404,
    label = "r00017011",
    reactant1 = 
"""
1 *1 C 0 {2,T}
2 *2 C 0 {1,T}
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,D}
2    C 0 {1,S} {4,T}
3 *3 C 1 {1,D}
4    C 0 {2,T}
""",
    product1 = 
"""
1 *3 C 0 {2,D} {3,S}
2    C 0 {1,D} {4,S}
3 *1 C 0 {1,S} {5,D}
4    C 0 {2,S} {6,T}
5 *2 C 1 {3,D}
6    C 0 {4,T}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.15382e+09,"cm^3/(mol*s)"),
        n = -1.51,
        Ea = (20204.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Westmoreland, P.R.", "Dean, A.M.", "Howard, J.B.", "Longwell, J.P."],
        title = u'Forming benzene in flames by chemically activated isomerization',
        journal = "J. Phys. Chem.",
        volume = "93",
        pages = """8171""",
        year = "1989",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00017011/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00017011/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:36:10 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00017011/rk00000002.xml"""),
    ],
)

entry(
    index = 405,
    label = "r00017013",
    reactant1 = 
"""
1    C 0 {2,D} {3,S}
2    C 0 {1,D} {4,S}
3 *1 C 0 {1,S} {5,D} {7,S}
4    C 0 {2,S} {6,T}
5 *2 C 1 {3,D}
6    C 0 {4,T}
7 *3 H 0 {3,S}
""",
    product1 = 
"""
1    C 0 {2,D} {3,S}
2    C 0 {1,D} {4,S}
3    C 0 {1,S} {5,T}
4 *1 C 0 {2,S} {6,T}
5    C 0 {3,T}
6 *2 C 0 {4,T}
""",
    product2 = 
"""
1 *3 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51189e+58,"s^-1"),
        n = -13.8,
        Ea = (208363,"kcal/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Braun-Unkhoff, M.", "Frank, P.", "Just, Th."],
        title = u'A shock tube study on the thermal decomposition of toluene and of the phenyl radical at high temperatures',
        journal = "Symp. Int. Combust. Proc.",
        volume = "22",
        pages = """1053""",
        year = "1989",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00017013/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00017013/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:36:10 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00017013/rk00000001.xml"""),
        ("Fri Jun  3 14:55:12 2011","Josh Allen <jwallen@mit.edu>","action","""Fixed incorrect values of the kinetic parameters."""),
    ],
)

entry(
    index = 406,
    label = "r00017118",
    reactant1 = 
"""
1    C 0 {2,D} {3,S}
2 *3 C 0 {1,D} {4,S}
3    C 0 {1,S} {5,D}
4 *1 C 0 {2,S} {6,D}
5    C 0 {3,D}
6 *2 C 1 {4,D}
""",
    product1 = 
"""
1 *2 C 0 {2,T}
2 *1 C 0 {1,T}
""",
    product2 = 
"""
1    C 0 {2,S} {3,D}
2    C 0 {1,S} {4,D}
3    C 0 {1,D}
4 *3 C 1 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.16e+13,"s^-1"),
        n = 0,
        Ea = (180424,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Dean, A.M."],
        title = u'Predictions of pressure and temperature effects upon radical addition and recombination reactions',
        journal = "J. Phys. Chem.",
        volume = "89",
        pages = """4600""",
        year = "1985",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00017118/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00017118/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:36:12 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00017118/rk00000001.xml"""),
    ],
)

entry(
    index = 407,
    label = "r00017118",
    reactant1 = 
"""
1 *1 C 0 {2,T}
2 *2 C 0 {1,T}
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,D}
2    C 0 {1,S} {4,D}
3    C 0 {1,D}
4 *3 C 1 {2,D}
""",
    product1 = 
"""
1    C 0 {2,D} {3,S}
2 *3 C 0 {1,D} {4,S}
3    C 0 {1,S} {5,D}
4 *1 C 0 {2,S} {6,D}
5    C 0 {3,D}
6 *2 C 1 {4,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.24474e+08,"cm^3/(mol*s)"),
        n = -1.38,
        Ea = (16628.9,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Westmoreland, P.R.", "Dean, A.M.", "Howard, J.B.", "Longwell, J.P."],
        title = u'Forming benzene in flames by chemically activated isomerization',
        journal = "J. Phys. Chem.",
        volume = "93",
        pages = """8171""",
        year = "1989",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00017118/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00017118/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:36:12 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00017118/rk00000002.xml"""),
    ],
)

