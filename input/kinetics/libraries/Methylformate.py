#!/usr/bin/env python
# encoding: utf-8

name = "Methylformate"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 1,
    reactant1 = 
"""
Mfmt
1 C 0 0 {4,S} {5,S} {6,S} {7,S}
2 C 0 0 {3,D} {4,S} {8,S}
3 O 0 2 {2,D}
4 O 0 2 {1,S} {2,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
8 H 0 0 {2,S}
""",
    product1 = 
"""
CO
1 C 2T 0 {2,D}
2 O 0  2 {1,D}
""",
    product2 = 
"""
CH3OH
1 O 0 2 {2,S} {3,S}
2 C 0 0 {1,S} {4,S} {5,S} {6,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
5 H 0 0 {2,S}
6 H 0 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2128000000000.0, 's^-1'),
        n = 0.735,
        Ea = (68.628, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("Thu Feb  6 13:58:32 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> updated this entry by importing the old RMG database."""),
    ],
)

entry(
    index = 2,
    reactant1 = 
"""
Mfmt
1 C 0 0 {4,S} {5,S} {6,S} {7,S}
2 C 0 0 {3,D} {4,S} {8,S}
3 O 0 2 {2,D}
4 O 0 2 {1,S} {2,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
8 H 0 0 {2,S}
""",
    product1 = 
"""
CH2O
1 C 0 0 {2,D} {3,S} {4,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    product2 = 
"""
CH2O
1 C 0 0 {2,D} {3,S} {4,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2158000000.0, 's^-1'),
        n = 1.28,
        Ea = (75.979, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("Thu Feb  6 13:58:32 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> updated this entry by importing the old RMG database."""),
    ],
)

entry(
    index = 3,
    reactant1 = 
"""
Mfmt
1 C 0 0 {4,S} {5,S} {6,S} {7,S}
2 C 0 0 {3,D} {4,S} {8,S}
3 O 0 2 {2,D}
4 O 0 2 {1,S} {2,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
8 H 0 0 {2,S}
""",
    product1 = 
"""
CO2
1 C 0 0 {2,D} {3,D}
2 O 0 2 {1,D}
3 O 0 2 {1,D}
""",
    product2 = 
"""
CH4
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (453600000000.0, 's^-1'),
        n = 0.832,
        Ea = (83.612, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("Thu Feb  6 13:58:32 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> updated this entry by importing the old RMG database."""),
    ],
)

entry(
    index = 4,
    reactant1 = 
"""
Mofml
1 C 0 0 {4,S} {5,S} {6,S} {7,S}
2 C 1 0 {3,D} {4,S}
3 O 0 2 {2,D}
4 O 0 2 {1,S} {2,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
""",
    product1 = 
"""
CO2
1 C 0 0 {2,D} {3,D}
2 O 0 2 {1,D}
3 O 0 2 {1,D}
""",
    product2 = 
"""
CH3j
1 C 1 0 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2300000000.0, 's^-1'), n=1.09, Ea=(14.9, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("Thu Feb  6 13:58:32 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> updated this entry by importing the old RMG database."""),
    ],
)

entry(
    index = 5,
    reactant1 = 
"""
CO
1 C 2T 0 {2,D}
2 O 0  2 {1,D}
""",
    reactant2 = 
"""
CH3Oj
1 O 1 2 {2,S}
2 C 0 0 {1,S} {3,S} {4,S} {5,S}
3 H 0 0 {2,S}
4 H 0 0 {2,S}
5 H 0 0 {2,S}
""",
    product1 = 
"""
Mofml
1 C 0 0 {4,S} {5,S} {6,S} {7,S}
2 C 1 0 {3,D} {4,S}
3 O 0 2 {2,D}
4 O 0 2 {1,S} {2,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1970000000.0, 'cm^3/(mol*s)'),
        n = 1.27,
        Ea = (5.81, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("Thu Feb  6 13:58:32 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> updated this entry by importing the old RMG database."""),
    ],
)

entry(
    index = 6,
    reactant1 = 
"""
HCjO
1 C 1 0 {2,D} {3,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
""",
    reactant2 = 
"""
CH2O
1 C 0 0 {2,D} {3,S} {4,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    product1 = 
"""
Fmoml
1 C 1 0 {4,S} {5,S} {6,S}
2 C 0 0 {3,D} {4,S} {7,S}
3 O 0 2 {2,D}
4 O 0 2 {1,S} {2,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5030, 'cm^3/(mol*s)'), n=2.48, Ea=(9.32, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("Thu Feb  6 13:58:32 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> updated this entry by importing the old RMG database."""),
    ],
)

