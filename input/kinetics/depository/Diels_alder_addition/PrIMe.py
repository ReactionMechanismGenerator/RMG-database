#!/usr/bin/env python
# encoding: utf-8

name = "Diels_alder_addition"
shortDesc = ""
longDesc = """

"""

entry(
    index = 1,
    label = "r00002185",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,D}
4  *6 C     0 {2,S} {6,D}
5  *4 C     0 {3,D} {6,S}
6  *5 C     0 {4,D} {5,S}
""",
    product1 = 
"""
1  *3 C     0 {3,S} {5,S} {7,S}
2  *6 C     0 {4,S} {6,S} {8,S}
3  *1 C     0 {1,S} {4,S}
4  *2 C     0 {2,S} {3,S}
5     C     0 {1,S} {6,S}
6     C     0 {2,S} {5,S}
7  *4 C     0 {1,S} {8,D}
8  *5 C     0 {2,S} {7,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (4.57e+09,"cm^3/(mol*s)"),
        n = 0,
        Ea = (108920,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Huybrechts, G.", "Rigaux, D.", "Vankeerberghen, J.", "Van Mele, B."], title=u'Kinetics of the Diels-Alder Addition of Ethene to Cyclohexa-1,3-Diene and Its Reverse Reaction in the Gas Phase', journal="Int. J. Chem. Kinet.", volume="12", pages="""253""", year="1980", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 2,
    label = "r00002185",
    reactant1 = 
"""
1  *3 C     0 {3,S} {4,S} {7,S}
2  *6 C     0 {5,S} {6,S} {8,S}
3  *1 C     0 {1,S} {5,S}
4     C     0 {1,S} {6,S}
5  *2 C     0 {2,S} {3,S}
6     C     0 {2,S} {4,S}
7  *4 C     0 {1,S} {8,D}
8  *5 C     0 {2,S} {7,D}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *6 C     0 {1,S} {5,D}
4  *3 C     0 {2,S} {6,D}
5  *5 C     0 {3,D} {6,S}
6  *4 C     0 {4,D} {5,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.88e+15,"s^-1"),
        n = 0,
        Ea = (244445,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Cocks, A.T.", "Frey, H.M."], title=u'Thermal Unimolecular Decomposition of Bicyclo[2.2.2]oct-2-ene', journal="J. Chem. Soc. A", pages="""1661""", year="1971", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 3,
    label = "r00002185",
    reactant1 = 
"""
1  *3 C     0 {3,S} {4,S} {7,S}
2  *6 C     0 {5,S} {6,S} {8,S}
3  *1 C     0 {1,S} {5,S}
4     C     0 {1,S} {6,S}
5  *2 C     0 {2,S} {3,S}
6     C     0 {2,S} {4,S}
7  *4 C     0 {1,S} {8,D}
8  *5 C     0 {2,S} {7,D}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *6 C     0 {1,S} {5,D}
4  *3 C     0 {2,S} {6,D}
5  *5 C     0 {3,D} {6,S}
6  *4 C     0 {4,D} {5,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.32e+15,"s^-1"),
        n = 0,
        Ea = (239457,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Huybrechts, G.", "Rigaux, D.", "Vankeerberghen, J.", "Van Mele, B."], title=u'Kinetics of the Diels-Alder Addition of Ethene to Cyclohexa-1,3-Diene and Its Reverse Reaction in the Gas Phase', journal="Int. J. Chem. Kinet.", volume="12", pages="""253""", year="1980", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 4,
    label = "r00003841",
    reactant1 = 
"""
1     C     0 {2,S}
2  *4 C     0 {1,S} {3,S} {4,D}
3  *5 C     0 {2,S} {5,D}
4  *3 C     0 {2,D}
5  *6 C     0 {3,D}
""",
    reactant2 = 
"""
1  *2 C     0 {2,D} {3,S}
2  *1 C     0 {1,D}
3     C     0 {1,S} {4,D}
4     O     0 {3,D}
""",
    product1 = 
"""
1  *2 C     0 {2,S} {4,S} {8,S}
2  *1 C     0 {1,S} {3,S}
3  *3 C     0 {2,S} {6,S}
4  *6 C     0 {1,S} {7,S}
5     C     0 {6,S}
6  *4 C     0 {3,S} {5,S} {7,D}
7  *5 C     0 {4,S} {6,D}
8     C     0 {1,S} {9,D}
9     O     0 {8,D}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.02e+09,"cm^3/(mol*s)"),
        n = 0,
        Ea = (78239.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kistiakowsky, G.B.", "Lacher, J.R."], title=u'The kinetics of some gaseous diels-alder reactions', journal="J. Am. Chem. Soc.", volume="58", pages="""123-133""", year="1936", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:38 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 5,
    label = "r00004731",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3  *2 C     0 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
1  *4 C     0 {2,S} {3,D}
2  *5 C     0 {1,S} {4,D}
3  *3 C     0 {1,D}
4  *6 C     0 {2,D}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S} {5,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {6,S}
4  *6 C     0 {2,S} {7,S}
5     C     0 {1,S} {8,D}
6  *4 C     0 {3,S} {7,D}
7  *5 C     0 {4,S} {6,D}
8     C     0 {5,D}
""",
    degeneracy = 32,
    kinetics = Arrhenius(
        A = (4.71e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (108920,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Vaughan, W.E."], title=u'The homogeneous thermal polymerization of 1,3-butadiene', journal="J. Am. Chem. Soc.", volume="54", pages="""3863-3876""", year="1932", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 6,
    label = "r00004731",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3  *2 C     0 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
1  *4 C     0 {2,S} {3,D}
2  *5 C     0 {1,S} {4,D}
3  *3 C     0 {1,D}
4  *6 C     0 {2,D}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S} {5,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {6,S}
4  *6 C     0 {2,S} {7,S}
5     C     0 {1,S} {8,D}
6  *4 C     0 {3,S} {7,D}
7  *5 C     0 {4,S} {6,D}
8     C     0 {5,D}
""",
    degeneracy = 32,
    kinetics = Arrhenius(
        A = (1.38e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (112245,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Rowley, D.", "Steiner, H."], title=u'Kinetics of diene reactions at high temperatures', journal="Discuss. Faraday Soc.", volume="10", pages="""198-213""", year="1951", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 7,
    label = "r00004731",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3  *2 C     0 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
1  *4 C     0 {2,S} {3,D}
2  *5 C     0 {1,S} {4,D}
3  *3 C     0 {1,D}
4  *6 C     0 {2,D}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S} {5,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {6,S}
4  *6 C     0 {2,S} {7,S}
5     C     0 {1,S} {8,D}
6  *4 C     0 {3,S} {7,D}
7  *5 C     0 {4,S} {6,D}
8     C     0 {5,D}
""",
    degeneracy = 32,
    kinetics = Arrhenius(
        A = (8.91e+09,"cm^3/(mol*s)"),
        n = 0,
        Ea = (102268,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Huybrechts, G.", "Luyckx, L.", "Vandenboom, Th.", "Van Mele, B."], title=u'Thermal Dimerization of 1,3-Butadiene: Kinetics of the Formation of cis, cis-Cycloocta-1,5-diene', journal="Int. J. Chem. Kinet.", volume="9", pages="""283""", year="1977", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 8,
    label = "r00004731",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {5,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {7,S}
4  *6 C     0 {2,S} {6,S}
5     C     0 {1,S} {8,D}
6  *5 C     0 {4,S} {7,D}
7  *4 C     0 {3,S} {6,D}
8     C     0 {5,D}
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
1  *5 C     0 {2,S} {4,D}
2  *4 C     0 {1,S} {3,D}
3  *3 C     0 {2,D}
4  *6 C     0 {1,D}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (5.02e+15,"s^-1"),
        n = 0,
        Ea = (258580,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Duncan, N.E.", "Janz, G.J."], title=u'The thermal dimerization of butadiene, and the equilibrium between butadiene and vinylcyclohexene', journal="J. Chem. Phys.", volume="20", pages="""1644-1645""", year="1952", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 9,
    label = "r00004731",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {5,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {7,S}
4  *6 C     0 {2,S} {6,S}
5     C     0 {1,S} {8,D}
6  *5 C     0 {4,S} {7,D}
7  *4 C     0 {3,S} {6,D}
8     C     0 {5,D}
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
1  *5 C     0 {2,S} {4,D}
2  *4 C     0 {1,S} {3,D}
3  *3 C     0 {2,D}
4  *6 C     0 {1,D}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.58e+15,"s^-1"),
        n = 0,
        Ea = (259412,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Decyclization of cyclohexene, 4-methylcyclohexene, and 4-vinylcyclohexene in a single-pulse shock tube', journal="J. Chem. Phys.", volume="42", pages="""1805-1809""", year="1965", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 10,
    label = "r00004731",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {5,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {7,S}
4  *6 C     0 {2,S} {6,S}
5     C     0 {1,S} {8,D}
6  *5 C     0 {4,S} {7,D}
7  *4 C     0 {3,S} {6,D}
8     C     0 {5,D}
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
1  *5 C     0 {2,S} {4,D}
2  *4 C     0 {1,S} {3,D}
3  *3 C     0 {2,D}
4  *6 C     0 {1,D}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (6.17e+15,"s^-1"),
        n = 0,
        Ea = (261906,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Barnard, J.A.", "Parrott, T.K."], title=u'Kinetics of the thermal unimolecular reactions of cyclohexene and 4-vinylcyclohexene behind reflected shock waves', journal="J. Chem. Soc. Faraday Trans. 1", volume="72", pages="""2404""", year="1976", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 11,
    label = "r00004731",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {5,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {7,S}
4  *6 C     0 {2,S} {6,S}
5     C     0 {1,S} {8,D}
6  *5 C     0 {4,S} {7,D}
7  *4 C     0 {3,S} {6,D}
8     C     0 {5,D}
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
1  *5 C     0 {2,S} {4,D}
2  *4 C     0 {1,S} {3,D}
3  *3 C     0 {2,D}
4  *6 C     0 {1,D}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (2.51e+14,"s^-1"),
        n = 0,
        Ea = (251929,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Huybrechts, G.", "Luyckx, L.", "Vandenboom, Th.", "Van Mele, B."], title=u'Thermal Dimerization of 1,3-Butadiene: Kinetics of the Formation of cis, cis-Cycloocta-1,5-diene', journal="Int. J. Chem. Kinet.", volume="9", pages="""283""", year="1977", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 12,
    label = "r00004734",
    reactant1 = 
"""
1  *4 C     0 {2,S} {3,D}
2  *5 C     0 {1,S} {4,D}
3  *3 C     0 {1,D}
4  *6 C     0 {2,D}
""",
    reactant2 = 
"""
1  *1 C     0 {2,D} {3,S}
2  *2 C     0 {1,D}
3     C     0 {1,S} {4,D}
4     O     0 {3,D}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S} {7,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,S}
4  *6 C     0 {2,S} {6,S}
5  *4 C     0 {3,S} {6,D}
6  *5 C     0 {4,S} {5,D}
7     C     0 {1,S} {8,D}
8     O     0 {7,D}
""",
    degeneracy = 16,
    kinetics = Arrhenius(
        A = (1.46e+09,"cm^3/(mol*s)"),
        n = 0,
        Ea = (82396.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kistiakowsky, G.B.", "Lacher, J.R."], title=u'The kinetics of some gaseous diels-alder reactions', journal="J. Am. Chem. Soc.", volume="58", pages="""123-133""", year="1936", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 13,
    label = "r00004737",
    reactant1 = 
"""
1  *4 C     0 {2,S} {3,D}
2  *5 C     0 {1,S} {4,D}
3  *3 C     0 {1,D}
4  *6 C     0 {2,D}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *1 C     0 {1,S} {5,D}
4     C     0 {2,S} {6,D}
5  *2 C     0 {3,D} {6,S}
6     C     0 {4,D} {5,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *2 C     0 {1,S} {5,S} {7,S}
3     C     0 {1,S} {6,S}
4  *3 C     0 {1,S} {8,S}
5  *6 C     0 {2,S} {9,S}
6     C     0 {3,S} {10,S}
7     C     0 {2,S} {10,D}
8  *4 C     0 {4,S} {9,D}
9  *5 C     0 {5,S} {8,D}
10    C     0 {6,S} {7,D}
""",
    degeneracy = 32,
    kinetics = Arrhenius(
        A = (1.05e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (106425,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Huybrechts, G.", "Hubin, Y.", "Narmon, M.", "Van Mele, B."], title=u'Kinetics and Mechanism of the Addition of 1,3-Butadiene to Cyclohexa-1,3-diene in the Gas Phase', journal="Int. J. Chem. Kinet.", volume="14", pages="""259""", year="1982", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 14,
    label = "r00004794",
    reactant1 = 
"""
1  *4 C     0 {2,S} {3,D}
2  *5 C     0 {1,S} {4,D}
3  *3 C     0 {1,D}
4  *6 C     0 {2,D}
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     0 {2,D} {4,S}
4     C     0 {3,S} {5,D}
5     O     0 {4,D}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S} {5,S}
2  *2 C     0 {1,S} {4,S} {8,S}
3  *3 C     0 {1,S} {6,S}
4  *6 C     0 {2,S} {7,S}
5     C     0 {1,S}
6  *4 C     0 {3,S} {7,D}
7  *5 C     0 {4,S} {6,D}
8     C     0 {2,S} {9,D}
9     O     0 {8,D}
""",
    degeneracy = 16,
    kinetics = Arrhenius(
        A = (8.99e+08,"cm^3/(mol*s)"),
        n = 0,
        Ea = (92290.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kistiakowsky, G.B.", "Lacher, J.R."], title=u'The kinetics of some gaseous diels-alder reactions', journal="J. Am. Chem. Soc.", volume="58", pages="""123-133""", year="1936", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:48 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 15,
    label = "r00004843",
    reactant1 = 
"""
1  *1 C     0 {2,D} {3,S}
2  *2 C     0 {1,D}
3     C     0 {1,S} {4,D}
4     O     0 {3,D}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,D}
4  *6 C     0 {2,S} {6,D}
5  *4 C     0 {3,D} {6,S}
6  *5 C     0 {4,D} {5,S}
""",
    product1 = 
"""
1  *3 C     0 {2,S} {5,S} {7,S}
2  *1 C     0 {1,S} {4,S} {9,S}
3  *6 C     0 {4,S} {6,S} {8,S}
4  *2 C     0 {2,S} {3,S}
5     C     0 {1,S} {6,S}
6     C     0 {3,S} {5,S}
7  *4 C     0 {1,S} {8,D}
8  *5 C     0 {3,S} {7,D}
9     C     0 {2,S} {10,D}
10    O     0 {9,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.24e+08,"cm^3/(mol*s)"),
        n = 0,
        Ea = (86470.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Huybrechts, G.", "Paternoster, G.", "Baetens, P."], title=u'Kinetics of the Diels-Alder Addition of Acrolein to Cyclohexa-1,3-diene and Its Reverse Reaction in the Gas Phase', journal="Int. J. Chem. Kinet.", volume="8", pages="""641""", year="1976", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:48 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 16,
    label = "r00004843",
    reactant1 = 
"""
1  *1 C     0 {2,D} {3,S}
2  *2 C     0 {1,D}
3     C     0 {1,S} {4,D}
4     O     0 {3,D}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,D}
4  *6 C     0 {2,S} {6,D}
5  *4 C     0 {3,D} {6,S}
6  *5 C     0 {4,D} {5,S}
""",
    product1 = 
"""
1  *3 C     0 {2,S} {5,S} {7,S}
2  *1 C     0 {1,S} {4,S} {9,S}
3  *6 C     0 {4,S} {6,S} {8,S}
4  *2 C     0 {2,S} {3,S}
5     C     0 {1,S} {6,S}
6     C     0 {3,S} {5,S}
7  *4 C     0 {1,S} {8,D}
8  *5 C     0 {3,S} {7,D}
9     C     0 {2,S} {10,D}
10    O     0 {9,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.02e+09,"cm^3/(mol*s)"),
        n = 0,
        Ea = (83976.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Van Mele, B.", "Tybaert, C.", "Huybrechts, G."], title=u'Kinetics, mechanism, and stereochemistry of Diels-Alder reactions of carbonyl-substituted ethenes with cyclohexa-1,3-diene in the gas phase', journal="Int. J. Chem. Kinet.", volume="19", pages="""1063""", year="1987", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:48 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 17,
    label = "r00005509",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,S}
4  *6 C     0 {2,S} {6,S}
5  *4 C     0 {3,S} {6,D}
6  *5 C     0 {4,S} {5,D}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1  *5 C     0 {2,S} {3,D}
2  *4 C     0 {1,S} {4,D}
3  *6 C     0 {1,D}
4  *3 C     0 {2,D}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (8.89e+12,"s^-1"),
        n = 0,
        Ea = (240288,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kuchler, L."], title=u'Homogenous thermal decomposition of some cyclic hydrocarbons', journal="J. Chem. Soc. Faraday Trans.", volume="35", pages="""874""", year="1939", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:53 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 18,
    label = "r00005509",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,S}
4  *6 C     0 {2,S} {6,S}
5  *4 C     0 {3,S} {6,D}
6  *5 C     0 {4,S} {5,D}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1  *5 C     0 {2,S} {3,D}
2  *4 C     0 {1,S} {4,D}
3  *6 C     0 {1,D}
4  *3 C     0 {2,D}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.22e+12,"s^-1"),
        n = 0,
        Ea = (230311,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kraus, M.", "Vavruska, M.", "Bazant, V."], title=u'Diene durch pyrolyse von cyclischen verbindungen. III. Die kinetik der spaltung von cyclohexen und cyclohexylacetat', journal="Collect. Czech. Chem. Commun.", volume="22", pages="""484""", year="1957", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:53 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 19,
    label = "r00005509",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,S}
4  *6 C     0 {2,S} {6,S}
5  *4 C     0 {3,S} {6,D}
6  *5 C     0 {4,S} {5,D}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1  *5 C     0 {2,S} {3,D}
2  *4 C     0 {1,S} {4,D}
3  *6 C     0 {1,D}
4  *3 C     0 {2,D}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.4e+17,"s^-1"),
        n = 0,
        Ea = (304310,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Smith, S.R.", "Gordon, A.S."], title=u'A study of the pyrolysis of cyclohexene', journal="J. Phys. Chem.", volume="65", pages="""1124""", year="1961", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:53 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 20,
    label = "r00005509",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,S}
4  *6 C     0 {2,S} {6,S}
5  *4 C     0 {3,S} {6,D}
6  *5 C     0 {4,S} {5,D}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1  *5 C     0 {2,S} {3,D}
2  *4 C     0 {1,S} {4,D}
3  *6 C     0 {1,D}
4  *3 C     0 {2,D}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.45e+15,"s^-1"),
        n = 0,
        Ea = (276872,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Uchiyama, M.", "Tomioka, T.", "Amano, A."], title=u'Thermal decomposition of cyclohexene', journal="Ber. Bunsenges. Phys. Chem.", volume="68", pages="""1878""", year="1964", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:53 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 21,
    label = "r00005509",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,S}
4  *6 C     0 {2,S} {6,S}
5  *4 C     0 {3,S} {6,D}
6  *5 C     0 {4,S} {5,D}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1  *5 C     0 {2,S} {3,D}
2  *4 C     0 {1,S} {4,D}
3  *6 C     0 {1,D}
4  *3 C     0 {2,D}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.58e+15,"s^-1"),
        n = 0,
        Ea = (279366,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Decyclization of cyclohexene, 4-methylcyclohexene, and 4-vinylcyclohexene in a single-pulse shock tube', journal="J. Chem. Phys.", volume="42", pages="""1805-1809""", year="1965", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:53 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 22,
    label = "r00005509",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,S}
4  *6 C     0 {2,S} {6,S}
5  *4 C     0 {3,S} {6,D}
6  *5 C     0 {4,S} {5,D}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1  *5 C     0 {2,S} {3,D}
2  *4 C     0 {1,S} {4,D}
3  *6 C     0 {1,D}
4  *3 C     0 {2,D}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (2e+15,"s^-1"),
        n = 0,
        Ea = (280198,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Comparative rate single-pulse shock tube studies on the thermal decomposition of cyclohexene, 2,2,3-trimethylbutane, isopropyl bromide, and ethylcyclobutane', journal="Int. J. Chem. Kinet.", volume="2", pages="""311""", year="1970", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:53 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 23,
    label = "r00005509",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,S}
4  *6 C     0 {2,S} {6,S}
5  *4 C     0 {3,S} {6,D}
6  *5 C     0 {4,S} {5,D}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1  *5 C     0 {2,S} {3,D}
2  *4 C     0 {1,S} {4,D}
3  *6 C     0 {1,D}
4  *3 C     0 {2,D}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.41e+15,"s^-1"),
        n = 0,
        Ea = (278535,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Thermal Decomposition of 1,1,2,2-Tetramethylcyclopropane in a Single-Pulse Shock Tube', journal="Int. J. Chem. Kinet.", volume="5", pages="""651""", year="1973", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:53 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 24,
    label = "r00005509",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,S}
4  *6 C     0 {2,S} {6,S}
5  *4 C     0 {3,S} {6,D}
6  *5 C     0 {4,S} {5,D}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1  *5 C     0 {2,S} {3,D}
2  *4 C     0 {1,S} {4,D}
3  *6 C     0 {1,D}
4  *3 C     0 {2,D}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.45e+15,"s^-1"),
        n = 0,
        Ea = (274378,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Barnard, J.A.", "Parrott, T.K."], title=u'Kinetics of the thermal unimolecular reactions of cyclohexene and 4-vinylcyclohexene behind reflected shock waves', journal="J. Chem. Soc. Faraday Trans. 1", volume="72", pages="""2404""", year="1976", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000008.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:53 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 25,
    label = "r00005509",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,S}
4  *6 C     0 {2,S} {6,S}
5  *4 C     0 {3,S} {6,D}
6  *5 C     0 {4,S} {5,D}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1  *5 C     0 {2,S} {3,D}
2  *4 C     0 {1,S} {4,D}
3  *6 C     0 {1,D}
4  *3 C     0 {2,D}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.82e+15,"s^-1"),
        n = 0,
        Ea = (274378,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Newman, C.G.", "O'Neal, H.E.", "Ring, M.A.", "Leska, F.", "Shipley, N."], title=u'Kinetics and mechanism of the silane decomposition', journal="Int. J. Chem. Kinet.", volume="11", pages="""1167""", year="1979", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000009.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:53 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 26,
    label = "r00005509",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,S}
4  *6 C     0 {2,S} {6,S}
5  *4 C     0 {3,S} {6,D}
6  *5 C     0 {4,S} {5,D}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1  *5 C     0 {2,S} {3,D}
2  *4 C     0 {1,S} {4,D}
3  *6 C     0 {1,D}
4  *3 C     0 {2,D}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (2.51e+15,"s^-1"),
        n = 0,
        Ea = (280198,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Skinner, G.B.", "Rogers, D.", "Patel, K.B."], title=u'Consistency of theory and experiment in the ethane-methyl radical system', journal="Int. J. Chem. Kinet.", volume="13", pages="""481""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000010.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:53 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 27,
    label = "r00005509",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,S}
4  *6 C     0 {2,S} {6,S}
5  *4 C     0 {3,S} {6,D}
6  *5 C     0 {4,S} {5,D}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1  *5 C     0 {2,S} {3,D}
2  *4 C     0 {1,S} {4,D}
3  *6 C     0 {1,D}
4  *3 C     0 {2,D}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.5e+15,"s^-1"),
        n = 0,
        Ea = (280198,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Hidaka, Y.", "Chimori, T.", "Shiba, S.", "Suga, M."], title=u'Decyclization of cyclohexene in shock waves', journal="Chem. Phys. Lett.", volume="111", pages="""181""", year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000011.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:53 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 28,
    label = "r00005509",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,S}
4  *6 C     0 {2,S} {6,S}
5  *4 C     0 {3,S} {6,D}
6  *5 C     0 {4,S} {5,D}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1  *5 C     0 {2,S} {3,D}
2  *4 C     0 {1,S} {4,D}
3  *6 C     0 {1,D}
4  *3 C     0 {2,D}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.41e+15,"s^-1"),
        n = 0,
        Ea = (1.09974e+06,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Lewis, D.K.", "Bergmann, J.", "Manjoney, R.", "Paddock, R.", "Kaira, B.L."], title=u'Rates of reactions of cyclopropane, cyclobutane, cyclopentene, and cyclohexene in the presence of boron trichloride', journal="J. Phys. Chem.", volume="88", pages="""4112""", year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000012.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:53 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 29,
    label = "r00005509",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,S}
4  *6 C     0 {2,S} {6,S}
5  *4 C     0 {3,S} {6,D}
6  *5 C     0 {4,S} {5,D}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1  *5 C     0 {2,S} {3,D}
2  *4 C     0 {1,S} {4,D}
3  *6 C     0 {1,D}
4  *3 C     0 {2,D}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (3.72e+15,"s^-1"),
        n = 0,
        Ea = (275209,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kiefer, J.H.", "Shah, J.N."], title=u'Unimolecular dissociation of cyclohexene at extremely high temperatures: Behavior of the energy-transfer collision efficiency', journal="J. Phys. Chem.", volume="91", pages="""3024""", year="1987", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000013.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:53 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 30,
    label = "r00005509",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,S}
4  *6 C     0 {2,S} {6,S}
5  *4 C     0 {3,S} {6,D}
6  *5 C     0 {4,S} {5,D}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1  *5 C     0 {2,S} {3,D}
2  *4 C     0 {1,S} {4,D}
3  *6 C     0 {1,D}
4  *3 C     0 {2,D}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (4.6e+39,"s^-1"),
        n = -25.3,
        Ea = (483071,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kiefer, J.H.", "Shah, J.N."], title=u'Unimolecular dissociation of cyclohexene at extremely high temperatures: Behavior of the energy-transfer collision efficiency', journal="J. Phys. Chem.", volume="91", pages="""3024""", year="1987", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000014.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:53 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 31,
    label = "r00005509",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,S}
4  *6 C     0 {2,S} {6,S}
5  *4 C     0 {3,S} {6,D}
6  *5 C     0 {4,S} {5,D}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1  *5 C     0 {2,S} {3,D}
2  *4 C     0 {1,S} {4,D}
3  *6 C     0 {1,D}
4  *3 C     0 {2,D}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (9.51e+37,"s^-1"),
        n = -23.6,
        Ea = (465610,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kiefer, J.H.", "Shah, J.N."], title=u'Unimolecular dissociation of cyclohexene at extremely high temperatures: Behavior of the energy-transfer collision efficiency', journal="J. Phys. Chem.", volume="91", pages="""3024""", year="1987", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000015.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:53 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 32,
    label = "r00007108",
    reactant1 = 
"""
1  *1 C     0 {2,S} {5,S}
2  *2 C     0 {1,S} {6,S}
3     C     0 {4,S} {7,S}
4     C     0 {3,S} {8,S}
5  *3 C     0 {1,S} {9,S}
6  *6 C     0 {2,S} {10,S}
7     C     0 {3,S} {9,S}
8     C     0 {4,S} {10,S}
9  *4 C     0 {5,S} {7,S} {10,D}
10 *5 C     0 {6,S} {8,S} {9,D}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S} {6,S}
5  *5 C     0 {3,S} {6,S} {7,D}
6  *4 C     0 {4,S} {5,S} {8,D}
7  *6 C     0 {5,D}
8  *3 C     0 {6,D}
""",
    degeneracy = 16,
    kinetics = Arrhenius(
        A = (5.13e+14,"s^-1"),
        n = 0,
        Ea = (260243,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Ondruschka, B.", "Zimmermann, G."], title=u'Pyrolysis kinetics of octalins', journal="J. Prakt. Chem.", volume="332", pages="""547""", year="1990", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:03 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 33,
    label = "r00007814",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {5,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {7,S}
4  *6 C     0 {2,S} {6,S}
5     C     0 {1,S}
6  *5 C     0 {4,S} {7,D}
7  *4 C     0 {3,S} {6,D}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    product2 = 
"""
1  *4 C     0 {2,S} {3,D}
2  *5 C     0 {1,S} {4,D}
3  *3 C     0 {1,D}
4  *6 C     0 {2,D}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.35e+15,"s^-1"),
        n = 0,
        Ea = (278535,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Decyclization of cyclohexene, 4-methylcyclohexene, and 4-vinylcyclohexene in a single-pulse shock tube', journal="J. Chem. Phys.", volume="42", pages="""1805-1809""", year="1965", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:10 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 34,
    label = "r00007814",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {5,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {7,S}
4  *6 C     0 {2,S} {6,S}
5     C     0 {1,S}
6  *5 C     0 {4,S} {7,D}
7  *4 C     0 {3,S} {6,D}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    product2 = 
"""
1  *4 C     0 {2,S} {3,D}
2  *5 C     0 {1,S} {4,D}
3  *3 C     0 {1,D}
4  *6 C     0 {2,D}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (2e+15,"s^-1"),
        n = 0,
        Ea = (277703,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Single-pulse shock tube study on the stability of perfluorobromomethane', journal="J. Phys. Chem.", volume="90", pages="""414-418""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:10 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 35,
    label = "r00007816",
    reactant1 = 
"""
1  *2 C     0 {2,S} {4,S}
2  *1 C     0 {1,S} {3,S}
3  *3 C     0 {2,S} {6,S}
4  *6 C     0 {1,S} {7,S}
5     C     0 {6,S}
6  *4 C     0 {3,S} {5,S} {7,D}
7  *5 C     0 {4,S} {6,D}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *4 C     0 {1,S} {3,S} {4,D}
3  *5 C     0 {2,S} {5,D}
4  *3 C     0 {2,D}
5  *6 C     0 {3,D}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (3.72e+15,"s^-1"),
        n = 0,
        Ea = (291007,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Simmie, J.M."], title=u'Kinetic Study of a Retro Diels-Alder Reaction in a Single-Pulse Shock Tube: Decyclization of 1-Methylcyclohex-1-ene', journal="Int. J. Chem. Kinet.", volume="10", pages="""227""", year="1978", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:10 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 36,
    label = "r00007816",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *4 C     0 {1,S} {3,S} {4,D}
3  *5 C     0 {2,S} {5,D}
4  *3 C     0 {2,D}
5  *6 C     0 {3,D}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {6,S}
4  *6 C     0 {2,S} {7,S}
5     C     0 {6,S}
6  *4 C     0 {3,S} {5,S} {7,D}
7  *5 C     0 {4,S} {6,D}
""",
    degeneracy = 16,
    kinetics = Arrhenius(
        A = (1.32e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (123886,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Simmie, J.M."], title=u'Kinetic Study of a Retro Diels-Alder Reaction in a Single-Pulse Shock Tube: Decyclization of 1-Methylcyclohex-1-ene', journal="Int. J. Chem. Kinet.", volume="10", pages="""227""", year="1978", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:10 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 37,
    label = "r00007902",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *1 C     0 {1,S} {5,D}
4     C     0 {2,S} {6,D}
5  *2 C     0 {3,D} {6,S}
6     C     0 {4,D} {5,S}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,D}
4  *6 C     0 {2,S} {6,D}
5  *4 C     0 {3,D} {6,S}
6  *5 C     0 {4,D} {5,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S} {5,S}
2  *2 C     0 {1,S} {4,S} {9,S}
3  *3 C     0 {1,S} {6,S} {10,S}
4  *6 C     0 {2,S} {7,S} {11,S}
5     C     0 {1,S} {8,S}
6     C     0 {3,S} {7,S}
7     C     0 {4,S} {6,S}
8     C     0 {5,S} {12,S}
9     C     0 {2,S} {12,D}
10 *4 C     0 {3,S} {11,D}
11 *5 C     0 {4,S} {10,D}
12    C     0 {8,S} {9,D}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (9.33e+08,"cm^3/(mol*s)"),
        n = 0,
        Ea = (104762,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["De Mare, G.R.", "Huybrechts, G.", "Toth, M.", "Goldfinger, P."], title=u'Thermal Dimerization of 1,3-Cyclohexadiene in the Gas Phase', journal="Trans. Faraday Soc.", volume="67", pages="""1397""", year="1971", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:11 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 38,
    label = "r00008812",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {5,S}
2  *2 C     0 {1,S} {4,S} {9,S}
3  *3 C     0 {1,S} {7,S} {11,S}
4  *6 C     0 {2,S} {6,S} {10,S}
5     C     0 {1,S} {8,S}
6     C     0 {4,S} {7,S}
7     C     0 {3,S} {6,S}
8     C     0 {5,S} {12,S}
9     C     0 {2,S} {12,D}
10 *5 C     0 {4,S} {11,D}
11 *4 C     0 {3,S} {10,D}
12    C     0 {8,S} {9,D}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *1 C     0 {1,S} {5,D}
4     C     0 {2,S} {6,D}
5  *2 C     0 {3,D} {6,S}
6     C     0 {4,D} {5,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,D}
4  *6 C     0 {2,S} {6,D}
5  *4 C     0 {3,D} {6,S}
6  *5 C     0 {4,D} {5,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.51e+14,"s^-1"),
        n = 0,
        Ea = (217839,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["De Mare, G.R.", "Huybrechts, G.", "Toth, M.", "Goldfinger, P."], title=u'Thermal Dimerization of 1,3-Cyclohexadiene in the Gas Phase', journal="Trans. Faraday Soc.", volume="67", pages="""1397""", year="1971", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:18 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 39,
    label = "r00008812",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *1 C     0 {1,S} {5,D}
4     C     0 {2,S} {6,D}
5  *2 C     0 {3,D} {6,S}
6     C     0 {4,D} {5,S}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,D}
4  *6 C     0 {2,S} {6,D}
5  *4 C     0 {3,D} {6,S}
6  *5 C     0 {4,D} {5,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S} {5,S}
2  *2 C     0 {1,S} {4,S} {9,S}
3  *3 C     0 {1,S} {6,S} {10,S}
4  *6 C     0 {2,S} {7,S} {11,S}
5     C     0 {1,S} {8,S}
6     C     0 {3,S} {7,S}
7     C     0 {4,S} {6,S}
8     C     0 {5,S} {12,S}
9     C     0 {2,S} {12,D}
10 *4 C     0 {3,S} {11,D}
11 *5 C     0 {4,S} {10,D}
12    C     0 {8,S} {9,D}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.2e+09,"cm^3/(mol*s)"),
        n = 0,
        Ea = (101437,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["De Mare, G.R.", "Huybrechts, G.", "Toth, M.", "Goldfinger, P."], title=u'Thermal Dimerization of 1,3-Cyclohexadiene in the Gas Phase', journal="Trans. Faraday Soc.", volume="67", pages="""1397""", year="1971", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:18 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 40,
    label = "r00009426",
    reactant1 = 
"""
1  *6 C     0 {2,S} {3,S} {9,S}
2  *2 C     0 {1,S} {5,S}
3     C     0 {1,S} {4,S}
4     C     0 {3,S} {6,S}
5  *1 C     0 {2,S} {8,S}
6     C     0 {4,S} {7,S}
7     C     0 {6,S} {9,S}
8  *3 C     0 {5,S} {10,S}
9  *5 C     0 {1,S} {7,S} {10,D}
10 *4 C     0 {8,S} {9,D}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S} {6,S}
5  *5 C     0 {3,S} {6,D} {7,S}
6  *6 C     0 {4,S} {5,D}
7  *4 C     0 {5,S} {8,D}
8  *3 C     0 {7,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.17e+13,"s^-1"),
        n = 0,
        Ea = (239457,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Ondruschka, B.", "Zimmermann, G."], title=u'Pyrolysis kinetics of octalins', journal="J. Prakt. Chem.", volume="332", pages="""547""", year="1990", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:25 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 41,
    label = "r00009910",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {7,S}
4  *6 C     0 {2,S} {8,S}
5     C     0 {7,S}
6     C     0 {8,S}
7  *4 C     0 {3,S} {5,S} {8,D}
8  *5 C     0 {4,S} {6,S} {7,D}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1     C     0 {3,S}
2     C     0 {4,S}
3  *5 C     0 {1,S} {4,S} {5,D}
4  *4 C     0 {2,S} {3,S} {6,D}
5  *6 C     0 {3,D}
6  *3 C     0 {4,D}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (3.2e+15,"s^-1"),
        n = 0,
        Ea = (292669,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Robaugh, D.", "Tsang, W."], title=u'Thermal decomposition of phenyl iodide and o-iodotoluene', journal="J. Phys. Chem.", volume="90", pages="""5363""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:29 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 42,
    label = "r00015550",
    reactant1 = 
"""
1     C     0 {2,S} {4,S} {7,S}
2  *3 C     0 {1,S} {6,S} {9,S}
3  *6 C     0 {4,S} {5,S} {8,S}
4     C     0 {1,S} {3,S}
5  *2 C     0 {3,S} {6,S}
6  *1 C     0 {2,S} {5,S}
7     C     0 {1,S}
8  *5 C     0 {3,S} {9,D}
9  *4 C     0 {2,S} {8,D}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4  *3 C     0 {1,S} {6,D}
5  *6 C     0 {2,S} {7,D}
6  *4 C     0 {4,D} {7,S}
7  *5 C     0 {5,D} {6,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.2e+14,"s^-1"),
        n = 0,
        Ea = (233637,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Huybrechts, G.", "Ngoy, G."], title=u'Kinetics of the Pyrolysis of Endo- and Exo-5-Methylbicyclo[2.2.2]oct-2-ene in the Gas Phase', journal="Int. J. Chem. Kinet.", volume="8", pages="""775""", year="1975", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:23 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 43,
    label = "r00015550",
    reactant1 = 
"""
1     C     0 {2,S} {4,S} {7,S}
2  *3 C     0 {1,S} {6,S} {9,S}
3  *6 C     0 {4,S} {5,S} {8,S}
4     C     0 {1,S} {3,S}
5  *2 C     0 {3,S} {6,S}
6  *1 C     0 {2,S} {5,S}
7     C     0 {1,S}
8  *5 C     0 {3,S} {9,D}
9  *4 C     0 {2,S} {8,D}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4  *3 C     0 {1,S} {6,D}
5  *6 C     0 {2,S} {7,D}
6  *4 C     0 {4,D} {7,S}
7  *5 C     0 {5,D} {6,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.17e+14,"s^-1"),
        n = 0,
        Ea = (241951,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["van Mele, B.", "Boon, G.", "Huybrechts, G."], title=u'Gas phase kinetic and thermochemical data for endo- and exo-5-monosubstituted bicyclo[2.2.2]oct-2-enes', journal="Int. J. Chem. Kinet.", volume="18", pages="""537""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:23 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 44,
    label = "r00015551",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S} {7,S}
2  *3 C     0 {1,S} {6,S} {9,S}
3  *6 C     0 {4,S} {5,S} {8,S}
4  *2 C     0 {1,S} {3,S}
5     C     0 {3,S} {6,S}
6     C     0 {2,S} {5,S}
7     C     0 {1,S}
8  *5 C     0 {3,S} {9,D}
9  *4 C     0 {2,S} {8,D}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,D}
4  *6 C     0 {2,S} {6,D}
5  *4 C     0 {3,D} {6,S}
6  *5 C     0 {4,D} {5,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.74e+14,"s^-1"),
        n = 0,
        Ea = (234468,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Huybrechts, G.", "Ngoy, G."], title=u'Kinetics of the Pyrolysis of Endo- and Exo-5-Methylbicyclo[2.2.2]oct-2-ene in the Gas Phase', journal="Int. J. Chem. Kinet.", volume="8", pages="""775""", year="1975", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:23 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 45,
    label = "r00015551",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S} {7,S}
2  *3 C     0 {1,S} {6,S} {9,S}
3  *6 C     0 {4,S} {5,S} {8,S}
4  *2 C     0 {1,S} {3,S}
5     C     0 {3,S} {6,S}
6     C     0 {2,S} {5,S}
7     C     0 {1,S}
8  *5 C     0 {3,S} {9,D}
9  *4 C     0 {2,S} {8,D}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,D}
4  *6 C     0 {2,S} {6,D}
5  *4 C     0 {3,D} {6,S}
6  *5 C     0 {4,D} {5,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.15e+15,"s^-1"),
        n = 0,
        Ea = (243614,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["van Mele, B.", "Boon, G.", "Huybrechts, G."], title=u'Gas phase kinetic and thermochemical data for endo- and exo-5-monosubstituted bicyclo[2.2.2]oct-2-enes', journal="Int. J. Chem. Kinet.", volume="18", pages="""537""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:23 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 46,
    label = "r00015551",
    reactant1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,D}
4  *6 C     0 {2,S} {6,D}
5  *4 C     0 {3,D} {6,S}
6  *5 C     0 {4,D} {5,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {4,S} {7,S}
2  *3 C     0 {1,S} {5,S} {8,S}
3  *6 C     0 {4,S} {6,S} {9,S}
4  *2 C     0 {1,S} {3,S}
5     C     0 {2,S} {6,S}
6     C     0 {3,S} {5,S}
7     C     0 {1,S}
8  *4 C     0 {2,S} {9,D}
9  *5 C     0 {3,S} {8,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (5.5e+08,"cm^3/(mol*s)"),
        n = 0,
        Ea = (108920,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Debande, G.", "Huybrechts, G."], title=u'Kinetics of the Addition of Propene to Cyclohexa-1,3-Diene in the Gas Phase', journal="Int. J. Chem. Kinet.", volume="6", pages="""545""", year="1974", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:23 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 47,
    label = "r00015551",
    reactant1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,D}
4  *6 C     0 {2,S} {6,D}
5  *4 C     0 {3,D} {6,S}
6  *5 C     0 {4,D} {5,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {4,S} {7,S}
2  *3 C     0 {1,S} {5,S} {8,S}
3  *6 C     0 {4,S} {6,S} {9,S}
4  *2 C     0 {1,S} {3,S}
5     C     0 {2,S} {6,S}
6     C     0 {3,S} {5,S}
7     C     0 {1,S}
8  *4 C     0 {2,S} {9,D}
9  *5 C     0 {3,S} {8,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.12e+09,"cm^3/(mol*s)"),
        n = 0,
        Ea = (111414,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Huybrechts, G.", "Poppelsdorf, H.", "Maesschalck, L.", "Van Mele, B."], title=u'Kinetics, mechanism, and endo selectivity of diels-alder reactions of alkylmonosubstituted ethenes with cyclohexa-1,3-diene in the gas phase', journal="Int. J. Chem. Kinet.", volume="16", pages="""93""", year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:23 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 48,
    label = "r00015563",
    reactant1 = 
"""
1     C     0 {2,S} {4,S} {7,S}
2  *3 C     0 {1,S} {6,S} {9,S}
3  *6 C     0 {4,S} {5,S} {8,S}
4     C     0 {1,S} {3,S}
5  *2 C     0 {3,S} {6,S}
6  *1 C     0 {2,S} {5,S}
7     C     0 {1,S}
8  *5 C     0 {3,S} {9,D}
9  *4 C     0 {2,S} {8,D}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4  *3 C     0 {1,S} {6,D}
5  *6 C     0 {2,S} {7,D}
6  *4 C     0 {4,D} {7,S}
7  *5 C     0 {5,D} {6,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.2e+15,"s^-1"),
        n = 0,
        Ea = (247771,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Huybrechts, G.", "Ngoy, G."], title=u'Kinetics of the Pyrolysis of Endo- and Exo-5-Methylbicyclo[2.2.2]oct-2-ene in the Gas Phase', journal="Int. J. Chem. Kinet.", volume="8", pages="""775""", year="1975", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:24 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 49,
    label = "r00015563",
    reactant1 = 
"""
1     C     0 {2,S} {4,S} {7,S}
2  *3 C     0 {1,S} {6,S} {9,S}
3  *6 C     0 {4,S} {5,S} {8,S}
4     C     0 {1,S} {3,S}
5  *2 C     0 {3,S} {6,S}
6  *1 C     0 {2,S} {5,S}
7     C     0 {1,S}
8  *5 C     0 {3,S} {9,D}
9  *4 C     0 {2,S} {8,D}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4  *3 C     0 {1,S} {6,D}
5  *6 C     0 {2,S} {7,D}
6  *4 C     0 {4,D} {7,S}
7  *5 C     0 {5,D} {6,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.32e+15,"s^-1"),
        n = 0,
        Ea = (247771,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["van Mele, B.", "Boon, G.", "Huybrechts, G."], title=u'Gas phase kinetic and thermochemical data for endo- and exo-5-monosubstituted bicyclo[2.2.2]oct-2-enes', journal="Int. J. Chem. Kinet.", volume="18", pages="""537""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:24 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 50,
    label = "r00015564",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S} {7,S}
2  *3 C     0 {1,S} {6,S} {9,S}
3  *6 C     0 {4,S} {5,S} {8,S}
4  *2 C     0 {1,S} {3,S}
5     C     0 {3,S} {6,S}
6     C     0 {2,S} {5,S}
7     C     0 {1,S}
8  *5 C     0 {3,S} {9,D}
9  *4 C     0 {2,S} {8,D}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,D}
4  *6 C     0 {2,S} {6,D}
5  *4 C     0 {3,D} {6,S}
6  *5 C     0 {4,D} {5,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.37e+14,"s^-1"),
        n = 0,
        Ea = (243614,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Huybrechts, G.", "Ngoy, G."], title=u'Kinetics of the Pyrolysis of Endo- and Exo-5-Methylbicyclo[2.2.2]oct-2-ene in the Gas Phase', journal="Int. J. Chem. Kinet.", volume="8", pages="""775""", year="1975", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:24 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 51,
    label = "r00015564",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S} {7,S}
2  *3 C     0 {1,S} {6,S} {9,S}
3  *6 C     0 {4,S} {5,S} {8,S}
4  *2 C     0 {1,S} {3,S}
5     C     0 {3,S} {6,S}
6     C     0 {2,S} {5,S}
7     C     0 {1,S}
8  *5 C     0 {3,S} {9,D}
9  *4 C     0 {2,S} {8,D}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,D}
4  *6 C     0 {2,S} {6,D}
5  *4 C     0 {3,D} {6,S}
6  *5 C     0 {4,D} {5,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.15e+15,"s^-1"),
        n = 0,
        Ea = (247771,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["van Mele, B.", "Boon, G.", "Huybrechts, G."], title=u'Gas phase kinetic and thermochemical data for endo- and exo-5-monosubstituted bicyclo[2.2.2]oct-2-enes', journal="Int. J. Chem. Kinet.", volume="18", pages="""537""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:24 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 52,
    label = "r00015564",
    reactant1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,D}
4  *6 C     0 {2,S} {6,D}
5  *4 C     0 {3,D} {6,S}
6  *5 C     0 {4,D} {5,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {4,S} {7,S}
2  *3 C     0 {1,S} {5,S} {8,S}
3  *6 C     0 {4,S} {6,S} {9,S}
4  *2 C     0 {1,S} {3,S}
5     C     0 {2,S} {6,S}
6     C     0 {3,S} {5,S}
7     C     0 {1,S}
8  *4 C     0 {2,S} {9,D}
9  *5 C     0 {3,S} {8,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (4.57e+09,"cm^3/(mol*s)"),
        n = 0,
        Ea = (125549,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Debande, G.", "Huybrechts, G."], title=u'Kinetics of the Addition of Propene to Cyclohexa-1,3-Diene in the Gas Phase', journal="Int. J. Chem. Kinet.", volume="6", pages="""545""", year="1974", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:24 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 53,
    label = "r00015564",
    reactant1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,D}
4  *6 C     0 {2,S} {6,D}
5  *4 C     0 {3,D} {6,S}
6  *5 C     0 {4,D} {5,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {4,S} {7,S}
2  *3 C     0 {1,S} {5,S} {8,S}
3  *6 C     0 {4,S} {6,S} {9,S}
4  *2 C     0 {1,S} {3,S}
5     C     0 {2,S} {6,S}
6     C     0 {3,S} {5,S}
7     C     0 {1,S}
8  *4 C     0 {2,S} {9,D}
9  *5 C     0 {3,S} {8,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.09e+09,"cm^3/(mol*s)"),
        n = 0,
        Ea = (120560,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Huybrechts, G.", "Poppelsdorf, H.", "Maesschalck, L.", "Van Mele, B."], title=u'Kinetics, mechanism, and endo selectivity of diels-alder reactions of alkylmonosubstituted ethenes with cyclohexa-1,3-diene in the gas phase', journal="Int. J. Chem. Kinet.", volume="16", pages="""93""", year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:24 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 54,
    label = "r00016017",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S} {9,S}
2  *3 C     0 {1,S} {6,S} {8,S}
3  *6 C     0 {4,S} {5,S} {7,S}
4  *2 C     0 {1,S} {3,S}
5     C     0 {3,S} {6,S}
6     C     0 {2,S} {5,S}
7  *5 C     0 {3,S} {8,D}
8  *4 C     0 {2,S} {7,D}
9     C     0 {1,S} {10,D}
10    C     0 {9,D}
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
1     C     0 {2,S} {4,S}
2     C     0 {1,S} {3,S}
3  *3 C     0 {2,S} {6,D}
4  *6 C     0 {1,S} {5,D}
5  *5 C     0 {4,D} {6,S}
6  *4 C     0 {3,D} {5,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.88e+14,"s^-1"),
        n = 0,
        Ea = (215345,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Huybrechts, G.", "Hubin, Y.", "Narmon, M.", "Van Mele, B."], title=u'Kinetics of the Thermal Reactions of Bicyclo[4.2.2]deca-3,7-diene and endo- and exo-5-Vinylbicyclo[2.2.2]oct-2-ene in the Gas Phase', journal="Int. J. Chem. Kinet.", volume="14", pages="""251""", year="1982", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 55,
    label = "r00016017",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3  *2 C     0 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,D}
4  *6 C     0 {2,S} {6,D}
5  *4 C     0 {3,D} {6,S}
6  *5 C     0 {4,D} {5,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {4,S} {9,S}
2  *3 C     0 {1,S} {5,S} {7,S}
3  *6 C     0 {4,S} {6,S} {8,S}
4  *2 C     0 {1,S} {3,S}
5     C     0 {2,S} {6,S}
6     C     0 {3,S} {5,S}
7  *4 C     0 {2,S} {8,D}
8  *5 C     0 {3,S} {7,D}
9     C     0 {1,S} {10,D}
10    C     0 {9,D}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (3.8e+09,"cm^3/(mol*s)"),
        n = 0,
        Ea = (103931,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Huybrechts, G.", "Hubin, Y.", "Narmon, M.", "Van Mele, B."], title=u'Kinetics and Mechanism of the Addition of 1,3-Butadiene to Cyclohexa-1,3-diene in the Gas Phase', journal="Int. J. Chem. Kinet.", volume="14", pages="""259""", year="1982", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 56,
    label = "r00016021",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S} {9,S}
2  *3 C     0 {1,S} {6,S} {8,S}
3  *6 C     0 {4,S} {5,S} {7,S}
4  *2 C     0 {1,S} {3,S}
5     C     0 {3,S} {6,S}
6     C     0 {2,S} {5,S}
7  *5 C     0 {3,S} {8,D}
8  *4 C     0 {2,S} {7,D}
9     C     0 {1,S} {10,D}
10    C     0 {9,D}
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
1     C     0 {2,S} {4,S}
2     C     0 {1,S} {3,S}
3  *3 C     0 {2,S} {6,D}
4  *6 C     0 {1,S} {5,D}
5  *5 C     0 {4,D} {6,S}
6  *4 C     0 {3,D} {5,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.91e+14,"s^-1"),
        n = 0,
        Ea = (221996,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Huybrechts, G.", "Hubin, Y.", "Narmon, M.", "Van Mele, B."], title=u'Kinetics of the Thermal Reactions of Bicyclo[4.2.2]deca-3,7-diene and endo- and exo-5-Vinylbicyclo[2.2.2]oct-2-ene in the Gas Phase', journal="Int. J. Chem. Kinet.", volume="14", pages="""251""", year="1982", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 57,
    label = "r00016021",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3  *2 C     0 {1,D}
4     C     0 {2,D}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,D}
4  *6 C     0 {2,S} {6,D}
5  *4 C     0 {3,D} {6,S}
6  *5 C     0 {4,D} {5,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {4,S} {9,S}
2  *3 C     0 {1,S} {5,S} {7,S}
3  *6 C     0 {4,S} {6,S} {8,S}
4  *2 C     0 {1,S} {3,S}
5     C     0 {2,S} {6,S}
6     C     0 {3,S} {5,S}
7  *4 C     0 {2,S} {8,D}
8  *5 C     0 {3,S} {7,D}
9     C     0 {1,S} {10,D}
10    C     0 {9,D}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.15e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (112245,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Huybrechts, G.", "Hubin, Y.", "Narmon, M.", "Van Mele, B."], title=u'Kinetics and Mechanism of the Addition of 1,3-Butadiene to Cyclohexa-1,3-diene in the Gas Phase', journal="Int. J. Chem. Kinet.", volume="14", pages="""259""", year="1982", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:34 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 58,
    label = "r00016478",
    reactant1 = 
"""
1  *3 C     0 {3,S} {6,S} {8,S}
2  *6 C     0 {4,S} {5,S} {7,S}
3  *1 C     0 {1,S} {4,S} {9,S}
4  *2 C     0 {2,S} {3,S}
5     C     0 {2,S} {6,S}
6     C     0 {1,S} {5,S}
7  *5 C     0 {2,S} {8,D}
8  *4 C     0 {1,S} {7,D}
9     C     0 {3,S} {10,D}
10    O     0 {9,D}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3  *2 C     0 {1,D}
4     O     0 {2,D}
""",
    product2 = 
"""
1     C     0 {2,S} {4,S}
2     C     0 {1,S} {3,S}
3  *3 C     0 {2,S} {6,D}
4  *6 C     0 {1,S} {5,D}
5  *5 C     0 {4,D} {6,S}
6  *4 C     0 {3,D} {5,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (9.55e+12,"s^-1"),
        n = 0,
        Ea = (193727,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Huybrechts, G.", "Paternoster, G.", "Baetens, P."], title=u'Kinetics of the Diels-Alder Addition of Acrolein to Cyclohexa-1,3-diene and Its Reverse Reaction in the Gas Phase', journal="Int. J. Chem. Kinet.", volume="8", pages="""641""", year="1976", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 59,
    label = "r00016478",
    reactant1 = 
"""
1  *1 C     0 {2,D} {3,S}
2  *2 C     0 {1,D}
3     C     0 {1,S} {4,D}
4     O     0 {3,D}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,D}
4  *6 C     0 {2,S} {6,D}
5  *4 C     0 {3,D} {6,S}
6  *5 C     0 {4,D} {5,S}
""",
    product1 = 
"""
1  *3 C     0 {2,S} {5,S} {7,S}
2  *1 C     0 {1,S} {4,S} {9,S}
3  *6 C     0 {4,S} {6,S} {8,S}
4  *2 C     0 {2,S} {3,S}
5     C     0 {1,S} {6,S}
6     C     0 {3,S} {5,S}
7  *4 C     0 {1,S} {8,D}
8  *5 C     0 {3,S} {7,D}
9     C     0 {2,S} {10,D}
10    O     0 {9,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (4.47e+08,"cm^3/(mol*s)"),
        n = 0,
        Ea = (81481.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Huybrechts, G.", "Paternoster, G.", "Baetens, P."], title=u'Kinetics of the Diels-Alder Addition of Acrolein to Cyclohexa-1,3-diene and Its Reverse Reaction in the Gas Phase', journal="Int. J. Chem. Kinet.", volume="8", pages="""641""", year="1976", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 60,
    label = "r00016478",
    reactant1 = 
"""
1  *1 C     0 {2,D} {3,S}
2  *2 C     0 {1,D}
3     C     0 {1,S} {4,D}
4     O     0 {3,D}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,D}
4  *6 C     0 {2,S} {6,D}
5  *4 C     0 {3,D} {6,S}
6  *5 C     0 {4,D} {5,S}
""",
    product1 = 
"""
1  *3 C     0 {2,S} {5,S} {7,S}
2  *1 C     0 {1,S} {4,S} {9,S}
3  *6 C     0 {4,S} {6,S} {8,S}
4  *2 C     0 {2,S} {3,S}
5     C     0 {1,S} {6,S}
6     C     0 {3,S} {5,S}
7  *4 C     0 {1,S} {8,D}
8  *5 C     0 {3,S} {7,D}
9     C     0 {2,S} {10,D}
10    O     0 {9,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (6.03e+08,"cm^3/(mol*s)"),
        n = 0,
        Ea = (87302,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Van Mele, B.", "Tybaert, C.", "Huybrechts, G."], title=u'Kinetics, mechanism, and stereochemistry of Diels-Alder reactions of carbonyl-substituted ethenes with cyclohexa-1,3-diene in the gas phase', journal="Int. J. Chem. Kinet.", volume="19", pages="""1063""", year="1987", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:47 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 61,
    label = "r00016991",
    reactant1 = 
"""
1     C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {8,S} {9,S}
3  *3 C     0 {1,S} {7,S} {11,S}
4  *6 C     0 {5,S} {6,S} {10,S}
5     C     0 {1,S} {4,S}
6  *2 C     0 {4,S} {7,S}
7  *1 C     0 {3,S} {6,S}
8     C     0 {2,S}
9     C     0 {2,S}
10 *5 C     0 {4,S} {11,D}
11 *4 C     0 {3,S} {10,D}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S} {6,S}
3     C     0 {2,S} {7,S}
4     C     0 {1,S}
5     C     0 {1,S}
6  *3 C     0 {2,S} {8,D}
7  *6 C     0 {3,S} {9,D}
8  *4 C     0 {6,D} {9,S}
9  *5 C     0 {7,D} {8,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.35e+15,"s^-1"),
        n = 0,
        Ea = (241951,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["van Mele, B.", "Boon, G.", "Huybrechts, G."], title=u'Gas phase kinetic and thermochemical data for endo- and exo-5-monosubstituted bicyclo[2.2.2]oct-2-enes', journal="Int. J. Chem. Kinet.", volume="18", pages="""537""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:36:08 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 62,
    label = "r00016992",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {8,S} {9,S}
3  *3 C     0 {1,S} {7,S} {11,S}
4  *6 C     0 {5,S} {6,S} {10,S}
5  *2 C     0 {1,S} {4,S}
6     C     0 {4,S} {7,S}
7     C     0 {3,S} {6,S}
8     C     0 {2,S}
9     C     0 {2,S}
10 *5 C     0 {4,S} {11,D}
11 *4 C     0 {3,S} {10,D}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *1 C     0 {1,S} {5,D}
5  *2 C     0 {4,D}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,D}
4  *6 C     0 {2,S} {6,D}
5  *4 C     0 {3,D} {6,S}
6  *5 C     0 {4,D} {5,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.1e+15,"s^-1"),
        n = 0,
        Ea = (240288,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["van Mele, B.", "Boon, G.", "Huybrechts, G."], title=u'Gas phase kinetic and thermochemical data for endo- and exo-5-monosubstituted bicyclo[2.2.2]oct-2-enes', journal="Int. J. Chem. Kinet.", volume="18", pages="""537""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:36:09 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 63,
    label = "r00016992",
    reactant1 = 
"""
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *1 C     0 {1,S} {5,D}
5  *2 C     0 {4,D}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,D}
4  *6 C     0 {2,S} {6,D}
5  *4 C     0 {3,D} {6,S}
6  *5 C     0 {4,D} {5,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {8,S} {9,S}
3  *3 C     0 {1,S} {6,S} {10,S}
4  *6 C     0 {5,S} {7,S} {11,S}
5  *2 C     0 {1,S} {4,S}
6     C     0 {3,S} {7,S}
7     C     0 {4,S} {6,S}
8     C     0 {2,S}
9     C     0 {2,S}
10 *4 C     0 {3,S} {11,D}
11 *5 C     0 {4,S} {10,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.72e+08,"cm^3/(mol*s)"),
        n = 0,
        Ea = (111414,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Huybrechts, G.", "Poppelsdorf, H.", "Maesschalck, L.", "Van Mele, B."], title=u'Kinetics, mechanism, and endo selectivity of diels-alder reactions of alkylmonosubstituted ethenes with cyclohexa-1,3-diene in the gas phase', journal="Int. J. Chem. Kinet.", volume="16", pages="""93""", year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:36:09 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 64,
    label = "r00016994",
    reactant1 = 
"""
1     C     0 {2,S} {4,S} {7,S}
2  *3 C     0 {1,S} {6,S} {10,S}
3  *6 C     0 {4,S} {5,S} {9,S}
4     C     0 {1,S} {3,S}
5  *2 C     0 {3,S} {6,S}
6  *1 C     0 {2,S} {5,S}
7     C     0 {1,S} {8,S}
8     C     0 {7,S}
9  *5 C     0 {3,S} {10,D}
10 *4 C     0 {2,S} {9,D}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {6,S}
4     C     0 {2,S}
5  *3 C     0 {1,S} {7,D}
6  *6 C     0 {3,S} {8,D}
7  *4 C     0 {5,D} {8,S}
8  *5 C     0 {6,D} {7,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.71e+14,"s^-1"),
        n = 0,
        Ea = (241120,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["van Mele, B.", "Boon, G.", "Huybrechts, G."], title=u'Gas phase kinetic and thermochemical data for endo- and exo-5-monosubstituted bicyclo[2.2.2]oct-2-enes', journal="Int. J. Chem. Kinet.", volume="18", pages="""537""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:36:09 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 65,
    label = "r00016995",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S} {7,S}
2  *3 C     0 {1,S} {6,S} {10,S}
3  *6 C     0 {4,S} {5,S} {9,S}
4  *2 C     0 {1,S} {3,S}
5     C     0 {3,S} {6,S}
6     C     0 {2,S} {5,S}
7     C     0 {1,S} {8,S}
8     C     0 {7,S}
9  *5 C     0 {3,S} {10,D}
10 *4 C     0 {2,S} {9,D}
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
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,D}
4  *6 C     0 {2,S} {6,D}
5  *4 C     0 {3,D} {6,S}
6  *5 C     0 {4,D} {5,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.66e+15,"s^-1"),
        n = 0,
        Ea = (244445,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["van Mele, B.", "Boon, G.", "Huybrechts, G."], title=u'Gas phase kinetic and thermochemical data for endo- and exo-5-monosubstituted bicyclo[2.2.2]oct-2-enes', journal="Int. J. Chem. Kinet.", volume="18", pages="""537""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:36:09 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 66,
    label = "r00016995",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *1 C     0 {1,S} {4,D}
4  *2 C     0 {3,D}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,D}
4  *6 C     0 {2,S} {6,D}
5  *4 C     0 {3,D} {6,S}
6  *5 C     0 {4,D} {5,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {4,S} {7,S}
2  *3 C     0 {1,S} {5,S} {9,S}
3  *6 C     0 {4,S} {6,S} {10,S}
4  *2 C     0 {1,S} {3,S}
5     C     0 {2,S} {6,S}
6     C     0 {3,S} {5,S}
7     C     0 {1,S} {8,S}
8     C     0 {7,S}
9  *4 C     0 {2,S} {10,D}
10 *5 C     0 {3,S} {9,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (7.08e+08,"cm^3/(mol*s)"),
        n = 0,
        Ea = (109751,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Huybrechts, G.", "Poppelsdorf, H.", "Maesschalck, L.", "Van Mele, B."], title=u'Kinetics, mechanism, and endo selectivity of diels-alder reactions of alkylmonosubstituted ethenes with cyclohexa-1,3-diene in the gas phase', journal="Int. J. Chem. Kinet.", volume="16", pages="""93""", year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:36:09 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 67,
    label = "r00016996",
    reactant1 = 
"""
1     C     0 {2,S} {4,S} {7,S}
2  *3 C     0 {1,S} {6,S} {10,S}
3  *6 C     0 {4,S} {5,S} {9,S}
4     C     0 {1,S} {3,S}
5  *2 C     0 {3,S} {6,S}
6  *1 C     0 {2,S} {5,S}
7     C     0 {1,S} {8,S}
8     C     0 {7,S}
9  *5 C     0 {3,S} {10,D}
10 *4 C     0 {2,S} {9,D}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {6,S}
4     C     0 {2,S}
5  *3 C     0 {1,S} {7,D}
6  *6 C     0 {3,S} {8,D}
7  *4 C     0 {5,D} {8,S}
8  *5 C     0 {6,D} {7,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.88e+15,"s^-1"),
        n = 0,
        Ea = (250266,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["van Mele, B.", "Boon, G.", "Huybrechts, G."], title=u'Gas phase kinetic and thermochemical data for endo- and exo-5-monosubstituted bicyclo[2.2.2]oct-2-enes', journal="Int. J. Chem. Kinet.", volume="18", pages="""537""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:36:09 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 68,
    label = "r00016997",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S} {7,S}
2  *3 C     0 {1,S} {6,S} {10,S}
3  *6 C     0 {4,S} {5,S} {9,S}
4  *2 C     0 {1,S} {3,S}
5     C     0 {3,S} {6,S}
6     C     0 {2,S} {5,S}
7     C     0 {1,S} {8,S}
8     C     0 {7,S}
9  *5 C     0 {3,S} {10,D}
10 *4 C     0 {2,S} {9,D}
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
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,D}
4  *6 C     0 {2,S} {6,D}
5  *4 C     0 {3,D} {6,S}
6  *5 C     0 {4,D} {5,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.29e+15,"s^-1"),
        n = 0,
        Ea = (246940,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["van Mele, B.", "Boon, G.", "Huybrechts, G."], title=u'Gas phase kinetic and thermochemical data for endo- and exo-5-monosubstituted bicyclo[2.2.2]oct-2-enes', journal="Int. J. Chem. Kinet.", volume="18", pages="""537""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:36:10 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 69,
    label = "r00016997",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *1 C     0 {1,S} {4,D}
4  *2 C     0 {3,D}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,D}
4  *6 C     0 {2,S} {6,D}
5  *4 C     0 {3,D} {6,S}
6  *5 C     0 {4,D} {5,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {4,S} {7,S}
2  *3 C     0 {1,S} {5,S} {9,S}
3  *6 C     0 {4,S} {6,S} {10,S}
4  *2 C     0 {1,S} {3,S}
5     C     0 {2,S} {6,S}
6     C     0 {3,S} {5,S}
7     C     0 {1,S} {8,S}
8     C     0 {7,S}
9  *4 C     0 {2,S} {10,D}
10 *5 C     0 {3,S} {9,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.17e+09,"cm^3/(mol*s)"),
        n = 0,
        Ea = (119728,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Huybrechts, G.", "Poppelsdorf, H.", "Maesschalck, L.", "Van Mele, B."], title=u'Kinetics, mechanism, and endo selectivity of diels-alder reactions of alkylmonosubstituted ethenes with cyclohexa-1,3-diene in the gas phase', journal="Int. J. Chem. Kinet.", volume="16", pages="""93""", year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:36:10 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 70,
    label = "r00016998",
    reactant1 = 
"""
1     C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {8,S} {9,S}
3  *3 C     0 {1,S} {7,S} {11,S}
4  *6 C     0 {5,S} {6,S} {10,S}
5     C     0 {1,S} {4,S}
6  *2 C     0 {4,S} {7,S}
7  *1 C     0 {3,S} {6,S}
8     C     0 {2,S}
9     C     0 {2,S}
10 *5 C     0 {4,S} {11,D}
11 *4 C     0 {3,S} {10,D}
""",
    product1 = 
"""
1  *2 C     0 {2,D}
2  *1 C     0 {1,D}
""",
    product2 = 
"""
1     C     0 {2,S} {4,S} {5,S}
2     C     0 {1,S} {3,S} {6,S}
3     C     0 {2,S} {7,S}
4     C     0 {1,S}
5     C     0 {1,S}
6  *3 C     0 {2,S} {8,D}
7  *6 C     0 {3,S} {9,D}
8  *4 C     0 {6,D} {9,S}
9  *5 C     0 {7,D} {8,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.76e+14,"s^-1"),
        n = 0,
        Ea = (246940,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["van Mele, B.", "Boon, G.", "Huybrechts, G."], title=u'Gas phase kinetic and thermochemical data for endo- and exo-5-monosubstituted bicyclo[2.2.2]oct-2-enes', journal="Int. J. Chem. Kinet.", volume="18", pages="""537""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:36:10 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 71,
    label = "r00016999",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {8,S} {9,S}
3  *3 C     0 {1,S} {7,S} {11,S}
4  *6 C     0 {5,S} {6,S} {10,S}
5  *2 C     0 {1,S} {4,S}
6     C     0 {4,S} {7,S}
7     C     0 {3,S} {6,S}
8     C     0 {2,S}
9     C     0 {2,S}
10 *5 C     0 {4,S} {11,D}
11 *4 C     0 {3,S} {10,D}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *1 C     0 {1,S} {5,D}
5  *2 C     0 {4,D}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,D}
4  *6 C     0 {2,S} {6,D}
5  *4 C     0 {3,D} {6,S}
6  *5 C     0 {4,D} {5,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.05e+15,"s^-1"),
        n = 0,
        Ea = (247771,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["van Mele, B.", "Boon, G.", "Huybrechts, G."], title=u'Gas phase kinetic and thermochemical data for endo- and exo-5-monosubstituted bicyclo[2.2.2]oct-2-enes', journal="Int. J. Chem. Kinet.", volume="18", pages="""537""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:36:10 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 72,
    label = "r00016999",
    reactant1 = 
"""
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *1 C     0 {1,S} {5,D}
5  *2 C     0 {4,D}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {5,D}
4  *6 C     0 {2,S} {6,D}
5  *4 C     0 {3,D} {6,S}
6  *5 C     0 {4,D} {5,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {8,S} {9,S}
3  *3 C     0 {1,S} {6,S} {10,S}
4  *6 C     0 {5,S} {7,S} {11,S}
5  *2 C     0 {1,S} {4,S}
6     C     0 {3,S} {7,S}
7     C     0 {4,S} {6,S}
8     C     0 {2,S}
9     C     0 {2,S}
10 *4 C     0 {3,S} {11,D}
11 *5 C     0 {4,S} {10,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.95e+08,"cm^3/(mol*s)"),
        n = 0,
        Ea = (118897,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Huybrechts, G.", "Poppelsdorf, H.", "Maesschalck, L.", "Van Mele, B."], title=u'Kinetics, mechanism, and endo selectivity of diels-alder reactions of alkylmonosubstituted ethenes with cyclohexa-1,3-diene in the gas phase', journal="Int. J. Chem. Kinet.", volume="16", pages="""93""", year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:36:10 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

