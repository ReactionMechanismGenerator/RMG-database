#!/usr/bin/env python
# encoding: utf-8

name = "Nitrogen_Glarborg_Zhang_et_al"
shortDesc = u""
longDesc = u"""
Kuiwen Zhang, Lidong Zhang, Mingfeng Xie, Lili Ye, Feng Zhang, Peter Glarborg, Fei Qi
An experimental and kinetic modeling study of premixed nitroethane flames at low pressure
Proceedings of the Combustion Institute 34 (2013) 617–624
"""
recommended = False

entry(
    index = 1,
    reactant1 = 
"""
C2H5NO2
1  C 0 {2,S} {3,S} {4,S} {5,S}
2  H 0 {1,S}
3  H 0 {1,S}
4  H 0 {1,S}
5  C 0 {1,S} {6,S} {7,S} {8,S}
6  H 0 {5,S}
7  H 0 {5,S}
8  N 0 {5,S} {9,S} {10,D}
9  O 0 {8,S}
10 O 0 {8,D}
""",
    product1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.8e+64, 's^-1'), n=-15.5, Ea=(73513, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2,
    reactant1 = 
"""
C2H5NO2
1  C 0 {2,S} {3,S} {4,S} {5,S}
2  H 0 {1,S}
3  H 0 {1,S}
4  H 0 {1,S}
5  C 0 {1,S} {6,S} {7,S} {8,S}
6  H 0 {5,S}
7  H 0 {5,S}
8  N 0 {5,S} {9,S} {10,D}
9  O 0 {8,S}
10 O 0 {8,D}
""",
    product1 = 
"""
HNO2
1 H 0 {2,S}
2 N 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {2,S}
""",
    product2 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.06e+77, 's^-1'), n=-19.6, Ea=(73632, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 3,
    reactant1 = 
"""
C2H5NO2
1  C 0 {2,S} {3,S} {4,S} {5,S}
2  H 0 {1,S}
3  H 0 {1,S}
4  H 0 {1,S}
5  C 0 {1,S} {6,S} {7,S} {8,S}
6  H 0 {5,S}
7  H 0 {5,S}
8  N 0 {5,S} {9,S} {10,D}
9  O 0 {8,S}
10 O 0 {8,D}
""",
    product1 = 
"""
CH2CHNO
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 C 1 {1,S} {5,S} {6,S}
5 H 0 {4,S}
6 N 0 {4,S} {7,D}
7 O 0 {6,D}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.9e+51, 's^-1'), n=-20, Ea=(92377, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 4,
    reactant1 = 
"""
C2H5NO2
1  C 0 {2,S} {3,S} {4,S} {5,S}
2  H 0 {1,S}
3  H 0 {1,S}
4  H 0 {1,S}
5  C 0 {1,S} {6,S} {7,S} {8,S}
6  H 0 {5,S}
7  H 0 {5,S}
8  N 0 {5,S} {9,S} {10,D}
9  O 0 {8,S}
10 O 0 {8,D}
""",
    product1 = 
"""
CH3CNO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,T}
6 N 0 {5,T} {7,S}
7 O 0 {6,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e+48, 's^-1'), n=-18.4, Ea=(85601, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 5,
    reactant1 = 
"""
C2H5NO2
1  C 0 {2,S} {3,S} {4,S} {5,S}
2  H 0 {1,S}
3  H 0 {1,S}
4  H 0 {1,S}
5  C 0 {1,S} {6,S} {7,S} {8,S}
6  H 0 {5,S}
7  H 0 {5,S}
8  N 0 {5,S} {9,S} {10,D}
9  O 0 {8,S}
10 O 0 {8,D}
""",
    product1 = 
"""
CH3CH2ONO
1  C 0 {2,S} {3,S} {4,S} {5,S}
2  H 0 {1,S}
3  H 0 {1,S}
4  H 0 {1,S}
5  C 0 {1,S} {6,S} {7,S} {8,S}
6  H 0 {5,S}
7  H 0 {5,S}
8  O 0 {5,S} {9,S}
9  N 0 {8,S} {10,D}
10 O 0 {9,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(21000000000.0, 's^-1'), n=1, Ea=(60660, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 6,
    reactant1 = 
"""
C2H5NO2
1  C 0 {2,S} {3,S} {4,S} {5,S}
2  H 0 {1,S}
3  H 0 {1,S}
4  H 0 {1,S}
5  C 0 {1,S} {6,S} {7,S} {8,S}
6  H 0 {5,S}
7  H 0 {5,S}
8  N 0 {5,S} {9,S} {10,D}
9  O 0 {8,S}
10 O 0 {8,D}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH2CH2NO2
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 C 0 {1,S} {5,S} {6,S} {7,S}
5 H 0 {4,S}
6 H 0 {4,S}
7 N 0 {4,S} {8,S} {9,D}
8 O 0 {7,S}
9 O 0 {7,D}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (98000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (9220, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 7,
    reactant1 = 
"""
C2H5NO2
1  C 0 {2,S} {3,S} {4,S} {5,S}
2  H 0 {1,S}
3  H 0 {1,S}
4  H 0 {1,S}
5  C 0 {1,S} {6,S} {7,S} {8,S}
6  H 0 {5,S}
7  H 0 {5,S}
8  N 0 {5,S} {9,S} {10,D}
9  O 0 {8,S}
10 O 0 {8,D}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH3CHNO2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 1 {1,S} {6,S} {7,S}
6 H 0 {5,S}
7 N 0 {5,S} {8,S} {9,D}
8 O 0 {7,S}
9 O 0 {7,D}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (26000000.0, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (2827, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 8,
    reactant1 = 
"""
C2H5NO2
1  C 0 {2,S} {3,S} {4,S} {5,S}
2  H 0 {1,S}
3  H 0 {1,S}
4  H 0 {1,S}
5  C 0 {1,S} {6,S} {7,S} {8,S}
6  H 0 {5,S}
7  H 0 {5,S}
8  N 0 {5,S} {9,S} {10,D}
9  O 0 {8,S}
10 O 0 {8,D}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C2H5NO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,S} {7,S} {8,S}
6 H 0 {5,S}
7 H 0 {5,S}
8 N 0 {5,S} {9,D}
9 O 0 {8,D}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1400000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3730, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 9,
    reactant1 = 
"""
C2H5NO2
1  C 0 {2,S} {3,S} {4,S} {5,S}
2  H 0 {1,S}
3  H 0 {1,S}
4  H 0 {1,S}
5  C 0 {1,S} {6,S} {7,S} {8,S}
6  H 0 {5,S}
7  H 0 {5,S}
8  N 0 {5,S} {9,S} {10,D}
9  O 0 {8,S}
10 O 0 {8,D}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH2CH2NO2
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 C 0 {1,S} {5,S} {6,S} {7,S}
5 H 0 {4,S}
6 H 0 {4,S}
7 N 0 {4,S} {8,S} {9,D}
8 O 0 {7,S}
9 O 0 {7,D}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e-07, 'cm^3/(mol*s)'), n=6.5, Ea=(274, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 10,
    reactant1 = 
"""
C2H5NO2
1  C 0 {2,S} {3,S} {4,S} {5,S}
2  H 0 {1,S}
3  H 0 {1,S}
4  H 0 {1,S}
5  C 0 {1,S} {6,S} {7,S} {8,S}
6  H 0 {5,S}
7  H 0 {5,S}
8  N 0 {5,S} {9,S} {10,D}
9  O 0 {8,S}
10 O 0 {8,D}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH3CHNO2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 1 {1,S} {6,S} {7,S}
6 H 0 {5,S}
7 N 0 {5,S} {8,S} {9,D}
8 O 0 {7,S}
9 O 0 {7,D}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (19000000.0, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (1824, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 11,
    reactant1 = 
"""
C2H5NO2
1  C 0 {2,S} {3,S} {4,S} {5,S}
2  H 0 {1,S}
3  H 0 {1,S}
4  H 0 {1,S}
5  C 0 {1,S} {6,S} {7,S} {8,S}
6  H 0 {5,S}
7  H 0 {5,S}
8  N 0 {5,S} {9,S} {10,D}
9  O 0 {8,S}
10 O 0 {8,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2CH2NO2
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 C 0 {1,S} {5,S} {6,S} {7,S}
5 H 0 {4,S}
6 H 0 {4,S}
7 N 0 {4,S} {8,S} {9,D}
8 O 0 {7,S}
9 O 0 {7,D}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9200000.0, 'cm^3/(mol*s)'), n=2, Ea=(990, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 12,
    reactant1 = 
"""
C2H5NO2
1  C 0 {2,S} {3,S} {4,S} {5,S}
2  H 0 {1,S}
3  H 0 {1,S}
4  H 0 {1,S}
5  C 0 {1,S} {6,S} {7,S} {8,S}
6  H 0 {5,S}
7  H 0 {5,S}
8  N 0 {5,S} {9,S} {10,D}
9  O 0 {8,S}
10 O 0 {8,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH3CHNO2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 1 {1,S} {6,S} {7,S}
6 H 0 {5,S}
7 N 0 {5,S} {8,S} {9,D}
8 O 0 {7,S}
9 O 0 {7,D}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (460000000000.0, 'cm^3/(mol*s)'),
        n = 0.1,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 13,
    reactant1 = 
"""
C2H5NO2
1  C 0 {2,S} {3,S} {4,S} {5,S}
2  H 0 {1,S}
3  H 0 {1,S}
4  H 0 {1,S}
5  C 0 {1,S} {6,S} {7,S} {8,S}
6  H 0 {5,S}
7  H 0 {5,S}
8  N 0 {5,S} {9,S} {10,D}
9  O 0 {8,S}
10 O 0 {8,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH3CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,S} {7,S} {8,S}
6 H 0 {5,S}
7 H 0 {5,S}
8 O 0 {5,S} {9,S}
9 H 0 {8,S}
""",
    product2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 14,
    reactant1 = 
"""
C2H5NO2
1  C 0 {2,S} {3,S} {4,S} {5,S}
2  H 0 {1,S}
3  H 0 {1,S}
4  H 0 {1,S}
5  C 0 {1,S} {6,S} {7,S} {8,S}
6  H 0 {5,S}
7  H 0 {5,S}
8  N 0 {5,S} {9,S} {10,D}
9  O 0 {8,S}
10 O 0 {8,D}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
CH2CH2NO2
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 C 0 {1,S} {5,S} {6,S} {7,S}
5 H 0 {4,S}
6 H 0 {4,S}
7 N 0 {4,S} {8,S} {9,D}
8 O 0 {7,S}
9 O 0 {7,D}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(110000, 'cm^3/(mol*s)'), n=2.5, Ea=(16850, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 15,
    reactant1 = 
"""
C2H5NO2
1  C 0 {2,S} {3,S} {4,S} {5,S}
2  H 0 {1,S}
3  H 0 {1,S}
4  H 0 {1,S}
5  C 0 {1,S} {6,S} {7,S} {8,S}
6  H 0 {5,S}
7  H 0 {5,S}
8  N 0 {5,S} {9,S} {10,D}
9  O 0 {8,S}
10 O 0 {8,D}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
CH3CHNO2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 1 {1,S} {6,S} {7,S}
6 H 0 {5,S}
7 N 0 {5,S} {8,S} {9,D}
8 O 0 {7,S}
9 O 0 {7,D}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8200, 'cm^3/(mol*s)'), n=2.5, Ea=(10750, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 16,
    reactant1 = 
"""
C2H5NO2
1  C 0 {2,S} {3,S} {4,S} {5,S}
2  H 0 {1,S}
3  H 0 {1,S}
4  H 0 {1,S}
5  C 0 {1,S} {6,S} {7,S} {8,S}
6  H 0 {5,S}
7  H 0 {5,S}
8  N 0 {5,S} {9,S} {10,D}
9  O 0 {8,S}
10 O 0 {8,D}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH2CH2NO2
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 C 0 {1,S} {5,S} {6,S} {7,S}
5 H 0 {4,S}
6 H 0 {4,S}
7 N 0 {4,S} {8,S} {9,D}
8 O 0 {7,S}
9 O 0 {7,D}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(730000, 'cm^3/(mol*s)'), n=2.5, Ea=(49160, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 17,
    reactant1 = 
"""
C2H5NO2
1  C 0 {2,S} {3,S} {4,S} {5,S}
2  H 0 {1,S}
3  H 0 {1,S}
4  H 0 {1,S}
5  C 0 {1,S} {6,S} {7,S} {8,S}
6  H 0 {5,S}
7  H 0 {5,S}
8  N 0 {5,S} {9,S} {10,D}
9  O 0 {8,S}
10 O 0 {8,D}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
CH2CH2NO2
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 C 0 {1,S} {5,S} {6,S} {7,S}
5 H 0 {4,S}
6 H 0 {4,S}
7 N 0 {4,S} {8,S} {9,D}
8 O 0 {7,S}
9 O 0 {7,D}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(220, 'cm^3/(mol*s)'), n=3.2, Ea=(9622, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 18,
    reactant1 = 
"""
C2H5NO2
1  C 0 {2,S} {3,S} {4,S} {5,S}
2  H 0 {1,S}
3  H 0 {1,S}
4  H 0 {1,S}
5  C 0 {1,S} {6,S} {7,S} {8,S}
6  H 0 {5,S}
7  H 0 {5,S}
8  N 0 {5,S} {9,S} {10,D}
9  O 0 {8,S}
10 O 0 {8,D}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
CH3CHNO2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 1 {1,S} {6,S} {7,S}
6 H 0 {5,S}
7 N 0 {5,S} {8,S} {9,D}
8 O 0 {7,S}
9 O 0 {7,D}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(730, 'cm^3/(mol*s)'), n=3, Ea=(7948, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 19,
    reactant1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
CH2CH2NO2
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 C 0 {1,S} {5,S} {6,S} {7,S}
5 H 0 {4,S}
6 H 0 {4,S}
7 N 0 {4,S} {8,S} {9,D}
8 O 0 {7,S}
9 O 0 {7,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9400000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 20,
    reactant1 = 
"""
CH3CHNO2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 1 {1,S} {6,S} {7,S}
6 H 0 {5,S}
7 N 0 {5,S} {8,S} {9,D}
8 O 0 {7,S}
9 O 0 {7,D}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(20000000000000.0, 's^-1'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 21,
    reactant1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product1 = 
"""
C2H5NO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,S} {7,S} {8,S}
6 H 0 {5,S}
7 H 0 {5,S}
8 N 0 {5,S} {9,D}
9 O 0 {8,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (140000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 22,
    reactant1 = 
"""
C2H5NO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,S} {7,S} {8,S}
6 H 0 {5,S}
7 H 0 {5,S}
8 N 0 {5,S} {9,D}
9 O 0 {8,D}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product3 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (98000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (9220, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 23,
    reactant1 = 
"""
C2H5NO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,S} {7,S} {8,S}
6 H 0 {5,S}
7 H 0 {5,S}
8 N 0 {5,S} {9,D}
9 O 0 {8,D}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH3CHNO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 1 {1,S} {6,S} {7,S}
6 H 0 {5,S}
7 N 0 {5,S} {8,D}
8 O 0 {7,D}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (440000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (378, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 24,
    reactant1 = 
"""
C2H5NO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,S} {7,S} {8,S}
6 H 0 {5,S}
7 H 0 {5,S}
8 N 0 {5,S} {9,D}
9 O 0 {8,D}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product3 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.1e-07, 'cm^3/(mol*s)'), n=6.5, Ea=(274, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 25,
    reactant1 = 
"""
C2H5NO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,S} {7,S} {8,S}
6 H 0 {5,S}
7 H 0 {5,S}
8 N 0 {5,S} {9,D}
9 O 0 {8,D}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH3CHNO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 1 {1,S} {6,S} {7,S}
6 H 0 {5,S}
7 N 0 {5,S} {8,D}
8 O 0 {7,D}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (330000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (3616, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 26,
    reactant1 = 
"""
C2H5NO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,S} {7,S} {8,S}
6 H 0 {5,S}
7 H 0 {5,S}
8 N 0 {5,S} {9,D}
9 O 0 {8,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product3 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(9200000.0, 'cm^3/(mol*s)'), n=2, Ea=(990, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 27,
    reactant1 = 
"""
C2H5NO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,S} {7,S} {8,S}
6 H 0 {5,S}
7 H 0 {5,S}
8 N 0 {5,S} {9,D}
9 O 0 {8,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH3CHNO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 1 {1,S} {6,S} {7,S}
6 H 0 {5,S}
7 N 0 {5,S} {8,D}
8 O 0 {7,D}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3600000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1192, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 28,
    reactant1 = 
"""
C2H5NO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,S} {7,S} {8,S}
6 H 0 {5,S}
7 H 0 {5,S}
8 N 0 {5,S} {9,D}
9 O 0 {8,D}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product3 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(110000, 'cm^3/(mol*s)'), n=2.5, Ea=(16850, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 29,
    reactant1 = 
"""
C2H5NO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,S} {7,S} {8,S}
6 H 0 {5,S}
7 H 0 {5,S}
8 N 0 {5,S} {9,D}
9 O 0 {8,D}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product3 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(730000, 'cm^3/(mol*s)'), n=2.5, Ea=(49160, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 30,
    reactant1 = 
"""
CH3CHNO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 1 {1,S} {6,S} {7,S}
6 H 0 {5,S}
7 N 0 {5,S} {8,D}
8 O 0 {7,D}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(20000000000000.0, 's^-1'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 31,
    reactant1 = 
"""
CH2CHNO
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 C 1 {1,S} {5,S} {6,S}
5 H 0 {4,S}
6 N 0 {4,S} {7,D}
7 O 0 {6,D}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CHCHNO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 C 0 {1,D} {4,S} {5,S}
4 H 0 {3,S}
5 N 0 {3,S} {6,D}
6 O 0 {5,D}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (440000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (378, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 32,
    reactant1 = 
"""
CH2CHNO
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 C 1 {1,S} {5,S} {6,S}
5 H 0 {4,S}
6 N 0 {4,S} {7,D}
7 O 0 {6,D}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C2H3
1 H 0 {2,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {4,S} {5,S}
4 H 0 {3,S}
5 H 0 {3,S}
""",
    product2 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2782, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 33,
    reactant1 = 
"""
CH2CHNO
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 C 1 {1,S} {5,S} {6,S}
5 H 0 {4,S}
6 N 0 {4,S} {7,D}
7 O 0 {6,D}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CHCHNO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 C 0 {1,D} {4,S} {5,S}
4 H 0 {3,S}
5 N 0 {3,S} {6,D}
6 O 0 {5,D}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (330000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (3616, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 34,
    reactant1 = 
"""
CH2CHNO
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 C 1 {1,S} {5,S} {6,S}
5 H 0 {4,S}
6 N 0 {4,S} {7,D}
7 O 0 {6,D}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
C2H3
1 H 0 {2,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {4,S} {5,S}
4 H 0 {3,S}
5 H 0 {3,S}
""",
    product2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (170000000.0, 'cm^3/(mol*s)'),
        n = 2.1,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 35,
    reactant1 = 
"""
CH2CHNO
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 C 1 {1,S} {5,S} {6,S}
5 H 0 {4,S}
6 N 0 {4,S} {7,D}
7 O 0 {6,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CHCHNO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 C 0 {1,D} {4,S} {5,S}
4 H 0 {3,S}
5 N 0 {3,S} {6,D}
6 O 0 {5,D}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3600000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1192, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 36,
    reactant1 = 
"""
CH2CHNO
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 C 1 {1,S} {5,S} {6,S}
5 H 0 {4,S}
6 N 0 {4,S} {7,D}
7 O 0 {6,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C2H3
1 H 0 {2,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {4,S} {5,S}
4 H 0 {3,S}
5 H 0 {3,S}
""",
    product2 = 
"""
HONO
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 N 0 {2,S} {4,D}
4 O 0 {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (994, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 37,
    reactant1 = 
"""
CHCHNO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 C 0 {1,D} {4,S} {5,S}
4 H 0 {3,S}
5 N 0 {3,S} {6,D}
6 O 0 {5,D}
""",
    product1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    product2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(100000000000000.0, 's^-1'), n=0, Ea=(890, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 38,
    reactant1 = 
"""
CH3CH2ONO2
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {7,S} {8,S} {9,S}
3  N 0 {4,S} {10,S} {11,D}
4  O 0 {1,S} {3,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 O 0 {3,S}
11 O 0 {3,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH3CH2O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 O 1 {2,S}
""",
    product2 = 
"""
HONO2
1 N 0 {2,S} {3,S} {4,D}
2 O 0 {1,S} {5,S}
3 O 0 {1,S}
4 O 0 {1,D}
5 H 0 {2,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (2200000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (2140, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (32000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (-250, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 40,
    reactant1 = 
"""
CH3CH2ONO
1  C 0 {2,S} {3,S} {4,S} {5,S}
2  H 0 {1,S}
3  H 0 {1,S}
4  H 0 {1,S}
5  C 0 {1,S} {6,S} {7,S} {8,S}
6  H 0 {5,S}
7  H 0 {5,S}
8  O 0 {5,S} {9,S}
9  N 0 {8,S} {10,D}
10 O 0 {9,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH3CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,S} {7,S} {8,S}
6 H 0 {5,S}
7 H 0 {5,S}
8 O 0 {5,S} {9,S}
9 H 0 {8,S}
""",
    product2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (160000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3505, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 41,
    reactant1 = 
"""
CH3CNO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,T}
6 N 0 {5,T} {7,S}
7 O 0 {6,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CHCHNO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 C 0 {1,D} {4,S} {5,S}
4 H 0 {3,S}
5 N 0 {3,S} {6,D}
6 O 0 {5,D}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (440000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (378, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 42,
    reactant1 = 
"""
CH3CNO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,T}
6 N 0 {5,T} {7,S}
7 O 0 {6,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C2H3
1 H 0 {2,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {4,S} {5,S}
4 H 0 {3,S}
5 H 0 {3,S}
""",
    product2 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2782, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 43,
    reactant1 = 
"""
CH3CNO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,T}
6 N 0 {5,T} {7,S}
7 O 0 {6,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CHCHNO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 C 0 {1,D} {4,S} {5,S}
4 H 0 {3,S}
5 N 0 {3,S} {6,D}
6 O 0 {5,D}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (330000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (3616, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 44,
    reactant1 = 
"""
CH3CNO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,T}
6 N 0 {5,T} {7,S}
7 O 0 {6,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
C2H3
1 H 0 {2,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {4,S} {5,S}
4 H 0 {3,S}
5 H 0 {3,S}
""",
    product2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (170000000.0, 'cm^3/(mol*s)'),
        n = 2.1,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 45,
    reactant1 = 
"""
CH3CNO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,T}
6 N 0 {5,T} {7,S}
7 O 0 {6,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CHCHNO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 C 0 {1,D} {4,S} {5,S}
4 H 0 {3,S}
5 N 0 {3,S} {6,D}
6 O 0 {5,D}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3600000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1192, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 46,
    reactant1 = 
"""
CH3CNO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,T}
6 N 0 {5,T} {7,S}
7 O 0 {6,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C2H3
1 H 0 {2,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {4,S} {5,S}
4 H 0 {3,S}
5 H 0 {3,S}
""",
    product2 = 
"""
HONO
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 N 0 {2,S} {4,D}
4 O 0 {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (994, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 47,
    reactant1 = 
"""
CH3NO2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 N 0 {1,S} {6,S} {7,D}
6 O 0 {5,S}
7 O 0 {5,D}
""",
    product1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {1,S}
""",
    product2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1200000000000000.0, 's^-1'),
        n = 0,
        Ea = (59200, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 48,
    reactant1 = 
"""
CH3NO2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 N 0 {1,S} {6,S} {7,D}
6 O 0 {5,S}
7 O 0 {5,D}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
HONO
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 N 0 {2,S} {4,D}
4 O 0 {3,D}
""",
    product2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3730, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 49,
    reactant1 = 
"""
CH3NO2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 N 0 {1,S} {6,S} {7,D}
6 O 0 {5,S}
7 O 0 {5,D}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH3NO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 N 0 {1,S} {6,D}
6 O 0 {5,D}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1400000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3730, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 50,
    reactant1 = 
"""
CH3NO2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 N 0 {1,S} {6,S} {7,D}
6 O 0 {5,S}
7 O 0 {5,D}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH2NO2
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 N 0 {1,S} {5,S} {6,D}
5 O 0 {4,S}
6 O 0 {4,D}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (49000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (9220, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 51,
    reactant1 = 
"""
CH3NO2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 N 0 {1,S} {6,S} {7,D}
6 O 0 {5,S}
7 O 0 {5,D}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH2NO2
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 N 0 {1,S} {5,S} {6,D}
5 O 0 {4,S}
6 O 0 {4,D}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (15000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5350, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 52,
    reactant1 = 
"""
CH3NO2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 N 0 {1,S} {6,S} {7,D}
6 O 0 {5,S}
7 O 0 {5,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 0 {1,S} {6,S}
6 H 0 {5,S}
""",
    product2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 53,
    reactant1 = 
"""
CH3NO2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 N 0 {1,S} {6,S} {7,D}
6 O 0 {5,S}
7 O 0 {5,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2NO2
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 N 0 {1,S} {5,S} {6,D}
5 O 0 {4,S}
6 O 0 {4,D}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(500000, 'cm^3/(mol*s)'), n=2, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 54,
    reactant1 = 
"""
CH3NO2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 N 0 {1,S} {6,S} {7,D}
6 O 0 {5,S}
7 O 0 {5,D}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
CH2NO2
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 N 0 {1,S} {5,S} {6,D}
5 O 0 {4,S}
6 O 0 {4,D}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (23000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 55,
    reactant1 = 
"""
CH3NO2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 N 0 {1,S} {6,S} {7,D}
6 O 0 {5,S}
7 O 0 {5,D}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH2NO2
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 N 0 {1,S} {5,S} {6,D}
5 O 0 {4,S}
6 O 0 {4,D}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (57000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 56,
    reactant1 = 
"""
CH3NO2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 N 0 {1,S} {6,S} {7,D}
6 O 0 {5,S}
7 O 0 {5,D}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
CH2NO2
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 N 0 {1,S} {5,S} {6,D}
5 O 0 {4,S}
6 O 0 {4,D}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.55, 'cm^3/(mol*s)'), n=4, Ea=(8300, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 57,
    reactant1 = 
"""
CH3NO2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 N 0 {1,S} {6,S} {7,D}
6 O 0 {5,S}
7 O 0 {5,D}
""",
    reactant2 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {1,S}
""",
    product1 = 
"""
CH2NO2
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 N 0 {1,S} {5,S} {6,D}
5 O 0 {4,S}
6 O 0 {4,D}
""",
    product2 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 0 {1,S} {6,S}
6 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 58,
    reactant1 = 
"""
CH3NO2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 N 0 {1,S} {6,S} {7,D}
6 O 0 {5,S}
7 O 0 {5,D}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
CH2NO2
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 N 0 {1,S} {5,S} {6,D}
5 O 0 {4,S}
6 O 0 {4,D}
""",
    product2 = 
"""
HONO
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 N 0 {2,S} {4,D}
4 O 0 {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (32000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 59,
    reactant1 = 
"""
CH2NO2
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 N 0 {1,S} {5,S} {6,D}
5 O 0 {4,S}
6 O 0 {4,D}
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(500000000000.0, 's^-1'), n=0, Ea=(36000, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 60,
    reactant1 = 
"""
CH2NO2
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 N 0 {1,S} {5,S} {6,D}
5 O 0 {4,S}
6 O 0 {4,D}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 61,
    reactant1 = 
"""
CH2NO2
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 N 0 {1,S} {5,S} {6,D}
5 O 0 {4,S}
6 O 0 {4,D}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 62,
    reactant1 = 
"""
CH2NO2
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 N 0 {1,S} {5,S} {6,D}
5 O 0 {4,S}
6 O 0 {4,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 63,
    reactant1 = 
"""
CH2NO2
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 N 0 {1,S} {5,S} {6,D}
5 O 0 {4,S}
6 O 0 {4,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
HONO
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 N 0 {2,S} {4,D}
4 O 0 {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 64,
    reactant1 = 
"""
CH2NO2
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 N 0 {1,S} {5,S} {6,D}
5 O 0 {4,S}
6 O 0 {4,D}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 65,
    reactant1 = 
"""
CH3ONO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 0 {1,S} {6,S}
6 N 0 {5,S} {7,D}
7 O 0 {6,D}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 0 {1,S} {6,S}
6 H 0 {5,S}
""",
    product2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (120000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1900, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 66,
    reactant1 = 
"""
CH3ONO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 0 {1,S} {6,S}
6 N 0 {5,S} {7,D}
7 O 0 {6,D}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    product3 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (140000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1900, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 67,
    reactant1 = 
"""
CH3ONO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 0 {1,S} {6,S}
6 N 0 {5,S} {7,D}
7 O 0 {6,D}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {1,S}
""",
    product2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5210, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 68,
    reactant1 = 
"""
CH3ONO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 0 {1,S} {6,S}
6 N 0 {5,S} {7,D}
7 O 0 {6,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 0 {1,S} {6,S}
6 H 0 {5,S}
""",
    product2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (60000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3505, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 69,
    reactant1 = 
"""
CH3ONO2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 0 {1,S} {6,S}
6 N 0 {5,S} {7,S} {8,D}
7 O 0 {6,S}
8 O 0 {6,D}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {1,S}
""",
    product2 = 
"""
HONO
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 N 0 {2,S} {4,D}
4 O 0 {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 70,
    reactant1 = 
"""
CH3ONO2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 0 {1,S} {6,S}
6 N 0 {5,S} {7,S} {8,D}
7 O 0 {6,S}
8 O 0 {6,D}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {1,S}
""",
    product2 = 
"""
NO3
1 N 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 O 0 {1,S}
4 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (15000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5260, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 71,
    reactant1 = 
"""
CH3ONO2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 0 {1,S} {6,S}
6 N 0 {5,S} {7,S} {8,D}
7 O 0 {6,S}
8 O 0 {6,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {1,S}
""",
    product2 = 
"""
HONO2
1 N 0 {2,S} {3,S} {4,D}
2 O 0 {1,S} {5,S}
3 O 0 {1,S}
4 O 0 {1,D}
5 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (490000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2027, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 72,
    reactant1 = 
"""
CH3NO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 N 0 {1,S} {6,D}
6 O 0 {5,D}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH2NO
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 N 0 {1,S} {5,D}
5 O 0 {4,D}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (440000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (378, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 73,
    reactant1 = 
"""
CH3NO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 N 0 {1,S} {6,D}
6 O 0 {5,D}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH2NO
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 N 0 {1,S} {5,D}
5 O 0 {4,D}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (330000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (3616, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 74,
    reactant1 = 
"""
CH3NO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 N 0 {1,S} {6,D}
6 O 0 {5,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2NO
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 N 0 {1,S} {5,D}
5 O 0 {4,D}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3600000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1192, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 75,
    reactant1 = 
"""
CH3NO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 N 0 {1,S} {6,D}
6 O 0 {5,D}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
CH2NO
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 N 0 {1,S} {5,D}
5 O 0 {4,D}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(790000, 'cm^3/(mol*s)'), n=1.9, Ea=(5415, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 76,
    reactant1 = 
"""
CH3NO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 N 0 {1,S} {6,D}
6 O 0 {5,D}
""",
    reactant2 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
CH2NO
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 N 0 {1,S} {5,D}
5 O 0 {4,D}
""",
    product2 = 
"""
NH3
1 N 0 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2800000.0, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (1073, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 77,
    reactant1 = 
"""
CH3NO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 N 0 {1,S} {6,D}
6 O 0 {5,D}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2782, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 78,
    reactant1 = 
"""
CH3NO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 N 0 {1,S} {6,D}
6 O 0 {5,D}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1700000.0, 'cm^3/(mol*s)'), n=2.1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 79,
    reactant1 = 
"""
CH3NO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 N 0 {1,S} {6,D}
6 O 0 {5,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
HONO
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 N 0 {2,S} {4,D}
4 O 0 {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (994, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 80,
    reactant1 = 
"""
CH2NO
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 N 0 {1,S} {5,D}
5 O 0 {4,D}
""",
    product1 = 
"""
HNCO
1 H 0 {2,S}
2 N 0 {1,S} {3,D}
3 C 0 {2,D} {4,D}
4 O 0 {3,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.3e+42, 's^-1'), n=-9.1, Ea=(53838, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 81,
    reactant1 = 
"""
CH2NO
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 N 0 {1,S} {5,D}
5 O 0 {4,D}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 82,
    reactant1 = 
"""
CH2NO
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 N 0 {1,S} {5,D}
5 O 0 {4,D}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
HCNO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T} {4,S}
4 O 0 {3,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (480000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-894, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 83,
    reactant1 = 
"""
CH2NO
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 N 0 {1,S} {5,D}
5 O 0 {4,D}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (70000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 84,
    reactant1 = 
"""
CH2NO
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 N 0 {1,S} {5,D}
5 O 0 {4,D}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
HCNO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T} {4,S}
4 O 0 {3,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (330000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-894, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 85,
    reactant1 = 
"""
CH2NO
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 N 0 {1,S} {5,D}
5 O 0 {4,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 86,
    reactant1 = 
"""
CH2NO
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 N 0 {1,S} {5,D}
5 O 0 {4,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
HCNO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T} {4,S}
4 O 0 {3,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2400000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1192, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 87,
    reactant1 = 
"""
CH2NO
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 N 0 {1,S} {5,D}
5 O 0 {4,D}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+23, 'cm^3/(mol*s)'),
        n = -3.3,
        Ea = (3895, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 88,
    reactant1 = 
"""
CH2NO
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 N 0 {1,S} {5,D}
5 O 0 {4,D}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 89,
    reactant1 = 
"""
CH2NO
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 N 0 {1,S} {5,D}
5 O 0 {4,D}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
HCNO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T} {4,S}
4 O 0 {3,S}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1600000.0, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (-1113, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 90,
    reactant1 = 
"""
H
1 H 1
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
O
1 O 2T
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3600000000000000.0, 'cm^3/(mol*s)'),
        n = -0.4,
        Ea = (16600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 91,
    reactant1 = 
"""
H
1 H 1
""",
    reactant2 = 
"""
H
1 H 1
""",
    reactant3 = 
"""
N2
1 N 0 {2,T}
2 N 0 {1,T}
""",
    product1 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
N2
1 N 0 {2,T}
2 N 0 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.4e+18, 'cm^6/(mol^2*s)'), n=-1.3, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 92,
    reactant1 = 
"""
H
1 H 1
""",
    reactant2 = 
"""
H
1 H 1
""",
    reactant3 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+17, 'cm^6/(mol^2*s)'), n=-0.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 93,
    reactant1 = 
"""
H
1 H 1
""",
    reactant2 = 
"""
H
1 H 1
""",
    reactant3 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+19, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 94,
    reactant1 = 
"""
O
1 O 2T
""",
    reactant2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (3800000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (7948, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (880000000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (19175, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 96,
    reactant1 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
O
1 O 2T
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4300, 'cm^3/(mol*s)'), n=2.7, Ea=(-1822, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 97,
    reactant1 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    reactant2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
H
1 H 1
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (210000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (3449, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 98,
    reactant1 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(740000, 'cm^3/(mol*s)'), n=2.4, Ea=(53502, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 99,
    reactant1 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (84000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (400, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 100,
    reactant1 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product2 = 
"""
O
1 O 2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1400000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 101,
    reactant1 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (16000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-445, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 102,
    reactant1 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (3.6e+21, 'cm^3/(mol*s)'),
                n = -2.1,
                Ea = (9000, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2000000000000000.0, 'cm^3/(mol*s)'),
                n = -0.6,
                Ea = (0, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 104,
    reactant1 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    product2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (190000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (-1408, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (100000000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (11034, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 106,
    reactant1 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3580, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 107,
    reactant1 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1700000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3760, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 108,
    reactant1 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9600000.0, 'cm^3/(mol*s)'), n=2, Ea=(3970, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 109,
    reactant1 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1900000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (427, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(1.6e+18, 'cm^3/(mol*s)'), n=0, Ea=(29410, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 111,
    reactant1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    product2 = 
"""
O
1 O 2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4700000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (60500, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 112,
    reactant1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(160000, 'cm^3/(mol*s)'), n=2.2, Ea=(17943, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 113,
    reactant1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    reactant2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    product1 = 
"""
HOCO
1 O 0 {2,S} {3,S}
2 C 1 {1,S} {4,D}
3 H 0 {1,S}
4 O 0 {2,D}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(36000, 'cm^3/(mol*s)'), n=2.5, Ea=(28660, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 114,
    reactant1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (93000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (0, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(710000, 'cm^3/(mol*s)'), n=1.8, Ea=(1133, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 116,
    reactant1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
HOCO
1 O 0 {2,S} {3,S}
2 C 1 {1,S} {4,D}
3 H 0 {1,S}
4 O 0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+25, 'cm^3/(mol*s)'), n=-6, Ea=(2981, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 117,
    reactant1 = 
"""
HOCO
1 O 0 {2,S} {3,S}
2 C 1 {1,S} {4,D}
3 H 0 {1,S}
4 O 0 {2,D}
""",
    product1 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(3.5e+56, 's^-1'), n=-15, Ea=(46500, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.5e+69, 's^-1'), n=-18, Ea=(60000, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 119,
    reactant1 = 
"""
HOCO
1 O 0 {2,S} {3,S}
2 C 1 {1,S} {4,D}
3 H 0 {1,S}
4 O 0 {2,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (4600000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (-89, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(9500000.0, 'cm^3/(mol*s)'), n=2, Ea=(-89, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 121,
    reactant1 = 
"""
HOCO
1 O 0 {2,S} {3,S}
2 C 1 {1,S} {4,D}
3 H 0 {1,S}
4 O 0 {2,D}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (990000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 122,
    reactant1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (410000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (2444, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 123,
    reactant1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (420000000000.0, 'cm^3/(mol*s)'),
        n = 0.6,
        Ea = (2760, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 124,
    reactant1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(240000, 'cm^3/(mol*s)'), n=2.5, Ea=(36461, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 125,
    reactant1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (78000000.0, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (-1055, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 126,
    reactant1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(41000, 'cm^3/(mol*s)'), n=2.5, Ea=(10206, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 127,
    reactant1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(32, 'cm^3/(mol*s)'), n=3.4, Ea=(4310, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 128,
    reactant1 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product1 = 
"""
H
1 H 1
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(49000000000.0, 's^-1'), n=-0.9, Ea=(16755, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 129,
    reactant1 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (110000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 130,
    reactant1 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 131,
    reactant1 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 132,
    reactant1 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (110000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 133,
    reactant1 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3400000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 134,
    reactant1 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product3 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 135,
    reactant1 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    reactant2 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (27000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 136,
    reactant1 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4100, 'cm^3/(mol*s)'), n=3.2, Ea=(8755, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 137,
    reactant1 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(440000, 'cm^3/(mol*s)'), n=2.5, Ea=(6577, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 138,
    reactant1 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1000000.0, 'cm^3/(mol*s)'),
        n = 2.2,
        Ea = (2506, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 139,
    reactant1 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(47000, 'cm^3/(mol*s)'), n=2.5, Ea=(21000, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 140,
    reactant1 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10030, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 141,
    reactant1 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (43000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 142,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (90000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (15100, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 143,
    reactant1 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (72000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 144,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (69000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 145,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product3 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (15000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 146,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1100, 'cm^3/(mol*s)'), n=3, Ea=(2780, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 147,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (44000000000000.0, 'cm^3/(mol*s)'),
        n = 0.3,
        Ea = (727, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 148,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1800, 'cm^3/(mol*s)'), n=2.8, Ea=(-3730, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 149,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1075, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 150,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {1,S}
""",
    product2 = 
"""
O
1 O 2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (28297, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 151,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (190000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (9842, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 152,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product1 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 153,
    reactant1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product1 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (5600000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (89000, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 154,
    reactant1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product1 = 
"""
C(T)
1 C 4T
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (5800000000000.0, 'cm^3/(mol*s)'),
            n = 0.5,
            Ea = (68500, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 155,
    reactant1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+18, 'cm^3/(mol*s)'), n=-1.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 156,
    reactant1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
H
1 H 1
""",
    product3 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 157,
    reactant1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 158,
    reactant1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000000000000.0, 'cm^3/(mol*s)'),
        n = 0.1,
        Ea = (161, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 159,
    reactant1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(860000, 'cm^3/(mol*s)'), n=2, Ea=(6776, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 160,
    reactant1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (180000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 161,
    reactant1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    product2 = 
"""
H
1 H 1
""",
    product3 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (380000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 162,
    reactant1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (340000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 163,
    reactant1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product3 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (610000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 164,
    reactant1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 165,
    reactant1 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (31000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (430, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 166,
    reactant1 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
N2
1 N 0 {2,T}
2 N 0 {1,T}
""",
    product1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product2 = 
"""
N2
1 N 0 {2,T}
2 N 0 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (13000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (430, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 167,
    reactant1 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (200000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 168,
    reactant1 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 169,
    reactant1 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
H
1 H 1
""",
    product3 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 170,
    reactant1 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 171,
    reactant1 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 172,
    reactant1 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (11000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 173,
    reactant1 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C(T)
1 C 4T
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (150000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 174,
    reactant1 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (57000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 175,
    reactant1 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 176,
    reactant1 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C(T)
1 C 4T
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40000000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (3000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 177,
    reactant1 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
O
1 O 2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (33000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 178,
    reactant1 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    reactant2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5700000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-755, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 179,
    reactant1 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    reactant2 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    product1 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8800000.0, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (-1040, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 180,
    reactant1 = 
"""
C(T)
1 C 4T
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 181,
    reactant1 = 
"""
C(T)
1 C 4T
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
O
1 O 2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 182,
    reactant1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 0 {1,S} {6,S}
6 H 0 {5,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2900000000.0, 'cm^3/(mol*s)'),
        n = 1.2,
        Ea = (4491, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 183,
    reactant1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 0 {1,S} {6,S}
6 H 0 {5,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {1,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (510000000.0, 'cm^3/(mol*s)'),
        n = 1.2,
        Ea = (4491, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 184,
    reactant1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 0 {1,S} {6,S}
6 H 0 {5,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (21000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5305, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 185,
    reactant1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 0 {1,S} {6,S}
6 H 0 {5,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3700000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5305, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 186,
    reactant1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 0 {1,S} {6,S}
6 H 0 {5,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (150000000.0, 'cm^3/(mol*s)'),
        n = 1.4,
        Ea = (113, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 187,
    reactant1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 0 {1,S} {6,S}
6 H 0 {5,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {1,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (27000000.0, 'cm^3/(mol*s)'),
        n = 1.4,
        Ea = (113, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 188,
    reactant1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 0 {1,S} {6,S}
6 H 0 {5,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (15000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 189,
    reactant1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 0 {1,S} {6,S}
6 H 0 {5,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (60000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (46600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 190,
    reactant1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 0 {1,S} {6,S}
6 H 0 {5,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {1,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (60000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (54800, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 191,
    reactant1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 192,
    reactant1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 193,
    reactant1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (66000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-693, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 194,
    reactant1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (24000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 195,
    reactant1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (12000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 196,
    reactant1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (72000000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (3736, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(2.9e+16, 'cm^3/(mol*s)'), n=-1.5, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 198,
    reactant1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 0 {1,S} {6,S}
6 H 0 {5,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 199,
    reactant1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (15000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 200,
    reactant1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 0 {1,S} {6,S}
6 H 0 {5,S}
""",
    product2 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5500, 'cm^3/(mol*s)'), n=2.8, Ea=(5862, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 201,
    reactant1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 0 {1,S} {6,S}
6 H 0 {5,S}
""",
    product2 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4800000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 202,
    reactant1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {1,S}
""",
    product1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 0 {1,S} {6,S}
6 H 0 {5,S}
""",
    product2 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2400000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 203,
    reactant1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 0 {1,S} {6,S}
6 H 0 {5,S}
""",
    product2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(22, 'cm^3/(mol*s)'), n=3.1, Ea=(16227, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 204,
    reactant1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {1,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (53000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (745, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 205,
    reactant1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {1,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4600000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (745, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 206,
    reactant1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {1,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3800000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 207,
    reactant1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {1,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 208,
    reactant1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {1,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 209,
    reactant1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {1,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (22000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1749, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 210,
    reactant1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {1,S}
""",
    reactant2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.5e+25, 'cm^3/(mol*s)'),
        n = -4.9,
        Ea = (9080, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 211,
    reactant1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {1,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (24000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 212,
    reactant1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {1,S}
""",
    reactant2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 0 {1,S} {6,S}
6 H 0 {5,S}
""",
    product2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (130000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (15073, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 213,
    reactant1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {1,S}
""",
    reactant2 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 0 {1,S} {6,S}
6 H 0 {5,S}
""",
    product2 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2981, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 214,
    reactant1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {1,S}
""",
    reactant2 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {1,S}
""",
    product1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 0 {1,S} {6,S}
6 H 0 {5,S}
""",
    product2 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (60000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 215,
    reactant1 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (98000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (9220, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 216,
    reactant1 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1e-07, 'cm^3/(mol*s)'), n=6.5, Ea=(274, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 217,
    reactant1 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9200000.0, 'cm^3/(mol*s)'), n=2, Ea=(990, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 218,
    reactant1 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(110000, 'cm^3/(mol*s)'), n=2.5, Ea=(16850, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 219,
    reactant1 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(730000, 'cm^3/(mol*s)'), n=2.5, Ea=(49160, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 220,
    reactant1 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (56000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (9418, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (840000000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (22250, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 222,
    reactant1 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    reactant2 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (120000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 223,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (54000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (16055, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 224,
    reactant1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (42000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 225,
    reactant1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH3CHO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 O 0 {2,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (53000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 226,
    reactant1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (31000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 227,
    reactant1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (24000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 228,
    reactant1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
CH3CH2O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 O 1 {2,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (31000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 229,
    reactant1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14000000.0, 'cm^3/(mol*s)'),
        n = 1.1,
        Ea = (-1975, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 230,
    reactant1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product1 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    product2 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5500, 'cm^3/(mol*s)'), n=2.8, Ea=(5860, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 231,
    reactant1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product1 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (43000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 232,
    reactant1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (900000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 233,
    reactant1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product1 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    product2 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 234,
    reactant1 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-400, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 235,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (42000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 236,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 237,
    reactant1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C2H3
1 H 0 {2,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {4,S} {5,S}
4 H 0 {3,S}
5 H 0 {3,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(240, 'cm^3/(mol*s)'), n=3.6, Ea=(11266, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 238,
    reactant1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (3900000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (1494, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (62000000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (6855, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 240,
    reactant1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH2CHO
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1700000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (1494, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (28000000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (6855, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 242,
    reactant1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C2H3
1 H 0 {2,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {4,S} {5,S}
4 H 0 {3,S}
5 H 0 {3,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.13, 'cm^3/(mol*s)'), n=4.2, Ea=(-860, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 243,
    reactant1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1800000.0, 'cm^3/(mol*s)'),
        n = 1.7,
        Ea = (2061, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 244,
    reactant1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH3CHO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 O 0 {2,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.024, 'cm^3/(mol*s)'), n=3.9, Ea=(1723, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 245,
    reactant1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2CHOH
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 O 0 {1,S} {7,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
7 H 0 {3,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(320000, 'cm^3/(mol*s)'), n=2.2, Ea=(5256, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 246,
    reactant1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
C2H3
1 H 0 {2,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {4,S} {5,S}
4 H 0 {3,S}
5 H 0 {3,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (71000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (60010, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 247,
    reactant1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
C2H3
1 H 0 {2,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {4,S} {5,S}
4 H 0 {3,S}
5 H 0 {3,S}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (60000000.0, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (16630, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 248,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C2H3
1 H 0 {2,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {4,S} {5,S}
4 H 0 {3,S}
5 H 0 {3,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 249,
    reactant1 = 
"""
C2H3
1 H 0 {2,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {4,S} {5,S}
4 H 0 {3,S}
5 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (45000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 250,
    reactant1 = 
"""
C2H3
1 H 0 {2,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {4,S} {5,S}
4 H 0 {3,S}
5 H 0 {3,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH2CO
1 H 0 {3,S}
2 H 0 {3,S}
3 C 0 {1,S} {2,S} {4,D}
4 C 0 {3,D} {5,D}
5 O 0 {4,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 251,
    reactant1 = 
"""
C2H3
1 H 0 {2,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {4,S} {5,S}
4 H 0 {3,S}
5 H 0 {3,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 252,
    reactant1 = 
"""
C2H3
1 H 0 {2,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {4,S} {5,S}
4 H 0 {3,S}
5 H 0 {3,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
CH2CHO
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 253,
    reactant1 = 
"""
C2H3
1 H 0 {2,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {4,S} {5,S}
4 H 0 {3,S}
5 H 0 {3,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1100000000000000.0, 'cm^3/(mol*s)'),
        n = -0.8,
        Ea = (179, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 254,
    reactant1 = 
"""
C2H3
1 H 0 {2,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {4,S} {5,S}
4 H 0 {3,S}
5 H 0 {3,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH2CHO
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
O
1 O 2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (640000000.0, 'cm^3/(mol*s)'),
        n = 1,
        Ea = (-197, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 255,
    reactant1 = 
"""
C2H3
1 H 0 {2,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {4,S} {5,S}
4 H 0 {3,S}
5 H 0 {3,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.7, 'cm^3/(mol*s)'), n=3.1, Ea=(-272, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 256,
    reactant1 = 
"""
C2H3
1 H 0 {2,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {4,S} {5,S}
4 H 0 {3,S}
5 H 0 {3,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {1,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (54000000000000.0, 'cm^3/(mol*s)'),
        n = -0.8,
        Ea = (179, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 257,
    reactant1 = 
"""
C2H3
1 H 0 {2,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {4,S} {5,S}
4 H 0 {3,S}
5 H 0 {3,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6000000000000.0, 'cm^3/(mol*s)'),
        n = -0.8,
        Ea = (179, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 258,
    reactant1 = 
"""
C2H3
1 H 0 {2,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {4,S} {5,S}
4 H 0 {3,S}
5 H 0 {3,S}
""",
    reactant2 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5400, 'cm^3/(mol*s)'), n=2.8, Ea=(5860, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 259,
    reactant1 = 
"""
C2H3
1 H 0 {2,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {4,S} {5,S}
4 H 0 {3,S}
5 H 0 {3,S}
""",
    reactant2 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (90000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 260,
    reactant1 = 
"""
C2H3
1 H 0 {2,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {4,S} {5,S}
4 H 0 {3,S}
5 H 0 {3,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (21000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 261,
    reactant1 = 
"""
C2H3
1 H 0 {2,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {4,S} {5,S}
4 H 0 {3,S}
5 H 0 {3,S}
""",
    reactant2 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product2 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 262,
    reactant1 = 
"""
C2H3
1 H 0 {2,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {4,S} {5,S}
4 H 0 {3,S}
5 H 0 {3,S}
""",
    reactant2 = 
"""
C2H3
1 H 0 {2,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {4,S} {5,S}
4 H 0 {3,S}
5 H 0 {3,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (15000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 263,
    reactant1 = 
"""
C2H3
1 H 0 {2,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {4,S} {5,S}
4 H 0 {3,S}
5 H 0 {3,S}
""",
    reactant2 = 
"""
C2H
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 1 {2,T}
""",
    product1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    product2 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 264,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
C(T)
1 C 4T
""",
    product1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 265,
    reactant1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 266,
    reactant1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    product2 = 
"""
H
1 H 1
""",
    product3 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (32000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 267,
    reactant1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
HCCO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {4,S}
4 O 1 {3,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14000000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (1900, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 268,
    reactant1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6100000.0, 'cm^3/(mol*s)'), n=2, Ea=(1900, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 269,
    reactant1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
C2H
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 1 {2,T}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3200000000000000.0, 'cm^3/(mol*s)'),
        n = -0.6,
        Ea = (15000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 270,
    reactant1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1300000000.0, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (2579, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 271,
    reactant1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
HCCOH
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {4,S}
4 O 0 {3,S} {5,S}
5 H 0 {4,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2400000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (12713, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 272,
    reactant1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2CO
1 H 0 {3,S}
2 H 0 {3,S}
3 C 0 {1,S} {2,S} {4,D}
4 C 0 {3,D} {5,D}
5 O 0 {4,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7500000.0, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (2106, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 273,
    reactant1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CHCHOH
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 O 0 {1,S} {6,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {3,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1.9e+44, 'cm^3/(mol*s)'),
                n = -11.4,
                Ea = (6299, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3.5e+31, 'cm^3/(mol*s)'),
                n = -6.2,
                Ea = (6635, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 275,
    reactant1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 276,
    reactant1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
CH2CHO
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
O
1 O 2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 277,
    reactant1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (70000000.0, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (30600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 278,
    reactant1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    product2 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 279,
    reactant1 = 
"""
H2CC
1 C 0  {2,S} {3,S} {4,D}
2 H 0  {1,S}
3 H 0  {1,S}
4 C 2S {1,D}
""",
    product1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(10000000.0, 's^-1'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 280,
    reactant1 = 
"""
H2CC
1 C 0  {2,S} {3,S} {4,D}
2 H 0  {1,S}
3 H 0  {1,S}
4 C 2S {1,D}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 281,
    reactant1 = 
"""
H2CC
1 C 0  {2,S} {3,S} {4,D}
2 H 0  {1,S}
3 H 0  {1,S}
4 C 2S {1,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2CO
1 H 0 {3,S}
2 H 0 {3,S}
3 C 0 {1,S} {2,S} {4,D}
4 C 0 {3,D} {5,D}
5 O 0 {4,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 282,
    reactant1 = 
"""
H2CC
1 C 0  {2,S} {3,S} {4,D}
2 H 0  {1,S}
3 H 0  {1,S}
4 C 2S {1,D}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product2 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 283,
    reactant1 = 
"""
C2
1 C 1 {2,T}
2 C 1 {1,T}
""",
    reactant2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C2H
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 1 {2,T}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(400000, 'cm^3/(mol*s)'), n=2.4, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 284,
    reactant1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
C(T)
1 C 4T
""",
    product1 = 
"""
C2H
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 1 {2,T}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 285,
    reactant1 = 
"""
C2H
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 1 {2,T}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 286,
    reactant1 = 
"""
C2H
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 1 {2,T}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
HCCO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {4,S}
4 O 1 {3,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 287,
    reactant1 = 
"""
C2H
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 1 {2,T}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C2
1 C 1 {2,T}
2 C 1 {1,T}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40000000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (8000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 288,
    reactant1 = 
"""
C2H
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 1 {2,T}
""",
    reactant2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(410000, 'cm^3/(mol*s)'), n=2.4, Ea=(864, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 289,
    reactant1 = 
"""
C2H
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 1 {2,T}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product3 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (47000000000000.0, 'cm^3/(mol*s)'),
        n = -0.2,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 290,
    reactant1 = 
"""
C2H
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 1 {2,T}
""",
    reactant2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (976, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 291,
    reactant1 = 
"""
C2
1 C 1 {2,T}
2 C 1 {1,T}
""",
    product1 = 
"""
C(T)
1 C 4T
""",
    product2 = 
"""
C(T)
1 C 4T
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.5e+16, 'cm^3/(mol*s)'), n=0, Ea=(142300, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 292,
    reactant1 = 
"""
C2
1 C 1 {2,T}
2 C 1 {1,T}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
C(T)
1 C 4T
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 293,
    reactant1 = 
"""
C2
1 C 1 {2,T}
2 C 1 {1,T}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C2O
1 C 2S {2,D}
2 C 0  {1,D} {3,D}
3 O 0  {2,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 294,
    reactant1 = 
"""
C2
1 C 1 {2,T}
2 C 1 {1,T}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (980, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 295,
    reactant1 = 
"""
CH3CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,S} {7,S} {8,S}
6 H 0 {5,S}
7 H 0 {5,S}
8 O 0 {5,S} {9,S}
9 H 0 {8,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH3CHOH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,S} {7,S}
3 O 0 {2,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (26000000.0, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (2827, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 296,
    reactant1 = 
"""
CH3CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,S} {7,S} {8,S}
6 H 0 {5,S}
7 H 0 {5,S}
8 O 0 {5,S} {9,S}
9 H 0 {8,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH2CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S}
3 O 0 {1,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (12000000.0, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (5098, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 297,
    reactant1 = 
"""
CH3CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,S} {7,S} {8,S}
6 H 0 {5,S}
7 H 0 {5,S}
8 O 0 {5,S} {9,S}
9 H 0 {8,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH3CH2O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 O 1 {2,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (15000000.0, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (3038, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 298,
    reactant1 = 
"""
CH3CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,S} {7,S} {8,S}
6 H 0 {5,S}
7 H 0 {5,S}
8 O 0 {5,S} {9,S}
9 H 0 {8,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH3CHOH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,S} {7,S}
3 O 0 {2,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (19000000.0, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (1824, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 299,
    reactant1 = 
"""
CH3CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,S} {7,S} {8,S}
6 H 0 {5,S}
7 H 0 {5,S}
8 O 0 {5,S} {9,S}
9 H 0 {8,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH2CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S}
3 O 0 {1,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (94000000.0, 'cm^3/(mol*s)'),
        n = 1.7,
        Ea = (5459, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 300,
    reactant1 = 
"""
CH3CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,S} {7,S} {8,S}
6 H 0 {5,S}
7 H 0 {5,S}
8 O 0 {5,S} {9,S}
9 H 0 {8,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH3CH2O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 O 1 {2,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (16000000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (4448, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 301,
    reactant1 = 
"""
CH3CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,S} {7,S} {8,S}
6 H 0 {5,S}
7 H 0 {5,S}
8 O 0 {5,S} {9,S}
9 H 0 {8,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH3CHOH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,S} {7,S}
3 O 0 {2,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (460000000000.0, 'cm^3/(mol*s)'),
        n = 0.1,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 302,
    reactant1 = 
"""
CH3CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,S} {7,S} {8,S}
6 H 0 {5,S}
7 H 0 {5,S}
8 O 0 {5,S} {9,S}
9 H 0 {8,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S}
3 O 0 {1,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (170000000000.0, 'cm^3/(mol*s)'),
        n = 0.3,
        Ea = (600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 303,
    reactant1 = 
"""
CH3CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,S} {7,S} {8,S}
6 H 0 {5,S}
7 H 0 {5,S}
8 O 0 {5,S} {9,S}
9 H 0 {8,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH3CH2O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 O 1 {2,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (750000000000.0, 'cm^3/(mol*s)'),
        n = 0.3,
        Ea = (1634, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 304,
    reactant1 = 
"""
CH3CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,S} {7,S} {8,S}
6 H 0 {5,S}
7 H 0 {5,S}
8 O 0 {5,S} {9,S}
9 H 0 {8,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
CH3CHOH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,S} {7,S}
3 O 0 {2,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8200, 'cm^3/(mol*s)'), n=2.5, Ea=(10750, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 305,
    reactant1 = 
"""
CH3CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,S} {7,S} {8,S}
6 H 0 {5,S}
7 H 0 {5,S}
8 O 0 {5,S} {9,S}
9 H 0 {8,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
CH2CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S}
3 O 0 {1,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(12000, 'cm^3/(mol*s)'), n=2.5, Ea=(15750, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 306,
    reactant1 = 
"""
CH3CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,S} {7,S} {8,S}
6 H 0 {5,S}
7 H 0 {5,S}
8 O 0 {5,S} {9,S}
9 H 0 {8,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
CH3CH2O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 O 1 {2,S}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (24000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 307,
    reactant1 = 
"""
CH3CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,S} {7,S} {8,S}
6 H 0 {5,S}
7 H 0 {5,S}
8 O 0 {5,S} {9,S}
9 H 0 {8,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
CH3CHOH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,S} {7,S}
3 O 0 {2,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(730, 'cm^3/(mol*s)'), n=3, Ea=(7948, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 308,
    reactant1 = 
"""
CH3CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,S} {7,S} {8,S}
6 H 0 {5,S}
7 H 0 {5,S}
8 O 0 {5,S} {9,S}
9 H 0 {8,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
CH2CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S}
3 O 0 {1,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(220, 'cm^3/(mol*s)'), n=3.2, Ea=(9622, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 309,
    reactant1 = 
"""
CH3CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,S} {7,S} {8,S}
6 H 0 {5,S}
7 H 0 {5,S}
8 O 0 {5,S} {9,S}
9 H 0 {8,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
CH3CH2O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 O 1 {2,S}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(150, 'cm^3/(mol*s)'), n=3, Ea=(7649, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 310,
    reactant1 = 
"""
CH3CHOH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,S} {7,S}
3 O 0 {2,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product1 = 
"""
CH3CHO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 O 0 {2,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (100000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (25000, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 311,
    reactant1 = 
"""
CH3CHOH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,S} {7,S}
3 O 0 {2,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH3CHO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 O 0 {2,D}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 312,
    reactant1 = 
"""
CH3CHOH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,S} {7,S}
3 O 0 {2,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 313,
    reactant1 = 
"""
CH3CHOH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,S} {7,S}
3 O 0 {2,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 314,
    reactant1 = 
"""
CH3CHOH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,S} {7,S}
3 O 0 {2,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH3CHO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 O 0 {2,D}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 315,
    reactant1 = 
"""
CH3CHOH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,S} {7,S}
3 O 0 {2,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
CH3CHO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 O 0 {2,D}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product3 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 316,
    reactant1 = 
"""
CH3CHOH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,S} {7,S}
3 O 0 {2,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH3CHO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 O 0 {2,D}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (8400000000000000.0, 'cm^3/(mol*s)'),
                n = -1.2,
                Ea = (0, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (480000000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (5017, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 318,
    reactant1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S}
3 O 0 {1,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(6e+37, 'cm^3/(mol*s)'), n=-8.1, Ea=(8043, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (7.3e+23, 'cm^3/(mol*s)'),
                n = -6.9,
                Ea = (2855, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 320,
    reactant1 = 
"""
CH2CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S}
3 O 0 {1,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 321,
    reactant1 = 
"""
CH2CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S}
3 O 0 {1,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 322,
    reactant1 = 
"""
CH2CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S}
3 O 0 {1,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2CHOH
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 O 0 {1,S} {7,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
7 H 0 {3,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (24000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 323,
    reactant1 = 
"""
CH2CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S}
3 O 0 {1,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
CH3CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,S} {7,S} {8,S}
6 H 0 {5,S}
7 H 0 {5,S}
8 O 0 {5,S} {9,S}
9 H 0 {8,S}
""",
    product2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 324,
    reactant1 = 
"""
CH2CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S}
3 O 0 {1,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product3 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 325,
    reactant1 = 
"""
CH2CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S}
3 O 0 {1,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH2CHOH
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 O 0 {1,S} {7,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
7 H 0 {3,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14000000.0, 'cm^3/(mol*s)'),
        n = 1.1,
        Ea = (-1975, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 326,
    reactant1 = 
"""
CH3CH2O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 O 1 {2,S}
""",
    product1 = 
"""
CH3CHO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 O 0 {2,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(13000000000000.0, 's^-1'), n=0, Ea=(20060, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 327,
    reactant1 = 
"""
CH3CH2O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 O 1 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH3CHO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 O 0 {2,D}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 328,
    reactant1 = 
"""
CH3CH2O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 O 1 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH3CHO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 O 0 {2,D}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 329,
    reactant1 = 
"""
CH3CH2O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 O 1 {2,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH3CHO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 O 0 {2,D}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (15000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (645, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 330,
    reactant1 = 
"""
CH3CH2O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 O 1 {2,S}
""",
    reactant2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.5e+25, 'cm^3/(mol*s)'),
        n = -4.9,
        Ea = (9080, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 331,
    reactant1 = 
"""
CH3CHO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 O 0 {2,D}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH3CO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 O 0 {2,D}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (47000000000000.0, 'cm^3/(mol*s)'),
        n = -0.3,
        Ea = (3000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 332,
    reactant1 = 
"""
CH3CHO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 O 0 {2,D}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH2CHO
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1900000000000.0, 'cm^3/(mol*s)'),
        n = 0.4,
        Ea = (5359, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 333,
    reactant1 = 
"""
CH3CHO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 O 0 {2,D}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH3CO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 O 0 {2,D}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+18, 'cm^3/(mol*s)'),
        n = -1.9,
        Ea = (2975, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 334,
    reactant1 = 
"""
CH3CHO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 O 0 {2,D}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH2CHO
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (37000000000000.0, 'cm^3/(mol*s)'),
        n = -0.2,
        Ea = (3556, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 335,
    reactant1 = 
"""
CH3CHO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 O 0 {2,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH3CO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 O 0 {2,D}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (240000000000.0, 'cm^3/(mol*s)'),
        n = 0.3,
        Ea = (-1000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 336,
    reactant1 = 
"""
CH3CHO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 O 0 {2,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2CHO
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = -0.6,
        Ea = (800, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 337,
    reactant1 = 
"""
CH3CHO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 O 0 {2,D}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
CH3CO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 O 0 {2,D}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+19, 'cm^3/(mol*s)'),
        n = -2.2,
        Ea = (14030, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 338,
    reactant1 = 
"""
CH3CHO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 O 0 {2,D}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
CH2CHO
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (230000000000.0, 'cm^3/(mol*s)'),
        n = 0.4,
        Ea = (14864, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 339,
    reactant1 = 
"""
CH3CHO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 O 0 {2,D}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH3CO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 O 0 {2,D}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(120000, 'cm^3/(mol*s)'), n=2.5, Ea=(37554, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 340,
    reactant1 = 
"""
CH3CHO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 O 0 {2,D}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
CH3CO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 O 0 {2,D}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.9e-07, 'cm^3/(mol*s)'), n=5.8, Ea=(2200, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 341,
    reactant1 = 
"""
CH3CHO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 O 0 {2,D}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
CH2CHO
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(25, 'cm^3/(mol*s)'), n=3.1, Ea=(5727, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 342,
    reactant1 = 
"""
CH2CHOH
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 O 0 {1,S} {7,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
7 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CHCHOH
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 O 0 {1,S} {6,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {3,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(240, 'cm^3/(mol*s)'), n=3.6, Ea=(11266, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 343,
    reactant1 = 
"""
CH2CHOH
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 O 0 {1,S} {7,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
7 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH2CHO
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (15000000.0, 'cm^3/(mol*s)'),
        n = 1.7,
        Ea = (3000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 344,
    reactant1 = 
"""
CH2CHOH
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 O 0 {1,S} {7,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
7 H 0 {3,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (3900000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (1494, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (62000000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (6855, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 346,
    reactant1 = 
"""
CH2CHOH
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 O 0 {1,S} {7,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
7 H 0 {3,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH2CHO
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (16000000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (4400, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 347,
    reactant1 = 
"""
CH2CHOH
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 O 0 {1,S} {7,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
7 H 0 {3,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CHCHOH
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 O 0 {1,S} {6,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {3,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.13, 'cm^3/(mol*s)'), n=4.2, Ea=(-860, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 348,
    reactant1 = 
"""
CH2CHOH
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 O 0 {1,S} {7,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
7 H 0 {3,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2CHO
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (750000000000.0, 'cm^3/(mol*s)'),
        n = 0.3,
        Ea = (1600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 349,
    reactant1 = 
"""
CH2CHOH
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 O 0 {1,S} {7,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
7 H 0 {3,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product3 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (35000000.0, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (39000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 350,
    reactant1 = 
"""
CH2CHO
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {2,S}
6 H 0 {2,S}
""",
    product1 = 
"""
CH2CO
1 H 0 {3,S}
2 H 0 {3,S}
3 C 0 {1,S} {2,S} {4,D}
4 C 0 {3,D} {5,D}
5 O 0 {4,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+25, 's^-1'), n=-4.8, Ea=(43424, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 351,
    reactant1 = 
"""
CH2CHO
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {2,S}
6 H 0 {2,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+30, 's^-1'), n=-6.1, Ea=(41332, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 352,
    reactant1 = 
"""
CH2CHO
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 353,
    reactant1 = 
"""
CH2CHO
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH3CO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 O 0 {2,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 354,
    reactant1 = 
"""
CH2CHO
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH2CO
1 H 0 {3,S}
2 H 0 {3,S}
3 C 0 {1,S} {2,S} {4,D}
4 C 0 {3,D} {5,D}
5 O 0 {4,D}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 355,
    reactant1 = 
"""
CH2CHO
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH2CO
1 H 0 {3,S}
2 H 0 {3,S}
3 C 0 {1,S} {2,S} {4,D}
4 C 0 {3,D} {5,D}
5 O 0 {4,D}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 356,
    reactant1 = 
"""
CH2CHO
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2CO
1 H 0 {3,S}
2 H 0 {3,S}
3 C 0 {1,S} {2,S} {4,D}
4 C 0 {3,D} {5,D}
5 O 0 {4,D}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 357,
    reactant1 = 
"""
CH2CHO
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 358,
    reactant1 = 
"""
CH2CHO
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product3 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.7e+17, 'cm^3/(mol*s)'),
        n = -1.8,
        Ea = (11067, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 359,
    reactant1 = 
"""
CH2CHO
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product3 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7000000000000.0, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 360,
    reactant1 = 
"""
CH2CHO
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
CH3CHO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 O 0 {2,D}
""",
    product2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3000000000000.0, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 361,
    reactant1 = 
"""
CH2CHO
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product3 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (490000000000000.0, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 362,
    reactant1 = 
"""
CH2CHO
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 363,
    reactant1 = 
"""
CH2CHO
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C2H3
1 H 0 {2,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {4,S} {5,S}
4 H 0 {3,S}
5 H 0 {3,S}
""",
    product2 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 364,
    reactant1 = 
"""
CH3CO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 O 0 {2,D}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (690000000000000.0, 's^-1'),
        n = -2,
        Ea = (14584, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 365,
    reactant1 = 
"""
CH3CO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 O 0 {2,D}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (21000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 366,
    reactant1 = 
"""
CH3CO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 O 0 {2,D}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH2CO
1 H 0 {3,S}
2 H 0 {3,S}
3 C 0 {1,S} {2,S} {4,D}
4 C 0 {3,D} {5,D}
5 O 0 {4,D}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (12000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 367,
    reactant1 = 
"""
CH3CO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 O 0 {2,D}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (160000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 368,
    reactant1 = 
"""
CH3CO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 O 0 {2,D}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH2CO
1 H 0 {3,S}
2 H 0 {3,S}
3 C 0 {1,S} {2,S} {4,D}
4 C 0 {3,D} {5,D}
5 O 0 {4,D}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (53000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 369,
    reactant1 = 
"""
CH3CO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 O 0 {2,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2CO
1 H 0 {3,S}
2 H 0 {3,S}
3 C 0 {1,S} {2,S} {4,D}
4 C 0 {3,D} {5,D}
5 O 0 {4,D}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (12000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 370,
    reactant1 = 
"""
CH3CO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 O 0 {2,D}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (33000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 371,
    reactant1 = 
"""
CH3CO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 O 0 {2,D}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
CH2CO
1 H 0 {3,S}
2 H 0 {3,S}
3 C 0 {1,S} {2,S} {4,D}
4 C 0 {3,D} {5,D}
5 O 0 {4,D}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (53000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 372,
    reactant1 = 
"""
CH3CO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 O 0 {2,D}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product3 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1900000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 373,
    reactant1 = 
"""
CH2CO
1 H 0 {3,S}
2 H 0 {3,S}
3 C 0 {1,S} {2,S} {4,D}
4 C 0 {3,D} {5,D}
5 O 0 {4,D}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (33000000000.0, 'cm^3/(mol*s)'),
        n = 0.9,
        Ea = (2840, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 374,
    reactant1 = 
"""
CH2CO
1 H 0 {3,S}
2 H 0 {3,S}
3 C 0 {1,S} {2,S} {4,D}
4 C 0 {3,D} {5,D}
5 O 0 {4,D}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
HCCO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {4,S}
4 O 1 {3,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (10000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 375,
    reactant1 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    reactant2 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product1 = 
"""
CH2CO
1 H 0 {3,S}
2 H 0 {3,S}
3 C 0 {1,S} {2,S} {4,D}
4 C 0 {3,D} {5,D}
5 O 0 {4,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (95000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-517, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 376,
    reactant1 = 
"""
CH2CO
1 H 0 {3,S}
2 H 0 {3,S}
3 C 0 {1,S} {2,S} {4,D}
4 C 0 {3,D} {5,D}
5 O 0 {4,D}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    product2 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1800000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1350, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 377,
    reactant1 = 
"""
CH2CO
1 H 0 {3,S}
2 H 0 {3,S}
3 C 0 {1,S} {2,S} {4,D}
4 C 0 {3,D} {5,D}
5 O 0 {4,D}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
HCCO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {4,S}
4 O 1 {3,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (10000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 378,
    reactant1 = 
"""
CH2CO
1 H 0 {3,S}
2 H 0 {3,S}
3 C 0 {1,S} {2,S} {4,D}
4 C 0 {3,D} {5,D}
5 O 0 {4,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1013, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 379,
    reactant1 = 
"""
CH2CO
1 H 0 {3,S}
2 H 0 {3,S}
3 C 0 {1,S} {2,S} {4,D}
4 C 0 {3,D} {5,D}
5 O 0 {4,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (670000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1013, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 380,
    reactant1 = 
"""
CH2CO
1 H 0 {3,S}
2 H 0 {3,S}
3 C 0 {1,S} {2,S} {4,D}
4 C 0 {3,D} {5,D}
5 O 0 {4,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
HCCO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {4,S}
4 O 1 {3,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (3000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 381,
    reactant1 = 
"""
CH2CO
1 H 0 {3,S}
2 H 0 {3,S}
3 C 0 {1,S} {2,S} {4,D}
4 C 0 {3,D} {5,D}
5 O 0 {4,D}
""",
    reactant2 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (160000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 382,
    reactant1 = 
"""
HCCOH
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {4,S}
4 O 0 {3,S} {5,S}
5 H 0 {4,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
HCCO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {4,S}
4 O 1 {3,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (1000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 383,
    reactant1 = 
"""
HCCOH
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {4,S}
4 O 0 {3,S} {5,S}
5 H 0 {4,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
HCCO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {4,S}
4 O 1 {3,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (1900, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 384,
    reactant1 = 
"""
HCCOH
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {4,S}
4 O 0 {3,S} {5,S}
5 H 0 {4,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
HCCO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {4,S}
4 O 1 {3,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (1000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 385,
    reactant1 = 
"""
HCCO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {4,S}
4 O 1 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (150000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 386,
    reactant1 = 
"""
HCCO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {4,S}
4 O 1 {3,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product3 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 387,
    reactant1 = 
"""
HCCO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {4,S}
4 O 1 {3,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 388,
    reactant1 = 
"""
HCCO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {4,S}
4 O 1 {3,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C2O
1 C 2S {2,D}
2 C 0  {1,D} {3,D}
3 O 0  {2,D}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (60000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 389,
    reactant1 = 
"""
HCCO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {4,S}
4 O 1 {3,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product3 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4900000000000.0, 'cm^3/(mol*s)'),
        n = -0.1,
        Ea = (1150, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 390,
    reactant1 = 
"""
HCCO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {4,S}
4 O 1 {3,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product3 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (160000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1020, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 391,
    reactant1 = 
"""
HCCO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {4,S}
4 O 1 {3,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product3 = 
"""
O
1 O 2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(220, 'cm^3/(mol*s)'), n=2.7, Ea=(3540, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 392,
    reactant1 = 
"""
HCCO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {4,S}
4 O 1 {3,S}
""",
    reactant2 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product1 = 
"""
C2H3
1 H 0 {2,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {4,S} {5,S}
4 H 0 {3,S}
5 H 0 {3,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 393,
    reactant1 = 
"""
HCCO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {4,S}
4 O 1 {3,S}
""",
    reactant2 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 394,
    reactant1 = 
"""
HCCO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {4,S}
4 O 1 {3,S}
""",
    reactant2 = 
"""
HCCO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {4,S}
4 O 1 {3,S}
""",
    product1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product3 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 395,
    reactant1 = 
"""
C2O
1 C 2S {2,D}
2 C 0  {1,D} {3,D}
3 O 0  {2,D}
""",
    product1 = 
"""
C(T)
1 C 4T
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (2000000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (44200, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 396,
    reactant1 = 
"""
C2O
1 C 2S {2,D}
2 C 0  {1,D} {3,D}
3 O 0  {2,D}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (13000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 397,
    reactant1 = 
"""
C2O
1 C 2S {2,D}
2 C 0  {1,D} {3,D}
3 O 0  {2,D}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (52000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 398,
    reactant1 = 
"""
C2O
1 C 2S {2,D}
2 C 0  {1,D} {3,D}
3 O 0  {2,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product3 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 399,
    reactant1 = 
"""
C2O
1 C 2S {2,D}
2 C 0  {1,D} {3,D}
3 O 0  {2,D}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product3 = 
"""
O
1 O 2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 400,
    reactant1 = 
"""
C2O
1 C 2S {2,D}
2 C 0  {1,D} {3,D}
3 O 0  {2,D}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 401,
    reactant1 = 
"""
C2O
1 C 2S {2,D}
2 C 0  {1,D} {3,D}
3 O 0  {2,D}
""",
    reactant2 = 
"""
C(T)
1 C 4T
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
C2
1 C 1 {2,T}
2 C 1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 402,
    reactant1 = 
"""
OCHCHO
1 O 0 {2,D}
2 C 0 {1,D} {3,S} {4,S}
3 H 0 {2,S}
4 C 0 {2,S} {5,S} {6,D}
5 H 0 {4,S}
6 O 0 {4,D}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 403,
    reactant1 = 
"""
OCHCHO
1 O 0 {2,D}
2 C 0 {1,D} {3,S} {4,S}
3 H 0 {2,S}
4 C 0 {2,S} {5,S} {6,D}
5 H 0 {4,S}
6 O 0 {4,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product3 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6600000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 404,
    reactant1 = 
"""
NH3
1 N 0 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(2.2e+16, 'cm^3/(mol*s)'), n=0, Ea=(93470, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 405,
    reactant1 = 
"""
NH3
1 N 0 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(640000, 'cm^3/(mol*s)'), n=2.4, Ea=(10171, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 406,
    reactant1 = 
"""
NH3
1 N 0 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9400000.0, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (6460, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 407,
    reactant1 = 
"""
NH3
1 N 0 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2000000.0, 'cm^3/(mol*s)'), n=2, Ea=(566, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 408,
    reactant1 = 
"""
NH3
1 N 0 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (22000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 409,
    reactant1 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
NH
1 N 2S {2,S}
2 H 0  {1,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(720000, 'cm^3/(mol*s)'), n=2.3, Ea=(799, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 410,
    reactant1 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (66000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 411,
    reactant1 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
NH
1 N 2S {2,S}
2 H 0  {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (7000000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (0, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(0.86, 'cm^3/(mol*s)'), n=4, Ea=(1673, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 413,
    reactant1 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
NH
1 N 2S {2,S}
2 H 0  {1,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4000000.0, 'cm^3/(mol*s)'), n=2, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 414,
    reactant1 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
H2NO
1 N 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 415,
    reactant1 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
NH3
1 N 0 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(920000, 'cm^3/(mol*s)'), n=1.9, Ea=(-1152, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 416,
    reactant1 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
H2NO
1 N 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
O
1 O 2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (250000000000.0, 'cm^3/(mol*s)'),
        n = 0.5,
        Ea = (29586, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 417,
    reactant1 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (62000000.0, 'cm^3/(mol*s)'),
        n = 1.2,
        Ea = (35100, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 418,
    reactant1 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    reactant2 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
NH3
1 N 0 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
NH
1 N 2S {2,S}
2 H 0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 419,
    reactant1 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    reactant2 = 
"""
NH
1 N 2S {2,S}
2 H 0  {1,S}
""",
    product1 = 
"""
NH3
1 N 0 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
N
1 N 3
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(920000, 'cm^3/(mol*s)'), n=1.9, Ea=(2444, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 420,
    reactant1 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    reactant2 = 
"""
N
1 N 3
""",
    product1 = 
"""
N2
1 N 0 {2,T}
2 N 0 {1,T}
""",
    product2 = 
"""
H
1 H 1
""",
    product3 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (70000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 421,
    reactant1 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    reactant2 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product1 = 
"""
NH3
1 N 0 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3600000.0, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (-1250, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 422,
    reactant1 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    reactant2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product1 = 
"""
N2
1 N 0 {2,T}
2 N 0 {1,T}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+20, 'cm^3/(mol*s)'),
        n = -2.7,
        Ea = (1258, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 423,
    reactant1 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    reactant2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product1 = 
"""
NNH
1 N 1 {2,D}
2 N 0 {1,D} {3,S}
3 H 0 {2,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (23000000000.0, 'cm^3/(mol*s)'),
        n = 0.4,
        Ea = (-814, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 424,
    reactant1 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    reactant2 = 
"""
HONO
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 N 0 {2,S} {4,D}
4 O 0 {3,D}
""",
    product1 = 
"""
NH3
1 N 0 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(71, 'cm^3/(mol*s)'), n=3, Ea=(-4940, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 425,
    reactant1 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
N2O
1 N 0 {2,D} {3,D}
2 N 0 {1,D}
3 O 0 {1,D}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+16, 'cm^3/(mol*s)'), n=-1.4, Ea=(268, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 426,
    reactant1 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
H2NO
1 N 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.5e+16, 'cm^3/(mol*s)'), n=-1.4, Ea=(268, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 427,
    reactant1 = 
"""
NH
1 N 2S {2,S}
2 H 0  {1,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
N
1 N 3
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 428,
    reactant1 = 
"""
NH
1 N 2S {2,S}
2 H 0  {1,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (92000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 429,
    reactant1 = 
"""
NH
1 N 2S {2,S}
2 H 0  {1,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 430,
    reactant1 = 
"""
NH
1 N 2S {2,S}
2 H 0  {1,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
N
1 N 3
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (500000000000.0, 'cm^3/(mol*s)'),
        n = 0.5,
        Ea = (2000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 431,
    reactant1 = 
"""
NH
1 N 2S {2,S}
2 H 0  {1,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
O
1 O 2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(460000, 'cm^3/(mol*s)'), n=2, Ea=(6500, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 432,
    reactant1 = 
"""
NH
1 N 2S {2,S}
2 H 0  {1,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1300000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (100, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 433,
    reactant1 = 
"""
NH
1 N 2S {2,S}
2 H 0  {1,S}
""",
    reactant2 = 
"""
NH
1 N 2S {2,S}
2 H 0  {1,S}
""",
    product1 = 
"""
N2
1 N 0 {2,T}
2 N 0 {1,T}
""",
    product2 = 
"""
H
1 H 1
""",
    product3 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (25000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 434,
    reactant1 = 
"""
NH
1 N 2S {2,S}
2 H 0  {1,S}
""",
    reactant2 = 
"""
N
1 N 3
""",
    product1 = 
"""
N2
1 N 0 {2,T}
2 N 0 {1,T}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 435,
    reactant1 = 
"""
NH
1 N 2S {2,S}
2 H 0  {1,S}
""",
    reactant2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product1 = 
"""
N2O
1 N 0 {2,D} {3,D}
2 N 0 {1,D}
3 O 0 {1,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (290000000000000.0, 'cm^3/(mol*s)'),
        n = -0.4,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 436,
    reactant1 = 
"""
NH
1 N 2S {2,S}
2 H 0  {1,S}
""",
    reactant2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product1 = 
"""
N2
1 N 0 {2,T}
2 N 0 {1,T}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (22000000000000.0, 'cm^3/(mol*s)'),
        n = -0.2,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 437,
    reactant1 = 
"""
NH
1 N 2S {2,S}
2 H 0  {1,S}
""",
    reactant2 = 
"""
HONO
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 N 0 {2,S} {4,D}
4 O 0 {3,D}
""",
    product1 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 438,
    reactant1 = 
"""
NH
1 N 2S {2,S}
2 H 0  {1,S}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
N2O
1 N 0 {2,D} {3,D}
2 N 0 {1,D}
3 O 0 {1,D}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 439,
    reactant1 = 
"""
N
1 N 3
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (38000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 440,
    reactant1 = 
"""
N
1 N 3
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product2 = 
"""
O
1 O 2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6400000000.0, 'cm^3/(mol*s)'),
        n = 1,
        Ea = (6280, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 441,
    reactant1 = 
"""
N
1 N 3
""",
    reactant2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product1 = 
"""
N2
1 N 0 {2,T}
2 N 0 {1,T}
""",
    product2 = 
"""
O
1 O 2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (21000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 442,
    reactant1 = 
"""
NNH
1 N 1 {2,D}
2 N 0 {1,D} {3,S}
3 H 0 {2,S}
""",
    product1 = 
"""
N2
1 N 0 {2,T}
2 N 0 {1,T}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(65000000.0, 's^-1'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 443,
    reactant1 = 
"""
NNH
1 N 1 {2,D}
2 N 0 {1,D} {3,S}
3 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
N2
1 N 0 {2,T}
2 N 0 {1,T}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 444,
    reactant1 = 
"""
NNH
1 N 1 {2,D}
2 N 0 {1,D} {3,S}
3 H 0 {2,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
N2O
1 N 0 {2,D} {3,D}
2 N 0 {1,D}
3 O 0 {1,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 445,
    reactant1 = 
"""
NNH
1 N 1 {2,D}
2 N 0 {1,D} {3,S}
3 H 0 {2,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
N2
1 N 0 {2,T}
2 N 0 {1,T}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (80000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 446,
    reactant1 = 
"""
NNH
1 N 1 {2,D}
2 N 0 {1,D} {3,S}
3 H 0 {2,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
NH
1 N 2S {2,S}
2 H 0  {1,S}
""",
    product2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 447,
    reactant1 = 
"""
NNH
1 N 1 {2,D}
2 N 0 {1,D} {3,S}
3 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
N2
1 N 0 {2,T}
2 N 0 {1,T}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 448,
    reactant1 = 
"""
NNH
1 N 1 {2,D}
2 N 0 {1,D} {3,S}
3 H 0 {2,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
N2
1 N 0 {2,T}
2 N 0 {1,T}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (200000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 449,
    reactant1 = 
"""
NNH
1 N 1 {2,D}
2 N 0 {1,D} {3,S}
3 H 0 {2,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
N2
1 N 0 {2,T}
2 N 0 {1,T}
""",
    product2 = 
"""
H
1 H 1
""",
    product3 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 450,
    reactant1 = 
"""
NNH
1 N 1 {2,D}
2 N 0 {1,D} {3,S}
3 H 0 {2,S}
""",
    reactant2 = 
"""
NH
1 N 2S {2,S}
2 H 0  {1,S}
""",
    product1 = 
"""
N2
1 N 0 {2,T}
2 N 0 {1,T}
""",
    product2 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 451,
    reactant1 = 
"""
NNH
1 N 1 {2,D}
2 N 0 {1,D} {3,S}
3 H 0 {2,S}
""",
    reactant2 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
N2
1 N 0 {2,T}
2 N 0 {1,T}
""",
    product2 = 
"""
NH3
1 N 0 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 452,
    reactant1 = 
"""
NNH
1 N 1 {2,D}
2 N 0 {1,D} {3,S}
3 H 0 {2,S}
""",
    reactant2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product1 = 
"""
N2
1 N 0 {2,T}
2 N 0 {1,T}
""",
    product2 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 453,
    reactant1 = 
"""
H2NO
1 N 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (2000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 454,
    reactant1 = 
"""
H2NO
1 N 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 455,
    reactant1 = 
"""
H2NO
1 N 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (2000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 456,
    reactant1 = 
"""
H2NO
1 N 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (1000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 457,
    reactant1 = 
"""
H2NO
1 N 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(29000, 'cm^3/(mol*s)'), n=2.7, Ea=(-1600, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 458,
    reactant1 = 
"""
H2NO
1 N 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (25000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 459,
    reactant1 = 
"""
H2NO
1 N 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    reactant2 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
NH3
1 N 0 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 460,
    reactant1 = 
"""
H2NO
1 N 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    reactant2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product1 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(20000, 'cm^3/(mol*s)'), n=2, Ea=(13000, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 461,
    reactant1 = 
"""
H2NO
1 N 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
HONO
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 N 0 {2,S} {4,D}
4 O 0 {3,D}
""",
    product2 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (600000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 462,
    reactant1 = 
"""
HNOH
1 N 1 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 463,
    reactant1 = 
"""
HNOH
1 N 1 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (480000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (378, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 464,
    reactant1 = 
"""
HNOH
1 N 1 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (70000000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (0, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (330000000.0, 'cm^3/(mol*s)'),
                n = 1.5,
                Ea = (-358, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 466,
    reactant1 = 
"""
HNOH
1 N 1 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2400000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1192, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 467,
    reactant1 = 
"""
HNOH
1 N 1 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(29000, 'cm^3/(mol*s)'), n=2.7, Ea=(-1600, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 468,
    reactant1 = 
"""
HNOH
1 N 1 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (25000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 469,
    reactant1 = 
"""
HNOH
1 N 1 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
N2H3
1 N 0 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 N 1 {1,S} {5,S}
5 H 0 {4,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(10, 'cm^3/(mol*s)'), n=3.5, Ea=(-467, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 470,
    reactant1 = 
"""
HNOH
1 N 1 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
H2NN
1 H 0  {3,S}
2 H 0  {3,S}
3 N 0  {1,S} {2,S} {4,S}
4 N 2S {3,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.8e+16, 'cm^3/(mol*s)'),
        n = -1.1,
        Ea = (1113, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 471,
    reactant1 = 
"""
HNOH
1 N 1 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
NH3
1 N 0 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1800000.0, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (-1152, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 472,
    reactant1 = 
"""
HNOH
1 N 1 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
HONO
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 N 0 {2,S} {4,D}
4 O 0 {3,D}
""",
    product2 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (600000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 473,
    reactant1 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (440000000000.0, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (650, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 474,
    reactant1 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (23000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 475,
    reactant1 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (36000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 476,
    reactant1 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (16000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 477,
    reactant1 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    reactant2 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product1 = 
"""
N2O
1 N 0 {2,D} {3,D}
2 N 0 {1,D}
3 O 0 {1,D}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (900000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3100, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 478,
    reactant1 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
HONO
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 N 0 {2,S} {4,D}
4 O 0 {3,D}
""",
    product2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(44000, 'cm^3/(mol*s)'), n=2.6, Ea=(4040, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 479,
    reactant1 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-497, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 480,
    reactant1 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (130000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (362, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 481,
    reactant1 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (110000000000000.0, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 482,
    reactant1 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
HONO
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 N 0 {2,S} {4,D}
4 O 0 {3,D}
""",
    product2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.9, 'cm^3/(mol*s)'), n=3.3, Ea=(3044, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 483,
    reactant1 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
HNO2
1 H 0 {2,S}
2 N 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {2,S}
""",
    product2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(19, 'cm^3/(mol*s)'), n=3.3, Ea=(4983, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 484,
    reactant1 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    reactant2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
HONO
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 N 0 {2,S} {4,D}
4 O 0 {3,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(13000, 'cm^3/(mol*s)'), n=2.8, Ea=(29770, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 485,
    reactant1 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    reactant2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
HNO2
1 H 0 {2,S}
2 N 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {2,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4, 'cm^3/(mol*s)'), n=3.7, Ea=(32400, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 486,
    reactant1 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product3 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (27599, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 487,
    reactant1 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
NO3
1 N 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 O 0 {1,S}
4 O 1 {1,S}
""",
    product2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9600000000.0, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (20900, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 488,
    reactant1 = 
"""
HONO
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 N 0 {2,S} {4,D}
4 O 0 {3,D}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (56000000000.0, 'cm^3/(mol*s)'),
        n = 0.9,
        Ea = (5000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 489,
    reactant1 = 
"""
HONO
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 N 0 {2,S} {4,D}
4 O 0 {3,D}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8100000.0, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (3850, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 490,
    reactant1 = 
"""
HONO
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 N 0 {2,S} {4,D}
4 O 0 {3,D}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (12000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5960, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 491,
    reactant1 = 
"""
HONO
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 N 0 {2,S} {4,D}
4 O 0 {3,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1700000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-520, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 492,
    reactant1 = 
"""
HONO
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 N 0 {2,S} {4,D}
4 O 0 {3,D}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
HONO2
1 N 0 {2,S} {3,S} {4,D}
2 O 0 {1,S} {5,S}
3 O 0 {1,S}
4 O 0 {1,D}
5 H 0 {2,S}
""",
    product2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (32700, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 493,
    reactant1 = 
"""
HONO
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 N 0 {2,S} {4,D}
4 O 0 {3,D}
""",
    reactant2 = 
"""
HONO
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 N 0 {2,S} {4,D}
4 O 0 {3,D}
""",
    product1 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product3 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.35, 'cm^3/(mol*s)'), n=3.6, Ea=(12140, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 494,
    reactant1 = 
"""
HNO2
1 H 0 {2,S}
2 N 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {2,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (170000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (2000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 495,
    reactant1 = 
"""
HNO2
1 H 0 {2,S}
2 N 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 496,
    reactant1 = 
"""
NO3
1 N 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 O 0 {1,S}
4 O 1 {1,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (60000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 497,
    reactant1 = 
"""
NO3
1 N 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 O 0 {1,S}
4 O 1 {1,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 498,
    reactant1 = 
"""
NO3
1 N 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 O 0 {1,S}
4 O 1 {1,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 499,
    reactant1 = 
"""
NO3
1 N 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 O 0 {1,S}
4 O 1 {1,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product3 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 500,
    reactant1 = 
"""
NO3
1 N 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 O 0 {1,S}
4 O 1 {1,S}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product3 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2940, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 501,
    reactant1 = 
"""
HONO2
1 N 0 {2,S} {3,S} {4,D}
2 O 0 {1,S} {5,S}
3 O 0 {1,S}
4 O 0 {1,D}
5 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
NO3
1 N 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 O 0 {1,S}
4 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (560000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (16400, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 502,
    reactant1 = 
"""
HONO2
1 N 0 {2,S} {3,S} {4,D}
2 O 0 {1,S} {5,S}
3 O 0 {1,S}
4 O 0 {1,D}
5 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(61, 'cm^3/(mol*s)'), n=3.3, Ea=(6285, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 503,
    reactant1 = 
"""
HONO2
1 N 0 {2,S} {3,S} {4,D}
2 O 0 {1,S} {5,S}
3 O 0 {1,S}
4 O 0 {1,D}
5 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
HONO
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 N 0 {2,S} {4,D}
4 O 0 {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(380000, 'cm^3/(mol*s)'), n=2.3, Ea=(6976, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 504,
    reactant1 = 
"""
HONO2
1 N 0 {2,S} {3,S} {4,D}
2 O 0 {1,S} {5,S}
3 O 0 {1,S}
4 O 0 {1,D}
5 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product2 = 
"""
NO3
1 N 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 O 0 {1,S}
4 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1240, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 505,
    reactant1 = 
"""
N2O
1 N 0 {2,D} {3,D}
2 N 0 {1,D}
3 O 0 {1,D}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
N2
1 N 0 {2,T}
2 N 0 {1,T}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (33000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (4729, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (440000000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (19254, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 507,
    reactant1 = 
"""
N2O
1 N 0 {2,D} {3,D}
2 N 0 {1,D}
3 O 0 {1,D}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (92000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (27679, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 508,
    reactant1 = 
"""
N2O
1 N 0 {2,D} {3,D}
2 N 0 {1,D}
3 O 0 {1,D}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
N2
1 N 0 {2,T}
2 N 0 {1,T}
""",
    product2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3700000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (15936, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 509,
    reactant1 = 
"""
N2O
1 N 0 {2,D} {3,D}
2 N 0 {1,D}
3 O 0 {1,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
N2
1 N 0 {2,T}
2 N 0 {1,T}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.013, 'cm^3/(mol*s)'), n=4.7, Ea=(36560, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 510,
    reactant1 = 
"""
N2O
1 N 0 {2,D} {3,D}
2 N 0 {1,D}
3 O 0 {1,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00012, 'cm^3/(mol*s)'),
        n = 4.3,
        Ea = (25080, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 511,
    reactant1 = 
"""
N2O
1 N 0 {2,D} {3,D}
2 N 0 {1,D}
3 O 0 {1,D}
""",
    reactant2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product1 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product2 = 
"""
N2
1 N 0 {2,T}
2 N 0 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(530000, 'cm^3/(mol*s)'), n=2.2, Ea=(46280, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 512,
    reactant1 = 
"""
HCN
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T}
""",
    reactant2 = 
"""
N2
1 N 0 {2,T}
2 N 0 {1,T}
""",
    product1 = 
"""
H
1 H 1
""",
    product2 = 
"""
CN
1 C 1 {2,T}
2 N 0 {1,T}
""",
    product3 = 
"""
N2
1 N 0 {2,T}
2 N 0 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.6e+26, 'cm^3/(mol*s)'),
        n = -2.6,
        Ea = (124890, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 513,
    reactant1 = 
"""
CN
1 C 1 {2,T}
2 N 0 {1,T}
""",
    reactant2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
HCN
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(110000, 'cm^3/(mol*s)'), n=2.6, Ea=(1908, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 514,
    reactant1 = 
"""
HCN
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14000, 'cm^3/(mol*s)'), n=2.6, Ea=(4980, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 515,
    reactant1 = 
"""
HCN
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CN
1 C 1 {2,T}
2 N 0 {1,T}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (42000000000.0, 'cm^3/(mol*s)'),
        n = 0.4,
        Ea = (20665, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 516,
    reactant1 = 
"""
HCN
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
NH
1 N 2S {2,S}
2 H 0  {1,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3500, 'cm^3/(mol*s)'), n=2.6, Ea=(4980, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 517,
    reactant1 = 
"""
HCN
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CN
1 C 1 {2,T}
2 N 0 {1,T}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3900000.0, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (10300, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 518,
    reactant1 = 
"""
HCN
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
HOCN
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,T}
4 N 0 {3,T}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(59000, 'cm^3/(mol*s)'), n=2.4, Ea=(12500, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 519,
    reactant1 = 
"""
HCN
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
HNCO
1 H 0 {2,S}
2 N 0 {1,S} {3,D}
3 C 0 {2,D} {4,D}
4 O 0 {3,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.002, 'cm^3/(mol*s)'), n=4, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 520,
    reactant1 = 
"""
HCN
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.00078, 'cm^3/(mol*s)'), n=4, Ea=(4000, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 521,
    reactant1 = 
"""
HCN
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CN
1 C 1 {2,T}
2 N 0 {1,T}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (75100, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 522,
    reactant1 = 
"""
HNC
1 H 0 {2,S}
2 N 0 {1,S} {3,T}
3 C 0 {2,T}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
HCN
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (78000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 523,
    reactant1 = 
"""
HNC
1 H 0 {2,S}
2 N 0 {1,S} {3,T}
3 C 0 {2,T}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
NH
1 N 2S {2,S}
2 H 0  {1,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4600000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2200, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 524,
    reactant1 = 
"""
HNC
1 H 0 {2,S}
2 N 0 {1,S} {3,T}
3 C 0 {2,T}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
HNCO
1 H 0 {2,S}
2 N 0 {1,S} {3,D}
3 C 0 {2,D} {4,D}
4 O 0 {3,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3700, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 525,
    reactant1 = 
"""
HNC
1 H 0 {2,S}
2 N 0 {1,S} {3,T}
3 C 0 {2,T}
""",
    reactant2 = 
"""
CN
1 C 1 {2,T}
2 N 0 {1,T}
""",
    product1 = 
"""
NCCN
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 C 0 {2,S} {4,T}
4 N 0 {3,T}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 526,
    reactant1 = 
"""
CN
1 C 1 {2,T}
2 N 0 {1,T}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
N
1 N 3
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1900000000000.0, 'cm^3/(mol*s)'),
        n = 0.5,
        Ea = (723, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 527,
    reactant1 = 
"""
CN
1 C 1 {2,T}
2 N 0 {1,T}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1000000000000000.0, 'cm^3/(mol*s)'),
        n = -0.4,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 528,
    reactant1 = 
"""
CN
1 C 1 {2,T}
2 N 0 {1,T}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    product2 = 
"""
O
1 O 2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-417, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 529,
    reactant1 = 
"""
CN
1 C 1 {2,T}
2 N 0 {1,T}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+17, 'cm^3/(mol*s)'), n=-2, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 530,
    reactant1 = 
"""
CN
1 C 1 {2,T}
2 N 0 {1,T}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    product2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5300000000000000.0, 'cm^3/(mol*s)'),
        n = -0.8,
        Ea = (344, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 531,
    reactant1 = 
"""
CN
1 C 1 {2,T}
2 N 0 {1,T}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
N2O
1 N 0 {2,D} {3,D}
2 N 0 {1,D}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (490000000000000.0, 'cm^3/(mol*s)'),
        n = -0.8,
        Ea = (344, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 532,
    reactant1 = 
"""
CN
1 C 1 {2,T}
2 N 0 {1,T}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
N2
1 N 0 {2,T}
2 N 0 {1,T}
""",
    product2 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (370000000000000.0, 'cm^3/(mol*s)'),
        n = -0.8,
        Ea = (344, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 533,
    reactant1 = 
"""
CN
1 C 1 {2,T}
2 N 0 {1,T}
""",
    reactant2 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product1 = 
"""
HCN
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T}
""",
    product2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 534,
    reactant1 = 
"""
CN
1 C 1 {2,T}
2 N 0 {1,T}
""",
    reactant2 = 
"""
HONO
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 N 0 {2,S} {4,D}
4 O 0 {3,D}
""",
    product1 = 
"""
HCN
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T}
""",
    product2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (12000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 535,
    reactant1 = 
"""
CN
1 C 1 {2,T}
2 N 0 {1,T}
""",
    reactant2 = 
"""
N2O
1 N 0 {2,D} {3,D}
2 N 0 {1,D}
3 O 0 {1,D}
""",
    product1 = 
"""
NCN
1 N 1 {2,D}
2 C 0 {1,D} {3,D}
3 N 1 {2,D}
""",
    product2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3800, 'cm^3/(mol*s)'), n=2.6, Ea=(3700, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 536,
    reactant1 = 
"""
CN
1 C 1 {2,T}
2 N 0 {1,T}
""",
    reactant2 = 
"""
HNCO
1 H 0 {2,S}
2 N 0 {1,S} {3,D}
3 C 0 {2,D} {4,D}
4 O 0 {3,D}
""",
    product1 = 
"""
HCN
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T}
""",
    product2 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 537,
    reactant1 = 
"""
CN
1 C 1 {2,T}
2 N 0 {1,T}
""",
    reactant2 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    product1 = 
"""
NCN
1 N 1 {2,D}
2 C 0 {1,D} {3,D}
3 N 1 {2,D}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 538,
    reactant1 = 
"""
HNCO
1 H 0 {2,S}
2 N 0 {1,S} {3,D}
3 C 0 {2,D} {4,D}
4 O 0 {3,D}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(36000, 'cm^3/(mol*s)'), n=2.5, Ea=(2345, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 539,
    reactant1 = 
"""
HNCO
1 H 0 {2,S}
2 N 0 {1,S} {3,D}
3 C 0 {2,D} {4,D}
4 O 0 {3,D}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (90000000.0, 'cm^3/(mol*s)'),
        n = 1.7,
        Ea = (13900, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 540,
    reactant1 = 
"""
HNCO
1 H 0 {2,S}
2 N 0 {1,S} {3,D}
3 C 0 {2,D} {4,D}
4 O 0 {3,D}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2200000.0, 'cm^3/(mol*s)'),
        n = 2.1,
        Ea = (11430, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 541,
    reactant1 = 
"""
HNCO
1 H 0 {2,S}
2 N 0 {1,S} {3,D}
3 C 0 {2,D} {4,D}
4 O 0 {3,D}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
NH
1 N 2S {2,S}
2 H 0  {1,S}
""",
    product2 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (96000000.0, 'cm^3/(mol*s)'),
        n = 1.4,
        Ea = (8520, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 542,
    reactant1 = 
"""
HNCO
1 H 0 {2,S}
2 N 0 {1,S} {3,D}
3 C 0 {2,D} {4,D}
4 O 0 {3,D}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (150000000.0, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (44012, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 543,
    reactant1 = 
"""
HNCO
1 H 0 {2,S}
2 N 0 {1,S} {3,D}
3 C 0 {2,D} {4,D}
4 O 0 {3,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (36000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (3600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 544,
    reactant1 = 
"""
HNCO
1 H 0 {2,S}
2 N 0 {1,S} {3,D}
3 C 0 {2,D} {4,D}
4 O 0 {3,D}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (22000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 545,
    reactant1 = 
"""
HNCO
1 H 0 {2,S}
2 N 0 {1,S} {3,D}
3 C 0 {2,D} {4,D}
4 O 0 {3,D}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (35000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 546,
    reactant1 = 
"""
HNCO
1 H 0 {2,S}
2 N 0 {1,S} {3,D}
3 C 0 {2,D} {4,D}
4 O 0 {3,D}
""",
    reactant2 = 
"""
NH
1 N 2S {2,S}
2 H 0  {1,S}
""",
    product1 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product2 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (23700, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 547,
    reactant1 = 
"""
HOCN
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,T}
4 N 0 {3,T}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
HNCO
1 H 0 {2,S}
2 N 0 {1,S} {3,D}
3 C 0 {2,D} {4,D}
4 O 0 {3,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (310000000.0, 'cm^3/(mol*s)'),
        n = 0.8,
        Ea = (1917, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 548,
    reactant1 = 
"""
HOCN
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,T}
4 N 0 {3,T}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (120000000.0, 'cm^3/(mol*s)'),
        n = 0.6,
        Ea = (2076, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 549,
    reactant1 = 
"""
HOCN
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,T}
4 N 0 {3,T}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (240000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (6617, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 550,
    reactant1 = 
"""
HOCN
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,T}
4 N 0 {3,T}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (170000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (4133, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 551,
    reactant1 = 
"""
HOCN
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,T}
4 N 0 {3,T}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product2 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1200000.0, 'cm^3/(mol*s)'), n=2, Ea=(-248, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 552,
    reactant1 = 
"""
HOCN
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,T}
4 N 0 {3,T}
""",
    reactant2 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    product2 = 
"""
NH3
1 N 0 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(920000, 'cm^3/(mol*s)'), n=1.9, Ea=(3646, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 553,
    reactant1 = 
"""
HCNO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T} {4,S}
4 O 0 {3,S}
""",
    product1 = 
"""
HCN
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T}
""",
    product2 = 
"""
O
1 O 2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.2e+31, 's^-1'), n=-6.1, Ea=(61210, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 554,
    reactant1 = 
"""
HCNO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T} {4,S}
4 O 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
HCN
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (72000000000.0, 'cm^3/(mol*s)'),
        n = 0.8,
        Ea = (8612, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 555,
    reactant1 = 
"""
HCNO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T} {4,S}
4 O 0 {3,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (63000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 556,
    reactant1 = 
"""
HCNO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T} {4,S}
4 O 0 {3,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 557,
    reactant1 = 
"""
HCNO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T} {4,S}
4 O 0 {3,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 558,
    reactant1 = 
"""
HCNO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T} {4,S}
4 O 0 {3,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product3 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 559,
    reactant1 = 
"""
HCNO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T} {4,S}
4 O 0 {3,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    product2 = 
"""
H
1 H 1
""",
    product3 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 560,
    reactant1 = 
"""
HCNO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T} {4,S}
4 O 0 {3,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 561,
    reactant1 = 
"""
HCNO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T} {4,S}
4 O 0 {3,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 562,
    reactant1 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
NH
1 N 2S {2,S}
2 H 0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (72000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 563,
    reactant1 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2000000000000000.0, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 564,
    reactant1 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
HON
1 O 0  {2,S} {3,S}
2 H 0  {1,S}
3 N 2S {1,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5300000000000.0, 'cm^3/(mol*s)'),
        n = -0.1,
        Ea = (5126, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 565,
    reactant1 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
H
1 H 1
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product3 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8300000000000.0, 'cm^3/(mol*s)'),
        n = -0.1,
        Ea = (8042, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 566,
    reactant1 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    product1 = 
"""
HNCO
1 H 0 {2,S}
2 N 0 {1,S} {3,D}
3 C 0 {2,D} {4,D}
4 O 0 {3,D}
""",
    product2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 567,
    reactant1 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product2 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (20000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 568,
    reactant1 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    reactant2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product1 = 
"""
N2O
1 N 0 {2,D} {3,D}
2 N 0 {1,D}
3 O 0 {1,D}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+19, 'cm^3/(mol*s)'), n=-2.2, Ea=(1743, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 569,
    reactant1 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    reactant2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product1 = 
"""
N2
1 N 0 {2,T}
2 N 0 {1,T}
""",
    product2 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+21, 'cm^3/(mol*s)'),
        n = -2.7,
        Ea = (1824, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 570,
    reactant1 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product3 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (250000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-707, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 571,
    reactant1 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    product2 = 
"""
N2O
1 N 0 {2,D} {3,D}
2 N 0 {1,D}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-707, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 572,
    reactant1 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    reactant2 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product1 = 
"""
HNCO
1 H 0 {2,S}
2 N 0 {1,S} {3,D}
3 C 0 {2,D} {4,D}
4 O 0 {3,D}
""",
    product2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 573,
    reactant1 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    reactant2 = 
"""
HONO
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 N 0 {2,S} {4,D}
4 O 0 {3,D}
""",
    product1 = 
"""
HNCO
1 H 0 {2,S}
2 N 0 {1,S} {3,D}
3 C 0 {2,D} {4,D}
4 O 0 {3,D}
""",
    product2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3600000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 574,
    reactant1 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    reactant2 = 
"""
N
1 N 3
""",
    product1 = 
"""
N2
1 N 0 {2,T}
2 N 0 {1,T}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 575,
    reactant1 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    reactant2 = 
"""
NH3
1 N 0 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
HNCO
1 H 0 {2,S}
2 N 0 {1,S} {3,D}
3 C 0 {2,D} {4,D}
4 O 0 {3,D}
""",
    product2 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(28000, 'cm^3/(mol*s)'), n=2.5, Ea=(980, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 576,
    reactant1 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    reactant2 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product3 = 
"""
N2
1 N 0 {2,T}
2 N 0 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 577,
    reactant1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product2 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (90000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (33800, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 578,
    reactant1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    reactant2 = 
"""
N2O
1 N 0 {2,D} {3,D}
2 N 0 {1,D}
3 O 0 {1,D}
""",
    product1 = 
"""
N2
1 N 0 {2,T}
2 N 0 {1,T}
""",
    product2 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (270000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (20237, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 579,
    reactant1 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    reactant2 = 
"""
N
1 N 3
""",
    product1 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (20000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 580,
    reactant1 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    reactant2 = 
"""
CN
1 C 1 {2,T}
2 N 0 {1,T}
""",
    product1 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3700000.0, 'cm^3/(mol*s)'),
        n = 2.2,
        Ea = (26900, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 581,
    reactant1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
HONO
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 N 0 {2,S} {4,D}
4 O 0 {3,D}
""",
    product2 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e-07, 'cm^3/(mol*s)'), n=5.6, Ea=(9220, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 582,
    reactant1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
HNO2
1 H 0 {2,S}
2 N 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {2,S}
""",
    product2 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.11, 'cm^3/(mol*s)'), n=4.2, Ea=(19850, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 583,
    reactant1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    reactant2 = 
"""
CN
1 C 1 {2,T}
2 N 0 {1,T}
""",
    product1 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
HCN
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1700, 'cm^3/(mol*s)'), n=2.7, Ea=(-1427, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 584,
    reactant1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    reactant2 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    product1 = 
"""
HNCO
1 H 0 {2,S}
2 N 0 {1,S} {3,D}
3 C 0 {2,D} {4,D}
4 O 0 {3,D}
""",
    product2 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 585,
    reactant1 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    reactant2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product1 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6900000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 586,
    reactant1 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product2 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    product3 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (23000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 587,
    reactant1 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
HONO
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 N 0 {2,S} {4,D}
4 O 0 {3,D}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 588,
    reactant1 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product3 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 589,
    reactant1 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    reactant2 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product1 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product2 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.58, 'cm^3/(mol*s)'), n=3.8, Ea=(115, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 590,
    reactant1 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    reactant2 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    product1 = 
"""
HNCO
1 H 0 {2,S}
2 N 0 {1,S} {3,D}
3 C 0 {2,D} {4,D}
4 O 0 {3,D}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (36000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 591,
    reactant1 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
NH3
1 N 0 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1500, 'cm^3/(mol*s)'), n=3, Ea=(9940, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 592,
    reactant1 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
CN
1 C 1 {2,T}
2 N 0 {1,T}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
HCN
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(860000, 'cm^3/(mol*s)'), n=2.3, Ea=(-32, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 593,
    reactant1 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
HNCO
1 H 0 {2,S}
2 N 0 {1,S} {3,D}
3 C 0 {2,D} {4,D}
4 O 0 {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9800000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8120, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 594,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
H2NO
1 N 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {1,S}
""",
    product2 = 
"""
NH2
1 N 1 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 595,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
H2NO
1 N 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product1 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product2 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1600000.0, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (2961, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 596,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product1 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (230000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8400, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 597,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product1 = 
"""
HCN
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.15, 'cm^3/(mol*s)'), n=3.5, Ea=(3950, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 598,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product1 = 
"""
H2CN
1 H 0 {3,S}
2 H 0 {3,S}
3 C 0 {1,S} {2,S} {4,D}
4 N 1 {3,D}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.15, 'cm^3/(mol*s)'), n=3.5, Ea=(3950, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 599,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {1,S}
""",
    product2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (11000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 600,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
HONO
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 N 0 {2,S} {4,D}
4 O 0 {3,D}
""",
    product1 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(810000, 'cm^3/(mol*s)'), n=1.9, Ea=(5504, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 601,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
HNO2
1 H 0 {2,S}
2 N 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {2,S}
""",
    product1 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(810000, 'cm^3/(mol*s)'), n=1.9, Ea=(4838, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 602,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
CN
1 C 1 {2,T}
2 N 0 {1,T}
""",
    product1 = 
"""
CH2CN
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 C 0 {1,S} {5,T}
5 N 0 {4,T}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 603,
    reactant1 = 
"""
CH3CN
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,T}
6 N 0 {5,T}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
HCN
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T}
""",
    product2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40000000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (2000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 604,
    reactant1 = 
"""
CH3CN
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,T}
6 N 0 {5,T}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH2CN
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 C 0 {1,S} {5,T}
5 N 0 {4,T}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (1000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 605,
    reactant1 = 
"""
CH3CN
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,T}
6 N 0 {5,T}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    product2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(15000, 'cm^3/(mol*s)'), n=2.6, Ea=(4980, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 606,
    reactant1 = 
"""
CH3CN
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,T}
6 N 0 {5,T}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2CN
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 C 0 {1,S} {5,T}
5 N 0 {4,T}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (2000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 607,
    reactant1 = 
"""
CH2CN
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 C 0 {1,S} {5,T}
5 N 0 {4,T}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
CN
1 C 1 {2,T}
2 N 0 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 608,
    reactant1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
CN
1 C 1 {2,T}
2 N 0 {1,T}
""",
    product1 = 
"""
CH2CN
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 C 0 {1,S} {5,T}
5 N 0 {4,T}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 609,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
HOCN
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,T}
4 N 0 {3,T}
""",
    product1 = 
"""
CH3CN
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,T}
6 N 0 {5,T}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 610,
    reactant1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
N
1 N 3
""",
    product1 = 
"""
HCN
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 611,
    reactant1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product1 = 
"""
HCNO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T} {4,S}
4 O 0 {3,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-378, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 612,
    reactant1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product1 = 
"""
HCN
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (390000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-378, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 613,
    reactant1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (59000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 614,
    reactant1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
N2
1 N 0 {2,T}
2 N 0 {1,T}
""",
    product1 = 
"""
HCN
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T}
""",
    product2 = 
"""
NH
1 N 2S {2,S}
2 H 0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (74000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 615,
    reactant1 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product1 = 
"""
HCN
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 616,
    reactant1 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 617,
    reactant1 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
N2O
1 N 0 {2,D} {3,D}
2 N 0 {1,D}
3 O 0 {1,D}
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
N2
1 N 0 {2,T}
2 N 0 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (38000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 618,
    reactant1 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
HCN
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T}
""",
    product1 = 
"""
CH2CN
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 C 0 {1,S} {5,T}
5 N 0 {4,T}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (180000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 619,
    reactant1 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    reactant2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
NH
1 N 2S {2,S}
2 H 0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 620,
    reactant1 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    reactant2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product1 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 621,
    reactant1 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    reactant2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product1 = 
"""
HCN
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T}
""",
    product2 = 
"""
O
1 O 2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (79000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 622,
    reactant1 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    reactant2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product1 = 
"""
CN
1 C 1 {2,T}
2 N 0 {1,T}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 623,
    reactant1 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    reactant2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product1 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
N
1 N 3
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6800000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 624,
    reactant1 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 625,
    reactant1 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    reactant2 = 
"""
N2O
1 N 0 {2,D} {3,D}
2 N 0 {1,D}
3 O 0 {1,D}
""",
    product1 = 
"""
HCN
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T}
""",
    product2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (19000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-511, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 626,
    reactant1 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    reactant2 = 
"""
N2
1 N 0 {2,T}
2 N 0 {1,T}
""",
    product1 = 
"""
NCN
1 N 1 {2,D}
2 C 0 {1,D} {3,D}
3 N 1 {2,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (37000000.0, 'cm^3/(mol*s)'),
        n = 1.4,
        Ea = (20723, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 627,
    reactant1 = 
"""
NCN
1 N 1 {2,D}
2 C 0 {1,D} {3,D}
3 N 1 {2,D}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
HCN
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T}
""",
    product2 = 
"""
N
1 N 3
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 628,
    reactant1 = 
"""
NCN
1 N 1 {2,D}
2 C 0 {1,D} {3,D}
3 N 1 {2,D}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CN
1 C 1 {2,T}
2 N 0 {1,T}
""",
    product2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 629,
    reactant1 = 
"""
NCN
1 N 1 {2,D}
2 C 0 {1,D} {3,D}
3 N 1 {2,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
HCN
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T}
""",
    product2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 630,
    reactant1 = 
"""
NCN
1 N 1 {2,D}
2 C 0 {1,D} {3,D}
3 N 1 {2,D}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product2 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4400000000.0, 'cm^3/(mol*s)'),
        n = 0.5,
        Ea = (24580, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 631,
    reactant1 = 
"""
C(T)
1 C 4T
""",
    reactant2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product1 = 
"""
CN
1 C 1 {2,T}
2 N 0 {1,T}
""",
    product2 = 
"""
O
1 O 2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 632,
    reactant1 = 
"""
C(T)
1 C 4T
""",
    reactant2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
N
1 N 3
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 633,
    reactant1 = 
"""
C(T)
1 C 4T
""",
    reactant2 = 
"""
N2O
1 N 0 {2,D} {3,D}
2 N 0 {1,D}
3 O 0 {1,D}
""",
    product1 = 
"""
CN
1 C 1 {2,T}
2 N 0 {1,T}
""",
    product2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4800000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 634,
    reactant1 = 
"""
CN
1 C 1 {2,T}
2 N 0 {1,T}
""",
    reactant2 = 
"""
N
1 N 3
""",
    product1 = 
"""
C(T)
1 C 4T
""",
    product2 = 
"""
N2
1 N 0 {2,T}
2 N 0 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (590000000000000.0, 'cm^3/(mol*s)'),
        n = -0.4,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 635,
    reactant1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 0 {1,S} {6,S}
6 H 0 {5,S}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
HONO
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 N 0 {2,S} {4,D}
4 O 0 {3,D}
""",
    product2 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(150, 'cm^3/(mol*s)'), n=3.3, Ea=(20035, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 636,
    reactant1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 0 {1,S} {6,S}
6 H 0 {5,S}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
HNO2
1 H 0 {2,S}
2 N 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {2,S}
""",
    product2 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2400, 'cm^3/(mol*s)'), n=2.9, Ea=(27470, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 637,
    reactant1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {1,S}
""",
    reactant2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product1 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (7500000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (2017, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(2.5e+18, 'cm^3/(mol*s)'), n=-2.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 639,
    reactant1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {1,S}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
HONO
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 N 0 {2,S} {4,D}
4 O 0 {3,D}
""",
    product2 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2285, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 640,
    reactant1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {1,S}
""",
    reactant2 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product1 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product2 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 0 {1,S} {6,S}
6 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (32000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 641,
    reactant1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 642,
    reactant1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
HONO
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 N 0 {2,S} {4,D}
4 O 0 {3,D}
""",
    product2 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 643,
    reactant1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product1 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product2 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 0 {1,S} {6,S}
6 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 644,
    reactant1 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    reactant2 = 
"""
CN
1 C 1 {2,T}
2 N 0 {1,T}
""",
    product1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
HCN
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (120000000.0, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (-994, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 645,
    reactant1 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    reactant2 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    product1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
HNCO
1 H 0 {2,S}
2 N 0 {1,S} {3,D}
3 C 0 {2,D} {4,D}
4 O 0 {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e-09, 'cm^3/(mol*s)'),
        n = 6.9,
        Ea = (-2910, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 646,
    reactant1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
HONO
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 N 0 {2,S} {4,D}
4 O 0 {3,D}
""",
    product1 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    product2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(810000, 'cm^3/(mol*s)'), n=1.9, Ea=(5504, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 647,
    reactant1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
HNO2
1 H 0 {2,S}
2 N 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {2,S}
""",
    product1 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    product2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(810000, 'cm^3/(mol*s)'), n=1.9, Ea=(4838, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 648,
    reactant1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product2 = 
"""
CH3CH2O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 O 1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40000000000000.0, 'cm^3/(mol*s)'),
        n = -0.2,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 649,
    reactant1 = 
"""
C2H3
1 H 0 {2,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {4,S} {5,S}
4 H 0 {3,S}
5 H 0 {3,S}
""",
    reactant2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product1 = 
"""
HCN
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T}
""",
    product2 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+21, 'cm^3/(mol*s)'), n=-3.4, Ea=(1025, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 650,
    reactant1 = 
"""
C2H3
1 H 0 {2,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {4,S} {5,S}
4 H 0 {3,S}
5 H 0 {3,S}
""",
    reactant2 = 
"""
HONO
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 N 0 {2,S} {4,D}
4 O 0 {3,D}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(810000, 'cm^3/(mol*s)'), n=1.9, Ea=(5504, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 651,
    reactant1 = 
"""
C2H3
1 H 0 {2,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {4,S} {5,S}
4 H 0 {3,S}
5 H 0 {3,S}
""",
    reactant2 = 
"""
HNO2
1 H 0 {2,S}
2 N 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {2,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(810000, 'cm^3/(mol*s)'), n=1.9, Ea=(4838, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 652,
    reactant1 = 
"""
C2H3
1 H 0 {2,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {4,S} {5,S}
4 H 0 {3,S}
5 H 0 {3,S}
""",
    reactant2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    product2 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 653,
    reactant1 = 
"""
C2H3
1 H 0 {2,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {4,S} {5,S}
4 H 0 {3,S}
5 H 0 {3,S}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product2 = 
"""
CH2CHO
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {2,S}
6 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (770000000000000.0, 'cm^3/(mol*s)'),
        n = -0.6,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 654,
    reactant1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    product1 = 
"""
HCCO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {4,S}
4 O 1 {3,S}
""",
    product2 = 
"""
HCN
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1400000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1815, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 655,
    reactant1 = 
"""
C2H
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 1 {2,T}
""",
    reactant2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product1 = 
"""
HCN
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (60000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (570, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 656,
    reactant1 = 
"""
C2
1 C 1 {2,T}
2 C 1 {1,T}
""",
    reactant2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product1 = 
"""
C2O
1 C 2S {2,D}
2 C 0  {1,D} {3,D}
3 O 0  {2,D}
""",
    product2 = 
"""
N
1 N 3
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (23000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8640, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 657,
    reactant1 = 
"""
C2
1 C 1 {2,T}
2 C 1 {1,T}
""",
    reactant2 = 
"""
N2
1 N 0 {2,T}
2 N 0 {1,T}
""",
    product1 = 
"""
CN
1 C 1 {2,T}
2 N 0 {1,T}
""",
    product2 = 
"""
CN
1 C 1 {2,T}
2 N 0 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (15000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (41730, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 658,
    reactant1 = 
"""
CH3CH2O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 O 1 {2,S}
""",
    reactant2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product1 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
CH3CHO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 O 0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6600000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 659,
    reactant1 = 
"""
CH3CH2O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 O 1 {2,S}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
HONO
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 N 0 {2,S} {4,D}
4 O 0 {3,D}
""",
    product2 = 
"""
CH3CHO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 O 0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1700000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 660,
    reactant1 = 
"""
CH2CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S}
3 O 0 {1,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product3 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (7000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 661,
    reactant1 = 
"""
CH2CHO
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
CH2CO
1 H 0 {3,S}
2 H 0 {3,S}
3 C 0 {1,S} {2,S} {4,D}
4 C 0 {3,D} {5,D}
5 O 0 {4,D}
""",
    product2 = 
"""
HONO
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 N 0 {2,S} {4,D}
4 O 0 {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2000000000000000.0, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (1430, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 662,
    reactant1 = 
"""
CH3CO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 O 0 {2,D}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    product3 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (15000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 663,
    reactant1 = 
"""
HCCO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {4,S}
4 O 1 {3,S}
""",
    reactant2 = 
"""
N
1 N 3
""",
    product1 = 
"""
HCN
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 664,
    reactant1 = 
"""
HCCO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {4,S}
4 O 1 {3,S}
""",
    reactant2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product1 = 
"""
HCNO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T} {4,S}
4 O 0 {3,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5900000000000.0, 'cm^3/(mol*s)'),
        n = 0.1,
        Ea = (-457, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 665,
    reactant1 = 
"""
HCCO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {4,S}
4 O 1 {3,S}
""",
    reactant2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product1 = 
"""
HCN
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T}
""",
    product2 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (370000000000000.0, 'cm^3/(mol*s)'),
        n = -0.8,
        Ea = (-90, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 666,
    reactant1 = 
"""
HCCO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {4,S}
4 O 1 {3,S}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
HCNO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T} {4,S}
4 O 0 {3,S}
""",
    product2 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (16000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 667,
    reactant1 = 
"""
C2O
1 C 2S {2,D}
2 C 0  {1,D} {3,D}
3 O 0  {2,D}
""",
    reactant2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (670, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 668,
    reactant1 = 
"""
C2O
1 C 2S {2,D}
2 C 0  {1,D} {3,D}
3 O 0  {2,D}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    product2 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (51000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (125, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 669,
    reactant1 = 
"""
CH3CH2O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 O 1 {2,S}
""",
    reactant2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product1 = 
"""
CH3CH2ONO
1  C 0 {2,S} {3,S} {4,S} {5,S}
2  H 0 {1,S}
3  H 0 {1,S}
4  H 0 {1,S}
5  C 0 {1,S} {6,S} {7,S} {8,S}
6  H 0 {5,S}
7  H 0 {5,S}
8  O 0 {5,S} {9,S}
9  N 0 {8,S} {10,D}
10 O 0 {9,D}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (12000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (-143, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(A=(9.43e+19, 'cm^6/(mol^2*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.6,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 670,
    reactant1 = 
"""
CH3CH2O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 O 1 {2,S}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
CH3CH2ONO2
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {7,S} {8,S} {9,S}
3  N 0 {4,S} {10,S} {11,D}
4  O 0 {1,S} {3,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 O 0 {3,S}
11 O 0 {3,D}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (5100000000000000.0, 'cm^3/(mol*s)'),
            n = -1,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(A=(5.88e+30, 'cm^6/(mol^2*s)'), n=-4, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.6,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 671,
    reactant1 = 
"""
CH3NO2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 N 0 {1,S} {6,S} {7,D}
6 O 0 {5,S}
7 O 0 {5,D}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.8e+16, 's^-1'), n=0, Ea=(58500, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.259e+17, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (42000, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.183,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        efficiencies = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 672,
    reactant1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {1,S}
""",
    reactant2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product1 = 
"""
CH3ONO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 0 {1,S} {6,S}
6 N 0 {5,S} {7,D}
7 O 0 {6,D}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (600000000000000.0, 'cm^3/(mol*s)'),
            n = -0.6,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (8.14e+25, 'cm^6/(mol^2*s)'),
            n = -2.8,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1,
        T3 = (1e-30, 'K'),
        T1 = (900, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 673,
    reactant1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {1,S}
""",
    reactant2 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    product1 = 
"""
CH3ONO2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 0 {1,S} {6,S}
6 N 0 {5,S} {7,S} {8,D}
7 O 0 {6,S}
8 O 0 {6,D}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (2200000000000000.0, 'cm^3/(mol*s)'),
            n = -0.9,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.911e+23, 'cm^6/(mol^2*s)'),
            n = -1.74,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.6,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 674,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    product1 = 
"""
CH3NO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 N 0 {1,S} {6,D}
6 O 0 {5,D}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (9000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (192, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.5e+16, 'cm^6/(mol^2*s)'),
            n = 0,
            Ea = (-2841, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 5,
        T3 = (1e-30, 'K'),
        T1 = (120, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 675,
    reactant1 = 
"""
H
1 H 1
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(7e+17, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'[H][H]': 0.0, 'O': 0.0, 'N#N': 0.0},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 676,
    reactant1 = 
"""
H
1 H 1
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(6.2e+16, 'cm^6/(mol^2*s)'), n=-0.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'O': 5.0},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 677,
    reactant1 = 
"""
H
1 H 1
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1500000000000.0, 'cm^3/(mol*s)'),
            n = 0.6,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (3.5e+16, 'cm^6/(mol^2*s)'),
            n = -0.41,
            Ea = (-1116, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        efficiencies = {'[H][H]': 2.0, '[O][O]': 0.78, 'O': 11.0, 'N#N': 0.0, '[Ar]': 0.0},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 678,
    reactant1 = 
"""
O
1 O 2T
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (19000000000000.0, 'cm^6/(mol^2*s)'),
            n = 0,
            Ea = (-1788, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'[O][O]': 1.5, 'O': 10.0, 'N#N': 1.5},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 679,
    reactant1 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4.5e+22, 'cm^6/(mol^2*s)'), n=-2, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'[H][H]': 0.73, 'O': 12.0, '[Ar]': 0.38},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 680,
    reactant1 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    product1 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(400000000000.0, 's^-1'), n=0, Ea=(37137, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.291e+16, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (43638, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {'[H][H]': 2.5, 'O': 12.0, '[Ar]': 0.64},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 681,
    reactant1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (18000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (2384, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.35e+24, 'cm^6/(mol^2*s)'),
            n = -2.79,
            Ea = (4191, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {'[H][H]': 2.5, '[C]=O': 1.9, 'C(=O)=O': 3.8, 'O': 12.0},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 682,
    reactant1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product1 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(
            A = (8000000000000000.0, 's^-1'),
            n = 0,
            Ea = (87726, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (3734000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (73479, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 683,
    reactant1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(37000000000000.0, 's^-1'), n=0, Ea=(71969, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5661000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (65849, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 684,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (210000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (6.467e+23, 'cm^6/(mol^2*s)'),
            n = -1.8,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.6376,
        T3 = (1e-30, 'K'),
        T1 = (3230, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {'CC': 4.8, 'C': 1.9},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 685,
    reactant1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.8e+16, 'cm^3/(mol*s)'), n=-0.8, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (4.8e+27, 'cm^6/(mol^2*s)'),
            n = -3.14,
            Ea = (1230, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.68,
        T3 = (78, 'K'),
        T1 = (1995, 'K'),
        T2 = (5590, 'K'),
        efficiencies = {'O': 6.0, 'N#N': 1.0, '[Ar]': 0.7},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 686,
    reactant1 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (10000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'[H]': 0.0, '[O][O]': 0.0, 'O': 0.0, 'N#N': 0.0, '[Ar]': 0.0},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 687,
    reactant1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 0 {1,S} {6,S}
6 H 0 {5,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.1e+18, 's^-1'), n=-0.6, Ea=(92540, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.6e+49, 'cm^3/(mol*s)'),
            n = -8.8,
            Ea = (101500, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7656,
        T3 = (1910, 'K'),
        T1 = (59.51, 'K'),
        T2 = (9374, 'K'),
        efficiencies = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 688,
    reactant1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (280000000000000.0, 's^-1'),
            n = -0.7,
            Ea = (32820, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (6.01e+33, 'cm^3/(mol*s)'),
            n = -5.39,
            Ea = (36200, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.96,
        T3 = (67.6, 'K'),
        T1 = (1855, 'K'),
        T2 = (7543, 'K'),
        efficiencies = {'[H][H]': 2.0, '[C]=O': 2.0, 'C(=O)=O': 3.0, 'O': 5.0},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 689,
    reactant1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 0 {1,S} {6,S}
6 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (4300000000000000.0, 'cm^3/(mol*s)'),
            n = -0.8,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (3.844e+37, 'cm^6/(mol^2*s)'),
            n = -6.21,
            Ea = (1333, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.25,
        T3 = (210, 'K'),
        T1 = (1434, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 690,
    reactant1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(68000000000000.0, 's^-1'), n=0, Ea=(26154, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.867e+25, 'cm^3/(mol*s)'),
            n = -3,
            Ea = (24291, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5,
        T3 = (1000, 'K'),
        T1 = (2000, 'K'),
        efficiencies = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 691,
    reactant1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 1 {1,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 O 0 {1,S} {6,S}
6 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (2400000000000.0, 'cm^3/(mol*s)'),
            n = 0.5,
            Ea = (50, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (4.66e+41, 'cm^6/(mol^2*s)'),
            n = -7.44,
            Ea = (14080, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7,
        T3 = (100, 'K'),
        T1 = (90000, 'K'),
        T2 = (10000, 'K'),
        efficiencies = {'C': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, 'C(=O)=O': 2.0, 'N#N': 1.0, '[C]=O': 1.5},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 692,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (36000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.269e+41, 'cm^6/(mol^2*s)'),
            n = -7,
            Ea = (2762, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.62,
        T3 = (73, 'K'),
        T1 = (1180, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 693,
    reactant1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1400000000.0, 'cm^3/(mol*s)'),
            n = 1.5,
            Ea = (1355, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2e+39, 'cm^6/(mol^2*s)'),
            n = -6.642,
            Ea = (5769, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -0.569,
        T3 = (299, 'K'),
        T1 = (9147, 'K'),
        T2 = (152.4, 'K'),
        efficiencies = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 694,
    reactant1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.2e+17, 'cm^3/(mol*s)'), n=-1, Ea=(1580, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.99e+41, 'cm^6/(mol^2*s)'),
            n = -7.08,
            Ea = (6685, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.8422,
        T3 = (125, 'K'),
        T1 = (2219, 'K'),
        T2 = (6882, 'K'),
        efficiencies = {'C': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, 'C(=O)=O': 2.0, 'N#N': 1.0, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 695,
    reactant1 = 
"""
C2H3
1 H 0 {2,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {4,S} {5,S}
4 H 0 {3,S}
5 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (39000000000000.0, 'cm^3/(mol*s)'),
            n = 0.2,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(A=(2.1e+24, 'cm^6/(mol^2*s)'), n=-1.3, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.5,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 696,
    reactant1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product1 = 
"""
H2CC
1 C 0  {2,S} {3,S} {4,D}
2 H 0  {1,S}
3 H 0  {1,S}
4 C 2S {1,D}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (8000000000000.0, 's^-1'),
            n = 0.4,
            Ea = (88800, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (7e+50, 'cm^3/(mol*s)'),
            n = -9.31,
            Ea = (99900, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.735,
        T3 = (180, 'K'),
        T1 = (1035, 'K'),
        T2 = (5417, 'K'),
        efficiencies = {'O': 6.0, '[Ar]': 0.7},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 697,
    reactant1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C2H3
1 H 0 {2,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {4,S} {5,S}
4 H 0 {3,S}
5 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (17000000000.0, 'cm^3/(mol*s)'),
            n = 1.3,
            Ea = (2709, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (6.3e+31, 'cm^6/(mol^2*s)'),
            n = -4.664,
            Ea = (3780, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7878,
        T3 = (-10212, 'K'),
        T1 = (1e+30, 'K'),
        efficiencies = {'[H][H]': 2.0, '[C]=O': 2.0, 'C(=O)=O': 3.0, 'O': 5.0},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 698,
    reactant1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    product1 = 
"""
C2H
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 1 {2,T}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (9.1e+30, 'cm^3/(mol*s)'),
            n = -3.7,
            Ea = (127138, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'[H][H]': 2.0, '[C]=O': 2.0, 'C(=O)=O': 3.0, 'O': 5.0},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 699,
    reactant1 = 
"""
CH3CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,S} {7,S} {8,S}
6 H 0 {5,S}
7 H 0 {5,S}
8 O 0 {5,S} {9,S}
9 H 0 {8,S}
""",
    product1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.9e+23, 's^-1'), n=-1.7, Ea=(91163, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.88e+85, 'cm^3/(mol*s)'),
            n = -18.9,
            Ea = (109910, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5,
        T3 = (200, 'K'),
        T1 = (890, 'K'),
        T2 = (4600, 'K'),
        efficiencies = {'[H][H]': 2.0, '[C]=O': 2.0, 'C(=O)=O': 3.0, 'O': 5.0},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 700,
    reactant1 = 
"""
CH3CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,S} {7,S} {8,S}
6 H 0 {5,S}
7 H 0 {5,S}
8 O 0 {5,S} {9,S}
9 H 0 {8,S}
""",
    product1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.3e+23, 's^-1'), n=-1.5, Ea=(96005, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.25e+85, 'cm^3/(mol*s)'),
            n = -18.81,
            Ea = (114930, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5,
        T3 = (300, 'K'),
        T1 = (900, 'K'),
        T2 = (5000, 'K'),
        efficiencies = {'[H][H]': 2.0, '[C]=O': 2.0, 'C(=O)=O': 3.0, 'O': 5.0},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 701,
    reactant1 = 
"""
CH3CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,S} {7,S} {8,S}
6 H 0 {5,S}
7 H 0 {5,S}
8 O 0 {5,S} {9,S}
9 H 0 {8,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (28000000000000.0, 's^-1'),
            n = 0.1,
            Ea = (66136, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.57e+83, 'cm^3/(mol*s)'),
            n = -18.85,
            Ea = (86452, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7,
        T3 = (350, 'K'),
        T1 = (800, 'K'),
        T2 = (3800, 'K'),
        efficiencies = {'O': 5.0},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 702,
    reactant1 = 
"""
CH3CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,S} {7,S} {8,S}
6 H 0 {5,S}
7 H 0 {5,S}
8 O 0 {5,S} {9,S}
9 H 0 {8,S}
""",
    product1 = 
"""
CH3CHO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 O 0 {2,D}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(720000000000.0, 's^-1'), n=0.1, Ea=(91007, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (4.46e+87, 'cm^3/(mol*s)'),
            n = -19.42,
            Ea = (115590, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.9,
        T3 = (900, 'K'),
        T1 = (1100, 'K'),
        T2 = (3500, 'K'),
        efficiencies = {'O': 5.0},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 703,
    reactant1 = 
"""
CH2CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S}
3 O 0 {1,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH3CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 C 0 {1,S} {6,S} {7,S} {8,S}
6 H 0 {5,S}
7 H 0 {5,S}
8 O 0 {5,S} {9,S}
9 H 0 {8,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.2e+17, 'cm^3/(mol*s)'), n=-1, Ea=(1580, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.99e+41, 'cm^6/(mol^2*s)'),
            n = -7.08,
            Ea = (6685, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.8422,
        T3 = (125, 'K'),
        T1 = (2219, 'K'),
        T2 = (6882, 'K'),
        efficiencies = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 704,
    reactant1 = 
"""
CH3CH2O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 O 1 {2,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CH2O
1 C 0 {2,S} {3,S} {4,D}
2 H 0 {1,S}
3 H 0 {1,S}
4 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(11000000000000.0, 's^-1'), n=0, Ea=(16790, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(2e+16, 'cm^3/(mol*s)'), n=0, Ea=(13970, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.78,
        T3 = (1e-30, 'K'),
        T1 = (1235, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 705,
    reactant1 = 
"""
CH3CHO
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,D}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 O 0 {2,D}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
HCO
1 C 1 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4.3e+22, 's^-1'), n=-1.9, Ea=(85480, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.22e+76, 'cm^3/(mol*s)'),
            n = -11.81,
            Ea = (95040, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.23,
        T3 = (80, 'K'),
        T1 = (7000, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 706,
    reactant1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product1 = 
"""
CH2CO
1 H 0 {3,S}
2 H 0 {3,S}
3 C 0 {1,S} {2,S} {4,D}
4 C 0 {3,D} {5,D}
5 O 0 {4,D}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (810000000000.0, 'cm^3/(mol*s)'),
            n = 0.5,
            Ea = (4510, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.69e+33, 'cm^6/(mol^2*s)'),
            n = -5.11,
            Ea = (7095, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5907,
        T3 = (275, 'K'),
        T1 = (1226, 'K'),
        T2 = (5185, 'K'),
        efficiencies = {'O': 6.0, 'N#N': 1.0, '[Ar]': 0.7},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 707,
    reactant1 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    reactant2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product1 = 
"""
HCCO
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {4,S}
4 O 1 {3,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (50000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.7e+28, 'cm^6/(mol^2*s)'),
            n = -3.74,
            Ea = (1936, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5757,
        T3 = (237, 'K'),
        T1 = (1652, 'K'),
        T2 = (5069, 'K'),
        efficiencies = {'C': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, 'C(=O)=O': 2.0, 'N#N': 1.0, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 708,
    reactant1 = 
"""
HNOH
1 N 1 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    product1 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(2e+24, 'cm^3/(mol*s)'), n=-2.8, Ea=(58934, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'O': 10.0},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 709,
    reactant1 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
HNO
1 N 0 {2,S} {3,D}
2 H 0 {1,S}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1500000000000000.0, 'cm^3/(mol*s)'),
            n = -0.4,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (240000000000000.0, 'cm^6/(mol^2*s)'),
            n = 0.206,
            Ea = (-1550, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.82,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {'N#N': 1.6},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 710,
    reactant1 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1300000000000000.0, 'cm^3/(mol*s)'),
            n = -0.8,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (4.72e+24, 'cm^6/(mol^2*s)'),
            n = -2.87,
            Ea = (1550, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.88,
        T3 = (1000, 'K'),
        T1 = (10000, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {'[Ar]': 0.0},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 711,
    reactant1 = 
"""
NO
1 N 1 {2,D}
2 O 0 {1,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
HONO
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 N 0 {2,S} {4,D}
4 O 0 {3,D}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (110000000000000.0, 'cm^3/(mol*s)'),
            n = -0.3,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (3.392e+23, 'cm^6/(mol^2*s)'),
            n = -2.5,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.75,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 712,
    reactant1 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
NO3
1 N 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 O 0 {1,S}
4 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (3500000000000.0, 'cm^3/(mol*s)'),
            n = 0.2,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(A=(2.5e+20, 'cm^6/(mol^2*s)'), n=-1.5, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.71,
        T3 = (1e-30, 'K'),
        T1 = (1700, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 713,
    reactant1 = 
"""
NO2
1 N 0 {2,D} {3,S}
2 O 0 {1,D}
3 O 1 {1,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
HONO2
1 N 0 {2,S} {3,S} {4,D}
2 O 0 {1,S} {5,S}
3 O 0 {1,S}
4 O 0 {1,D}
5 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (30000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(A=(2.938e+25, 'cm^6/(mol^2*s)'), n=-3, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.4,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 714,
    reactant1 = 
"""
HNO2
1 H 0 {2,S}
2 N 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {2,S}
""",
    product1 = 
"""
HONO
1 H 0 {2,S}
2 O 0 {1,S} {3,S}
3 N 0 {2,S} {4,D}
4 O 0 {3,D}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (250000000000000.0, 's^-1'),
            n = 0,
            Ea = (32300, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(A=(3.1e+18, 'cm^3/(mol*s)'), n=0, Ea=(31500, 'cal/mol'), T0=(1, 'K')),
        alpha = 1.149,
        T3 = (1e-30, 'K'),
        T1 = (3125, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 715,
    reactant1 = 
"""
N2O
1 N 0 {2,D} {3,D}
2 N 0 {1,D}
3 O 0 {1,D}
""",
    product1 = 
"""
N2
1 N 0 {2,T}
2 N 0 {1,T}
""",
    product2 = 
"""
O
1 O 2T
""",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(1300000000000.0, 's^-1'), n=0, Ea=(62570, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (400000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (56600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'O': 12.0, '[O][O]': 1.4, 'C(=O)=O': 3.0, 'N#N': 1.7},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 716,
    reactant1 = 
"""
HCN
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T}
""",
    product1 = 
"""
H
1 H 1
""",
    product2 = 
"""
CN
1 C 1 {2,T}
2 N 0 {1,T}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (3.4e+35, 'cm^3/(mol*s)'),
            n = -5.1,
            Ea = (133000, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'[O][O]': 1.5, 'O': 10.0, 'N#N': 0.0},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 717,
    reactant1 = 
"""
HCN
1 H 0 {2,S}
2 C 0 {1,S} {3,T}
3 N 0 {2,T}
""",
    product1 = 
"""
HNC
1 H 0 {2,S}
2 N 0 {1,S} {3,T}
3 C 0 {2,T}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.6e+26, 'cm^3/(mol*s)'),
            n = -3.2,
            Ea = (54600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C(=O)=O': 2.0, 'O': 7.0, '[Ar]': 0.7},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 718,
    reactant1 = 
"""
HNCO
1 H 0 {2,S}
2 N 0 {1,S} {3,D}
3 C 0 {2,D} {4,D}
4 O 0 {3,D}
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
NH
1 N 2S {2,S}
2 H 0  {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.1e+16, 'cm^3/(mol*s)'), n=0, Ea=(86000, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'N#N': 1.5},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 719,
    reactant1 = 
"""
NCO
1 N 0 {2,T}
2 C 0 {1,T} {3,S}
3 O 1 {2,S}
""",
    product1 = 
"""
N
1 N 3
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (220000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (54050, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'N#N': 1.5},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Mar 11 14:03:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> imported this entry from the old RMG database."""),
    ],
)

