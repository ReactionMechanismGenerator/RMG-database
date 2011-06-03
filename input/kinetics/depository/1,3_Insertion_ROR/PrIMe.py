#!/usr/bin/env python
# encoding: utf-8

name = "1,3_Insertion_ROR"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 1,
    label = "r00001556",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {10,S}
2  *2 C     0 {1,S} {9,S}
3     C     0 {1,S} {4,B} {5,B}
4     C     0 {3,B} {7,B}
5     C     0 {3,B} {8,B}
6     C     0 {7,B} {8,B}
7     C     0 {4,B} {6,B}
8     C     0 {5,B} {6,B}
9  *4 O     0 {2,S}
10 *3 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,B} {3,B} {4,S}
2     C     0 {1,B} {6,B}
3     C     0 {1,B} {7,B}
4  *1 C     0 {1,S} {8,D}
5     C     0 {6,B} {7,B}
6     C     0 {2,B} {5,B}
7     C     0 {3,B} {5,B}
8  *2 C     0 {4,D}
""",
    product2 = 
"""
1  *4 O     0 {2,S}
2  *3 H     0 {1,S}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (2.5e+12,"s^-1"),
        n = 0,
        Ea = (3786.97,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Chuchani, G.", "Rotinov, A.", "Dominguez, R.M."], title=u'The kinetics and mechanisms of gas phase elimination of primary, secondary, and tertiary 2-hydroxyalkylbenzenes', journal="Int. J. Chem. Kinet.", volume="31", pages="""401-407""", year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 2,
    label = "r00001557",
    reactant1 = 
"""
1  *2 C     0 {3,S} {5,S}
2     C     0 {4,S} {5,S}
3  *1 C     0 {1,S} {6,S}
4     C     0 {2,S}
5  *4 O     0 {1,S} {2,S}
6  *3 H     0 {3,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *4 O     0 {1,S} {4,S}
4  *3 H     0 {3,S}
""",
    degeneracy = 24,
    kinetics = Arrhenius(
        A = (2.75e+18,"s^-1"),
        n = 0,
        Ea = (350871,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Laidler, K.J.", "McKenney, D.J."], title=u'Kinetics and mechanisms of the pyrolysis of diethyl ether. II. The reaction inhibited by nitric oxide', journal="Proc. R. Soc. London", volume="278", pages="""517-526""", year="1964", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 3,
    label = "r00001557",
    reactant1 = 
"""
1  *2 C     0 {3,S} {5,S}
2     C     0 {4,S} {5,S}
3  *1 C     0 {1,S} {6,S}
4     C     0 {2,S}
5  *4 O     0 {1,S} {2,S}
6  *3 H     0 {3,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *4 O     0 {1,S} {4,S}
4  *3 H     0 {3,S}
""",
    degeneracy = 24,
    kinetics = Arrhenius(
        A = (7.94e+13,"s^-1"),
        n = 0,
        Ea = (276040,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Seres, I.", "Huhn, P."], title=u'A dietil-eter termikus bomlasa, III.', journal="Magy. Kem. Foly.", volume="81", pages="""120-123""", year="1975", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 4,
    label = "r00001557",
    reactant1 = 
"""
1  *2 C     0 {3,S} {5,S}
2     C     0 {4,S} {5,S}
3  *1 C     0 {1,S} {6,S}
4     C     0 {2,S}
5  *4 O     0 {1,S} {2,S}
6  *3 H     0 {3,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *4 O     0 {1,S} {4,S}
4  *3 H     0 {3,S}
""",
    degeneracy = 24,
    kinetics = Arrhenius(
        A = (1e+13,"s^-1"),
        n = 0,
        Ea = (260243,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Foucaut, J.-F.", "Martin, R."], title=u"No. 18. - Etude analytique et cinetique de la pyrolyse de l'ether ethylique vers 500 \xb0C et a faible avancement", journal="J. Chim. Phys.", volume="75", pages="""132""", year="1978", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 5,
    label = "r00001601",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S}
3  *4 O     0 {1,S}
4  *3 H     0 {2,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1  *4 O     0 {2,S}
2  *3 H     0 {1,S}
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (4.66e+13,"s^-1"),
        n = 0.09,
        Ea = (276872,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Marinov, N.M."], title=u'A detailed chemical kinetic model for high temperature ethanol oxidation', journal="Int. J. Chem. Kinet.", volume="31", pages="""183-220""", year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 6,
    label = "r00001601",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S}
3  *4 O     0 {1,S}
4  *3 H     0 {2,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1  *4 O     0 {2,S}
2  *3 H     0 {1,S}
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (7.67e+14,"s^-1"),
        n = 0,
        Ea = (1067.52,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Rajakumar, B.", "Reddy, K.P.J.", "Arunan, E."], title=u'Thermal decomposition of 2-fluoroethanol:  Single pulse shock tube and ab initio studies', journal="J. Phys. Chem. A", volume="107", pages="""9782-9793""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 7,
    label = "r00001646",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S}
2  *2 C     0 {1,S} {3,S} {5,D}
3  *4 O     0 {2,S}
4  *3 H     0 {1,S}
5     O     0 {2,D}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    product2 = 
"""
1  *4 O     0 {2,S}
2  *3 H     0 {1,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (8.99e+12,"s^-1"),
        n = 0,
        Ea = (282692,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Bamford, C.H.", "Dewar, M.J.S."], title=u'608. The thermal decomposition of acetic acid', journal="J. Chem. Soc.", pages="""2877-2882""", year="1949", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 8,
    label = "r00001646",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S}
2  *2 C     0 {1,S} {3,S} {5,D}
3  *4 O     0 {2,S}
4  *3 H     0 {1,S}
5     O     0 {2,D}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    product2 = 
"""
1  *4 O     0 {2,S}
2  *3 H     0 {1,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.82e+12,"s^-1"),
        n = 0,
        Ea = (271883,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Blake, P.G.", "Jackson, G.E."], title=u'High- and low-temperature mechanisms in the thermal decomposition of acetic acid', journal="J. Chem. Soc. B", pages="""94-96""", year="1969", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 9,
    label = "r00001646",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S}
2  *2 C     0 {1,S} {3,S} {5,D}
3  *4 O     0 {2,S}
4  *3 H     0 {1,S}
5     O     0 {2,D}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    product2 = 
"""
1  *4 O     0 {2,S}
2  *3 H     0 {1,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.26e+13,"s^-1"),
        n = 0,
        Ea = (304310,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Mackie, J.C.", "Doolan, K.R."], title=u'High-temperature kinetics of thermal decomposition of acetic acid and its products', journal="Int. J. Chem. Kinet.", volume="16", pages="""525""", year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 10,
    label = "r00001646",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S}
2  *2 C     0 {1,S} {3,S} {5,D}
3  *4 O     0 {2,S}
4  *3 H     0 {1,S}
5     O     0 {2,D}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    product2 = 
"""
1  *4 O     0 {2,S}
2  *3 H     0 {1,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (5.25e+12,"s^-1"),
        n = 0,
        Ea = (295164,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Mackie, J.C.", "Doolan, K.R."], title=u'High-temperature kinetics of thermal decomposition of acetic acid and its products', journal="Int. J. Chem. Kinet.", volume="16", pages="""525""", year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 11,
    label = "r00001646",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S}
2  *2 C     0 {1,S} {3,S} {5,D}
3  *4 O     0 {2,S}
4  *3 H     0 {1,S}
5     O     0 {2,D}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    product2 = 
"""
1  *4 O     0 {2,S}
2  *3 H     0 {1,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (4.47e+14,"s^-1"),
        n = 0,
        Ea = (334242,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Duan, X.", "Page, M."], title=u'Theoretical investigation of competing mechanisms in the thermal unimolecular decomposition of acetic acid and the hydration reaction of ketene', journal="J. Am. Chem. Soc.", volume="117", pages="""5114-5119""", year="1995", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 12,
    label = "r00001741",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S}
2  *1 C     0 {1,S} {5,S}
3     C     0 {1,S}
4  *4 O     0 {1,S}
5  *3 H     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    product2 = 
"""
1  *4 O     0 {2,S}
2  *3 H     0 {1,S}
""",
    degeneracy = 24,
    kinetics = Arrhenius(
        A = (1.26e+13,"s^-1"),
        n = 0,
        Ea = (243614,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Trenwith, A.B."], title=u'Thermal Decomposition of Isopropanol', journal="J. Chem. Soc. Faraday Trans. 1", volume="71", pages="""2405""", year="1975", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 13,
    label = "r00001741",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S}
2  *1 C     0 {1,S} {5,S}
3     C     0 {1,S}
4  *4 O     0 {1,S}
5  *3 H     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    product2 = 
"""
1  *4 O     0 {2,S}
2  *3 H     0 {1,S}
""",
    degeneracy = 24,
    kinetics = Arrhenius(
        A = (1.6e+51,"s^-1"),
        n = -11.46,
        Ea = (336096,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Bui, B.H.", "Zhu, R.S.", "Lin, M.C."], title=u'Thermal Decomposition of Iso-Propanol:  First-Principles Prediction of Total and Product-Branching Rate Constants', journal="J. Chem. Phys.", volume="117", pages="""11188-11195""", year="2002", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 14,
    label = "r00001741",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S}
2  *1 C     0 {1,S} {5,S}
3     C     0 {1,S}
4  *4 O     0 {1,S}
5  *3 H     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    product2 = 
"""
1  *4 O     0 {2,S}
2  *3 H     0 {1,S}
""",
    degeneracy = 24,
    kinetics = Arrhenius(
        A = (6.1e+43,"s^-1"),
        n = -9.13,
        Ea = (325811,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Bui, B.H.", "Zhu, R.S.", "Lin, M.C."], title=u'Thermal Decomposition of Iso-Propanol:  First-Principles Prediction of Total and Product-Branching Rate Constants', journal="J. Chem. Phys.", volume="117", pages="""11188-11195""", year="2002", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 15,
    label = "r00001741",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S}
2  *1 C     0 {1,S} {5,S}
3     C     0 {1,S}
4  *4 O     0 {1,S}
5  *3 H     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    product2 = 
"""
1  *4 O     0 {2,S}
2  *3 H     0 {1,S}
""",
    degeneracy = 24,
    kinetics = Arrhenius(
        A = (2e+06,"s^-1"),
        n = 2.12,
        Ea = (254980,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Bui, B.H.", "Zhu, R.S.", "Lin, M.C."], title=u'Thermal Decomposition of Iso-Propanol:  First-Principles Prediction of Total and Product-Branching Rate Constants', journal="J. Chem. Phys.", volume="117", pages="""11188-11195""", year="2002", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 16,
    label = "r00003587",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S} {5,S}
2  *1 C     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *4 O     0 {1,S}
6  *3 H     0 {2,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *2 C     0 {1,S} {2,S} {4,D}
4  *1 C     0 {3,D}
""",
    product2 = 
"""
1  *4 O     0 {2,S}
2  *3 H     0 {1,S}
""",
    degeneracy = 36,
    kinetics = Arrhenius(
        A = (3.24e+11,"s^-1"),
        n = 0,
        Ea = (227817,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Barnard, J.A."], title=u'The pyrolysis of tert-butanol', journal="Trans. Faraday Soc.", volume="55", pages="""947-951""", year="1959", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:37 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 17,
    label = "r00003587",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S} {5,S}
2  *1 C     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *4 O     0 {1,S}
6  *3 H     0 {2,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *2 C     0 {1,S} {2,S} {4,D}
4  *1 C     0 {3,D}
""",
    product2 = 
"""
1  *4 O     0 {2,S}
2  *3 H     0 {1,S}
""",
    degeneracy = 36,
    kinetics = Arrhenius(
        A = (2.51e+13,"s^-1"),
        n = 0,
        Ea = (257749,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Thermal decomposition of some tert-butyl compounds at elevated temperatures', journal="J. Chem. Phys.", volume="40", pages="""1498-1505""", year="1964", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:37 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 18,
    label = "r00003587",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S} {5,S}
2  *1 C     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *4 O     0 {1,S}
6  *3 H     0 {2,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *2 C     0 {1,S} {2,S} {4,D}
4  *1 C     0 {3,D}
""",
    product2 = 
"""
1  *4 O     0 {2,S}
2  *3 H     0 {1,S}
""",
    degeneracy = 36,
    kinetics = Arrhenius(
        A = (2.24e+13,"s^-1"),
        n = 0,
        Ea = (252760,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dorko, E.A.", "McGhee, D.B.", "Painter, C.E.", "Caponecchi, A.J.", "Crossley, R.W."], title=u'Shock Tube Isomerization of Cyclopropane', journal="J. Phys. Chem.", volume="75", pages="""2526""", year="1971", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:37 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 19,
    label = "r00003587",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S} {5,S}
2  *1 C     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *4 O     0 {1,S}
6  *3 H     0 {2,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *2 C     0 {1,S} {2,S} {4,D}
4  *1 C     0 {3,D}
""",
    product2 = 
"""
1  *4 O     0 {2,S}
2  *3 H     0 {1,S}
""",
    degeneracy = 36,
    kinetics = Arrhenius(
        A = (250000,"s^-1"),
        n = 0,
        Ea = (125549,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Gonzalez, M.G.", "Lew, L.", "Cunningham, R.E."], title=u'Determinacion de la Cinetica de Descomposicion Termica de Alcoholes e Hidrocarburos Mediante un Reactor Pulso', journal="Lab. Ensayo Mater. Invest. Tecnol. Prov. Buenos Aires Publ. Ser. 2", pages="""103-123""", year="1971", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:37 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 20,
    label = "r00003587",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S} {5,S}
2  *1 C     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *4 O     0 {1,S}
6  *3 H     0 {2,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *2 C     0 {1,S} {2,S} {4,D}
4  *1 C     0 {3,D}
""",
    product2 = 
"""
1  *4 O     0 {2,S}
2  *3 H     0 {1,S}
""",
    degeneracy = 36,
    kinetics = Arrhenius(
        A = (3.98e+14,"s^-1"),
        n = 0,
        Ea = (276872,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Lewis, D.", "Keil, M.", "Sarr, M."], title=u'Gas Phase Thermal Decomposition of tert-Butyl Alcohol', journal="J. Am. Chem. Soc.", volume="96", pages="""4398""", year="1974", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000008.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:37 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 21,
    label = "r00003587",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S} {5,S}
2  *1 C     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *4 O     0 {1,S}
6  *3 H     0 {2,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *2 C     0 {1,S} {2,S} {4,D}
4  *1 C     0 {3,D}
""",
    product2 = 
"""
1  *4 O     0 {2,S}
2  *3 H     0 {1,S}
""",
    degeneracy = 36,
    kinetics = Arrhenius(
        A = (7.76e+14,"s^-1"),
        n = 0,
        Ea = (275209,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Newman, C.G.", "O'Neal, H.E.", "Ring, M.A.", "Leska, F.", "Shipley, N."], title=u'Kinetics and mechanism of the silane decomposition', journal="Int. J. Chem. Kinet.", volume="11", pages="""1167""", year="1979", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000009.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:37 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 22,
    label = "r00005036",
    reactant1 = 
"""
1  *2 C     0 {3,S} {4,S} {7,S}
2     C     0 {5,S} {6,S} {7,S}
3  *1 C     0 {1,S} {8,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     C     0 {2,S}
7  *4 O     0 {1,S} {2,S}
8  *3 H     0 {3,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *4 O     0 {1,S} {5,S}
5  *3 H     0 {4,S}
""",
    degeneracy = 48,
    kinetics = Arrhenius(
        A = (4.17e+14,"s^-1"),
        n = 0,
        Ea = (266063,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Daly, N.J.", "Stimson, V.R."], title=u'The thermal decomposition of diisopropyl ether', journal="Aust. J. Chem.", volume="19", pages="""239-250""", year="1966", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:49 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 23,
    label = "r00006952",
    reactant1 = 
"""
1  *2 C     0 {3,S} {6,S}
2     C     0 {4,S} {7,S}
3  *1 C     0 {1,S} {8,S}
4     C     0 {2,S}
5     C     0 {6,S} {7,S}
6  *4 O     0 {1,S} {5,S}
7     O     0 {2,S} {5,S}
8  *3 H     0 {3,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1     C     0 {2,S} {4,S}
2     C     0 {1,S}
3     C     0 {4,S} {5,S}
4     O     0 {1,S} {3,S}
5  *4 O     0 {3,S} {6,S}
6  *3 H     0 {5,S}
""",
    degeneracy = 24,
    kinetics = Arrhenius(
        A = (1.17e+15,"s^-1"),
        n = 0,
        Ea = (286849,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Herzler, J.", "Manion, J.A.", "Tsang, W."], title=u'Single-pulse shock tube studies of the decomposition of ethoxy compounds', journal="J. Phys. Chem. A", volume="101", pages="""5494-5499""", year="1997", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:01 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 24,
    label = "r00007088",
    reactant1 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2  *2 C     0 {1,S} {6,S} {7,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6  *1 C     0 {2,S} {8,S}
7  *4 O     0 {2,S}
8  *3 H     0 {6,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *2 C     0 {1,S} {6,D}
6  *1 C     0 {5,D}
""",
    product2 = 
"""
1  *4 O     0 {2,S}
2  *3 H     0 {1,S}
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (1e+14,"s^-1"),
        n = 0,
        Ea = (284355,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Thermal Stability of Alcohols', journal="Int. J. Chem. Kinet.", volume="8", pages="""173""", year="1976", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:02 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 25,
    label = "r00007803",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S} {6,S}
2  *2 C     0 {1,S} {5,S}
3     C     0 {4,S}
4     C     0 {1,S} {3,S} {7,D}
5  *4 O     0 {2,S}
6  *3 H     0 {1,S}
7     O     0 {4,D}
""",
    product1 = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S} {5,D}
3  *1 C     0 {2,S} {4,D}
4  *2 C     0 {3,D}
5     O     0 {2,D}
""",
    product2 = 
"""
1  *4 O     0 {2,S}
2  *3 H     0 {1,S}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (2.24e+12,"s^-1"),
        n = 0,
        Ea = (155481,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Rotinov, A.", "Chuchani, G.", "Machado, R.A.", "Rivas, C."], title=u'The retro-aldol mechanism in the pyrolysis kinetics of primary, secondary, and tertiary \u03b2-hydroxy ketones in the gas phase', journal="Int. J. Chem. Kinet.", volume="24", pages="""909-915""", year="1992", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:10 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 26,
    label = "r00008052",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S} {7,S}
2     C     0 {1,S} {5,S} {6,S}
3  *1 C     0 {1,S} {8,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     C     0 {2,S}
7  *4 O     0 {1,S}
8  *3 H     0 {3,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {5,S}
5  *2 C     0 {1,S} {4,S} {6,D}
6  *1 C     0 {5,D}
""",
    product2 = 
"""
1  *4 O     0 {2,S}
2  *3 H     0 {1,S}
""",
    degeneracy = 24,
    kinetics = Arrhenius(
        A = (1.48e+14,"s^-1"),
        n = 0,
        Ea = (268557,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Thermal Stability of Alcohols', journal="Int. J. Chem. Kinet.", volume="8", pages="""173""", year="1976", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:11 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 27,
    label = "r00008053",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S} {7,S}
2  *1 C     0 {1,S} {5,S} {6,S} {8,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     C     0 {2,S}
7  *4 O     0 {1,S}
8  *3 H     0 {2,S}
""",
    product1 = 
"""
1     C     0 {5,S}
2     C     0 {5,S}
3     C     0 {6,S}
4     C     0 {6,S}
5  *2 C     0 {1,S} {2,S} {6,D}
6  *1 C     0 {3,S} {4,S} {5,D}
""",
    product2 = 
"""
1  *4 O     0 {2,S}
2  *3 H     0 {1,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (4.57e+13,"s^-1"),
        n = 0,
        Ea = (271883,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Thermal Stability of Alcohols', journal="Int. J. Chem. Kinet.", volume="8", pages="""173""", year="1976", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:11 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 28,
    label = "r00008094",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {5,S}
2  *1 C     0 {1,S} {6,S}
3     C     0 {1,S} {4,D}
4     C     0 {3,D}
5  *4 O     0 {1,S}
6  *3 H     0 {2,S}
""",
    product1 = 
"""
1  *2 C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3  *1 C     0 {1,D}
4     C     0 {2,D}
""",
    product2 = 
"""
1  *4 O     0 {2,S}
2  *3 H     0 {1,S}
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (7.94e+12,"s^-1"),
        n = 0,
        Ea = (232805,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Trenwith, A.B."], title=u'Dissociation of 3-Hydroxybut-1-ene and the Resonance Energy of the Hydroxyallyl Radical', journal="J. Chem. Soc. Faraday Trans. 1", volume="69", pages="""1737""", year="1973", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:12 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 29,
    label = "r00008622",
    reactant1 = 
"""
1  *2 C     0 {3,S} {4,S} {5,S} {7,S}
2     C     0 {6,S} {7,S}
3  *1 C     0 {1,S} {8,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7  *4 O     0 {1,S} {2,S}
8  *3 H     0 {3,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *2 C     0 {1,S} {2,S} {4,D}
4  *1 C     0 {3,D}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *4 O     0 {1,S} {4,S}
4  *3 H     0 {3,S}
""",
    degeneracy = 36,
    kinetics = Arrhenius(
        A = (1.15e+14,"s^-1"),
        n = 0,
        Ea = (248603,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Daly, N.J.", "Wentrup, C."], title=u'The thermal decomposition of t-butyl ethyl ether', journal="Aust. J. Chem.", volume="21", pages="""1535""", year="1968", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:16 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 30,
    label = "r00009888",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S} {6,S}
2  *1 C     0 {1,S} {7,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {6,S}
6  *4 O     0 {1,S} {5,S}
7  *3 H     0 {2,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *2 C     0 {1,S} {2,S} {4,D}
4  *1 C     0 {3,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *4 O     0 {1,S} {3,S}
3  *3 H     0 {2,S}
""",
    degeneracy = 36,
    kinetics = Arrhenius(
        A = (2.23e+14,"s^-1"),
        n = 0,
        Ea = (255254,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Daly, N.J.", "Wentrup, C."], title=u'The thermal decomposition of t-butyl methyl ether', journal="Aust. J. Chem.", volume="21", pages="""2711-2716""", year="1968", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:29 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 31,
    label = "r00009888",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S} {6,S}
2  *1 C     0 {1,S} {7,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {6,S}
6  *4 O     0 {1,S} {5,S}
7  *3 H     0 {2,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *2 C     0 {1,S} {2,S} {4,D}
4  *1 C     0 {3,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *4 O     0 {1,S} {3,S}
3  *3 H     0 {2,S}
""",
    degeneracy = 36,
    kinetics = Arrhenius(
        A = (7.94e+13,"s^-1"),
        n = 0,
        Ea = (246940,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Choo, K-Y.", "Golden, D.M.", "Benson, S.W."], title=u'Very Low-Pressure Pyrolysis (VLPP) of t-Butylmethyl Ether', journal="Int. J. Chem. Kinet.", volume="6", pages="""631""", year="1974", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:29 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 32,
    label = "r00009888",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S} {6,S}
2  *1 C     0 {1,S} {7,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {6,S}
6  *4 O     0 {1,S} {5,S}
7  *3 H     0 {2,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *2 C     0 {1,S} {2,S} {4,D}
4  *1 C     0 {3,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *4 O     0 {1,S} {3,S}
3  *3 H     0 {2,S}
""",
    degeneracy = 36,
    kinetics = Arrhenius(
        A = (1e+14,"s^-1"),
        n = 0,
        Ea = (249434,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Brocard, J.C.", "Baronnet, F."], title=u'Pyrolysis of methyl tert-butyl ether', journal="Oxid. Commun.", volume="1", pages="""321""", year="1980", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:29 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 33,
    label = "r00009888",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S} {6,S}
2  *1 C     0 {1,S} {7,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {6,S}
6  *4 O     0 {1,S} {5,S}
7  *3 H     0 {2,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *2 C     0 {1,S} {2,S} {4,D}
4  *1 C     0 {3,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *4 O     0 {1,S} {3,S}
3  *3 H     0 {2,S}
""",
    degeneracy = 36,
    kinetics = Arrhenius(
        A = (7.94e+13,"s^-1"),
        n = 0,
        Ea = (246940,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Brocard, J.C.", "Baronnet, F."], title=u'Effets de parois dans la pyrolyse du methyl tert-butyl ether (MTBE)', journal="J. Chim. Phys. Phys. Chim. Biol.", volume="84", pages="""19""", year="1987", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:29 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 34,
    label = "r00015783",
    reactant1 = 
"""
1  *2 C     0 {3,S} {4,S} {5,S} {8,S}
2     C     0 {6,S} {7,S} {8,S}
3  *1 C     0 {1,S} {9,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {2,S}
8  *4 O     0 {1,S} {2,S}
9  *3 H     0 {3,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *2 C     0 {1,S} {2,S} {4,D}
4  *1 C     0 {3,D}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *4 O     0 {1,S} {5,S}
5  *3 H     0 {4,S}
""",
    degeneracy = 36,
    kinetics = Arrhenius(
        A = (2.34e+13,"s^-1"),
        n = 0,
        Ea = (231974,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Daly, N.J.", "Ziolkowski, F.J."], title=u'The thermal decomposition of t-butyl isopropyl ether', journal="Aust. J. Chem.", volume="23", pages="""541""", year="1970", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:29 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 35,
    label = "r00015784",
    reactant1 = 
"""
1     C     0 {3,S} {4,S} {5,S} {8,S}
2  *2 C     0 {6,S} {7,S} {8,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6  *1 C     0 {2,S} {9,S}
7     C     0 {2,S}
8  *4 O     0 {1,S} {2,S}
9  *3 H     0 {6,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *4 O     0 {1,S} {6,S}
6  *3 H     0 {5,S}
""",
    degeneracy = 24,
    kinetics = Arrhenius(
        A = (9.12e+12,"s^-1"),
        n = 0,
        Ea = (236131,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Daly, N.J.", "Ziolkowski, F.J."], title=u'The thermal decomposition of t-butyl isopropyl ether', journal="Aust. J. Chem.", volume="23", pages="""541""", year="1970", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:29 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 36,
    label = "r00016319",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {6,S}
2  *1 C     0 {1,S} {8,S}
3     C     0 {1,S}
4     C     0 {5,S} {6,S}
5     C     0 {4,S} {7,S} {9,D}
6  *4 O     0 {1,S} {4,S}
7     O     0 {5,S}
8  *3 H     0 {2,S}
9     O     0 {5,D}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S} {5,D}
3  *4 O     0 {1,S} {6,S}
4     O     0 {2,S}
5     O     0 {2,D}
6  *3 H     0 {3,S}
""",
    degeneracy = 24,
    kinetics = Arrhenius(
        A = (1.12e+12,"s^-1"),
        n = 0,
        Ea = (195390,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Chuchani, G.", "Rotinov, A.", "Dominguez, R.M."], title=u'Elimination kinetics and mechanisms for several 2-alkoxyacetic acids in the gas phase', journal="J. Phys. Org. Chem.", volume="9", pages="""787-794""", year="1996", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:43 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

