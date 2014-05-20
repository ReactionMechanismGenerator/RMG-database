#!/usr/bin/env python
# encoding: utf-8

name = "Dooley/methylformate_2"
shortDesc = u""
longDesc = u"""

"""
entry(
    index        = 1,
    reactant1 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    reactant2 = 
"""
CH2OCHO
multiplicity 2
1 C U1 L0 E0  {3,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {4,D} {7,S}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {2,D}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
CH3OCHO
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 2,
    reactant1 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    reactant2 = 
"""
CH3OCO
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 C U1 L0 E0  {2,S} {7,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {3,D}
""",
    product1 = 
"""
CH3OCHO
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
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
CH3OCHO
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH2OCHO
multiplicity 2
1 C U1 L0 E0  {3,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {4,D} {7,S}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {2,D}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (665000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (6494, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 4,
    reactant1 = 
"""
CH3OCHO
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2OCHO
multiplicity 2
1 C U1 L0 E0  {3,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {4,D} {7,S}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {2,D}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8860000000000.0, 'cm^3/(mol*s)'),
        n = 0.1,
        Ea = (3340, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 5,
    reactant1 = 
"""
CH3OCHO
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2OCHO
multiplicity 2
1 C U1 L0 E0  {3,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {4,D} {7,S}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {2,D}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.291, 'cm^3/(mol*s)'),
        n = 3.7,
        Ea = (6823, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 6,
    reactant1 = 
"""
CH3OCHO
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2OCHO
multiplicity 2
1 C U1 L0 E0  {3,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {4,D} {7,S}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {2,D}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H2O2
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (56600, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (16594, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 7,
    reactant1 = 
"""
CH3OCHO
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
CH3O2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U1 L2 E0  {2,S}
""",
    product1 = 
"""
CH2OCHO
multiplicity 2
1 C U1 L0 E0  {3,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {4,D} {7,S}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {2,D}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
CH3O2H
multiplicity 1
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 O U0 L2 E0  {2,S} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (56600, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (16594, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 8,
    reactant1 = 
"""
CH3OCHO
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
CH3O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2OCHO
multiplicity 2
1 C U1 L0 E0  {3,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {4,D} {7,S}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {2,D}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
CH3OH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4590000000.0, 'cm^3/(mol*s)'),
        n = 0.5,
        Ea = (4823, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 9,
    reactant1 = 
"""
CH3OCHO
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CH2OCHO
multiplicity 2
1 C U1 L0 E0  {3,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {4,D} {7,S}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {2,D}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (884000, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (4593, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 10,
    reactant1 = 
"""
CH3OCHO
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
CH2OCHO
multiplicity 2
1 C U1 L0 E0  {3,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {4,D} {7,S}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {2,D}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (15300000000000.0, 'cm^3/(mol*s)'),
        n = 0.1,
        Ea = (51749, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 11,
    reactant1 = 
"""
CH3OCHO
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2OCHO
multiplicity 2
1 C U1 L0 E0  {3,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {4,D} {7,S}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {2,D}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (102000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (18430, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 12,
    reactant1 = 
"""
CH3OCHO
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
OCHO
multiplicity 2
1 C U0 L0 E0  {2,S} {3,D} {4,S}
2 O U1 L2 E0  {1,S}
3 O U0 L2 E0  {1,D}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2OCHO
multiplicity 2
1 C U1 L0 E0  {3,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {4,D} {7,S}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {2,D}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
HCOOH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,D} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 O U0 L2 E0  {1,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (56600, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (16594, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 13,
    reactant1 = 
"""
CH3OCHO
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
C2H5
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,S} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
CH2OCHO
multiplicity 2
1 C U1 L0 E0  {3,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {4,D} {7,S}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {2,D}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
C2H6
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10400, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 14,
    reactant1 = 
"""
CH3OCHO
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
C2H3
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U1 L0 E0  {1,D} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
CH2OCHO
multiplicity 2
1 C U1 L0 E0  {3,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {4,D} {7,S}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {2,D}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
""",
    product2 = 
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
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10400, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 15,
    reactant1 = 
"""
CH3OCHO
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH3OCO
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 C U1 L0 E0  {2,S} {7,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {3,D}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (258000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (5736, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 16,
    reactant1 = 
"""
CH3OCHO
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3OCO
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 C U1 L0 E0  {2,S} {7,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {3,D}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.22e+16, 'cm^3/(mol*s)'),
        n = -1,
        Ea = (4946, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 17,
    reactant1 = 
"""
CH3OCHO
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3OCO
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 C U1 L0 E0  {2,S} {7,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {3,D}
""",
    product2 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0921, 'cm^3/(mol*s)'),
        n = 3.7,
        Ea = (6052, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 18,
    reactant1 = 
"""
CH3OCHO
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3OCO
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 C U1 L0 E0  {2,S} {7,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {3,D}
""",
    product2 = 
"""
H2O2
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (157000, 'cm^3/(mol*s)'),
        n = 2.2,
        Ea = (16544, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 19,
    reactant1 = 
"""
CH3OCHO
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
CH3O2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U1 L2 E0  {2,S}
""",
    product1 = 
"""
CH3OCO
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 C U1 L0 E0  {2,S} {7,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {3,D}
""",
    product2 = 
"""
CH3O2H
multiplicity 1
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 O U0 L2 E0  {2,S} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (157000, 'cm^3/(mol*s)'),
        n = 2.2,
        Ea = (16544, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 20,
    reactant1 = 
"""
CH3OCHO
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
CH3O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3OCO
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 C U1 L0 E0  {2,S} {7,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {3,D}
""",
    product2 = 
"""
CH3OH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5270000000.0, 'cm^3/(mol*s)'),
        n = 0.8,
        Ea = (2912, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 21,
    reactant1 = 
"""
CH3OCHO
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CH3OCO
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 C U1 L0 E0  {2,S} {7,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {3,D}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (245000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (4047, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 22,
    reactant1 = 
"""
CH3OCHO
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
CH3OCO
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 C U1 L0 E0  {2,S} {7,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {3,D}
""",
    product2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3850000000000.0, 'cm^3/(mol*s)'),
        n = 0.1,
        Ea = (50759, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 23,
    reactant1 = 
"""
CH3OCHO
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
OCHO
multiplicity 2
1 C U0 L0 E0  {2,S} {3,D} {4,S}
2 O U1 L2 E0  {1,S}
3 O U0 L2 E0  {1,D}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3OCO
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 C U1 L0 E0  {2,S} {7,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {3,D}
""",
    product2 = 
"""
HCOOH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,D} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 O U0 L2 E0  {1,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (157000, 'cm^3/(mol*s)'),
        n = 2.2,
        Ea = (16544, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 24,
    reactant1 = 
"""
CH3OCHO
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3OCO
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 C U1 L0 E0  {2,S} {7,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {3,D}
""",
    product2 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5400000.0, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (17010, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 25,
    reactant1 = 
"""
CH3OCHO
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
C2H5
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,S} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
CH3OCO
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 C U1 L0 E0  {2,S} {7,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {3,D}
""",
    product2 = 
"""
C2H6
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10400, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 26,
    reactant1 = 
"""
CH3OCHO
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
C2H3
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U1 L0 E0  {1,D} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
CH3OCO
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 C U1 L0 E0  {2,S} {7,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {3,D}
""",
    product2 = 
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
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10400, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 27,
    reactant1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CO2
multiplicity 1
1 C U0 L0 E0  {2,D} {3,D}
2 O U0 L2 E0  {1,D}
3 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
CH3OCO
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 C U1 L0 E0  {2,S} {7,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (47600000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (34700, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 28,
    reactant1 = 
"""
CH3O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    product1 = 
"""
CH3OCO
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 C U1 L0 E0  {2,S} {7,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1550000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (5730, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 29,
    reactant1 = 
"""
CH2OCHO
multiplicity 2
1 C U1 L0 E0  {3,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {4,D} {7,S}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {2,D}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
CH3OCO
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 C U1 L0 E0  {2,S} {7,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (262000000000.0, 's^-1'),
        n = 0,
        Ea = (38178, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 30,
    reactant1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2OCHO
multiplicity 2
1 C U1 L0 E0  {3,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {4,D} {7,S}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {2,D}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (389000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (22000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 31,
    reactant1 = 
"""
CH3OCO
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 C U1 L0 E0  {2,S} {7,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {3,D}
""",
    reactant2 = 
"""
CH3OCHO
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
CH3OCHO
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
CH2OCHO
multiplicity 2
1 C U1 L0 E0  {3,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {4,D} {7,S}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {2,D}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10400, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 32,
    reactant1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CH2OCHO
multiplicity 2
1 C U1 L0 E0  {3,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {4,D} {7,S}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {2,D}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
CH3CH2OCHO
multiplicity 1
1  C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2  C U0 L0 E0  {1,S} {7,S} {8,S} {9,S}
3  C U0 L0 E0  {4,S} {10,D} {11,S}
4  O U0 L2 E0  {1,S} {3,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {1,S}
7  H U0 L0 E0  {2,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {2,S}
10 O U0 L2 E0  {3,D}
11 H U0 L0 E0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 33,
    reactant1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CH3OCO
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 C U1 L0 E0  {2,S} {7,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {3,D}
""",
    product1 = 
"""
CH3CO2CH3
multiplicity 1
1  C U0 L0 E0  {3,S} {5,S} {6,S} {7,S}
2  C U0 L0 E0  {4,S} {8,S} {9,S} {10,S}
3  C U0 L0 E0  {1,S} {4,S} {11,D}
4  O U0 L2 E0  {2,S} {3,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {1,S}
7  H U0 L0 E0  {1,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {2,S}
10 H U0 L0 E0  {2,S}
11 O U0 L2 E0  {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 34,
    reactant1 = 
"""
CH2OCHO
multiplicity 2
1 C U1 L0 E0  {3,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {4,D} {7,S}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {2,D}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HO2CH2OCHO
multiplicity 1
1  C U0 L0 E0  {3,S} {4,S} {6,S} {7,S}
2  C U0 L0 E0  {3,S} {8,D} {9,S}
3  O U0 L2 E0  {1,S} {2,S}
4  O U0 L2 E0  {1,S} {5,S}
5  O U0 L2 E0  {4,S} {10,S}
6  H U0 L0 E0  {1,S}
7  H U0 L0 E0  {1,S}
8  O U0 L2 E0  {2,D}
9  H U0 L0 E0  {2,S}
10 H U0 L0 E0  {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 35,
    reactant1 = 
"""
CH3OCO
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 C U1 L0 E0  {2,S} {7,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {3,D}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3OCOO2H
multiplicity 1
1  C U0 L0 E0  {3,S} {6,S} {7,S} {8,S}
2  C U0 L0 E0  {3,S} {4,S} {9,D}
3  O U0 L2 E0  {1,S} {2,S}
4  O U0 L2 E0  {2,S} {5,S}
5  O U0 L2 E0  {4,S} {10,S}
6  H U0 L0 E0  {1,S}
7  H U0 L0 E0  {1,S}
8  H U0 L0 E0  {1,S}
9  O U0 L2 E0  {2,D}
10 H U0 L0 E0  {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 36,
    reactant1 = 
"""
OCH2OCHO
multiplicity 2
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 O U1 L2 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HO2CH2OCHO
multiplicity 1
1  C U0 L0 E0  {3,S} {4,S} {6,S} {7,S}
2  C U0 L0 E0  {3,S} {8,D} {9,S}
3  O U0 L2 E0  {1,S} {2,S}
4  O U0 L2 E0  {1,S} {5,S}
5  O U0 L2 E0  {4,S} {10,S}
6  H U0 L0 E0  {1,S}
7  H U0 L0 E0  {1,S}
8  O U0 L2 E0  {2,D}
9  H U0 L0 E0  {2,S}
10 H U0 L0 E0  {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1550000.0, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (-4132, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 37,
    reactant1 = 
"""
CH3OCOO
multiplicity 2
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 O U1 L2 E0  {2,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3OCOO2H
multiplicity 1
1  C U0 L0 E0  {3,S} {6,S} {7,S} {8,S}
2  C U0 L0 E0  {3,S} {4,S} {9,D}
3  O U0 L2 E0  {1,S} {2,S}
4  O U0 L2 E0  {2,S} {5,S}
5  O U0 L2 E0  {4,S} {10,S}
6  H U0 L0 E0  {1,S}
7  H U0 L0 E0  {1,S}
8  H U0 L0 E0  {1,S}
9  O U0 L2 E0  {2,D}
10 H U0 L0 E0  {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1550000.0, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (-4132, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 38,
    reactant1 = 
"""
CO2
multiplicity 1
1 C U0 L0 E0  {2,D} {3,D}
2 O U0 L2 E0  {1,D}
3 O U0 L2 E0  {1,D}
""",
    reactant2 = 
"""
CH3O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3OCOO
multiplicity 2
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 O U1 L2 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (9200, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 39,
    reactant1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
OCHO
multiplicity 2
1 C U0 L0 E0  {2,S} {3,D} {4,S}
2 O U1 L2 E0  {1,S}
3 O U0 L2 E0  {1,D}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
OCH2OCHO
multiplicity 2
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 O U1 L2 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (389000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 40,
    reactant1 = 
"""
CH3OCO
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 C U1 L0 E0  {2,S} {7,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {3,D}
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
CH3OCOOO
multiplicity 2
1 C U0 L0 E0  {3,S} {5,S} {6,S} {7,S}
2 C U0 L0 E0  {3,S} {4,S} {8,D}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {2,S} {9,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {1,S}
8 O U0 L2 E0  {2,D}
9 O U1 L2 E0  {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4520000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 41,
    reactant1 = 
"""
CH2OCHO
multiplicity 2
1 C U1 L0 E0  {3,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {4,D} {7,S}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {2,D}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
OOCH2OCHO
multiplicity 2
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {1,S} {9,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
9 O U1 L2 E0  {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4520000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 42,
    reactant1 = 
"""
OOCH2OCHO
multiplicity 2
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {1,S} {9,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
9 O U1 L2 E0  {4,S}
""",
    product1 = 
"""
HOOCH2OCO
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {6,S} {7,S}
2 O U0 L2 E0  {1,S} {4,S}
3 O U0 L2 E0  {1,S} {5,S}
4 C U1 L0 E0  {2,S} {8,D}
5 O U0 L2 E0  {3,S} {9,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {1,S}
8 O U0 L2 E0  {4,D}
9 H U0 L0 E0  {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (247000000000.0, 's^-1'),
        n = 0,
        Ea = (28900, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 43,
    reactant1 = 
"""
CH3OCOOO
multiplicity 2
1 C U0 L0 E0  {3,S} {5,S} {6,S} {7,S}
2 C U0 L0 E0  {3,S} {4,S} {8,D}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {2,S} {9,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {1,S}
8 O U0 L2 E0  {2,D}
9 O U1 L2 E0  {4,S}
""",
    product1 = 
"""
CH2OCOOOH
multiplicity 2
1 C U0 L0 E0  {3,S} {4,S} {6,D}
2 C U1 L0 E0  {3,S} {7,S} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {1,S} {5,S}
5 O U0 L2 E0  {4,S} {9,S}
6 O U0 L2 E0  {1,D}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (741000000000.0, 's^-1'),
        n = 0,
        Ea = (28900, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 44,
    reactant1 = 
"""
CH2O2H
multiplicity 2
1 C U1 L0 E0  {2,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {3,S}
3 O U0 L2 E0  {2,S} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
CO2
multiplicity 1
1 C U0 L0 E0  {2,D} {3,D}
2 O U0 L2 E0  {1,D}
3 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
HOOCH2OCO
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {6,S} {7,S}
2 O U0 L2 E0  {1,S} {4,S}
3 O U0 L2 E0  {1,S} {5,S}
4 C U1 L0 E0  {2,S} {8,D}
5 O U0 L2 E0  {3,S} {9,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {1,S}
8 O U0 L2 E0  {4,D}
9 H U0 L0 E0  {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2920000.0, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (36591, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 45,
    reactant1 = 
"""
OCH2O2H
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 O U0 L2 E0  {2,S} {7,S}
4 O U1 L2 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    product1 = 
"""
HOOCH2OCO
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {6,S} {7,S}
2 O U0 L2 E0  {1,S} {4,S}
3 O U0 L2 E0  {1,S} {5,S}
4 C U1 L0 E0  {2,S} {8,D}
5 O U0 L2 E0  {3,S} {9,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {1,S}
8 O U0 L2 E0  {4,D}
9 H U0 L0 E0  {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10800000.0, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (5588, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 46,
    reactant1 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2O2H
multiplicity 2
1 C U1 L0 E0  {2,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {3,S}
3 O U0 L2 E0  {2,S} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (23000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12900, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 47,
    reactant1 = 
"""
OCH2O2H
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 O U0 L2 E0  {2,S} {7,S}
4 O U1 L2 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.27e+18, 's^-1'),
        n = -1.8,
        Ea = (10460, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 48,
    reactant1 = 
"""
CH2OCOOOH
multiplicity 2
1 C U0 L0 E0  {3,S} {4,S} {6,D}
2 C U1 L0 E0  {3,S} {7,S} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {1,S} {5,S}
5 O U0 L2 E0  {4,S} {9,S}
6 O U0 L2 E0  {1,D}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {5,S}
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CO2
multiplicity 1
1 C U0 L0 E0  {2,D} {3,D}
2 O U0 L2 E0  {1,D}
3 O U0 L2 E0  {1,D}
""",
    product3 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.8e+18, 's^-1'),
        n = -1.5,
        Ea = (37360, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 49,
    reactant1 = 
"""
CH2OCOOOH
multiplicity 2
1 C U0 L0 E0  {3,S} {4,S} {6,D}
2 C U1 L0 E0  {3,S} {7,S} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {1,S} {5,S}
5 O U0 L2 E0  {4,S} {9,S}
6 O U0 L2 E0  {1,D}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {5,S}
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    product3 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.8e+18, 's^-1'),
        n = -1.5,
        Ea = (37360, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 50,
    reactant1 = 
"""
CH2OCOOOH
multiplicity 2
1 C U0 L0 E0  {3,S} {4,S} {6,D}
2 C U1 L0 E0  {3,S} {7,S} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {1,S} {5,S}
5 O U0 L2 E0  {4,S} {9,S}
6 O U0 L2 E0  {1,D}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {5,S}
""",
    product1 = 
"""
cyOCH2OCO
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {4,S} {7,D}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {1,S} {2,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (75000000000.0, 's^-1'),
        n = 0,
        Ea = (15250, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 51,
    reactant1 = 
"""
HOOCH2OCO
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {6,S} {7,S}
2 O U0 L2 E0  {1,S} {4,S}
3 O U0 L2 E0  {1,S} {5,S}
4 C U1 L0 E0  {2,S} {8,D}
5 O U0 L2 E0  {3,S} {9,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {1,S}
8 O U0 L2 E0  {4,D}
9 H U0 L0 E0  {5,S}
""",
    product1 = 
"""
cyOCH2OCO
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {4,S} {7,D}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {1,S} {2,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (75000000000.0, 's^-1'),
        n = 0,
        Ea = (15250, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 52,
    reactant1 = 
"""
CH2OCOOOH
multiplicity 2
1 C U0 L0 E0  {3,S} {4,S} {6,D}
2 C U1 L0 E0  {3,S} {7,S} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {1,S} {5,S}
5 O U0 L2 E0  {4,S} {9,S}
6 O U0 L2 E0  {1,D}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {5,S}
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
OOCH2OCOOOH
multiplicity 2
1  C U0 L0 E0  {3,S} {5,S} {7,S} {8,S}
2  C U0 L0 E0  {3,S} {4,S} {9,D}
3  O U0 L2 E0  {1,S} {2,S}
4  O U0 L2 E0  {2,S} {6,S}
5  O U0 L2 E0  {1,S} {10,S}
6  O U0 L2 E0  {4,S} {11,S}
7  H U0 L0 E0  {1,S}
8  H U0 L0 E0  {1,S}
9  O U0 L2 E0  {2,D}
10 O U1 L2 E0  {5,S}
11 H U0 L0 E0  {6,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4520000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 53,
    reactant1 = 
"""
HOOCH2OCO
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {6,S} {7,S}
2 O U0 L2 E0  {1,S} {4,S}
3 O U0 L2 E0  {1,S} {5,S}
4 C U1 L0 E0  {2,S} {8,D}
5 O U0 L2 E0  {3,S} {9,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {1,S}
8 O U0 L2 E0  {4,D}
9 H U0 L0 E0  {5,S}
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
HOOCH2OCOOO
multiplicity 2
1  C U0 L0 E0  {3,S} {4,S} {7,S} {8,S}
2  C U0 L0 E0  {3,S} {5,S} {9,D}
3  O U0 L2 E0  {1,S} {2,S}
4  O U0 L2 E0  {1,S} {6,S}
5  O U0 L2 E0  {2,S} {10,S}
6  O U0 L2 E0  {4,S} {11,S}
7  H U0 L0 E0  {1,S}
8  H U0 L0 E0  {1,S}
9  O U0 L2 E0  {2,D}
10 O U1 L2 E0  {5,S}
11 H U0 L0 E0  {6,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4520000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 54,
    reactant1 = 
"""
OOCH2OCOOOH
multiplicity 2
1  C U0 L0 E0  {3,S} {5,S} {7,S} {8,S}
2  C U0 L0 E0  {3,S} {4,S} {9,D}
3  O U0 L2 E0  {1,S} {2,S}
4  O U0 L2 E0  {2,S} {6,S}
5  O U0 L2 E0  {1,S} {10,S}
6  O U0 L2 E0  {4,S} {11,S}
7  H U0 L0 E0  {1,S}
8  H U0 L0 E0  {1,S}
9  O U0 L2 E0  {2,D}
10 O U1 L2 E0  {5,S}
11 H U0 L0 E0  {6,S}
""",
    product1 = 
"""
OCHOCOOOH
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {6,D}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {1,S} {5,S}
5 O U0 L2 E0  {4,S} {9,S}
6 O U0 L2 E0  {1,D}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {5,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28900000000.0, 's^-1'),
        n = 0,
        Ea = (21863, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 55,
    reactant1 = 
"""
HOOCH2OCOOO
multiplicity 2
1  C U0 L0 E0  {3,S} {4,S} {7,S} {8,S}
2  C U0 L0 E0  {3,S} {5,S} {9,D}
3  O U0 L2 E0  {1,S} {2,S}
4  O U0 L2 E0  {1,S} {6,S}
5  O U0 L2 E0  {2,S} {10,S}
6  O U0 L2 E0  {4,S} {11,S}
7  H U0 L0 E0  {1,S}
8  H U0 L0 E0  {1,S}
9  O U0 L2 E0  {2,D}
10 O U1 L2 E0  {5,S}
11 H U0 L0 E0  {6,S}
""",
    product1 = 
"""
OCHOCOOOH
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {6,D}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {1,S} {5,S}
5 O U0 L2 E0  {4,S} {9,S}
6 O U0 L2 E0  {1,D}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {5,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (248000000000.0, 's^-1'),
        n = 0,
        Ea = (20900, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 56,
    reactant1 = 
"""
OCHOCOOOH
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {6,D}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {1,S} {5,S}
5 O U0 L2 E0  {4,S} {9,S}
6 O U0 L2 E0  {1,D}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {5,S}
""",
    product1 = 
"""
CO2
multiplicity 1
1 C U0 L0 E0  {2,D} {3,D}
2 O U0 L2 E0  {1,D}
3 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
OCHO
multiplicity 2
1 C U0 L0 E0  {2,S} {3,D} {4,S}
2 O U1 L2 E0  {1,S}
3 O U0 L2 E0  {1,D}
4 H U0 L0 E0  {1,S}
""",
    product3 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.05e+16, 's^-1'),
        n = 0,
        Ea = (41600, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 57,
    reactant1 = 
"""
cyOCH2OCO
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {4,S} {7,D}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {1,S} {2,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CHOOCO
multiplicity 2
1 C U1 L0 E0  {3,S} {4,S} {6,S}
2 C U0 L0 E0  {3,S} {4,S} {5,D}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {1,S} {2,S}
5 O U0 L2 E0  {2,D}
6 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (480000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (2005, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 58,
    reactant1 = 
"""
cyOCH2OCO
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {4,S} {7,D}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {1,S} {2,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CHOOCO
multiplicity 2
1 C U1 L0 E0  {3,S} {4,S} {6,S}
2 C U0 L0 E0  {3,S} {4,S} {5,D}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {1,S} {2,S}
5 O U0 L2 E0  {2,D}
6 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2400000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1192, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 59,
    reactant1 = 
"""
cyOCH2OCO
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {4,S} {7,D}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {1,S} {2,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CHOOCO
multiplicity 2
1 C U1 L0 E0  {3,S} {4,S} {6,S}
2 C U0 L0 E0  {3,S} {4,S} {5,D}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {1,S} {2,S}
5 O U0 L2 E0  {2,D}
6 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2O2
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12976, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 60,
    reactant1 = 
"""
OCHO
multiplicity 2
1 C U0 L0 E0  {2,S} {3,D} {4,S}
2 O U1 L2 E0  {1,S}
3 O U0 L2 E0  {1,D}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    product1 = 
"""
CHOOCO
multiplicity 2
1 C U1 L0 E0  {3,S} {4,S} {6,S}
2 C U0 L0 E0  {3,S} {4,S} {5,D}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {1,S} {2,S}
5 O U0 L2 E0  {2,D}
6 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10800000.0, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (5588, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 61,
    reactant1 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CO2
multiplicity 1
1 C U0 L0 E0  {2,D} {3,D}
2 O U0 L2 E0  {1,D}
3 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
CHOOCO
multiplicity 2
1 C U1 L0 E0  {3,S} {4,S} {6,S}
2 C U0 L0 E0  {3,S} {4,S} {5,D}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {1,S} {2,S}
5 O U0 L2 E0  {2,D}
6 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2920000.0, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (36591, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 62,
    reactant1 = 
"""
CH3OCHO
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
CH3OH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(20000000000000.0, 's^-1'), n=0, Ea=(60000, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.4e+59, 'cm^3/(mol*s)'),
            n = -11.8,
            Ea = (71400, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.239,
        T3 = (555.1, 'K'),
        T1 = (8430000000.0, 'K'),
        T2 = (8210000000.0, 'K'),
        efficiencies = {},
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 63,
    reactant1 = 
"""
CH3OCHO
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CO2
multiplicity 1
1 C U0 L0 E0  {2,D} {3,D}
2 O U0 L2 E0  {1,D}
3 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1500000000000.0, 's^-1'), n=0, Ea=(59700, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.63e+61, 'cm^3/(mol*s)'),
            n = -12.79,
            Ea = (71100, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.179,
        T3 = (357.5, 'K'),
        T1 = (9918000000.0, 'K'),
        T2 = (3280000000.0, 'K'),
        efficiencies = {},
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 64,
    reactant1 = 
"""
CH3OCHO
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1000000000000.0, 's^-1'), n=0, Ea=(60500, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.55e+57, 'cm^3/(mol*s)'),
            n = -11.57,
            Ea = (71700, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.781,
        T3 = (6490000000.0, 'K'),
        T1 = (618, 'K'),
        T2 = (6710000000.0, 'K'),
        efficiencies = {},
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 65,
    reactant1 = 
"""
CH3OCHO
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
OCHO
multiplicity 2
1 C U0 L0 E0  {2,S} {3,D} {4,S}
2 O U1 L2 E0  {1,S}
3 O U0 L2 E0  {1,D}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.17e+24, 's^-1'), n=-2.4, Ea=(92600, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.71e+47, 'cm^3/(mol*s)'),
            n = -8.43,
            Ea = (98490, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 6.89e-15,
        T3 = (4730, 'K'),
        T1 = (9330000000.0, 'K'),
        T2 = (1780000000.0, 'K'),
        efficiencies = {},
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 66,
    reactant1 = 
"""
CH3OCHO
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
CH3O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4.18e+16, 's^-1'), n=0, Ea=(97400, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.27e+63, 'cm^3/(mol*s)'),
            n = -12.3,
            Ea = (109180, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.894,
        T3 = (7490000000.0, 'K'),
        T1 = (647, 'K'),
        T2 = (669000000.0, 'K'),
        efficiencies = {},
        comment = 'Reaction and kinetics from Dooley\\methylformate_2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

