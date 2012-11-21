#!/usr/bin/env python
# encoding: utf-8

name = "Sulfur/thiophene"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 1,
    reactant1 = 
"""
CH2CHS
1 C 0 {2,D}
2 C 0 {1,D} {3,S}
3 S 1 {2,S}
""",
    reactant2 = 
"""
C2H4
1 C 0 {2,D}
2 C 0 {1,D}
""",
    product1 = 
"""
C4H7SJ(1)
1 C 0 {2,D}
2 C 0 {1,D} {3,S}
3 S 0 {2,S} {4,S}
4 C 0 {3,S} {5,S}
5 C 1 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (231.428, 'cm^3/(mol*s)'),
        n = 3.03333,
        Ea = (2.63333, 'kcal/mol'),
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
    ],
)

entry(
    index = 2,
    reactant1 = 
"""
C4H7SJ(1)
1 C 0 {2,D}
2 C 0 {1,D} {3,S}
3 S 0 {2,S} {4,S}
4 C 0 {3,S} {5,S}
5 C 1 {4,S}
""",
    product1 = 
"""
C4H7SJ(2)
1 C 0 {2,S} {5,S}
2 C 1 {1,S} {3,S}
3 S 0 {2,S} {4,S}
4 C 0 {3,S} {5,S}
5 C 0 {1,S} {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(122000000.0, 's^-1'), n=1.05, Ea=(15.82, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 3,
    reactant1 = 
"""
C4H6S
1 C 0 {2,D} {5,S}
2 C 0 {1,D} {3,S}
3 S 0 {2,S} {4,S}
4 C 0 {3,S} {5,S}
5 C 0 {1,S} {4,S}
""",
    reactant2 = 
"""
HJ
1 H 1
""",
    product1 = 
"""
C4H7SJ(2)
1 C 0 {2,S} {5,S}
2 C 1 {1,S} {3,S}
3 S 0 {2,S} {4,S}
4 C 0 {3,S} {5,S}
5 C 0 {1,S} {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (210178000.0, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (1.76498, 'kcal/mol'),
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
    ],
)

entry(
    index = 4,
    reactant1 = 
"""
C4H6S
1 C 0 {2,D} {5,S}
2 C 0 {1,D} {3,S}
3 S 0 {2,S} {4,S}
4 C 0 {3,S} {5,S}
5 C 0 {1,S} {4,S}
""",
    reactant2 = 
"""
HJ
1 H 1
""",
    product1 = 
"""
C4H7SJ(8)
1 C 0 {2,S} {5,S}
2 C 1 {1,S} {3,S}
3 S 0 {2,S} {4,S}
4 C 0 {3,S} {5,S}
5 C 0 {1,S} {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (242784000.0, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (0.959667, 'kcal/mol'),
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
    ],
)

entry(
    index = 5,
    reactant1 = 
"""
C4H6S
1 C 0 {2,D} {5,S}
2 C 0 {1,D} {3,S}
3 S 0 {2,S} {4,S}
4 C 0 {3,S} {5,S}
5 C 0 {1,S} {4,S}
""",
    reactant2 = 
"""
HJ
1 H 1
""",
    product1 = 
"""
C4H7SJ(9)
1 C 1 {2,S} {5,S}
2 C 0 {1,S} {3,S}
3 S 0 {2,S} {4,S}
4 C 0 {3,S} {5,S}
5 C 0 {1,S} {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (210178000.0, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (1.76498, 'kcal/mol'),
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
    ],
)

entry(
    index = 6,
    reactant1 = 
"""
thiophene
1 C 0 {2,D} {5,S}
2 C 0 {1,D} {3,S}
3 S 0 {2,S} {4,S}
4 C 0 {3,S} {5,D}
5 C 0 {1,S} {4,D}
""",
    reactant2 = 
"""
HJ
1 H 1
""",
    product1 = 
"""
C4H5SJ(6)
1 C 0 {2,D} {5,S}
2 C 0 {1,D} {3,S}
3 S 0 {2,S} {4,S}
4 C 1 {3,S} {5,S}
5 C 0 {1,S} {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (579853000.0, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (1.493, 'kcal/mol'),
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
    ],
)

entry(
    index = 7,
    reactant1 = 
"""
thiophene
1 C 0 {2,D} {5,S}
2 C 0 {1,D} {3,S}
3 S 0 {2,S} {4,S}
4 C 0 {3,S} {5,D}
5 C 0 {1,S} {4,D}
""",
    reactant2 = 
"""
HJ
1 H 1
""",
    product1 = 
"""
C4H5SJ(7)
1 C 0 {2,S} {5,D}
2 C 1 {1,S} {3,S}
3 S 0 {2,S} {4,S}
4 C 0 {3,S} {5,S}
5 C 0 {1,D} {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (420357000.0, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (1.76498, 'kcal/mol'),
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
    ],
)

