#!/usr/bin/env python
# encoding: utf-8

name = "Disproportionation"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 1,
    label = "r00001361",
    reactant1 = 
"""
1  *3 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    reactant2 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
1  *3 C     1 {2,S}
2  *2 O     0 {1,S} {3,S}
3  *4 H     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.39e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (79985.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsuboi, T.", "Hashimoto, K."], title=u'Shock Tube Study on Homogeneous Thermal Oxidation of Methanol', journal="Combust. Flame", volume="42", pages="""61""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:30 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 2,
    label = "r00001361",
    reactant1 = 
"""
1  *3 C     1 {2,S}
2  *2 O     0 {1,S} {3,S}
3  *4 H     0 {2,S}
""",
    reactant2 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1  *3 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.8e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:30 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 3,
    label = "r00001361",
    reactant1 = 
"""
1  *3 C     1 {2,S}
2  *2 O     0 {1,S} {3,S}
3  *4 H     0 {2,S}
""",
    reactant2 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1  *3 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20952.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Vandooren, J.", "Van Tiggelen, P.J."], title=u'Experimental Investigation of Methanol Oxidation in Flames: Mechanism and Rate Constants of Elementary Steps', journal="Symp. Int. Combust. Proc.", volume="18", pages="""473""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:30 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 4,
    label = "r00001361",
    reactant1 = 
"""
1  *3 C     1 {2,S}
2  *2 O     0 {1,S} {3,S}
3  *4 H     0 {2,S}
""",
    reactant2 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1  *3 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (25109.7,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Olsson, J.M.", "Olsson, I.B.M.", "Andersson, L.L."], title=u'Lean premixed laminar methanol flames: A computational study', journal="J. Phys. Chem.", volume="91", pages="""4160""", year="1987", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000010.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:30 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 5,
    label = "r00001361",
    reactant1 = 
"""
1  *3 C     1 {2,S}
2  *2 O     0 {1,S} {3,S}
3  *4 H     0 {2,S}
""",
    reactant2 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1  *3 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.56227e-06,"cm^3/(mol*s)"),
        n = 5.94,
        Ea = (-18957,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Grotheer, H.", "Riekert, G.", "Walter, D.", "Just, Th."], title=u'Non-arrhenius behavior of the reaction of hydroxymethyl radicals with molecular oxygen', journal="J. Phys. Chem.", volume="92", pages="""4028""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000012.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:30 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 6,
    label = "r00001361",
    reactant1 = 
"""
1  *3 C     1 {2,S}
2  *2 O     0 {1,S} {3,S}
3  *4 H     0 {2,S}
""",
    reactant2 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1  *3 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.03e+15,"cm^3/(mol*s)"),
        n = 0,
        Ea = (14300.9,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Nesbitt, F.L.", "Payne, W.A.", "Stief, L.J."], title=u'Temperature dependence for the absolute rate constant for the reaction CH_2OH + O_2 \u2192 HO_2 + H_2CO from 215 to 300 K', journal="J. Phys. Chem.", volume="92", pages="""4030""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000013.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:30 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 7,
    label = "r00001361",
    reactant1 = 
"""
1  *3 C     1 {2,S}
2  *2 O     0 {1,S} {3,S}
3  *4 H     0 {2,S}
""",
    reactant2 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1  *3 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.01e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1654.58,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Nesbitt, F.L.", "Payne, W.A.", "Stief, L.J."], title=u'Temperature dependence for the absolute rate constant for the reaction CH_2OH + O_2 \u2192 HO_2 + H_2CO from 215 to 300 K', journal="J. Phys. Chem.", volume="92", pages="""4030""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000014.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:30 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 8,
    label = "r00002190",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    reactant2 = 
"""
1  *4 H     0 {2,S}
2  *1 H     0 {1,S}
""",
    product1 = 
"""
1  *1 H     1
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *3 C     1 {1,S}
3  *4 H     0 {1,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.02e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (285186,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W.", "Hampson, R.F."], title=u'Chemical kinetic data base for combustion chemistry. Part I. Methane and related compounds', journal="J. Phys. Chem. Ref. Data", volume="15", pages="""1087""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:34 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 9,
    label = "r00002190",
    reactant1 = 
"""
1  *1 H     1
""",
    reactant2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *3 C     1 {1,S}
3  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 H     0 {2,S}
2  *4 H     0 {1,S}
""",
    product2 = 
"""
1  *3 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:34 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 10,
    label = "r00005815",
    reactant1 = 
"""
1  *1 C     0 {3,S} {5,S}
2     C     0 {3,S}
3     C     0 {1,S} {2,S} {4,D}
4     C     0 {3,D}
5  *4 H     0 {1,S}
""",
    reactant2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *3 C     0 {1,S} {2,S} {4,D}
4  *2 C     0 {3,D}
""",
    product1 = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S} {4,D}
3  *1 C     1 {2,S}
4     C     0 {2,D}
""",
    product2 = 
"""
1  *2 C     0 {4,S} {5,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *3 C     1 {1,S} {2,S} {3,S}
5  *4 H     0 {1,S}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (2e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (209525,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Douhou, S.", "Perrin, D.", "Martin, R."], title=u"Etude cinetique et modelisaiton de la reaction thermique de l'isobutene vers 800 K. I. Isobutene pur", journal="J. Chim. Phys.", volume="91", pages="""1597-1627""", year="1994", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 11,
    label = "r00005816",
    reactant1 = 
"""
1  *1 C     0 {3,S} {5,S}
2     C     0 {3,S}
3     C     0 {1,S} {2,S} {4,D}
4     C     0 {3,D}
5  *4 H     0 {1,S}
""",
    reactant2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *2 C     0 {1,S} {2,S} {4,D}
4  *3 C     0 {3,D}
""",
    product1 = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S} {4,D}
