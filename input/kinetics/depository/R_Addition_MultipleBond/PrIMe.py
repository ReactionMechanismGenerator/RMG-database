#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_MultipleBond"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 1,
    label = "r00000050",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S}
3  *3 C     0 {1,S} {4,D}
4     C     0 {3,D}
5  *2 O     1 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 O     0 {2,D}
""",
    product2 = 
"""
1     C     0 {2,D}
2  *3 C     1 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.74e+14,"s^-1"),
        n = 0,
        Ea = (1414.33,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."], title=u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds', journal="Can. J. Chem.", volume="81", pages="""431-442""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:23 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 2,
    label = "r00000051",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {5,S} {6,S}
2     C     0 {1,S}
3     C     0 {1,S} {4,D}
4     C     0 {3,D}
5  *2 O     1 {1,S}
6  *3 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,S} {5,D}
3     C     0 {2,S} {4,D}
4     C     0 {3,D}
5  *2 O     0 {2,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.77e+13,"s^-1"),
        n = 0,
        Ea = (1192.93,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."], title=u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds', journal="Can. J. Chem.", volume="81", pages="""431-442""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:23 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 3,
    label = "r00000052",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {5,S}
2  *3 C     0 {1,S}
3     C     0 {1,S} {4,D}
4     C     0 {3,D}
5  *2 O     1 {1,S}
""",
    product1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *1 C     0 {1,S} {4,D}
4  *2 O     0 {3,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.69e+13,"s^-1"),
        n = 0,
        Ea = (837.694,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."], title=u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds', journal="Can. J. Chem.", volume="81", pages="""431-442""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:23 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 4,
    label = "r00001349",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *3 C     1 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S} {4,S}
