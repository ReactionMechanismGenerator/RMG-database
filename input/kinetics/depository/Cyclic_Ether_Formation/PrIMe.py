#!/usr/bin/env python
# encoding: utf-8

name = "Cyclic_Ether_Formation"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 1,
    label = "r00016872",
    reactant1 = 
"""
1  *4 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *1 C     1 {1,S}
6  *2 O     0 {2,S} {7,S}
7  *3 O     0 {6,S}
""",
    product1 = 
"""
1  *4 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S} {6,S}
3  *1 C     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6  *2 O     0 {2,S} {3,S}
""",
    product2 = 
"""
1  *3 O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+11,"s^-1"),
        n = 0,
        Ea = (73001.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baldwin, R.R.", "Hisham, M.W.M.", "Walker, R.W."], title=u'Arrhenius parameters of elementary reactions involved in the oxidation of neopentane', journal="J. Chem. Soc. Faraday Trans. 1", volume="78", pages="""1615""", year="1982", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
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
    index = 2,
    label = "r00016872",
    reactant1 = 
"""
1  *4 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *1 C     1 {1,S}
6  *2 O     0 {2,S} {7,S}
7  *3 O     0 {6,S}
""",
    product1 = 
"""
1  *4 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S} {6,S}
3  *1 C     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6  *2 O     0 {2,S} {3,S}
""",
    product2 = 
"""
1  *3 O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.05e+35,"s^-1"),
        n = -7.46,
        Ea = (396327,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Sun, H.", "Bozzelli, J.W."], title=u'Thermochemical and kinetic analysis on the reactions of neopentyl and hydroperoxy-neopentyl radicals with oxygen: Part I.  OH and initial stable HC product formation', journal="J. Phys. Chem. A", volume="108", pages="""1694-1711""", year="2004", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
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
    index = 3,
    label = "r00016872",
    reactant1 = 
"""
1  *4 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *1 C     1 {1,S}
6  *2 O     0 {2,S} {7,S}
7  *3 O     0 {6,S}
""",
    product1 = 
"""
1  *4 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S} {6,S}
3  *1 C     0 {1,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6  *2 O     0 {2,S} {3,S}
""",
    product2 = 
"""
1  *3 O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.78e+17,"s^-1"),
        n = -2.45,
        Ea = (189960,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Sun, H.", "Bozzelli, J.W."], title=u'Thermochemical and kinetic analysis on the reactions of neopentyl and hydroperoxy-neopentyl radicals with oxygen: Part I.  OH and initial stable HC product formation', journal="J. Phys. Chem. A", volume="108", pages="""1694-1711""", year="2004", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:36:03 2011","jwallen","action","""jwallen added this entry to the database."""),
    ],
)

