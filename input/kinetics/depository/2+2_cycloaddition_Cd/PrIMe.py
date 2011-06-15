#!/usr/bin/env python
# encoding: utf-8

name = "2+2_cycloaddition_Cd/PrIMe"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 1,
    label = "r00006431",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S} {5,S}
2  *4 C     0 {1,S} {4,S} {6,S}
3     C     0 {1,S} {7,S}
4     C     0 {2,S} {7,S}
5  *1 C     0 {1,S} {6,S}
6  *2 C     0 {2,S} {5,S}
7     C     0 {3,S} {4,S}
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
4  *3 C     0 {2,S} {5,D}
5  *4 C     0 {3,S} {4,D}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (6.92e+14,"s^-1"),
        n = 0,
        Ea = (254423,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Ellis, R.J.", "Frey, H.M."], title=u'The thermal unimolecular decomposition of bicyclo[3,2,0]-heptane', journal="J. Chem. Soc.", pages="""4184-4187""", year="1964", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:59 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 2,
    label = "r00006456",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {4,S}
4  *4 C     0 {2,S} {3,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1  *4 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    degeneracy = 16,
    kinetics = Arrhenius(
        A = (4e+15,"s^-1"),
        n = 0,
        Ea = (261906,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Genaux, C.T.", "Kern, F.", "Walters, W.D."], title=u'The thermal decomposition of cyclobutane', journal="J. Am. Chem. Soc.", volume="75", pages="""6196-6199""", year="1953", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:01 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 3,
    label = "r00006456",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {4,S}
4  *4 C     0 {2,S} {3,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1  *4 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    degeneracy = 16,
    kinetics = Arrhenius(
        A = (2e+15,"s^-1"),
        n = 0,
        Ea = (257749,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Butler, J.N.", "Ogawa, R.B."], title=u'The thermal decomposition of cyclobutane at low pressures', journal="J. Am. Chem. Soc.", volume="85", pages="""3346-3349""", year="1963", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000012.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:01 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 4,
    label = "r00006456",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {4,S}
4  *4 C     0 {2,S} {3,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1  *4 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    degeneracy = 16,
    kinetics = Arrhenius(
        A = (4.2e+15,"s^-1"),
        n = 0,
        Ea = (261906,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Carr, R.W., Jr.", "Walters, W.D."], title=u'The thermal decomposition of cyclobutane', journal="J. Phys. Chem.", volume="67", pages="""1370-1372""", year="1963", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000013.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:01 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 5,
    label = "r00006456",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {4,S}
4  *4 C     0 {2,S} {3,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1  *4 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    degeneracy = 16,
    kinetics = Arrhenius(
        A = (7.01e+15,"s^-1"),
        n = 0,
        Ea = (264400,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Vreeland, R.W.", "Swinehart, D.F."], title=u'A mass spectometric investigation of the thermal decomposition of cyclobutane at low pressures', journal="J. Am. Chem. Soc.", volume="85", pages="""3349-3353""", year="1963", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000014.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:01 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 6,
    label = "r00006456",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {4,S}
4  *4 C     0 {2,S} {3,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1  *4 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    degeneracy = 16,
    kinetics = Arrhenius(
        A = (2.63e+15,"s^-1"),
        n = 0,
        Ea = (259412,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Beadle, P.C.", "Golden, D.M.", "King, K.D.", "Benson, S.W."], title=u'Pyrolysis of Cyclobutane', journal="J. Am. Chem. Soc.", volume="94", pages="""2943""", year="1972", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000016.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:01 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 7,
    label = "r00006456",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {4,S}
4  *4 C     0 {2,S} {3,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1  *4 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    degeneracy = 16,
    kinetics = Arrhenius(
        A = (3.16e+16,"s^-1"),
        n = 0,
        Ea = (274378,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Beadle, P.C.", "Golden, D.M.", "King, K.D.", "Benson, S.W."], title=u'Pyrolysis of Cyclobutane', journal="J. Am. Chem. Soc.", volume="94", pages="""2943""", year="1972", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000017.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:01 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 8,
    label = "r00006456",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {4,S}
4  *4 C     0 {2,S} {3,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1  *4 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    degeneracy = 16,
    kinetics = Arrhenius(
        A = (1.52e+14,"s^-1"),
        n = 0,
        Ea = (229479,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Barnard, J.A.", "Cocks, A.T.", "Lee, R.K.Y."], title=u'Kinetics of the Thermal Unimolecular Reactions of Cyclopropane and Cyclobutane behind Reflected Shock Waves', journal="J. Chem. Soc. Faraday Trans. 1", volume="70", pages="""1782""", year="1974", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000018.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:01 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 9,
    label = "r00006456",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {4,S}
4  *4 C     0 {2,S} {3,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1  *4 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    degeneracy = 16,
    kinetics = Arrhenius(
        A = (3.98e+15,"s^-1"),
        n = 0,
        Ea = (261906,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Lewis, D.K.", "Bergmann, J.", "Manjoney, R.", "Paddock, R.", "Kaira, B.L."], title=u'Rates of reactions of cyclopropane, cyclobutane, cyclopentene, and cyclohexene in the presence of boron trichloride', journal="J. Phys. Chem.", volume="88", pages="""4112""", year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000019.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:01 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 10,
    label = "r00006456",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    reactant2 = 
"""
1  *3 C     0 {2,D}
2  *4 C     0 {1,D}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {4,S}
4  *4 C     0 {2,S} {3,S}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (6.92e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (182918,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Quick, L.M.", "Knecht, D.A.", "Back, M.H."], title=u'Kinetics of the Formation of Cyclobutane from Ethylene', journal="Int. J. Chem. Kinet.", volume="4", pages="""61""", year="1972", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000020.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:01 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 11,
    label = "r00007176",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {4,S}
4  *4 O     0 {2,S} {3,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1  *3 C     0 {2,D}
2  *4 O     0 {1,D}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (5.13e+15,"s^-1"),
        n = 0,
        Ea = (263569,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Holbrook, K.A.", "Scott, R.A."], title=u'Gas-phase Thermal Unimolecular Decomposition of Oxetan', journal="J. Chem. Soc. Faraday Trans. 1", volume="71", pages="""1849""", year="1975", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:03 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 12,
    label = "r00007176",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {4,S}
4  *4 O     0 {2,S} {3,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1  *3 C     0 {2,D}
2  *4 O     0 {1,D}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (2.63e+15,"s^-1"),
        n = 0,
        Ea = (259412,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Zalotai, L.", "Hunyadi-Zoltan, Zs.", "Berces, T.", "Marta, F."], title=u'Kinetics of gas phase decomposition of oxetan and oxetan-2,2-d_2', journal="Int. J. Chem. Kinet.", volume="15", pages="""505""", year="1983", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:03 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 13,
    label = "r00008107",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {5,S}
2  *1 C     0 {1,S} {4,S}
3  *4 C     0 {1,S} {4,S}
4  *3 C     0 {2,S} {3,S}
5     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    product2 = 
"""
1  *4 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (2.4e+15,"s^-1"),
        n = 0,
        Ea = (256086,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Das, M.N.", "Walters, W.D."], title=u'The thermal decomposition of methylcyclobutane', journal="Z. Phys. Chem. (Neue Folge)", volume="15", pages="""22-33""", year="1958", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:12 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 14,
    label = "r00008107",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {5,S}
2  *1 C     0 {1,S} {4,S}
3  *4 C     0 {1,S} {4,S}
4  *3 C     0 {2,S} {3,S}
5     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    product2 = 
"""
1  *4 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (1.9e+15,"s^-1"),
        n = 0,
        Ea = (254423,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Pataracchia, A.F.", "Walters, W.D."], title=u'The thermal decomposition of methylcyclobutane at low pressures', journal="J. Phys. Chem.", volume="68", pages="""3894-3899""", year="1964", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:12 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 15,
    label = "r00008107",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {5,S}
2  *1 C     0 {1,S} {4,S}
3  *4 C     0 {1,S} {4,S}
4  *3 C     0 {2,S} {3,S}
5     C     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    product2 = 
"""
1  *4 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (1.06e+16,"s^-1"),
        n = 0,
        Ea = (264400,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Thomas, T.F.", "Conn, P.J.", "Swinehart, D.F."], title=u'Unimolecular reactions of methylcyclobutane at low pressures', journal="J. Am. Chem. Soc.", volume="91", pages="""7611-7616""", year="1969", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:12 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 16,
    label = "r00008915",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {6,S}
2  *1 C     0 {1,S} {4,S}
3  *4 C     0 {1,S} {4,S}
4  *3 C     0 {2,S} {3,S}
5     C     0 {7,S}
6     C     0 {1,S} {7,S} {8,D}
7     O     0 {5,S} {6,S}
8     O     0 {6,D}
""",
    product1 = 
"""
1     C     0 {5,S}
2  *2 C     0 {3,S} {4,D}
3     C     0 {2,S} {5,S} {6,D}
4  *1 C     0 {2,D}
5     O     0 {1,S} {3,S}
6     O     0 {3,D}
""",
    product2 = 
"""
1  *4 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (7e+14,"s^-1"),
        n = 0,
        Ea = (239457,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Zupan, M.", "Walters, W.D."], title=u'The kinetics of the thermal decomposition of methyl cyclobutanecarboxylate', journal="J. Am. Chem. Soc.", volume="86", pages="""173-176""", year="1964", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 17,
    label = "r00008919",
    reactant1 = 
"""
1  *4 C     0 {2,S} {5,S} {6,S} {7,S}
2  *2 C     0 {1,S} {3,S} {8,S}
3  *1 C     0 {2,S} {4,S} {7,S}
4     C     0 {3,S} {9,S}
5     C     0 {1,S}
6     C     0 {1,S}
7  *3 C     0 {1,S} {3,S} {10,D}
8     C     0 {2,S} {9,D}
9     C     0 {4,S} {8,D}
10    O     0 {7,D}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3  *1 C     0 {1,S} {5,D}
4     C     0 {2,D} {5,S}
5  *2 C     0 {3,D} {4,S}
""",
    product2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *4 C     0 {1,S} {2,S} {4,D}
4  *3 C     0 {3,D} {5,D}
5     O     0 {4,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.94e+12,"s^-1"),
        n = 0,
        Ea = (157975,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Egger, K.W."], title=u'The Gas-Phase Thermal Unimolecular Elimination of 1,1-Dimethylketene from 7,7-Dimethylbicyclo[3.2.0]hept-2-en-6-one', journal="Int. J. Chem. Kinet.", volume="5", pages="""285""", year="1973", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:19 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 18,
    label = "r00009049",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {6,S} {7,S}
3  *1 C     0 {1,S} {5,S}
4  *4 C     0 {1,S} {5,S}
5  *3 C     0 {3,S} {4,S}
6     C     0 {2,S}
7     C     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *2 C     0 {1,S} {5,D}
5  *1 C     0 {4,D}
""",
    product2 = 
"""
1  *4 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (4.3e+15,"s^-1"),
        n = 0,
        Ea = (261906,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Zupan, M.", "Walters, W.D."], title=u'The kinetics of the thermal decomposition of isopropylcyclobutane', journal="J. Phys. Chem.", volume="67", pages="""1845-1848""", year="1963", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:20 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 19,
    label = "r00009414",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {4,S}
4  *4 C     0 {2,S} {3,S} {5,D}
5     O     0 {4,D}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1  *3 C     0 {2,D}
2  *4 C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (3.6e+14,"s^-1"),
        n = 0,
        Ea = (217839,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Das, M.N.", "Kern, F.", "Coyle, T.D.", "Walters, W.D."], title=u'The thermal decomposition of cyclobutanone', journal="J. Am. Chem. Soc.", volume="76", pages="""6271-6274""", year="1954", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:25 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 20,
    label = "r00009414",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {4,S}
4  *4 C     0 {2,S} {3,S} {5,D}
5     O     0 {4,D}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1  *3 C     0 {2,D}
2  *4 C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (3.6e+14,"s^-1"),
        n = 0,
        Ea = (217008,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["McGee, T.H.", "Schleifer, A."], title=u'Thermal Decomposition of Cyclobutanone', journal="J. Phys. Chem.", volume="76", pages="""963""", year="1972", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:25 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 21,
    label = "r00009414",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S}
3  *3 C     0 {1,S} {4,S}
4  *4 C     0 {2,S} {3,S} {5,D}
5     O     0 {4,D}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1  *3 C     0 {2,D}
2  *4 C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (5e+14,"s^-1"),
        n = 0,
        Ea = (220334,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Braun, W.", "McNesby, J.R.", "Scheer, M.D."], title=u'A comparative rate method for the study of unimolecular falloff behavior', journal="J. Phys. Chem.", volume="88", pages="""1846""", year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:25 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 22,
    label = "r00009420",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S}
2  *1 C     0 {1,S} {5,S}
3  *4 C     0 {1,S} {5,S}
4     C     0 {1,S}
5  *3 C     0 {2,S} {3,S} {6,D}
6     O     0 {5,D}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    product2 = 
"""
1  *4 C     0 {2,D}
2  *3 C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.74e+14,"s^-1"),
        n = 0,
        Ea = (200379,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Frey, H.M.", "Watts, H.P.", "Stevens, I.D.R."], title=u'The thermal unimolecular decomposition of 3-methylcyclobutanone', journal="J. Chem. Soc. Faraday Trans. 2", volume="83", pages="""601""", year="1987", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:25 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 23,
    label = "r00009421",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S} {5,S}
2  *1 C     0 {1,S} {6,S}
3  *4 C     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6  *3 C     0 {2,S} {3,S} {7,D}
7     O     0 {6,D}
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
1  *4 C     0 {2,D}
2  *3 C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.74e+14,"s^-1"),
        n = 0,
        Ea = (192896,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Frey, H.M.", "Smith, R.A."], title=u'Thermal decomposition of 3,3-dimethylcyclobutanone', journal="J. Chem. Soc. Perkin Trans. 2", pages="""752""", year="1977", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:25 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 24,
    label = "r00010716",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S}
2  *1 C     0 {1,S} {5,S}
3  *4 C     0 {1,S} {5,S}
4     C     0 {1,S}
5  *3 O     0 {2,S} {3,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    product2 = 
"""
1  *4 C     0 {2,D}
2  *3 O     0 {1,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.4e+15,"s^-1"),
        n = 0,
        Ea = (258580,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Zalotai, L.", "Berces, T.", "Marta, F."], title=u'Kinetics and energy transfer in the thermal decomposition of 2-methyloxetane and 3-methyloxetane', journal="J. Chem. Soc. Faraday Trans. 1", volume="86", pages="""21""", year="1990", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:40 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 25,
    label = "r00010716",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S}
2  *1 C     0 {1,S} {5,S}
3  *4 C     0 {1,S} {5,S}
4     C     0 {1,S}
5  *3 O     0 {2,S} {3,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    product2 = 
"""
1  *4 C     0 {2,D}
2  *3 O     0 {1,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.4e+15,"s^-1"),
        n = 0,
        Ea = (258580,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Zalotai, L.", "Berces, T.", "Marta, F."], title=u'Collisional energy transfer in the decomposition of 2-methyloxetane and 3-methyloxetane, I. Gas/gas collisions', journal="React. Kinet. Catal. Lett.", volume="42", pages="""79""", year="1990", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:40 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 26,
    label = "r00010718",
    reactant1 = 
"""
1  *2 C     0 {2,S} {4,S} {5,S}
2  *1 C     0 {1,S} {3,S}
3  *3 C     0 {2,S} {5,S}
4     C     0 {1,S}
5  *4 O     0 {1,S} {3,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    product2 = 
"""
1  *3 C     0 {2,D}
2  *4 O     0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.4e+14,"s^-1"),
        n = 0,
        Ea = (249434,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Hammonds, P.", "Holbrook, K.A."], title=u'Thermolyses of 2-Methyloxetan and 2,2-Dimethyloxetan', journal="J. Chem. Soc. Faraday Trans. 1", volume="78", pages="""2195""", year="1982", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:40 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 27,
    label = "r00010718",
    reactant1 = 
"""
1  *2 C     0 {2,S} {4,S} {5,S}
2  *1 C     0 {1,S} {3,S}
3  *3 C     0 {2,S} {5,S}
4     C     0 {1,S}
5  *4 O     0 {1,S} {3,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    product2 = 
"""
1  *3 C     0 {2,D}
2  *4 O     0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.39e+14,"s^-1"),
        n = 0,
        Ea = (249434,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Zalotai, L.", "Berces, T.", "Marta, F."], title=u'Kinetics and energy transfer in the thermal decomposition of 2-methyloxetane and 3-methyloxetane', journal="J. Chem. Soc. Faraday Trans. 1", volume="86", pages="""21""", year="1990", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:40 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 28,
    label = "r00010718",
    reactant1 = 
"""
1  *2 C     0 {2,S} {4,S} {5,S}
2  *1 C     0 {1,S} {3,S}
3  *3 C     0 {2,S} {5,S}
4     C     0 {1,S}
5  *4 O     0 {1,S} {3,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    product2 = 
"""
1  *3 C     0 {2,D}
2  *4 O     0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.39e+14,"s^-1"),
        n = 0,
        Ea = (249434,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Zalotai, L.", "Berces, T.", "Marta, F."], title=u'Collisional energy transfer in the decomposition of 2-methyloxetane and 3-methyloxetane, I. Gas/gas collisions', journal="React. Kinet. Catal. Lett.", volume="42", pages="""79""", year="1990", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:40 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 29,
    label = "r00010719",
    reactant1 = 
"""
1  *3 C     0 {2,S} {4,S} {5,S}
2  *1 C     0 {1,S} {3,S}
3  *2 C     0 {2,S} {5,S}
4     C     0 {1,S}
5  *4 O     0 {1,S} {3,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *3 C     0 {1,S} {3,D}
3  *4 O     0 {2,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.36e+14,"s^-1"),
        n = 0,
        Ea = (249434,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Hammonds, P.", "Holbrook, K.A."], title=u'Thermolyses of 2-Methyloxetan and 2,2-Dimethyloxetan', journal="J. Chem. Soc. Faraday Trans. 1", volume="78", pages="""2195""", year="1982", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:40 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 30,
    label = "r00010719",
    reactant1 = 
"""
1  *3 C     0 {2,S} {4,S} {5,S}
2  *1 C     0 {1,S} {3,S}
3  *2 C     0 {2,S} {5,S}
4     C     0 {1,S}
5  *4 O     0 {1,S} {3,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *3 C     0 {1,S} {3,D}
3  *4 O     0 {2,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (4.68e+15,"s^-1"),
        n = 0,
        Ea = (269389,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Zalotai, L.", "Berces, T.", "Marta, F."], title=u'Kinetics and energy transfer in the thermal decomposition of 2-methyloxetane and 3-methyloxetane', journal="J. Chem. Soc. Faraday Trans. 1", volume="86", pages="""21""", year="1990", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:40 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 31,
    label = "r00010719",
    reactant1 = 
"""
1  *3 C     0 {2,S} {4,S} {5,S}
2  *1 C     0 {1,S} {3,S}
3  *2 C     0 {2,S} {5,S}
4     C     0 {1,S}
5  *4 O     0 {1,S} {3,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *3 C     0 {1,S} {3,D}
3  *4 O     0 {2,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (4.68e+15,"s^-1"),
        n = 0,
        Ea = (269389,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Zalotai, L.", "Berces, T.", "Marta, F."], title=u'Collisional energy transfer in the decomposition of 2-methyloxetane and 3-methyloxetane, I. Gas/gas collisions', journal="React. Kinet. Catal. Lett.", volume="42", pages="""79""", year="1990", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:40 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 32,
    label = "r00011373",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {5,S}
2  *1 C     0 {1,S} {4,S}
3  *4 C     0 {1,S} {4,S}
4  *3 C     0 {2,S} {3,S}
5     C     0 {1,S} {6,D}
6     C     0 {5,D}
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
1  *4 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (7.41e+14,"s^-1"),
        n = 0,
        Ea = (212019,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Frey, H.M.", "Pottinger, R."], title=u'Thermal unimolecular reactions of vinylcyclobutane and isopropenylcyclobutane', journal="J. Chem. Soc. Faraday Trans. 1", volume="74", pages="""1827""", year="1978", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 33,
    label = "r00011373",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {5,S}
2  *1 C     0 {1,S} {4,S}
3  *4 C     0 {1,S} {4,S}
4  *3 C     0 {2,S} {3,S}
5     C     0 {1,S} {6,D}
6     C     0 {5,D}
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
1  *4 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (3.16e+14,"s^-1"),
        n = 0,
        Ea = (208693,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Lewis, D.K.", "Charney, D.J.", "Kalra, B.L.", "Plate, A-M.", "Woodard, M.H."], title=u'Kinetics of the thermal isomerizations of gaseous vinylcyclopropane and vinylcyclobutane', journal="J. Phys. Chem. A", volume="101", pages="""4097-4102""", year="1997", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 34,
    label = "r00011611",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {5,S}
2  *1 C     0 {1,S} {4,S}
3  *4 C     0 {1,S} {4,S}
4  *3 C     0 {2,S} {3,S}
5     C     0 {1,S} {6,D}
6     O     0 {5,D}
""",
    product1 = 
"""
1  *2 C     0 {2,S} {3,D}
2     C     0 {1,S} {4,D}
3  *1 C     0 {1,D}
4     O     0 {2,D}
""",
    product2 = 
"""
1  *4 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (2.7e+14,"s^-1"),
        n = 0,
        Ea = (222828,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Roquitte, B.C.", "Walters, W.D."], title=u'The thermal decomposition of cyclobutanecarboxaldehyde', journal="J. Am. Chem. Soc.", volume="84", pages="""4049-4052""", year="1962", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:48 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 35,
    label = "r00011630",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {6,S}
2  *1 C     0 {1,S} {4,S}
3  *4 C     0 {1,S} {4,S}
4  *3 C     0 {2,S} {3,S}
5     C     0 {6,S}
6     C     0 {1,S} {5,S} {7,D}
7     C     0 {6,D}
""",
    product1 = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S} {4,D}
3  *2 C     0 {2,S} {5,D}
4     C     0 {2,D}
5  *1 C     0 {3,D}
""",
    product2 = 
"""
1  *4 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (4.37e+14,"s^-1"),
        n = 0,
        Ea = (213682,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Ellis, R.J.", "Frey, H.M."], title=u'Thermal unimolecular decomposition of isopropenylcyclobutane', journal="Trans. Faraday Soc.", volume="59", pages="""2076-2079""", year="1963", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:49 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 36,
    label = "r00011630",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {6,S}
2  *1 C     0 {1,S} {4,S}
3  *4 C     0 {1,S} {4,S}
4  *3 C     0 {2,S} {3,S}
5     C     0 {6,S}
6     C     0 {1,S} {5,S} {7,D}
7     C     0 {6,D}
""",
    product1 = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S} {4,D}
3  *2 C     0 {2,S} {5,D}
4     C     0 {2,D}
5  *1 C     0 {3,D}
""",
    product2 = 
"""
1  *4 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (1.66e+15,"s^-1"),
        n = 0,
        Ea = (218671,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Frey, H.M.", "Pottinger, R."], title=u'Thermal unimolecular reactions of vinylcyclobutane and isopropenylcyclobutane', journal="J. Chem. Soc. Faraday Trans. 1", volume="74", pages="""1827""", year="1978", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:49 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 37,
    label = "r00011632",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {6,S}
2  *1 C     0 {1,S} {4,S}
3  *4 C     0 {1,S} {4,S}
4  *3 C     0 {2,S} {3,S}
5     C     0 {6,S}
6     C     0 {1,S} {5,S} {7,D}
7     O     0 {6,D}
""",
    product1 = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S} {5,D}
3  *2 C     0 {2,S} {4,D}
4  *1 C     0 {3,D}
5     O     0 {2,D}
""",
    product2 = 
"""
1  *4 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (3.4e+14,"s^-1"),
        n = 0,
        Ea = (227817,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Daignault, L.G.", "Walters, W.D."], title=u'The thermal decomposition of methyl cyclobutyl ketone', journal="J. Am. Chem. Soc.", volume="80", pages="""541-545""", year="1958", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:49 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 38,
    label = "r00012680",
    reactant1 = 
"""
1  *2 C     0 {3,S} {4,S} {5,S} {8,S}
2  *3 C     0 {3,S} {6,S} {7,S} {8,S}
3  *1 C     0 {1,S} {2,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {2,S}
8  *4 C     0 {1,S} {2,S} {9,D}
9     O     0 {8,D}
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
1     C     0 {3,S}
2     C     0 {3,S}
3  *3 C     0 {1,S} {2,S} {4,D}
4  *4 C     0 {3,D} {5,D}
5     O     0 {4,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (7.23e+14,"s^-1"),
        n = 0,
        Ea = (234468,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Frey, H.M.", "Hopf, H."], title=u'The thermal unimolecular decomposition of 2,2,4,4-tetramethylcyclobutanone', journal="J. Chem. Soc. Perkin Trans. 2", pages="""2016""", year="1973", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:56 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 39,
    label = "r00012719",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {5,S}
2  *1 C     0 {1,S} {4,S}
3  *4 C     0 {1,S} {4,S}
4  *3 C     0 {2,S} {3,S}
5     C     0 {1,S} {6,S}
6     O     0 {5,S}
""",
    product1 = 
"""
1     C     0 {2,S} {4,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
4     O     0 {1,S}
""",
    product2 = 
"""
1  *4 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (1.51e+15,"s^-1"),
        n = 0,
        Ea = (256086,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dirjal, N.K.", "Holbrook, K.A."], title=u'Thermal unimolecular decomposition of cyclobutanemethanol', journal="J. Chem. Soc. Faraday Trans.", volume="87", pages="""691-693""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:57 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 40,
    label = "r00012797",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S}
2  *1 C     0 {1,S} {5,S}
3  *4 C     0 {1,S} {5,S}
4     C     0 {1,S} {6,S}
5  *3 C     0 {2,S} {3,S}
6     C     0 {4,S}
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
1  *4 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (3.6e+15,"s^-1"),
        n = 0,
        Ea = (259412,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Wellman, R.E.", "Walters, W.D."], title=u'The thermal decomposition of ethylcyclobutane', journal="J. Am. Chem. Soc.", volume="79", pages="""1542-1546""", year="1957", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:58 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 41,
    label = "r00012798",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S} {6,S}
3  *1 C     0 {1,S} {5,S}
4  *4 C     0 {1,S} {5,S}
5  *3 C     0 {3,S} {4,S}
6     C     0 {2,S} {7,S}
7     C     0 {6,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4  *2 C     0 {2,S} {5,D}
5  *1 C     0 {4,D}
""",
    product2 = 
"""
1  *4 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (3.4e+15,"s^-1"),
        n = 0,
        Ea = (257749,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kellner, S.M.E.", "Walters, W.D."], title=u'The thermal decomposition of n-propylcyclobutane', journal="J. Phys. Chem.", volume="65", pages="""466-469""", year="1961", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:58 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 42,
    label = "r00012962",
    reactant1 = 
"""
1  *2 C     0 {2,S} {4,S} {5,S} {6,S}
2  *1 C     0 {1,S} {3,S}
3  *3 C     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6  *4 O     0 {1,S} {3,S}
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
1  *3 C     0 {2,D}
2  *4 O     0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.02e+13,"s^-1"),
        n = 0,
        Ea = (221996,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Hammonds, P.", "Holbrook, K.A."], title=u'Thermolyses of 2-Methyloxetan and 2,2-Dimethyloxetan', journal="J. Chem. Soc. Faraday Trans. 1", volume="78", pages="""2195""", year="1982", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:05 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 43,
    label = "r00012963",
    reactant1 = 
"""
1  *3 C     0 {2,S} {4,S} {5,S} {6,S}
2  *1 C     0 {1,S} {3,S}
3  *2 C     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6  *4 O     0 {1,S} {3,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *3 C     0 {1,S} {2,S} {4,D}
4  *4 O     0 {3,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.63e+15,"s^-1"),
        n = 0,
        Ea = (270220,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Hammonds, P.", "Holbrook, K.A."], title=u'Thermolyses of 2-Methyloxetan and 2,2-Dimethyloxetan', journal="J. Chem. Soc. Faraday Trans. 1", volume="78", pages="""2195""", year="1982", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:05 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 44,
    label = "r00013004",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {7,S}
2  *1 C     0 {1,S} {4,S}
3  *4 C     0 {1,S} {4,S}
4  *3 C     0 {2,S} {3,S}
5     C     0 {6,S} {7,S}
6     C     0 {5,S}
7     C     0 {1,S} {5,S} {8,D}
8     O     0 {7,D}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S} {4,S} {6,D}
4  *2 C     0 {3,S} {5,D}
5  *1 C     0 {4,D}
6     O     0 {3,D}
""",
    product2 = 
"""
1  *4 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (3.4e+14,"s^-1"),
        n = 0,
        Ea = (226985,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Roquitte, B.C.", "Walters, W.D."], title=u'The thermal decomposition of ethyl cyclobutyl ketone', journal="J. Phys. Chem.", volume="68", pages="""1606-1609""", year="1964", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:10 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 45,
    label = "r00013035",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S} {5,S}
2  *1 C     0 {1,S} {6,S}
3  *4 C     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6  *3 O     0 {2,S} {3,S}
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
1  *4 C     0 {2,D}
2  *3 O     0 {1,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.8e+15,"s^-1"),
        n = 0,
        Ea = (253591,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Cohoe, G.F.", "Walters, W.D."], title=u'The kinetics of the thermal decomposition of 3,3-dimethyloxetane', journal="J. Phys. Chem.", volume="71", pages="""2326-2331""", year="1967", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:11 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 46,
    label = "r00013054",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S} {5,S}
2  *4 C     0 {1,S} {4,S} {6,S}
3  *1 C     0 {1,S} {4,S}
4  *2 C     0 {2,S} {3,S}
5     C     0 {1,S} {7,S}
6     C     0 {2,S} {7,D}
7     C     0 {5,S} {6,D}
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
3  *3 C     0 {1,S} {5,D}
4     C     0 {2,D} {5,S}
5  *4 C     0 {3,D} {4,S}
""",
    degeneracy = 5,
    kinetics = Arrhenius(
        A = (7.94e+15,"s^-1"),
        n = 0,
        Ea = (222828,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Cocks, A.T.", "Frey, H.M."], title=u'Thermal Unimolecular Reactions of Bicyclo[3.2.0]hept-2-ene', journal="J. Chem. Soc. A", pages="""2564""", year="1971", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:11 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 47,
    label = "r00014886",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S} {6,S}
3     C     0 {1,S} {7,S}
4  *1 C     0 {1,S} {8,S}
5  *4 C     0 {1,S} {8,S}
6     C     0 {2,S}
7     C     0 {3,S}
8  *3 O     0 {4,S} {5,S}
""",
    product1 = 
"""
1     C     0 {3,S} {5,S}
2     C     0 {4,S} {5,S}
3     C     0 {1,S}
4     C     0 {2,S}
5  *2 C     0 {1,S} {2,S} {6,D}
6  *1 C     0 {5,D}
""",
    product2 = 
"""
1  *4 C     0 {2,D}
2  *3 O     0 {1,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.98e+15,"s^-1"),
        n = 0,
        Ea = (250266,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Clements, A.D.", "Frey, H.M.", "Frey, J.G."], title=u'Thermal Decomposition of 3-Ethyl-3-methyloxetan and 3,3-Diethyloxetan', journal="J. Chem. Soc. Faraday Trans. 1", volume="71", pages="""2485""", year="1975", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:16 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 48,
    label = "r00015146",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S} {5,S}
2  *2 C     0 {1,S} {3,S} {6,S}
3  *4 C     0 {2,S} {5,S}
4     C     0 {1,S} {7,S}
5  *3 C     0 {1,S} {3,S} {8,D}
6     C     0 {2,S} {7,D}
7     C     0 {4,S} {6,D}
8     O     0 {5,D}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3  *1 C     0 {1,S} {5,D}
4     C     0 {2,D} {5,S}
5  *2 C     0 {3,D} {4,S}
""",
    product2 = 
"""
1  *4 C     0 {2,D}
2  *3 C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.45e+13,"s^-1"),
        n = 0,
        Ea = (157144,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Egger, K.W.", "Cocks, A.T."], title=u'Kinetics of the Four-centre Elimination of Keten from Bicyclo[3.2.0]hept-2-en-6-one in the Gas Phase', journal="J. Chem. Soc. Perkin Trans. 2", pages="""211""", year="1972", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:17 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 49,
    label = "r00015261",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {6,S}
2  *2 C     0 {1,S} {4,S} {7,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S} {5,S}
5     C     0 {3,S} {4,S}
6  *3 C     0 {1,S} {7,S}
7  *4 C     0 {2,S} {6,S} {8,D}
8     O     0 {7,D}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4  *1 C     0 {2,S} {5,D}
5  *2 C     0 {3,S} {4,D}
""",
    product2 = 
"""
1  *3 C     0 {2,D}
2  *4 C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.62e+14,"s^-1"),
        n = 0,
        Ea = (202873,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Cocks, A.T.", "Egger, K.W."], title=u'The Gas-Phase Thermal Unimolecular Elimination of Keten from Bicyclo-[3.2.0]heptan-6-one', journal="J. Chem. Soc. Perkin Trans. 2", pages="""2014""", year="1972", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:18 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 50,
    label = "r00015648",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S} {5,S}
2  *4 C     0 {1,S} {4,S} {6,S}
3  *1 C     0 {1,S} {4,S}
4  *2 C     0 {2,S} {3,S}
5     C     0 {1,S}
6     C     0 {2,S}
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
3  *4 C     0 {1,S} {4,D}
4  *3 C     0 {2,S} {3,D}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (3.7e+15,"s^-1"),
        n = 0,
        Ea = (263569,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Gerberich, H.R.", "Walters, W.D."], title=u'The thermal decomposition of cis-1,2-dimethylcyclobutane', journal="J. Am. Chem. Soc.", volume="83", pages="""3935-3939""", year="1961", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:25 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 51,
    label = "r00015649",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {5,S}
2  *4 C     0 {1,S} {4,S} {6,S}
3  *1 C     0 {1,S} {4,S}
4  *3 C     0 {2,S} {3,S}
5     C     0 {1,S}
6     C     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *4 C     0 {1,S} {3,D}
3  *3 C     0 {2,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3e+15,"s^-1"),
        n = 0,
        Ea = (252760,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Gerberich, H.R.", "Walters, W.D."], title=u'The thermal decomposition of cis-1,2-dimethylcyclobutane', journal="J. Am. Chem. Soc.", volume="83", pages="""3935-3939""", year="1961", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:25 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 52,
    label = "r00015651",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S} {5,S}
2  *4 C     0 {1,S} {4,S} {6,S}
3  *1 C     0 {1,S} {4,S}
4  *2 C     0 {2,S} {3,S}
5     C     0 {1,S}
6     C     0 {2,S}
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
3  *4 C     0 {1,S} {4,D}
4  *3 C     0 {2,S} {3,D}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (2.9e+15,"s^-1"),
        n = 0,
        Ea = (265232,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Gerberich, H.R.", "Walters, W.D."], title=u'The thermal decomposition of trans-1,2-dimethylcyclobutane', journal="J. Am. Chem. Soc.", volume="83", pages="""4884-4888""", year="1961", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:25 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 53,
    label = "r00015652",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {5,S}
2  *4 C     0 {1,S} {4,S} {6,S}
3  *1 C     0 {1,S} {4,S}
4  *3 C     0 {2,S} {3,S}
5     C     0 {1,S}
6     C     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *4 C     0 {1,S} {3,D}
3  *3 C     0 {2,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.8e+15,"s^-1"),
        n = 0,
        Ea = (257749,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Gerberich, H.R.", "Walters, W.D."], title=u'The thermal decomposition of trans-1,2-dimethylcyclobutane', journal="J. Am. Chem. Soc.", volume="83", pages="""4884-4888""", year="1961", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:25 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 54,
    label = "r00016155",
    reactant1 = 
"""
1  *2 C     0 {3,S} {4,S} {5,S} {6,S}
2  *3 C     0 {3,S} {4,S} {7,S} {8,S}
3  *1 C     0 {1,S} {2,S}
4  *4 C     0 {1,S} {2,S}
5     C     0 {1,S}
6     C     0 {1,S}
7     C     0 {2,S}
8     C     0 {2,S}
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
1     C     0 {3,S}
2     C     0 {3,S}
3  *3 C     0 {1,S} {2,S} {4,D}
4  *4 C     0 {3,D}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (2.04e+16,"s^-1"),
        n = 0,
        Ea = (272715,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Cocks, A.T.", "Frey, H.M."], title=u'Thermal unimolecular decomposition of 1,1,3,3-tetramethylcyclobutane', journal="J. Chem. Soc. A", pages="""1671-1673""", year="1969", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:38 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 55,
    label = "r00016231",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *2 C     0 {1,S} {5,S} {6,S}
3  *3 C     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6  *4 O     0 {2,S} {3,S}
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
1  *3 C     0 {2,D}
2  *4 O     0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.09e+15,"s^-1"),
        n = 0,
        Ea = (266063,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Holbrook, K.A.", "Scott, R.A."], title=u'Gas-phase Unimolecular Pyrolyses of cis- and trans-2,3-Dimethyloxetan', journal="J. Chem. Soc. Faraday Trans. 1", volume="70", pages="""43""", year="1974", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:40 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 56,
    label = "r00016232",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S}
2  *4 C     0 {1,S} {5,S} {6,S}
3  *1 C     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6  *3 O     0 {2,S} {3,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *4 C     0 {1,S} {3,D}
3  *3 O     0 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.13e+15,"s^-1"),
        n = 0,
        Ea = (270220,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Holbrook, K.A.", "Scott, R.A."], title=u'Gas-phase Unimolecular Pyrolyses of cis- and trans-2,3-Dimethyloxetan', journal="J. Chem. Soc. Faraday Trans. 1", volume="70", pages="""43""", year="1974", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:40 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 57,
    label = "r00016297",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2  *2 C     0 {1,S} {5,S} {6,S}
3  *3 C     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6  *4 O     0 {2,S} {3,S}
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
1  *3 C     0 {2,D}
2  *4 O     0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.74e+15,"s^-1"),
        n = 0,
        Ea = (261074,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Holbrook, K.A.", "Scott, R.A."], title=u'Gas-phase Unimolecular Pyrolyses of cis- and trans-2,3-Dimethyloxetan', journal="J. Chem. Soc. Faraday Trans. 1", volume="70", pages="""43""", year="1974", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:42 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 58,
    label = "r00016298",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S}
2  *4 C     0 {1,S} {5,S} {6,S}
3  *1 C     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {2,S}
6  *3 O     0 {2,S} {3,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *1 C     0 {2,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *4 C     0 {1,S} {3,D}
3  *3 O     0 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.01e+15,"s^-1"),
        n = 0,
        Ea = (264400,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Holbrook, K.A.", "Scott, R.A."], title=u'Gas-phase Unimolecular Pyrolyses of cis- and trans-2,3-Dimethyloxetan', journal="J. Chem. Soc. Faraday Trans. 1", volume="70", pages="""43""", year="1974", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:42 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 59,
    label = "r00016299",
    reactant1 = 
"""
1  *3 C     0 {2,S} {3,S} {5,S} {6,S}
2  *4 C     0 {1,S} {4,S} {7,S}
3  *1 C     0 {1,S} {4,S}
4  *2 C     0 {2,S} {3,S}
5     C     0 {1,S}
6     C     0 {1,S}
7     C     0 {2,S}
""",
    product1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    product2 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {5,S}
4  *3 C     0 {1,S} {2,S} {5,D}
5  *4 C     0 {3,S} {4,D}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (8.51e+15,"s^-1"),
        n = 0,
        Ea = (266895,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Cocks, A.T.", "Frey, H.M."], title=u'The Thermal Unimolecular Decomposition of 1,1,2-Trimethylcyclobutane', journal="J. Phys. Chem.", volume="75", pages="""1437""", year="1971", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:42 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 60,
    label = "r00016300",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {5,S} {6,S}
2  *4 C     0 {1,S} {4,S} {7,S}
3  *1 C     0 {1,S} {4,S}
4  *3 C     0 {2,S} {3,S}
5     C     0 {1,S}
6     C     0 {1,S}
7     C     0 {2,S}
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
2  *4 C     0 {1,S} {3,D}
3  *3 C     0 {2,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (5.62e+15,"s^-1"),
        n = 0,
        Ea = (251929,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Cocks, A.T.", "Frey, H.M."], title=u'The Thermal Unimolecular Decomposition of 1,1,2-Trimethylcyclobutane', journal="J. Phys. Chem.", volume="75", pages="""1437""", year="1971", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:42 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 61,
    label = "r00016368",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S} {6,S}
3  *1 C     0 {1,S} {7,S}
4  *4 C     0 {1,S} {7,S}
5     C     0 {1,S}
6     C     0 {2,S}
7  *3 O     0 {3,S} {4,S}
""",
    product1 = 
"""
1     C     0 {2,S} {4,S}
2     C     0 {1,S}
3     C     0 {4,S}
4  *2 C     0 {1,S} {3,S} {5,D}
5  *1 C     0 {4,D}
""",
    product2 = 
"""
1  *4 C     0 {2,D}
2  *3 O     0 {1,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.28e+15,"s^-1"),
        n = 0,
        Ea = (251097,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Clements, A.D.", "Frey, H.M.", "Frey, J.G."], title=u'Thermal Decomposition of 3-Ethyl-3-methyloxetan and 3,3-Diethyloxetan', journal="J. Chem. Soc. Faraday Trans. 1", volume="71", pages="""2485""", year="1975", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:44 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 62,
    label = "r00016567",
    reactant1 = 
"""
1  *2 C     0 {2,S} {4,S} {5,S} {8,S}
2  *1 C     0 {1,S} {3,S} {6,S}
3  *3 C     0 {2,S} {7,S} {8,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {3,S}
8  *4 O     0 {1,S} {3,S}
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
1     C     0 {2,S}
2  *3 C     0 {1,S} {3,D}
3  *4 O     0 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e+14,"s^-1"),
        n = 0,
        Ea = (236962,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Hammonds, P.", "Holbrook, K.A.", "Carless, H.A.J."], title=u'Thermolyses of cis- and trans-2,2,3,4-tetramethyloxetane', journal="J. Chem. Soc. Faraday Trans. 1", volume="80", pages="""691""", year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:49 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 63,
    label = "r00016568",
    reactant1 = 
"""
1  *2 C     0 {2,S} {4,S} {5,S} {8,S}
2  *1 C     0 {1,S} {3,S} {6,S}
3  *3 C     0 {2,S} {7,S} {8,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {2,S}
7     C     0 {3,S}
8  *4 O     0 {1,S} {3,S}
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
1     C     0 {2,S}
2  *3 C     0 {1,S} {3,D}
3  *4 O     0 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.94e+13,"s^-1"),
        n = 0,
        Ea = (228648,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Hammonds, P.", "Holbrook, K.A.", "Carless, H.A.J."], title=u'Thermolyses of cis- and trans-2,2,3,4-tetramethyloxetane', journal="J. Chem. Soc. Faraday Trans. 1", volume="80", pages="""691""", year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:50 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 64,
    label = "r00016669",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {6,S}
2  *1 C     0 {1,S} {4,S} {8,S}
3  *4 C     0 {1,S} {5,S} {8,S}
4     C     0 {2,S}
5     C     0 {3,S}
6     C     0 {1,S} {7,D}
7     C     0 {6,D}
8  *3 O     0 {2,S} {3,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,D}
3  *2 C     0 {2,D} {4,S}
4     C     0 {3,S} {5,D}
5     C     0 {4,D}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *4 C     0 {1,S} {3,D}
3  *3 O     0 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.63e+13,"s^-1"),
        n = 0,
        Ea = (200379,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Carless, H.A.J.", "Maitra, A.K.", "Pottinger, R.", "Frey, H.M."], title=u'Thermal decomposition of cis-2,4-dimethyl-trans-3-vinyloxetan', journal="J. Chem. Soc. Faraday Trans. 1", volume="76", pages="""1849""", year="1980", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:52 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 65,
    label = "r00017015",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {5,S} {6,S}
2  *4 C     0 {1,S} {4,S} {7,S}
3  *1 C     0 {1,S} {4,S}
4  *3 C     0 {2,S} {3,S}
5     C     0 {1,S}
6     C     0 {1,S}
7     C     0 {2,S} {8,D}
8     C     0 {7,D}
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
1     C     0 {2,S} {3,D}
2  *4 C     0 {1,S} {4,D}
3     C     0 {1,D}
4  *3 C     0 {2,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.22e+15,"s^-1"),
        n = 0,
        Ea = (199547,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Chickos, J.S.", "Frey, H.M."], title=u'The thermolysis of 2,2-dimethyl-1-vinylcyclobutane', journal="J. Chem. Soc. Perkin Trans. 2", pages="""365""", year="1987", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:36:10 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

