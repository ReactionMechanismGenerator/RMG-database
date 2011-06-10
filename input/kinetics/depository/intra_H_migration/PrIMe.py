#!/usr/bin/env python
# encoding: utf-8

name = "intra_H_migration"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 1,
    label = "r00000033",
    reactant1 = 
"""
1  *2 C     0 {2,S} {5,S} {6,S} {8,S}
2  *5 C     0 {1,S} {3,S}
3     C     0 {2,S} {4,S}
4  *4 C     0 {3,S} {7,S} {9,S}
5     C     0 {1,S}
6     C     0 {1,S}
7     C     0 {4,S}
8  *3 H     0 {1,S}
9  *1 O     1 {4,S}
""",
    product1 = 
"""
1  *5 C     0 {2,S} {4,S} {8,S}
2     C     0 {1,S} {3,S}
3  *4 C     0 {2,S} {7,S}
4     C     0 {1,S}
5     C     0 {7,S}
6     C     0 {7,S}
7  *1 C     1 {3,S} {5,S} {6,S}
8  *2 O     0 {1,S} {9,S}
9  *3 H     0 {8,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.9e+11,"s^-1"),
        n = 0,
        Ea = (61.1335,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Mereau, R.", "Rayez, M.T.", "Caralp, F.", "Rayez, J.C."], title=u'Isomerization reactions of alkoxy radicals: theoretical study and structure-activity relationships', journal="Phys. Chem. Chem. Phys.", volume="5", pages="""4828-4833""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:23 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 2,
    label = "r00000034",
    reactant1 = 
"""
1  *4 C     0 {2,S} {5,S} {6,S} {8,S}
2     C     0 {1,S} {3,S}
3  *5 C     0 {2,S} {4,S}
4  *2 C     0 {3,S} {7,S} {9,S}
5     C     0 {1,S}
6     C     0 {1,S}
7     C     0 {4,S}
8  *1 O     1 {1,S}
9  *3 H     0 {4,S}
""",
    product1 = 
"""
1  *5 C     0 {2,S} {4,S} {5,S} {8,S}
2     C     0 {1,S} {3,S}
3  *4 C     0 {2,S} {7,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {7,S}
7  *1 C     1 {3,S} {6,S}
8  *2 O     0 {1,S} {9,S}
9  *3 H     0 {8,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.7e+12,"s^-1"),
        n = 0,
        Ea = (115.658,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Mereau, R.", "Rayez, M.T.", "Caralp, F.", "Rayez, J.C."], title=u'Isomerization reactions of alkoxy radicals: theoretical study and structure-activity relationships', journal="Phys. Chem. Chem. Phys.", volume="5", pages="""4828-4833""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:23 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 3,
    label = "r00000087",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {7,S}
