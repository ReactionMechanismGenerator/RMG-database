#!/usr/bin/env python
# encoding: utf-8

name = "OxygenSingTrip"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 1,
    reactant1 = 
"""
O2S
1 O 0 2 {2,D}
2 O 0 2 {1,D}
""",
    product1 = 
"""
O2
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(A=(0.00023, 's^-1'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
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
O2S
1 O 0 2 {2,D}
2 O 0 2 {1,D}
""",
    product1 = 
"""
O2
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    reversible = False,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4.05, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
        efficiencies = {'[O][O]': 5.43, 'O=C=O': 4.29},
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
O2S
1 O 0 2 {2,D}
2 O 0 2 {1,D}
""",
    product1 = 
"""
O2
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(3000000.0, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
        efficiencies = {'c1ccccc1': 1.067, 'O': 1.783, '[H][H]': 1.0, '[O][O]': 0.34, 'N#N': 0.028, '[C]=O': 14.0, '[Ar]': 0.00166},
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

