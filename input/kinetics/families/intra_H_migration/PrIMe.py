#!/usr/bin/env python
# encoding: utf-8

name = "intra_H_migration/PrIMe"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 41,
    label = "r00015688",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2 *5 C 0 {1,S} {4,S}
3 *4 C 0 {1,S} {5,S}
4 *2 C 0 {2,S} {6,D} {7,S}
5 *1 C 1 {3,S}
6    C 0 {4,D}
7 *3 H 0 {4,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2 *5 C 0 {1,S} {4,S}
3 *4 C 0 {1,S} {6,S}
4 *2 C 0 {2,S} {7,S}
5    C 0 {6,D}
6 *1 C 1 {3,S} {5,D}
7 *3 H 0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11,"s^-1"),
        n = 0,
        Ea = (84807.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Handford-Styring, S.M.", "Walker, R.W."],
        title = u'Addition of cyclopentane to slowly reacting mixtures of H_2 + O_2 between 673 and 783 K: reactions of H and OH with cyclopentane and of cyclopentyl radicals',
        journal = "J. Chem. Soc. Faraday Trans.",
        volume = "91",
        pages = """1431-1438""",
        year = "1995",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00015688/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015688/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:25 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015688/rk00000001.xml"""),
    ],
)

entry(
    index = 42,
    label = "r00015689",
    reactant1 = 
"""
1 *5 C 0 {2,S} {3,S}
2 *2 C 0 {1,S} {4,S} {7,S}
3 *4 C 0 {1,S} {5,S}
4    C 0 {2,S} {6,D}
5 *1 C 1 {3,S}
6    C 0 {4,D}
7 *3 H 0 {2,S}
""",
    product1 = 
"""
1 *5 C 0 {2,S} {3,S}
2 *4 C 0 {1,S} {4,S}
3 *2 C 0 {1,S} {7,S}
4 *1 C 1 {2,S} {5,S}
5    C 0 {4,S} {6,D}
6    C 0 {5,D}
7 *3 H 0 {3,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+12,"s^-1"),
        n = 0,
        Ea = (124717,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Handford-Styring, S.M.", "Walker, R.W."],
        title = u'Addition of cyclopentane to slowly reacting mixtures of H_2 + O_2 between 673 and 783 K: reactions of H and OH with cyclopentane and of cyclopentyl radicals',
        journal = "J. Chem. Soc. Faraday Trans.",
        volume = "91",
        pages = """1431-1438""",
        year = "1995",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00015689/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015689/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:26 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015689/rk00000001.xml"""),
    ],
)

entry(
    index = 43,
    label = "r00015689",
    reactant1 = 
"""
1 *5 C 0 {2,S} {3,S}
2 *2 C 0 {1,S} {4,S} {7,S}
3 *4 C 0 {1,S} {5,S}
4    C 0 {2,S} {6,D}
5 *1 C 1 {3,S}
6    C 0 {4,D}
7 *3 H 0 {2,S}
""",
    product1 = 
"""
1 *5 C 0 {2,S} {3,S}
2 *4 C 0 {1,S} {4,S}
3 *2 C 0 {1,S} {7,S}
4 *1 C 1 {2,S} {5,S}
5    C 0 {4,S} {6,D}
6    C 0 {5,D}
7 *3 H 0 {3,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.67e+12,"s^-1"),
        n = -0.6,
        Ea = (252.795,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Matheu, D.M.", "Green, W.H.", "Grenda, J.M."],
        title = u'Capturing pressure-dependence in automated mechanism generation: Reactions through cycloalkyl intermediates',
        journal = "Int. J. Chem. Kinet.",
        volume = "35",
        pages = """95-119""",
        year = "2003",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00015689/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015689/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:35:26 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015689/rk00000002.xml"""),
    ],
)

entry(
    index = 44,
    label = "r00015924",
    reactant1 = 
"""
1 *5 C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3 *2 C 0 {1,S} {6,S}
4 *4 C 0 {2,S} {5,S}
5 *1 O 1 {4,S}
6 *3 H 0 {3,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2 *4 C 0 {1,S} {4,S}
3 *5 C 0 {1,S} {5,S}
4 *1 C 1 {2,S}
5 *2 O 0 {3,S} {6,S}
6 *3 H 0 {5,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.51e+11,"s^-1"),
        n = 0,
        Ea = (32260.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Baldwin, A.C.", "Barker, J.R.", "Golden, D.M.", "Hendry, D.G."],
        title = u'Photochemical smog. Rate parameter estimates and computer simulations',
        journal = "J. Phys. Chem.",
        volume = "81",
        pages = """2483""",
        year = "1977",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00015924/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015924/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:30 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015924/rk00000001.xml"""),
    ],
)

entry(
    index = 45,
    label = "r00015924",
    reactant1 = 
"""
1 *5 C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3 *2 C 0 {1,S} {6,S}
4 *4 C 0 {2,S} {5,S}
5 *1 O 1 {4,S}
6 *3 H 0 {3,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2 *4 C 0 {1,S} {4,S}
3 *5 C 0 {1,S} {5,S}
4 *1 C 1 {2,S}
5 *2 O 0 {3,S} {6,S}
6 *3 H 0 {5,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.51e+11,"s^-1"),
        n = 0,
        Ea = (32260.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Baldwin, A.C.", "Golden, D.M."],
        title = u'Alkoxy Radical Reactions: The Isomerization of n-Butoxy Radicals Generated from the Pyrolysis of n-Butyl Nitrite',
        journal = "Chem. Phys. Lett.",
        volume = "60",
        pages = """108""",
        year = "1978",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00015924/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015924/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:35:30 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015924/rk00000002.xml"""),
    ],
)

entry(
    index = 46,
    label = "r00015924",
    reactant1 = 
"""
1 *5 C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3 *2 C 0 {1,S} {6,S}
4 *4 C 0 {2,S} {5,S}
5 *1 O 1 {4,S}
6 *3 H 0 {3,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2 *4 C 0 {1,S} {4,S}
3 *5 C 0 {1,S} {5,S}
4 *1 C 1 {2,S}
5 *2 O 0 {3,S} {6,S}
6 *3 H 0 {5,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.78e+11,"s^-1"),
        n = 0,
        Ea = (33341,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Morabito, P.", "Heicklen, J."],
        title = u'The reactions of alkoxyl radicals with O_2. IV. n-C_4H_9O radicals',
        journal = "Bull. Chem. Soc. Jpn.",
        volume = "60",
        pages = """2641""",
        year = "1987",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00015924/rk00000003.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015924/rk00000003.xml
""",
    history = [
        ("Tue May 17 14:35:30 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015924/rk00000003.xml"""),
    ],
)

entry(
    index = 47,
    label = "r00015924",
    reactant1 = 
"""
1 *5 C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3 *2 C 0 {1,S} {6,S}
4 *4 C 0 {2,S} {5,S}
5 *1 O 1 {4,S}
6 *3 H 0 {3,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2 *4 C 0 {1,S} {4,S}
3 *5 C 0 {1,S} {5,S}
4 *1 C 1 {2,S}
5 *2 O 0 {3,S} {6,S}
6 *3 H 0 {5,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.5e+12,"s^-1"),
        n = 0,
        Ea = (160.269,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Mereau, R.", "Rayez, M.T.", "Caralp, F.", "Rayez, J.C."],
        title = u'Isomerization reactions of alkoxy radicals: theoretical study and structure-activity relationships',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "5",
        pages = """4828-4833""",
        year = "2003",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00015924/rk00000005.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015924/rk00000005.xml
""",
    history = [
        ("Tue May 17 14:35:30 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015924/rk00000005.xml"""),
    ],
)

entry(
    index = 48,
    label = "r00015924",
    reactant1 = 
"""
1 *5 C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3 *2 C 0 {1,S} {6,S}
4 *4 C 0 {2,S} {5,S}
5 *1 O 1 {4,S}
6 *3 H 0 {3,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2 *4 C 0 {1,S} {4,S}
3 *5 C 0 {1,S} {5,S}
4 *1 C 1 {2,S}
5 *2 O 0 {3,S} {6,S}
6 *3 H 0 {5,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.43e+11,"s^-1"),
        n = 0,
        Ea = (134.989,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Vereecken, L.", "Peeters, J."],
        title = u'The 1,5-H-shift in 1-butoxy: A case study in the rigorous implementation of transition state theory for a multirotamer system',
        journal = "J. Chem. Phys.",
        volume = "119",
        pages = """5159-5170""",
        year = "2003",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00015924/rk00000010.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015924/rk00000010.xml
""",
    history = [
        ("Tue May 17 14:35:30 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015924/rk00000010.xml"""),
    ],
)

entry(
    index = 53,
    label = "r00016683",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S} {5,S}
4 *2 C 0 {2,S} {6,S} {7,S}
5    O 0 {3,S}
6 *1 O 1 {4,S}
7 *3 H 0 {4,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S} {5,S}
4 *1 C 1 {2,S} {6,S}
5    O 0 {3,S}
6 *2 O 0 {4,S} {7,S}
7 *3 H 0 {6,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.58e+11,"s^-1"),
        n = 0,
        Ea = (27188.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Baldwin, A.C.", "Barker, J.R.", "Golden, D.M.", "Hendry, D.G."],
        title = u'Photochemical smog. Rate parameter estimates and computer simulations',
        journal = "J. Phys. Chem.",
        volume = "81",
        pages = """2483""",
        year = "1977",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016683/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016683/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:53 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016683/rk00000001.xml"""),
    ],
)

entry(
    index = 54,
    label = "r00017030",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S} {6,S}
4    C 0 {2,S} {8,S}
5 *2 C 0 {7,S} {8,S} {9,S}
6    C 0 {3,S}
7    C 0 {5,S}
8 *1 C 1 {4,S} {5,S}
9 *3 H 0 {5,S}
""",
    product1 = 
"""
1    C 0 {2,S} {4,S}
2    C 0 {1,S} {3,S}
3    C 0 {2,S} {5,S}
4    C 0 {1,S} {6,S}
5 *2 C 0 {3,S} {8,S} {9,S}
6    C 0 {4,S}
7    C 0 {8,S}
8 *1 C 1 {5,S} {7,S}
9 *3 H 0 {5,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.51e+09,"s^-1"),
        n = 0,
        Ea = (46893.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Dobe, S.", "Berces, T.", "Reti, F.", "Marta, F."],
        title = u'Isomerization of n-hexyl and s-octyl radicals by 1,5 and 1,4 intramolecular hydrogen atom transfer reactions',
        journal = "Int. J. Chem. Kinet.",
        volume = "19",
        pages = """895""",
        year = "1987",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00017030/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00017030/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:36:11 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00017030/rk00000001.xml"""),
    ],
)

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

entry(
    index = 57,
    label = "r00017157",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2 *5 C 0 {1,S} {4,S}
3 *4 C 0 {1,S} {5,S} {6,S}
4 *2 C 0 {2,S} {7,S}
5    C 0 {3,S}
6 *1 O 1 {3,S}
7 *3 H 0 {4,S}
""",
    product1 = 
"""
1 *5 C 0 {2,S} {4,S} {6,S}
2    C 0 {1,S} {3,S}
3 *4 C 0 {2,S} {5,S}
4    C 0 {1,S}
5 *1 C 1 {3,S}
6 *2 O 0 {1,S} {7,S}
7 *3 H 0 {6,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.4e+12,"s^-1"),
        n = 0,
        Ea = (153.66,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Mereau, R.", "Rayez, M.T.", "Caralp, F.", "Rayez, J.C."],
        title = u'Isomerization reactions of alkoxy radicals: theoretical study and structure-activity relationships',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "5",
        pages = """4828-4833""",
        year = "2003",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00017157/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00017157/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:36:12 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00017157/rk00000001.xml"""),
    ],
)

entry(
    index = 58,
    label = "r00017157",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2 *5 C 0 {1,S} {4,S}
3 *4 C 0 {1,S} {5,S} {6,S}
4 *2 C 0 {2,S} {7,S}
5    C 0 {3,S}
6 *1 O 1 {3,S}
7 *3 H 0 {4,S}
""",
    product1 = 
"""
1 *5 C 0 {2,S} {4,S} {6,S}
2    C 0 {1,S} {3,S}
3 *4 C 0 {2,S} {5,S}
4    C 0 {1,S}
5 *1 C 1 {3,S}
6 *2 O 0 {1,S} {7,S}
7 *3 H 0 {6,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.26e+11,"s^-1"),
        n = 0,
        Ea = (39743.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Dobe, S.", "Berces, T.", "Marta, F."],
        title = u'Gas phase decomposition and isomerization reactions of 2-pentoxy radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "18",
        pages = """329""",
        year = "1986",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00017157/rk00000005.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00017157/rk00000005.xml
""",
    history = [
        ("Tue May 17 14:36:12 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00017157/rk00000005.xml"""),
    ],
)