2  *5 C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S} {6,S}
5     C     0 {3,S}
6  *4 C     0 {4,S} {8,S}
7  *3 H     0 {1,S}
8  *1 O     1 {6,S}
""",
    product1 = 
"""
1     C     0 {2,S} {4,S}
2  *4 C     0 {1,S} {6,S}
3     C     0 {5,S} {6,S}
4  *5 C     0 {1,S} {7,S}
5     C     0 {3,S}
6  *1 C     1 {2,S} {3,S}
7  *2 O     0 {4,S} {8,S}
8  *3 H     0 {7,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.4e+12,"s^-1"),
        n = 0,
        Ea = (127.224,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Mereau, R.", "Rayez, M.T.", "Caralp, F.", "Rayez, J.C."], title=u'Isomerization reactions of alkoxy radicals: theoretical study and structure-activity relationships', journal="Phys. Chem. Chem. Phys.", volume="5", pages="""4828-4833""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:24 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 4,
    label = "r00000088",
    reactant1 = 
"""
1  *5 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S} {6,S}
3     C     0 {1,S} {5,S}
4     C     0 {2,S}
5  *4 C     0 {3,S} {7,S}
6  *3 H     0 {2,S}
7  *1 O     1 {5,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2  *4 C     0 {1,S} {5,S}
3  *5 C     0 {1,S} {6,S}
4     C     0 {5,S}
5  *1 C     1 {2,S} {4,S}
6  *2 O     0 {3,S} {7,S}
7  *3 H     0 {6,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.7e+12,"s^-1"),
        n = 0,
        Ea = (130.528,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Mereau, R.", "Rayez, M.T.", "Caralp, F.", "Rayez, J.C."], title=u'Isomerization reactions of alkoxy radicals: theoretical study and structure-activity relationships', journal="Phys. Chem. Chem. Phys.", volume="5", pages="""4828-4833""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:24 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 5,
    label = "r00000089",
    reactant1 = 
"""
1     C     0 {2,S} {3,S} {4,S}
2  *5 C     0 {1,S} {5,S}
3     C     0 {1,S}
4  *4 C     0 {1,S} {6,S}
5  *2 C     0 {2,S} {7,S}
6  *1 O     1 {4,S}
7  *3 H     0 {5,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {4,S}
2  *4 C     0 {1,S} {5,S}
3  *5 C     0 {1,S} {6,S}
4     C     0 {1,S}
5  *1 C     1 {2,S}
6  *2 O     0 {3,S} {7,S}
7  *3 H     0 {6,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (3.1e+12,"s^-1"),
        n = 0,
        Ea = (160.269,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Mereau, R.", "Rayez, M.T.", "Caralp, F.", "Rayez, J.C."], title=u'Isomerization reactions of alkoxy radicals: theoretical study and structure-activity relationships', journal="Phys. Chem. Chem. Phys.", volume="5", pages="""4828-4833""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:24 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 6,
    label = "r00000090",
    reactant1 = 
"""
1  *2 C     0 {3,S} {5,S} {6,S} {10,S}
2  *4 C     0 {4,S} {7,S} {8,S} {9,S}
3  *5 C     0 {1,S} {4,S}
4     C     0 {2,S} {3,S}
5     C     0 {1,S}
6     C     0 {1,S}
7     C     0 {2,S}
8     C     0 {2,S}
9  *1 O     1 {2,S}
10 *3 H     0 {1,S}
""",
    product1 = 
"""
1  *5 C     0 {2,S} {4,S} {5,S} {9,S}
2     C     0 {1,S} {3,S}
3  *4 C     0 {2,S} {8,S}
4     C     0 {1,S}
5     C     0 {1,S}
6     C     0 {8,S}
7     C     0 {8,S}
8  *1 C     1 {3,S} {6,S} {7,S}
9  *2 O     0 {1,S} {10,S}
10 *3 H     0 {9,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.6e+11,"s^-1"),
        n = 0,
        Ea = (64.438,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Mereau, R.", "Rayez, M.T.", "Caralp, F.", "Rayez, J.C."], title=u'Isomerization reactions of alkoxy radicals: theoretical study and structure-activity relationships', journal="Phys. Chem. Chem. Phys.", volume="5", pages="""4828-4833""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:24 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 7,
    label = "r00000091",
    reactant1 = 
"""
1  *5 C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *2 C     0 {1,S} {5,S} {8,S}
4  *4 C     0 {2,S} {6,S} {7,S}
5     C     0 {3,S}
6     C     0 {4,S}
7  *1 O     1 {4,S}
8  *3 H     0 {3,S}
""",
    product1 = 
"""
1  *5 C     0 {2,S} {4,S} {7,S}
2     C     0 {1,S} {3,S}
3  *4 C     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {6,S}
6  *1 C     1 {3,S} {5,S}
7  *2 O     0 {1,S} {8,S}
8  *3 H     0 {7,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.5e+12,"s^-1"),
        n = 0,
        Ea = (122.267,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Mereau, R.", "Rayez, M.T.", "Caralp, F.", "Rayez, J.C."], title=u'Isomerization reactions of alkoxy radicals: theoretical study and structure-activity relationships', journal="Phys. Chem. Chem. Phys.", volume="5", pages="""4828-4833""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:24 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 8,
    label = "r00000092",
    reactant1 = 
"""
1  *2 C     0 {2,S} {4,S} {5,S} {7,S}
2  *5 C     0 {1,S} {3,S}
3     C     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6  *4 C     0 {3,S} {8,S}
7  *3 H     0 {1,S}
8  *1 O     1 {6,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2  *4 C     0 {1,S} {6,S}
3  *5 C     0 {1,S} {7,S}
4     C     0 {6,S}
5     C     0 {6,S}
6  *1 C     1 {2,S} {4,S} {5,S}
7  *2 O     0 {3,S} {8,S}
8  *3 H     0 {7,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.7e+11,"s^-1"),
        n = 0,
        Ea = (82.6129,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Mereau, R.", "Rayez, M.T.", "Caralp, F.", "Rayez, J.C."], title=u'Isomerization reactions of alkoxy radicals: theoretical study and structure-activity relationships', journal="Phys. Chem. Chem. Phys.", volume="5", pages="""4828-4833""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:24 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 9,
    label = "r00000093",
    reactant1 = 
"""
1  *4 C     0 {2,S} {4,S} {5,S} {7,S}
2     C     0 {1,S} {3,S}
3  *5 C     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6  *2 C     0 {3,S} {8,S}
7  *1 O     1 {1,S}
8  *3 H     0 {6,S}
""",
    product1 = 
"""
1  *5 C     0 {2,S} {4,S} {5,S} {7,S}
2     C     0 {1,S} {3,S}
3  *4 C     0 {2,S} {6,S}
4     C     0 {1,S}
5     C     0 {1,S}
6  *1 C     1 {3,S}
7  *2 O     0 {1,S} {8,S}
8  *3 H     0 {7,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.1e+12,"s^-1"),
        n = 0,
        Ea = (148.703,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Mereau, R.", "Rayez, M.T.", "Caralp, F.", "Rayez, J.C."], title=u'Isomerization reactions of alkoxy radicals: theoretical study and structure-activity relationships', journal="Phys. Chem. Chem. Phys.", volume="5", pages="""4828-4833""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:24 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 10,
    label = "r00000094",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2  *4 C     0 {1,S} {4,S} {7,S}
3  *5 C     0 {1,S} {5,S}
4     C     0 {2,S} {6,S}
5  *2 C     0 {3,S} {8,S}
6     C     0 {4,S}
7  *1 O     1 {2,S}
8  *3 H     0 {5,S}
""",
    product1 = 
"""
1  *5 C     0 {2,S} {3,S} {7,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4  *4 C     0 {2,S} {6,S}
5     C     0 {3,S}
6  *1 C     1 {4,S}
7  *2 O     0 {1,S} {8,S}
8  *3 H     0 {7,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.3e+12,"s^-1"),
        n = 0,
        Ea = (158.617,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Mereau, R.", "Rayez, M.T.", "Caralp, F.", "Rayez, J.C."], title=u'Isomerization reactions of alkoxy radicals: theoretical study and structure-activity relationships', journal="Phys. Chem. Chem. Phys.", volume="5", pages="""4828-4833""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:33:24 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 11,
    label = "r00010491",
    reactant1 = 
"""
1     C     0 {2,S} {3,S} {7,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S} {6,S}
4  *2 C     0 {5,S} {6,S} {8,S}
5  *5 C     0 {2,S} {4,S}
6     C     0 {3,S} {4,S}
7  *4 O     0 {1,S} {9,S}
8  *3 H     0 {4,S}
9  *1 O     1 {7,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S} {7,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4  *4 C     0 {2,S} {6,S}
5     C     0 {3,S} {6,S}
6  *1 C     1 {4,S} {5,S}
7  *5 O     0 {1,S} {8,S}
8  *2 O     0 {7,S} {9,S}
9  *3 H     0 {8,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.51e+11,"s^-1"),
        n = 0,
        Ea = (1858.79,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Handford-Styring, S.M.", "Walker, R.W."], title=u'Arrhenius Parameters for the Reaction HO_2 + Cyclohexane Between 673 and 773 K, and for H Atom Transfer in Cyclohexylperoxy Radicals', journal="Phys. Chem. Chem. Phys.", volume="3", pages="""2043-2052""", year="2001", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:35 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 12,
    label = "r00010492",
    reactant1 = 
"""
1     C     0 {2,S} {3,S} {7,S}
2  *5 C     0 {1,S} {5,S}
3     C     0 {1,S} {6,S}
4     C     0 {5,S} {6,S}
5  *2 C     0 {2,S} {4,S} {8,S}
6     C     0 {3,S} {4,S}
7  *4 O     0 {1,S} {9,S}
8  *3 H     0 {5,S}
9  *1 O     1 {7,S}
""",
    product1 = 
"""
1     C     0 {2,S} {4,S} {7,S}
2     C     0 {1,S} {3,S}
3     C     0 {2,S} {5,S}
4  *4 C     0 {1,S} {6,S}
5     C     0 {3,S} {6,S}
6  *1 C     1 {4,S} {5,S}
7  *5 O     0 {1,S} {8,S}
8  *2 O     0 {7,S} {9,S}
9  *3 H     0 {8,S}
""",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (2.57e+12,"s^-1"),
        n = 0,
        Ea = (2040.54,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Handford-Styring, S.M.", "Walker, R.W."], title=u'Arrhenius Parameters for the Reaction HO_2 + Cyclohexane Between 673 and 773 K, and for H Atom Transfer in Cyclohexylperoxy Radicals', journal="Phys. Chem. Chem. Phys.", volume="3", pages="""2043-2052""", year="2001", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:35 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 13,
    label = "r00010493",
    reactant1 = 
"""
1  *5 C     0 {2,S} {3,S} {7,S}
2  *2 C     0 {1,S} {5,S} {8,S}
3     C     0 {1,S} {6,S}
4     C     0 {5,S} {6,S}
5     C     0 {2,S} {4,S}
6     C     0 {3,S} {4,S}
7  *4 O     0 {1,S} {9,S}
8  *3 H     0 {2,S}
9  *1 O     1 {7,S}
""",
    product1 = 
"""
1  *4 C     0 {2,S} {6,S} {7,S}
2     C     0 {1,S} {3,S}
3     C     0 {2,S} {4,S}
4     C     0 {3,S} {5,S}
5     C     0 {4,S} {6,S}
6  *1 C     1 {1,S} {5,S}
7  *5 O     0 {1,S} {8,S}
8  *2 O     0 {7,S} {9,S}
9  *3 H     0 {8,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.47e+12,"s^-1"),
        n = 0,
        Ea = (2242.11,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Handford-Styring, S.M.", "Walker, R.W."], title=u'Arrhenius Parameters for the Reaction HO_2 + Cyclohexane Between 673 and 773 K, and for H Atom Transfer in Cyclohexylperoxy Radicals', journal="Phys. Chem. Chem. Phys.", volume="3", pages="""2043-2052""", year="2001", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:35 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 14,
    label = "r00010505",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S}
2     C     0 {1,S}
3  *1 C     1 {1,S}
4  *3 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S}
2  *2 C     0 {3,S} {4,S}
3  *1 C     1 {1,S} {2,S}
4  *3 H     0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.56e+10,"s^-1"),
        n = 0.88,
        Ea = (616.292,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Matheu, D.M.", "Green, W.H.", "Grenda, J.M."], title=u'Capturing pressure-dependence in automated mechanism generation: Reactions through cycloalkyl intermediates', journal="Int. J. Chem. Kinet.", volume="35", pages="""95-119""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:35 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 15,
    label = "r00010565",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *1 O     1 {1,S}
3  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *1 C     1 {2,S}
2  *2 O     0 {1,S} {3,S}
3  *3 H     0 {2,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1e+13,"s^-1"),
        n = 0,
        Ea = (108920,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Batt, L.", "Burrows, J.P.", "Robinson, G.N."], title=u'On the Isomerisation of the Methoxy Radical: Relevance to Atmospheric Chemistry and Combustion', journal="Chem. Phys. Lett.", volume="78", pages="""467""", year="1981", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
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
    index = 16,
    label = "r00010707",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {5,S}
2     C     0 {1,S} {4,D}
3  *1 C     1 {1,S}
4     C     0 {2,D}
5  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,S} {5,S}
2  *1 C     1 {1,S} {3,S}
3     C     0 {2,S} {4,D}
4     C     0 {3,D}
5  *3 H     0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.56e+10,"s^-1"),
        n = 0.88,
        Ea = (489.068,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Matheu, D.M.", "Green, W.H.", "Grenda, J.M."], title=u'Capturing pressure-dependence in automated mechanism generation: Reactions through cycloalkyl intermediates', journal="Int. J. Chem. Kinet.", volume="35", pages="""95-119""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
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
    index = 17,
    label = "r00011212",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S} {5,S}
3     C     0 {1,S}
4  *1 C     1 {2,S}
5  *3 H     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S} {4,S}
2     C     0 {1,S}
3  *2 C     0 {4,S} {5,S}
4  *1 C     1 {1,S} {3,S}
5  *3 H     0 {3,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (5.2e+14,"s^-1"),
        n = 0,
        Ea = (171278,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Lin, M.C.", "Back, M.H."], title=u'The thermal decomposition of ethane. Part III. Secondary reactions', journal="Can. J. Chem.", volume="44", pages="""2369""", year="1966", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
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
    index = 18,
    label = "r00011212",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S} {5,S}
3     C     0 {1,S}
4  *1 C     1 {2,S}
5  *3 H     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S} {4,S}
2     C     0 {1,S}
3  *2 C     0 {4,S} {5,S}
4  *1 C     1 {1,S} {3,S}
5  *3 H     0 {3,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.32e+12,"s^-1"),
        n = 0,
        Ea = (137189,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Gierczak, T.", "Gawlowski, J.", "Niedzielski, J."], title=u'Isomerization of chemically activated secondary butyl radical', journal="React. Kinet. Catal. Lett.", volume="36", pages="""435""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
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
    index = 19,
    label = "r00011212",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S} {5,S}
3     C     0 {1,S}
4  *1 C     1 {2,S}
5  *3 H     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S} {4,S}
2     C     0 {1,S}
3  *2 C     0 {4,S} {5,S}
4  *1 C     1 {1,S} {3,S}
5  *3 H     0 {3,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.56e+10,"s^-1"),
        n = 0.88,
        Ea = (616.292,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Matheu, D.M.", "Green, W.H.", "Grenda, J.M."], title=u'Capturing pressure-dependence in automated mechanism generation: Reactions through cycloalkyl intermediates', journal="Int. J. Chem. Kinet.", volume="35", pages="""95-119""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
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
    index = 20,
    label = "r00011212",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S} {5,S}
3     C     0 {1,S}
4  *1 C     1 {2,S}
5  *3 H     0 {2,S}
""",
    product1 = 
"""
1     C     0 {2,S} {4,S}
2     C     0 {1,S}
3  *2 C     0 {4,S} {5,S}
4  *1 C     1 {1,S} {3,S}
5  *3 H     0 {3,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.8e+10,"s^-1"),
        n = 0.67,
        Ea = (604.726,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Matheu, D.M.", "Green, W.H.", "Grenda, J.M."], title=u'Capturing pressure-dependence in automated mechanism generation: Reactions through cycloalkyl intermediates', journal="Int. J. Chem. Kinet.", volume="35", pages="""95-119""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
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
    index = 21,
    label = "r00011212",
    reactant1 = 
"""
1     C     0 {2,S} {4,S}
2     C     0 {1,S}
3  *2 C     0 {4,S} {5,S}
4  *1 C     1 {1,S} {3,S}
5  *3 H     0 {3,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S} {5,S}
3     C     0 {1,S}
4  *1 C     1 {2,S}
5  *3 H     0 {2,S}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (2e+12,"s^-1"),
        n = 0,
        Ea = (153818,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Gierczak, T.", "Gawlowski, J.", "Niedzielski, J."], title=u'Isomerization of chemically activated secondary butyl radical', journal="React. Kinet. Catal. Lett.", volume="36", pages="""435""", year="1988", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
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
    index = 22,
    label = "r00011467",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *2 C     0 {1,S} {5,S} {6,S}
4     C     0 {2,S}
5  *1 C     1 {3,S}
6  *3 H     0 {3,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4  *2 C     0 {5,S} {6,S}
5  *1 C     1 {2,S} {4,S}
6  *3 H     0 {4,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.4e+07,"s^-1"),
        n = 0,
        Ea = (45147.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Endrenyi, L.", "Le Roy, D.J."], title=u'The isomerization of n-pentyl and 4-oxo-1-pentyl radicals in the gas phase', journal="J. Phys. Chem.", volume="70", pages="""4081""", year="1966", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
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
    index = 23,
    label = "r00011467",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *2 C     0 {1,S} {5,S} {6,S}
4     C     0 {2,S}
5  *1 C     1 {3,S}
6  *3 H     0 {3,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4  *2 C     0 {5,S} {6,S}
5  *1 C     1 {2,S} {4,S}
6  *3 H     0 {4,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.3e+08,"s^-1"),
        n = 0,
        Ea = (63190,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Watkins, K.W."], title=u'Photolysis of n-Pentylazomethane Vapor. Reactions of the n-Pentyl Radical', journal="J. Am. Chem. Soc.", volume="93", pages="""6355""", year="1971", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
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
    index = 24,
    label = "r00011467",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *2 C     0 {1,S} {5,S} {6,S}
4     C     0 {2,S}
5  *1 C     1 {3,S}
6  *3 H     0 {3,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4  *2 C     0 {5,S} {6,S}
5  *1 C     1 {2,S} {4,S}
6  *3 H     0 {4,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (5.01e+11,"s^-1"),
        n = 0,
        Ea = (88133.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Watkins, K.W."], title=u'On the rate constant for n-pentyl radical isomerization', journal="Can. J. Chem.", volume="50", pages="""3738""", year="1972", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
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
    index = 25,
    label = "r00011467",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *2 C     0 {1,S} {5,S} {6,S}
4     C     0 {2,S}
5  *1 C     1 {3,S}
6  *3 H     0 {3,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4  *2 C     0 {5,S} {6,S}
5  *1 C     1 {2,S} {4,S}
6  *3 H     0 {4,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.2e+11,"s^-1"),
        n = 0,
        Ea = (83976.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Marshall, R.M."], title=u'The rate constant for the intramolecular isomerization of pentyl radicals', journal="Int. J. Chem. Kinet.", volume="22", pages="""935""", year="1990", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
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
    index = 26,
    label = "r00011467",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *2 C     0 {1,S} {5,S} {6,S}
4     C     0 {2,S}
5  *1 C     1 {3,S}
6  *3 H     0 {3,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4  *2 C     0 {5,S} {6,S}
5  *1 C     1 {2,S} {4,S}
6  *3 H     0 {4,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (9.12e+11,"s^-1"),
        n = 0,
        Ea = (98110.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Marshall, R.M."], title=u'The rate constant for the intramolecular isomerization of pentyl radicals', journal="Int. J. Chem. Kinet.", volume="22", pages="""935""", year="1990", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
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
    index = 27,
    label = "r00011467",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *2 C     0 {1,S} {5,S} {6,S}
4     C     0 {2,S}
5  *1 C     1 {3,S}
6  *3 H     0 {3,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4  *2 C     0 {5,S} {6,S}
5  *1 C     1 {2,S} {4,S}
6  *3 H     0 {4,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (6.05e+10,"s^-1"),
        n = 0.846,
        Ea = (81731.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Yamauchi, N.", "Miyoshi, A.", "Kosaka, K.", "Koshi, M.", "Matsui, H."], title=u'Thermal decomposition and isomerization processes of alkyl radicals', journal="J. Phys. Chem. A", volume="103", pages="""2723-2733""", year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
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
    index = 28,
    label = "r00011467",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *2 C     0 {1,S} {5,S} {6,S}
4     C     0 {2,S}
5  *1 C     1 {3,S}
6  *3 H     0 {3,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4  *2 C     0 {5,S} {6,S}
5  *1 C     1 {2,S} {4,S}
6  *3 H     0 {4,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.56e+10,"s^-1"),
        n = 0.88,
        Ea = (616.292,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Matheu, D.M.", "Green, W.H.", "Grenda, J.M."], title=u'Capturing pressure-dependence in automated mechanism generation: Reactions through cycloalkyl intermediates', journal="Int. J. Chem. Kinet.", volume="35", pages="""95-119""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000007.xml"),
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
    index = 29,
    label = "r00011467",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *2 C     0 {1,S} {5,S} {6,S}
4     C     0 {2,S}
5  *1 C     1 {3,S}
6  *3 H     0 {3,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {5,S}
3     C     0 {1,S}
4  *2 C     0 {5,S} {6,S}
5  *1 C     1 {2,S} {4,S}
6  *3 H     0 {4,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (7.85e+11,"s^-1"),
        n = -0.12,
        Ea = (340.365,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Matheu, D.M.", "Green, W.H.", "Grenda, J.M."], title=u'Capturing pressure-dependence in automated mechanism generation: Reactions through cycloalkyl intermediates', journal="Int. J. Chem. Kinet.", volume="35", pages="""95-119""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000008.xml"),
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
    index = 30,
    label = "r00011468",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {6,S}
2     C     0 {1,S} {4,S}
3  *4 C     0 {1,S} {5,S}
4     C     0 {2,S}
5  *1 C     1 {3,S}
6  *3 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {3,S} {5,S}
2  *4 C     0 {4,S} {5,S}
3     C     0 {1,S}
4  *2 C     0 {2,S} {6,S}
5  *1 C     1 {1,S} {2,S}
6  *3 H     0 {4,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.8e+10,"s^-1"),
        n = 0.67,
        Ea = (604.726,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Matheu, D.M.", "Green, W.H.", "Grenda, J.M."], title=u'Capturing pressure-dependence in automated mechanism generation: Reactions through cycloalkyl intermediates', journal="Int. J. Chem. Kinet.", volume="35", pages="""95-119""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
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
    index = 31,
    label = "r00011474",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4  *2 C     0 {2,S} {6,S} {7,S}
5     C     0 {3,S}
6  *1 C     1 {4,S}
7  *3 H     0 {4,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {6,S}
4     C     0 {2,S}
5  *2 C     0 {6,S} {7,S}
6  *1 C     1 {3,S} {5,S}
7  *3 H     0 {5,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2e+07,"s^-1"),
        n = 0,
        Ea = (34754.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Watkins, K.W.", "Ostreko, L.A."], title=u'Isomerization of n-hexyl radicals in the gas phase', journal="J. Phys. Chem.", volume="73", pages="""2080""", year="1969", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
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
    index = 32,
    label = "r00011474",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4  *2 C     0 {2,S} {6,S} {7,S}
5     C     0 {3,S}
6  *1 C     1 {4,S}
7  *3 H     0 {4,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {6,S}
4     C     0 {2,S}
5  *2 C     0 {6,S} {7,S}
6  *1 C     1 {3,S} {5,S}
7  *3 H     0 {5,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.16e+09,"s^-1"),
        n = 0,
        Ea = (48556.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dobe, S.", "Berces, T.", "Reti, F.", "Marta, F."], title=u'Isomerization of n-hexyl and s-octyl radicals by 1,5 and 1,4 intramolecular hydrogen atom transfer reactions', journal="Int. J. Chem. Kinet.", volume="19", pages="""895""", year="1987", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
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
    index = 33,
    label = "r00011474",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4  *2 C     0 {2,S} {6,S} {7,S}
5     C     0 {3,S}
6  *1 C     1 {4,S}
7  *3 H     0 {4,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {6,S}
4     C     0 {2,S}
5  *2 C     0 {6,S} {7,S}
6  *1 C     1 {3,S} {5,S}
7  *3 H     0 {5,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.16e+10,"s^-1"),
        n = 0,
        Ea = (71171.9,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Imbert, F.E.", "Marshall, R.M."], title=u'The mechanism and rate parameters for the pyrolysis of n-hexane in the range 723-823 K', journal="Int. J. Chem. Kinet.", volume="19", pages="""81""", year="1987", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
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
    index = 34,
    label = "r00011474",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4  *2 C     0 {2,S} {6,S} {7,S}
5     C     0 {3,S}
6  *1 C     1 {4,S}
7  *3 H     0 {4,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {6,S}
4     C     0 {2,S}
5  *2 C     0 {6,S} {7,S}
6  *1 C     1 {3,S} {5,S}
7  *3 H     0 {5,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (7.23e+09,"s^-1"),
        n = 0.823,
        Ea = (52048.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Yamauchi, N.", "Miyoshi, A.", "Kosaka, K.", "Koshi, M.", "Matsui, H."], title=u'Thermal decomposition and isomerization processes of alkyl radicals', journal="J. Phys. Chem. A", volume="103", pages="""2723-2733""", year="1999", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000004.xml"),
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
    label = "r00011474",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {6,S}
4     C     0 {2,S}
5  *2 C     0 {6,S} {7,S}
6  *1 C     1 {3,S} {5,S}
7  *3 H     0 {5,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4  *2 C     0 {2,S} {6,S} {7,S}
5     C     0 {3,S}
6  *1 C     1 {4,S}
7  *3 H     0 {4,S}
""",
    degeneracy = 6,
    kinetics = Arrhenius(
        A = (2.51e+10,"s^-1"),
        n = 0,
        Ea = (88133.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Imbert, F.E.", "Marshall, R.M."], title=u'The mechanism and rate parameters for the pyrolysis of n-hexane in the range 723-823 K', journal="Int. J. Chem. Kinet.", volume="19", pages="""81""", year="1987", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
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
    index = 36,
    label = "r00011969",
    reactant1 = 
"""
1     C     0 {2,S} {4,S}
2     C     0 {1,S} {3,S}
3  *2 C     0 {2,S} {5,S} {9,S}
4     C     0 {1,S} {6,S}
5  *4 C     0 {3,S} {8,S}
6     C     0 {4,S}
7     C     0 {8,S}
8  *1 C     1 {5,S} {7,S}
9  *3 H     0 {3,S}
""",
    product1 = 
"""
1     C     0 {2,S} {4,S}
2     C     0 {1,S} {6,S}
3  *2 C     0 {5,S} {7,S} {9,S}
4     C     0 {1,S} {8,S}
5  *4 C     0 {3,S} {8,S}
6     C     0 {2,S}
7     C     0 {3,S}
8  *1 C     1 {4,S} {5,S}
9  *3 H     0 {3,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.16e+10,"s^-1"),
        n = 0,
        Ea = (71171.9,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dobe, S.", "Berces, T.", "Reti, F.", "Marta, F."], title=u'Isomerization of n-hexyl and s-octyl radicals by 1,5 and 1,4 intramolecular hydrogen atom transfer reactions', journal="Int. J. Chem. Kinet.", volume="19", pages="""895""", year="1987", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:51 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 37,
    label = "r00012711",
    reactant1 = 
"""
1  *1 C     1 {2,S}
2  *2 C     0 {1,S} {3,D} {4,S}
3     O     0 {2,D}
4  *3 H     0 {2,S}
""",
    product1 = 
"""
1  *2 C     0 {2,S} {3,S}
2  *1 C     1 {1,S} {4,D}
3  *3 H     0 {1,S}
4     O     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"s^-1"),
        n = 0,
        Ea = (197053,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Colket, M.B., III", "Naegeli, D.W.", "Glassman, I."], title=u'High-Temperature Pyrolysis of Acetaldehyde', journal="Int. J. Chem. Kinet.", volume="7", pages="""223""", year="1975", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
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
    index = 38,
    label = "r00012770",
    reactant1 = 
"""
1  *2 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S}
3     C     0 {1,S}
4  *1 C     1 {1,S}
5  *3 H     0 {1,S}
""",
    product1 = 
"""
1     C     0 {4,S}
2     C     0 {4,S}
3  *2 C     0 {4,S} {5,S}
4  *1 C     1 {1,S} {2,S} {3,S}
5  *3 H     0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.56e+10,"s^-1"),
        n = 0.88,
        Ea = (571.681,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Matheu, D.M.", "Green, W.H.", "Grenda, J.M."], title=u'Capturing pressure-dependence in automated mechanism generation: Reactions through cycloalkyl intermediates', journal="Int. J. Chem. Kinet.", volume="35", pages="""95-119""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
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
    index = 39,
    label = "r00015630",
    reactant1 = 
"""
1  *2 C     0 {3,S} {4,S}
2     C     0 {3,D}
3  *1 C     1 {1,S} {2,D}
4  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {2,S} {3,D} {4,S}
2  *1 C     1 {1,S}
3     C     0 {1,D}
4  *3 H     0 {1,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2e+13,"s^-1"),
        n = 0,
        Ea = (197053,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Ondruschka, B.", "Ziegler, U.", "Zimmermann, G."], title=u'Zu moglichen umlagerungen zwischen isomeren C_3H_5-radikalen', journal="Z. Phys. Chem. (Leipzig)", volume="267", pages="""1127""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
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
    index = 40,
    label = "r00015630",
    reactant1 = 
"""
1  *2 C     0 {2,D} {3,S} {4,S}
2     C     0 {1,D}
3  *1 C     1 {1,S}
4  *3 H     0 {1,S}
""",
    product1 = 
"""
1  *2 C     0 {3,S} {4,S}
2     C     0 {3,D}
3  *1 C     1 {1,S} {2,D}
4  *3 H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.94e+12,"s^-1"),
        n = 0,
        Ea = (147166,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Ondruschka, B.", "Ziegler, U.", "Zimmermann, G."], title=u'Zu moglichen umlagerungen zwischen isomeren C_3H_5-radikalen', journal="Z. Phys. Chem. (Leipzig)", volume="267", pages="""1127""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
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
    index = 41,
    label = "r00015688",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2  *5 C     0 {1,S} {4,S}
3  *4 C     0 {1,S} {5,S}
4  *2 C     0 {2,S} {6,D} {7,S}
5  *1 C     1 {3,S}
6     C     0 {4,D}
7  *3 H     0 {4,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2  *5 C     0 {1,S} {4,S}
3  *4 C     0 {1,S} {6,S}
4  *2 C     0 {2,S} {7,S}
5     C     0 {6,D}
6  *1 C     1 {3,S} {5,D}
7  *3 H     0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11,"s^-1"),
        n = 0,
        Ea = (84807.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Handford-Styring, S.M.", "Walker, R.W."], title=u'Addition of cyclopentane to slowly reacting mixtures of H_2 + O_2 between 673 and 783 K: reactions of H and OH with cyclopentane and of cyclopentyl radicals', journal="J. Chem. Soc. Faraday Trans.", volume="91", pages="""1431-1438""", year="1995", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
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
    index = 42,
    label = "r00015689",
    reactant1 = 
"""
1  *5 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S} {7,S}
3  *4 C     0 {1,S} {5,S}
4     C     0 {2,S} {6,D}
5  *1 C     1 {3,S}
6     C     0 {4,D}
7  *3 H     0 {2,S}
""",
    product1 = 
"""
1  *5 C     0 {2,S} {3,S}
2  *4 C     0 {1,S} {4,S}
3  *2 C     0 {1,S} {7,S}
4  *1 C     1 {2,S} {5,S}
5     C     0 {4,S} {6,D}
6     C     0 {5,D}
7  *3 H     0 {3,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+12,"s^-1"),
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
        ("Tue May 17 14:35:26 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 43,
    label = "r00015689",
    reactant1 = 
"""
1  *5 C     0 {2,S} {3,S}
2  *2 C     0 {1,S} {4,S} {7,S}
3  *4 C     0 {1,S} {5,S}
4     C     0 {2,S} {6,D}
5  *1 C     1 {3,S}
6     C     0 {4,D}
7  *3 H     0 {2,S}
""",
    product1 = 
"""
1  *5 C     0 {2,S} {3,S}
2  *4 C     0 {1,S} {4,S}
3  *2 C     0 {1,S} {7,S}
4  *1 C     1 {2,S} {5,S}
5     C     0 {4,S} {6,D}
6     C     0 {5,D}
7  *3 H     0 {3,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.67e+12,"s^-1"),
        n = -0.6,
        Ea = (252.795,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Matheu, D.M.", "Green, W.H.", "Grenda, J.M."], title=u'Capturing pressure-dependence in automated mechanism generation: Reactions through cycloalkyl intermediates', journal="Int. J. Chem. Kinet.", volume="35", pages="""95-119""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:26 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 44,
    label = "r00015924",
    reactant1 = 
"""
1  *5 C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *2 C     0 {1,S} {6,S}
4  *4 C     0 {2,S} {5,S}
5  *1 O     1 {4,S}
6  *3 H     0 {3,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2  *4 C     0 {1,S} {4,S}
3  *5 C     0 {1,S} {5,S}
4  *1 C     1 {2,S}
5  *2 O     0 {3,S} {6,S}
6  *3 H     0 {5,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.51e+11,"s^-1"),
        n = 0,
        Ea = (32260.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baldwin, A.C.", "Barker, J.R.", "Golden, D.M.", "Hendry, D.G."], title=u'Photochemical smog. Rate parameter estimates and computer simulations', journal="J. Phys. Chem.", volume="81", pages="""2483""", year="1977", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:30 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 45,
    label = "r00015924",
    reactant1 = 
"""
1  *5 C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *2 C     0 {1,S} {6,S}
4  *4 C     0 {2,S} {5,S}
5  *1 O     1 {4,S}
6  *3 H     0 {3,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2  *4 C     0 {1,S} {4,S}
3  *5 C     0 {1,S} {5,S}
4  *1 C     1 {2,S}
5  *2 O     0 {3,S} {6,S}
6  *3 H     0 {5,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.51e+11,"s^-1"),
        n = 0,
        Ea = (32260.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baldwin, A.C.", "Golden, D.M."], title=u'Alkoxy Radical Reactions: The Isomerization of n-Butoxy Radicals Generated from the Pyrolysis of n-Butyl Nitrite', journal="Chem. Phys. Lett.", volume="60", pages="""108""", year="1978", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:30 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 46,
    label = "r00015924",
    reactant1 = 
"""
1  *5 C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *2 C     0 {1,S} {6,S}
4  *4 C     0 {2,S} {5,S}
5  *1 O     1 {4,S}
6  *3 H     0 {3,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2  *4 C     0 {1,S} {4,S}
3  *5 C     0 {1,S} {5,S}
4  *1 C     1 {2,S}
5  *2 O     0 {3,S} {6,S}
6  *3 H     0 {5,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.78e+11,"s^-1"),
        n = 0,
        Ea = (33341,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Morabito, P.", "Heicklen, J."], title=u'The reactions of alkoxyl radicals with O_2. IV. n-C_4H_9O radicals', journal="Bull. Chem. Soc. Jpn.", volume="60", pages="""2641""", year="1987", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:30 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 47,
    label = "r00015924",
    reactant1 = 
"""
1  *5 C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *2 C     0 {1,S} {6,S}
4  *4 C     0 {2,S} {5,S}
5  *1 O     1 {4,S}
6  *3 H     0 {3,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2  *4 C     0 {1,S} {4,S}
3  *5 C     0 {1,S} {5,S}
4  *1 C     1 {2,S}
5  *2 O     0 {3,S} {6,S}
6  *3 H     0 {5,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.5e+12,"s^-1"),
        n = 0,
        Ea = (160.269,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Mereau, R.", "Rayez, M.T.", "Caralp, F.", "Rayez, J.C."], title=u'Isomerization reactions of alkoxy radicals: theoretical study and structure-activity relationships', journal="Phys. Chem. Chem. Phys.", volume="5", pages="""4828-4833""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:30 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 48,
    label = "r00015924",
    reactant1 = 
"""
1  *5 C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3  *2 C     0 {1,S} {6,S}
4  *4 C     0 {2,S} {5,S}
5  *1 O     1 {4,S}
6  *3 H     0 {3,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2  *4 C     0 {1,S} {4,S}
3  *5 C     0 {1,S} {5,S}
4  *1 C     1 {2,S}
5  *2 O     0 {3,S} {6,S}
6  *3 H     0 {5,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.43e+11,"s^-1"),
        n = 0,
        Ea = (134.989,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Vereecken, L.", "Peeters, J."], title=u'The 1,5-H-shift in 1-butoxy: A case study in the rigorous implementation of transition state theory for a multirotamer system', journal="J. Chem. Phys.", volume="119", pages="""5159-5170""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000010.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:30 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 49,
    label = "r00016217",
    reactant1 = 
"""
1  *5 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S} {6,S}
3  *2 C     0 {1,S} {7,S}
4     C     0 {1,S}
5     C     0 {1,S}
6  *4 O     0 {2,S} {8,S}
7  *3 H     0 {3,S}
8  *1 O     1 {6,S}
""",
    product1 = 
"""
1  *4 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *1 C     1 {1,S}
6  *5 O     0 {2,S} {7,S}
7  *2 O     0 {6,S} {8,S}
8  *3 H     0 {7,S}
""",
    degeneracy = 9,
    kinetics = Arrhenius(
        A = (1.2e+13,"s^-1"),
        n = 0,
        Ea = (119728,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baldwin, R.R.", "Hisham, M.W.M.", "Walker, R.W."], title=u'Arrhenius parameters of elementary reactions involved in the oxidation of neopentane', journal="J. Chem. Soc. Faraday Trans. 1", volume="78", pages="""1615""", year="1982", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:39 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 50,
    label = "r00016217",
    reactant1 = 
"""
1  *5 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S} {6,S}
3  *2 C     0 {1,S} {7,S}
4     C     0 {1,S}
5     C     0 {1,S}
6  *4 O     0 {2,S} {8,S}
7  *3 H     0 {3,S}
8  *1 O     1 {6,S}
""",
    product1 = 
"""
1  *4 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *1 C     1 {1,S}
6  *5 O     0 {2,S} {7,S}
7  *2 O     0 {6,S} {8,S}
8  *3 H     0 {7,S}
""",
    degeneracy = 9,
    kinetics = Arrhenius(
        A = (1.58e+12,"s^-1"),
        n = 0,
        Ea = (123054,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Hughes, K.J.", "Halford-Maw, P.A.", "Lightfoot, P.D.", "Turanyi, T.", "Pilling, M.J."], title=u'Direct measurements of the neopentyl peroxy-hydroperoxy radical isomerisation over the temperature range 660-750 K', journal="Symp. Int. Combust. Proc.", volume="24", pages="""645-652""", year="1992", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000003.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:39 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 51,
    label = "r00016217",
    reactant1 = 
"""
1  *5 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S} {6,S}
3  *2 C     0 {1,S} {7,S}
4     C     0 {1,S}
5     C     0 {1,S}
6  *4 O     0 {2,S} {8,S}
7  *3 H     0 {3,S}
8  *1 O     1 {6,S}
""",
    product1 = 
"""
1  *4 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *1 C     1 {1,S}
6  *5 O     0 {2,S} {7,S}
7  *2 O     0 {6,S} {8,S}
8  *3 H     0 {7,S}
""",
    degeneracy = 9,
    kinetics = Arrhenius(
        A = (8.87e+07,"s^-1"),
        n = 1.07,
        Ea = (389635,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Sun, H.", "Bozzelli, J.W."], title=u'Thermochemical and kinetic analysis on the reactions of neopentyl and hydroperoxy-neopentyl radicals with oxygen: Part I.  OH and initial stable HC product formation', journal="J. Phys. Chem. A", volume="108", pages="""1694-1711""", year="2004", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:39 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 52,
    label = "r00016217",
    reactant1 = 
"""
1  *5 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S} {6,S}
3  *2 C     0 {1,S} {7,S}
4     C     0 {1,S}
5     C     0 {1,S}
6  *4 O     0 {2,S} {8,S}
7  *3 H     0 {3,S}
8  *1 O     1 {6,S}
""",
    product1 = 
"""
1  *4 C     0 {2,S} {3,S} {4,S} {5,S}
2     C     0 {1,S} {6,S}
3     C     0 {1,S}
4     C     0 {1,S}
5  *1 C     1 {1,S}
6  *5 O     0 {2,S} {7,S}
7  *2 O     0 {6,S} {8,S}
8  *3 H     0 {7,S}
""",
    degeneracy = 9,
    kinetics = Arrhenius(
        A = (1.44e+35,"s^-1"),
        n = -7.2,
        Ea = (577513,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Sun, H.", "Bozzelli, J.W."], title=u'Thermochemical and kinetic analysis on the reactions of neopentyl and hydroperoxy-neopentyl radicals with oxygen: Part I.  OH and initial stable HC product formation', journal="J. Phys. Chem. A", volume="108", pages="""1694-1711""", year="2004", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000006.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:39 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 53,
    label = "r00016683",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4  *2 C     0 {2,S} {6,S} {7,S}
5     O     0 {3,S}
6  *1 O     1 {4,S}
7  *3 H     0 {4,S}
""",
    product1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {5,S}
4  *1 C     1 {2,S} {6,S}
5     O     0 {3,S}
6  *2 O     0 {4,S} {7,S}
7  *3 H     0 {6,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.58e+11,"s^-1"),
        n = 0,
        Ea = (27188.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Baldwin, A.C.", "Barker, J.R.", "Golden, D.M.", "Hendry, D.G."], title=u'Photochemical smog. Rate parameter estimates and computer simulations', journal="J. Phys. Chem.", volume="81", pages="""2483""", year="1977", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:35:53 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 54,
    label = "r00017030",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {6,S}
4     C     0 {2,S} {8,S}
5  *2 C     0 {7,S} {8,S} {9,S}
6     C     0 {3,S}
7     C     0 {5,S}
8  *1 C     1 {4,S} {5,S}
9  *3 H     0 {5,S}
""",
    product1 = 
"""
1     C     0 {2,S} {4,S}
2     C     0 {1,S} {3,S}
3     C     0 {2,S} {5,S}
4     C     0 {1,S} {6,S}
5  *2 C     0 {3,S} {8,S} {9,S}
6     C     0 {4,S}
7     C     0 {8,S}
8  *1 C     1 {5,S} {7,S}
9  *3 H     0 {5,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.51e+09,"s^-1"),
        n = 0,
        Ea = (46893.6,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dobe, S.", "Berces, T.", "Reti, F.", "Marta, F."], title=u'Isomerization of n-hexyl and s-octyl radicals by 1,5 and 1,4 intramolecular hydrogen atom transfer reactions', journal="Int. J. Chem. Kinet.", volume="19", pages="""895""", year="1987", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:36:11 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 55,
    label = "r00017124",
    reactant1 = 
"""
1  *4 C     0 {2,B} {4,S} {8,B}
2     C     0 {1,B} {3,B}
3     C     0 {2,B} {5,B}
4  *5 C     0 {1,S} {7,D}
5     C     0 {3,B} {6,B}
6     C     0 {5,B} {8,B}
7  *2 C     0 {4,D} {9,S}
8  *1 C     1 {1,B} {6,B}
9  *3 H     0 {7,S}
""",
    product1 = 
"""
1  *5 C     0 {2,B} {3,B} {7,S}
2     C     0 {1,B} {4,B}
3  *2 C     0 {1,B} {6,B} {9,S}
4     C     0 {2,B} {5,B}
5     C     0 {4,B} {6,B}
6     C     0 {3,B} {5,B}
7  *4 C     0 {1,S} {8,D}
8  *1 C     1 {7,D}
9  *3 H     0 {3,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.57e+09,"s^-1"),
        n = 0.81,
        Ea = (434.048,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tokmakov, I.V.", "Lin, M.C."], title=u'Reaction of phenyl radicals with acetylene: Quantum chemical investigation of the mechanism and master equation analysis of the kinetics', journal="J. Am. Chem. Soc.", volume="125", pages="""11397-11408""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:36:12 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 56,
    label = "r00017124",
    reactant1 = 
"""
1  *5 C     0 {2,B} {3,B} {7,S}
2  *2 C     0 {1,B} {5,B} {9,S}
3     C     0 {1,B} {6,B}
4     C     0 {5,B} {6,B}
5     C     0 {2,B} {4,B}
6     C     0 {3,B} {4,B}
7  *4 C     0 {1,S} {8,D}
8  *1 C     1 {7,D}
9  *3 H     0 {2,S}
""",
    product1 = 
"""
1  *4 C     0 {2,B} {5,S} {8,B}
2     C     0 {1,B} {3,B}
3     C     0 {2,B} {4,B}
4     C     0 {3,B} {6,B}
5  *5 C     0 {1,S} {7,D}
6     C     0 {4,B} {8,B}
7  *2 C     0 {5,D} {9,S}
8  *1 C     1 {1,B} {6,B}
9  *3 H     0 {7,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.04e+10,"s^-1"),
        n = 0.7,
        Ea = (454.371,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Tokmakov, I.V.", "Lin, M.C."], title=u'Reaction of phenyl radicals with acetylene: Quantum chemical investigation of the mechanism and master equation analysis of the kinetics', journal="J. Am. Chem. Soc.", volume="125", pages="""11397-11408""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000002.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:36:12 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 57,
    label = "r00017157",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2  *5 C     0 {1,S} {4,S}
3  *4 C     0 {1,S} {5,S} {6,S}
4  *2 C     0 {2,S} {7,S}
5     C     0 {3,S}
6  *1 O     1 {3,S}
7  *3 H     0 {4,S}
""",
    product1 = 
"""
1  *5 C     0 {2,S} {4,S} {6,S}
2     C     0 {1,S} {3,S}
3  *4 C     0 {2,S} {5,S}
4     C     0 {1,S}
5  *1 C     1 {3,S}
6  *2 O     0 {1,S} {7,S}
7  *3 H     0 {6,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.4e+12,"s^-1"),
        n = 0,
        Ea = (153.66,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Mereau, R.", "Rayez, M.T.", "Caralp, F.", "Rayez, J.C."], title=u'Isomerization reactions of alkoxy radicals: theoretical study and structure-activity relationships', journal="Phys. Chem. Chem. Phys.", volume="5", pages="""4828-4833""", year="2003", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:36:12 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 58,
    label = "r00017157",
    reactant1 = 
"""
1     C     0 {2,S} {3,S}
2  *5 C     0 {1,S} {4,S}
3  *4 C     0 {1,S} {5,S} {6,S}
4  *2 C     0 {2,S} {7,S}
5     C     0 {3,S}
6  *1 O     1 {3,S}
7  *3 H     0 {4,S}
""",
    product1 = 
"""
1  *5 C     0 {2,S} {4,S} {6,S}
2     C     0 {1,S} {3,S}
3  *4 C     0 {2,S} {5,S}
4     C     0 {1,S}
5  *1 C     1 {3,S}
6  *2 O     0 {1,S} {7,S}
7  *3 H     0 {6,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.26e+11,"s^-1"),
        n = 0,
        Ea = (39743.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Dobe, S.", "Berces, T.", "Marta, F."], title=u'Gas phase decomposition and isomerization reactions of 2-pentoxy radicals', journal="Int. J. Chem. Kinet.", volume="18", pages="""329""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000005.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:36:12 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