entry(
    index = 7,
    reactant1 = 
"""
Hj
1 H 1 0
""",
    reactant2 = 
"""
Mfmt
1 C 0 0 {4,S} {5,S} {6,S} {7,S}
2 C 0 0 {3,D} {4,S} {8,S}
3 O 0 2 {2,D}
4 O 0 2 {1,S} {2,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
8 H 0 0 {2,S}
""",
    product1 = 
"""
H2
1 H 0 0 {2,S}
2 H 0 0 {1,S}
""",
    product2 = 
"""
Mofml
1 C 0 0 {4,S} {5,S} {6,S} {7,S}
2 C 1 0 {3,D} {4,S}
3 O 0 2 {2,D}
4 O 0 2 {1,S} {2,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(228000, 'cm^3/(mol*s)'), n=2.5, Ea=(6.56, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("Thu Feb  6 13:58:32 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> updated this entry by importing the old RMG database."""),
    ],
)

entry(
    index = 8,
    reactant1 = 
"""
Hj
1 H 1 0
""",
    reactant2 = 
"""
Mfmt
1 C 0 0 {4,S} {5,S} {6,S} {7,S}
2 C 0 0 {3,D} {4,S} {8,S}
3 O 0 2 {2,D}
4 O 0 2 {1,S} {2,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
8 H 0 0 {2,S}
""",
    product1 = 
"""
H2
1 H 0 0 {2,S}
2 H 0 0 {1,S}
""",
    product2 = 
"""
Fmoml
1 C 1 0 {4,S} {5,S} {6,S}
2 C 0 0 {3,D} {4,S} {7,S}
3 O 0 2 {2,D}
4 O 0 2 {1,S} {2,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (116000, 'cm^3/(mol*s)'),
        n = 2.55,
        Ea = (7.62, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("Thu Feb  6 13:58:32 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> updated this entry by importing the old RMG database."""),
    ],
)

entry(
    index = 9,
    reactant1 = 
"""
CH3j
1 C 1 0 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    reactant2 = 
"""
Mfmt
1 C 0 0 {4,S} {5,S} {6,S} {7,S}
2 C 0 0 {3,D} {4,S} {8,S}
3 O 0 2 {2,D}
4 O 0 2 {1,S} {2,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
8 H 0 0 {2,S}
""",
    product1 = 
"""
CH4
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
""",
    product2 = 
"""
Mofml
1 C 0 0 {4,S} {5,S} {6,S} {7,S}
2 C 1 0 {3,D} {4,S}
3 O 0 2 {2,D}
4 O 0 2 {1,S} {2,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.34, 'cm^3/(mol*s)'), n=2.82, Ea=(6.81, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("Thu Feb  6 13:58:32 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> updated this entry by importing the old RMG database."""),
    ],
)

entry(
    index = 10,
    reactant1 = 
"""
CH3j
1 C 1 0 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    reactant2 = 
"""
Mfmt
1 C 0 0 {4,S} {5,S} {6,S} {7,S}
2 C 0 0 {3,D} {4,S} {8,S}
3 O 0 2 {2,D}
4 O 0 2 {1,S} {2,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
8 H 0 0 {2,S}
""",
    product1 = 
"""
CH4
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
""",
    product2 = 
"""
Fmoml
1 C 1 0 {4,S} {5,S} {6,S}
2 C 0 0 {3,D} {4,S} {7,S}
3 O 0 2 {2,D}
4 O 0 2 {1,S} {2,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.257, 'cm^3/(mol*s)'), n=3.96, Ea=(8.02, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("Thu Feb  6 13:58:32 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> updated this entry by importing the old RMG database."""),
    ],
)

entry(
    index = 11,
    reactant1 = 
"""
CH3Oj
1 O 1 2 {2,S}
2 C 0 0 {1,S} {3,S} {4,S} {5,S}
3 H 0 0 {2,S}
4 H 0 0 {2,S}
5 H 0 0 {2,S}
""",
    reactant2 = 
"""
HCjO
1 C 1 0 {2,D} {3,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
""",
    product1 = 
"""
Mfmt
1 C 0 0 {4,S} {5,S} {6,S} {7,S}
2 C 0 0 {3,D} {4,S} {8,S}
3 O 0 2 {2,D}
4 O 0 2 {1,S} {2,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
8 H 0 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("Thu Feb  6 13:58:32 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> updated this entry by importing the old RMG database."""),
    ],
)

entry(
    index = 12,
    reactant1 = 
"""
CH3j
1 C 1 0 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    reactant2 = 
"""
OjCHO
1 O 1 2 {2,S}
2 C 0 0 {1,S} {3,D} {4,S}
3 O 0 2 {2,D}
4 H 0 0 {2,S}
""",
    product1 = 
"""
Mfmt
1 C 0 0 {4,S} {5,S} {6,S} {7,S}
2 C 0 0 {3,D} {4,S} {8,S}
3 O 0 2 {2,D}
4 O 0 2 {1,S} {2,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
8 H 0 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("Thu Feb  6 13:58:32 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> updated this entry by importing the old RMG database."""),
    ],
)

