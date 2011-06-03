#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_Endocyclic"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 1,
    label = "r00011188",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *3 C     0 {1,S} {3,S}
3  *2 C     1 {1,S} {2,S}
""",
    product1 = 
"""
1  *2 C     0 {2,S} {3,D}
2  *1 C     1 {1,S}
3  *3 C     0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+13,"s^-1"),
        n = 0,
        Ea = (92290.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Greig, G.", "Thynne, J.C.J."], title=u'Reactions of cyclic akyl radicals. Part 2.-Photolysis of cyclopropane carboxaldehyde', journal="Trans. Faraday Soc.", volume="63", pages="""1367""", year="1967", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:45 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 2,
    label = "r00011188",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *3 C     0 {1,S} {3,S}
3  *2 C     1 {1,S} {2,S}
""",
    product1 = 
"""
1  *2 C     0 {2,S} {3,D}
2  *1 C     1 {1,S}
3  *3 C     0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.51e+10,"s^-1"),
        n = 0,
        Ea = (79902.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kerr, J.A.", "Smith, A.", "Trotman-Dickenson, A.F."], title=u'Reactions of cyclopropyl radicals in the methyl-initiated decomposition of cyclopropanecarbaldehyde', journal="J. Chem. Soc. A", pages="""1400""", year="1969", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:45 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 3,
    label = "r00012751",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *4 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {4,S}
4  *2 C     1 {2,S} {3,S}
""",
    product1 = 
"""
1  *4 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,D}
3  *1 C     1 {1,S}
4  *3 C     0 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.1e+10,"s^-1"),
        n = 0.79,
        Ea = (427.935,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Matheu, D.M.", "Green, W.H.", "Grenda, J.M."], title=u'Capturing pressure-dependence in automated mechanism generation: Reactions through cycloalkyl intermediates', journal="Int. J. Chem. Kinet.", volume="35", pages="""95-119""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:57 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 4,
    label = "r00013098",
    reactant1 = 
"""
1  *5 C     0 {2,S} {3,S}
2  *4 C     0 {1,S} {4,S}
3  *2 C     0 {1,S} {5,D}
4  *1 C     1 {2,S}
5  *3 C     0 {3,D}
""",
    product1 = 
"""
1  *4 C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S}
3  *5 C     0 {1,S} {5,S}
4  *3 C     0 {2,S} {5,S}
5  *2 C     1 {3,S} {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.41e+11,"s^-1"),
        n = 0,
        Ea = (67762.9,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Gierczak, T.", "Gawlowski, J.", "Niedzielski, J."], title=u'Mutual isomerization of cyclopentyl and 1-penten-5-yl radicals', journal="Int. J. Chem. Kinet.", volume="18", pages="""623-637""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:12 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 5,
    label = "r00013098",
    reactant1 = 
"""
1  *5 C     0 {2,S} {3,S}
2  *4 C     0 {1,S} {4,S}
3  *2 C     0 {1,S} {5,D}
4  *1 C     1 {2,S}
5  *3 C     0 {3,D}
""",
    product1 = 
"""
1  *4 C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S}
3  *5 C     0 {1,S} {5,S}
4  *3 C     0 {2,S} {5,S}
5  *2 C     1 {3,S} {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+08,"s^-1"),
        n = 1.05,
        Ea = (261.057,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Matheu, D.M.", "Green, W.H.", "Grenda, J.M."], title=u'Capturing pressure-dependence in automated mechanism generation: Reactions through cycloalkyl intermediates', journal="Int. J. Chem. Kinet.", volume="35", pages="""95-119""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:12 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 6,
    label = "r00013098",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *4 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,S}
4  *5 C     0 {2,S} {5,S}
5  *2 C     1 {3,S} {4,S}
""",
    product1 = 
"""
1  *5 C     0 {2,S} {3,S}
2  *4 C     0 {1,S} {4,S}
3  *2 C     0 {1,S} {5,D}
4  *1 C     1 {2,S}
5  *3 C     0 {3,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.38e+14,"s^-1"),
        n = 0,
        Ea = (133863,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Gierczak, T.", "Gawlowski, J.", "Niedzielski, J."], title=u'Mutual isomerization of cyclopentyl and 1-penten-5-yl radicals', journal="Int. J. Chem. Kinet.", volume="18", pages="""623-637""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:12 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 7,
    label = "r00013098",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *4 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,S}