2  *3 C     0 {1,S} {3,S}
3  *1 C     0 {2,S} {5,S}
4     C     0 {1,S}
5  *2 O     1 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.94e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (28019.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Knoll, H.", "Nacsa, A.", "Foergeteg, S.", "Berces, T."], title=u'Free Radical Additions to the C=O Bond of Formaldehyde', journal="React. Kinet. Catal. Lett.", volume="15", pages="""481""", year="1980", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:30 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 5,
    label = "r00001349",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2  *3 C     0 {1,S} {4,S}
3     C     0 {1,S}
4  *1 C     0 {2,S} {5,S}
5  *2 O     1 {4,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *3 C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.98e+13,"s^-1"),
        n = 0,
        Ea = (79902.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baldwin, A.C.", "Barker, J.R.", "Golden, D.M.", "Hendry, D.G."], title=u'Photochemical smog. Rate parameter estimates and computer simulations', journal="J. Phys. Chem.", volume="81", pages="""2483""", year="1977", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:30 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 6,
    label = "r00001349",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2  *3 C     0 {1,S} {4,S}
3     C     0 {1,S}
4  *1 C     0 {2,S} {5,S}
5  *2 O     1 {4,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *3 C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.98e+13,"s^-1"),
        n = 0,
        Ea = (79902.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baldwin, A.C.", "Golden, D.M."], title=u'Alkoxy Radical Reactions: The Isomerization of n-Butoxy Radicals Generated from the Pyrolysis of n-Butyl Nitrite', journal="Chem. Phys. Lett.", volume="60", pages="""108""", year="1978", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:30 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 7,
    label = "r00002194",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *3 C     1 {1,S} {2,S} {3,S}
""",
    product1 = 
"""
1  *3 C     0 {2,S} {3,S} {4,S} {5,S}
2  *1 C     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6  *2 C     1 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.58e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (29682.7,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Birrell, R.N.", "Trotman-Dickenson, A.F."], title=u'The reactions of alkyl radicals. Part VII. t-butyl radicals from the photolysis of pivalaldehyde', journal="J. Chem. Soc.", pages="""4218""", year="1960", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 8,
    label = "r00002199",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *3 C     1 {1,S} {2,S}
""",
    product1 = 
"""
1  *3 C     0 {2,S} {3,S} {4,S}
2  *1 C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *2 C     1 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.5e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (28851.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kerr, J.A.", "Trotman-Dickenson, A.F."], title=u'The reactions of alkyl radicals. Part 2. s-Propyl radicals from the photolysis of isobutyraldehyde', journal="Trans. Faraday Soc.", volume="55", pages="""921""", year="1959", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 9,
    label = "r00002199",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *3 C     1 {1,S} {2,S}
""",
    product1 = 
"""
1  *3 C     0 {2,S} {3,S} {4,S}
2  *1 C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *2 C     1 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.66e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (29017.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Watkins, K.W.", "O'Deen, L.A."], title=u'Kinetics of the addition of ethyl, isopropyl, n-butyl, and isopentyl radicals to ethylene', journal="J. Phys. Chem.", volume="73", pages="""4094-4102""", year="1969", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 10,
    label = "r00002210",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *3 C     1 {1,S}
""",
    product1 = 
"""
1  *3 C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *1 C     0 {1,S} {5,S}
4     C     0 {2,S}
5  *2 C     1 {3,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.94e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (27188.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kerr, J.A.", "Trotman-Dickenson, A.F."], title=u'The reactions of alkyl radicals. Part 1.-n-Propyl radicals from the photolysis of n-butyraldehyde', journal="Trans. Faraday Soc.", volume="55", pages="""572""", year="1959", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 11,
    label = "r00002210",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *3 C     1 {1,S}
""",
    product1 = 
"""
1  *3 C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *1 C     0 {1,S} {5,S}
4     C     0 {2,S}
5  *2 C     1 {3,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.41e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (30929.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Watkins, K.W.", "Lawson, D.R."], title=u'Isomerization of Chemically Activated n-Pentyl Radicals', journal="J. Phys. Chem.", volume="75", pages="""1632""", year="1971", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 12,
    label = "r00002218",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1  *3 C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *3 C     0 {1,S}
3  *2 C     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.59e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (32759,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Hogg, A.M.", "Kebarle, P."], title=u'Addition of methyl radicals to vinyl chloride and catalysis of di-t-butyl peroxide decomposition by chlorinated compounds', journal="J. Am. Chem. Soc.", volume="86", pages="""4558-4562""", year="1964", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 13,
    label = "r00002218",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1  *3 C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *3 C     0 {1,S}
3  *2 C     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (33008.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Camilleri, P.", "Marshall, R.M.", "Purnell, H."], title=u'Arrhenius Parameters for the Unimolecular Decompositions of Azomethane and n-Propyl and Isopropyl Radicals and for Methyl Radical Attack on Propane', journal="J. Chem. Soc. Faraday Trans. 1", volume="71", pages="""1491""", year="1975", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 14,
    label = "r00002218",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1  *3 C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *3 C     0 {1,S}
3  *2 C     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.09e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (30514.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Holt, P.M.", "Kerr, J.A."], title=u'Kinetics of Gas-Phase Addition Reactions of Methyl Radicals. I. Addition to Ethylene, Acetylene, and Benzene', journal="Int. J. Chem. Kinet.", volume="9", pages="""185""", year="1977", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 15,
    label = "r00002218",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1  *3 C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *3 C     0 {1,S}
3  *2 C     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.31e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (32260.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W.", "Hampson, R.F."], title=u'Chemical kinetic data base for combustion chemistry. Part I. Methane and related compounds', journal="J. Phys. Chem. Ref. Data", volume="15", pages="""1087""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000009.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 16,
    label = "r00002218",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1  *3 C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *3 C     0 {1,S}
3  *2 C     1 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.11e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (30763.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Esser, C.", "Frank, P.", "Just, Th.", "Kerr, J.A.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."], title=u'Evaluated kinetic data for combustion modelling', journal="J. Phys. Chem. Ref. Data", volume="21", pages="""411-429""", year="1992", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000010.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 17,
    label = "r00002223",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *3 C     1 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S} {5,S} {6,S}
2     C     0 {1,S} {3,S}
3  *3 C     0 {2,S} {4,S}
4  *1 C     0 {3,S} {7,S}
5     C     0 {1,S}
6     C     0 {1,S}
7  *2 C     1 {4,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (26938.9,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Watkins, K.W.", "O'Deen, L.A."], title=u'Kinetics of the addition of ethyl, isopropyl, n-butyl, and isopentyl radicals to ethylene', journal="J. Phys. Chem.", volume="73", pages="""4094-4102""", year="1969", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 18,
    label = "r00002224",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4  *3 C     1 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2  *3 C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4  *1 C     0 {2,S} {6,S}
5     C     0 {3,S}
6  *2 C     1 {4,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.26e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (30514.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kerr, J.A.", "Trotman-Dickenson, A.F."], title=u'The reactions of alkyl radicals. Part III. n-Butyl radicals from the photolysis of n-Valeraldehyde', journal="J. Chem. Soc.", pages="""1602""", year="1960", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 19,
    label = "r00002224",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4  *3 C     1 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2  *3 C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4  *1 C     0 {2,S} {6,S}
5     C     0 {3,S}
6  *2 C     1 {4,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.19e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (28019.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Watkins, K.W.", "O'Deen, L.A."], title=u'Kinetics of the addition of ethyl, isopropyl, n-butyl, and isopentyl radicals to ethylene', journal="J. Phys. Chem.", volume="73", pages="""4094-4102""", year="1969", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 20,
    label = "r00002226",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1  *3 C     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *3 C     0 {1,S} {4,S}
3  *2 C     1 {1,S}
4     O     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.82e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (29100.7,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part 2. Methanol', journal="J. Phys. Chem. Ref. Data", volume="16", pages="""471""", year="1987", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 21,
    label = "r00002230",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1     C     0 {2,D}
2  *3 C     1 {1,D}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *3 C     0 {1,S} {4,D}
3  *2 C     1 {1,S}
4     C     0 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8397.62,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Weissman, M.", "Benson, S.W."], title=u'Pyrolysis of methyl chloride, a pathway in the chlorine-catalyzed polymerization of methane', journal="Int. J. Chem. Kinet.", volume="16", pages="""307""", year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 22,
    label = "r00002406",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *3 C     1 {1,S} {2,S} {3,S}
""",
    product1 = 
"""
1  *3 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *1 C     0 {1,S} {6,D}
6  *2 C     1 {5,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.01e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (22199.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Garcia Dominguez, J.A.", "Trotman-Dickenson, A.F."], title=u'The reactions of alkyl radicals. Part IX. The addition of methyl, ethyl, isopropyl, and t-butyl radicals to acetylene and the isomerization of alkenyl radicals', journal="J. Chem. Soc.", pages="""940-944""", year="1962", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 23,
    label = "r00002408",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *3 C     1 {1,S}
""",
    product1 = 
"""
1  *3 C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3  *1 C     0 {1,S} {5,D}
4     C     0 {2,D}
5  *2 C     1 {3,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.19e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (29100.7,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part V. Propene', journal="J. Phys. Chem. Ref. Data", volume="20", pages="""221-273""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 24,
    label = "r00002410",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *3 C     1 {1,S} {2,S}
""",
    product1 = 
"""
1  *3 C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *1 C     0 {1,S} {5,D}
5  *2 C     1 {4,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.58e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (28851.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Garcia Dominguez, J.A.", "Trotman-Dickenson, A.F."], title=u'The reactions of alkyl radicals. Part IX. The addition of methyl, ethyl, isopropyl, and t-butyl radicals to acetylene and the isomerization of alkenyl radicals', journal="J. Chem. Soc.", pages="""940-944""", year="1962", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 25,
    label = "r00002412",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *3 C     1 {1,S}
""",
    product1 = 
"""
1  *3 C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *1 C     0 {1,S} {4,D}
4  *2 C     1 {3,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (29266.9,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Garcia Dominguez, J.A.", "Trotman-Dickenson, A.F."], title=u'The reactions of alkyl radicals. Part IX. The addition of methyl, ethyl, isopropyl, and t-butyl radicals to acetylene and the isomerization of alkenyl radicals', journal="J. Chem. Soc.", pages="""940-944""", year="1962", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 26,
    label = "r00002857",
    reactant1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,T}
3  *2 C     0 {2,T}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D} {4,S}
3  *2 C     1 {2,D}
4  *3 H     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.79e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (12970.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Wagner, H.Gg.", "Zellner, R."], title=u'Reaktionen von Wasserstoffatomen mit ungesaettigten C_3-Kohlenwasserstoffen. II. Die Reaktion von H-Atomen mit Methylacetylen', journal="Ber. Bunsenges. Phys. Chem.", volume="76", pages="""518""", year="1972", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 27,
    label = "r00002857",
    reactant1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D} {4,S}
3  *2 C     1 {2,D}
4  *3 H     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,T}
3  *2 C     0 {2,T}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.98e+12,"s^-1"),
        n = 0,
        Ea = (152986,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 28,
    label = "r00002857",
    reactant1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D} {4,S}
3  *2 C     1 {2,D}
4  *3 H     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,T}
3  *2 C     0 {2,T}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.24e+13,"s^-1"),
        n = 0,
        Ea = (182087,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Naroznik, M.", "Niedzielski, J."], title=u'Propylene photolysis at 6.7 eV: Calculation of the quantum yields for the secondary processes', journal="J. Photochem.", volume="32", pages="""281""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 29,
    label = "r00003845",
    reactant1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,S} {4,D}
3     C     0 {2,S} {5,D}
4  *2 C     0 {2,D}
5     C     0 {3,D}
""",
    reactant2 = 
"""
1  *3 O     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {6,S}
2     C     0 {1,S}
3     C     0 {1,S} {5,D}
4  *2 C     1 {1,S}
5     C     0 {3,D}
6  *3 O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6e-13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (23870.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Francisco-Marquez, M.", "Alvarez-Idaboy, J.R.", "Galano, A.", "Vivier-Bunge, A."], title=u'Theoretical study of the initial reaction between OH and isoprene in tropospheric conditions', journal="Phys. Chem. Chem. Phys.", volume="5", pages="""1392-1399""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:38 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 30,
    label = "r00003846",
    reactant1 = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S} {4,D}
3  *1 C     0 {2,S} {5,D}
4     C     0 {2,D}
5  *2 C     0 {3,D}
""",
    reactant2 = 
"""
1  *3 O     1
""",
    product1 = 
"""
1  *1 C     0 {3,S} {4,S} {6,S}
2     C     0 {3,S}
3     C     0 {1,S} {2,S} {5,D}
4  *2 C     1 {1,S}
5     C     0 {3,D}
6  *3 O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e-12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (13028.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Francisco-Marquez, M.", "Alvarez-Idaboy, J.R.", "Galano, A.", "Vivier-Bunge, A."], title=u'Theoretical study of the initial reaction between OH and isoprene in tropospheric conditions', journal="Phys. Chem. Chem. Phys.", volume="5", pages="""1392-1399""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:38 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 31,
    label = "r00003847",
    reactant1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,S} {4,D}
3     C     0 {2,S} {5,D}
4  *1 C     0 {2,D}
5     C     0 {3,D}
""",
    reactant2 = 
"""
1  *3 O     1
""",
    product1 = 
"""
1  *1 C     0 {3,S} {6,S}
2     C     0 {3,S}
3  *2 C     1 {1,S} {2,S} {4,S}
4     C     0 {3,S} {5,D}
5     C     0 {4,D}
6  *3 O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.25e-11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-2103.56,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Francisco-Marquez, M.", "Alvarez-Idaboy, J.R.", "Galano, A.", "Vivier-Bunge, A."], title=u'Theoretical study of the initial reaction between OH and isoprene in tropospheric conditions', journal="Phys. Chem. Chem. Phys.", volume="5", pages="""1392-1399""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:38 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 32,
    label = "r00003848",
    reactant1 = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S} {4,D}
3  *2 C     0 {2,S} {5,D}
4     C     0 {2,D}
5  *1 C     0 {3,D}
""",
    reactant2 = 
"""
1  *3 O     1
""",
    product1 = 
"""
1  *1 C     0 {4,S} {6,S}
2     C     0 {3,S}
3     C     0 {2,S} {4,S} {5,D}
4  *2 C     1 {1,S} {3,S}
5     C     0 {3,D}
6  *3 O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.39e-12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-5620.58,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Francisco-Marquez, M.", "Alvarez-Idaboy, J.R.", "Galano, A.", "Vivier-Bunge, A."], title=u'Theoretical study of the initial reaction between OH and isoprene in tropospheric conditions', journal="Phys. Chem. Chem. Phys.", volume="5", pages="""1392-1399""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:38 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 33,
    label = "r00004745",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3  *1 C     0 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
1  *3 C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *3 C     0 {1,S}
3  *2 C     1 {1,S} {4,S}
4     C     0 {3,S} {5,D}
5     C     0 {4,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.31e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (31345.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Perrin, D.", "Richard, C.", "Martin, R."], title=u'H_2S-promoted thermal isomerization of Cis-2-pentene to 1-pentene and trans-2-pentene around 800 K', journal="Int. J. Chem. Kinet.", volume="20", pages="""621""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:48 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 34,
    label = "r00004745",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *3 C     0 {1,S}
3  *2 C     1 {1,S} {4,S}
4     C     0 {3,S} {5,D}
5     C     0 {4,D}
""",
    product1 = 
"""
1     C     0 {2,S} {3,D}
2  *2 C     0 {1,S} {4,D}
3     C     0 {1,D}
4  *1 C     0 {2,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.26e+13,"s^-1"),
        n = 0,
        Ea = (159638,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Perrin, D.", "Richard, C.", "Martin, R."], title=u'H_2S-promoted thermal isomerization of Cis-2-pentene to 1-pentene and trans-2-pentene around 800 K', journal="Int. J. Chem. Kinet.", volume="20", pages="""621""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:48 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 35,
    label = "r00004930",
    reactant1 = 
"""
1     C     0 {2,S} {4,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
4     O     0 {1,S}
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *3 C     1 {1,S}
""",
    product1 = 
"""
1  *3 C     0 {2,S} {4,S}
2  *1 C     0 {1,S} {5,S}
3     C     0 {5,S} {6,S}
4     C     0 {1,S}
5  *2 C     1 {2,S} {3,S}
6     O     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.46e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (36833.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Brown, A.C.R.", "James, D.G.L."], title=u'A kinetic study of the metathetical and addition reactions characteristic of allyl polymerization', journal="Can. J. Chem.", volume="40", pages="""796-803""", year="1962", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:48 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 36,
    label = "r00005528",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S} {6,S}
5  *1 C     0 {3,S} {6,D}
6  *2 C     0 {4,S} {5,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S} {6,S}
5  *1 C     0 {3,S} {6,S} {7,S}
6  *2 C     1 {4,S} {5,S}
7  *3 H     0 {5,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (10476.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Hoyermann, K.", "Preuss, A.W.", "Wagner, H.G."], title=u'Die reaktionen von atomarem wasserstoff mit cyclohexen, cyclohexadien-1,3 und benzol', journal="Ber. Bunsenges. Phys. Chem.", volume="79", pages="""156""", year="1975", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:53 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 37,
    label = "r00005635",
    reactant1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    reactant2 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *3 C     1 {1,S} {2,S} {3,S}
""",
    product1 = 
"""
1  *3 C     0 {2,S} {3,S} {4,S} {5,S}
2  *1 C     0 {1,S} {7,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {7,S}
7  *2 C     1 {2,S} {6,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.07e+09,"cm^3/(mol*s)"),
        n = 0,
        Ea = (24610.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part V. Propene', journal="J. Phys. Chem. Ref. Data", volume="20", pages="""221-273""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:54 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 38,
    label = "r00005637",
    reactant1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    reactant2 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *3 C     1 {1,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {4,S}
2  *3 C     0 {1,S} {5,S}
3     C     0 {4,S}
4  *2 C     1 {1,S} {3,S}
5     C     0 {2,S} {6,D}
6     C     0 {5,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.55e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (70673,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Barbe, P.", "Martin, R.", "Perrin, D.", "Scacchi, G."], title=u'Kinetics and modeling of the thermal reaction of propene at 800 K. Part I. Pure propene', journal="Int. J. Chem. Kinet.", volume="28", pages="""829-847""", year="1996", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:54 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 39,
    label = "r00005827",
    reactant1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *2 C     0 {1,S} {2,S} {4,D}
4  *1 C     0 {3,D}
""",
    reactant2 = 
"""
1  *3 C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {5,S}
2  *3 C     0 {1,S}
3     C     0 {5,S}
4     C     0 {5,S}
5  *2 C     1 {1,S} {3,S} {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (28019.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Seres, L.", "Nacsa, A.", "Arthur, N.L."], title=u'Thermal decomposition of di-t-butyl peroxide in the presence of (CH_3)_2C=CH_2: reactions of CH_3, (CH_3)_2CCH_2CH_3, and (CH_3)_2CCH_2C(CH_3)_2CH_2CH_3 radicals', journal="Int. J. Chem. Kinet.", volume="26", pages="""227-246""", year="1994", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:55 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 40,
    label = "r00005846",
    reactant1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *2 C     0 {1,S} {2,S} {4,D}
4  *1 C     0 {3,D}
""",
    reactant2 = 
"""
1     C     0 {2,S} {5,S}
2     C     0 {1,S}
3     C     0 {5,S}
4     C     0 {5,S}
5  *3 C     1 {1,S} {3,S} {4,S}
""",
    product1 = 
"""
1  *3 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S} {6,S}
3  *1 C     0 {1,S} {9,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {9,S}
8     C     0 {9,S}
9  *2 C     1 {3,S} {7,S} {8,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.98e+09,"cm^3/(mol*s)"),
        n = 0,
        Ea = (24361.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Seres, L.", "Nacsa, A.", "Arthur, N.L."], title=u'Thermal decomposition of di-t-butyl peroxide in the presence of (CH_3)_2C=CH_2: reactions of CH_3, (CH_3)_2CCH_2CH_3, and (CH_3)_2CCH_2C(CH_3)_2CH_2CH_3 radicals', journal="Int. J. Chem. Kinet.", volume="26", pages="""227-246""", year="1994", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:55 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 41,
    label = "r00006972",
    reactant1 = 
"""
1  *1 C     0 {3,D}
2     C     0 {3,D}
3  *2 C     0 {1,D} {2,D}
""",
    reactant2 = 
"""
1  *3 C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {4,S}
2  *3 C     0 {1,S}
3     C     0 {4,D}
4  *2 C     1 {1,S} {3,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (33923,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Getty, R.R.", "Kerr, J.A.", "Trotman-Dickenson, A.F."], title=u'The reactions of alkyl radicals. Part XII. The additions of methyl, ethyl, and isopropyl radicals to allene', journal="J. Chem. Soc. A", pages="""979-982""", year="1967", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
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
    index = 42,
    label = "r00006972",
    reactant1 = 
"""
1  *1 C     0 {3,D}
2     C     0 {3,D}
3  *2 C     0 {1,D} {2,D}
""",
    reactant2 = 
"""
1  *3 C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {4,S}
2  *3 C     0 {1,S}
3     C     0 {4,D}
4  *2 C     1 {1,S} {3,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.75e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (28601.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Scherzer, K.", "Claus, P.", "Dabbagh, M."], title=u'Kinetische untersuchungen der reaktionen von methylradikalen mit allen', journal="J. Prakt. Chem.", volume="325", pages="""680""", year="1983", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
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
    index = 43,
    label = "r00006975",
    reactant1 = 
"""
1  *2 C     0 {3,D}
2     C     0 {3,D}
3  *1 C     0 {1,D} {2,D}
""",
    reactant2 = 
"""
1     C     0 {2,B} {3,B}
2     C     0 {1,B} {4,B}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6  *3 C     1 {4,B} {5,B}
""",
    product1 = 
"""
1  *3 C     0 {2,S} {3,B} {4,B}
2  *1 C     0 {1,S} {8,S} {9,D}
3     C     0 {1,B} {6,B}
4     C     0 {1,B} {7,B}
5     C     0 {6,B} {7,B}
6     C     0 {3,B} {5,B}
7     C     0 {4,B} {5,B}
8  *2 C     1 {2,S}
9     C     0 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.19e-20,"cm^3/(mol*s)"),
        n = 2.64,
        Ea = (256.926,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Vereecken, L.", "Peeters, J."], title=u'Reactions of chemically activated C9H9 species II: The reaction of phenyl radicals with allene and cyclopropene, and of benzyl radicals with acetylene', journal="Phys. Chem. Chem. Phys.", volume="5", pages="""2807-2817""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
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
    index = 44,
    label = "r00006976",
    reactant1 = 
"""
1  *1 C     0 {3,D}
2     C     0 {3,D}
3  *2 C     0 {1,D} {2,D}
""",
    reactant2 = 
"""
1     C     0 {2,B} {3,B}
2     C     0 {1,B} {4,B}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6  *3 C     1 {4,B} {5,B}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {9,S}
2  *3 C     0 {1,S} {3,B} {4,B}
3     C     0 {2,B} {6,B}
4     C     0 {2,B} {7,B}
5     C     0 {6,B} {7,B}
6     C     0 {3,B} {5,B}
7     C     0 {4,B} {5,B}
8     C     0 {9,D}
9  *2 C     1 {1,S} {8,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.97e-20,"cm^3/(mol*s)"),
        n = 2.53,
        Ea = (196.949,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Vereecken, L.", "Peeters, J."], title=u'Reactions of chemically activated C9H9 species II: The reaction of phenyl radicals with allene and cyclopropene, and of benzyl radicals with acetylene', journal="Phys. Chem. Chem. Phys.", volume="5", pages="""2807-2817""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
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
    index = 45,
    label = "r00006986",
    reactant1 = 
"""
1  *2 C     0 {3,D}
2     C     0 {3,D}
3  *1 C     0 {1,D} {2,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,D} {4,S}
2  *2 C     1 {1,S}
3     C     0 {1,D}
4  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (11307.7,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Wagner, H.Gg.", "Zellner, R."], title=u'Reaktionen von Wasserstoffatomen mit ungesaettigten C_3-Kohlenwasserstoffen. III. Die Reaktion von H-Atomen mit Allen', journal="Ber. Bunsenges. Phys. Chem.", volume="76", pages="""667""", year="1972", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
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
    index = 46,
    label = "r00006986",
    reactant1 = 
"""
1  *2 C     0 {3,D}
2     C     0 {3,D}
3  *1 C     0 {1,D} {2,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,D} {4,S}
2  *2 C     1 {1,S}
3     C     0 {1,D}
4  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8813.34,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Warnatz, J."], year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
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
    index = 47,
    label = "r00006986",
    reactant1 = 
"""
1  *2 C     0 {3,D}
2     C     0 {3,D}
3  *1 C     0 {1,D} {2,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,D} {4,S}
2  *2 C     1 {1,S}
3     C     0 {1,D}
4  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.19904e+11,"cm^3/(mol*s)"),
        n = 0.69,
        Ea = (12554.9,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W.", "Walker, J.A."], title=u'Pyrolysis of 1,7-octadiene and the kinetic and thermodynamic stability of allyl and 4-pentenyl radicals', journal="J. Phys. Chem.", volume="96", pages="""8378-8384""", year="1992", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
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
    index = 48,
    label = "r00006986",
    reactant1 = 
"""
1  *1 C     0 {2,D} {3,S} {4,S}
2     C     0 {1,D}
3  *2 C     1 {1,S}
4  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {3,D}
2     C     0 {3,D}
3  *1 C     0 {1,D} {2,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.26e+13,"s^-1"),
        n = 0,
        Ea = (256086,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
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
    index = 49,
    label = "r00006986",
    reactant1 = 
"""
1  *1 C     0 {2,D} {3,S} {4,S}
2     C     0 {1,D}
3  *2 C     1 {1,S}
4  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {3,D}
2     C     0 {3,D}
3  *1 C     0 {1,D} {2,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.63e+13,"s^-1"),
        n = 0,
        Ea = (250266,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Naroznik, M.", "Niedzielski, J."], title=u'Propylene photolysis at 6.7 eV: Calculation of the quantum yields for the secondary processes', journal="J. Photochem.", volume="32", pages="""281""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
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
    index = 50,
    label = "r00006986",
    reactant1 = 
"""
1  *1 C     0 {2,D} {3,S} {4,S}
2     C     0 {1,D}
3  *2 C     1 {1,S}
4  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {3,D}
2     C     0 {3,D}
3  *1 C     0 {1,D} {2,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+13,"s^-1"),
        n = 0,
        Ea = (251097,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part V. Propene', journal="J. Phys. Chem. Ref. Data", volume="20", pages="""221-273""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
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
    index = 51,
    label = "r00006986",
    reactant1 = 
"""
1  *1 C     0 {2,D} {3,S} {4,S}
2     C     0 {1,D}
3  *2 C     1 {1,S}
4  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {3,D}
2     C     0 {3,D}
3  *1 C     0 {1,D} {2,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.79e+13,"s^-1"),
        n = 0.84,
        Ea = (250266,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W.", "Walker, J.A."], title=u'Pyrolysis of 1,7-octadiene and the kinetic and thermodynamic stability of allyl and 4-pentenyl radicals', journal="J. Phys. Chem.", volume="96", pages="""8378-8384""", year="1992", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
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
    index = 52,
    label = "r00007721",
    reactant1 = 
"""
1     C     0 {3,S}
2     C     0 {4,S}
3  *1 C     0 {1,S} {4,D}
4  *2 C     0 {2,S} {3,D}
""",
    reactant2 = 
"""
1  *3 C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S}
3  *3 C     0 {1,S}
4     C     0 {5,S}
5  *2 C     1 {1,S} {4,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.5e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (29266.9,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Yokoyama, N.", "Brinton, R.K."], title=u'Reaction of methyl radicals with cis-butene-2', journal="Can. J. Chem.", volume="47", pages="""2987""", year="1969", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:09 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 53,
    label = "r00007920",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S} {6,S}
5     C     0 {3,S}
6  *2 C     0 {4,S} {7,D}
7  *1 C     0 {6,D}
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *3 C     1 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S} {7,S}
4  *3 C     0 {6,S} {8,S}
5     C     0 {2,S} {9,S}
6  *1 C     0 {4,S} {9,S}
7     C     0 {3,S}
8     C     0 {4,S}
9  *2 C     1 {5,S} {6,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.93e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (33424.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["James, D.G.L.", "Steacie, E.W.R."], title=u'Reactions of the ethyl radical. II. Addition to unsaturated hydrocarbons', journal="Proc. R. Soc. London A", volume="244", pages="""297-311""", year="1958", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
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
    index = 54,
    label = "r00008207",
    reactant1 = 
"""
1     C     0 {3,S}
2     C     0 {4,S}
3  *1 C     0 {1,S} {4,D}
4  *2 C     0 {2,S} {3,D}
""",
    reactant2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *3 C     1 {1,S} {2,S}
""",
    product1 = 
"""
1  *3 C     0 {2,S} {3,S} {4,S}
2  *1 C     0 {1,S} {5,S} {7,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     C     0 {7,S}
7  *2 C     1 {2,S} {6,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.31e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (39493.7,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Seres, L.", "Fischer, R.", "Scherzer, K.", "Gorgenyl, M."], title=u'Thermal reaction of azoisopropane in the presence of (E)-CH_3CH = CHCH_3: reactions of the radical 2-C_3H_7', journal="J. Chem. Soc. Faraday Trans.", volume="91", pages="""1303-1312""", year="1995", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:14 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 55,
    label = "r00009777",
    reactant1 = 
"""
1  *1 C     0 {4,S} {5,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *2 C     1 {1,S} {2,S} {3,S}
5  *3 H     0 {1,S}
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
1  *3 H     1
""",
    degeneracy = 9,
    kinetics = Arrhenius(
        A = (2e+16,"s^-1"),
        n = 0,
        Ea = (182087,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Birrell, R.N.", "Trotman-Dickenson, A.F."], title=u'The reactions of alkyl radicals. Part VII. t-butyl radicals from the photolysis of pivalaldehyde', journal="J. Chem. Soc.", pages="""4218""", year="1960", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:27 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 56,
    label = "r00009777",
    reactant1 = 
"""
1  *1 C     0 {4,S} {5,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *2 C     1 {1,S} {2,S} {3,S}
5  *3 H     0 {1,S}
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
1  *3 H     1
""",
    degeneracy = 9,
    kinetics = Arrhenius(
        A = (4.68e+14,"s^-1"),
        n = 0,
        Ea = (164627,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Canosa, C.E.", "Marshall, R.M."], title=u'The Rate Constant for t-C_4H_9 \u2192 H + i-C_4H_8 and the Thermodynamic Parameters of t-C_4H_9', journal="Int. J. Chem. Kinet.", volume="13", pages="""303""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:27 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 57,
    label = "r00009777",
    reactant1 = 
"""
1  *1 C     0 {4,S} {5,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *2 C     1 {1,S} {2,S} {3,S}
5  *3 H     0 {1,S}
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
1  *3 H     1
""",
    degeneracy = 9,
    kinetics = Arrhenius(
        A = (8.32e+13,"s^-1"),
        n = 0,
        Ea = (157144,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'The stability of alkyl radicals', journal="J. Am. Chem. Soc.", volume="107", pages="""2872""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:27 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 58,
    label = "r00009777",
    reactant1 = 
"""
1  *1 C     0 {4,S} {5,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *2 C     1 {1,S} {2,S} {3,S}
5  *3 H     0 {1,S}
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
1  *3 H     1
""",
    degeneracy = 9,
    kinetics = Arrhenius(
        A = (8.3e+13,"s^-1"),
        n = 0,
        Ea = (159638,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part 4. Isobutane', journal="J. Phys. Chem. Ref. Data", volume="19", pages="""1-68""", year="1990", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:27 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 59,
    label = "r00009777",
    reactant1 = 
"""
1  *1 C     0 {4,S} {5,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *2 C     1 {1,S} {2,S} {3,S}
5  *3 H     0 {1,S}
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
1  *3 H     1
""",
    degeneracy = 9,
    kinetics = Arrhenius(
        A = (1e+13,"s^-1"),
        n = 1.48,
        Ea = (150492,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Knyazev, V.D.", "Dubinsky, I.A.", "Slagle, I.R.", "Gutman, D."], title=u'Unimolecular decomposition of t-C_4H_9 radical', journal="J. Phys. Chem.", volume="98", pages="""5279-5289""", year="1994", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:27 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 60,
    label = "r00009777",
    reactant1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *2 C     0 {1,S} {2,S} {4,D}
4  *1 C     0 {3,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3  *1 C     0 {4,S} {5,S}
4  *2 C     1 {1,S} {2,S} {3,S}
5  *3 H     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.63e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (5936.53,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dalgleish, D.G.", "Knox, J.H."], title=u'The reactions of hydrogen atoms with isobutane and isobutene', journal="J. Chem. Soc. Chem. Commun.", pages="""917-918""", year="1966", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:27 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 61,
    label = "r00009777",
    reactant1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *2 C     0 {1,S} {2,S} {4,D}
4  *1 C     0 {3,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3  *1 C     0 {4,S} {5,S}
4  *2 C     1 {1,S} {2,S} {3,S}
5  *3 H     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (6302.37,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Bradley, J.N.", "West, K.O."], title=u'Single-pulse Shock Tube Studies of Hydrocarbon Pyrolysis. Part 5. Pyrolysis of Neopentane', journal="J. Chem. Soc. Faraday Trans. 1", volume="72", pages="""8""", year="1976", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:27 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 62,
    label = "r00009777",
    reactant1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *2 C     0 {1,S} {2,S} {4,D}
4  *1 C     0 {3,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3  *1 C     0 {4,S} {5,S}
4  *2 C     1 {1,S} {2,S} {3,S}
5  *3 H     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.89e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (7491.34,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Canosa, C.E.", "Marshall, R.M.", "Sheppard, A."], title=u'The Rate Constant for H + i-C_4H_8 \u2192 t-C_4H_9 in the Range of 298-563 K', journal="Int. J. Chem. Kinet.", volume="13", pages="""295""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000008.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:27 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 63,
    label = "r00009777",
    reactant1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *2 C     0 {1,S} {2,S} {4,D}
4  *1 C     0 {3,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3  *1 C     0 {4,S} {5,S}
4  *2 C     1 {1,S} {2,S} {3,S}
5  *3 H     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.25e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (3600.17,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kyogoku, T.", "Watanabe, T.", "Tsunashima, S.", "Sato, S."], title=u'Arrhenius parameters for the reactions of hydrogen and deuterium atoms with four butenes', journal="Bull. Chem. Soc. Jpn.", volume="56", pages="""19""", year="1983", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000009.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:27 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 64,
    label = "r00009777",
    reactant1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *2 C     0 {1,S} {2,S} {4,D}
4  *1 C     0 {3,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3  *1 C     0 {4,S} {5,S}
4  *2 C     1 {1,S} {2,S} {3,S}
5  *3 H     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.20963e+12,"cm^3/(mol*s)"),
        n = 0.25,
        Ea = (6127.77,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Knyazev, V.D.", "Dubinsky, I.A.", "Slagle, I.R.", "Gutman, D."], title=u'Unimolecular decomposition of t-C_4H_9 radical', journal="J. Phys. Chem.", volume="98", pages="""5279-5289""", year="1994", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000010.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:27 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 65,
    label = "r00009777",
    reactant1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *2 C     0 {1,S} {2,S} {4,D}
4  *1 C     0 {3,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3  *1 C     0 {4,S} {5,S}
4  *2 C     1 {1,S} {2,S} {3,S}
5  *3 H     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.57e-11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-6061.25,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Bryukov, M.G.", "Slagle, I.R.", "Knyazev, V.D."], title=u'Kinetics of Reactions of H Atoms with Methane and Chlorinated Methanes', journal="J. Phys. Chem. A", volume="105", pages="""3107-3122""", year="2001", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000011.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:27 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 66,
    label = "r00010166",
    reactant1 = 
"""
1  *1 C     0 {3,S} {4,S}
2     C     0 {3,S}
3  *2 C     1 {1,S} {2,S}
4  *3 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (6.31e+13,"s^-1"),
        n = 0,
        Ea = (154649,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kerr, J.A.", "Trotman-Dickenson, A.F."], title=u'The reactions of alkyl radicals. Part 2. s-Propyl radicals from the photolysis of isobutyraldehyde', journal="Trans. Faraday Soc.", volume="55", pages="""921""", year="1959", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 67,
    label = "r00010166",
    reactant1 = 
"""
1  *1 C     0 {3,S} {4,S}
2     C     0 {3,S}
3  *2 C     1 {1,S} {2,S}
4  *3 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (1e+15,"s^-1"),
        n = 0,
        Ea = (175435,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Leathard, D.A.", "Purnell, J.H."], title=u'Propyl radical isomerization and heterogeneous effects in the pyrolysis of propane below 500\xb0C', journal="Proc. R. Soc. London A", volume="306", pages="""553""", year="1968", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 68,
    label = "r00010166",
    reactant1 = 
"""
1  *1 C     0 {3,S} {4,S}
2     C     0 {3,S}
3  *2 C     1 {1,S} {2,S}
4  *3 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (2e+14,"s^-1"),
        n = 0,
        Ea = (162132,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Papic, M.M.", "Laidler, K.J."], title=u'Kinetics of the Mercury-Photosensitized Decomposition of Propane. Part II. Reactions of the Propyl Radicals', journal="Can. J. Chem.", volume="49", pages="""549""", year="1971", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 69,
    label = "r00010166",
    reactant1 = 
"""
1  *1 C     0 {3,S} {4,S}
2     C     0 {3,S}
3  *2 C     1 {1,S} {2,S}
4  *3 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (2.51e+13,"s^-1"),
        n = 0,
        Ea = (171278,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Camilleri, P.", "Marshall, R.M.", "Purnell, H."], title=u'Arrhenius Parameters for the Unimolecular Decompositions of Azomethane and n-Propyl and Isopropyl Radicals and for Methyl Radical Attack on Propane', journal="J. Chem. Soc. Faraday Trans. 1", volume="71", pages="""1491""", year="1975", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 70,
    label = "r00010166",
    reactant1 = 
"""
1  *1 C     0 {3,S} {4,S}
2     C     0 {3,S}
3  *2 C     1 {1,S} {2,S}
4  *3 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (2e+14,"s^-1"),
        n = 0,
        Ea = (162132,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Warnatz, J."], year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 71,
    label = "r00010166",
    reactant1 = 
"""
1  *1 C     0 {3,S} {4,S}
2     C     0 {3,S}
3  *2 C     1 {1,S} {2,S}
4  *3 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (3.98e+13,"s^-1"),
        n = 0,
        Ea = (165458,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 72,
    label = "r00010166",
    reactant1 = 
"""
1  *1 C     0 {3,S} {4,S}
2     C     0 {3,S}
3  *2 C     1 {1,S} {2,S}
4  *3 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (2.19e+13,"s^-1"),
        n = 0,
        Ea = (155481,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'The stability of alkyl radicals', journal="J. Am. Chem. Soc.", volume="107", pages="""2872""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 73,
    label = "r00010166",
    reactant1 = 
"""
1  *1 C     0 {3,S} {4,S}
2     C     0 {3,S}
3  *2 C     1 {1,S} {2,S}
4  *3 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (1.6e+13,"s^-1"),
        n = 0,
        Ea = (149660,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part 3. Propane', journal="J. Phys. Chem. Ref. Data", volume="17", pages="""887""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000008.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 74,
    label = "r00010166",
    reactant1 = 
"""
1  *1 C     0 {3,S} {4,S}
2     C     0 {3,S}
3  *2 C     1 {1,S} {2,S}
4  *3 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (2.19e+12,"s^-1"),
        n = 1.83,
        Ea = (147998,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Seakins, P.W.", "Robertson, S.H.", "Pilling, M.J.", "Slagle, I.R.", "Gmurczyk, G.W.", "Bencsura, A.", "Gutman, D.", "Tsang, W."], title=u'Kinetics of the unimolecular decomposition of iso-C_3H_7: weak collision effects in helium, argon, and nitrogen', journal="J. Phys. Chem.", volume="97", pages="""4450-4458""", year="1993", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000010.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 75,
    label = "r00010166",
    reactant1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1     C     0 {3,S}
2  *1 C     0 {3,S} {4,S}
3  *2 C     1 {1,S} {2,S}
4  *3 H     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.14e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (5063.51,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kurylo, M.J.", "Peterson, N.C.", "Braun, W."], title=u'Temperature and Pressure Effects in the Addition of H Atoms to Propylene', journal="J. Chem. Phys.", volume="54", pages="""4662""", year="1971", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000011.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 76,
    label = "r00010166",
    reactant1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1     C     0 {3,S}
2  *1 C     0 {3,S} {4,S}
3  *2 C     1 {1,S} {2,S}
4  *3 H     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.4e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (5229.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Wagner, H.Gg.", "Zellner, R."], title=u'Reaktionen von Wasserstoffatomen mit ungesaettigten C_3-Kohlenwasserstoffen. I. Die Reaktion von H-Atomen mit Propylen', journal="Ber. Bunsenges. Phys. Chem.", volume="76", pages="""440""", year="1972", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000012.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 77,
    label = "r00010166",
    reactant1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1     C     0 {3,S}
2  *1 C     0 {3,S} {4,S}
3  *2 C     1 {1,S} {2,S}
4  *3 H     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (3999.26,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Warnatz, J."], year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000013.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 78,
    label = "r00010166",
    reactant1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1     C     0 {3,S}
2  *1 C     0 {3,S} {4,S}
3  *2 C     1 {1,S} {2,S}
4  *3 H     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.32e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (6526.86,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part V. Propene', journal="J. Phys. Chem. Ref. Data", volume="20", pages="""221-273""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000015.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 79,
    label = "r00010166",
    reactant1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1     C     0 {3,S}
2  *1 C     0 {3,S} {4,S}
3  *2 C     1 {1,S} {2,S}
4  *3 H     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (6526.86,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for hydrocarbon pyrolysis', journal="Ind. Eng. Chem.", volume="31", pages="""3-8""", year="1992", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000016.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 80,
    label = "r00010166",
    reactant1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1     C     0 {3,S}
2  *1 C     0 {3,S} {4,S}
3  *2 C     1 {1,S} {2,S}
4  *3 H     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.70492e+09,"cm^3/(mol*s)"),
        n = 1.16,
        Ea = (3658.37,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Seakins, P.W.", "Robertson, S.H.", "Pilling, M.J.", "Slagle, I.R.", "Gmurczyk, G.W.", "Bencsura, A.", "Gutman, D.", "Tsang, W."], title=u'Kinetics of the unimolecular decomposition of iso-C_3H_7: weak collision effects in helium, argon, and nitrogen', journal="J. Phys. Chem.", volume="97", pages="""4450-4458""", year="1993", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000017.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:33 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 81,
    label = "r00010238",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1e+10,"s^-1"),
        n = 0,
        Ea = (152986,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Brodsky, A.M.", "Kalinenko, R.A.", "Lavrovsky, K.P."], title=u'The principles governing high-temperature ethane cracking', journal="J. Chem. Soc.", pages="""4443""", year="1960", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 82,
    label = "r00010238",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.58e+11,"s^-1"),
        n = 0,
        Ea = (129706,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kerr, J.A.", "Trotman-Dickenson, A.F."], title=u'The reactions of alkyl radicals. Part V. Ethyl radicals from propionaldehyde', journal="J. Chem. Soc.", pages="""1611""", year="1960", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 83,
    label = "r00010238",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1e+13,"s^-1"),
        n = 0,
        Ea = (167121,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Purnell, J.H.", "Quinn, C.P."], title=u'The pyrolysis of n-butane', journal="Proc. R. Soc. London A", volume="270", pages="""267""", year="1962", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 84,
    label = "r00010238",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (3.8e+13,"s^-1"),
        n = 0,
        Ea = (158806,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Lin, M.C.", "Back, M.H."], title=u'the thermal decomposition of ethane. Part II. The unimolecular decomposition of the ethane molecule and the ethyl radical', journal="Can. J. Chem.", volume="44", pages="""2357""", year="1966", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 85,
    label = "r00010238",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.7e+14,"s^-1"),
        n = 0,
        Ea = (171278,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Loucks, L.F.", "Laidler, K.J."], title=u'Thermal decomposition of the ethyl radical', journal="Can. J. Chem.", volume="45", pages="""2795-2803""", year="1967", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000008.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 86,
    label = "r00010238",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1e+11,"s^-1"),
        n = 0,
        Ea = (126380,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Koski, A.A.", "Price, S.J.W.", "Trudell, B.C."], title=u'Studies of the pyrolysis of diethylzinc by the toluene carrier method and of the reaction of ethyl radicals with toluene', journal="Can. J. Chem.", volume="54", pages="""482-487""", year="1976", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000011.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 87,
    label = "r00010238",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2e+13,"s^-1"),
        n = 0,
        Ea = (166289,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Warnatz, J."], year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000018.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 88,
    label = "r00010238",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (5.01e+13,"s^-1"),
        n = 0,
        Ea = (171278,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000020.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 89,
    label = "r00010238",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.2e+12,"s^-1"),
        n = 0,
        Ea = (146335,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Hidaka, Y.", "Shiba, S.", "Takuma, H.", "Suga, M."], title=u'Thermal decomposition of ethane in shock waves', journal="Int. J. Chem. Kinet.", volume="17", pages="""441""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000021.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 90,
    label = "r00010238",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.92e+11,"s^-1"),
        n = 0,
        Ea = (141346,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Brouard, M.", "Lightfoot, P.D.", "Pilling, M.J."], title=u'Observation of equilibration in the system H + C_2H_4 = C_2H_5. The determination of the heat of formation of C_2H_5', journal="J. Phys. Chem.", volume="90", pages="""445""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000022.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 91,
    label = "r00010238",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (8.91e+12,"s^-1"),
        n = 0,
        Ea = (158806,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Trenwith, A.B."], title=u'The pyrolysis of ethane. A study of the dissociation reaction C_2H_5 \u2192 C_2H_4 + H', journal="J. Chem. Soc. Faraday Trans. 2", volume="82", pages="""457""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000023.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 92,
    label = "r00010238",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (4.31e+12,"s^-1"),
        n = 1.19,
        Ea = (155481,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W.", "Hampson, R.F."], title=u'Chemical kinetic data base for combustion chemistry. Part I. Methane and related compounds', journal="J. Phys. Chem. Ref. Data", volume="15", pages="""1087""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000024.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 93,
    label = "r00010238",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.58e+13,"s^-1"),
        n = 0,
        Ea = (158806,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Simon, Y.", "Foucaut, J.F.", "Scacchi, G."], title=u'Etude experimentale et modelisation theorique de la decomposition du radical ethyle', journal="Can. J. Chem.", volume="66", pages="""2142""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000025.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 94,
    label = "r00010238",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (9.46e+19,"s^-1"),
        n = -9.54,
        Ea = (213682,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Bozzelli, J.W.", "Dean, A.M."], title=u'Chemical activation analysis of the reaction of C_2H_5 with O_2', journal="J. Phys. Chem.", volume="94", pages="""3313""", year="1990", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000027.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 95,
    label = "r00010238",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (4.08e+12,"s^-1"),
        n = 1.04,
        Ea = (153818,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Feng, Y.", "Niiranen, J.T.", "Bencsura, A.", "Knyazev, V.D.", "Gutman, D.", "Tsang, W."], title=u'Weak collision effects in the reaction C_2H_5 = C_2H_4 + H', journal="J. Phys. Chem.", volume="97", pages="""871-880""", year="1993", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000028.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 96,
    label = "r00010238",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (8.2e+13,"s^-1"),
        n = 0,
        Ea = (167121,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Frank, P.", "Hayman, G.", "Just, Th.", "Kerr, J.A.", "Murrells, T.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."], title=u'Evaluated kinetic data for combusion modelling. Supplement I', journal="J. Phys. Chem. Ref. Data", volume="23", pages="""847-1033""", year="1994", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000030.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 97,
    label = "r00010238",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6e+41,"cm^3/(mol*s)"),
        n = -7.62,
        Ea = (6970,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000032.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 98,
    label = "r00010238",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.2e+42,"cm^3/(mol*s)"),
        n = -7.62,
        Ea = (6970,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000033.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 99,
    label = "r00010238",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.6e+42,"cm^3/(mol*s)"),
        n = -7.62,
        Ea = (6970,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000034.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 100,
    label = "r00010238",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.2e+42,"cm^3/(mol*s)"),
        n = -7.62,
        Ea = (6970,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000035.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 101,
    label = "r00010238",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (9e+41,"cm^3/(mol*s)"),
        n = -7.62,
        Ea = (6970,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000036.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 102,
    label = "r00010238",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.2e+42,"cm^3/(mol*s)"),
        n = -7.62,
        Ea = (6970,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000037.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 103,
    label = "r00010238",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.8e+42,"cm^3/(mol*s)"),
        n = -7.62,
        Ea = (6970,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000038.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 104,
    label = "r00010238",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.2e+41,"cm^3/(mol*s)"),
        n = -7.62,
        Ea = (6970,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000039.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 105,
    label = "r00010238",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.4e+11,"cm^3/(mol*s)"),
        n = 0.454,
        Ea = (1820,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000040.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 106,
    label = "r00010238",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.94e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (7948.64,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Yang, K."], title=u'Free radical reactions initiated by ionizing radiations. I. Arrhenius parameters for the reactions of hydrogen atoms with propane, ethylene and propylene', journal="J. Am. Chem. Soc.", volume="84", pages="""719-721""", year="1962", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000045.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 107,
    label = "r00010238",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.08326e+12,"cm^3/(mol*s)"),
        n = 0.5,
        Ea = (6693.15,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dodonov, A.F.", "Lavrovskaya, G.K.", "Talroze, V.L."], title=u'Mass-spectroscopic determination of rate constants for elementary reactions. III. The rections H + C_2H_4, H + C_3H_6, and H + n-C_4H_8', journal="Kinet. Catal.", volume="10", pages="""14""", year="1969", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000054.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 108,
    label = "r00010238",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.89e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (3051.41,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Teng, L.", "Jones, W.E."], title=u'Kinetics of the Reactions of Hydrogen Atoms with Ethylene and Vinyl Fluoride', journal="J. Chem. Soc. Faraday Trans. 1", volume="68", pages="""1267""", year="1972", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000065.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 109,
    label = "r00010238",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.21e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8647.05,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Lee, J.H.", "Michael, J.V.", "Payne, W.A.", "Stief, L.J."], title=u'Absolute Rate of the Reaction of Atomic Hydrogen with Ethylene from 198 to 320 K at High Pressure', journal="J. Chem. Phys.", volume="68", pages="""1817""", year="1978", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000072.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 110,
    label = "r00010238",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.98e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (19455.9,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Billaud, F.", "Baronnet, F.", "Niclause, M."], title=u"Influence de l'Ethylene sur la Pyrolyse de l'Ethane vers 540^oC", journal="J. Chim. Phys.", volume="77", pages="""357""", year="1980", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000074.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 111,
    label = "r00010238",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.77e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8979.63,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Sugawara, K.", "Okazaki, K.", "Sato, S."], title=u'Kinetic Isotope Effects in the Reaction H + C_2H_4 \u2192 C_2H_5', journal="Chem. Phys. Lett.", volume="78", pages="""259""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000076.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 112,
    label = "r00010238",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.83e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (9145.92,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Sugawara, K.", "Okazaki, K.", "Sato, S."], title=u'Temperature Dependence of the Rate Constants of H and D-Atom Additions to C_2H_4, C_2H_3D, C_2D_4, C_2H_2, and C_2D_2', journal="Bull. Chem. Soc. Jpn.", volume="54", pages="""2872""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000077.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 113,
    label = "r00010238",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (6302.37,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Warnatz, J."], year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000079.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 114,
    label = "r00010238",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.73e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-15548.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Brouard, M.", "Lightfoot, P.D.", "Pilling, M.J."], title=u'Observation of equilibration in the system H + C_2H_4 = C_2H_5. The determination of the heat of formation of C_2H_5', journal="J. Phys. Chem.", volume="90", pages="""445""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000080.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 115,
    label = "r00010238",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.41669e+08,"cm^3/(mol*s)"),
        n = 1.49,
        Ea = (4148.92,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W.", "Hampson, R.F."], title=u'Chemical kinetic data base for combustion chemistry. Part I. Methane and related compounds', journal="J. Phys. Chem. Ref. Data", volume="15", pages="""1087""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000082.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 116,
    label = "r00010238",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.64e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (9062.77,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Lightfoot, P.D.", "Pilling, M.J."], title=u'Temperature and pressure dependence of the rate constant for the addition of H to C_2H_4', journal="J. Phys. Chem.", volume="91", pages="""3373""", year="1987", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000083.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 117,
    label = "r00010238",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.75e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (9395.35,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Lightfoot, P.D.", "Pilling, M.J."], title=u'Temperature and pressure dependence of the rate constant for the addition of H to C_2H_4', journal="J. Phys. Chem.", volume="91", pages="""3373""", year="1987", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000084.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 118,
    label = "r00010238",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.96891e+09,"cm^3/(mol*s)"),
        n = 1.28,
        Ea = (5404.41,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Frank, P.", "Hayman, G.", "Just, Th.", "Kerr, J.A.", "Murrells, T.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."], title=u'Evaluated kinetic data for combusion modelling. Supplement I', journal="J. Phys. Chem. Ref. Data", volume="23", pages="""847-1033""", year="1994", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000087.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 119,
    label = "r00010504",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3  *2 C     1 {1,S}
4  *3 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.98e+13,"s^-1"),
        n = 0,
        Ea = (146335,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kerr, J.A.", "Trotman-Dickenson, A.F."], title=u'The reactions of alkyl radicals. Part 1.-n-Propyl radicals from the photolysis of n-butyraldehyde', journal="Trans. Faraday Soc.", volume="55", pages="""572""", year="1959", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 120,
    label = "r00010504",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3  *2 C     1 {1,S}
4  *3 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.26e+14,"s^-1"),
        n = 0,
        Ea = (154649,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Jackson, W.M.", "McNesby, J.R."], title=u'Photolysis of acetone-d_6 in the presence of propane-2,2-d_2. Decomposition of the n-propyl radical', journal="J. Am. Chem. Soc.", volume="83", pages="""4891""", year="1961", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 121,
    label = "r00010504",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3  *2 C     1 {1,S}
4  *3 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.11e+11,"s^-1"),
        n = 0,
        Ea = (112245,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Mintz, K.J.", "Le Roy, D.J."], title=u'Kinetics of radical reactions in sodium diffusion flames', journal="Can. J. Chem.", volume="56", pages="""941""", year="1978", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 122,
    label = "r00010504",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3  *2 C     1 {1,S}
4  *3 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+14,"s^-1"),
        n = 0,
        Ea = (156312,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Warnatz, J."], year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 123,
    label = "r00010504",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3  *2 C     1 {1,S}
4  *3 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.31e+13,"s^-1"),
        n = 0,
        Ea = (158806,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Weissman, M.", "Benson, S.W."], title=u'Pyrolysis of methyl chloride, a pathway in the chlorine-catalyzed polymerization of methane', journal="Int. J. Chem. Kinet.", volume="16", pages="""307""", year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 124,
    label = "r00010504",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3  *2 C     1 {1,S}
4  *3 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.26e+13,"s^-1"),
        n = 0,
        Ea = (161301,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 125,
    label = "r00010504",
    reactant1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3  *2 C     1 {1,S}
4  *3 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.4e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (11474,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Wagner, H.Gg.", "Zellner, R."], title=u'Reaktionen von Wasserstoffatomen mit ungesaettigten C_3-Kohlenwasserstoffen. I. Die Reaktion von H-Atomen mit Propylen', journal="Ber. Bunsenges. Phys. Chem.", volume="76", pages="""440""", year="1972", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 126,
    label = "r00010504",
    reactant1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3  *2 C     1 {1,S}
4  *3 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (10975.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Warnatz, J."], year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000008.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 127,
    label = "r00010504",
    reactant1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3  *2 C     1 {1,S}
4  *3 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.32e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (13635.7,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part V. Propene', journal="J. Phys. Chem. Ref. Data", volume="20", pages="""221-273""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000009.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 128,
    label = "r00010504",
    reactant1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3  *2 C     1 {1,S}
4  *3 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (13635.7,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for hydrocarbon pyrolysis', journal="Ind. Eng. Chem.", volume="31", pages="""3-8""", year="1992", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000010.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:35 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 129,
    label = "r00010564",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 O     1 {1,S}
3  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.58e+14,"s^-1"),
        n = 0,
        Ea = (114740,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Batt, L."], title=u'The Gas-Phase Decomposition of Alkoxy Radicals', journal="Int. J. Chem. Kinet.", volume="11", pages="""977""", year="1979", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 130,
    label = "r00010564",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 O     1 {1,S}
3  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.6e+14,"s^-1"),
        n = 0,
        Ea = (104762,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Warnatz, J."], year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 131,
    label = "r00010564",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 O     1 {1,S}
3  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (3.16e+14,"s^-1"),
        n = 0,
        Ea = (108088,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Greenhill, P.G.", "O'Grady, B.V.", "Gilbert, R.G."], title=u'Theoretical prediction of CH_3O and CH_2OH gas phase decomposition rate coefficients', journal="Aust. J. Chem.", volume="39", pages="""1929""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 132,
    label = "r00010564",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 O     1 {1,S}
3  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2e+14,"s^-1"),
        n = 0,
        Ea = (104762,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Heicklen, J."], title=u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals', journal="Adv. Photochem.", volume="14", pages="""177""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 133,
    label = "r00010564",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 O     1 {1,S}
3  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1e+15,"s^-1"),
        n = 0,
        Ea = (143009,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Zaslonko, I.S.", "Mukoseev, Yu.K.", "Tyurin, A.N."], title=u'Reactions of CH_3O radicals in shock waves', journal="Kinet. Catal.", volume="29", pages="""244""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000008.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 134,
    label = "r00010564",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 O     1 {1,S}
3  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (6.8e+13,"s^-1"),
        n = 0,
        Ea = (1809.22,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Hippler, H.", "Striebel, F.", "Viskolcz, B."], title=u'A Detailed Experimental and Theoretical Study on the Decomposition of Methoxy Radicals', journal="Phys. Chem. Chem. Phys.", volume="3", pages="""2450-2458""", year="2001", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000018.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 135,
    label = "r00010564",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 O     1 {1,S}
3  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (5.5e+13,"s^-1"),
        n = 0,
        Ea = (1670.43,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."], title=u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds', journal="Can. J. Chem.", volume="81", pages="""431-442""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000022.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 136,
    label = "r00010564",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 O     1 {1,S}
3  *3 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+30,"cm^3/(mol*s)"),
        n = -4.8,
        Ea = (5560,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000023.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 137,
    label = "r00010564",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 O     1 {1,S}
3  *3 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.4e+30,"cm^3/(mol*s)"),
        n = -4.8,
        Ea = (5560,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000024.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 138,
    label = "r00010564",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 O     1 {1,S}
3  *3 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.32e+31,"cm^3/(mol*s)"),
        n = -4.8,
        Ea = (5560,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000025.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 139,
    label = "r00010564",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 O     1 {1,S}
3  *3 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.4e+30,"cm^3/(mol*s)"),
        n = -4.8,
        Ea = (5560,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000026.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 140,
    label = "r00010564",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 O     1 {1,S}
3  *3 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+30,"cm^3/(mol*s)"),
        n = -4.8,
        Ea = (5560,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000027.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 141,
    label = "r00010564",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 O     1 {1,S}
3  *3 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.4e+30,"cm^3/(mol*s)"),
        n = -4.8,
        Ea = (5560,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000028.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 142,
    label = "r00010564",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 O     1 {1,S}
3  *3 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.6e+30,"cm^3/(mol*s)"),
        n = -4.8,
        Ea = (5560,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000029.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 143,
    label = "r00010564",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 O     1 {1,S}
3  *3 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.4e+11,"cm^3/(mol*s)"),
        n = 0.454,
        Ea = (2600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000030.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 144,
    label = "r00010632",
    reactant1 = 
"""
1  *3 C     0 {2,S}
2  *1 C     0 {1,S} {3,S}
3  *2 O     1 {2,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.41e+12,"s^-1"),
        n = 0,
        Ea = (92290.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Leggett, C.", "Thynne, J.C.J."], title=u'Decomposition of ethoxyl radicals', journal="J. Chem. Soc. A", pages="""1188""", year="1970", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 145,
    label = "r00010632",
    reactant1 = 
"""
1  *3 C     0 {2,S}
2  *1 C     0 {1,S} {3,S}
3  *2 O     1 {2,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.01e+13,"s^-1"),
        n = 0,
        Ea = (90627.7,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baldwin, A.C.", "Barker, J.R.", "Golden, D.M.", "Hendry, D.G."], title=u'Photochemical smog. Rate parameter estimates and computer simulations', journal="J. Phys. Chem.", volume="81", pages="""2483""", year="1977", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 146,
    label = "r00010632",
    reactant1 = 
"""
1  *3 C     0 {2,S}
2  *1 C     0 {1,S} {3,S}
3  *2 O     1 {2,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+15,"s^-1"),
        n = 0,
        Ea = (90627.7,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Batt, L.", "Milne, R.T."], title=u'The Gas-Phase Pyrolysis of Alkyl Nitrites. IV. Ethyl Nitrite', journal="Int. J. Chem. Kinet.", volume="9", pages="""549""", year="1977", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 147,
    label = "r00010632",
    reactant1 = 
"""
1  *3 C     0 {2,S}
2  *1 C     0 {1,S} {3,S}
3  *2 O     1 {2,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+15,"s^-1"),
        n = 0,
        Ea = (90627.7,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Batt, L."], title=u'The Gas-Phase Decomposition of Alkoxy Radicals', journal="Int. J. Chem. Kinet.", volume="11", pages="""977""", year="1979", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 148,
    label = "r00010632",
    reactant1 = 
"""
1  *3 C     0 {2,S}
2  *1 C     0 {1,S} {3,S}
3  *2 O     1 {2,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.98e+13,"s^-1"),
        n = 0,
        Ea = (83976.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Choo, K.Y.", "Benson, S.W."], title=u'Arrhenius Parameters for the Alkoxy Radical Decomposition Reactions', journal="Int. J. Chem. Kinet.", volume="13", pages="""833""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 149,
    label = "r00010632",
    reactant1 = 
"""
1  *3 C     0 {2,S}
2  *1 C     0 {1,S} {3,S}
3  *2 O     1 {2,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+15,"s^-1"),
        n = 0,
        Ea = (90627.7,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Heicklen, J."], title=u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals', journal="Adv. Photochem.", volume="14", pages="""177""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 150,
    label = "r00010632",
    reactant1 = 
"""
1  *3 C     0 {2,S}
2  *1 C     0 {1,S} {3,S}
3  *2 O     1 {2,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+13,"s^-1"),
        n = 0,
        Ea = (89796.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Esser, C.", "Frank, P.", "Just, Th.", "Kerr, J.A.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."], title=u'Evaluated kinetic data for combustion modelling', journal="J. Phys. Chem. Ref. Data", volume="21", pages="""411-429""", year="1992", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 151,
    label = "r00010632",
    reactant1 = 
"""
1  *3 C     0 {2,S}
2  *1 C     0 {1,S} {3,S}
3  *2 O     1 {2,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.98e+13,"s^-1"),
        n = 0,
        Ea = (1163.19,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."], title=u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds', journal="Can. J. Chem.", volume="81", pages="""431-442""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000010.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 152,
    label = "r00010632",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    reactant2 = 
"""
1  *3 C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *3 C     0 {1,S}
3  *2 O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.41e-29,"cm^3/(mol*s)"),
        n = 4.98,
        Ea = (18.5053,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Che, C.-b.", "Zhang, H.", "Zhang, X.", "Liu, Y.", "Liu, B."], title=u'Ab Initio and Kinetic Study on CH_3 Radical Reaction with H_2CO', journal="J. Phys. Chem. A", volume="107", pages="""2929-2933""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000011.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 153,
    label = "r00010633",
    reactant1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,S} {4,S}
3  *2 O     1 {2,S}
4  *3 H     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 O     0 {2,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.51e+14,"s^-1"),
        n = 0,
        Ea = (81149.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Batt, L.", "Milne, R.T."], title=u'The Gas-Phase Pyrolysis of Alkyl Nitrites. IV. Ethyl Nitrite', journal="Int. J. Chem. Kinet.", volume="9", pages="""549""", year="1977", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 154,
    label = "r00010633",
    reactant1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,S} {4,S}
3  *2 O     1 {2,S}
4  *3 H     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 O     0 {2,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.51e+14,"s^-1"),
        n = 0,
        Ea = (98110.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Batt, L."], title=u'The Gas-Phase Decomposition of Alkoxy Radicals', journal="Int. J. Chem. Kinet.", volume="11", pages="""977""", year="1979", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 155,
    label = "r00010633",
    reactant1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,S} {4,S}
3  *2 O     1 {2,S}
4  *3 H     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 O     0 {2,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+14,"s^-1"),
        n = 0,
        Ea = (97279.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Heicklen, J."], title=u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals', journal="Adv. Photochem.", volume="14", pages="""177""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 156,
    label = "r00010633",
    reactant1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,S} {4,S}
3  *2 O     1 {2,S}
4  *3 H     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 O     0 {2,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.46e+13,"s^-1"),
        n = 0,
        Ea = (1447.38,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."], title=u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds', journal="Can. J. Chem.", volume="81", pages="""431-442""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 157,
    label = "r00010706",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {4,D}
3  *2 C     1 {1,S}
4     C     0 {2,D}
5  *3 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,D}
2  *1 C     0 {1,S} {4,D}
3     C     0 {1,D}
4  *2 C     0 {2,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e+13,"s^-1"),
        n = 0,
        Ea = (145503,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Weissman, M.", "Benson, S.W."], title=u'Pyrolysis of methyl chloride, a pathway in the chlorine-catalyzed polymerization of methane', journal="Int. J. Chem. Kinet.", volume="16", pages="""307""", year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:40 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 158,
    label = "r00010737",
    reactant1 = 
"""
1  *3 C     0 {2,S} {5,S}
2     C     0 {1,S}
3     C     0 {4,S}
4  *2 C     1 {3,S} {5,S}
5  *1 O     0 {1,S} {4,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 O     0 {2,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *3 C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+13,"s^-1"),
        n = 0,
        Ea = (73250.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["East, R.L.", "Phillips, L."], title=u'Pressure-dependence of the gas-phase pyrolysis of the s-butoxyl radical at 150-190\xb0', journal="J. Chem. Soc. A", pages="""1939""", year="1967", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:40 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 159,
    label = "r00010737",
    reactant1 = 
"""
1  *3 C     0 {2,S} {5,S}
2     C     0 {1,S}
3     C     0 {4,S}
4  *2 C     1 {3,S} {5,S}
5  *1 O     0 {1,S} {4,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 O     0 {2,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *3 C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.01e+09,"s^-1"),
        n = 0,
        Ea = (66931.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Hohlein, G.", "Freeman, G.R."], title=u'Radiation-sensitized pyrolysis of diethyl ether. Free-radical reaction rate parameters', journal="J. Am. Chem. Soc.", volume="92", pages="""6118""", year="1970", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:40 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 160,
    label = "r00011104",
    reactant1 = 
"""
1     C     0 {2,S} {4,S}
2     C     0 {1,S}
3  *1 C     0 {4,S} {5,S}
4  *2 C     1 {1,S} {3,S}
5  *3 H     0 {3,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *2 C     0 {1,S} {4,D}
4  *1 C     0 {3,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (5e+12,"s^-1"),
        n = 0,
        Ea = (166289,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Lin, M.C.", "Laidler, K.J."], title=u'Thermal decomposition of the sec-butl radical', journal="Can. J. Chem.", volume="45", pages="""1315""", year="1967", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:43 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 161,
    label = "r00011104",
    reactant1 = 
"""
1     C     0 {2,S} {4,S}
2     C     0 {1,S}
3  *1 C     0 {4,S} {5,S}
4  *2 C     1 {1,S} {3,S}
5  *3 H     0 {3,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *2 C     0 {1,S} {4,D}
4  *1 C     0 {3,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.58e+13,"s^-1"),
        n = 0,
        Ea = (165458,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:43 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 162,
    label = "r00011104",
    reactant1 = 
"""
1     C     0 {2,S} {4,S}
2     C     0 {1,S}
3  *1 C     0 {4,S} {5,S}
4  *2 C     1 {1,S} {3,S}
5  *3 H     0 {3,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *2 C     0 {1,S} {4,D}
4  *1 C     0 {3,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.29e+13,"s^-1"),
        n = 0,
        Ea = (152155,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'The stability of alkyl radicals', journal="J. Am. Chem. Soc.", volume="107", pages="""2872""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:43 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 163,
    label = "r00011105",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {4,S}
4  *2 C     1 {1,S} {3,S}
5  *3 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {4,S}
3  *2 C     0 {1,S} {4,D}
4  *1 C     0 {2,S} {3,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e+12,"s^-1"),
        n = 0,
        Ea = (154649,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:43 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 164,
    label = "r00011106",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S}
2  *3 C     0 {1,S}
3     C     0 {4,S}
4  *2 C     1 {1,S} {3,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.5e+11,"s^-1"),
        n = 0,
        Ea = (100605,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Gruver, J.T.", "Calvert, J.C."], title=u'The vapor phase photolysis of 2-methylbutanal at wave length 3130 A', journal="J. Am. Chem. Soc.", volume="78", pages="""5208""", year="1956", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:43 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 165,
    label = "r00011106",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S}
2  *3 C     0 {1,S}
3     C     0 {4,S}
4  *2 C     1 {1,S} {3,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.1e+14,"s^-1"),
        n = 0,
        Ea = (136357,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Lin, M.C.", "Laidler, K.J."], title=u'Thermal decomposition of the sec-butl radical', journal="Can. J. Chem.", volume="45", pages="""1315""", year="1967", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:43 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 166,
    label = "r00011106",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S}
2  *3 C     0 {1,S}
3     C     0 {4,S}
4  *2 C     1 {1,S} {3,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3e+14,"s^-1"),
        n = 0,
        Ea = (137189,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Warnatz, J."], year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:43 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 167,
    label = "r00011106",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S}
2  *3 C     0 {1,S}
3     C     0 {4,S}
4  *2 C     1 {1,S} {3,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.31e+12,"s^-1"),
        n = 0,
        Ea = (135526,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:43 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 168,
    label = "r00011106",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S}
2  *3 C     0 {1,S}
3     C     0 {4,S}
4  *2 C     1 {1,S} {3,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.33e+12,"s^-1"),
        n = 0,
        Ea = (122223,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'The stability of alkyl radicals', journal="J. Am. Chem. Soc.", volume="107", pages="""2872""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:43 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 169,
    label = "r00011106",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S}
2  *3 C     0 {1,S}
3     C     0 {4,S}
4  *2 C     1 {1,S} {3,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.63e+13,"s^-1"),
        n = 0,
        Ea = (133032,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Gierczak, T.", "Gawlowski, J.", "Niedzielski, J."], title=u'Isomerization of chemically activated secondary butyl radical', journal="React. Kinet. Catal. Lett.", volume="36", pages="""435""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:43 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 170,
    label = "r00011106",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S}
2  *3 C     0 {1,S}
3     C     0 {4,S}
4  *2 C     1 {1,S} {3,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.72e+14,"s^-1"),
        n = 0,
        Ea = (138020,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Marshall, R.M."], title=u'The rate constant for the intramolecular isomerization of pentyl radicals', journal="Int. J. Chem. Kinet.", volume="22", pages="""935""", year="1990", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:43 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 171,
    label = "r00011106",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S}
2  *3 C     0 {1,S}
3     C     0 {4,S}
4  *2 C     1 {1,S} {3,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.52e+13,"s^-1"),
        n = 1.11,
        Ea = (130537,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Knyazev, V.D.", "Dubinsky, I.A.", "Slagle, I.R.", "Gutman, D."], title=u'Experimental and theoretical study of the sec-C_4H_9 = CH_3 + C_3H_6 reaction', journal="J. Phys. Chem.", volume="98", pages="""11099-11108""", year="1994", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000008.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:43 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 172,
    label = "r00011106",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S}
2  *3 C     0 {1,S}
3     C     0 {4,S}
4  *2 C     1 {1,S} {3,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.12e+13,"s^-1"),
        n = 1.06,
        Ea = (129706,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Gang, J.", "Pilling, M.J.", "Robertson, S.H."], title=u'Asymmetric internal rotation: application to the 2-C_4H_9=CH_3 + C_3H_6 reaction', journal="J. Chem. Soc. Faraday Trans.", volume="93", pages="""1481-1491""", year="1997", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000010.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:43 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 173,
    label = "r00011106",
    reactant1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    reactant2 = 
"""
1  *3 C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {4,S}
2  *3 C     0 {1,S}
3     C     0 {4,S}
4  *2 C     1 {1,S} {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.94e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (29682.7,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tedder, J.M.", "Walton, J.C.", "Winton, K.D.R."], title=u'Free Radical Addition to Olefins Part 9. Addition of Methyl Radicals to Fluoro-ethylenes', journal="J. Chem. Soc. Faraday Trans. 1", volume="68", pages="""1866""", year="1972", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000013.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:43 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 174,
    label = "r00011106",
    reactant1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    reactant2 = 
"""
1  *3 C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {4,S}
2  *3 C     0 {1,S}
3     C     0 {4,S}
4  *2 C     1 {1,S} {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.78e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (29516.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baldwin, R.R.", "Keen, A.", "Walker, R.W."], title=u'Rate constants for the addition of methyl radicals to propene', journal="J. Chem. Soc. Faraday Trans. 2", volume="83", pages="""759""", year="1987", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000014.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:43 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 175,
    label = "r00011106",
    reactant1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    reactant2 = 
"""
1  *3 C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {4,S}
2  *3 C     0 {1,S}
3     C     0 {4,S}
4  *2 C     1 {1,S} {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.69e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (31013,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part V. Propene', journal="J. Phys. Chem. Ref. Data", volume="20", pages="""221-273""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000016.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:43 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 176,
    label = "r00011106",
    reactant1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    reactant2 = 
"""
1  *3 C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {4,S}
2  *3 C     0 {1,S}
3     C     0 {4,S}
4  *2 C     1 {1,S} {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (128159,"cm^3/(mol*s)"),
        n = 2.28,
        Ea = (27604,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Knyazev, V.D.", "Dubinsky, I.A.", "Slagle, I.R.", "Gutman, D."], title=u'Experimental and theoretical study of the sec-C_4H_9 = CH_3 + C_3H_6 reaction', journal="J. Phys. Chem.", volume="98", pages="""11099-11108""", year="1994", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000017.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:43 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 177,
    label = "r00011107",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {4,S}
4  *2 C     1 {1,S} {3,S}
5  *3 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {4,S}
3  *2 C     0 {1,S} {4,D}
4  *1 C     0 {2,S} {3,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.17e+12,"s^-1"),
        n = 0,
        Ea = (145503,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'The stability of alkyl radicals', journal="J. Am. Chem. Soc.", volume="107", pages="""2872""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:43 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 178,
    label = "r00011107",
    reactant1 = 
"""
1     C     0 {3,S}
2     C     0 {4,S}
3  *1 C     0 {1,S} {4,D}
4  *2 C     0 {2,S} {3,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {4,S}
4  *2 C     1 {1,S} {3,S}
5  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.61e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8023.47,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kyogoku, T.", "Watanabe, T.", "Tsunashima, S.", "Sato, S."], title=u'Arrhenius parameters for the reactions of hydrogen and deuterium atoms with four butenes', journal="Bull. Chem. Soc. Jpn.", volume="56", pages="""19""", year="1983", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:43 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 179,
    label = "r00011108",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {4,S}
4  *2 C     1 {1,S} {3,S}
5  *3 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {4,S}
3  *2 C     0 {1,S} {4,D}
4  *1 C     0 {2,S} {3,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.57e+12,"s^-1"),
        n = 0,
        Ea = (142177,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'The stability of alkyl radicals', journal="J. Am. Chem. Soc.", volume="107", pages="""2872""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:43 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 180,
    label = "r00011108",
    reactant1 = 
"""
1     C     0 {3,S}
2     C     0 {4,S}
3  *1 C     0 {1,S} {4,D}
4  *2 C     0 {2,S} {3,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {4,S}
4  *2 C     1 {1,S} {3,S}
5  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.08e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8647.05,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Harris, G.W.", "Pitts, J.N., Jr."], title=u'Absolute Rate Constants and Temperature Dependences for the Gas Phase Reactions of H Atoms with Propene and the Butenes in the Temperature Range 298 to 445 K', journal="J. Chem. Phys.", volume="77", pages="""3994""", year="1982", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000013.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:43 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 181,
    label = "r00011108",
    reactant1 = 
"""
1     C     0 {3,S}
2     C     0 {4,S}
3  *1 C     0 {1,S} {4,D}
4  *2 C     0 {2,S} {3,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {4,S}
4  *2 C     1 {1,S} {3,S}
5  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.39e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8813.34,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kyogoku, T.", "Watanabe, T.", "Tsunashima, S.", "Sato, S."], title=u'Arrhenius parameters for the reactions of hydrogen and deuterium atoms with four butenes', journal="Bull. Chem. Soc. Jpn.", volume="56", pages="""19""", year="1983", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000014.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:43 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 182,
    label = "r00011148",
    reactant1 = 
"""
1     C     0 {2,B} {3,B}
2     C     0 {1,B} {4,B}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6  *3 C     1 {4,B} {5,B}
""",
    reactant2 = 
"""
1  *2 C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3  *1 C     0 {1,D}
4     C     0 {2,D}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *3 C     0 {1,S} {4,B} {5,B}
3  *2 C     1 {1,S} {9,S}
4     C     0 {2,B} {7,B}
5     C     0 {2,B} {8,B}
6     C     0 {7,B} {8,B}
7     C     0 {4,B} {6,B}
8     C     0 {5,B} {6,B}
9     C     0 {3,S} {10,D}
10    C     0 {9,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.01e+46,"cm^3/(mol*s)"),
        n = -10.2,
        Ea = (272755,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Fascella, S.", "Cavallotti, C.", "Rota, R.", "Carra, S."], title=u'Quantum chemistry investigation of key reactions involved in the formation of naphthalene and indene', journal="J. Phys. Chem. A", volume="108", pages="""3829-3843""", year="2004", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:44 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 183,
    label = "r00011148",
    reactant1 = 
"""
1     C     0 {2,B} {3,B}
2     C     0 {1,B} {4,B}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6  *3 C     1 {4,B} {5,B}
""",
    reactant2 = 
"""
1  *2 C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3  *1 C     0 {1,D}
4     C     0 {2,D}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *3 C     0 {1,S} {4,B} {5,B}
3  *2 C     1 {1,S} {9,S}
4     C     0 {2,B} {7,B}
5     C     0 {2,B} {8,B}
6     C     0 {7,B} {8,B}
7     C     0 {4,B} {6,B}
8     C     0 {5,B} {6,B}
9     C     0 {3,S} {10,D}
10    C     0 {9,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.98e+67,"cm^3/(mol*s)"),
        n = -16.85,
        Ea = (385059,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Fascella, S.", "Cavallotti, C.", "Rota, R.", "Carra, S."], title=u'Quantum chemistry investigation of key reactions involved in the formation of naphthalene and indene', journal="J. Phys. Chem. A", volume="108", pages="""3829-3843""", year="2004", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:44 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 184,
    label = "r00011148",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *3 C     0 {1,S} {4,B} {5,B}
3  *2 C     1 {1,S} {9,S}
4     C     0 {2,B} {7,B}
5     C     0 {2,B} {8,B}
6     C     0 {7,B} {8,B}
7     C     0 {4,B} {6,B}
8     C     0 {5,B} {6,B}
9     C     0 {3,S} {10,D}
10    C     0 {9,D}
""",
    product1 = 
"""
1     C     0 {2,S} {3,D}
2  *2 C     0 {1,S} {4,D}
3     C     0 {1,D}
4  *1 C     0 {2,D}
""",
    product2 = 
"""
1     C     0 {2,B} {3,B}
2     C     0 {1,B} {4,B}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6  *3 C     1 {4,B} {5,B}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.3e+17,"s^-1"),
        n = -1,
        Ea = (807954,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Fascella, S.", "Cavallotti, C.", "Rota, R.", "Carra, S."], title=u'Quantum chemistry investigation of key reactions involved in the formation of naphthalene and indene', journal="J. Phys. Chem. A", volume="108", pages="""3829-3843""", year="2004", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:44 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 185,
    label = "r00011160",
    reactant1 = 
"""
1     C     0 {2,B} {3,B}
2     C     0 {1,B} {4,B}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6  *3 C     1 {4,B} {5,B}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     0 {1,S} {2,D}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,B} {6,B}
4  *2 C     1 {1,S} {2,S}
5     C     0 {3,B} {8,B}
6     C     0 {3,B} {9,B}
7     C     0 {8,B} {9,B}
8     C     0 {5,B} {7,B}
9     C     0 {6,B} {7,B}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.99e-20,"cm^3/(mol*s)"),
        n = 2.57,
        Ea = (22.8012,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Vereecken, L.", "Peeters, J."], title=u'Reactions of chemically activated C9H9 species II: The reaction of phenyl radicals with allene and cyclopropene, and of benzyl radicals with acetylene', journal="Phys. Chem. Chem. Phys.", volume="5", pages="""2807-2817""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
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
    index = 186,
    label = "r00011209",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S}
3     C     0 {1,S}
4  *2 C     1 {2,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *3 C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.58e+11,"s^-1"),
        n = 0,
        Ea = (92290.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kerr, J.A.", "Trotman-Dickenson, A.F."], title=u'The reactions of alkyl radicals. Part III. n-Butyl radicals from the photolysis of n-Valeraldehyde', journal="J. Chem. Soc.", pages="""1602""", year="1960", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:46 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 187,
    label = "r00011209",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S}
3     C     0 {1,S}
4  *2 C     1 {2,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *3 C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.73e+13,"s^-1"),
        n = 0,
        Ea = (119728,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Morganroth, W.E.", "Calvert, J.G."], title=u"The photolysis of 1,1'-azo-n-butane vapor. The reactions of the n-butyl free radical", journal="J. Am. Chem. Soc.", volume="88", pages="""5387""", year="1966", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:46 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 188,
    label = "r00011209",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S}
3     C     0 {1,S}
4  *2 C     1 {2,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *3 C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.7e+13,"s^-1"),
        n = 0,
        Ea = (119728,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Warnatz, J."], year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:46 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 189,
    label = "r00011209",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S}
3     C     0 {1,S}
4  *2 C     1 {2,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *3 C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.01e+12,"s^-1"),
        n = 0,
        Ea = (116403,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:46 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 190,
    label = "r00011209",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S}
3     C     0 {1,S}
4  *2 C     1 {2,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *3 C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.47e+13,"s^-1"),
        n = 0,
        Ea = (121391,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Gierczak, T.", "Gawlowski, J.", "Niedzielski, J."], title=u'Isomerization of chemically activated secondary butyl radical', journal="React. Kinet. Catal. Lett.", volume="36", pages="""435""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:46 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 191,
    label = "r00011209",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S}
3     C     0 {1,S}
4  *2 C     1 {2,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *3 C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.95e+13,"s^-1"),
        n = 0,
        Ea = (119728,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Marshall, R.M."], title=u'The rate constant for the intramolecular isomerization of pentyl radicals', journal="Int. J. Chem. Kinet.", volume="22", pages="""935""", year="1990", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:46 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 192,
    label = "r00011209",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S}
3     C     0 {1,S}
4  *2 C     1 {2,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *3 C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.06e+13,"s^-1"),
        n = 0,
        Ea = (116403,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Knyazev, V.D.", "Slagle, I.R."], title=u'Unimolecular decomposition of n-C_4H_9 and iso-C_4H_9 radicals', journal="J. Phys. Chem.", volume="100", pages="""5318-5328""", year="1996", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000008.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:46 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 193,
    label = "r00011209",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *3 C     1 {1,S}
""",
    product1 = 
"""
1  *3 C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S}
3     C     0 {1,S}
4  *2 C     1 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.12e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (36001.7,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kerr, J.A.", "Trotman-Dickenson, A.F."], title=u'The reactions of alkyl radicals. Part V. Ethyl radicals from propionaldehyde', journal="J. Chem. Soc.", pages="""1611""", year="1960", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000011.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:46 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 194,
    label = "r00011209",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *3 C     1 {1,S}
""",
    product1 = 
"""
1  *3 C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S}
3     C     0 {1,S}
4  *2 C     1 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.9e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (27188.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Morganroth, W.E.", "Calvert, J.G."], title=u"The photolysis of 1,1'-azo-n-butane vapor. The reactions of the n-butyl free radical", journal="J. Am. Chem. Soc.", volume="88", pages="""5387""", year="1966", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000012.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:46 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 195,
    label = "r00011209",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *3 C     1 {1,S}
""",
    product1 = 
"""
1  *3 C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S}
3     C     0 {1,S}
4  *2 C     1 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.48e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (31595,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Watkins, K.W.", "O'Deen, L.A."], title=u'Kinetics of the addition of ethyl, isopropyl, n-butyl, and isopentyl radicals to ethylene', journal="J. Phys. Chem.", volume="73", pages="""4094-4102""", year="1969", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000013.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:46 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 196,
    label = "r00011209",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *3 C     1 {1,S}
""",
    product1 = 
"""
1  *3 C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S}
3     C     0 {1,S}
4  *2 C     1 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3975.58,"cm^3/(mol*s)"),
        n = 2.44,
        Ea = (22449.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Knyazev, V.D.", "Slagle, I.R."], title=u'Unimolecular decomposition of n-C_4H_9 and iso-C_4H_9 radicals', journal="J. Phys. Chem.", volume="100", pages="""5318-5328""", year="1996", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000014.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:46 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 197,
    label = "r00011210",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S} {5,S}
3     C     0 {1,S}
4  *2 C     1 {2,S}
5  *3 H     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *1 C     0 {1,S} {4,D}
4  *2 C     0 {3,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+14,"s^-1"),
        n = 0,
        Ea = (167121,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Lin, M.C.", "Back, M.H."], title=u'The thermal decomposition of ethane. Part III. Secondary reactions', journal="Can. J. Chem.", volume="44", pages="""2369""", year="1966", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:46 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 198,
    label = "r00011210",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S} {5,S}
3     C     0 {1,S}
4  *2 C     1 {2,S}
5  *3 H     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *1 C     0 {1,S} {4,D}
4  *2 C     0 {3,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.51e+13,"s^-1"),
        n = 0,
        Ea = (148829,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["MacKenzie, A.L.", "Pacey, P.D.", "Wimalasena, J.H."], title=u'Radical addition, decomposition, and isomerization reactions in the pyrolysis of ethane and ethylene', journal="Can. J. Chem.", volume="62", pages="""1325""", year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:46 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 199,
    label = "r00011210",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S} {5,S}
3     C     0 {1,S}
4  *2 C     1 {2,S}
5  *3 H     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *1 C     0 {1,S} {4,D}
4  *2 C     0 {3,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+14,"s^-1"),
        n = 0,
        Ea = (160469,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:46 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 200,
    label = "r00011210",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *1 C     0 {1,S} {4,D}
4  *2 C     0 {3,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S} {5,S}
3     C     0 {1,S}
4  *2 C     1 {2,S}
5  *3 H     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.49e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (6244.17,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kyogoku, T.", "Watanabe, T.", "Tsunashima, S.", "Sato, S."], title=u'Arrhenius parameters for the reactions of hydrogen and deuterium atoms with four butenes', journal="Bull. Chem. Soc. Jpn.", volume="56", pages="""19""", year="1983", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:46 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 201,
    label = "r00011228",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *1 C     0 {1,S} {6,S}
4     C     0 {2,S}
5     C     0 {6,S}
6  *2 C     1 {3,S} {5,S}
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
2     C     0 {1,S}
3  *3 C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13,"s^-1"),
        n = 0,
        Ea = (93953.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Quinn, C.P."], title=u'Isomerization of primary n-alkyl radicals in the pyrolysis of ethane', journal="J. Chem. Soc. Faraday Trans. 2", volume="59", pages="""2543""", year="1963", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:46 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 202,
    label = "r00011228",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *1 C     0 {1,S} {6,S}
4     C     0 {2,S}
5     C     0 {6,S}
6  *2 C     1 {3,S} {5,S}
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
2     C     0 {1,S}
3  *3 C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+13,"s^-1"),
        n = 0,
        Ea = (108920,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Lin, M.C.", "Back, M.H."], title=u'The thermal decomposition of ethane. Part III. Secondary reactions', journal="Can. J. Chem.", volume="44", pages="""2369""", year="1966", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:46 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 203,
    label = "r00011228",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *1 C     0 {1,S} {6,S}
4     C     0 {2,S}
5     C     0 {6,S}
6  *2 C     1 {3,S} {5,S}
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
2     C     0 {1,S}
3  *3 C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13,"s^-1"),
        n = 0,
        Ea = (125549,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Imbert, F.E.", "Marshall, R.M."], title=u'The mechanism and rate parameters for the pyrolysis of n-hexane in the range 723-823 K', journal="Int. J. Chem. Kinet.", volume="19", pages="""81""", year="1987", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:46 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 204,
    label = "r00011282",
    reactant1 = 
"""
1  *2 C     1 {2,S}
2  *1 O     0 {1,S} {3,S}
3  *3 H     0 {2,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 O     0 {1,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+09,"s^-1"),
        n = 0,
        Ea = (121391,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Bowman, C.T."], title=u'A Shock-Tube Investigation of the High-Temperature Oxidation of Methanol', journal="Combust. Flame", volume="25", pages="""343""", year="1975", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:46 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 205,
    label = "r00011282",
    reactant1 = 
"""
1  *2 C     1 {2,S}
2  *1 O     0 {1,S} {3,S}
3  *3 H     0 {2,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 O     0 {1,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.6e+10,"s^-1"),
        n = 0,
        Ea = (121391,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsuboi, T.", "Katoh, M.", "Kikuchi, S.", "Hashimoto, K."], title=u'Thermal Decomposition of Methanol behind Shock Waves', journal="Jpn. J. Appl. Phys.", volume="20", pages="""985""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:46 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 206,
    label = "r00011282",
    reactant1 = 
"""
1  *2 C     1 {2,S}
2  *1 O     0 {1,S} {3,S}
3  *3 H     0 {2,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 O     0 {1,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+14,"s^-1"),
        n = 0,
        Ea = (123886,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Greenhill, P.G.", "O'Grady, B.V.", "Gilbert, R.G."], title=u'Theoretical prediction of CH_3O and CH_2OH gas phase decomposition rate coefficients', journal="Aust. J. Chem.", volume="39", pages="""1929""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:46 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 207,
    label = "r00011282",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *1 O     0 {1,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *2 C     1 {2,S}
2  *1 O     0 {1,S} {3,S}
3  *3 H     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.27e+32,"cm^3/(mol*s)"),
        n = -4.82,
        Ea = (6530,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000010.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:46 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 208,
    label = "r00011282",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *1 O     0 {1,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *2 C     1 {2,S}
2  *1 O     0 {1,S} {3,S}
3  *3 H     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.54e+32,"cm^3/(mol*s)"),
        n = -4.82,
        Ea = (6530,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000011.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:46 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 209,
    label = "r00011282",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *1 O     0 {1,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *2 C     1 {2,S}
2  *1 O     0 {1,S} {3,S}
3  *3 H     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.62e+32,"cm^3/(mol*s)"),
        n = -4.82,
        Ea = (6530,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000012.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:46 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 210,
    label = "r00011282",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *1 O     0 {1,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *2 C     1 {2,S}
2  *1 O     0 {1,S} {3,S}
3  *3 H     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.54e+32,"cm^3/(mol*s)"),
        n = -4.82,
        Ea = (6530,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000013.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:46 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 211,
    label = "r00011282",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *1 O     0 {1,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *2 C     1 {2,S}
2  *1 O     0 {1,S} {3,S}
3  *3 H     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.905e+32,"cm^3/(mol*s)"),
        n = -4.82,
        Ea = (6530,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000014.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:46 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 212,
    label = "r00011282",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *1 O     0 {1,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *2 C     1 {2,S}
2  *1 O     0 {1,S} {3,S}
3  *3 H     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.54e+32,"cm^3/(mol*s)"),
        n = -4.82,
        Ea = (6530,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000015.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:46 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 213,
    label = "r00011282",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *1 O     0 {1,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *2 C     1 {2,S}
2  *1 O     0 {1,S} {3,S}
3  *3 H     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.81e+32,"cm^3/(mol*s)"),
        n = -4.82,
        Ea = (6530,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000016.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:46 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 214,
    label = "r00011282",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *1 O     0 {1,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *2 C     1 {2,S}
2  *1 O     0 {1,S} {3,S}
3  *3 H     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.4e+11,"cm^3/(mol*s)"),
        n = 0.454,
        Ea = (3600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000017.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:46 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 215,
    label = "r00011282",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *1 O     0 {1,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *2 C     1 {2,S}
2  *1 O     0 {1,S} {3,S}
3  *3 H     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.26e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (4997,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsuboi, T.", "Katoh, M.", "Kikuchi, S.", "Hashimoto, K."], title=u'Thermal Decomposition of Methanol behind Shock Waves', journal="Jpn. J. Appl. Phys.", volume="20", pages="""985""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000019.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:46 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 216,
    label = "r00011402",
    reactant1 = 
"""
1  *1 C     0 {2,D} {3,S}
2  *2 C     1 {1,D}
3  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,T}
2  *1 C     0 {1,T}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.6e+14,"s^-1"),
        n = 0,
        Ea = (158806,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Warnatz, J."], year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 217,
    label = "r00011402",
    reactant1 = 
"""
1  *1 C     0 {2,D} {3,S}
2  *2 C     1 {1,D}
3  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,T}
2  *1 C     0 {1,T}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+11,"s^-1"),
        n = 0,
        Ea = (168784,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Weissman, M.", "Benson, S.W."], title=u'Pyrolysis of methyl chloride, a pathway in the chlorine-catalyzed polymerization of methane', journal="Int. J. Chem. Kinet.", volume="16", pages="""307""", year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 218,
    label = "r00011402",
    reactant1 = 
"""
1  *1 C     0 {2,D} {3,S}
2  *2 C     1 {1,D}
3  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,T}
2  *1 C     0 {1,T}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e+12,"s^-1"),
        n = 0,
        Ea = (160469,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 219,
    label = "r00011402",
    reactant1 = 
"""
1  *1 C     0 {2,D} {3,S}
2  *2 C     1 {1,D}
3  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,T}
2  *1 C     0 {1,T}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.29e+13,"s^-1"),
        n = 0,
        Ea = (192064,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Naroznik, M.", "Niedzielski, J."], title=u'Propylene photolysis at 6.7 eV: Calculation of the quantum yields for the secondary processes', journal="J. Photochem.", volume="32", pages="""281""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000008.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 220,
    label = "r00011402",
    reactant1 = 
"""
1  *1 C     0 {2,D} {3,S}
2  *2 C     1 {1,D}
3  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,T}
2  *1 C     0 {1,T}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+13,"s^-1"),
        n = 0,
        Ea = (172110,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Manion, J.A.", "Louw, R."], title=u'Gas-phase hydrogenolysis of chloroethene: Rates, products, and computer modelling', journal="J. Chem. Soc. Perkin Trans. 2", pages="""1547-1555""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000012.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 221,
    label = "r00011402",
    reactant1 = 
"""
1  *1 C     0 {2,D} {3,S}
2  *2 C     1 {1,D}
3  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,T}
2  *1 C     0 {1,T}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.93e+12,"s^-1"),
        n = 0,
        Ea = (186244,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Rao, V.S.", "Skinner, G.B."], title=u'Reactions of vinyl radicals at high temperatures: Pyrolysis of vinyl bromide and vinyl iodide and the reaction H + C_2D_2 \u2192 D + C_2HD', journal="J. Phys. Chem.", volume="92", pages="""6313""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000013.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 222,
    label = "r00011402",
    reactant1 = 
"""
1  *1 C     0 {2,D} {3,S}
2  *2 C     1 {1,D}
3  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,T}
2  *1 C     0 {1,T}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+14,"s^-1"),
        n = 0,
        Ea = (166289,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Esser, C.", "Frank, P.", "Just, Th.", "Kerr, J.A.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."], title=u'Evaluated kinetic data for combustion modelling', journal="J. Phys. Chem. Ref. Data", volume="21", pages="""411-429""", year="1992", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000016.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 223,
    label = "r00011402",
    reactant1 = 
"""
1  *1 C     0 {2,D} {3,S}
2  *2 C     1 {1,D}
3  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,T}
2  *1 C     0 {1,T}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.94e+12,"s^-1"),
        n = 1.62,
        Ea = (154649,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Knyazev, V.D.", "Slagle, I.R."], title=u'Experimental and theoretical study of the C_2H_3 = H + C_2H_2 reaction. Tunneling and the shape of falloff curves', journal="J. Phys. Chem.", volume="100", pages="""16899-16911""", year="1996", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000018.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 224,
    label = "r00011402",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,S}
2  *2 C     1 {1,D}
3  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.8e+40,"cm^3/(mol*s)"),
        n = -7.27,
        Ea = (7220,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000019.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 225,
    label = "r00011402",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,S}
2  *2 C     1 {1,D}
3  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.6e+40,"cm^3/(mol*s)"),
        n = -7.27,
        Ea = (7220,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000020.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 226,
    label = "r00011402",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,S}
2  *2 C     1 {1,D}
3  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.28e+41,"cm^3/(mol*s)"),
        n = -7.27,
        Ea = (7220,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000021.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 227,
    label = "r00011402",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,S}
2  *2 C     1 {1,D}
3  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.6e+40,"cm^3/(mol*s)"),
        n = -7.27,
        Ea = (7220,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000022.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 228,
    label = "r00011402",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,S}
2  *2 C     1 {1,D}
3  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.7e+40,"cm^3/(mol*s)"),
        n = -7.27,
        Ea = (7220,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000023.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 229,
    label = "r00011402",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,S}
2  *2 C     1 {1,D}
3  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.6e+40,"cm^3/(mol*s)"),
        n = -7.27,
        Ea = (7220,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000024.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 230,
    label = "r00011402",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,S}
2  *2 C     1 {1,D}
3  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.14e+41,"cm^3/(mol*s)"),
        n = -7.27,
        Ea = (7220,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000025.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 231,
    label = "r00011402",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,S}
2  *2 C     1 {1,D}
3  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.66e+40,"cm^3/(mol*s)"),
        n = -7.27,
        Ea = (7220,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000026.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 232,
    label = "r00011402",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,S}
2  *2 C     1 {1,D}
3  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.6e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (2400,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000027.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 233,
    label = "r00011402",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,S}
2  *2 C     1 {1,D}
3  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.3e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (10476.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Hoyermann, K.", "Wagner, H.Gg.", "Wolfrum, J."], title=u'Die geschwindigkeit der reaktion von atomarem Wasserstoff mit azetylen', journal="Ber. Bunsenges. Phys. Chem.", volume="72", pages="""1004""", year="1968", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000034.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 234,
    label = "r00011402",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,S}
2  *2 C     1 {1,D}
3  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.55e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (10060.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Payne, W.A.", "Stief, L.J."], title=u'Absolute Rate Constant for the Reaction of Atomic Hydrogen with Acetylene over an Extended Pressure and Temperature Range', journal="J. Chem. Phys.", volume="64", pages="""1150""", year="1976", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000037.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 235,
    label = "r00011402",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,S}
2  *2 C     1 {1,D}
3  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.43e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (11307.7,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Ellul, R.", "Potzinger, P.", "Reimann, B.", "Camilleri, P."], title=u'Arrhenius parameters for the system (CH_3)_3Si + D_2 = (CH_3)_3SiD + D. The (CH_3)_3Si-D bond dissociation energy', journal="Ber. Bunsenges. Phys. Chem.", volume="85", pages="""407""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000040.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 236,
    label = "r00011402",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,S}
2  *2 C     1 {1,D}
3  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.29e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (11390.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Sugawara, K.", "Okazaki, K.", "Sato, S."], title=u'Temperature Dependence of the Rate Constants of H and D-Atom Additions to C_2H_4, C_2H_3D, C_2D_4, C_2H_2, and C_2D_2', journal="Bull. Chem. Soc. Jpn.", volume="54", pages="""2872""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000042.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 237,
    label = "r00011402",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,S}
2  *2 C     1 {1,D}
3  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (10143.7,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Warnatz, J."], year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000043.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 238,
    label = "r00011402",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,S}
2  *2 C     1 {1,D}
3  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.43e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (10808.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Esser, C.", "Frank, P.", "Just, Th.", "Kerr, J.A.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."], title=u'Evaluated kinetic data for combustion modelling', journal="J. Phys. Chem. Ref. Data", volume="21", pages="""411-429""", year="1992", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000046.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 239,
    label = "r00011402",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,S}
2  *2 C     1 {1,D}
3  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.63733e+10,"cm^3/(mol*s)"),
        n = 1.09,
        Ea = (11058.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Knyazev, V.D.", "Slagle, I.R."], title=u'Experimental and theoretical study of the C_2H_3 = H + C_2H_2 reaction. Tunneling and the shape of falloff curves', journal="J. Phys. Chem.", volume="100", pages="""16899-16911""", year="1996", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000048.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 240,
    label = "r00011527",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,D} {5,S}
2     C     0 {1,S} {4,T}
3  *2 C     1 {1,D}
4     C     0 {2,T}
5  *3 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,T}
2  *1 C     0 {1,S} {4,T}
3     C     0 {1,T}
4  *2 C     0 {2,T}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14,"s^-1"),
        n = 0,
        Ea = (167121,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Back, M.H."], title=u'Mechanism of the pyrolysis of acetylene', journal="Can. J. Chem.", volume="49", pages="""2199""", year="1971", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:48 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 241,
    label = "r00011527",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,D} {5,S}
2     C     0 {1,S} {4,T}
3  *2 C     1 {1,D}
4     C     0 {2,T}
5  *3 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,T}
2  *1 C     0 {1,S} {4,T}
3     C     0 {1,T}
4  *2 C     0 {2,T}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14,"s^-1"),
        n = 0,
        Ea = (170447,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Weissman, M.", "Benson, S.W."], title=u'Pyrolysis of methyl chloride, a pathway in the chlorine-catalyzed polymerization of methane', journal="Int. J. Chem. Kinet.", volume="16", pages="""307""", year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:48 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 242,
    label = "r00011527",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,D} {5,S}
2     C     0 {1,S} {4,T}
3  *2 C     1 {1,D}
4     C     0 {2,T}
5  *3 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,T}
2  *1 C     0 {1,S} {4,T}
3     C     0 {1,T}
4  *2 C     0 {2,T}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.28e+27,"s^-1"),
        n = -13.9,
        Ea = (256917,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Braun-Unkhoff, M.", "Frank, P.", "Just, Th."], title=u'A shock tube study on the thermal decomposition of toluene and of the phenyl radical at high temperatures', journal="Symp. Int. Combust. Proc.", volume="22", pages="""1053""", year="1989", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:48 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 243,
    label = "r00011689",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *2 O     1 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 O     0 {3,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (5.01e+09,"s^-1"),
        n = 0,
        Ea = (55208.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Birss, F.W.", "Danby, C.J.", "Hinshelwood, C."], title=u'The thermal dissociation of tertiary butyl peroxide in presence of nitric oxide', journal="Proc. R. Soc. London A", volume="239", pages="""154-164""", year="1957", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:50 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 244,
    label = "r00011689",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *2 O     1 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 O     0 {3,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1e+11,"s^-1"),
        n = 0,
        Ea = (46062.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["McMillan, G.R."], title=u'Photolysis of di-t-butyl peroxide-azomethane and ei-t-butyl peroxide-isobutane mixtures', journal="J. Am. Chem. Soc.", volume="82", pages="""2422""", year="1960", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:50 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 245,
    label = "r00011689",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *2 O     1 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 O     0 {3,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (5.01e+14,"s^-1"),
        n = 0,
        Ea = (95616.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Quee, M.J.Y.", "Thynne, J.C.J."], title=u'Pressure-dependence of decomposition of tert-butoxyl radical', journal="J. Chem. Soc. Faraday Trans.", volume="63", pages="""2970""", year="1967", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:50 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 246,
    label = "r00011689",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *2 O     1 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 O     0 {3,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (5.01e+14,"s^-1"),
        n = 0,
        Ea = (95616.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Yee Quee, M.J.", "Thynne, J.C.J."], title=u'Pressure-dependence of decomposition of tert-butoxyl radical', journal="Trans. Faraday Soc.", volume="63", pages="""2970-2974""", year="1967", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:50 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 247,
    label = "r00011689",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *2 O     1 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 O     0 {3,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.34e+13,"s^-1"),
        n = 0,
        Ea = (70174.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Cadman, P.", "Trotman-Dickenson, A.F.", "White, A.J."], title=u'Kinetics and Pressure-Dependence of the t-Butoxyl Radical Decomposition', journal="J. Chem. Soc. A", pages="""2296""", year="1971", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000009.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:50 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 248,
    label = "r00011689",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *2 O     1 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 O     0 {3,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (3.98e+15,"s^-1"),
        n = 0,
        Ea = (71504.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Batt, L.", "McCulloch, R.D.", "Milne, R.T."], title=u'Thermochemical and Kinetic Studies of Alkyl Nitrites (RONO)-D(RO-NO), The Reactions between RO. and NO, and the Decomposition RO.', journal="Proc. Symp. Chem. Kinet. Data Upper Lower Atmos. 1974", pages="""441""", year="1975", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000010.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:50 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 249,
    label = "r00011689",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *2 O     1 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 O     0 {3,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (5.01e+15,"s^-1"),
        n = 0,
        Ea = (71171.9,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Batt, L.", "Milne, R.T."], title=u'The Gas Phase Pyrolysis of Alkyl Nitrites. I. t-Butyl Nitrite', journal="Int. J. Chem. Kinet.", volume="8", pages="""59""", year="1976", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000011.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:50 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 250,
    label = "r00011689",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *2 O     1 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 O     0 {3,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.58e+15,"s^-1"),
        n = 0,
        Ea = (66515.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baldwin, A.C.", "Barker, J.R.", "Golden, D.M.", "Hendry, D.G."], title=u'Photochemical smog. Rate parameter estimates and computer simulations', journal="J. Phys. Chem.", volume="81", pages="""2483""", year="1977", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000012.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:50 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 251,
    label = "r00011689",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *2 O     1 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 O     0 {3,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (3.16e+15,"s^-1"),
        n = 0,
        Ea = (71171.9,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Batt, L."], title=u'The Gas-Phase Decomposition of Alkoxy Radicals', journal="Int. J. Chem. Kinet.", volume="11", pages="""977""", year="1979", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000013.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:50 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 252,
    label = "r00011689",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *2 O     1 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 O     0 {3,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.26e+14,"s^-1"),
        n = 0,
        Ea = (64021.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Choo, K.Y.", "Benson, S.W."], title=u'Arrhenius Parameters for the Alkoxy Radical Decomposition Reactions', journal="Int. J. Chem. Kinet.", volume="13", pages="""833""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000014.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:50 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 253,
    label = "r00011689",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *2 O     1 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 O     0 {3,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (7.94e+14,"s^-1"),
        n = 0,
        Ea = (69425.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Batt, L.", "Robinson, G.N."], title=u'Arrhenius Parameters for the Decomposition of the t-Butoxy Radical', journal="Int. J. Chem. Kinet.", volume="14", pages="""1053""", year="1982", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000015.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:50 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 254,
    label = "r00011689",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *2 O     1 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 O     0 {3,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (3.98e+14,"s^-1"),
        n = 0,
        Ea = (66515.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Batt, L.", "Robinson, G.N."], title=u'Arrhenius Parameters for the Decomposition of the t-Butoxy Radical', journal="Int. J. Chem. Kinet.", volume="14", pages="""1053""", year="1982", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000016.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:50 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 255,
    label = "r00011689",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *2 O     1 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 O     0 {3,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (3.98e+14,"s^-1"),
        n = 0,
        Ea = (66515.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Batt, L.", "Robinson, G.N."], title=u'Decomposition of the t-butoxy radical', journal="Phys. Chem. Behav. Atmos. Pollut. Proc. Eur. Symp.", pages="""172""", year="1982", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000017.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:50 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 256,
    label = "r00011689",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *2 O     1 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 O     0 {3,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (7.94e+14,"s^-1"),
        n = 0,
        Ea = (69425.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Batt, L.", "Robinson, G.N."], title=u'Decomposition of the t-butoxy radical', journal="Phys. Chem. Behav. Atmos. Pollut. Proc. Eur. Symp.", pages="""172""", year="1982", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000018.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:50 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 257,
    label = "r00011689",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *2 O     1 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 O     0 {3,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (3.98e+14,"s^-1"),
        n = 0,
        Ea = (66931.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Batt, L.", "Robinson, G.N."], title=u'Decomposition of the t-Butoxy radical. I. Studies over the temperature range 402-443 K', journal="Int. J. Chem. Kinet.", volume="19", pages="""391""", year="1987", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000019.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:50 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 258,
    label = "r00011689",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *2 O     1 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 O     0 {3,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1e+15,"s^-1"),
        n = 0,
        Ea = (69010.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Heicklen, J."], title=u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals', journal="Adv. Photochem.", volume="14", pages="""177""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000020.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:50 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 259,
    label = "r00011689",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *2 O     1 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 O     0 {3,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.1e+14,"s^-1"),
        n = 0,
        Ea = (62524.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Batt, L.", "Hisham, M.W.M.", "Mackay, M."], title=u'Decomposition of the t-butoxy radical: II. Studies over the temperature range 303-393 K', journal="Int. J. Chem. Kinet.", volume="21", pages="""535""", year="1989", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000021.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:50 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 260,
    label = "r00011689",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *2 O     1 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 O     0 {3,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.15e+13,"s^-1"),
        n = 0,
        Ea = (940.134,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."], title=u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds', journal="Can. J. Chem.", volume="81", pages="""431-442""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000023.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:50 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 261,
    label = "r00011689",
    reactant1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 O     0 {3,D}
""",
    reactant2 = 
"""
1  *3 C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *3 C     0 {1,S}
5  *2 O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.74e+09,"cm^3/(mol*s)"),
        n = 0,
        Ea = (56289,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Cadman, P.", "Trotman-Dickenson, A.F.", "White, A.J."], title=u'Kinetics and Pressure-Dependence of the t-Butoxyl Radical Decomposition', journal="J. Chem. Soc. A", pages="""2296""", year="1971", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000024.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:50 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 262,
    label = "r00011689",
    reactant1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 O     0 {3,D}
""",
    reactant2 = 
"""
1  *3 C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *3 C     0 {1,S}
5  *2 O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.16e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (48140.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Knoll, H.", "Richter, G.", "Schliebs, R."], title=u'On the Gas-Phase Free Radical Displacement Reaction CH_3 + CD_3COCD_3 \u2192 CD_3 + CH_3COCD_3', journal="Int. J. Chem. Kinet.", volume="12", pages="""623""", year="1980", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000025.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:50 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 263,
    label = "r00011862",
    reactant1 = 
"""
1     O     0 {2,S}
2  *3 O     1 {1,S}
""",
    reactant2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 C     0 {3,D}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *2 C     1 {1,S}
5  *3 O     0 {1,S} {6,S}
6     O     0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.06e+09,"cm^3/(mol*s)"),
        n = 2.10058,
        Ea = (124.58,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Chen, C.-J.", "Bozzelli, J.W."], title=u'Analysis of Tertiary Butyl Radical + O_2, Isobutene + HO_2, Isobutene + OH, and Isobutene-OH Adducts + O_2: A Detailed Tertiary Butyl Oxidation Mechanism', journal="J. Phys. Chem. A", volume="103", pages="""9731-9769""", year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:51 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 264,
    label = "r00011972",
    reactant1 = 
"""
1     C     0 {3,S} {5,S}
2  *1 C     0 {4,S} {5,S}
3     C     0 {1,S}
4  *2 C     1 {2,S}
5  *3 O     0 {1,S} {2,S}
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
3  *3 O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+11,"s^-1"),
        n = 0,
        Ea = (100605,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Foucaut, J.-F.", "Martin, R."], title=u"No. 18. - Etude analytique et cinetique de la pyrolyse de l'ether ethylique vers 500 \xb0C et a faible avancement", journal="J. Chim. Phys.", volume="75", pages="""132""", year="1978", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:51 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 265,
    label = "r00012477",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *2 C     1 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 C     0 {3,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.5e+13,"s^-1"),
        n = 0,
        Ea = (121391,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Furimsky, E.", "Laidler, K.J."], title=u'Kinetics of the Mercury- Photosensitized Decomposition of Neopentane. Part II. Reactions of the Methyl and Neopentyl Radicals', journal="Can. J. Chem.", volume="50", pages="""1123""", year="1972", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:53 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 266,
    label = "r00012477",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *2 C     1 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 C     0 {3,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2e+13,"s^-1"),
        n = 0,
        Ea = (124717,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Szirovicza, L.", "Marta, F."], title=u'Kinetics of the Decomposition of neo-Pentane Sensitized by Azoisopropane', journal="React. Kinet. Catal. Lett.", volume="3", pages="""9""", year="1975", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:53 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 267,
    label = "r00012477",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *2 C     1 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 C     0 {3,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1e+13,"s^-1"),
        n = 0,
        Ea = (125549,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Muller, J.", "Baronnet, F.", "Scacchi, G.", "Dzierzynski, M.", "Niclause, M."], title=u'Influences of ClH and BrH on the Pyrolyses of Neopentane and Ethane at Small Extents of Reaction', journal="Int. J. Chem. Kinet.", volume="9", pages="""425""", year="1977", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:53 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 268,
    label = "r00012477",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *2 C     1 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 C     0 {3,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.51e+13,"s^-1"),
        n = 0,
        Ea = (123886,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Szirovicza, L.", "Marta, F."], title=u'Kinetics of the Decomposition of Neopentane Sensitized by Azoisopropane', journal="Magy. Kem. Foly.", volume="85", pages="""369""", year="1979", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:53 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 269,
    label = "r00012477",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *2 C     1 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 C     0 {3,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (4.45e+13,"s^-1"),
        n = 0,
        Ea = (127211,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baldwin, R.R.", "Hisham, M.W.M.", "Walker, R.W."], title=u'Arrhenius parameters of elementary reactions involved in the oxidation of neopentane', journal="J. Chem. Soc. Faraday Trans. 1", volume="78", pages="""1615""", year="1982", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:53 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 270,
    label = "r00012477",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *2 C     1 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 C     0 {3,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.07e+13,"s^-1"),
        n = 0,
        Ea = (124717,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'The stability of alkyl radicals', journal="J. Am. Chem. Soc.", volume="107", pages="""2872""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000008.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:53 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 271,
    label = "r00012477",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *2 C     1 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 C     0 {3,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (7.94e+13,"s^-1"),
        n = 0,
        Ea = (128874,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Slagle, I.R.", "Batt, L.", "Gmurczyk, G.W.", "Gutman, D."], title=u'Unimolecular decomposition of the neopentyl radical', journal="J. Phys. Chem.", volume="95", pages="""7732-7739""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000009.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:53 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 272,
    label = "r00012477",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *2 C     1 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 C     0 {3,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.21e+10,"s^-1"),
        n = 1.085,
        Ea = (492.042,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Sun, H.", "Bozzelli, J.W."], title=u'Thermochemical and kinetic analysis on the reactions of neopentyl and hydroperoxy-neopentyl radicals with oxygen: Part I.  OH and initial stable HC product formation', journal="J. Phys. Chem. A", volume="108", pages="""1694-1711""", year="2004", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000011.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:53 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 273,
    label = "r00012477",
    reactant1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 C     0 {3,D}
""",
    reactant2 = 
"""
1  *3 C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *3 C     0 {1,S}
5  *2 C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.23e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (44316.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Slagle, I.R.", "Batt, L.", "Gmurczyk, G.W.", "Gutman, D."], title=u'Unimolecular decomposition of the neopentyl radical', journal="J. Phys. Chem.", volume="95", pages="""7732-7739""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000012.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:53 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 274,
    label = "r00012570",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *2 O     1 {1,S}
5  *3 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 O     0 {3,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.7e+12,"s^-1"),
        n = 0,
        Ea = (79902.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Liu, M.T.H.", "Laidler, K.J."], title=u'Elementary processes in the acetaldehyde pyrolysis', journal="Can. J. Chem.", volume="46", pages="""479""", year="1968", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:54 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 275,
    label = "r00012570",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *2 O     1 {1,S}
5  *3 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 O     0 {3,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+14,"s^-1"),
        n = 0,
        Ea = (89796.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Batt, L."], title=u'The Gas-Phase Decomposition of Alkoxy Radicals', journal="Int. J. Chem. Kinet.", volume="11", pages="""977""", year="1979", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:54 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 276,
    label = "r00012570",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *2 O     1 {1,S}
5  *3 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 O     0 {3,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+14,"s^-1"),
        n = 0,
        Ea = (89796.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Heicklen, J."], title=u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals', journal="Adv. Photochem.", volume="14", pages="""177""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:54 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 277,
    label = "r00012570",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *2 O     1 {1,S}
5  *3 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 O     0 {3,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.58e+13,"s^-1"),
        n = 0,
        Ea = (1265.63,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."], title=u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds', journal="Can. J. Chem.", volume="81", pages="""431-442""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:54 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 278,
    label = "r00012571",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4  *2 O     1 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 O     0 {2,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.5e+10,"s^-1"),
        n = 0,
        Ea = (66931.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Ferguson, J.M.", "Phillips, L."], title=u'Reactions of the isopropoxyl radical. Part I. Pyrolysis of isopropyl nitrite in a static system at 175-200\xb0', journal="J. Chem. Soc.", pages="""4416""", year="1965", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:54 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 279,
    label = "r00012571",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4  *2 O     1 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 O     0 {2,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.31e+11,"s^-1"),
        n = 0,
        Ea = (72335.9,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Cox, D.L.", "Livermore, R.A.", "Phillips, L."], title=u'Reactions of the isopropoxyl radical. Part II. Pressure dependence and kinetics of pyrolysis at 160-200\xb0 in the gas phase', journal="J. Chem. Soc. London B", pages="""245-249""", year="1966", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:54 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 280,
    label = "r00012571",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4  *2 O     1 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 O     0 {2,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.26e+12,"s^-1"),
        n = 0,
        Ea = (67347.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Yee Quee, M.J.", "Thynne, J.C.J."], title=u'The pressure dependence of the decomposition of the isopropoxyl radical', journal="J. Phys. Chem.", volume="72", pages="""2824""", year="1968", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:54 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 281,
    label = "r00012571",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4  *2 O     1 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 O     0 {2,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.51e+14,"s^-1"),
        n = 0,
        Ea = (71504.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Batt, L.", "McCulloch, R.D.", "Milne, R.T."], title=u'Thermochemical and Kinetic Studies of Alkyl Nitrites (RONO)-D(RO-NO), The Reactions between RO. and NO, and the Decomposition RO.', journal="Proc. Symp. Chem. Kinet. Data Upper Lower Atmos. 1974", pages="""441""", year="1975", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:54 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 282,
    label = "r00012571",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4  *2 O     1 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 O     0 {2,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.98e+14,"s^-1"),
        n = 0,
        Ea = (74497.7,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baldwin, A.C.", "Barker, J.R.", "Golden, D.M.", "Hendry, D.G."], title=u'Photochemical smog. Rate parameter estimates and computer simulations', journal="J. Phys. Chem.", volume="81", pages="""2483""", year="1977", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:54 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 283,
    label = "r00012571",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4  *2 O     1 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 O     0 {2,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.98e+14,"s^-1"),
        n = 0,
        Ea = (72003.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Batt, L."], title=u'The Gas-Phase Decomposition of Alkoxy Radicals', journal="Int. J. Chem. Kinet.", volume="11", pages="""977""", year="1979", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000008.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:54 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 284,
    label = "r00012571",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4  *2 O     1 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 O     0 {2,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.31e+13,"s^-1"),
        n = 0,
        Ea = (70257.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Choo, K.Y.", "Benson, S.W."], title=u'Arrhenius Parameters for the Alkoxy Radical Decomposition Reactions', journal="Int. J. Chem. Kinet.", volume="13", pages="""833""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000009.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:54 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 285,
    label = "r00012571",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4  *2 O     1 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 O     0 {2,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+15,"s^-1"),
        n = 0,
        Ea = (73250.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Heicklen, J."], title=u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals', journal="Adv. Photochem.", volume="14", pages="""177""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000014.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:54 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 286,
    label = "r00012571",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4  *2 O     1 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 O     0 {2,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (9.12e+13,"s^-1"),
        n = 0,
        Ea = (993.007,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."], title=u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds', journal="Can. J. Chem.", volume="81", pages="""431-442""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000015.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:54 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 287,
    label = "r00012710",
    reactant1 = 
"""
1     C     0 {2,D}
2  *1 C     0 {1,D} {3,S} {4,S}
3  *2 O     1 {2,S}
4  *3 H     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,D}
2  *1 C     0 {1,D} {3,D}
3  *2 O     0 {2,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.58e+13,"s^-1"),
        n = 0,
        Ea = (146335,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Colket, M.B., III", "Naegeli, D.W.", "Glassman, I."], title=u'High-Temperature Pyrolysis of Acetaldehyde', journal="Int. J. Chem. Kinet.", volume="7", pages="""223""", year="1975", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
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
    index = 288,
    label = "r00012710",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *2 C     1 {2,S}
2  *1 C     0 {1,S} {3,D} {4,S}
3     O     0 {2,D}
4  *3 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.012e+42,"cm^3/(mol*s)"),
        n = -7.63,
        Ea = (3854,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
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
    index = 289,
    label = "r00012710",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *2 C     1 {2,S}
2  *1 C     0 {1,S} {3,D} {4,S}
3     O     0 {2,D}
4  *3 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.024e+42,"cm^3/(mol*s)"),
        n = -7.63,
        Ea = (3854,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
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
    index = 290,
    label = "r00012710",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *2 C     1 {2,S}
2  *1 C     0 {1,S} {3,D} {4,S}
3     O     0 {2,D}
4  *3 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.072e+42,"cm^3/(mol*s)"),
        n = -7.63,
        Ea = (3854,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
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
    index = 291,
    label = "r00012710",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *2 C     1 {2,S}
2  *1 C     0 {1,S} {3,D} {4,S}
3     O     0 {2,D}
4  *3 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.024e+42,"cm^3/(mol*s)"),
        n = -7.63,
        Ea = (3854,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
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
    index = 292,
    label = "r00012710",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *2 C     1 {2,S}
2  *1 C     0 {1,S} {3,D} {4,S}
3     O     0 {2,D}
4  *3 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.518e+42,"cm^3/(mol*s)"),
        n = -7.63,
        Ea = (3854,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
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
    index = 293,
    label = "r00012710",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *2 C     1 {2,S}
2  *1 C     0 {1,S} {3,D} {4,S}
3     O     0 {2,D}
4  *3 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.024e+42,"cm^3/(mol*s)"),
        n = -7.63,
        Ea = (3854,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
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
    index = 294,
    label = "r00012710",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *2 C     1 {2,S}
2  *1 C     0 {1,S} {3,D} {4,S}
3     O     0 {2,D}
4  *3 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.036e+42,"cm^3/(mol*s)"),
        n = -7.63,
        Ea = (3854,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000008.xml"),
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
    index = 295,
    label = "r00012710",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *2 C     1 {2,S}
2  *1 C     0 {1,S} {3,D} {4,S}
3     O     0 {2,D}
4  *3 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.084e+41,"cm^3/(mol*s)"),
        n = -7.63,
        Ea = (3854,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000009.xml"),
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
    index = 296,
    label = "r00012710",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *2 C     1 {2,S}
2  *1 C     0 {1,S} {3,D} {4,S}
3     O     0 {2,D}
4  *3 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.865e+11,"cm^3/(mol*s)"),
        n = 0.422,
        Ea = (-1755,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000010.xml"),
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
    index = 297,
    label = "r00012720",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 O     0 {1,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1  *3 O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.19e+11,"s^-1"),
        n = 0,
        Ea = (98942.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Diau, E.W-G.", "Lee, Y-P."], title=u'Detailed rate coefficients and the enthalpy change of the equilibrium reaction OH+C_2H_4(+M) = HOC_2H_4(+M) over the temperature range 544-673 K', journal="J. Chem. Phys.", volume="96", pages="""377-386""", year="1992", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
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
    index = 298,
    label = "r00012720",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1  *3 O     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 O     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.23e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-4888.91,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Liu, A.-D.", "Mulac, W.A.", "Jonah, C.D."], title=u'Pulse radiolysis study of the reaction of OH radicals with C_2H_4 over the temperature range 343-1173 K', journal="Int. J. Chem. Kinet.", volume="19", pages="""25""", year="1987", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
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
    index = 299,
    label = "r00012720",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1  *3 O     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 O     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (9.93e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-3990.95,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Liu, A.", "Mulac, W.A.", "Jonah, C.D."], title=u'Kinetic isotope effects in the gas-phase reaction of hydroxyl radicals with ethylene in the temperature range 343-1173 K and at 1-atm pressure', journal="J. Phys. Chem.", volume="92", pages="""3828""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
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
    index = 300,
    label = "r00012720",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1  *3 O     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 O     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (9.93e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-4015.89,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Liu, A.", "Jonah, C.D.", "Mulac, W.A."], title=u'The gas-phase reactions of hydroxyl radicals with several unsaturated hydrocarbons at atmosphere pressure', journal="Radiat. Phys. Chem.", volume="34", pages="""687-691""", year="1989", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
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
    index = 301,
    label = "r00012720",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1  *3 O     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 O     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.41e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-9977.37,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Diau, E.W-G.", "Lee, Y-P."], title=u'Detailed rate coefficients and the enthalpy change of the equilibrium reaction OH+C_2H_4(+M) = HOC_2H_4(+M) over the temperature range 544-673 K', journal="J. Chem. Phys.", volume="96", pages="""377-386""", year="1992", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
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
    index = 302,
    label = "r00012720",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1  *3 O     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 O     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-15.2008,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Yamada, T.", "Bozzelli, J.W.", "Lay, T."], title=u'Kinetic and Thermodynamic Analysis on OH Addition to Ethylene: Adduct Formation, Isomerization, and Isomer Dissociations', journal="J. Phys. Chem. A", volume="103", pages="""7646-7655""", year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000010.xml"),
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
    index = 303,
    label = "r00012720",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1  *3 O     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     1 {1,S}
3  *3 O     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.19e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (15.2008,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Yamada, T.", "Bozzelli, J.W.", "Lay, T."], title=u'Kinetic and Thermodynamic Analysis on OH Addition to Ethylene: Adduct Formation, Isomerization, and Isomer Dissociations', journal="J. Phys. Chem. A", volume="103", pages="""7646-7655""", year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000012.xml"),
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
    index = 304,
    label = "r00012768",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4  *2 C     1 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.61e+12,"s^-1"),
        n = 0,
        Ea = (109751,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Metcalfe, E.L.", "Trotman-Dickenson, A.F."], title=u'The reactions of alkyl radicals. Part VIII. Isobutyl radicals from the photolysis of isovaleraldehyde', journal="J. Chem. Soc.", pages="""5072-5077""", year="1960", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
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
    index = 305,
    label = "r00012768",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4  *2 C     1 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.4e+12,"s^-1"),
        n = 0,
        Ea = (129706,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Slater, D.H.", "Collier, S.S.", "Calvert, J.G."], title=u"The photolysis of 1,1'-azoisobutane vapor at 3660 A. The reactions of the isobutyl free radical", journal="J. Am. Chem. Soc.", volume="90", pages="""268-273""", year="1968", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
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
    index = 306,
    label = "r00012768",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4  *2 C     1 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7e+12,"s^-1"),
        n = 0,
        Ea = (109751,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Warnatz, J."], year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
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
    index = 307,
    label = "r00012768",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4  *2 C     1 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+13,"s^-1"),
        n = 0,
        Ea = (125549,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part 4. Isobutane', journal="J. Phys. Chem. Ref. Data", volume="19", pages="""1-68""", year="1990", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
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
    index = 308,
    label = "r00012768",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4  *2 C     1 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+12,"s^-1"),
        n = 0,
        Ea = (137189,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Douhou, S.", "Perrin, D.", "Martin, R."], title=u"Etude cinetique et modelisation de la reaction thermique de l'isobutene vers 800 K. II. Isobutene en presence d'hydrogene", journal="J. Chim. Phys.", volume="91", pages="""1628-1647""", year="1994", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
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
    index = 309,
    label = "r00012768",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4  *2 C     1 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.69e+13,"s^-1"),
        n = 0.65,
        Ea = (128874,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Knyazev, V.D.", "Slagle, I.R."], title=u'Unimolecular decomposition of n-C_4H_9 and iso-C_4H_9 radicals', journal="J. Phys. Chem.", volume="100", pages="""5318-5328""", year="1996", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000008.xml"),
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
    index = 310,
    label = "r00012768",
    reactant1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    reactant2 = 
"""
1  *3 C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3  *3 C     0 {1,S}
4  *2 C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (36500.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baldwin, R.R.", "Keen, A.", "Walker, R.W."], title=u'Rate constants for the addition of methyl radicals to propene', journal="J. Chem. Soc. Faraday Trans. 2", volume="83", pages="""759""", year="1987", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000011.xml"),
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
    index = 311,
    label = "r00012768",
    reactant1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    reactant2 = 
"""
1  *3 C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3  *3 C     0 {1,S}
4  *2 C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.64e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (33507.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part V. Propene', journal="J. Phys. Chem. Ref. Data", volume="20", pages="""221-273""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000013.xml"),
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
    index = 312,
    label = "r00012768",
    reactant1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    reactant2 = 
"""
1  *3 C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3  *3 C     0 {1,S}
4  *2 C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10025.4,"cm^3/(mol*s)"),
        n = 2.57,
        Ea = (32260.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Knyazev, V.D.", "Slagle, I.R."], title=u'Unimolecular decomposition of n-C_4H_9 and iso-C_4H_9 radicals', journal="J. Phys. Chem.", volume="100", pages="""5318-5328""", year="1996", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000014.xml"),
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
    index = 313,
    label = "r00012769",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *2 C     1 {1,S}
5  *3 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 C     0 {3,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"s^-1"),
        n = 0,
        Ea = (128043,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Metcalfe, E.L.", "Trotman-Dickenson, A.F."], title=u'The reactions of alkyl radicals. Part VIII. Isobutyl radicals from the photolysis of isovaleraldehyde', journal="J. Chem. Soc.", pages="""5072-5077""", year="1960", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
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
    index = 314,
    label = "r00012769",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *2 C     1 {1,S}
5  *3 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 C     0 {3,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14,"s^-1"),
        n = 0,
        Ea = (152155,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Weissman, M.", "Benson, S.W."], title=u'Pyrolysis of methyl chloride, a pathway in the chlorine-catalyzed polymerization of methane', journal="Int. J. Chem. Kinet.", volume="16", pages="""307""", year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
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
    index = 315,
    label = "r00012935",
    reactant1 = 
"""
1  *3 C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     1 {2,D}
""",
    product1 = 
"""
1  *2 C     0 {2,T}
2  *1 C     0 {1,T}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.26e+13,"s^-1"),
        n = 0,
        Ea = (139683,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:04 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 316,
    label = "r00012935",
    reactant1 = 
"""
1  *3 C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     1 {2,D}
""",
    product1 = 
"""
1  *2 C     0 {2,T}
2  *1 C     0 {1,T}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.77e+12,"s^-1"),
        n = 0,
        Ea = (180424,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Naroznik, M.", "Niedzielski, J."], title=u'Propylene photolysis at 6.7 eV: Calculation of the quantum yields for the secondary processes', journal="J. Photochem.", volume="32", pages="""281""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:04 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 317,
    label = "r00012935",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1  *3 C     1
""",
    product1 = 
"""
1  *3 C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     1 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.51e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (32177,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Garcia Dominguez, J.A.", "Trotman-Dickenson, A.F."], title=u'The reactions of alkyl radicals. Part IX. The addition of methyl, ethyl, isopropyl, and t-butyl radicals to acetylene and the isomerization of alkenyl radicals', journal="J. Chem. Soc.", pages="""940-944""", year="1962", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:04 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 318,
    label = "r00012935",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1  *3 C     1
""",
    product1 = 
"""
1  *3 C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     1 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.61048e+40,"cm^3/(mol*s)"),
        n = -8.58,
        Ea = (84807.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M.", "Westmoreland, P.R."], title=u'Bimolecular QRRK analyss of methyl radical reactions', journal="Int. J. Chem. Kinet.", volume="19", pages="""207""", year="1987", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:04 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 319,
    label = "r00012935",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1  *3 C     1
""",
    product1 = 
"""
1  *3 C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     1 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.03e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (32426.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Esser, C.", "Frank, P.", "Just, Th.", "Kerr, J.A.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."], title=u'Evaluated kinetic data for combustion modelling', journal="J. Phys. Chem. Ref. Data", volume="21", pages="""411-429""", year="1992", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:04 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 320,
    label = "r00012935",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1  *3 C     1
""",
    product1 = 
"""
1  *3 C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     1 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.56501e+56,"cm^3/(mol*s)"),
        n = -13.7,
        Ea = (116403,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Diau, E.W.", "Lin, M.C."], title=u'A theoretical study of the CH_3 + C_2H_2 reaction', journal="J. Chem. Phys.", volume="101", pages="""3923-3927""", year="1994", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:04 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 321,
    label = "r00012935",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1  *3 C     1
""",
    product1 = 
"""
1  *3 C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     1 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.2934e+30,"cm^3/(mol*s)"),
        n = -5.98,
        Ea = (55790.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Diau, E.W.", "Lin, M.C."], title=u'A theoretical study of the CH_3 + C_2H_2 reaction', journal="J. Chem. Phys.", volume="101", pages="""3923-3927""", year="1994", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:04 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 322,
    label = "r00012935",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1  *3 C     1
""",
    product1 = 
"""
1  *3 C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     1 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.75e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (32509.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Diau, E.W.", "Lin, M.C."], title=u'Kinetic modeling of the CH_3 + C_2H_2 reaction data with sensitivity analyses', journal="Int. J. Chem. Kinet.", volume="27", pages="""855-866""", year="1995", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000008.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:04 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 323,
    label = "r00013083",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3  *2 C     1 {1,S}
4  *3 O     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    product2 = 
"""
1  *3 O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.7e+12,"s^-1"),
        n = 0,
        Ea = (112245,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dunlop, J.R.", "Tully, F.P."], title=u'Catalytic dehydration of alcohols by OH. 2-propanol: an intermediate case', journal="J. Phys. Chem.", volume="97", pages="""6457-6464""", year="1993", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
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
    index = 324,
    label = "r00013096",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S}
3     C     0 {1,S} {5,D}
4  *2 C     1 {2,S}
5     C     0 {3,D}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *3 C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.31e+13,"s^-1"),
        n = 0,
        Ea = (93953.5,"J/mol"),
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
    index = 325,
    label = "r00015135",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {6,S}
2  *3 C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {2,S}
6  *2 O     1 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 O     0 {3,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *3 C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.01e+14,"s^-1"),
        n = 0,
        Ea = (59864.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Batt, L.", "Islam, T.S.A.", "Rattray, G.N."], title=u'The Gas-Phase Pyrolysis of Alkyl Nitrites. VI. t-Amyl Nitrite', journal="Int. J. Chem. Kinet.", volume="10", pages="""931""", year="1978", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:17 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 326,
    label = "r00015135",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {6,S}
2  *3 C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {2,S}
6  *2 O     1 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 O     0 {3,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *3 C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.31e+14,"s^-1"),
        n = 0,
        Ea = (57702.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Batt, L."], title=u'The Gas-Phase Decomposition of Alkoxy Radicals', journal="Int. J. Chem. Kinet.", volume="11", pages="""977""", year="1979", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:17 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 327,
    label = "r00015135",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {6,S}
2  *3 C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {2,S}
6  *2 O     1 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 O     0 {3,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *3 C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.98e+13,"s^-1"),
        n = 0,
        Ea = (51882.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Choo, K.Y.", "Benson, S.W."], title=u'Arrhenius Parameters for the Alkoxy Radical Decomposition Reactions', journal="Int. J. Chem. Kinet.", volume="13", pages="""833""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:17 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 328,
    label = "r00015135",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {6,S}
2  *3 C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {2,S}
6  *2 O     1 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 O     0 {3,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *3 C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+15,"s^-1"),
        n = 0,
        Ea = (64021.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Heicklen, J."], title=u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals', journal="Adv. Photochem.", volume="14", pages="""177""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:17 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 329,
    label = "r00015136",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {6,S}
2     C     0 {1,S} {5,S}
3  *3 C     0 {1,S}
4     C     0 {1,S}
5     C     0 {2,S}
6  *2 O     1 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S} {4,S}
2     C     0 {1,S}
3     C     0 {4,S}
4  *1 C     0 {1,S} {3,S} {5,D}
5  *2 O     0 {4,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+15,"s^-1"),
        n = 0,
        Ea = (78239.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Batt, L.", "Islam, T.S.A.", "Rattray, G.N."], title=u'The Gas-Phase Pyrolysis of Alkyl Nitrites. VI. t-Amyl Nitrite', journal="Int. J. Chem. Kinet.", volume="10", pages="""931""", year="1978", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:17 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 330,
    label = "r00015136",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {6,S}
2     C     0 {1,S} {5,S}
3  *3 C     0 {1,S}
4     C     0 {1,S}
5     C     0 {2,S}
6  *2 O     1 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S} {4,S}
2     C     0 {1,S}
3     C     0 {4,S}
4  *1 C     0 {1,S} {3,S} {5,D}
5  *2 O     0 {4,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.31e+13,"s^-1"),
        n = 0,
        Ea = (67347.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Choo, K.Y.", "Benson, S.W."], title=u'Arrhenius Parameters for the Alkoxy Radical Decomposition Reactions', journal="Int. J. Chem. Kinet.", volume="13", pages="""833""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:17 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 331,
    label = "r00015136",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {6,S}
2     C     0 {1,S} {5,S}
3  *3 C     0 {1,S}
4     C     0 {1,S}
5     C     0 {2,S}
6  *2 O     1 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S} {4,S}
2     C     0 {1,S}
3     C     0 {4,S}
4  *1 C     0 {1,S} {3,S} {5,D}
5  *2 O     0 {4,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+15,"s^-1"),
        n = 0,
        Ea = (78239.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Heicklen, J."], title=u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals', journal="Adv. Photochem.", volume="14", pages="""177""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:17 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 332,
    label = "r00015595",
    reactant1 = 
"""
1  *3 C     0 {2,S}
2  *1 C     0 {1,S} {3,D} {4,S}
3     C     0 {2,D}
4  *2 C     1 {2,S}
""",
    product1 = 
"""
1  *2 C     0 {3,D}
2     C     0 {3,D}
3  *1 C     0 {1,D} {2,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13,"s^-1"),
        n = 0,
        Ea = (209525,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Pyrolysis of 2,4-Dimethylhexene-1 and the Stability of Isobutenyl Radicals', journal="Int. J. Chem. Kinet.", volume="5", pages="""929""", year="1973", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:24 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 333,
    label = "r00015595",
    reactant1 = 
"""
1  *2 C     0 {3,D}
2     C     0 {3,D}
3  *1 C     0 {1,D} {2,D}
""",
    reactant2 = 
"""
1  *3 C     1
""",
    product1 = 
"""
1  *3 C     0 {2,S}
2  *1 C     0 {1,S} {3,S} {4,D}
3  *2 C     1 {2,S}
4     C     0 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.58e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20786.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Pyrolysis of 2,4-Dimethylhexene-1 and the Stability of Isobutenyl Radicals', journal="Int. J. Chem. Kinet.", volume="5", pages="""929""", year="1973", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:24 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 334,
    label = "r00015628",
    reactant1 = 
"""
1     C     0 {3,S}
2  *1 C     0 {3,D} {4,S}
3  *2 C     1 {1,S} {2,D}
4  *3 H     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,T}
3  *1 C     0 {2,T}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (9.55e+12,"s^-1"),
        n = 0,
        Ea = (192896,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Naroznik, M.", "Niedzielski, J."], title=u'Propylene photolysis at 6.7 eV: Calculation of the quantum yields for the secondary processes', journal="J. Photochem.", volume="32", pages="""281""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:25 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 335,
    label = "r00015628",
    reactant1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,T}
3  *1 C     0 {2,T}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1     C     0 {3,S}
2  *1 C     0 {3,D} {4,S}
3  *2 C     1 {1,S} {2,D}
4  *3 H     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8397.62,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Wagner, H.Gg.", "Zellner, R."], title=u'Reaktionen von Wasserstoffatomen mit ungesaettigten C_3-Kohlenwasserstoffen. II. Die Reaktion von H-Atomen mit Methylacetylen', journal="Ber. Bunsenges. Phys. Chem.", volume="76", pages="""518""", year="1972", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:25 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 336,
    label = "r00015629",
    reactant1 = 
"""
1  *1 C     0 {3,S} {4,S}
2     C     0 {3,D}
3  *2 C     1 {1,S} {2,D}
4  *3 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {3,D}
2  *1 C     0 {3,D}
3  *2 C     0 {1,D} {2,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.32e+13,"s^-1"),
        n = 0,
        Ea = (199547,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Naroznik, M.", "Niedzielski, J."], title=u'Propylene photolysis at 6.7 eV: Calculation of the quantum yields for the secondary processes', journal="J. Photochem.", volume="32", pages="""281""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:25 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 337,
    label = "r00015629",
    reactant1 = 
"""
1  *1 C     0 {3,D}
2     C     0 {3,D}
3  *2 C     0 {1,D} {2,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {3,S} {4,S}
2     C     0 {3,D}
3  *2 C     1 {1,S} {2,D}
4  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.49e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8397.62,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Wagner, H.Gg.", "Zellner, R."], title=u'Reaktionen von Wasserstoffatomen mit ungesaettigten C_3-Kohlenwasserstoffen. III. Die Reaktion von H-Atomen mit Allen', journal="Ber. Bunsenges. Phys. Chem.", volume="76", pages="""667""", year="1972", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:25 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 338,
    label = "r00015690",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *1 C     0 {1,S} {5,S}
4     C     0 {2,S} {6,D}
5  *2 C     1 {3,S}
6     C     0 {4,D}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3  *3 C     1 {1,S}
4     C     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"s^-1"),
        n = 0,
        Ea = (124717,"J/mol"),
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
    index = 339,
    label = "r00015701",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *1 C     0 {1,S} {4,S}
4  *2 O     1 {3,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *3 C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.31e+13,"s^-1"),
        n = 0,
        Ea = (81565,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baldwin, A.C.", "Barker, J.R.", "Golden, D.M.", "Hendry, D.G."], title=u'Photochemical smog. Rate parameter estimates and computer simulations', journal="J. Phys. Chem.", volume="81", pages="""2483""", year="1977", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
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
    index = 340,
    label = "r00015701",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *1 C     0 {1,S} {4,S}
4  *2 O     1 {3,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *3 C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.01e+13,"s^-1"),
        n = 0,
        Ea = (65268.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Choo, K.Y.", "Benson, S.W."], title=u'Arrhenius Parameters for the Alkoxy Radical Decomposition Reactions', journal="Int. J. Chem. Kinet.", volume="13", pages="""833""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
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
    index = 341,
    label = "r00015702",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *1 C     0 {1,S} {4,S} {5,S}
4  *2 O     1 {3,S}
5  *3 H     0 {3,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *1 C     0 {1,S} {4,D}
4  *2 O     0 {3,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.7e+13,"s^-1"),
        n = 0,
        Ea = (1417.64,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."], title=u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds', journal="Can. J. Chem.", volume="81", pages="""431-442""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
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
    index = 342,
    label = "r00015704",
    reactant1 = 
"""
1  *1 C     0 {2,D} {3,S} {4,S}
2     O     0 {1,D}
3  *2 O     1 {1,S}
4  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,D}
2     O     0 {1,D}
3  *2 O     0 {1,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"s^-1"),
        n = 0.307,
        Ea = (138020,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Larson, c.W.", "Stewart, P.H.", "Golden, D.M."], title=u'Pressure and temperature dependence of reactions proceeding via a bound complex. An approach for combustion and atmospheric chemistry modelers. Application to HO + CO \u2192 [HOCO] \u2192 H + CO_2', journal="Int. J. Chem. Kinet.", volume="20", pages="""27""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
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
    index = 343,
    label = "r00015716",
    reactant1 = 
"""
1  *3 C     0 {3,S}
2  *2 C     1 {3,S}
3  *1 O     0 {1,S} {2,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 O     0 {1,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+13,"s^-1"),
        n = 0,
        Ea = (106425,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Loucks, L.F.", "Laidler, K.J."], title=u'Mercury-photosensitized decomposition of dimethyl ether. Part II. The thermal decomposition of the methoxymethyl radical', journal="Can. J. Chem.", volume="45", pages="""2767-2773""", year="1967", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
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
    index = 344,
    label = "r00015716",
    reactant1 = 
"""
1  *3 C     0 {3,S}
2  *2 C     1 {3,S}
3  *1 O     0 {1,S} {2,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 O     0 {1,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+13,"s^-1"),
        n = 0,
        Ea = (106425,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Sehested, J.", "Sehested, K.", "Platz, J.", "Egsgaard, H.", "Nielsen, O.J."], title=u'Oxidation of dimethyl ether: absolute rate constants for the self reaction of CH_3OCH_2 radicals, the reaction of CH_3OCH_2 radicals with O_2, and the thermal decomposition of CH_3OCH_2 radicals', journal="Int. J. Chem. Kinet.", volume="29", pages="""627-636""", year="1997", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
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
    index = 345,
    label = "r00015716",
    reactant1 = 
"""
1  *3 C     0 {3,S}
2  *2 C     1 {3,S}
3  *1 O     0 {1,S} {2,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 O     0 {1,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.45e+14,"s^-1"),
        n = -0.22,
        Ea = (113908,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Li, Q.S.", "Zhang, Y.", "Zhang, S.W."], title=u'Dual level direct ab initio and density-functional theory dynamics study on the unimolecular decomposition of CH_3OCH_2 radical', journal="J. Phys. Chem. A:", volume="108", pages="""2014-2019""", year="2004", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
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
    index = 346,
    label = "r00015756",
    reactant1 = 
"""
1     C     0 {2,S} {3,B} {4,B}
2  *1 C     0 {1,S} {5,D}
3     C     0 {1,B} {7,B}
4     C     0 {1,B} {8,B}
5  *2 C     0 {2,D} {9,S}
6     C     0 {7,B} {8,B}
7     C     0 {3,B} {6,B}
8     C     0 {4,B} {6,B}
9     C     0 {5,S} {10,D}
10    C     0 {9,D}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S} {11,S}
2     C     0 {1,S} {4,B} {5,B}
3  *2 C     1 {1,S} {9,S}
4     C     0 {2,B} {7,B}
5     C     0 {2,B} {8,B}
6     C     0 {7,B} {8,B}
7     C     0 {4,B} {6,B}
8     C     0 {5,B} {6,B}
9     C     0 {3,S} {10,D}
10    C     0 {9,D}
11 *3 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.2e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (145399,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Fascella, S.", "Cavallotti, C.", "Rota, R.", "Carra, S."], title=u'Quantum chemistry investigation of key reactions involved in the formation of naphthalene and indene', journal="J. Phys. Chem. A", volume="108", pages="""3829-3843""", year="2004", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:28 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 347,
    label = "r00015756",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {11,S}
2     C     0 {1,S} {4,B} {5,B}
3  *2 C     1 {1,S} {9,S}
4     C     0 {2,B} {7,B}
5     C     0 {2,B} {8,B}
6     C     0 {7,B} {8,B}
7     C     0 {4,B} {6,B}
8     C     0 {5,B} {6,B}
9     C     0 {3,S} {10,D}
10    C     0 {9,D}
11 *3 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,B} {4,B}
2  *1 C     0 {1,S} {5,D}
3     C     0 {1,B} {6,B}
4     C     0 {1,B} {7,B}
5  *2 C     0 {2,D} {9,S}
6     C     0 {3,B} {8,B}
7     C     0 {4,B} {8,B}
8     C     0 {6,B} {7,B}
9     C     0 {5,S} {10,D}
10    C     0 {9,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.4e+12,"s^-1"),
        n = 0,
        Ea = (773256,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Fascella, S.", "Cavallotti, C.", "Rota, R.", "Carra, S."], title=u'Quantum chemistry investigation of key reactions involved in the formation of naphthalene and indene', journal="J. Phys. Chem. A", volume="108", pages="""3829-3843""", year="2004", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:28 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 348,
    label = "r00016107",
    reactant1 = 
"""
1  *3 C     0 {2,B} {3,B} {7,S}
2     C     0 {1,B} {5,B}
3     C     0 {1,B} {6,B}
4     C     0 {5,B} {6,B}
5     C     0 {2,B} {4,B}
6     C     0 {3,B} {4,B}
7  *1 C     0 {1,S} {8,D}
8  *2 C     1 {7,D}
""",
    product1 = 
"""
1  *2 C     0 {2,T}
2  *1 C     0 {1,T}
""",
    product2 = 
"""
1     C     0 {2,B} {3,B}
2     C     0 {1,B} {4,B}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6  *3 C     1 {4,B} {5,B}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.35e+14,"s^-1"),
        n = 0.34,
        Ea = (755.247,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tokmakov, I.V.", "Lin, M.C."], title=u'Reaction of phenyl radicals with acetylene: Quantum chemical investigation of the mechanism and master equation analysis of the kinetics', journal="J. Am. Chem. Soc.", volume="125", pages="""11397-11408""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:37 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 349,
    label = "r00016107",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1     C     0 {2,B} {3,B}
2     C     0 {1,B} {4,B}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6  *3 C     1 {4,B} {5,B}
""",
    product1 = 
"""
1  *3 C     0 {2,B} {3,B} {7,S}
2     C     0 {1,B} {5,B}
3     C     0 {1,B} {6,B}
4     C     0 {5,B} {6,B}
5     C     0 {2,B} {4,B}
6     C     0 {3,B} {4,B}
7  *1 C     0 {1,S} {8,D}
8  *2 C     1 {7,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.69e+06,"cm^3/(mol*s)"),
        n = 2.05,
        Ea = (61.464,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tokmakov, I.V.", "Lin, M.C."], title=u'Reaction of phenyl radicals with acetylene: Quantum chemical investigation of the mechanism and master equation analysis of the kinetics', journal="J. Am. Chem. Soc.", volume="125", pages="""11397-11408""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:37 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 350,
    label = "r00016108",
    reactant1 = 
"""
1     C     0 {2,B} {3,B} {7,S}
2     C     0 {1,B} {5,B}
3     C     0 {1,B} {6,B}
4     C     0 {5,B} {6,B}
5     C     0 {2,B} {4,B}
6     C     0 {3,B} {4,B}
7  *1 C     0 {1,S} {8,D} {9,S}
8  *2 C     1 {7,D}
9  *3 H     0 {7,S}
""",
    product1 = 
"""
1     C     0 {2,B} {3,B} {7,S}
2     C     0 {1,B} {4,B}
3     C     0 {1,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {6,B}
6     C     0 {4,B} {5,B}
7  *1 C     0 {1,S} {8,T}
8  *2 C     0 {7,T}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.8e+11,"s^-1"),
        n = 0.82,
        Ea = (642.893,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tokmakov, I.V.", "Lin, M.C."], title=u'Reaction of phenyl radicals with acetylene: Quantum chemical investigation of the mechanism and master equation analysis of the kinetics', journal="J. Am. Chem. Soc.", volume="125", pages="""11397-11408""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:37 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 351,
    label = "r00016147",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S} {4,S} {5,S}
2  *1 C     0 {1,S} {6,S} {7,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7  *2 C     1 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    product2 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *3 C     1 {1,S} {2,S} {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.31e+13,"s^-1"),
        n = 0,
        Ea = (111414,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baldwin, R.R.", "Walker, R.W.", "Walker, R.W."], title=u'Addition of 2,2,3-Trimethylbutane to Slowly Reacting Mixtures of Hydrogen and Oxygen at 480^oC', journal="J. Chem. Soc. Faraday Trans. 1", volume="77", pages="""2157""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:37 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 352,
    label = "r00016148",
    reactant1 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2  *1 C     0 {1,S} {6,S} {7,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {1,S}
6  *3 C     0 {2,S}
7  *2 C     1 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *1 C     0 {1,S} {6,D}
6  *2 C     0 {5,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.31e+13,"s^-1"),
        n = 0,
        Ea = (129706,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baldwin, R.R.", "Walker, R.W.", "Walker, R.W."], title=u'Addition of 2,2,3-Trimethylbutane to Slowly Reacting Mixtures of Hydrogen and Oxygen at 480^oC', journal="J. Chem. Soc. Faraday Trans. 1", volume="77", pages="""2157""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:37 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 353,
    label = "r00016149",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {6,S}
2  *3 C     0 {1,S}
3     C     0 {1,S}
4     C     0 {6,S}
5     C     0 {6,S}
6  *2 C     1 {1,S} {4,S} {5,S}
""",
    product1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {5,S}
4  *2 C     0 {1,S} {2,S} {5,D}
5  *1 C     0 {3,S} {4,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.31e+13,"s^-1"),
        n = 0,
        Ea = (129706,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baldwin, R.R.", "Drewery, G.R.", "Walker, R.W."], title=u'Decomposition of 2,3-dimethylbutane in the presence of oxygen. Part 2.-Elementary reactions involved in the formation of products', journal="J. Chem. Soc. Faraday Trans. 1", volume="80", pages="""3195""", year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:38 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 354,
    label = "r00016150",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {6,S} {7,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {6,S}
5     C     0 {6,S}
6  *2 C     1 {1,S} {4,S} {5,S}
7  *3 H     0 {1,S}
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
1  *3 H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.31e+13,"s^-1"),
        n = 0,
        Ea = (148829,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baldwin, R.R.", "Drewery, G.R.", "Walker, R.W."], title=u'Decomposition of 2,3-dimethylbutane in the presence of oxygen. Part 2.-Elementary reactions involved in the formation of products', journal="J. Chem. Soc. Faraday Trans. 1", volume="80", pages="""3195""", year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:38 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 355,
    label = "r00016184",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S}
2  *3 C     0 {1,S} {3,D}
3     C     0 {2,D}
4  *2 O     1 {1,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    product2 = 
"""
1     C     0 {2,D}
2  *3 C     1 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.39e+14,"s^-1"),
        n = 0,
        Ea = (1566.34,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."], title=u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds', journal="Can. J. Chem.", volume="81", pages="""431-442""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:38 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 356,
    label = "r00016185",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,D}
3     C     0 {2,D}
4  *2 O     1 {1,S}
5  *3 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *1 C     0 {1,S} {4,D}
4  *2 O     0 {3,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.1e+13,"s^-1"),
        n = 0,
        Ea = (1275.54,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."], title=u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds', journal="Can. J. Chem.", volume="81", pages="""431-442""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:38 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 357,
    label = "r00016186",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *1 C     0 {1,S} {5,S}
5  *2 O     1 {4,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    product2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *3 C     1 {1,S} {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.01e+13,"s^-1"),
        n = 0,
        Ea = (51882.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Choo, K.Y.", "Benson, S.W."], title=u'Arrhenius Parameters for the Alkoxy Radical Decomposition Reactions', journal="Int. J. Chem. Kinet.", volume="13", pages="""833""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:38 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 358,
    label = "r00016187",
    reactant1 = 
"""
1  *1 C     0 {2,S} {8,S} {9,S}
2     C     0 {1,S} {3,B} {4,B}
3     C     0 {2,B} {6,B}
4     C     0 {2,B} {7,B}
5     C     0 {6,B} {7,B}
6     C     0 {3,B} {5,B}
7     C     0 {4,B} {5,B}
8  *2 O     1 {1,S}
9  *3 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,B} {3,B} {7,S}
2     C     0 {1,B} {4,B}
3     C     0 {1,B} {6,B}
4     C     0 {2,B} {5,B}
5     C     0 {4,B} {6,B}
6     C     0 {3,B} {5,B}
7  *1 C     0 {1,S} {8,D}
8  *2 O     0 {7,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.27e+14,"s^-1"),
        n = 0,
        Ea = (4614.53,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Brezinsky, K.", "Litzinger, T.A.", "Glassman, I."], title=u'The high temperature oxidation of the methyl side chain of toluene', journal="Int. J. Chem. Kinet.", volume="16", pages="""1053""", year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:39 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 359,
    label = "r00016188",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S} {5,S}
3     C     0 {1,S}
4     C     0 {2,S}
5  *2 O     1 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 O     0 {2,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *3 C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+16,"s^-1"),
        n = 0,
        Ea = (73250.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Batt, L.", "McCulloch, R.D.", "Milne, R.T."], title=u'Thermochemical and Kinetic Studies of Alkyl Nitrites (RONO)-D(RO-NO), The Reactions between RO. and NO, and the Decomposition RO.', journal="Proc. Symp. Chem. Kinet. Data Upper Lower Atmos. 1974", pages="""441""", year="1975", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:39 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 360,
    label = "r00016188",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S} {5,S}
3     C     0 {1,S}
4     C     0 {2,S}
5  *2 O     1 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 O     0 {2,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *3 C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.31e+14,"s^-1"),
        n = 0,
        Ea = (64021.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Batt, L.", "McCulloch, R.D."], title=u'The Gas-Phase Pyrolysis of Alkyl Nitrites. II. s-Butyl Nitrite', journal="Int. J. Chem. Kinet.", volume="8", pages="""911""", year="1976", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:39 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 361,
    label = "r00016188",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S} {5,S}
3     C     0 {1,S}
4     C     0 {2,S}
5  *2 O     1 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 O     0 {2,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *3 C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.76e+14,"s^-1"),
        n = 0,
        Ea = (61111.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baldwin, A.C.", "Barker, J.R.", "Golden, D.M.", "Hendry, D.G."], title=u'Photochemical smog. Rate parameter estimates and computer simulations', journal="J. Phys. Chem.", volume="81", pages="""2483""", year="1977", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:39 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 362,
    label = "r00016188",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S} {5,S}
3     C     0 {1,S}
4     C     0 {2,S}
5  *2 O     1 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 O     0 {2,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *3 C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.94e+14,"s^-1"),
        n = 0,
        Ea = (64021.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Batt, L."], title=u'The Gas-Phase Decomposition of Alkoxy Radicals', journal="Int. J. Chem. Kinet.", volume="11", pages="""977""", year="1979", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:39 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 363,
    label = "r00016188",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S} {5,S}
3     C     0 {1,S}
4     C     0 {2,S}
5  *2 O     1 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 O     0 {2,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *3 C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.98e+13,"s^-1"),
        n = 0,
        Ea = (56455.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Choo, K.Y.", "Benson, S.W."], title=u'Arrhenius Parameters for the Alkoxy Radical Decomposition Reactions', journal="Int. J. Chem. Kinet.", volume="13", pages="""833""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:39 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 364,
    label = "r00016188",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S} {5,S}
3     C     0 {1,S}
4     C     0 {2,S}
5  *2 O     1 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 O     0 {2,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *3 C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+15,"s^-1"),
        n = 0,
        Ea = (64437.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Heicklen, J."], title=u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals', journal="Adv. Photochem.", volume="14", pages="""177""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:39 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 365,
    label = "r00016188",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S} {5,S}
3     C     0 {1,S}
4     C     0 {2,S}
5  *2 O     1 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 O     0 {2,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *3 C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.35e+13,"s^-1"),
        n = 0,
        Ea = (62774.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Heiss, A.", "Tardieu de Maleissye, J.", "Viossat, V.", "Sahetchian, K.A."], title=u'Reactions of primary and secondary butoxy radicals in oxygen at atmospheric pressure', journal="Int. J. Chem. Kinet.", volume="23", pages="""607-622""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000008.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:39 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 366,
    label = "r00016188",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S} {5,S}
3     C     0 {1,S}
4     C     0 {2,S}
5  *2 O     1 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 O     0 {2,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *3 C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.25e+13,"s^-1"),
        n = 0,
        Ea = (807.954,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."], title=u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds', journal="Can. J. Chem.", volume="81", pages="""431-442""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000009.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:39 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 367,
    label = "r00016189",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S} {5,S} {6,S}
3     C     0 {1,S}
4     C     0 {2,S}
5  *2 O     1 {2,S}
6  *3 H     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S} {4,S}
2     C     0 {1,S}
3     C     0 {4,S}
4  *1 C     0 {1,S} {3,S} {5,D}
5  *2 O     0 {4,D}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.51e+13,"s^-1"),
        n = 0,
        Ea = (1249.11,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."], title=u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds', journal="Can. J. Chem.", volume="81", pages="""431-442""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:39 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 368,
    label = "r00016190",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S} {5,S}
3     C     0 {1,S}
4  *3 C     0 {2,S}
5  *2 O     1 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *1 C     0 {1,S} {4,D}
4  *2 O     0 {3,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.94e+14,"s^-1"),
        n = 0,
        Ea = (79486.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Batt, L."], title=u'The Gas-Phase Decomposition of Alkoxy Radicals', journal="Int. J. Chem. Kinet.", volume="11", pages="""977""", year="1979", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:39 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 369,
    label = "r00016190",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S} {5,S}
3     C     0 {1,S}
4  *3 C     0 {2,S}
5  *2 O     1 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *1 C     0 {1,S} {4,D}
4  *2 O     0 {3,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+15,"s^-1"),
        n = 0,
        Ea = (79902.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Heicklen, J."], title=u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals', journal="Adv. Photochem.", volume="14", pages="""177""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:39 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 370,
    label = "r00016190",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S} {5,S}
3     C     0 {1,S}
4  *3 C     0 {2,S}
5  *2 O     1 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *1 C     0 {1,S} {4,D}
4  *2 O     0 {3,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.78e+13,"s^-1"),
        n = 0,
        Ea = (1029.36,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."], title=u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds', journal="Can. J. Chem.", volume="81", pages="""431-442""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:39 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 371,
    label = "r00016227",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S} {4,S}
2  *1 C     0 {1,S} {5,S} {6,S} {7,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     C     0 {2,S}
7  *2 O     1 {2,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 O     0 {3,D}
""",
    product2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *3 C     1 {1,S} {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.98e+13,"s^-1"),
        n = 0,
        Ea = (40574.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Choo, K.Y.", "Benson, S.W."], title=u'Arrhenius Parameters for the Alkoxy Radical Decomposition Reactions', journal="Int. J. Chem. Kinet.", volume="13", pages="""833""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:39 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 372,
    label = "r00016551",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S} {4,S}
2  *1 C     0 {1,S} {5,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {2,S}
6  *2 O     1 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 O     0 {2,D}
""",
    product2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *3 C     1 {1,S} {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.01e+13,"s^-1"),
        n = 0,
        Ea = (51882.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baldwin, R.R.", "Walker, R.W."], title=u'Elementary Reactions in the Oxidation of Alkenes', journal="Symp. Int. Combust. Proc.", volume="18", pages="""819""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:49 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 373,
    label = "r00016656",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *1 C     0 {1,S} {5,S} {6,S}
4     C     0 {2,S}
5     C     0 {3,S}
6  *2 O     1 {3,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 O     0 {2,D}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *3 C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.58e+14,"s^-1"),
        n = 0,
        Ea = (57702.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dobe, S.", "Berces, T.", "Marta, F."], title=u'Gas phase decomposition and isomerization reactions of 2-pentoxy radicals', journal="Int. J. Chem. Kinet.", volume="18", pages="""329""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:51 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 374,
    label = "r00016656",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *1 C     0 {1,S} {5,S} {6,S}
4     C     0 {2,S}
5     C     0 {3,S}
6  *2 O     1 {3,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 O     0 {2,D}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *3 C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+15,"s^-1"),
        n = 0,
        Ea = (64437.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Heicklen, J."], title=u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals', journal="Adv. Photochem.", volume="14", pages="""177""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:51 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 375,
    label = "r00016657",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *1 C     0 {1,S} {5,S} {6,S}
4     C     0 {2,S}
5  *3 C     0 {3,S}
6  *2 O     1 {3,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4  *1 C     0 {2,S} {5,D}
5  *2 O     0 {4,D}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.58e+14,"s^-1"),
        n = 0,
        Ea = (72834.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dobe, S.", "Berces, T.", "Marta, F."], title=u'Gas phase decomposition and isomerization reactions of 2-pentoxy radicals', journal="Int. J. Chem. Kinet.", volume="18", pages="""329""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:52 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 376,
    label = "r00016678",
    reactant1 = 
"""
1  *1 C     0 {2,D} {5,S}
2  *2 C     1 {1,D} {3,S}
3     C     0 {2,S} {4,T}
4     C     0 {3,T}
5  *3 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,T}
2  *2 C     0 {1,S} {4,T}
3     C     0 {1,T}
4  *1 C     0 {2,T}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+14,"s^-1"),
        n = 0,
        Ea = (216176,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Ghibaudi, E.", "Colussi, A.J."], title=u'Kinetics and thermochemistry of the equilibrium 2 (acetylene) = vinylacetylene. Direct evidence against a chain mechanism', journal="J. Phys. Chem.", volume="92", pages="""5839""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:53 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 377,
    label = "r00016678",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,T}
2     C     0 {1,S} {4,T}
3  *1 C     0 {1,T}
4     C     0 {2,T}
""",
    reactant2 = 
"""
1  *3 H     1
""",
    product1 = 
"""
1  *1 C     0 {2,D} {5,S}
2  *2 C     1 {1,D} {3,S}
3     C     0 {2,S} {4,T}
4     C     0 {3,T}
5  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.3e+30,"cm^3/(mol*s)"),
        n = -4.92,
        Ea = (45189.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Eiteneer, B.", "Frenklach, M."], title=u'Experimental and Modeling Study of Shock-Tube Oxidation of Acetylene', journal="Int J. Chem. Kinet.", volume="35", pages="""391-414""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:53 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 378,
    label = "r00016682",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2  *3 C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4  *1 C     0 {2,S} {6,S}
5     O     0 {3,S}
6  *2 O     1 {4,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *3 C     1 {1,S}
4     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13,"s^-1"),
        n = 0,
        Ea = (79486.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baldwin, A.C.", "Barker, J.R.", "Golden, D.M.", "Hendry, D.G."], title=u'Photochemical smog. Rate parameter estimates and computer simulations', journal="J. Phys. Chem.", volume="81", pages="""2483""", year="1977", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:53 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 379,
    label = "r00016688",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3  *1 C     0 {1,S} {5,S}
4     O     0 {1,S}
5  *2 O     1 {3,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *3 C     1 {1,S} {3,S}
3     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.94e+13,"s^-1"),
        n = 0,
        Ea = (87302,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baldwin, A.C.", "Barker, J.R.", "Golden, D.M.", "Hendry, D.G."], title=u'Photochemical smog. Rate parameter estimates and computer simulations', journal="J. Phys. Chem.", volume="81", pages="""2483""", year="1977", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:53 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 380,
    label = "r00016689",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {4,S}
4  *3 C     0 {1,S} {3,S} {6,D}
5  *2 O     1 {1,S}
6     O     0 {4,D}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 O     0 {2,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *3 C     1 {1,S} {3,D}
3     O     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.16e+14,"s^-1"),
        n = 0,
        Ea = (53545.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baldwin, A.C.", "Barker, J.R.", "Golden, D.M.", "Hendry, D.G."], title=u'Photochemical smog. Rate parameter estimates and computer simulations', journal="J. Phys. Chem.", volume="81", pages="""2483""", year="1977", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:53 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 381,
    label = "r00016804",
    reactant1 = 
"""
1  *3 C     0 {3,S}
2     C     0 {4,S}
3  *1 C     0 {1,S} {4,D}
4  *2 C     1 {2,S} {3,D}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,T}
3  *1 C     0 {2,T}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.01e+13,"s^-1"),
        n = 0,
        Ea = (131369,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:36:00 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 382,
    label = "r00016804",
    reactant1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,T}
3  *1 C     0 {2,T}
""",
    reactant2 = 
"""
1  *3 C     1
""",
    product1 = 
"""
1  *3 C     0 {3,S}
2     C     0 {4,S}
3  *1 C     0 {1,S} {4,D}
4  *2 C     1 {2,S} {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.01e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (36833.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Getty, R.R.", "Kerr, J.A.", "Trotman-Dickenson, A.F."], title=u'The reactions of alkyl radicals. Part XIII. The additions of methyl, isopropyl, and t-butyl radicals to propyne and the isomerisation of alkenyl radicals', journal="J. Chem. Soc. A", pages="""1360""", year="1967", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:36:00 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 383,
    label = "r00016835",
    reactant1 = 
"""
1  *1 C     0 {3,S} {4,S} {6,S}
2     C     0 {5,S} {6,S}
3  *3 C     0 {1,S}
4     C     0 {1,S} {5,B} {8,B}
5     C     0 {2,S} {4,B} {7,B}
6  *2 C     1 {1,S} {2,S}
7     C     0 {5,B} {9,B}
8     C     0 {4,B} {10,B}
9     C     0 {7,B} {10,B}
10    C     0 {8,B} {9,B}
""",
    product1 = 
"""
1     C     0 {2,S} {4,S}
2     C     0 {1,S} {3,B} {6,B}
3     C     0 {2,B} {5,S} {7,B}
4  *2 C     0 {1,S} {5,D}
5  *1 C     0 {3,S} {4,D}
6     C     0 {2,B} {9,B}
7     C     0 {3,B} {8,B}
8     C     0 {7,B} {9,B}
9     C     0 {6,B} {8,B}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13,"s^-1"),
        n = 0,
        Ea = (520461,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Fascella, S.", "Cavallotti, C.", "Rota, R.", "Carra, S."], title=u'Quantum chemistry investigation of key reactions involved in the formation of naphthalene and indene', journal="J. Phys. Chem. A", volume="108", pages="""3829-3843""", year="2004", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:36:01 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 384,
    label = "r00016835",
    reactant1 = 
"""
1     C     0 {2,S} {4,S}
2     C     0 {1,S} {3,B} {5,B}
3     C     0 {2,B} {6,S} {7,B}
4  *2 C     0 {1,S} {6,D}
5     C     0 {2,B} {9,B}
6  *1 C     0 {3,S} {4,D}
7     C     0 {3,B} {8,B}
8     C     0 {7,B} {9,B}
9     C     0 {5,B} {8,B}
""",
    reactant2 = 
"""
1  *3 C     1
""",
    product1 = 
"""
1  *1 C     0 {3,S} {4,S} {6,S}
2     C     0 {5,S} {6,S}
3  *3 C     0 {1,S}
4     C     0 {1,S} {5,B} {8,B}
5     C     0 {2,S} {4,B} {7,B}
6  *2 C     1 {1,S} {2,S}
7     C     0 {5,B} {10,B}
8     C     0 {4,B} {9,B}
9     C     0 {8,B} {10,B}
10    C     0 {7,B} {9,B}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (199923,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Fascella, S.", "Cavallotti, C.", "Rota, R.", "Carra, S."], title=u'Quantum chemistry investigation of key reactions involved in the formation of naphthalene and indene', journal="J. Phys. Chem. A", volume="108", pages="""3829-3843""", year="2004", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:36:01 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 385,
    label = "r00016870",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2  *3 C     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *2 C     1 {1,S}
6     O     0 {2,S} {7,S}
7     O     0 {6,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 C     0 {3,D}
""",
    product2 = 
"""
1  *3 C     1 {2,S}
2     O     0 {1,S} {3,S}
3     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.5e+13,"s^-1"),
        n = 0,
        Ea = (116403,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baldwin, R.R.", "Hisham, M.W.M.", "Walker, R.W."], title=u'Arrhenius parameters of elementary reactions involved in the oxidation of neopentane', journal="J. Chem. Soc. Faraday Trans. 1", volume="78", pages="""1615""", year="1982", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:36:02 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 386,
    label = "r00016871",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S} {6,S}
3  *3 C     0 {1,S}
4     C     0 {1,S}
5  *2 C     1 {1,S}
6     O     0 {2,S} {7,S}
7     O     0 {6,S}
""",
    product1 = 
"""
1     C     0 {3,S} {5,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 C     0 {3,D}
5     O     0 {1,S} {6,S}
6     O     0 {5,S}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.17e+45,"s^-1"),
        n = -11,
        Ea = (585411,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Sun, H.", "Bozzelli, J.W."], title=u'Thermochemical and kinetic analysis on the reactions of neopentyl and hydroperoxy-neopentyl radicals with oxygen: Part I.  OH and initial stable HC product formation', journal="J. Phys. Chem. A", volume="108", pages="""1694-1711""", year="2004", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:36:02 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 387,
    label = "r00016871",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S} {6,S}
3  *3 C     0 {1,S}
4     C     0 {1,S}
5  *2 C     1 {1,S}
6     O     0 {2,S} {7,S}
7     O     0 {6,S}
""",
    product1 = 
"""
1     C     0 {3,S} {5,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 C     0 {3,D}
5     O     0 {1,S} {6,S}
6     O     0 {5,S}
""",
    product2 = 
"""
1  *3 C     1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.72e+26,"s^-1"),
        n = -5.92,
        Ea = (325660,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Sun, H.", "Bozzelli, J.W."], title=u'Thermochemical and kinetic analysis on the reactions of neopentyl and hydroperoxy-neopentyl radicals with oxygen: Part I.  OH and initial stable HC product formation', journal="J. Phys. Chem. A", volume="108", pages="""1694-1711""", year="2004", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:36:03 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 388,
    label = "r00016900",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,D}
2  *1 C     0 {1,S} {4,D}
3     C     0 {1,D}
4  *2 C     1 {2,D}
""",
    product1 = 
"""
1  *2 C     0 {2,T}
2  *1 C     0 {1,T}
""",
    product2 = 
"""
1     C     0 {2,D}
2  *3 C     1 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14,"s^-1"),
        n = 0,
        Ea = (183750,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:36:03 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 389,
    label = "r00016900",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1     C     0 {2,D}
2  *3 C     1 {1,D}
""",
    product1 = 
"""
1  *3 C     0 {2,S} {3,D}
2  *1 C     0 {1,S} {4,D}
3     C     0 {1,D}
4  *2 C     1 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.15e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (12970.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Callear, A.B.", "Smith, G.B."], title=u'Addition of atomic hydrogen to acetylene. Chain reactions of the vinyl radical', journal="Chem. Phys. Lett.", volume="105", pages="""119""", year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:36:03 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 390,
    label = "r00016900",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1     C     0 {2,D}
2  *3 C     1 {1,D}
""",
    product1 = 
"""
1  *3 C     0 {2,S} {3,D}
2  *1 C     0 {1,S} {4,D}
3     C     0 {1,D}
4  *2 C     1 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.31e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (19622.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Weissman, M.", "Benson, S.W."], title=u'Pyrolysis of methyl chloride, a pathway in the chlorine-catalyzed polymerization of methane', journal="Int. J. Chem. Kinet.", volume="16", pages="""307""", year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:36:03 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 391,
    label = "r00016900",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1     C     0 {2,D}
2  *3 C     1 {1,D}
""",
    product1 = 
"""
1  *3 C     0 {2,S} {3,D}
2  *1 C     0 {1,S} {4,D}
3     C     0 {1,D}
4  *2 C     1 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.19e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20287.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Duran, R.P.", "Amorebieta, V.T.", "Colussi, A.J."], title=u'Is the homogeneous thermal dimerization of acetylene a free-radical chain reaction? Kinetic and thermochemical analysis', journal="J. Phys. Chem.", volume="92", pages="""636""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:36:03 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 392,
    label = "r00016900",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1     C     0 {2,D}
2  *3 C     1 {1,D}
""",
    product1 = 
"""
1  *3 C     0 {2,S} {3,D}
2  *1 C     0 {1,S} {4,D}
3     C     0 {1,D}
4  *2 C     1 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (250819,"cm^3/(mol*s)"),
        n = 1.9,
        Ea = (8813.34,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Weissman, M.A.", "Benson, S.W."], title=u'Rate parameters for the reactions of C_2H_3 and C_4H_5 with H_2 and C_2H_2', journal="J. Phys. Chem.", volume="92", pages="""4080""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:36:03 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 393,
    label = "r00016900",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1     C     0 {2,D}
2  *3 C     1 {1,D}
""",
    product1 = 
"""
1  *3 C     0 {2,S} {3,D}
2  *1 C     0 {1,S} {4,D}
3     C     0 {1,D}
4  *2 C     1 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (25109.7,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Benson, S.W."], title=u'The mechanism of the reversible reaction: 2C_2H_2 = vinyl acetylene and the pyrolysis of butadiene', journal="Int. J. Chem. Kinet.", volume="21", pages="""233""", year="1989", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000008.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:36:03 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 394,
    label = "r00016901",
    reactant1 = 
"""
1     C     0 {2,S} {3,D}
2  *1 C     0 {1,S} {4,D} {5,S}
3     C     0 {1,D}
4  *2 C     1 {2,D}
5  *3 H     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *1 C     0 {1,S} {4,T}
4  *2 C     0 {3,T}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14,"s^-1"),
        n = 0,
        Ea = (172941,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Weissman, M.", "Benson, S.W."], title=u'Pyrolysis of methyl chloride, a pathway in the chlorine-catalyzed polymerization of methane', journal="Int. J. Chem. Kinet.", volume="16", pages="""307""", year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:36:03 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 395,
    label = "r00016901",
    reactant1 = 
"""
1     C     0 {2,S} {3,D}
2  *1 C     0 {1,S} {4,D} {5,S}
3     C     0 {1,D}
4  *2 C     1 {2,D}
5  *3 H     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *1 C     0 {1,S} {4,T}
4  *2 C     0 {3,T}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+14,"s^-1"),
        n = 0,
        Ea = (172941,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Colket, M.B., III", "Seery, D.J.", "Palmer, H.B."], title=u'The pyrolysis of acetylene initiated by acetone', journal="Combust. Flame", volume="75", pages="""343-366""", year="1989", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:36:03 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 396,
    label = "r00017010",
    reactant1 = 
"""
1  *1 C     0 {2,D} {3,S}
2  *2 C     1 {1,D}
3  *3 O     0 {1,S}
""",
    product1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    product2 = 
"""
1  *3 O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+12,"s^-1"),
        n = 0,
        Ea = (125549,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Lai, L-H.", "Hsu, Y-C.", "Lee, Y-P."], title=u'The enthalpy change and the detailed rate coefficients of the equilibrium reaction OH+C_2H_2 + M = HOC_2H_2 + M over the temperature range 627-713K', journal="J. Chem. Phys.", volume="97", pages="""3092-3099""", year="1992", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:36:10 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 397,
    label = "r00017010",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1  *3 O     1
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,S}
2  *2 C     1 {1,D}
3  *3 O     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.12e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (5861.7,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Liu, A.", "Mulac, W.A.", "Jonah, C.D."], title=u'Temperature dependence of the rate constants of the reactions of OH radicals with C_2H_2 and C_2D_2 at 1 atm in Ar and from 333 to 1273 K', journal="J. Phys. Chem.", volume="92", pages="""5942""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:36:10 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 398,
    label = "r00017010",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1  *3 O     1
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,S}
2  *2 C     1 {1,D}
3  *3 O     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.12e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (5853.39,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Liu, A.", "Jonah, C.D.", "Mulac, W.A."], title=u'The gas-phase reactions of hydroxyl radicals with several unsaturated hydrocarbons at atmosphere pressure', journal="Radiat. Phys. Chem.", volume="34", pages="""687-691""", year="1989", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:36:10 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 399,
    label = "r00017010",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1  *3 O     1
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,S}
2  *2 C     1 {1,D}
3  *3 O     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.51783e+08,"cm^3/(mol*s)"),
        n = 1.7,
        Ea = (4182.18,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Miller, J.A.", "Melius, C.F."], title=u'A theoretical analysis of the reaction between hydroxyl and acetylene', journal="Symp. Int. Combust. Proc.", volume="22", pages="""1031-1039""", year="1989", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:36:10 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 400,
    label = "r00017010",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1  *3 O     1
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,S}
2  *2 C     1 {1,D}
3  *3 O     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.21e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1912.33,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Esser, C.", "Frank, P.", "Just, Th.", "Kerr, J.A.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."], title=u'Evaluated kinetic data for combustion modelling', journal="J. Phys. Chem. Ref. Data", volume="21", pages="""411-429""", year="1992", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:36:10 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 401,
    label = "r00017010",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1  *3 O     1
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,S}
2  *2 C     1 {1,D}
3  *3 O     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.62e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-12139.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Lai, L-H.", "Hsu, Y-C.", "Lee, Y-P."], title=u'The enthalpy change and the detailed rate coefficients of the equilibrium reaction OH+C_2H_2 + M = HOC_2H_2 + M over the temperature range 627-713K', journal="J. Chem. Phys.", volume="97", pages="""3092-3099""", year="1992", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:36:10 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 402,
    label = "r00017010",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1  *3 O     1
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,S}
2  *2 C     1 {1,D}
3  *3 O     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.23e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1687.84,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Siese, M.", "Zetzsch, C."], title=u'Addition of OH to acetylene and consecutive reactions of the adduct with O_2', journal="Z. Phys. Chem. (Munich)", volume="188", pages="""75-89""", year="1995", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:36:10 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 403,
    label = "r00017011",
    reactant1 = 
"""
1  *3 C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3  *1 C     0 {1,S} {5,D}
4     C     0 {2,S} {6,T}
5  *2 C     1 {3,D}
6     C     0 {4,T}
""",
    product1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    product2 = 
"""
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,T}
3  *3 C     1 {1,D}
4     C     0 {2,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.69e+26,"s^-1"),
        n = -14.7,
        Ea = (240288,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Braun-Unkhoff, M.", "Frank, P.", "Just, Th."], title=u'A shock tube study on the thermal decomposition of toluene and of the phenyl radical at high temperatures', journal="Symp. Int. Combust. Proc.", volume="22", pages="""1053""", year="1989", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:36:10 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 404,
    label = "r00017011",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,T}
3  *3 C     1 {1,D}
4     C     0 {2,T}
""",
    product1 = 
"""
1  *3 C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3  *1 C     0 {1,S} {5,D}
4     C     0 {2,S} {6,T}
5  *2 C     1 {3,D}
6     C     0 {4,T}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.15382e+15,"cm^3/(mol*s)"),
        n = -1.51,
        Ea = (20204.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Westmoreland, P.R.", "Dean, A.M.", "Howard, J.B.", "Longwell, J.P."], title=u'Forming benzene in flames by chemically activated isomerization', journal="J. Phys. Chem.", volume="93", pages="""8171""", year="1989", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:36:10 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 405,
    label = "r00017013",
    reactant1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3  *1 C     0 {1,S} {5,D} {7,S}
4     C     0 {2,S} {6,T}
5  *2 C     1 {3,D}
6     C     0 {4,T}
7  *3 H     0 {3,S}
""",
    product1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {4,S}
3     C     0 {1,S} {5,T}
4  *1 C     0 {2,S} {6,T}
5     C     0 {3,T}
6  *2 C     0 {4,T}
""",
    product2 = 
"""
1  *3 H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+24,"s^-1"),
        n = -13.8,
        Ea = (208693,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Braun-Unkhoff, M.", "Frank, P.", "Just, Th."], title=u'A shock tube study on the thermal decomposition of toluene and of the phenyl radical at high temperatures', journal="Symp. Int. Combust. Proc.", volume="22", pages="""1053""", year="1989", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:36:10 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 406,
    label = "r00017118",
    reactant1 = 
"""
1     C     0 {2,D} {3,S}
2  *3 C     0 {1,D} {4,S}
3     C     0 {1,S} {5,D}
4  *1 C     0 {2,S} {6,D}
5     C     0 {3,D}
6  *2 C     1 {4,D}
""",
    product1 = 
"""
1  *2 C     0 {2,T}
2  *1 C     0 {1,T}
""",
    product2 = 
"""
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4  *3 C     1 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.16e+13,"s^-1"),
        n = 0,
        Ea = (180424,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dean, A.M."], title=u'Predictions of pressure and temperature effects upon radical addition and recombination reactions', journal="J. Phys. Chem.", volume="89", pages="""4600""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:36:12 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 407,
    label = "r00017118",
    reactant1 = 
"""
1  *1 C     0 {2,T}
2  *2 C     0 {1,T}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3     C     0 {1,D}
4  *3 C     1 {2,D}
""",
    product1 = 
"""
1     C     0 {2,D} {3,S}
2  *3 C     0 {1,D} {4,S}
3     C     0 {1,S} {5,D}
4  *1 C     0 {2,S} {6,D}
5     C     0 {3,D}
6  *2 C     1 {4,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.24474e+14,"cm^3/(mol*s)"),
        n = -1.38,
        Ea = (16628.9,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Westmoreland, P.R.", "Dean, A.M.", "Howard, J.B.", "Longwell, J.P."], title=u'Forming benzene in flames by chemically activated isomerization', journal="J. Phys. Chem.", volume="93", pages="""8171""", year="1989", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:36:12 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

