#!/usr/bin/env python
# encoding: utf-8

name = "Sulfur/DMDS"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 1,
    reactant1 = 
"""
C2H5SJ1
1 C 1 {2,S} {4,S} {5,S}
2 C 0 {1,S} {3,S} {6,S} {7,S}
3 S 0 {2,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product1 = 
"""
C2H5SJ2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 S 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(85.5, 's^-1'), n=3.04, Ea=(11.62, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
small molecule oxidation library, reaction file, version 2, JS, August 6, 2003
originally from Leeds methane oxidation mechanism v1.5
http://www.chem.leeds.ac.uk/Combustion/Combustion.html
fix bug for O2 + HCO = HO2 + CO 1.52E13 0.00 -7.09, change E into positive, change A into 5.12E13 according to NIST




Ontbinding DMDS
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2,
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
SH
1 S 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C2H5SJ2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 S 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9960, 'cm^3/(mol*s)'), n=2.7, Ea=(-0.8, 'kcal/mol'), T0=(1, 'K')),
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
SJJ
1 S 2S
""",
    reactant2 = 
"""
SJJ
1 S 2S
""",
    product1 = 
"""
S2
1 S 1 {2,S}
2 S 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (160000000000.0, 'cm^3/(mol*s)'),
        n = 1.3,
        Ea = (-0.88, 'kcal/mol'),
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