4  *5 C     0 {2,S} {5,S}
5  *2 C     1 {3,S} {4,S}
""",
    product1 = 
"""
1  *5 C     0 {2,S} {3,S}
2  *4 C     0 {1,S} {4,S}
3  *2 C     0 {1,S} {5,D}
4  *1 C     1 {2,S}
5  *3 C     0 {3,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.38e+13,"s^-1"),
        n = 0,
        Ea = (143840,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Handford-Styring, S.M.", "Walker, R.W."], title=u'Addition of cyclopentane to slowly reacting mixtures of H_2 + O_2 between 673 and 783 K: reactions of H and OH with cyclopentane and of cyclopentyl radicals', journal="J. Chem. Soc. Faraday Trans.", volume="91", pages="""1431-1438""", year="1995", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:12 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 8,
    label = "r00015692",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2  *5 C     0 {1,S} {4,S}
3  *4 C     0 {1,S} {5,S}
4  *2 C     0 {2,S} {6,D}
5  *1 C     1 {3,S}
6  *3 C     0 {4,D}
""",
    product1 = 
"""
1  *4 C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *1 C     0 {1,S} {5,S}
4  *5 C     0 {2,S} {6,S}
5  *3 C     0 {3,S} {6,S}
6  *2 C     1 {4,S} {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+10,"s^-1"),
        n = 0,
        Ea = (35003.9,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Handford-Styring, S.M.", "Walker, R.W."], title=u'Addition of cyclopentane to slowly reacting mixtures of H_2 + O_2 between 673 and 783 K: reactions of H and OH with cyclopentane and of cyclopentyl radicals', journal="J. Chem. Soc. Faraday Trans.", volume="91", pages="""1431-1438""", year="1995", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:26 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 9,
    label = "r00015692",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2  *5 C     0 {1,S} {4,S}
3  *4 C     0 {1,S} {5,S}
4  *2 C     0 {2,S} {6,D}
5  *1 C     1 {3,S}
6  *3 C     0 {4,D}
""",
    product1 = 
"""
1  *4 C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *1 C     0 {1,S} {5,S}
4  *5 C     0 {2,S} {6,S}
5  *3 C     0 {3,S} {6,S}
6  *2 C     1 {4,S} {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+08,"s^-1"),
        n = 0.86,
        Ea = (97.4832,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Matheu, D.M.", "Green, W.H.", "Grenda, J.M."], title=u'Capturing pressure-dependence in automated mechanism generation: Reactions through cycloalkyl intermediates', journal="Int. J. Chem. Kinet.", volume="35", pages="""95-119""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:26 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 10,
    label = "r00017190",
    reactant1 = 
"""
1  *3 C     0 {2,S} {4,S}
2  *1 C     0 {1,S} {3,B} {5,B}
3  *4 C     0 {2,B} {4,S} {6,B}
4  *2 C     1 {1,S} {3,S}
5     C     0 {2,B} {8,B}
6     C     0 {3,B} {7,B}
7     C     0 {6,B} {8,B}
8     C     0 {5,B} {7,B}
""",
    product1 = 
"""
1  *4 C     0 {2,B} {4,S} {8,B}
2     C     0 {1,B} {3,B}
3     C     0 {2,B} {5,B}
4  *2 C     0 {1,S} {7,D}
5     C     0 {3,B} {6,B}
6     C     0 {5,B} {8,B}
7  *3 C     0 {4,D}
8  *1 C     1 {1,B} {6,B}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.91e+12,"s^-1"),
        n = 0.26,
        Ea = (624.223,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tokmakov, I.V.", "Lin, M.C."], title=u'Reaction of phenyl radicals with acetylene: Quantum chemical investigation of the mechanism and master equation analysis of the kinetics', journal="J. Am. Chem. Soc.", volume="125", pages="""11397-11408""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:36:12 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

