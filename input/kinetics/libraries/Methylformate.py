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
1 C 0 {4,S} {5,S} {6,S} {7,S}
2 C 0 {3,D} {4,S} {8,S}
3 O 0 {2,D}
4 O 0 {1,S} {2,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
CH3OH
1 O 0 {2,S} {3,S}
2 C 0 {1,S} {4,S} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {2,S}
5 H 0 {2,S}
6 H 0 {2,S}
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
Some methylformate reactions.
These are HIGH PRESSURE LIMITS (for use as a reaction library, not a seed mechanism)
Some rates provided by CFGold; file compiled by RWest.



Mfmt is methylformate              SMILES:     COC=O
Mofml is methoxy-formyl radical    SMILES:   CO[C]=O
Fmoml is Formyloxy-methyl radical  SMILES: [CH2]OC=O

Unimolecular decomposition high-pressure rates.

These are from http://dx.doi.org/10.1021/jp9120436
W. K. Metcalfe, J. M. Simmie, and H. J. Curran. Ab Initio Chemical Kinetics of
Methyl Formate Decomposition: The Simplest Model Biodiesel. The Journal of
Physical Chemistry A, 114(17):5478-5484, May 2010.
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2,
    reactant1 = 
"""
Mfmt
1 C 0 {4,S} {5,S} {6,S} {7,S}
2 C 0 {3,D} {4,S} {8,S}
3 O 0 {2,D}
4 O 0 {1,S} {2,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
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
    ],
)

entry(
    index = 3,
    reactant1 = 
"""
Mfmt
1 C 0 {4,S} {5,S} {6,S} {7,S}
2 C 0 {3,D} {4,S} {8,S}
3 O 0 {2,D}
4 O 0 {1,S} {2,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
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
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
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
    ],
)

entry(
    index = 4,
    reactant1 = 
"""
Mofml
1 C 0 {4,S} {5,S} {6,S} {7,S}
2 C 1 {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {1,S} {2,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
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
CH3j
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2300000000.0, 's^-1'), n=1.09, Ea=(14.9, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
These are CFGoldsmith's QCI calculations
Mfmt        = CO + CH3OH    6.49e+04    2.62    64.4    0   0   0
Mfmt        = CO2 + CH4     4.52e+06    2.06    79.4    0   0   0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 5,
    reactant1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    reactant2 = 
"""
CH3Oj
1 O 1 {2,S}
2 C 0 {1,S} {3,S} {4,S} {5,S}
3 H 0 {2,S}
4 H 0 {2,S}
5 H 0 {2,S}
""",
    product1 = 
"""
Mofml
1 C 0 {4,S} {5,S} {6,S} {7,S}
2 C 1 {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {1,S} {2,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
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
    ],
)

entry(
    index = 6,
    reactant1 = 
"""
HCjO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    reactant2 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
Fmoml
1 C 1 {4,S} {5,S} {6,S}
2 C 0 {3,D} {4,S} {7,S}
3 O 0 {2,D}
4 O 0 {1,S} {2,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
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
    ],
)

entry(
    index = 7,
    reactant1 = 
"""
Hj
1 H 1
""",
    reactant2 = 
"""
Mfmt
1 C 0 {4,S} {5,S} {6,S} {7,S}
2 C 0 {3,D} {4,S} {8,S}
3 O 0 {2,D}
4 O 0 {1,S} {2,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
""",
    product1 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
Mofml
1 C 0 {4,S} {5,S} {6,S} {7,S}
2 C 1 {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {1,S} {2,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(228000, 'cm^3/(mol*s)'), n=2.5, Ea=(6.56, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
H-abstraction
These are done using CBS-QB3, since the QCI method takes too long.
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 8,
    reactant1 = 
"""
Hj
1 H 1
""",
    reactant2 = 
"""
Mfmt
1 C 0 {4,S} {5,S} {6,S} {7,S}
2 C 0 {3,D} {4,S} {8,S}
3 O 0 {2,D}
4 O 0 {1,S} {2,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
""",
    product1 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
Fmoml
1 C 1 {4,S} {5,S} {6,S}
2 C 0 {3,D} {4,S} {7,S}
3 O 0 {2,D}
4 O 0 {1,S} {2,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
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
    ],
)

entry(
    index = 9,
    reactant1 = 
"""
CH3j
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
Mfmt
1 C 0 {4,S} {5,S} {6,S} {7,S}
2 C 0 {3,D} {4,S} {8,S}
3 O 0 {2,D}
4 O 0 {1,S} {2,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
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
Mofml
1 C 0 {4,S} {5,S} {6,S} {7,S}
2 C 1 {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {1,S} {2,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
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
    ],
)

entry(
    index = 10,
    reactant1 = 
"""
CH3j
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
Mfmt
1 C 0 {4,S} {5,S} {6,S} {7,S}
2 C 0 {3,D} {4,S} {8,S}
3 O 0 {2,D}
4 O 0 {1,S} {2,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
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
Fmoml
1 C 1 {4,S} {5,S} {6,S}
2 C 0 {3,D} {4,S} {7,S}
3 O 0 {2,D}
4 O 0 {1,S} {2,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
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
    ],
)

entry(
    index = 11,
    reactant1 = 
"""
CH3Oj
1 O 1 {2,S}
2 C 0 {1,S} {3,S} {4,S} {5,S}
3 H 0 {2,S}
4 H 0 {2,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
HCjO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product1 = 
"""
Mfmt
1 C 0 {4,S} {5,S} {6,S} {7,S}
2 C 0 {3,D} {4,S} {8,S}
3 O 0 {2,D}
4 O 0 {1,S} {2,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
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
Radical-Radical recombinations guessed by Mike (based on Klippenstein's rule of thumb)
(Klippenstein said they were 1.8e13 times-or-divide 5)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 12,
    reactant1 = 
"""
CH3j
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
OjCHO
1 O 1 {2,S}
2 C 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 H 0 {2,S}
""",
    product1 = 
"""
Mfmt
1 C 0 {4,S} {5,S} {6,S} {7,S}
2 C 0 {3,D} {4,S} {8,S}
3 O 0 {2,D}
4 O 0 {1,S} {2,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
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
    ],
)

