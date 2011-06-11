#!/usr/bin/env python
# encoding: utf-8

name = "2+2_cycloaddition_CCO"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 1,
    label = "r00007002",
    reactant1 = 
"""
1  *1 C     0 {2,D}
2  *2 C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    reactant2 = 
"""
1  *4 C     0 {2,D}
2  *3 C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    product1 = 
"""
1  *1 C     0 {3,S} {4,S}
2  *4 C     0 {3,S} {4,S}
3  *2 C     0 {1,S} {2,S} {5,D}
4  *3 C     0 {1,S} {2,S} {6,D}
5     O     0 {3,D}
6     O     0 {4,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.78e+08,"cm^3/(mol*s)"),
        n = 0,
        Ea = (73998.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Blake, P.G.", "Davis, H.H."], title=u'Kinetics of Dimerisation of Gaseous Keten', journal="J. Appl. Chem. Biotechnol.", volume="22", pages="""491""", year="1972", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:02 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

entry(
    index = 2,
    label = "r00009168",
    reactant1 = 
"""
1  *1 C     0 {3,S} {4,S} {7,S} {8,S}
2  *4 C     0 {5,S} {6,S} {7,S} {8,S}
3     C     0 {1,S}
4     C     0 {1,S}
5     C     0 {2,S}
6     C     0 {2,S}
7  *2 C     0 {1,S} {2,S} {9,D}
8  *3 C     0 {1,S} {2,S} {10,D}
9     O     0 {7,D}
10    O     0 {8,D}
""",
    product1 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *1 C     0 {1,S} {2,S} {4,D}
4  *2 C     0 {3,D} {5,D}
5     O     0 {4,D}
""",
    product2 = 
"""
1     C     0 {3,S}
2     C     0 {3,S}
3  *4 C     0 {1,S} {2,S} {4,D}
4  *3 C     0 {3,D} {5,D}
5     O     0 {4,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (6.03e+13,"s^-1"),
        n = 0,
        Ea = (202873,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(authors=["Vala, M.", "Baiardo, J.", "Latham, D.", "Mukherjee, R.", "Pascyz, S."], title=u'Fourier transform infrared kinetic study of the thermal decomposition of tetramethyl-1-3-cyclobutanedione and dimethylketene', journal="J. Indian Chem. Soc.", volume="63", pages="""16""", year="1986", url="http://warehouse.primekinetics.org/depository/kinetics/catalog/rk00000001.xml"),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue May 17 14:34:22 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)

