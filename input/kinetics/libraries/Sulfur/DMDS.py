#!/usr/bin/env python
# encoding: utf-8

name = "Sulfur/DMDS"
shortDesc = u""
longDesc = u"""

"""
entry(
    index        = 1,
    reactant1 = 
"""
C2H5SJ1
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,S} {7,S}
3 S U0 L2 E0  {1,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
""",
    product1 = 
"""
C2H5SJ2
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {1,S} {3,S} {7,S} {8,S}
3 S U1 L2 E0  {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (85.5, 's^-1'),
        n = 3.04,
        Ea = (11.62, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\DMDS.\nsmall molecule oxidation library, reaction file, version 2, JS, August 6, 2003\noriginally from Leeds methane oxidation mechanism v1.5\nhttp://www.chem.leeds.ac.uk/Combustion/Combustion.html\nfix bug for O2 + HCO = HO2 + CO 1.52E13 0.00 -7.09, change E into positive, change A into 5.12E13 according to NIST\nOntbinding DMDS',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
small molecule oxidation library, reaction file, version 2, JS, August 6, 2003
originally from Leeds methane oxidation mechanism v1.5
http://www.chem.leeds.ac.uk/Combustion/Combustion.html
fix bug for O2 + HCO = HO2 + CO 1.52E13 0.00 -7.09, change E into positive, change A into 5.12E13 according to NIST




Ontbinding DMDS
""",
)

entry(
    index        = 2,
    reactant1 = 
"""
C2H4
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
SH
multiplicity 2
1 S U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
C2H5SJ2
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {1,S} {3,S} {7,S} {8,S}
3 S U1 L2 E0  {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9960, 'cm^3/(mol*s)'),
        n = 2.7,
        Ea = (-0.8, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\DMDS.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 3,
    reactant1 = 
"""
SJJ_(S)
multiplicity 1
1 S U2 L2 E0 
""",
    reactant2 = 
"""
SJJ_(S)
multiplicity 1
1 S U2 L2 E0 
""",
    product1 = 
"""
S2_(S)
multiplicity 1
1 S U1 L2 E0  {2,S}
2 S U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (160000000000.0, 'cm^3/(mol*s)'),
        n = 1.3,
        Ea = (-0.88, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\DMDS.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

