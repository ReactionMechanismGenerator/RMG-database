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

