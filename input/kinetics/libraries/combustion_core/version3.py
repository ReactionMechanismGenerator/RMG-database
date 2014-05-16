#!/usr/bin/env python
# encoding: utf-8

name = "combustion_core/version3"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    reactant1 = 
"""
C2H2
multiplicity 1
1 C 0 0 {2,T} {3,S}
2 C 0 0 {1,T} {4,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O 2 2
""",
    product1 = 
"""
CH2_(T)
multiplicity 3
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2170000.0, 'cm^3/(mol*s)'),
        n = 2.1,
        Ea = (6.57, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    reactant1 = 
"""
C2H2
multiplicity 1
1 C 0 0 {2,T} {3,S}
2 C 0 0 {1,T} {4,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O 2 2
""",
    product1 = 
"""
HCCO
multiplicity 2
1 C 1 0 {2,D} {4,S}
2 C 0 0 {1,D} {3,D}
3 O 0 2 {2,D}
4 H 0 0 {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5060000.0, 'cm^3/(mol*s)'),
        n = 2.1,
        Ea = (6.57, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    reactant1 = 
"""
C4H2
multiplicity 1
1 C 0 0 {2,S} {3,T}
2 C 0 0 {1,S} {4,T}
3 C 0 0 {1,T} {5,S}
4 C 0 0 {2,T} {6,S}
5 H 0 0 {3,S}
6 H 0 0 {4,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O 2 2
""",
    product1 = 
"""
C3H2_(S)
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 C 0 0 {1,D} {3,S} {5,S}
3 C 2 0 {1,S} {2,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7890000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5.64, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    reactant1 = 
"""
O2_(T)
multiplicity 3
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    reactant2 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    product1 = 
"""
CO2
multiplicity 1
1 C 0 0 {2,D} {3,D}
2 O 0 2 {1,D}
3 O 0 2 {1,D}
""",
    product2 = 
"""
O_(T)
multiplicity 3
1 O 2 2
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (12600000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (196.9, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    reactant1 = 
"""
O2_(T)
multiplicity 3
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    reactant2 = 
"""
CH_(Q)
multiplicity 4
1 C 3 0 {2,S}
2 H 0 0 {1,S}
""",
    product1 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    product2 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (16600000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    reactant1 = 
"""
O2_(T)
multiplicity 3
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    reactant2 = 
"""
CH_(Q)
multiplicity 4
1 C 3 0 {2,S}
2 H 0 0 {1,S}
""",
    product1 = 
"""
CO2
multiplicity 1
1 C 0 0 {2,D} {3,D}
2 O 0 2 {1,D}
3 O 0 2 {1,D}
""",
    product2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (16600000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    reactant1 = 
"""
O2_(T)
multiplicity 3
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    reactant2 = 
"""
CH2_(T)
multiplicity 3
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product1 = 
"""
CO2
multiplicity 1
1 C 0 0 {2,D} {3,D}
2 O 0 2 {1,D}
3 O 0 2 {1,D}
""",
    product2 = 
"""
H2
multiplicity 1
1 H 0 0 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5430000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6.24, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    reactant1 = 
"""
O2_(T)
multiplicity 3
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    reactant2 = 
"""
CH2_(T)
multiplicity 3
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product1 = 
"""
CO2
multiplicity 1
1 C 0 0 {2,D} {3,D}
2 O 0 2 {1,D}
3 O 0 2 {1,D}
""",
    product2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    product3 = 
"""
H
multiplicity 2
1 H 1 0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5430000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6.24, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    reactant1 = 
"""
O2_(T)
multiplicity 3
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    reactant2 = 
"""
CH2_(T)
multiplicity 3
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product1 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    product2 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    product3 = 
"""
H
multiplicity 2
1 H 1 0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8150000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6.24, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    reactant1 = 
"""
O2_(T)
multiplicity 3
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    reactant2 = 
"""
CH2_(T)
multiplicity 3
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product1 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O 0 2 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1480000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6.24, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    reactant1 = 
"""
O2_(T)
multiplicity 3
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    reactant2 = 
"""
CH2_(T)
multiplicity 3
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    product2 = 
"""
O_(T)
multiplicity 3
1 O 2 2
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6.24, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    reactant1 = 
"""
O2_(T)
multiplicity 3
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    reactant2 = 
"""
CH2_(S)
multiplicity 1
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product1 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    product2 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    product3 = 
"""
H
multiplicity 2
1 H 1 0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (31300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    reactant1 = 
"""
O2_(T)
multiplicity 3
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    reactant2 = 
"""
HCO
multiplicity 2
1 C 1 0 {2,D} {3,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
""",
    product1 = 
"""
HO2
multiplicity 2
1 O 0 2 {2,S} {3,S}
2 O 1 2 {1,S}
3 H 0 0 {1,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3010000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    reactant1 = 
"""
O2_(T)
multiplicity 3
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    reactant2 = 
"""
HCCO
multiplicity 2
1 C 1 0 {2,D} {4,S}
2 C 0 0 {1,D} {3,D}
3 O 0 2 {2,D}
4 H 0 0 {1,S}
""",
    product1 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    product2 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    product3 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1630000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3.58, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    reactant1 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    product1 = 
"""
CO2
multiplicity 1
1 C 0 0 {2,D} {3,D}
2 O 0 2 {1,D}
3 O 0 2 {1,D}
""",
    product2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (16600000.0, 'cm^3/(mol*s)'),
        n = 1.3,
        Ea = (-3.2, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    reactant1 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O 0 2 {2,S} {3,S}
2 O 1 2 {1,S}
3 H 0 0 {1,S}
""",
    product1 = 
"""
CO2
multiplicity 1
1 C 0 0 {2,D} {3,D}
2 O 0 2 {1,D}
3 O 0 2 {1,D}
""",
    product2 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (151000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (99.02, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    reactant1 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    reactant2 = 
"""
CH_(Q)
multiplicity 4
1 C 3 0 {2,S}
2 H 0 0 {1,S}
""",
    product1 = 
"""
HCCO
multiplicity 2
1 C 1 0 {2,D} {4,S}
2 C 0 0 {1,D} {3,D}
3 O 0 2 {2,D}
4 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (277000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-7.15, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    reactant1 = 
"""
CO2
multiplicity 1
1 C 0 0 {2,D} {3,D}
2 O 0 2 {1,D}
3 O 0 2 {1,D}
""",
    reactant2 = 
"""
CH_(Q)
multiplicity 4
1 C 3 0 {2,S}
2 H 0 0 {1,S}
""",
    product1 = 
"""
HCO
multiplicity 2
1 C 1 0 {2,D} {3,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3430000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2.87, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    reactant1 = 
"""
CO2
multiplicity 1
1 C 0 0 {2,D} {3,D}
2 O 0 2 {1,D}
3 O 0 2 {1,D}
""",
    reactant2 = 
"""
CH2_(T)
multiplicity 3
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (23500000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    reactant1 = 
"""
CH2CO
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 C 0 0 {1,D} {5,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 O 0 2 {2,D}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    product1 = 
"""
CH3
multiplicity 2
1 C 1 0 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14.13, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    reactant1 = 
"""
CH2CO
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 C 0 0 {1,D} {5,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 O 0 2 {2,D}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O 2 2
""",
    product1 = 
"""
CH2_(T)
multiplicity 3
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product2 = 
"""
CO2
multiplicity 1
1 C 0 0 {2,D} {3,D}
2 O 0 2 {1,D}
3 O 0 2 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1330000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5.65, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    reactant1 = 
"""
CH2CO
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 C 0 0 {1,D} {5,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 O 0 2 {2,D}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O 2 2
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (458000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5.65, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    reactant1 = 
"""
CH2CO
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 C 0 0 {1,D} {5,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 O 0 2 {2,D}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O 2 2
""",
    product1 = 
"""
HCO
multiplicity 2
1 C 1 0 {2,D} {3,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    product3 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (252000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5.65, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    reactant1 = 
"""
CH2CO
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 C 0 0 {1,D} {5,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 O 0 2 {2,D}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O 2 2
""",
    product1 = 
"""
HCO
multiplicity 2
1 C 1 0 {2,D} {3,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
""",
    product2 = 
"""
HCO
multiplicity 2
1 C 1 0 {2,D} {3,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (252000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5.65, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    reactant1 = 
"""
CH2CO
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 C 0 0 {1,D} {5,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 O 0 2 {2,D}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    product1 = 
"""
CH3
multiplicity 2
1 C 1 0 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    product2 = 
"""
CO2
multiplicity 1
1 C 0 0 {2,D} {3,D}
2 O 0 2 {1,D}
3 O 0 2 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2520000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    reactant1 = 
"""
CH2CO
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 C 0 0 {1,D} {5,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 O 0 2 {2,D}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    product1 = 
"""
CH2OH
multiplicity 2
1 C 1 0 {2,S} {3,S} {4,S}
2 O 0 2 {1,S} {5,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4680000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    reactant1 = 
"""
H
multiplicity 2
1 H 1 0
""",
    reactant2 = 
"""
HCO
multiplicity 2
1 C 1 0 {2,D} {3,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
""",
    product1 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    product2 = 
"""
H2
multiplicity 1
1 H 0 0 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (90300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    reactant1 = 
"""
H
multiplicity 2
1 H 1 0
""",
    reactant2 = 
"""
HCCO
multiplicity 2
1 C 1 0 {2,D} {4,S}
2 C 0 0 {1,D} {3,D}
3 O 0 2 {2,D}
4 H 0 0 {1,S}
""",
    product1 = 
"""
CH2_(T)
multiplicity 3
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (151000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    reactant1 = 
"""
CH_(Q)
multiplicity 4
1 C 3 0 {2,S}
2 H 0 0 {1,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O 2 2
""",
    product1 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    product2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (39700000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    reactant1 = 
"""
CH3
multiplicity 2
1 C 1 0 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    reactant2 = 
"""
HCO
multiplicity 2
1 C 1 0 {2,D} {3,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
""",
    product1 = 
"""
CH4
multiplicity 1
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (120000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    reactant1 = 
"""
C2H
multiplicity 2
1 C 0 0 {2,T} {3,S}
2 C 1 0 {1,T}
3 H 0 0 {1,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O 2 2
""",
    product1 = 
"""
CH_(Q)
multiplicity 4
1 C 3 0 {2,S}
2 H 0 0 {1,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    reactant1 = 
"""
C2H
multiplicity 2
1 C 0 0 {2,T} {3,S}
2 C 1 0 {1,T}
3 H 0 0 {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    product1 = 
"""
CH2_(T)
multiplicity 3
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    reactant1 = 
"""
C2H3
multiplicity 2
1 C 0 0 {2,D} {3,S} {4,S}
2 C 1 0 {1,D} {5,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O 2 2
""",
    product1 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    product2 = 
"""
CH3
multiplicity 2
1 C 1 0 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    reactant1 = 
"""
H2CCCH
multiplicity 2
1 C 1 0 {2,S} {4,S} {5,S}
2 C 0 0 {1,S} {3,T}
3 C 0 0 {2,T} {6,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {3,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O 2 2
""",
    product1 = 
"""
C2H2
multiplicity 1
1 C 0 0 {2,T} {3,S}
2 C 0 0 {1,T} {4,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    product3 = 
"""
H
multiplicity 2
1 H 1 0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (139000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    reactant1 = 
"""
O_(T)
multiplicity 3
1 O 2 2
""",
    reactant2 = 
"""
HCO
multiplicity 2
1 C 1 0 {2,D} {3,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
""",
    product1 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    product2 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    reactant1 = 
"""
O_(T)
multiplicity 3
1 O 2 2
""",
    reactant2 = 
"""
HCCO
multiplicity 2
1 C 1 0 {2,D} {4,S}
2 C 0 0 {1,D} {3,D}
3 O 0 2 {2,D}
4 H 0 0 {1,S}
""",
    product1 = 
"""
H
multiplicity 2
1 H 1 0
""",
    product2 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    product3 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (96400000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    reactant1 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    reactant2 = 
"""
HCO
multiplicity 2
1 C 1 0 {2,D} {3,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
""",
    product1 = 
"""
H2O
multiplicity 1
1 O 0 2 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (102000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    reactant1 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    reactant2 = 
"""
HCCO
multiplicity 2
1 C 1 0 {2,D} {4,S}
2 C 0 0 {1,D} {3,D}
3 O 0 2 {2,D}
4 H 0 0 {1,S}
""",
    product1 = 
"""
HCO
multiplicity 2
1 C 1 0 {2,D} {3,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
""",
    product2 = 
"""
HCO
multiplicity 2
1 C 1 0 {2,D} {3,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    reactant1 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    reactant2 = 
"""
HCCO
multiplicity 2
1 C 1 0 {2,D} {4,S}
2 C 0 0 {1,D} {3,D}
3 O 0 2 {2,D}
4 H 0 0 {1,S}
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    reactant1 = 
"""
HCO
multiplicity 2
1 C 1 0 {2,D} {3,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
""",
    reactant2 = 
"""
HCO
multiplicity 2
1 C 1 0 {2,D} {3,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    reactant1 = 
"""
HCCO
multiplicity 2
1 C 1 0 {2,D} {4,S}
2 C 0 0 {1,D} {3,D}
3 O 0 2 {2,D}
4 H 0 0 {1,S}
""",
    reactant2 = 
"""
HCCO
multiplicity 2
1 C 1 0 {2,D} {4,S}
2 C 0 0 {1,D} {3,D}
3 O 0 2 {2,D}
4 H 0 0 {1,S}
""",
    product1 = 
"""
C2H2
multiplicity 1
1 C 0 0 {2,T} {3,S}
2 C 0 0 {1,T} {4,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    product3 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    reactant1 = 
"""
CH_(Q)
multiplicity 4
1 C 3 0 {2,S}
2 H 0 0 {1,S}
""",
    reactant2 = 
"""
HCCO
multiplicity 2
1 C 1 0 {2,D} {4,S}
2 C 0 0 {1,D} {3,D}
3 O 0 2 {2,D}
4 H 0 0 {1,S}
""",
    product1 = 
"""
C2H2
multiplicity 1
1 C 0 0 {2,T} {3,S}
2 C 0 0 {1,T} {4,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    reactant1 = 
"""
CH2_(T)
multiplicity 3
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O 2 2
""",
    product1 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    product2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    product3 = 
"""
H
multiplicity 2
1 H 1 0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (72000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    reactant1 = 
"""
CH2_(T)
multiplicity 3
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O 2 2
""",
    product1 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    product2 = 
"""
H2
multiplicity 1
1 H 0 0 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (48000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    reactant1 = 
"""
CH2_(T)
multiplicity 3
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    reactant2 = 
"""
HCO
multiplicity 2
1 C 1 0 {2,D} {3,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
""",
    product1 = 
"""
CH3
multiplicity 2
1 C 1 0 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    reactant1 = 
"""
CH2_(T)
multiplicity 3
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    reactant2 = 
"""
HCCO
multiplicity 2
1 C 1 0 {2,D} {4,S}
2 C 0 0 {1,D} {3,D}
3 O 0 2 {2,D}
4 H 0 0 {1,S}
""",
    product1 = 
"""
C2H3
multiplicity 2
1 C 0 0 {2,D} {3,S} {4,S}
2 C 1 0 {1,D} {5,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    reactant1 = 
"""
O2_(T)
multiplicity 3
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    reactant2 = 
"""
C2H
multiplicity 2
1 C 0 0 {2,T} {3,S}
2 C 1 0 {1,T}
3 H 0 0 {1,S}
""",
    product1 = 
"""
CO2
multiplicity 1
1 C 0 0 {2,D} {3,D}
2 O 0 2 {1,D}
3 O 0 2 {1,D}
""",
    product2 = 
"""
CH_(Q)
multiplicity 4
1 C 3 0 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9050000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    reactant1 = 
"""
O_(T)
multiplicity 3
1 O 2 2
""",
    reactant2 = 
"""
HCO
multiplicity 2
1 C 1 0 {2,D} {3,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
""",
    product1 = 
"""
CO2
multiplicity 1
1 C 0 0 {2,D} {3,D}
2 O 0 2 {1,D}
3 O 0 2 {1,D}
""",
    product2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    reactant1 = 
"""
CH4
multiplicity 1
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
""",
    reactant2 = 
"""
CH_(Q)
multiplicity 4
1 C 3 0 {2,S}
2 H 0 0 {1,S}
""",
    product1 = 
"""
C2H4
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 C 0 0 {1,D} {5,S} {6,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
6 H 0 0 {2,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1.66, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 50,
    reactant1 = 
"""
C2H2
multiplicity 1
1 C 0 0 {2,T} {3,S}
2 C 0 0 {1,T} {4,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
""",
    reactant2 = 
"""
CH_(Q)
multiplicity 4
1 C 3 0 {2,S}
2 H 0 0 {1,S}
""",
    product1 = 
"""
C2H
multiplicity 2
1 C 0 0 {2,T} {3,S}
2 C 1 0 {1,T}
3 H 0 0 {1,S}
""",
    product2 = 
"""
CH2_(T)
multiplicity 3
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (211000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.51, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    reactant1 = 
"""
C2H4
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 C 0 0 {1,D} {5,S} {6,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
6 H 0 0 {2,S}
""",
    reactant2 = 
"""
CH_(Q)
multiplicity 4
1 C 3 0 {2,S}
2 H 0 0 {1,S}
""",
    product1 = 
"""
C3H4
multiplicity 1
1 C 0 0 {3,D} {4,S} {5,S}
2 C 0 0 {3,D} {6,S} {7,S}
3 C 0 0 {1,D} {2,D}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {2,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (132000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1.44, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    reactant1 = 
"""
C2H6
multiplicity 1
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {2,S}
8 H 0 0 {2,S}
""",
    reactant2 = 
"""
CH_(Q)
multiplicity 4
1 C 3 0 {2,S}
2 H 0 0 {1,S}
""",
    product1 = 
"""
C2H4
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 C 0 0 {1,D} {5,S} {6,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
6 H 0 0 {2,S}
""",
    product2 = 
"""
CH3
multiplicity 2
1 C 1 0 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (108000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1.1, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 53,
    reactant1 = 
"""
CH2O
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    reactant2 = 
"""
CH_(Q)
multiplicity 4
1 C 3 0 {2,S}
2 H 0 0 {1,S}
""",
    product1 = 
"""
CH2_(T)
multiplicity 3
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product2 = 
"""
HCO
multiplicity 2
1 C 1 0 {2,D} {3,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (96400000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-2.16, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    reactant1 = 
"""
H
multiplicity 2
1 H 1 0
""",
    reactant2 = 
"""
CH2_(T)
multiplicity 3
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product1 = 
"""
CH_(Q)
multiplicity 4
1 C 3 0 {2,S}
2 H 0 0 {1,S}
""",
    product2 = 
"""
H2
multiplicity 1
1 H 0 0 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6020000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-7.48, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
    reactant1 = 
"""
CH_(Q)
multiplicity 4
1 C 3 0 {2,S}
2 H 0 0 {1,S}
""",
    reactant2 = 
"""
CH2_(T)
multiplicity 3
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product1 = 
"""
C2H2
multiplicity 1
1 C 0 0 {2,T} {3,S}
2 C 0 0 {1,T} {4,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
    reactant1 = 
"""
CH_(Q)
multiplicity 4
1 C 3 0 {2,S}
2 H 0 0 {1,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C 1 0 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    product1 = 
"""
C2H3
multiplicity 2
1 C 0 0 {2,D} {3,S} {4,S}
2 C 1 0 {1,D} {5,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 57,
    reactant1 = 
"""
CH_(Q)
multiplicity 4
1 C 3 0 {2,S}
2 H 0 0 {1,S}
""",
    reactant2 = 
"""
C2H3
multiplicity 2
1 C 0 0 {2,D} {3,S} {4,S}
2 C 1 0 {1,D} {5,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
""",
    product1 = 
"""
CH2_(T)
multiplicity 3
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product2 = 
"""
C2H2
multiplicity 1
1 C 0 0 {2,T} {3,S}
2 C 0 0 {1,T} {4,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 58,
    reactant1 = 
"""
CH_(Q)
multiplicity 4
1 C 3 0 {2,S}
2 H 0 0 {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    product1 = 
"""
HCO
multiplicity 2
1 C 1 0 {2,D} {3,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 59,
    reactant1 = 
"""
CH2_(T)
multiplicity 3
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    reactant2 = 
"""
CH2_(T)
multiplicity 3
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product1 = 
"""
C2H2
multiplicity 1
1 C 0 0 {2,T} {3,S}
2 C 0 0 {1,T} {4,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
""",
    product2 = 
"""
H2
multiplicity 1
1 H 0 0 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (12000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3.33, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
    reactant1 = 
"""
CH2_(T)
multiplicity 3
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    reactant2 = 
"""
CH2_(T)
multiplicity 3
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product1 = 
"""
C2H2
multiplicity 1
1 C 0 0 {2,T} {3,S}
2 C 0 0 {1,T} {4,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    product3 = 
"""
H
multiplicity 2
1 H 1 0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (108000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3.33, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 61,
    reactant1 = 
"""
CH2_(T)
multiplicity 3
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C 1 0 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    product1 = 
"""
C2H4
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 C 0 0 {1,D} {5,S} {6,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
6 H 0 0 {2,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (42200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
    reactant1 = 
"""
CH2_(T)
multiplicity 3
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    reactant2 = 
"""
C2H3
multiplicity 2
1 C 0 0 {2,D} {3,S} {4,S}
2 C 1 0 {1,D} {5,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
""",
    product1 = 
"""
C2H2
multiplicity 1
1 C 0 0 {2,T} {3,S}
2 C 0 0 {1,T} {4,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
""",
    product2 = 
"""
CH3
multiplicity 2
1 C 1 0 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    reactant1 = 
"""
CH2_(T)
multiplicity 3
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 64,
    reactant1 = 
"""
CH2_(T)
multiplicity 3
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    reactant2 = 
"""
HCCO
multiplicity 2
1 C 1 0 {2,D} {4,S}
2 C 0 0 {1,D} {3,D}
3 O 0 2 {2,D}
4 H 0 0 {1,S}
""",
    product1 = 
"""
C2H
multiplicity 2
1 C 0 0 {2,T} {3,S}
2 C 1 0 {1,T}
3 H 0 0 {1,S}
""",
    product2 = 
"""
CH2O
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8.37, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 65,
    reactant1 = 
"""
CH4
multiplicity 1
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
""",
    reactant2 = 
"""
CH2_(T)
multiplicity 3
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product1 = 
"""
CH3
multiplicity 2
1 C 1 0 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    product2 = 
"""
CH3
multiplicity 2
1 C 1 0 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (42, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 66,
    reactant1 = 
"""
CH4
multiplicity 1
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
""",
    reactant2 = 
"""
CH2_(S)
multiplicity 1
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product1 = 
"""
CH3
multiplicity 2
1 C 1 0 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    product2 = 
"""
CH3
multiplicity 2
1 C 1 0 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (70000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 67,
    reactant1 = 
"""
C2H2
multiplicity 1
1 C 0 0 {2,T} {3,S}
2 C 0 0 {1,T} {4,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
""",
    reactant2 = 
"""
CH2_(T)
multiplicity 3
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product1 = 
"""
C3H4
multiplicity 1
1 C 0 0 {3,D} {4,S} {5,S}
2 C 0 0 {3,D} {6,S} {7,S}
3 C 0 0 {1,D} {2,D}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (12000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (27.69, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 68,
    reactant1 = 
"""
C2H2
multiplicity 1
1 C 0 0 {2,T} {3,S}
2 C 0 0 {1,T} {4,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
""",
    reactant2 = 
"""
CH2_(S)
multiplicity 1
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product1 = 
"""
H2CCCH
multiplicity 2
1 C 1 0 {2,S} {4,S} {5,S}
2 C 0 0 {1,S} {3,T}
3 C 0 0 {2,T} {6,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {3,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (175000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    reactant1 = 
"""
H
multiplicity 2
1 H 1 0
""",
    reactant2 = 
"""
CH2_(S)
multiplicity 1
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product1 = 
"""
CH2_(T)
multiplicity 3
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (200000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 70,
    reactant1 = 
"""
H2
multiplicity 1
1 H 0 0 {2,S}
2 H 0 0 {1,S}
""",
    reactant2 = 
"""
CH2_(S)
multiplicity 1
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product1 = 
"""
CH3
multiplicity 2
1 C 1 0 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (72300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    reactant1 = 
"""
C2H4
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 C 0 0 {1,D} {5,S} {6,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
6 H 0 0 {2,S}
""",
    reactant2 = 
"""
CH2_(S)
multiplicity 1
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product1 = 
"""
C3H6
multiplicity 1
1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 0 {1,S} {3,D} {7,S}
3 C 0 0 {2,D} {8,S} {9,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
8 H 0 0 {3,S}
9 H 0 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (96400000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 72,
    reactant1 = 
"""
C2H6
multiplicity 1
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {2,S}
8 H 0 0 {2,S}
""",
    reactant2 = 
"""
CH2_(S)
multiplicity 1
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product1 = 
"""
CH3
multiplicity 2
1 C 1 0 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    product2 = 
"""
C2H5
multiplicity 2
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 0 {1,S} {6,S} {7,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (240000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 73,
    reactant1 = 
"""
CH3
multiplicity 2
1 C 1 0 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    product1 = 
"""
CH2_(S)
multiplicity 1
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O 0 2 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (72300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.64, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 74,
    reactant1 = 
"""
C2H2
multiplicity 1
1 C 0 0 {2,T} {3,S}
2 C 0 0 {1,T} {4,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
""",
    reactant2 = 
"""
C2H2
multiplicity 1
1 C 0 0 {2,T} {3,S}
2 C 0 0 {1,T} {4,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
""",
    product1 = 
"""
H2CCCCH
multiplicity 2
1 C 0 0 {2,D} {5,S} {6,S}
2 C 1 0 {1,D} {3,S}
3 C 0 0 {2,S} {4,T}
4 C 0 0 {3,T} {7,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {4,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (242, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 75,
    reactant1 = 
"""
C2H2
multiplicity 1
1 C 0 0 {2,T} {3,S}
2 C 0 0 {1,T} {4,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
""",
    reactant2 = 
"""
C2H
multiplicity 2
1 C 0 0 {2,T} {3,S}
2 C 1 0 {1,T}
3 H 0 0 {1,S}
""",
    product1 = 
"""
C4H2
multiplicity 1
1 C 0 0 {2,S} {3,T}
2 C 0 0 {1,S} {4,T}
3 C 0 0 {1,T} {5,S}
4 C 0 0 {2,T} {6,S}
5 H 0 0 {3,S}
6 H 0 0 {4,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (90300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
    reactant1 = 
"""
C2H4
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 C 0 0 {1,D} {5,S} {6,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
6 H 0 0 {2,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O 2 2
""",
    product1 = 
"""
H
multiplicity 2
1 H 1 0
""",
    product2 = 
"""
CH2HCO
multiplicity 2
1 C 1 0 {2,S} {4,S} {5,S}
2 C 0 0 {1,S} {3,D} {6,S}
3 O 0 2 {2,D}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4740000.0, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (0.75, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 77,
    reactant1 = 
"""
C2H4
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 C 0 0 {1,D} {5,S} {6,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
6 H 0 0 {2,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O 2 2
""",
    product1 = 
"""
CH3
multiplicity 2
1 C 1 0 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    product2 = 
"""
HCO
multiplicity 2
1 C 1 0 {2,D} {3,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8130000.0, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (0.75, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 78,
    reactant1 = 
"""
C2H4
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 C 0 0 {1,D} {5,S} {6,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
6 H 0 0 {2,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O 2 2
""",
    product1 = 
"""
CH2CO
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 C 0 0 {1,D} {5,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 O 0 2 {2,D}
""",
    product2 = 
"""
H2
multiplicity 1
1 H 0 0 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (680000, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (0.75, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 79,
    reactant1 = 
"""
C4H2
multiplicity 1
1 C 0 0 {2,S} {3,T}
2 C 0 0 {1,S} {4,T}
3 C 0 0 {1,T} {5,S}
4 C 0 0 {2,T} {6,S}
5 H 0 0 {3,S}
6 H 0 0 {4,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    product1 = 
"""
C3H2_(S)
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 C 0 0 {1,D} {3,S} {5,S}
3 C 2 0 {1,S} {2,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
""",
    product2 = 
"""
HCO
multiplicity 2
1 C 1 0 {2,D} {3,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6680000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1.71, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 80,
    reactant1 = 
"""
O2_(T)
multiplicity 3
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    reactant3 = 
"""
H2O
multiplicity 1
1 O 0 2 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product1 = 
"""
HO2
multiplicity 2
1 O 0 2 {2,S} {3,S}
2 O 1 2 {1,S}
3 H 0 0 {1,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O 0 2 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6890000000000000.0, 'cm^6/(mol^2*s)'),
        n = 0,
        Ea = (-8.73, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 81,
    reactant1 = 
"""
O2_(T)
multiplicity 3
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    product1 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    product2 = 
"""
O_(T)
multiplicity 3
1 O 2 2
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (97560000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (62.11, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 82,
    reactant1 = 
"""
O2_(T)
multiplicity 3
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C 1 0 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (331000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (37.42, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 83,
    reactant1 = 
"""
O2_(T)
multiplicity 3
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    reactant2 = 
"""
C2H
multiplicity 2
1 C 0 0 {2,T} {3,S}
2 C 1 0 {1,T}
3 H 0 0 {1,S}
""",
    product1 = 
"""
HCCO
multiplicity 2
1 C 1 0 {2,D} {4,S}
2 C 0 0 {1,D} {3,D}
3 O 0 2 {2,D}
4 H 0 0 {1,S}
""",
    product2 = 
"""
O_(T)
multiplicity 3
1 O 2 2
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9050000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 84,
    reactant1 = 
"""
O2_(T)
multiplicity 3
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    reactant2 = 
"""
C3H2_(S)
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 C 0 0 {1,D} {3,S} {5,S}
3 C 2 0 {1,S} {2,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
""",
    product1 = 
"""
HCO
multiplicity 2
1 C 1 0 {2,D} {3,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
""",
    product2 = 
"""
HCCO
multiplicity 2
1 C 1 0 {2,D} {4,S}
2 C 0 0 {1,D} {3,D}
3 O 0 2 {2,D}
4 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 85,
    reactant1 = 
"""
O2_(T)
multiplicity 3
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    reactant2 = 
"""
H2CCCH
multiplicity 2
1 C 1 0 {2,S} {4,S} {5,S}
2 C 0 0 {1,S} {3,T}
3 C 0 0 {2,T} {6,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {3,S}
""",
    product1 = 
"""
CH2CO
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 C 0 0 {1,D} {5,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 O 0 2 {2,D}
""",
    product2 = 
"""
HCO
multiplicity 2
1 C 1 0 {2,D} {3,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30100000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 86,
    reactant1 = 
"""
H2O2
multiplicity 1
1 O 0 2 {2,S} {3,S}
2 O 0 2 {1,S} {4,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    product1 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O 0 2 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14.97, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 87,
    reactant1 = 
"""
CH3
multiplicity 2
1 C 1 0 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C 1 0 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    product1 = 
"""
C2H5
multiplicity 2
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 0 {1,S} {6,S} {7,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {2,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (56.54, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 88,
    reactant1 = 
"""
H
multiplicity 2
1 H 1 0
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O 0 2 {2,S} {3,S}
2 O 1 2 {1,S}
3 H 0 0 {1,S}
""",
    product1 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (169000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3.66, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 89,
    reactant1 = 
"""
H
multiplicity 2
1 H 1 0
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O 0 2 {2,S} {3,S}
2 O 1 2 {1,S}
3 H 0 0 {1,S}
""",
    product1 = 
"""
H2O
multiplicity 1
1 O 0 2 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product2 = 
"""
O_(T)
multiplicity 3
1 O 2 2
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7.2, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 90,
    reactant1 = 
"""
H
multiplicity 2
1 H 1 0
""",
    reactant2 = 
"""
CH2OH
multiplicity 2
1 C 1 0 {2,S} {3,S} {4,S}
2 O 0 2 {1,S} {5,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
""",
    product1 = 
"""
CH3
multiplicity 2
1 C 1 0 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 91,
    reactant1 = 
"""
CH3
multiplicity 2
1 C 1 0 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O 2 2
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (84300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 92,
    reactant1 = 
"""
CH3
multiplicity 2
1 C 1 0 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O 0 2 {2,S} {3,S}
2 O 1 2 {1,S}
3 H 0 0 {1,S}
""",
    product1 = 
"""
CH3O
multiplicity 2
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 2 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 93,
    reactant1 = 
"""
C2H
multiplicity 2
1 C 0 0 {2,T} {3,S}
2 C 1 0 {1,T}
3 H 0 0 {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    product1 = 
"""
HCCO
multiplicity 2
1 C 1 0 {2,D} {4,S}
2 C 0 0 {1,D} {3,D}
3 O 0 2 {2,D}
4 H 0 0 {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 94,
    reactant1 = 
"""
C2H5
multiplicity 2
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 0 {1,S} {6,S} {7,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {2,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O 2 2
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    product2 = 
"""
CH3
multiplicity 2
1 C 1 0 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (66200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 95,
    reactant1 = 
"""
O2_(T)
multiplicity 3
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C 1 0 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    product1 = 
"""
CH3O
multiplicity 2
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 2 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
""",
    product2 = 
"""
O_(T)
multiplicity 3
1 O 2 2
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (44000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (131.37, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 96,
    reactant1 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    product1 = 
"""
O_(T)
multiplicity 3
1 O 2 2
""",
    product2 = 
"""
H2O
multiplicity 1
1 O 0 2 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1510000000.0, 'cm^3/(mol*s)'),
        n = 1.14,
        Ea = (0.42, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 97,
    reactant1 = 
"""
H2
multiplicity 1
1 H 0 0 {2,S}
2 H 0 0 {1,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O 2 2
""",
    product1 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (51200, 'cm^3/(mol*s)'),
        n = 2.67,
        Ea = (26.27, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 98,
    reactant1 = 
"""
H2O
multiplicity 1
1 O 0 2 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    product1 = 
"""
H2
multiplicity 1
1 H 0 0 {2,S}
2 H 0 0 {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (452000000.0, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (77.08, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 99,
    reactant1 = 
"""
CH4
multiplicity 1
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O 2 2
""",
    product1 = 
"""
CH3
multiplicity 2
1 C 1 0 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (723000000.0, 'cm^3/(mol*s)'),
        n = 1.56,
        Ea = (35.5, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 100,
    reactant1 = 
"""
CH4
multiplicity 1
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    product1 = 
"""
CH3
multiplicity 2
1 C 1 0 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O 0 2 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (15700000.0, 'cm^3/(mol*s)'),
        n = 1.83,
        Ea = (11.64, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 101,
    reactant1 = 
"""
C2H2
multiplicity 1
1 C 0 0 {2,T} {3,S}
2 C 0 0 {1,T} {4,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    product1 = 
"""
C2H
multiplicity 2
1 C 0 0 {2,T} {3,S}
2 C 1 0 {1,T}
3 H 0 0 {1,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O 0 2 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (60000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (54.04, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 102,
    reactant1 = 
"""
C2H4
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 C 0 0 {1,D} {5,S} {6,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
6 H 0 0 {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    product1 = 
"""
C2H3
multiplicity 2
1 C 0 0 {2,D} {3,S} {4,S}
2 C 1 0 {1,D} {5,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
""",
    product2 = 
"""
H2
multiplicity 1
1 H 0 0 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (542000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (62.36, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 103,
    reactant1 = 
"""
C2H4
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 C 0 0 {1,D} {5,S} {6,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
6 H 0 0 {2,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    product1 = 
"""
C2H3
multiplicity 2
1 C 0 0 {2,D} {3,S} {4,S}
2 C 1 0 {1,D} {5,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O 0 2 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (24.86, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 104,
    reactant1 = 
"""
C2H6
multiplicity 1
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {2,S}
8 H 0 0 {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    product1 = 
"""
C2H5
multiplicity 2
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 0 {1,S} {6,S} {7,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {2,S}
""",
    product2 = 
"""
H2
multiplicity 1
1 H 0 0 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1450000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (31.01, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 105,
    reactant1 = 
"""
C2H6
multiplicity 1
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {2,S}
8 H 0 0 {2,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C 1 0 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    product1 = 
"""
C2H5
multiplicity 2
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 0 {1,S} {6,S} {7,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {2,S}
""",
    product2 = 
"""
CH4
multiplicity 1
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.51e-07, 'cm^3/(mol*s)'),
        n = 6,
        Ea = (25.3, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 106,
    reactant1 = 
"""
C2H6
multiplicity 1
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {2,S}
8 H 0 0 {2,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O 2 2
""",
    product1 = 
"""
C2H5
multiplicity 2
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 0 {1,S} {6,S} {7,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {2,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1000000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (24.28, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 107,
    reactant1 = 
"""
C2H6
multiplicity 1
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {2,S}
8 H 0 0 {2,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    product1 = 
"""
C2H5
multiplicity 2
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 0 {1,S} {6,S} {7,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {2,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O 0 2 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7230000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (3.62, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 108,
    reactant1 = 
"""
C2H6
multiplicity 1
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {2,S}
8 H 0 0 {2,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O 0 2 {2,S} {3,S}
2 O 1 2 {1,S}
3 H 0 0 {1,S}
""",
    product1 = 
"""
H2O2
multiplicity 1
1 O 0 2 {2,S} {3,S}
2 O 0 2 {1,S} {4,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
""",
    product2 = 
"""
C2H5
multiplicity 2
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 0 {1,S} {6,S} {7,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (13200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (85.63, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 109,
    reactant1 = 
"""
O2_(T)
multiplicity 3
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    reactant2 = 
"""
CH2O
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    product1 = 
"""
HCO
multiplicity 2
1 C 1 0 {2,D} {3,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
""",
    product2 = 
"""
HO2
multiplicity 2
1 O 0 2 {2,S} {3,S}
2 O 1 2 {1,S}
3 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (60200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (170.11, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 110,
    reactant1 = 
"""
O2_(T)
multiplicity 3
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    reactant2 = 
"""
CH3O
multiplicity 2
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 2 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    product2 = 
"""
HO2
multiplicity 2
1 O 0 2 {2,S} {3,S}
2 O 1 2 {1,S}
3 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (21700000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7.32, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 111,
    reactant1 = 
"""
H2O2
multiplicity 1
1 O 0 2 {2,S} {3,S}
2 O 0 2 {1,S} {4,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    product1 = 
"""
HO2
multiplicity 2
1 O 0 2 {2,S} {3,S}
2 O 1 2 {1,S}
3 H 0 0 {1,S}
""",
    product2 = 
"""
H2
multiplicity 1
1 H 0 0 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1690000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (15.71, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 112,
    reactant1 = 
"""
H2O2
multiplicity 1
1 O 0 2 {2,S} {3,S}
2 O 0 2 {1,S} {4,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O 2 2
""",
    product1 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    product2 = 
"""
HO2
multiplicity 2
1 O 0 2 {2,S} {3,S}
2 O 1 2 {1,S}
3 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (662000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (16.63, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 113,
    reactant1 = 
"""
H2O2
multiplicity 1
1 O 0 2 {2,S} {3,S}
2 O 0 2 {1,S} {4,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    product1 = 
"""
H2O
multiplicity 1
1 O 0 2 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product2 = 
"""
HO2
multiplicity 2
1 O 0 2 {2,S} {3,S}
2 O 1 2 {1,S}
3 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7830000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5.57, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 114,
    reactant1 = 
"""
CH2O
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    product1 = 
"""
HCO
multiplicity 2
1 C 1 0 {2,D} {3,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
""",
    product2 = 
"""
H2
multiplicity 1
1 H 0 0 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (126000000.0, 'cm^3/(mol*s)'),
        n = 1.62,
        Ea = (9.06, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 115,
    reactant1 = 
"""
CH2O
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C 1 0 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    product1 = 
"""
CH4
multiplicity 1
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
""",
    product2 = 
"""
HCO
multiplicity 2
1 C 1 0 {2,D} {3,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.83e-08, 'cm^3/(mol*s)'),
        n = 6.1,
        Ea = (8.23, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 116,
    reactant1 = 
"""
CH2O
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O 2 2
""",
    product1 = 
"""
HCO
multiplicity 2
1 C 1 0 {2,D} {3,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (416000000000.0, 'cm^3/(mol*s)'),
        n = 0.57,
        Ea = (11.56, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 117,
    reactant1 = 
"""
CH2O
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    product1 = 
"""
HCO
multiplicity 2
1 C 1 0 {2,D} {3,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O 0 2 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3430000000.0, 'cm^3/(mol*s)'),
        n = 1.18,
        Ea = (-1.87, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 118,
    reactant1 = 
"""
H
multiplicity 2
1 H 1 0
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O 0 2 {2,S} {3,S}
2 O 1 2 {1,S}
3 H 0 0 {1,S}
""",
    product1 = 
"""
H2
multiplicity 1
1 H 0 0 {2,S}
2 H 0 0 {1,S}
""",
    product2 = 
"""
O2_(T)
multiplicity 3
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (42800000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5.9, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 119,
    reactant1 = 
"""
H
multiplicity 2
1 H 1 0
""",
    reactant2 = 
"""
CH3O
multiplicity 2
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 2 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    product2 = 
"""
H2
multiplicity 1
1 H 0 0 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 120,
    reactant1 = 
"""
O_(T)
multiplicity 3
1 O 2 2
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O 0 2 {2,S} {3,S}
2 O 1 2 {1,S}
3 H 0 0 {1,S}
""",
    product1 = 
"""
O2_(T)
multiplicity 3
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (31900000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 121,
    reactant1 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O 0 2 {2,S} {3,S}
2 O 1 2 {1,S}
3 H 0 0 {1,S}
""",
    product1 = 
"""
H2O
multiplicity 1
1 O 0 2 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product2 = 
"""
O2_(T)
multiplicity 3
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28900000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-2.08, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 122,
    reactant1 = 
"""
O2_(T)
multiplicity 3
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C 1 0 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    product1 = 
"""
CH3O2
multiplicity 2
1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 2 {1,S} {3,S}
3 O 1 2 {2,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (261300000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 123,
    reactant1 = 
"""
O2_(T)
multiplicity 3
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    reactant2 = 
"""
C3H5
multiplicity 2
1 C 0 0 {2,D} {3,S} {4,S}
2 C 0 0 {1,D} {5,S} {6,S}
3 C 1 0 {1,S} {7,S} {8,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
6 H 0 0 {2,S}
7 H 0 0 {3,S}
8 H 0 0 {3,S}
""",
    product1 = 
"""
C3H5O2
multiplicity 2
1  C 0 0 {2,D} {3,S} {6,S}
2  C 0 0 {1,D} {7,S} {8,S}
3  C 0 0 {1,S} {4,S} {9,S} {10,S}
4  O 0 2 {3,S} {5,S}
5  O 1 2 {4,S}
6  H 0 0 {1,S}
7  H 0 0 {2,S}
8  H 0 0 {2,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30559000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 124,
    reactant1 = 
"""
O2_(T)
multiplicity 3
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    reactant2 = 
"""
C2H5
multiplicity 2
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 0 {1,S} {6,S} {7,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {2,S}
""",
    product1 = 
"""
C2H5O2
multiplicity 2
1 C 0 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 0 {1,S} {3,S} {8,S} {9,S}
3 O 0 2 {2,S} {4,S}
4 O 1 2 {3,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
8 H 0 0 {2,S}
9 H 0 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (147960000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 125,
    reactant1 = 
"""
O2_(T)
multiplicity 3
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    reactant2 = 
"""
CH2OH
multiplicity 2
1 C 1 0 {2,S} {3,S} {4,S}
2 O 0 2 {1,S} {5,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
""",
    product1 = 
"""
CH3O3_2
multiplicity 2
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 2 {1,S} {7,S}
3 O 0 2 {1,S} {6,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 O 1 2 {3,S}
7 H 0 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (57828000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 126,
    reactant1 = 
"""
O2_(T)
multiplicity 3
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    reactant2 = 
"""
C3H7
multiplicity 2
1  C 0 0 {3,S} {4,S} {5,S} {6,S}
2  C 0 0 {3,S} {7,S} {8,S} {9,S}
3  C 1 0 {1,S} {2,S} {10,S}
4  H 0 0 {1,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {2,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 H 0 0 {3,S}
""",
    product1 = 
"""
C3H7O2
multiplicity 2
1  C 0 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 2 {2,S} {5,S}
5  O 1 2 {4,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {2,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
12 H 0 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (592070000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 127,
    reactant1 = 
"""
C2H4
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 C 0 0 {1,D} {5,S} {6,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
6 H 0 0 {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    product1 = 
"""
C2H5
multiplicity 2
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 0 {1,S} {6,S} {7,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7059770.0, 'cm^3/(mol*s)'),
        n = 1.28,
        Ea = (1.29, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 128,
    reactant1 = 
"""
O2_(T)
multiplicity 3
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    reactant2 = 
"""
CH2HCO
multiplicity 2
1 C 1 0 {2,S} {4,S} {5,S}
2 C 0 0 {1,S} {3,D} {6,S}
3 O 0 2 {2,D}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
""",
    product1 = 
"""
C2H3O3
multiplicity 2
1 C 0 0 {2,S} {3,D} {6,S}
2 C 0 0 {1,S} {4,S} {7,S} {8,S}
3 O 0 2 {1,D}
4 O 0 2 {2,S} {5,S}
5 O 1 2 {4,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
8 H 0 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (149671000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 129,
    reactant1 = 
"""
C3H6
multiplicity 1
1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 0 {1,S} {3,D} {7,S}
3 C 0 0 {2,D} {8,S} {9,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
8 H 0 0 {3,S}
9 H 0 0 {3,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    product1 = 
"""
C3H7
multiplicity 2
1  C 0 0 {3,S} {4,S} {5,S} {6,S}
2  C 0 0 {3,S} {7,S} {8,S} {9,S}
3  C 1 0 {1,S} {2,S} {10,S}
4  H 0 0 {1,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {2,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 H 0 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (694934000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1.56, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 130,
    reactant1 = 
"""
O2_(T)
multiplicity 3
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    reactant2 = 
"""
HCO
multiplicity 2
1 C 1 0 {2,D} {3,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
""",
    product1 = 
"""
CHO3
multiplicity 2
1 C 0 0 {2,D} {3,S} {5,S}
2 O 0 2 {1,D}
3 O 0 2 {1,S} {4,S}
4 O 1 2 {3,S}
5 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (291137000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 131,
    reactant1 = 
"""
CH2O
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O 0 2 {2,S} {3,S}
2 O 1 2 {1,S}
3 H 0 0 {1,S}
""",
    product1 = 
"""
CH3O3_1
multiplicity 2
1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 2 {1,S} {3,S}
3 O 0 2 {2,S} {7,S}
4 O 1 2 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (838, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3.6089, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 132,
    reactant1 = 
"""
C2H5
multiplicity 2
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 0 {1,S} {6,S} {7,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {2,S}
""",
    reactant2 = 
"""
C2H4
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 C 0 0 {1,D} {5,S} {6,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
6 H 0 0 {2,S}
""",
    product1 = 
"""
C4H9
multiplicity 2
1  C 0 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 0 {2,S} {4,S} {10,S} {11,S}
4  C 1 0 {3,S} {12,S} {13,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
12 H 0 0 {4,S}
13 H 0 0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.048071, 'cm^3/(mol*s)'),
        n = 2.44,
        Ea = (5.37, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 133,
    reactant1 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O 2 2
""",
    product1 = 
"""
CO2
multiplicity 1
1 C 0 0 {2,D} {3,D}
2 O 0 2 {1,D}
3 O 0 2 {1,D}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1540000000000000.0, 'cm^6/(mol^2*s)'),
            n = 0,
            Ea = (12.56, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 3.0, 'O=C=O': 1.5, 'CC': 3.0, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 134,
    reactant1 = 
"""
CH2O
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    product1 = 
"""
HCO
multiplicity 2
1 C 1 0 {2,D} {3,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.4e+36, 'cm^3/(mol*s)'),
            n = -5.54,
            Ea = (404.58, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 3.0, 'O=C=O': 1.5, 'CC': 3.0, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 135,
    reactant1 = 
"""
CH2O
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    product1 = 
"""
H2
multiplicity 1
1 H 0 0 {2,S}
2 H 0 0 {1,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (3.26e+36, 'cm^3/(mol*s)'),
            n = -5.54,
            Ea = (404.58, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 3.0, 'O=C=O': 1.5, 'CC': 3.0, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 136,
    reactant1 = 
"""
CH2CO
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 C 0 0 {1,D} {5,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 O 0 2 {2,D}
""",
    product1 = 
"""
CH2_(T)
multiplicity 3
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (6570000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (241.03, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 3.0, 'O=C=O': 1.5, 'CC': 3.0, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 137,
    reactant1 = 
"""
HCO
multiplicity 2
1 C 1 0 {2,D} {3,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
""",
    product1 = 
"""
H
multiplicity 2
1 H 1 0
""",
    product2 = 
"""
CO
multiplicity 1
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (449000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (65.93, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 3.0, 'O=C=O': 1.5, 'CC': 3.0, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 138,
    reactant1 = 
"""
CH2_(S)
multiplicity 1
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product1 = 
"""
CH2_(T)
multiplicity 3
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (15100000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (0, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 0.48, 'O=C=O': 1.5, 'CC': 1.44, 'O': 6.5, '[O][O]': 0.4, '[C]=O': 0.75, 'N#N': 0.4, 'C=C': 1.6, 'C#C': 3.2, '[Ar]': 0.24},
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 139,
    reactant1 = 
"""
CH3
multiplicity 2
1 C 1 0 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    product1 = 
"""
CH2_(T)
multiplicity 3
1 C 2 0 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(2.91e+16, 'cm^3/(mol*s)'), n=0, Ea=(379.14, 'kJ/mol'), T0=(1, 'K')),
        efficiencies = {'C': 3.0, 'O=C=O': 1.5, 'CC': 3.0, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 140,
    reactant1 = 
"""
C2H4
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 C 0 0 {1,D} {5,S} {6,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
6 H 0 0 {2,S}
""",
    product1 = 
"""
C2H2
multiplicity 1
1 C 0 0 {2,T} {3,S}
2 C 0 0 {1,T} {4,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
""",
    product2 = 
"""
H2
multiplicity 1
1 H 0 0 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(9.97e+16, 'cm^3/(mol*s)'), n=0, Ea=(299.32, 'kJ/mol'), T0=(1, 'K')),
        efficiencies = {'C': 3.0, 'O=C=O': 1.5, 'CC': 3.0, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 141,
    reactant1 = 
"""
O_(T)
multiplicity 3
1 O 2 2
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O 2 2
""",
    product1 = 
"""
O2_(T)
multiplicity 3
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (54000000000000.0, 'cm^6/(mol^2*s)'),
            n = 0,
            Ea = (-7.48, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 3.0, 'O=C=O': 1.5, 'CC': 3.0, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 142,
    reactant1 = 
"""
O2_(T)
multiplicity 3
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    product1 = 
"""
HO2
multiplicity 2
1 O 0 2 {2,S} {3,S}
2 O 1 2 {1,S}
3 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(2.1e+18, 'cm^6/(mol^2*s)'), n=-0.8, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
        efficiencies = {'C': 3.0, 'O=C=O': 1.5, 'CC': 3.0, 'O': 0.0, '[O][O]': 0.4, 'N#N': 0.67, '[C]=O': 0.75, '[Ar]': 0.29},
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 143,
    reactant1 = 
"""
C2H4
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 C 0 0 {1,D} {5,S} {6,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
6 H 0 0 {2,S}
""",
    product1 = 
"""
C2H3
multiplicity 2
1 C 0 0 {2,D} {3,S} {4,S}
2 C 1 0 {1,D} {5,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(7.4e+17, 'cm^3/(mol*s)'), n=0, Ea=(404.09, 'kJ/mol'), T0=(1, 'K')),
        efficiencies = {'C': 3.0, 'O=C=O': 1.5, 'CC': 3.0, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 144,
    reactant1 = 
"""
H
multiplicity 2
1 H 1 0
""",
    reactant2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    product1 = 
"""
H2
multiplicity 1
1 H 0 0 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.87e+18, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
        efficiencies = {'C': 3.0, 'O=C=O': 1.5, 'CC': 3.0, 'O': 6.5, '[H][H]': 0.0, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 145,
    reactant1 = 
"""
H
multiplicity 2
1 H 1 0
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O 2 2
""",
    product1 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.18e+19, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
        efficiencies = {'C': 3.0, 'O=C=O': 1.5, 'CC': 3.0, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 146,
    reactant1 = 
"""
H
multiplicity 2
1 H 1 0
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    product1 = 
"""
H2O
multiplicity 1
1 O 0 2 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(5.53e+22, 'cm^6/(mol^2*s)'), n=-2, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
        efficiencies = {'C': 3.0, 'O=C=O': 1.5, 'CC': 3.0, 'O': 2.55, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.15},
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 147,
    reactant1 = 
"""
CH3O
multiplicity 2
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 2 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (155000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (56.46, 'kJ/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 3.0, 'O=C=O': 1.5, 'CC': 3.0, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 148,
    reactant1 = 
"""
CH2OH
multiplicity 2
1 C 1 0 {2,S} {3,S} {4,S}
2 O 0 2 {1,S} {5,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C 0 0 {2,D} {3,S} {4,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.26e+16, 'cm^3/(mol*s)'), n=0, Ea=(125.6, 'kJ/mol'), T0=(1, 'K')),
        efficiencies = {'C': 3.0, 'O=C=O': 1.5, 'CC': 3.0, 'O': 6.5, '[O][O]': 0.4, 'N#N': 0.4, '[C]=O': 0.75, '[Ar]': 0.35},
        comment = 'Reaction and kinetics from combustion_core\x0bersion3.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