3  *1 C     1 {2,S}
4     C     0 {2,D}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *3 C     1 {1,S}
5  *4 H     0 {1,S}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (3.9e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (231142,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Douhou, S.", "Perrin, D.", "Martin, R."], title=u"Etude cinetique et modelisaiton de la reaction thermique de l'isobutene vers 800 K. I. Isobutene pur", journal="J. Chim. Phys.", volume="91", pages="""1597-1627""", year="1994", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 12,
    label = "r00009781",
    reactant1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *1 C     1 {1,S} {2,S} {3,S}
""",
    reactant2 = 
"""
1  *2 C     0 {2,D} {3,S} {4,S}
2     C     0 {1,D}
3  *3 C     1 {1,S}
4  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *4 H     0 {1,S}
""",
    product2 = 
"""
1  *3 C     0 {3,D}
2     C     0 {3,D}
3  *2 C     0 {1,D} {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.89046e+13,"cm^3/(mol*s)"),
        n = -0.75,
        Ea = (-548.755,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part V. Propene', journal="J. Phys. Chem. Ref. Data", volume="20", pages="""221-273""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:27 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 13,
    label = "r00009782",
    reactant1 = 
"""
1  *2 C     0 {4,S} {5,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *3 C     1 {1,S} {2,S} {3,S}
5  *4 H     0 {1,S}
""",
    reactant2 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *1 C     1 {1,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {4,S}
2     C     0 {1,S} {3,D}
3     C     0 {2,D}
4  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *3 C     0 {1,S} {2,S} {4,D}
4  *2 C     0 {3,D}
""",
    degeneracy = 9,
    kinetics = Arrhenius(
        A = (4.33211e+14,"cm^3/(mol*s)"),
        n = -0.75,
        Ea = (-548.755,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part V. Propene', journal="J. Phys. Chem. Ref. Data", volume="20", pages="""221-273""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:27 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 14,
    label = "r00009800",
    reactant1 = 
"""
1  *2 C     0 {4,S} {5,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *3 C     1 {1,S} {2,S} {3,S}
5  *4 H     0 {1,S}
""",
    reactant2 = 
"""
1  *1 C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *3 C     0 {1,S} {2,S} {4,D}
4  *2 C     0 {3,D}
""",
    degeneracy = 9,
    kinetics = Arrhenius(
        A = (1.26e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-2494.34,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part 4. Isobutane', journal="J. Phys. Chem. Ref. Data", volume="19", pages="""1-68""", year="1990", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:28 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 15,
    label = "r00009826",
    reactant1 = 
"""
1  *2 C     0 {4,S} {5,S}
2     C     0 {4,S}
3     C     0 {4,S}
4  *3 C     1 {1,S} {2,S} {3,S}
5  *4 H     0 {1,S}
""",
    reactant2 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *3 C     0 {1,S} {2,S} {4,D}
4  *2 C     0 {3,D}
""",
    degeneracy = 18,
    kinetics = Arrhenius(
        A = (8e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (9062.77,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Evans, G.A.", "Walker, R.W."], title=u'Reaction of t-Butyl Radicals with Hydrogen and with Oxygen', journal="J. Chem. Soc. Faraday Trans. 1", volume="75", pages="""1458""", year="1979", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:28 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 16,
    label = "r00010092",
    reactant1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *1 C     1 {1,S}
""",
    reactant2 = 
"""
1  *2 C     0 {2,D} {3,S} {4,S}
2     C     0 {1,D}
3  *3 C     1 {1,S}
4  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {4,S}
2     C     0 {1,S} {3,D}
3     C     0 {2,D}
4  *4 H     0 {1,S}
""",
    product2 = 
"""
1  *3 C     0 {3,D}
2     C     0 {3,D}
3  *2 C     0 {1,D} {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.43e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1097.51,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part V. Propene', journal="J. Phys. Chem. Ref. Data", volume="20", pages="""221-273""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:31 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 17,
    label = "r00010092",
    reactant1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *1 C     1 {1,S}
""",
    reactant2 = 
"""
1  *2 C     0 {2,D} {3,S} {4,S}
2     C     0 {1,D}
3  *3 C     1 {1,S}
4  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {4,S}
2     C     0 {1,S} {3,D}
3     C     0 {2,D}
4  *4 H     0 {1,S}
""",
    product2 = 
"""
1  *3 C     0 {3,D}
2     C     0 {3,D}
3  *2 C     0 {1,D} {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.39e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (39327.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Barbe, P.", "Martin, R.", "Perrin, D.", "Scacchi, G."], title=u'Kinetics and modeling of the thermal reaction of propene at 800 K. Part I. Pure propene', journal="Int. J. Chem. Kinet.", volume="28", pages="""829-847""", year="1996", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:31 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 18,
    label = "r00010094",
    reactant1 = 
"""
1  *2 C     0 {2,D} {3,S} {4,S}
2     C     0 {1,D}
3  *3 C     1 {1,S}
4  *4 H     0 {1,S}
""",
    reactant2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     1 {1,S} {2,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {3,D}
2  *3 C     0 {3,D}
3  *2 C     0 {1,D} {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.58311e+12,"cm^3/(mol*s)"),
        n = -0.35,
        Ea = (-548.755,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part V. Propene', journal="J. Phys. Chem. Ref. Data", volume="20", pages="""221-273""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:31 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 19,
    label = "r00010095",
    reactant1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *1 C     1 {1,S}
""",
    reactant2 = 
"""
1  *2 C     0 {3,S} {4,S}
2     C     0 {3,S}
3  *3 C     1 {1,S} {2,S}
4  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {4,S}
2     C     0 {1,S} {3,D}
3     C     0 {2,D}
4  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *3 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (2.29156e+13,"cm^3/(mol*s)"),
        n = -0.35,
        Ea = (-548.755,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part V. Propene', journal="J. Phys. Chem. Ref. Data", volume="20", pages="""221-273""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:31 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 20,
    label = "r00010095",
    reactant1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *1 C     1 {1,S}
""",
    reactant2 = 
"""
1  *2 C     0 {3,S} {4,S}
2     C     0 {3,S}
3  *3 C     1 {1,S} {2,S}
4  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {4,S}
2     C     0 {1,S} {3,D}
3     C     0 {2,D}
4  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *3 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (5.01e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (19622.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Barbe, P.", "Martin, R.", "Perrin, D.", "Scacchi, G."], title=u'Kinetics and modeling of the thermal reaction of propene at 800 K. Part I. Pure propene', journal="Int. J. Chem. Kinet.", volume="28", pages="""829-847""", year="1996", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:31 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 21,
    label = "r00010095",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S}
2     C     0 {1,S} {3,D}
3     C     0 {2,D}
4  *4 H     0 {1,S}
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *3 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    product1 = 
"""
1     C     0 {2,S} {3,D}
2  *1 C     1 {1,S}
3     C     0 {1,D}
""",
    product2 = 
"""
1  *2 C     0 {3,S} {4,S}
2     C     0 {3,S}
3  *3 C     1 {1,S} {2,S}
4  *4 H     0 {1,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.32e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (202873,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Back, M.H."], title=u'Mechanism of the bimolecular reactions of ethylene and propylene', journal="Int. J. Chem. Kinet.", volume="2", pages="""409-418""", year="1970", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:31 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 22,
    label = "r00010095",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S}
2     C     0 {1,S} {3,D}
3     C     0 {2,D}
4  *4 H     0 {1,S}
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *3 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    product1 = 
"""
1     C     0 {2,S} {3,D}
2  *1 C     1 {1,S}
3     C     0 {1,D}
""",
    product2 = 
"""
1  *2 C     0 {3,S} {4,S}
2     C     0 {3,S}
3  *3 C     1 {1,S} {2,S}
4  *4 H     0 {1,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.51e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (182087,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Simon, M.", "Back, M.H."], title=u'The Kinetics of the Reaction 2C_3H_6 \u2192 C_3H_5 + C_3H_7', journal="Can. J. Chem.", volume="51", pages="""2934""", year="1973", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:31 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 23,
    label = "r00010095",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S}
2     C     0 {1,S} {3,D}
3     C     0 {2,D}
4  *4 H     0 {1,S}
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *3 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    product1 = 
"""
1     C     0 {2,S} {3,D}
2  *1 C     1 {1,S}
3     C     0 {1,D}
""",
    product2 = 
"""
1  *2 C     0 {3,S} {4,S}
2     C     0 {3,S}
3  *3 C     1 {1,S} {2,S}
4  *4 H     0 {1,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (4.88e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (218671,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part V. Propene', journal="J. Phys. Chem. Ref. Data", volume="20", pages="""221-273""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:31 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 24,
    label = "r00010095",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S}
2     C     0 {1,S} {3,D}
3     C     0 {2,D}
4  *4 H     0 {1,S}
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *3 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    product1 = 
"""
1     C     0 {2,S} {3,D}
2  *1 C     1 {1,S}
3     C     0 {1,D}
""",
    product2 = 
"""
1  *2 C     0 {3,S} {4,S}
2     C     0 {3,S}
3  *3 C     1 {1,S} {2,S}
4  *4 H     0 {1,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.57e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (236962,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Barbe, P.", "Martin, R.", "Perrin, D.", "Scacchi, G."], title=u'Kinetics and modeling of the thermal reaction of propene at 800 K. Part I. Pure propene', journal="Int. J. Chem. Kinet.", volume="28", pages="""829-847""", year="1996", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:31 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 25,
    label = "r00010098",
    reactant1 = 
"""
1  *2 C     0 {2,D} {3,S} {4,S}
2     C     0 {1,D}
3  *3 C     1 {1,S}
4  *4 H     0 {1,S}
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *1 C     1 {1,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {3,D}
2  *3 C     0 {3,D}
3  *2 C     0 {1,D} {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.64e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-548.755,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part V. Propene', journal="J. Phys. Chem. Ref. Data", volume="20", pages="""221-273""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:31 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 26,
    label = "r00010098",
    reactant1 = 
"""
1  *1 C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *4 H     0 {1,S}
""",
    reactant2 = 
"""
1  *3 C     0 {3,D}
2     C     0 {3,D}
3  *2 C     0 {1,D} {2,D}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     1 {1,S}
""",
    product2 = 
"""
1  *2 C     0 {2,D} {3,S} {4,S}
2     C     0 {1,D}
3  *3 C     1 {1,S}
4  *4 H     0 {1,S}
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (7.35e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (164627,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Korzun, N.V.", "Trushkova, L.V."], title=u'Kinetic parameters of the reaction C_2H_6 + C_3H_4 \u2192 C_2H_5 + C_3H_5', journal="Kinet. Catal.", volume="26", pages="""1068""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:31 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 27,
    label = "r00010099",
    reactant1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *1 C     1 {1,S}
""",
    reactant2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *3 C     1 {1,S}
3  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {4,S}
2     C     0 {1,S} {3,D}
3     C     0 {2,D}
4  *4 H     0 {1,S}
""",
    product2 = 
"""
1  *3 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.59e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-548.755,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part V. Propene', journal="J. Phys. Chem. Ref. Data", volume="20", pages="""221-273""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:31 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 28,
    label = "r00010099",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    reactant2 = 
"""
1  *1 C     0 {2,S} {4,S}
2     C     0 {1,S} {3,D}
3     C     0 {2,D}
4  *4 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *1 C     1 {1,S}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *3 C     1 {1,S}
3  *4 H     0 {1,S}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (1e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (206199,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Back, M.H."], title=u'Mechanism of the bimolecular reactions of ethylene and propylene', journal="Int. J. Chem. Kinet.", volume="2", pages="""409-418""", year="1970", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:31 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 29,
    label = "r00010099",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    reactant2 = 
"""
1  *1 C     0 {2,S} {4,S}
2     C     0 {1,S} {3,D}
3     C     0 {2,D}
4  *4 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *1 C     1 {1,S}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *3 C     1 {1,S}
3  *4 H     0 {1,S}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (5.78e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (216176,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part V. Propene', journal="J. Phys. Chem. Ref. Data", volume="20", pages="""221-273""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:31 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 30,
    label = "r00010105",
    reactant1 = 
"""
1  *2 C     0 {2,D} {3,S} {4,S}
2     C     0 {1,D}
3  *3 C     1 {1,S}
4  *4 H     0 {1,S}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *1 C     1 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2  *1 C     0 {1,S} {4,S}
3     C     0 {1,S}
4  *4 H     0 {2,S}
""",
    product2 = 
"""
1     C     0 {3,D}
2  *3 C     0 {3,D}
3  *2 C     0 {1,D} {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.23e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-548.755,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part V. Propene', journal="J. Phys. Chem. Ref. Data", volume="20", pages="""221-273""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:31 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 31,
    label = "r00010106",
    reactant1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *1 C     1 {1,S}
""",
    reactant2 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3  *3 C     1 {1,S}
4  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {4,S}
2     C     0 {1,S} {3,D}
3     C     0 {2,D}
4  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *3 C     0 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.45e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-548.755,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part V. Propene', journal="J. Phys. Chem. Ref. Data", volume="20", pages="""221-273""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:31 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 32,
    label = "r00010106",
    reactant1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *1 C     1 {1,S}
""",
    reactant2 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3  *3 C     1 {1,S}
4  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {4,S}
2     C     0 {1,S} {3,D}
3     C     0 {2,D}
4  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *3 C     0 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.75e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (19622.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Barbe, P.", "Martin, R.", "Perrin, D.", "Scacchi, G."], title=u'Kinetics and modeling of the thermal reaction of propene at 800 K. Part I. Pure propene', journal="Int. J. Chem. Kinet.", volume="28", pages="""829-847""", year="1996", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:31 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 33,
    label = "r00010106",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S}
2     C     0 {1,S} {3,D}
3     C     0 {2,D}
4  *4 H     0 {1,S}
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *3 C     0 {2,D}
""",
    product1 = 
"""
1     C     0 {2,S} {3,D}
2  *1 C     1 {1,S}
3     C     0 {1,D}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3  *3 C     1 {1,S}
4  *4 H     0 {1,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.53e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (231142,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part V. Propene', journal="J. Phys. Chem. Ref. Data", volume="20", pages="""221-273""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:31 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 34,
    label = "r00010106",
    reactant1 = 
"""
1  *1 C     0 {2,S} {4,S}
2     C     0 {1,S} {3,D}
3     C     0 {2,D}
4  *4 H     0 {1,S}
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *3 C     0 {2,D}
""",
    product1 = 
"""
1     C     0 {2,S} {3,D}
2  *1 C     1 {1,S}
3     C     0 {1,D}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3  *3 C     1 {1,S}
4  *4 H     0 {1,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (3.89e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (249434,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Barbe, P.", "Martin, R.", "Perrin, D.", "Scacchi, G."], title=u'Kinetics and modeling of the thermal reaction of propene at 800 K. Part I. Pure propene', journal="Int. J. Chem. Kinet.", volume="28", pages="""829-847""", year="1996", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:31 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 35,
    label = "r00010110",
    reactant1 = 
"""
1  *2 C     0 {2,D} {3,S} {4,S}
2     C     0 {1,D}
3  *3 C     1 {1,S}
4  *4 H     0 {1,S}
""",
    reactant2 = 
"""
1  *1 C     1
""",
    product1 = 
"""
1  *1 C     0 {2,S}
2  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {3,D}
2  *3 C     0 {3,D}
3  *2 C     0 {1,D} {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.00875e+12,"cm^3/(mol*s)"),
        n = -0.32,
        Ea = (-548.755,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part V. Propene', journal="J. Phys. Chem. Ref. Data", volume="20", pages="""221-273""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:31 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 36,
    label = "r00010124",
    reactant1 = 
"""
1  *2 C     0 {2,D} {3,S} {4,S}
2     C     0 {1,D}
3  *3 C     1 {1,S}
4  *4 H     0 {1,S}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *1 C     1 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {4,S}
2  *1 C     0 {1,S} {5,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *4 H     0 {2,S}
""",
    product2 = 
"""
1     C     0 {3,D}
2  *3 C     0 {3,D}
3  *2 C     0 {1,D} {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.83e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-548.755,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part V. Propene', journal="J. Phys. Chem. Ref. Data", volume="20", pages="""221-273""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:32 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 37,
    label = "r00010125",
    reactant1 = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *1 C     1 {1,S}
""",
    reactant2 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *3 C     1 {1,S}
5  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {4,S}
2     C     0 {1,S} {3,D}
3     C     0 {2,D}
4  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *2 C     0 {1,S} {2,S} {4,D}
4  *3 C     0 {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.83e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-548.755,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part V. Propene', journal="J. Phys. Chem. Ref. Data", volume="20", pages="""221-273""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:32 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 38,
    label = "r00010133",
    reactant1 = 
"""
1  *2 C     0 {2,D} {3,S} {4,S}
2     C     0 {1,D}
3  *3 C     1 {1,S}
4  *4 H     0 {1,S}
""",
    reactant2 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {3,D}
2  *3 C     0 {3,D}
3  *2 C     0 {1,D} {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.21e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (56704.7,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part V. Propene', journal="J. Phys. Chem. Ref. Data", volume="20", pages="""221-273""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:32 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 39,
    label = "r00010168",
    reactant1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     1 {1,S} {2,S}
""",
    reactant2 = 
"""
1  *2 C     0 {3,S} {4,S}
2     C     0 {3,S}
3  *3 C     1 {1,S} {2,S}
4  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *3 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (3.01e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-207.862,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Arrowsmith, P.", "Kirsch, L.J."], title=u'Mutual Reaction of Isopropyl Radicals', journal="J. Chem. Soc. Faraday Trans. 1", volume="74", pages="""3016""", year="1978", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000013.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:33 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 40,
    label = "r00010195",
    reactant1 = 
"""
1  *1 C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *4 H     0 {1,S}
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *3 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    product1 = 
"""
1     C     0 {2,D}
2  *1 C     1 {1,D}
""",
    product2 = 
"""
1  *2 C     0 {3,S} {4,S}
2     C     0 {3,S}
3  *3 C     1 {1,S} {2,S}
4  *4 H     0 {1,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (9.12e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (264400,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Back, M.H."], title=u'Mechanism of the bimolecular reactions of ethylene and propylene', journal="Int. J. Chem. Kinet.", volume="2", pages="""409-418""", year="1970", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:33 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 41,
    label = "r00010195",
    reactant1 = 
"""
1  *1 C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *4 H     0 {1,S}
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *3 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    product1 = 
"""
1     C     0 {2,D}
2  *1 C     1 {1,D}
""",
    product2 = 
"""
1  *2 C     0 {3,S} {4,S}
2     C     0 {3,S}
3  *3 C     1 {1,S} {2,S}
4  *4 H     0 {1,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (7.22205e+15,"cm^3/(mol*s)"),
        n = -0.65,
        Ea = (308467,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part V. Propene', journal="J. Phys. Chem. Ref. Data", volume="20", pages="""221-273""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:33 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 42,
    label = "r00010209",
    reactant1 = 
"""
1  *2 C     0 {3,S} {4,S}
2     C     0 {3,S}
3  *3 C     1 {1,S} {2,S}
4  *4 H     0 {1,S}
""",
    reactant2 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *3 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (1e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (12471.7,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Warnatz, J."], year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 43,
    label = "r00010209",
    reactant1 = 
"""
1  *2 C     0 {3,S} {4,S}
2     C     0 {3,S}
3  *3 C     1 {1,S} {2,S}
4  *4 H     0 {1,S}
""",
    reactant2 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *3 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (2.75e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-8979.63,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Gulati, S.K.", "Walker, R.W."], title=u'Arrhenius parameters for the reaction i-C_3H_7 + O_2 \u2192 C_3H_6 + HO_2', journal="J. Chem. Soc. Faraday Trans. 2", volume="84", pages="""401""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 44,
    label = "r00010209",
    reactant1 = 
"""
1  *2 C     0 {3,S} {4,S}
2     C     0 {3,S}
3  *3 C     1 {1,S} {2,S}
4  *4 H     0 {1,S}
""",
    reactant2 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *3 C     0 {1,S} {3,D}
3  *2 C     0 {2,D}
""",
    degeneracy = 12,
    kinetics = Arrhenius(
        A = (0.00111215,"cm^3/(mol*s)"),
        n = -3.02,
        Ea = (10476.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["DeSain, J.D.", "Klippenstein, S.J.", "Miller, J.A.", "Taatjes, C.A."], title=u'Measurements, Theory, and Modeling of OH Formation in Ethyl + O_2 and Propyl + O_2 Reactions', journal="J. Phys. Chem. A", volume="107", pages="""4415-4427""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 45,
    label = "r00010240",
    reactant1 = 
"""
1     C     0 {2,S}
2  *1 C     1 {1,S}
""",
    reactant2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *3 C     1 {1,S}
3  *4 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {2,S}
2  *1 C     0 {1,S} {3,S}
3  *4 H     0 {2,S}
""",
    product2 = 
"""
1  *3 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.65e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (3342.42,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Ivin, K.J.", "Steacie, E.W.R."], title=u'The disproportionation and combination of ethyl radicals: The photolysis of mercury diethyl', journal="Proc. R. Soc. London A", volume="208", pages="""25""", year="1951", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:34 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 46,
    label = "r00010524",
    reactant1 = 
"""
1  *1 C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *4 H     0 {1,S}
""",
    reactant2 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *3 C     0 {2,D}
""",
    product1 = 
"""
1     C     0 {2,D}
2  *1 C     1 {1,D}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3  *3 C     1 {1,S}
4  *4 H     0 {1,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (6.03e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (315950,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W."], title=u'Chemical kinetic data base for combustion chemistry. Part V. Propene', journal="J. Phys. Chem. Ref. Data", volume="20", pages="""221-273""", year="1991", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 47,
    label = "r00010543",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3  *3 C     1 {1,S}
4  *4 H     0 {1,S}
""",
    reactant2 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *3 C     0 {2,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (21035.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Warnatz, J."], year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 48,
    label = "r00010543",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3  *3 C     1 {1,S}
4  *4 H     0 {1,S}
""",
    reactant2 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *3 C     0 {2,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (6.14961e-08,"cm^3/(mol*s)"),
        n = -1.63,
        Ea = (14300.9,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["DeSain, J.D.", "Klippenstein, S.J.", "Miller, J.A.", "Taatjes, C.A."], title=u'Measurements, Theory, and Modeling of OH Formation in Ethyl + O_2 and Propyl + O_2 Reactions', journal="J. Phys. Chem. A", volume="107", pages="""4415-4427""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000010.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 49,
    label = "r00010580",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *3 O     1 {1,S}
3  *4 H     0 {1,S}
""",
    reactant2 = 
"""
1  *1 O     1
""",
    product1 = 
"""
1  *1 O     0 {2,S}
2  *4 H     0 {1,S}
""",
    product2 = 
"""
1  *2 C     0 {2,D}
2  *3 O     0 {1,D}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 50,
    label = "r00010588",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *3 O     0 {1,D}
""",
    reactant2 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *4 H     0 {1,S}
3  *3 O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.16e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (16712.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Barker, J.R.", "Benson, S.W.", "Golden, D.M."], title=u'The Decomposition of Dimethyl Peroxide and the Rate Constant for CH_3O + O_2 \u2192 CH_2O +HO_2', journal="Int. J. Chem. Kinet.", volume="9", pages="""31""", year="1977", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000010.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 51,
    label = "r00010588",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *3 O     0 {1,D}
""",
    reactant2 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *4 H     0 {1,S}
3  *3 O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (18790.7,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Batt, L.", "Rattray, G.N."], title=u'The Reaction of Methoxy Radicals with Nitric Oxide and Nitrogen Dioxide', journal="Int. J. Chem. Kinet.", volume="11", pages="""1183""", year="1979", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000011.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 52,
    label = "r00010588",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *3 O     0 {1,D}
""",
    reactant2 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *4 H     0 {1,S}
3  *3 O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20121,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Batt, L.", "Robinson, G.N."], title=u'Reaction of Methoxy Radicals with Oxygen. I. Using Dimethyl Peroxide as a Thermal Source of Methoxy Radicals', journal="Int. J. Chem. Kinet.", volume="11", pages="""1045""", year="1979", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000012.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 53,
    label = "r00010588",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *3 O     0 {1,D}
""",
    reactant2 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *4 H     0 {1,S}
3  *3 O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.59e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (11224.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Cox, R.A.", "Derwent, R.G.", "Kearsey, S.V.", "Batt, L.", "Partick, K.G."], title=u'Photolysis of Methyl Nitrite: Kinetics of the Reaction of the Methoxy Radical with O_2', journal="J. Photochem.", volume="13", pages="""149""", year="1980", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000013.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 54,
    label = "r00010588",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *3 O     0 {1,D}
""",
    reactant2 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *4 H     0 {1,S}
3  *3 O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.06e+21,"cm^3/(mol*s)"),
        n = 0,
        Ea = (136357,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Moshkina, R.I.", "Polyak, S.S.", "Sokolova, N.A.", "Masterovoi, I.F.", "Nalbandyan, A.B."], title=u'Study of the ethane oxidation reaction by the kinetic tracer method', journal="Int. J. Chem. Kinet.", volume="12", pages="""315""", year="1980", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000014.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 55,
    label = "r00010588",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *3 O     0 {1,D}
""",
    reactant2 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *4 H     0 {1,S}
3  *3 O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.3e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (10892,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Gutman, D.", "Sanders, N.", "Butler, J.E."], title=u'Kinetic of the Reactions of Methoxy and Ethoxy Radicals with Oxygen', journal="J. Phys. Chem.", volume="86", pages="""66""", year="1982", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000019.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 56,
    label = "r00010588",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *3 O     0 {1,D}
""",
    reactant2 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *4 H     0 {1,S}
3  *3 O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (30015.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Warnatz, J."], year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000020.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 57,
    label = "r00010588",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *3 O     0 {1,D}
""",
    reactant2 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *4 H     0 {1,S}
3  *3 O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.31e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8314.47,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Lorenz, K.", "Rhasa, D.", "Zellner, R.", "Fritz, B."], title=u'Laser photolysis - LIF kinetic studies of the reactions of CH_3O and CH_2CHO with O_2 between 300 and 500 K', journal="Ber. Bunsenges. Phys. Chem.", volume="89", pages="""341""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000021.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 58,
    label = "r00010588",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *3 O     0 {1,D}
""",
    reactant2 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *4 H     0 {1,S}
3  *3 O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.62e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (10892,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W.", "Hampson, R.F."], title=u'Chemical kinetic data base for combustion chemistry. Part I. Methane and related compounds', journal="J. Phys. Chem. Ref. Data", volume="15", pages="""1087""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000022.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 59,
    label = "r00010588",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *3 O     0 {1,D}
""",
    reactant2 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *4 H     0 {1,S}
3  *3 O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.37596e-19,"cm^3/(mol*s)"),
        n = 9.5,
        Ea = (-23031.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Wantuck, P.J.", "Oldenborg, R.C.", "Baughcum, S.L.", "Winn, K.R."], title=u'Removal rate constant measurements for CH_3O by O_2 over the 298-973 K range', journal="J. Phys. Chem.", volume="91", pages="""4653""", year="1987", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000023.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 60,
    label = "r00010588",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *3 O     0 {1,D}
""",
    reactant2 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *4 H     0 {1,S}
3  *3 O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.31e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8314.47,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Zellner, R."], title=u'Recent advances in free radical kinetics of oxygenated hydrocarbon radicals', journal="J. Chim. Phys.", volume="84", pages="""403-407""", year="1987", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000024.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 61,
    label = "r00010588",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *3 O     0 {1,D}
""",
    reactant2 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *4 H     0 {1,S}
3  *3 O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.13e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (10725.7,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Heicklen, J."], title=u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals', journal="Adv. Photochem.", volume="14", pages="""177""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000025.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 62,
    label = "r00010588",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *3 O     0 {1,D}
""",
    reactant2 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *4 H     0 {1,S}
3  *3 O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.3e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (10892,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Zaslonko, I.S.", "Mukoseev, Yu.K.", "Tyurin, A.N."], title=u'Reactions of CH_3O radicals in shock waves', journal="Kinet. Catal.", volume="29", pages="""244""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000026.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 63,
    label = "r00010588",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *3 O     0 {1,D}
""",
    reactant2 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *4 H     0 {1,S}
3  *3 O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (15049.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Ballod, A.P.", "Poroikova, A.I.", "Titarchuk, T.A.", "Khabarov, V.N."], title=u'Determination of the rate constant of the reaction of methoxyl radicals with molecular oxygen', journal="Kinet. Catal.", volume="30", pages="""483""", year="1989", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000028.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 64,
    label = "r00010588",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *3 O     0 {1,D}
""",
    reactant2 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *4 H     0 {1,S}
3  *3 O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.61e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8896.49,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Esser, C.", "Frank, P.", "Just, Th.", "Kerr, J.A.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."], title=u'Evaluated kinetic data for combustion modelling', journal="J. Phys. Chem. Ref. Data", volume="21", pages="""411-429""", year="1992", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000031.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 65,
    label = "r00010588",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *3 O     0 {1,D}
""",
    reactant2 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *4 H     0 {1,S}
3  *3 O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.17e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (7316.74,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Frank, P.", "Hayman, G.", "Just, Th.", "Kerr, J.A.", "Murrells, T.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."], title=u'Evaluated kinetic data for combusion modelling. Supplement I', journal="J. Phys. Chem. Ref. Data", volume="23", pages="""847-1033""", year="1994", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000032.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 66,
    label = "r00010588",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *3 O     0 {1,D}
""",
    reactant2 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *4 H     0 {1,S}
3  *3 O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.34e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8979.63,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Hampson, R.F., Jr.", "Kerr, J.A.", "Rossi, M.J.", "Troe, J."], title=u'Evaluated kinetic, photochemical and heterogeneous data for atmospheric chemistry: supplement V, IUPAC subcommittee on gas kinetic data evaluation for atmospheric chemistry', journal="J. Phys. Chem. Ref. Data", volume="26", pages="""521-1011""", year="1997", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000034.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 67,
    label = "r00010588",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *3 O     0 {1,D}
""",
    reactant2 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *4 H     0 {1,S}
3  *3 O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.34e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8979.63,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Atkinson, R."], title=u'Atmospheric reactions of alkoxy and \u03b2-hydroxyalkoxy radicals', journal="Int. J. Chem. Kinet.", volume="29", pages="""99-111""", year="1997", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000035.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 68,
    label = "r00010588",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *3 O     0 {1,D}
""",
    reactant2 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *4 H     0 {1,S}
3  *3 O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (7483.02,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["DeMore, W.B.", "Sander, S.P.", "Golden, D.M.", "Hampson, R.F.", "Kurylo, M.J.", "Howard, C.J.", "Ravishankara, A.R.", "Kolb, C.E.", "Molina, M.J."], title=u'Chemical kinetics and photochemical data for use in stratospheric modeling. Evaluation number 12', journal="JPL Publication 97-4", pages="""1-266""", year="1997", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000036.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 69,
    label = "r00010588",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *3 O     0 {1,D}
""",
    reactant2 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *4 H     0 {1,S}
3  *3 O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.2e-14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8979.63,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Crowley, J.N.", "Hampson, R.F, Jr.", "Kerr, J.A.", "Rossi, M.J.", "Troe, J."], title=u'Summary of Evaluated Kinetic and Photochemical Data for Atmospheric Chemistry', journal="Not in System", pages="""1-56""", year="2001", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000037.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 70,
    label = "r00010588",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *3 O     1 {1,S}
3  *4 H     0 {1,S}
""",
    reactant2 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1  *2 C     0 {2,D}
2  *3 O     0 {1,D}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (4.28e-13,"cm^3/(mol*s)"),
        n = 7.6,
        Ea = (-3530,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000038.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 71,
    label = "r00010601",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *3 O     1 {1,S}
3  *4 H     0 {1,S}
""",
    reactant2 = 
"""
1  *1 H     1
""",
    product1 = 
"""
1  *1 H     0 {2,S}
2  *4 H     0 {1,S}
""",
    product2 = 
"""
1  *2 C     0 {2,D}
2  *3 O     0 {1,D}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 72,
    label = "r00010641",
    reactant1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,S} {4,S}
3  *3 O     1 {2,S}
4  *4 H     0 {2,S}
""",
    reactant2 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *3 O     0 {2,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.72e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (3142.87,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Gutman, D.", "Sanders, N.", "Butler, J.E."], title=u'Kinetic of the Reactions of Methoxy and Ethoxy Radicals with Oxygen', journal="J. Phys. Chem.", volume="86", pages="""66""", year="1982", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 73,
    label = "r00010641",
    reactant1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,S} {4,S}
3  *3 O     1 {2,S}
4  *4 H     0 {2,S}
""",
    reactant2 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *3 O     0 {2,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.81e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (7682.57,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Zabarnick, S.", "Heicklen, J."], title=u'Reactions of alkoxy radicals with O_2. I. C_2H_5O radicals', journal="Int. J. Chem. Kinet.", volume="17", pages="""455""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 74,
    label = "r00010641",
    reactant1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,S} {4,S}
3  *3 O     1 {2,S}
4  *4 H     0 {2,S}
""",
    reactant2 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *3 O     0 {2,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (9.77e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (6651.58,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Heicklen, J."], title=u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals', journal="Adv. Photochem.", volume="14", pages="""177""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 75,
    label = "r00010641",
    reactant1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,S} {4,S}
3  *3 O     1 {2,S}
4  *4 H     0 {2,S}
""",
    reactant2 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *3 O     0 {2,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (4.28e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (4589.59,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Hartmann, D.", "Karthauser, J.", "Sawerysyn, J.P.", "Zellner, R."], title=u'Kinetics and HO_2 product yield of the reaction C_2H_5O + O_2 between 295 and 411 K', journal="Ber. Bunsenges. Phys. Chem.", volume="94", pages="""639""", year="1990", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:37 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 76,
    label = "r00010641",
    reactant1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,S} {4,S}
3  *3 O     1 {2,S}
4  *4 H     0 {2,S}
""",
    reactant2 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *3 O     0 {2,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (6.03e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (6901.01,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Esser, C.", "Frank, P.", "Just, Th.", "Kerr, J.A.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."], title=u'Evaluated kinetic data for combustion modelling', journal="J. Phys. Chem. Ref. Data", volume="21", pages="""411-429""", year="1992", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000009.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:37 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 77,
    label = "r00010641",
    reactant1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,S} {4,S}
3  *3 O     1 {2,S}
4  *4 H     0 {2,S}
""",
    reactant2 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *3 O     0 {2,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.61e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (4572.96,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Hampson, R.F., Jr.", "Kerr, J.A.", "Rossi, M.J.", "Troe, J."], title=u'Evaluated kinetic, photochemical and heterogeneous data for atmospheric chemistry: supplement V, IUPAC subcommittee on gas kinetic data evaluation for atmospheric chemistry', journal="J. Phys. Chem. Ref. Data", volume="26", pages="""521-1011""", year="1997", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000011.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:37 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 78,
    label = "r00010641",
    reactant1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,S} {4,S}
3  *3 O     1 {2,S}
4  *4 H     0 {2,S}
""",
    reactant2 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *3 O     0 {2,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.61e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (4572.96,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Atkinson, R."], title=u'Atmospheric reactions of alkoxy and \u03b2-hydroxyalkoxy radicals', journal="Int. J. Chem. Kinet.", volume="29", pages="""99-111""", year="1997", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000012.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:37 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 79,
    label = "r00010641",
    reactant1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,S} {4,S}
3  *3 O     1 {2,S}
4  *4 H     0 {2,S}
""",
    reactant2 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *3 O     0 {2,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.79e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (4572.96,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["DeMore, W.B.", "Sander, S.P.", "Golden, D.M.", "Hampson, R.F.", "Kurylo, M.J.", "Howard, C.J.", "Ravishankara, A.R.", "Kolb, C.E.", "Molina, M.J."], title=u'Chemical kinetics and photochemical data for use in stratospheric modeling. Evaluation number 12', journal="JPL Publication 97-4", pages="""1-266""", year="1997", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000013.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:37 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 80,
    label = "r00010641",
    reactant1 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,S} {4,S}
3  *3 O     1 {2,S}
4  *4 H     0 {2,S}
""",
    reactant2 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *2 C     0 {1,S} {3,D}
3  *3 O     0 {2,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (6e-14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (4572.96,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Crowley, J.N.", "Hampson, R.F, Jr.", "Kerr, J.A.", "Rossi, M.J.", "Troe, J."], title=u'Summary of Evaluated Kinetic and Photochemical Data for Atmospheric Chemistry', journal="Not in System", pages="""1-56""", year="2001", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000014.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:37 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 81,
    label = "r00011080",
    reactant1 = 
"""
1     C     0 {2,S}
2  *3 C     1 {1,S} {3,S}
3  *2 O     0 {2,S} {4,S}
4  *4 H     0 {3,S}
""",
    reactant2 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S}
2  *3 C     0 {1,S} {3,D}
3  *2 O     0 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (23280.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Natarajan, K.", "Bhaskaran, K.A."], title=u'An Experimental and Analytical Investigation of High Temperature Ignition of Ethanol', journal="Proc. Int. Symp. Shock Tubes Waves", volume="13", pages="""834""", year="1982", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:42 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 82,
    label = "r00011216",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4  *1 C     1 {2,S}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S} {5,S}
3     C     0 {1,S}
4  *3 C     1 {2,S}
5  *4 H     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4  *1 C     0 {2,S} {5,S}
5  *4 H     0 {4,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *2 C     0 {1,S} {4,D}
4  *3 C     0 {3,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.98e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (5437.66,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Kerr, J.A.", "Trotman-Dickenson, A.F."], title=u'The reactions of alkyl radicals. Part III. n-Butyl radicals from the photolysis of n-Valeraldehyde', journal="J. Chem. Soc.", pages="""1602""", year="1960", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:46 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 83,
    label = "r00011296",
    reactant1 = 
"""
1  *3 C     1 {2,S}
2  *2 O     0 {1,S} {3,S}
3  *4 H     0 {2,S}
""",
    reactant2 = 
"""
1  *1 O     1
""",
    product1 = 
"""
1  *1 O     0 {2,S}
2  *4 H     0 {1,S}
""",
    product2 = 
"""
1  *3 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:46 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 84,
    label = "r00011312",
    reactant1 = 
"""
1  *3 C     1 {2,S}
2  *2 O     0 {1,S} {3,S}
3  *4 H     0 {2,S}
""",
    reactant2 = 
"""
1  *1 H     1
""",
    product1 = 
"""
1  *1 H     0 {2,S}
2  *4 H     0 {1,S}
""",
    product2 = 
"""
1  *3 C     0 {2,D}
2  *2 O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:46 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 85,
    label = "r00011408",
    reactant1 = 
"""
1  *1 C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *4 H     0 {1,S}
""",
    reactant2 = 
"""
1  *2 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    product1 = 
"""
1     C     0 {2,D}
2  *1 C     1 {1,D}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *3 C     1 {1,S}
3  *4 H     0 {1,S}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.82e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (267726,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Back, M.H."], title=u'Mechanism of the bimolecular reactions of ethylene and propylene', journal="Int. J. Chem. Kinet.", volume="2", pages="""409-418""", year="1970", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
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
    index = 86,
    label = "r00011408",
    reactant1 = 
"""
1  *1 C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *4 H     0 {1,S}
""",
    reactant2 = 
"""
1  *2 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    product1 = 
"""
1     C     0 {2,D}
2  *1 C     1 {1,D}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *3 C     1 {1,S}
3  *4 H     0 {1,S}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.58e+16,"cm^3/(mol*s)"),
        n = 0,
        Ea = (280198,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Ayranci, G.", "Back, M.H."], title=u'Kinetics of the Bimolecular Initiation Process in the Thermal Reactions of Ethylene', journal="Int. J. Chem. Kinet.", volume="13", pages="""897""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
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
    index = 87,
    label = "r00011408",
    reactant1 = 
"""
1  *1 C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *4 H     0 {1,S}
""",
    reactant2 = 
"""
1  *2 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    product1 = 
"""
1     C     0 {2,D}
2  *1 C     1 {1,D}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *3 C     1 {1,S}
3  *4 H     0 {1,S}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (1.86e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (268557,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Ayranci, G.", "Back, M.H."], title=u'Kinetics of the reaction: 2C_2H_4 \u2192 C_2H_5 + C_2H_3. Heat of formation of the vinyl radical', journal="Int. J. Chem. Kinet.", volume="15", pages="""83""", year="1983", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
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
    index = 88,
    label = "r00011408",
    reactant1 = 
"""
1  *1 C     0 {2,D} {3,S}
2     C     0 {1,D}
3  *4 H     0 {1,S}
""",
    reactant2 = 
"""
1  *2 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    product1 = 
"""
1     C     0 {2,D}
2  *1 C     1 {1,D}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *3 C     1 {1,S}
3  *4 H     0 {1,S}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (4.82e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (299321,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W.", "Hampson, R.F."], title=u'Chemical kinetic data base for combustion chemistry. Part I. Methane and related compounds', journal="J. Phys. Chem. Ref. Data", volume="15", pages="""1087""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000008.xml"),
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
    index = 89,
    label = "r00012573",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *3 O     1 {1,S}
5  *4 H     0 {1,S}
""",
    reactant2 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *2 C     0 {1,S} {2,S} {4,D}
4  *3 O     0 {3,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (9.1e+09,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1629.64,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Balla, R.J.", "Nelson, H.H.", "McDonald, J.R."], title=u'Kinetics of the reactions of isopropoxy radicals with NO, NO_2, and O_2', journal="Chem. Phys.", volume="99", pages="""323""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:54 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 90,
    label = "r00012573",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *3 O     1 {1,S}
5  *4 H     0 {1,S}
""",
    reactant2 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *2 C     0 {1,S} {2,S} {4,D}
4  *3 O     0 {3,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.9e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (6651.58,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Heicklen, J."], title=u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals', journal="Adv. Photochem.", volume="14", pages="""177""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:54 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 91,
    label = "r00012573",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *3 O     1 {1,S}
5  *4 H     0 {1,S}
""",
    reactant2 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *2 C     0 {1,S} {2,S} {4,D}
4  *3 O     0 {3,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (9.04e+09,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1662.89,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Hampson, R.F., Jr.", "Kerr, J.A.", "Rossi, M.J.", "Troe, J."], title=u'Evaluated kinetic, photochemical and heterogeneous data for atmospheric chemistry: supplement V, IUPAC subcommittee on gas kinetic data evaluation for atmospheric chemistry', journal="J. Phys. Chem. Ref. Data", volume="26", pages="""521-1011""", year="1997", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:54 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 92,
    label = "r00012573",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *3 O     1 {1,S}
5  *4 H     0 {1,S}
""",
    reactant2 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *2 C     0 {1,S} {2,S} {4,D}
4  *3 O     0 {3,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (9.04e+09,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1662.89,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Atkinson, R."], title=u'Atmospheric reactions of alkoxy and \u03b2-hydroxyalkoxy radicals', journal="Int. J. Chem. Kinet.", volume="29", pages="""99-111""", year="1997", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:54 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 93,
    label = "r00012573",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *3 O     1 {1,S}
5  *4 H     0 {1,S}
""",
    reactant2 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *2 C     0 {1,S} {2,S} {4,D}
4  *3 O     0 {3,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.4e-14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1746.04,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Crowley, J.N.", "Hampson, R.F, Jr.", "Kerr, J.A.", "Rossi, M.J.", "Troe, J."], title=u'Summary of Evaluated Kinetic and Photochemical Data for Atmospheric Chemistry', journal="Not in System", pages="""1-56""", year="2001", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:54 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 94,
    label = "r00012779",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *3 C     1 {1,S}
5  *4 H     0 {1,S}
""",
    reactant2 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *2 C     0 {1,S} {2,S} {4,D}
4  *3 C     0 {3,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (26606.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baker, R.R.", "Baldwin, R.R.", "Walker, R.W."], title=u'Addition of i-Butane to Slowly Reacting Mixtures of Hydrogen and Oxygen at 480^o C', journal="J. Chem. Soc. Faraday Trans. 1", volume="74", pages="""2229""", year="1978", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
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
    index = 95,
    label = "r00013871",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    reactant2 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *3 C     1 {1,S}
3  *4 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.17e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (5770.24,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baker, R.R.", "Baldwin, R.R.", "Walker, R.W."], title=u'The Use of the H_2 + O_2 Reaction in Determining the Velocity Constants of Elementary Reactions in Hydrocarbon Oxidation', journal="Symp. Int. Combust. Proc.", volume="13", pages="""291""", year="1971", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:14 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 96,
    label = "r00013871",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    reactant2 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *3 C     1 {1,S}
3  *4 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.16e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20952.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Cooke, D.F.", "Williams, A."], title=u'Shock-tube studies of the ignition and combustion of ethane and slightly rich methane mixtures with oxygen', journal="Symp. Int. Combust. Proc.", volume="13", pages="""757""", year="1971", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000011.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:14 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 97,
    label = "r00013871",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    reactant2 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *3 C     1 {1,S}
3  *4 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.51e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (16213.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baldwin, R.R.", "Pickering, I.A.", "Walker, R.W."], title=u'Reactions of Ethyl Radicals with Oxygen over the Temperature Range 400-540^oC', journal="J. Chem. Soc. Faraday Trans. 1", volume="76", pages="""2374""", year="1980", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000012.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:14 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 98,
    label = "r00013871",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    reactant2 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *3 C     1 {1,S}
3  *4 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20869.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Warnatz, J."], year="1984", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000016.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:14 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 99,
    label = "r00013871",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    reactant2 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *3 C     1 {1,S}
3  *4 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.43e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (16213.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tsang, W.", "Hampson, R.F."], title=u'Chemical kinetic data base for combustion chemistry. Part I. Methane and related compounds', journal="J. Phys. Chem. Ref. Data", volume="15", pages="""1087""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000017.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:14 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 100,
    label = "r00013871",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    reactant2 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *3 C     1 {1,S}
3  *4 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.12e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-6302.37,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["McAdam, K.G.", "Walker, R.W."], title=u'Arrhenius Parameters for the reaction C_2H_5 + O_2 \u2192 C_2H_4 + HO_2', journal="J. Chem. Soc. Faraday Trans. 2", volume="83", pages="""1509""", year="1987", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000018.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:14 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 101,
    label = "r00013871",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    reactant2 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *3 C     1 {1,S}
3  *4 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.56256e+19,"cm^3/(mol*s)"),
        n = -2.77,
        Ea = (8272.9,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Bozzelli, J.W.", "Dean, A.M."], title=u'Chemical activation analysis of the reaction of C_2H_5 with O_2', journal="J. Phys. Chem.", volume="94", pages="""3313""", year="1990", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000020.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:14 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 102,
    label = "r00013871",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    reactant2 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *3 C     1 {1,S}
3  *4 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.02e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-9145.92,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baulch, D.L.", "Cobos, C.J.", "Cox, R.A.", "Esser, C.", "Frank, P.", "Just, Th.", "Kerr, J.A.", "Pilling, M.J.", "Troe, J.", "Walker, R.W.", "Warnatz, J."], title=u'Evaluated kinetic data for combustion modelling', journal="J. Phys. Chem. Ref. Data", volume="21", pages="""411-429""", year="1992", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000026.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:14 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 103,
    label = "r00013871",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    reactant2 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *3 C     1 {1,S}
3  *4 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (8.55e+06,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-21201.9,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dobis, O.", "Benson, S.W."], title=u'Reaction of the ethyl radical with oxygen at millitorr pressures at 243-368 K and a study of the Cl + HO_2, ethyl + HO_2, and HO_2 + HO_2 reactions', journal="J. Am. Chem. Soc.", volume="115", pages="""8798-8809""", year="1993", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000027.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:14 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 104,
    label = "r00013871",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    reactant2 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *3 C     1 {1,S}
3  *4 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.67e-14,"cm^3/(mol*s)"),
        n = -0.772,
        Ea = (38.4976,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Clifford, E.P.", "Farrell, J.T.", "DeSain, J.D.", "Taatjes, C.A."], title=u'Infrared Frequency-Modulation Probing of Product Formation in Alkyl + O_2 Reactions: I. The Reaction of C_2H_5 with O_2 between 295 and 698 K', journal="J. Phys. Chem. A", volume="104", pages="""11549-11560""", year="2000", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000032.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:14 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 105,
    label = "r00013871",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    reactant2 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *3 C     1 {1,S}
3  *4 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.85e-12,"cm^3/(mol*s)"),
        n = 6.53,
        Ea = (-13779.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Miller, J.A.", "Klippenstein, S.J."], title=u'The Reaction Between Ethyl and Molecular Oxygen II. Further Analysis', journal="Int J. Chem. Kinet.", volume="33", pages="""654-668""", year="2001", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000033.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:14 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 106,
    label = "r00013871",
    reactant1 = 
"""
1  *2 C     0 {2,D}
2  *3 C     0 {1,D}
""",
    reactant2 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *3 C     1 {1,S}
3  *4 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.81727e-08,"cm^3/(mol*s)"),
        n = -1.87,
        Ea = (5878.33,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["DeSain, J.D.", "Klippenstein, S.J.", "Miller, J.A.", "Taatjes, C.A."], title=u'Measurements, Theory, and Modeling of OH Formation in Ethyl + O_2 and Propyl + O_2 Reactions', journal="J. Phys. Chem. A", volume="107", pages="""4415-4427""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000034.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:14 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 107,
    label = "r00013871",
    reactant1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *3 C     1 {1,S}
3  *4 H     0 {1,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1  *3 C     0 {2,D}
2  *2 C     0 {1,D}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (8.4e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (3875,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000035.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:14 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 108,
    label = "r00013958",
    reactant1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *2 C     0 {1,S} {4,S} {5,S}
4  *3 O     1 {3,S}
5  *4 H     0 {3,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *2 C     0 {1,S} {4,D}
4  *3 O     0 {3,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.75e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (7308.42,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Zabarnick, S.", "Heicklen, J."], title=u'The reactions of alkoxy radicals with O_2. II. n-C_3H_7O radicals', journal="Int. J. Chem. Kinet.", volume="17", pages="""477""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:14 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 109,
    label = "r00013958",
    reactant1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *2 C     0 {1,S} {4,S} {5,S}
4  *3 O     1 {3,S}
5  *4 H     0 {3,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *2 C     0 {1,S} {4,D}
4  *3 O     0 {3,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.95e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8281.21,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Heicklen, J."], title=u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals', journal="Adv. Photochem.", volume="14", pages="""177""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:14 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 110,
    label = "r00013958",
    reactant1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *2 C     0 {1,S} {4,S} {5,S}
4  *3 O     1 {3,S}
5  *4 H     0 {3,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3  *2 C     0 {1,S} {4,D}
4  *3 O     0 {3,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.4e-14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (914.592,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Crowley, J.N.", "Hampson, R.F, Jr.", "Kerr, J.A.", "Rossi, M.J.", "Troe, J."], title=u'Summary of Evaluated Kinetic and Photochemical Data for Atmospheric Chemistry', journal="Not in System", pages="""1-56""", year="2001", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:14 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 111,
    label = "r00013972",
    reactant1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4  *2 C     0 {2,S} {5,S} {6,S}
5  *3 O     1 {4,S}
6  *4 H     0 {4,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4  *2 C     0 {2,S} {5,D}
5  *3 O     0 {4,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (4.5e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (9811.08,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Morabito, P.", "Heicklen, J."], title=u'The reactions of alkoxyl radicals with O_2. IV. n-C_4H_9O radicals', journal="Bull. Chem. Soc. Jpn.", volume="60", pages="""2641""", year="1987", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:14 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 112,
    label = "r00013972",
    reactant1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4  *2 C     0 {2,S} {5,S} {6,S}
5  *3 O     1 {4,S}
6  *4 H     0 {4,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4  *2 C     0 {2,S} {5,D}
5  *3 O     0 {4,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.95e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8281.21,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Heicklen, J."], title=u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals', journal="Adv. Photochem.", volume="14", pages="""177""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:14 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 113,
    label = "r00013972",
    reactant1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4  *2 C     0 {2,S} {5,S} {6,S}
5  *3 O     1 {4,S}
6  *4 H     0 {4,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4  *2 C     0 {2,S} {5,D}
5  *3 O     0 {4,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (6e-14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (4572.96,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Atkinson, R.", "Baulch, D.L.", "Cox, R.A.", "Crowley, J.N.", "Hampson, R.F, Jr.", "Kerr, J.A.", "Rossi, M.J.", "Troe, J."], title=u'Summary of Evaluated Kinetic and Photochemical Data for Atmospheric Chemistry', journal="Not in System", pages="""1-56""", year="2001", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:14 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 114,
    label = "r00013994",
    reactant1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *2 C     0 {1,S} {5,S} {6,S}
5  *3 O     1 {4,S}
6  *4 H     0 {4,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *2 C     0 {1,S} {5,D}
5  *3 O     0 {4,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.93e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (6950.9,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Zabarnick, S.", "Heicklen, J."], title=u'Reactions of alkoxy radicals with O_2. III. i-C_4H_9O radicals', journal="Int. J. Chem. Kinet.", volume="17", pages="""503""", year="1985", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:15 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 115,
    label = "r00013994",
    reactant1 = 
"""
1  *1 O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *2 C     0 {1,S} {5,S} {6,S}
5  *3 O     1 {4,S}
6  *4 H     0 {4,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S} {3,S}
2     O     1 {1,S}
3  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *2 C     0 {1,S} {5,D}
5  *3 O     0 {4,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.95e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8281.21,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Heicklen, J."], title=u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals', journal="Adv. Photochem.", volume="14", pages="""177""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:15 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 116,
    label = "r00017290",
    reactant1 = 
"""
1  *1 H     1
""",
    reactant2 = 
"""
1     C     0 {2,D}
2  *2 C     0 {1,D} {3,S} {4,S}
3  *3 O     1 {2,S}
4  *4 H     0 {2,S}
""",
    product1 = 
"""
1  *4 H     0 {2,S}
2  *1 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {2,D}
2  *2 C     0 {1,D} {3,D}
3  *3 O     0 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:36:14 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 117,
    label = "r00017303",
    reactant1 = 
"""
1  *1 O     1
""",
    reactant2 = 
"""
1     C     0 {2,D}
2  *2 C     0 {1,D} {3,S} {4,S}
3  *3 O     1 {2,S}
4  *4 H     0 {2,S}
""",
    product1 = 
"""
1  *1 O     0 {2,S}
2  *4 H     0 {1,S}
""",
    product2 = 
"""
1     C     0 {2,D}
2  *2 C     0 {1,D} {3,D}
3  *3 O     0 {2,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(authors=["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."], year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:36:14 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

