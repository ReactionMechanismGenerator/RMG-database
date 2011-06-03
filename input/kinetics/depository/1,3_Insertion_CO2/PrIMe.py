#!/usr/bin/env python
# encoding: utf-8

name = "1,3_Insertion_CO2"
shortDesc = ""
longDesc = """

"""

entry(
    index = 1,
    label = "r00001636",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,D} {4,S}
2  *1 O     0 {1,S} {5,S}
3     O     0 {1,D}
4  *4 H     0 {1,S}
5  *3 H     0 {2,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D} {3,D}
2  *1 O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
1  *3 H     0 {2,S}
2  *4 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (63100,"s^-1"),
        n = 0,
        Ea = (128043,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Blake, P.G.", "Hinshelwood, C."], title=u'The homogeneous decomposition reactions of gaseous formic acid', journal="Proc. R. Soc. London A", volume="255", pages="""444-455""", year="1960", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 2,
    label = "r00001636",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,D} {4,S}
2  *1 O     0 {1,S} {5,S}
3     O     0 {1,D}
4  *4 H     0 {1,S}
5  *3 H     0 {2,S}
""",
    product1 = 
"""
1  *2 C     0 {2,D} {3,D}
2  *1 O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
1  *3 H     0 {2,S}
2  *4 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.95e+09,"s^-1"),
        n = 0,
        Ea = (202873,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Blake, P.G.", "Davies, H.H.", "Jackson, G.E."], title=u'Dehydration Mechanisms in the Thermal Decomposition of Gaseous Formic Acid', journal="J. Chem. Soc. B", volume="10", pages="""1923""", year="1971", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 3,
    label = "r00001645",
    reactant1 = 
"""
1  *3 C     0 {2,S}
2  *1 C     0 {1,S} {3,S} {4,D}
3  *2 O     0 {2,S} {5,S}
4     O     0 {2,D}
5  *4 H     0 {3,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,D}
2  *2 O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
1  *3 C     0 {2,S}
2  *4 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+11,"s^-1"),
        n = 0,
        Ea = (259412,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Bamford, C.H.", "Dewar, M.J.S."], title=u'608. The thermal decomposition of acetic acid', journal="J. Chem. Soc.", pages="""2877-2882""", year="1949", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 4,
    label = "r00001645",
    reactant1 = 
"""
1  *3 C     0 {2,S}
2  *1 C     0 {1,S} {3,S} {4,D}
3  *2 O     0 {2,S} {5,S}
4     O     0 {2,D}
5  *4 H     0 {3,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,D}
2  *2 O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
1  *3 C     0 {2,S}
2  *4 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.32e+11,"s^-1"),
        n = 0,
        Ea = (244445,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Blake, P.G.", "Jackson, G.E."], title=u'The thermal decomposition of acetic acid', journal="J. Chem. Soc. B", pages="""1153-1155""", year="1968", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 5,
    label = "r00001645",
    reactant1 = 
"""
1  *3 C     0 {2,S}
2  *1 C     0 {1,S} {3,S} {4,D}
3  *2 O     0 {2,S} {5,S}
4     O     0 {2,D}
5  *4 H     0 {3,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,D}
2  *2 O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
1  *3 C     0 {2,S}
2  *4 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.89e+13,"s^-1"),
        n = 0,
        Ea = (291838,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Blake, P.G.", "Jackson, G.E."], title=u'High- and low-temperature mechanisms in the thermal decomposition of acetic acid', journal="J. Chem. Soc. B", pages="""94-96""", year="1969", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 6,
    label = "r00001645",
    reactant1 = 
"""
1  *3 C     0 {2,S}
2  *1 C     0 {1,S} {3,S} {4,D}
3  *2 O     0 {2,S} {5,S}
4     O     0 {2,D}
5  *4 H     0 {3,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,D}
2  *2 O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
1  *3 C     0 {2,S}
2  *4 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.26e+13,"s^-1"),
        n = 0,
        Ea = (304310,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Mackie, J.C.", "Doolan, K.R."], title=u'High-temperature kinetics of thermal decomposition of acetic acid and its products', journal="Int. J. Chem. Kinet.", volume="16", pages="""525""", year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 7,
    label = "r00001645",
    reactant1 = 
"""
1  *3 C     0 {2,S}
2  *1 C     0 {1,S} {3,S} {4,D}
3  *2 O     0 {2,S} {5,S}
4     O     0 {2,D}
5  *4 H     0 {3,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,D}
2  *2 O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
1  *3 C     0 {2,S}
2  *4 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.75e+12,"s^-1"),
        n = 0,
        Ea = (295164,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Mackie, J.C.", "Doolan, K.R."], title=u'High-temperature kinetics of thermal decomposition of acetic acid and its products', journal="Int. J. Chem. Kinet.", volume="16", pages="""525""", year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 8,
    label = "r00001645",
    reactant1 = 
"""
1  *3 C     0 {2,S}
2  *1 C     0 {1,S} {3,S} {4,D}
3  *2 O     0 {2,S} {5,S}
4     O     0 {2,D}
5  *4 H     0 {3,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,D}
2  *2 O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
1  *3 C     0 {2,S}
2  *4 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.08e+13,"s^-1"),
        n = 0,
        Ea = (311793,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Duan, X.", "Page, M."], title=u'Theoretical investigation of competing mechanisms in the thermal unimolecular decomposition of acetic acid and the hydration reaction of ketene', journal="J. Am. Chem. Soc.", volume="117", pages="""5114-5119""", year="1995", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:31 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 9,
    label = "r00003987",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *1 C     0 {1,S} {4,S} {5,D}
4  *2 O     0 {3,S} {6,S}
5     O     0 {3,D}
6  *4 H     0 {4,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,D}
2  *2 O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
1  *3 C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *4 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.03e+09,"s^-1"),
        n = 0,
        Ea = (206199,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Blake, P.G.", "Hole, K.J."], title=u'The thermal decomposition of propionic acid', journal="J. Chem. Soc. B", pages="""577-579""", year="1966", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
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
    index = 10,
    label = "r00004480",
    reactant1 = 
"""
1  *3 C     0 {2,S} {8,S}
2     C     0 {1,S} {3,B} {4,B}
3     C     0 {2,B} {6,B}
4     C     0 {2,B} {7,B}
5     C     0 {6,B} {7,B}
6     C     0 {3,B} {5,B}
7     C     0 {4,B} {5,B}
8  *1 C     0 {1,S} {9,S} {10,D}
9  *2 O     0 {8,S} {11,S}
10    O     0 {8,D}
11 *4 H     0 {9,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,D}
2  *2 O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
1  *3 C     0 {2,S} {8,S}
2     C     0 {1,S} {3,B} {4,B}
3     C     0 {2,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {7,B}
6     C     0 {4,B} {7,B}
7     C     0 {5,B} {6,B}
8  *4 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"s^-1"),
        n = 0,
        Ea = (101437,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Colussi, A.J.", "Amorebieta, V.T.", "Grela, M.A."], title=u'Very low pressure pyrolysis of phenylacetic acid', journal="J. Chem. Soc. Faraday Trans.", volume="88", pages="""2125-2127""", year="1992", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:44 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 11,
    label = "r00006301",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S} {6,D}
3     C     0 {1,S} {5,S} {7,D}
4  *2 O     0 {2,S} {8,S}
5     O     0 {3,S}
6     O     0 {2,D}
7     O     0 {3,D}
8  *4 H     0 {4,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,D}
2  *2 O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
1  *3 C     0 {2,S} {4,S}
2     C     0 {1,S} {3,S} {5,D}
3     O     0 {2,S}
4  *4 H     0 {1,S}
5     O     0 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.86e+13,"s^-1"),
        n = 0,
        Ea = (129706,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Cao, J.-R.", "Back, R.A."], title=u'The thermolysis and photolysis of malonic acid in the gas phase', journal="Can. J. Chem.", volume="64", pages="""967""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:33:58 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 12,
    label = "r00008130",
    reactant1 = 
"""
1  *3 C     0 {2,S} {8,S} {9,S}
2     C     0 {1,S} {3,B} {4,B}
3     C     0 {2,B} {6,B}
4     C     0 {2,B} {7,B}
5     C     0 {6,B} {7,B}
6     C     0 {3,B} {5,B}
7     C     0 {4,B} {5,B}
8  *1 C     0 {1,S} {10,S} {11,D}
9     O     0 {1,S}
10 *2 O     0 {8,S} {12,S}
11    O     0 {8,D}
12 *4 H     0 {10,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,D}
2  *2 O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
1  *3 C     0 {2,S} {8,S} {9,S}
2     C     0 {1,S} {3,B} {4,B}
3     C     0 {2,B} {5,B}
4     C     0 {2,B} {6,B}
5     C     0 {3,B} {7,B}
6     C     0 {4,B} {7,B}
7     C     0 {5,B} {6,B}
8     O     0 {1,S}
9  *4 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.41e+14,"s^-1"),
        n = 0,
        Ea = (3349.13,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Chuchani, G.", "Martin, I."], title=u'ELIMINATION KINETICS OF DL-MANDELIC ACID IN THE GAS PHASE', journal="J. Phys. Org. Chem.", volume="10", pages="""121-124""", year="1997", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:12 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 13,
    label = "r00008316",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3  *1 C     0 {1,S} {5,S} {6,D}
4     C     0 {2,D}
5  *2 O     0 {3,S} {7,S}
6     O     0 {3,D}
7  *4 H     0 {5,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,D}
2  *2 O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
1  *3 C     0 {2,S} {4,S}
2     C     0 {1,S} {3,D}
3     C     0 {2,D}
4  *4 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.54e+11,"s^-1"),
        n = 0,
        Ea = (162132,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Smith, G.G.", "Blau, S.E."], title=u'Decarboxylation. I. Kinetic study of the vapor phase thermal decarboxylation of 3-butenoic acid', journal="J. Phys. Chem.", volume="68", pages="""1231-1234""", year="1964", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:15 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 14,
    label = "r00008316",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3  *1 C     0 {1,S} {5,S} {6,D}
4     C     0 {2,D}
5  *2 O     0 {3,S} {7,S}
6     O     0 {3,D}
7  *4 H     0 {5,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,D}
2  *2 O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
1  *3 C     0 {2,S} {4,S}
2     C     0 {1,S} {3,D}
3     C     0 {2,D}
4  *4 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.97e+11,"s^-1"),
        n = 0,
        Ea = (167952,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Bigley, D.B.", "Weatherhead, R.H.", "May, R.W."], title=u'Studies in Decarboxylation. Part 10. Effect of \u03b2-Substituents on the Rate of Gas-phase Decarboxylation of \u03b2\u03b2\u03b2\u03b2\u03c0\u03b2-Unsaturated Acids', journal="J. Chem. Soc. Perkin Trans. 2", pages="""745""", year="1977", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:15 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 15,
    label = "r00008316",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3  *1 C     0 {1,S} {5,S} {6,D}
4     C     0 {2,D}
5  *2 O     0 {3,S} {7,S}
6     O     0 {3,D}
7  *4 H     0 {5,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,D}
2  *2 O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
1  *3 C     0 {2,S} {4,S}
2     C     0 {1,S} {3,D}
3     C     0 {2,D}
4  *4 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.12e+13,"s^-1"),
        n = 0,
        Ea = (190401,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Bigley, D.B.", "Clarke, M.J."], title=u'Studies in Decarboxylation. Part 14. The Gas-phase Decarboxylation of But-3-enoic Acid and the Intermediacy of Isocrotonic (cis-But-2-enoic) Acid in its Isomerization to Crotonic (trans-But-2-enoic) Acid', journal="J. Chem. Soc. Perkin Trans. 2", pages="""1""", year="1982", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:15 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 16,
    label = "r00012640",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S} {5,S} {6,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {5,S}
5     C     0 {1,S} {4,S} {7,D}
6  *1 C     0 {1,S} {8,S} {9,D}
7     C     0 {5,D}
8  *2 O     0 {6,S} {10,S}
9     O     0 {6,D}
10 *4 H     0 {8,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,D}
2  *2 O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
1  *3 C     0 {2,S} {3,S} {5,S} {7,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {5,S}
5     C     0 {1,S} {4,S} {6,D}
6     C     0 {5,D}
7  *4 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.65e+10,"s^-1"),
        n = 0,
        Ea = (133863,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Bigley, D.B.", "May, R.W."], title=u'Studies in decarboxylation. Part IV. The effect of alkyl substituents on the rate of gas-phase decarboxylation of some \u03b2\u03b3-unsaturated acids', journal="J. Chem. Soc. B", pages="""557-559""", year="1967", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:56 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 17,
    label = "r00012640",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S} {5,S} {6,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {5,S}
5     C     0 {1,S} {4,S} {7,D}
6  *1 C     0 {1,S} {8,S} {9,D}
7     C     0 {5,D}
8  *2 O     0 {6,S} {10,S}
9     O     0 {6,D}
10 *4 H     0 {8,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,D}
2  *2 O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
1  *3 C     0 {2,S} {3,S} {5,S} {7,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {5,S}
5     C     0 {1,S} {4,S} {6,D}
6     C     0 {5,D}
7  *4 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.04e+11,"s^-1"),
        n = 0,
        Ea = (143009,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Al-Borno, A.", "Bigley, D.B."], title=u'Studies in Decarboxylation. Par t 15. The Effects of 3-Substitution on the Rate of Decarboxylation of \u03b2\u03b2\u03c0\u03b2-Unsaturated Acids', journal="J. Chem. Soc. Perkin Trans. 2", pages="""15""", year="1982", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:34:56 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 18,
    label = "r00012860",
    reactant1 = 
"""
1  *3 C     0 {3,S} {5,S}
2     C     0 {4,S}
3     C     0 {1,S} {4,D}
4     C     0 {2,S} {3,D}
5  *1 C     0 {1,S} {6,S} {7,D}
6  *2 O     0 {5,S} {8,S}
7     O     0 {5,D}
8  *4 H     0 {6,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,D}
2  *2 O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
1  *3 C     0 {3,S} {5,S}
2     C     0 {4,S}
3     C     0 {1,S} {4,D}
4     C     0 {2,S} {3,D}
5  *4 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.34e+11,"s^-1"),
        n = 0,
        Ea = (172941,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Bigley, D.B.", "Weatherhead, R.H."], title=u'Studies in Decarboxylation. Part VIII. The Gas-phase Pyrolysis of \u03b2\u03c0-Acetylenic Acids', journal="J. Chem. Soc. Perkin Trans. 2", pages="""592""", year="1976", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:01 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 19,
    label = "r00014891",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S} {6,D}
5  *1 C     0 {1,S} {7,S} {8,D}
6     C     0 {4,D}
7  *2 O     0 {5,S} {9,S}
8     O     0 {5,D}
9  *4 H     0 {7,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,D}
2  *2 O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
1  *3 C     0 {2,S} {3,S} {4,S} {6,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S} {5,D}
5     C     0 {4,D}
6  *4 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.65e+10,"s^-1"),
        n = 0,
        Ea = (148829,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Bigley, D.B.", "May, R.W."], title=u'Studies in decarboxylation. Part IV. The effect of alkyl substituents on the rate of gas-phase decarboxylation of some \u03b2\u03b3-unsaturated acids', journal="J. Chem. Soc. B", pages="""557-559""", year="1967", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:16 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 20,
    label = "r00014891",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S} {6,D}
5  *1 C     0 {1,S} {7,S} {8,D}
6     C     0 {4,D}
7  *2 O     0 {5,S} {9,S}
8     O     0 {5,D}
9  *4 H     0 {7,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,D}
2  *2 O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
1  *3 C     0 {2,S} {3,S} {4,S} {6,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S} {5,D}
5     C     0 {4,D}
6  *4 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.03e+11,"s^-1"),
        n = 0,
        Ea = (154649,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Al-Borno, A.", "Bigley, D.B."], title=u'Studies in Decarboxylation. Par t 15. The Effects of 3-Substitution on the Rate of Decarboxylation of \u03b2\u03b2\u03c0\u03b2-Unsaturated Acids', journal="J. Chem. Soc. Perkin Trans. 2", pages="""15""", year="1982", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:16 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 21,
    label = "r00015735",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S} {5,S} {7,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {6,S}
5     C     0 {1,S} {6,D}
6     C     0 {4,S} {5,D}
7  *1 C     0 {1,S} {8,S} {9,D}
8  *2 O     0 {7,S} {10,S}
9     O     0 {7,D}
10 *4 H     0 {8,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,D}
2  *2 O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
1  *3 C     0 {2,S} {3,S} {5,S} {7,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {6,S}
5     C     0 {1,S} {6,D}
6     C     0 {4,S} {5,D}
7  *4 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.64e+11,"s^-1"),
        n = 0,
        Ea = (164627,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Bigley, D.B.", "May, R.W."], title=u'Studies in decarboxylation. Part IV. The effect of alkyl substituents on the rate of gas-phase decarboxylation of some \u03b2\u03b3-unsaturated acids', journal="J. Chem. Soc. B", pages="""557-559""", year="1967", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:27 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 22,
    label = "r00015736",
    reactant1 = 
"""
1  *3 C     0 {3,S} {4,S} {7,S} {9,S}
2     C     0 {5,S} {7,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     C     0 {8,S}
7     C     0 {1,S} {2,S} {8,D}
8     C     0 {6,S} {7,D}
9  *1 C     0 {1,S} {10,S} {11,D}
10 *2 O     0 {9,S} {12,S}
11    O     0 {9,D}
12 *4 H     0 {10,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,D}
2  *2 O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
1  *3 C     0 {3,S} {4,S} {7,S} {9,S}
2     C     0 {5,S} {7,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     C     0 {8,S}
7     C     0 {1,S} {2,S} {8,D}
8     C     0 {6,S} {7,D}
9  *4 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.07e+11,"s^-1"),
        n = 0,
        Ea = (146335,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Bigley, D.B.", "May, R.W."], title=u'Studies in decarboxylation. Part IV. The effect of alkyl substituents on the rate of gas-phase decarboxylation of some \u03b2\u03b3-unsaturated acids', journal="J. Chem. Soc. B", pages="""557-559""", year="1967", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:27 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 23,
    label = "r00015737",
    reactant1 = 
"""
1  *3 C     0 {5,S} {6,S} {7,S} {9,S}
2     C     0 {3,S} {4,S}
3     C     0 {2,S} {7,S}
4     C     0 {2,S} {8,S}
5     C     0 {1,S}
6     C     0 {1,S}
7     C     0 {1,S} {3,S} {8,D}
8     C     0 {4,S} {7,D}
9  *1 C     0 {1,S} {10,S} {11,D}
10 *2 O     0 {9,S} {12,S}
11    O     0 {9,D}
12 *4 H     0 {10,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D} {3,D}
2  *2 O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
1  *3 C     0 {5,S} {6,S} {7,S} {9,S}
2     C     0 {3,S} {4,S}
3     C     0 {2,S} {7,S}
4     C     0 {2,S} {8,S}
5     C     0 {1,S}
6     C     0 {1,S}
7     C     0 {1,S} {3,S} {8,D}
8     C     0 {4,S} {7,D}
9  *4 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.25e+08,"s^-1"),
        n = 0,
        Ea = (121391,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Bigley, D.B.", "May, R.W."], title=u'Studies in decarboxylation. Part IV. The effect of alkyl substituents on the rate of gas-phase decarboxylation of some \u03b2\u03b3-unsaturated acids', journal="J. Chem. Soc. B", pages="""557-559""", year="1967", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""
""",
    history = [
        ("Tue May 17 14:35:28 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

