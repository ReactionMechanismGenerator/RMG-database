#!/usr/bin/env python
# encoding: utf-8

name = "Sulfur/Sendt"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    reactant1 = 
"""
H2S
multiplicity 1
1 S 0 2 {2,S} {3,S}
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
SH
multiplicity 2
1 S 1 2 {2,S}
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
        A = (34900000.0, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (0.9, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\Sendt.\nReactions from Sendt et al. Proc. Comb. Inst. 2002\nNot including reactions 1, 19, 20, 21',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Reactions from Sendt et al. Proc. Comb. Inst. 2002
Not including reactions 1, 19, 20, 21
""",
)

entry(
    index = 2,
    reactant1 = 
"""
H2S
multiplicity 1
1 S 0 2 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    reactant2 = 
"""
S
multiplicity 1
1 S 2 2
""",
    product1 = 
"""
SH
multiplicity 2
1 S 1 2 {2,S}
2 H 0 0 {1,S}
""",
    product2 = 
"""
SH
multiplicity 2
1 S 1 2 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (83200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7.38, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\Sendt.',
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
S
multiplicity 1
1 S 2 2
""",
    reactant2 = 
"""
H2
multiplicity 1
1 H 0 0 {2,S}
2 H 0 0 {1,S}
""",
    product1 = 
"""
SH
multiplicity 2
1 S 1 2 {2,S}
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
        A = (135000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (19.29, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\Sendt.',
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
S
multiplicity 1
1 S 2 2
""",
    reactant2 = 
"""
SH
multiplicity 2
1 S 1 2 {2,S}
2 H 0 0 {1,S}
""",
    product1 = 
"""
S2
multiplicity 1
1 S 0 2 {2,D}
2 S 0 2 {1,D}
""",
    product2 = 
"""
H
multiplicity 2
1 H 1 0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (27000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\Sendt.',
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
H
multiplicity 2
1 H 1 0
""",
    reactant2 = 
"""
HSS
multiplicity 2
1 S 0 2 {2,S} {3,S}
2 S 1 2 {1,S}
3 H 0 0 {1,S}
""",
    product1 = 
"""
SH
multiplicity 2
1 S 1 2 {2,S}
2 H 0 0 {1,S}
""",
    product2 = 
"""
SH
multiplicity 2
1 S 1 2 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (11000000000000.0, 'cm^3/(mol*s)'),
        n = 0.353,
        Ea = (0.21, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\Sendt.\nUsing unadjusted singlet surface calculation for this one (see paper)',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Using unadjusted singlet surface calculation for this one (see paper)
""",
)

entry(
    index = 6,
    reactant1 = 
"""
SH
multiplicity 2
1 S 1 2 {2,S}
2 H 0 0 {1,S}
""",
    reactant2 = 
"""
HSS
multiplicity 2
1 S 0 2 {2,S} {3,S}
2 S 1 2 {1,S}
3 H 0 0 {1,S}
""",
    product1 = 
"""
H2S
multiplicity 1
1 S 0 2 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product2 = 
"""
S2
multiplicity 1
1 S 0 2 {2,D}
2 S 0 2 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6270, 'cm^3/(mol*s)'),
        n = 3.05,
        Ea = (-1.1, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\Sendt.',
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
H
multiplicity 2
1 H 1 0
""",
    reactant2 = 
"""
HSS
multiplicity 2
1 S 0 2 {2,S} {3,S}
2 S 1 2 {1,S}
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
S2
multiplicity 1
1 S 0 2 {2,D}
2 S 0 2 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (123000000.0, 'cm^3/(mol*s)'),
        n = 1.653,
        Ea = (-1.1, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\Sendt.',
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
H
multiplicity 2
1 H 1 0
""",
    reactant2 = 
"""
HSS
multiplicity 2
1 S 0 2 {2,S} {3,S}
2 S 1 2 {1,S}
3 H 0 0 {1,S}
""",
    product1 = 
"""
H2S
multiplicity 1
1 S 0 2 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product2 = 
"""
S
multiplicity 1
1 S 2 2
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (44100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6.33, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\Sendt.',
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
S
multiplicity 1
1 S 2 2
""",
    reactant2 = 
"""
HSS
multiplicity 2
1 S 0 2 {2,S} {3,S}
2 S 1 2 {1,S}
3 H 0 0 {1,S}
""",
    product1 = 
"""
S2
multiplicity 1
1 S 0 2 {2,D}
2 S 0 2 {1,D}
""",
    product2 = 
"""
SH
multiplicity 2
1 S 1 2 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4170000.0, 'cm^3/(mol*s)'),
        n = 2.2,
        Ea = (-0.6, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\Sendt.',
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
HSS
multiplicity 2
1 S 0 2 {2,S} {3,S}
2 S 1 2 {1,S}
3 H 0 0 {1,S}
""",
    reactant2 = 
"""
HSS
multiplicity 2
1 S 0 2 {2,S} {3,S}
2 S 1 2 {1,S}
3 H 0 0 {1,S}
""",
    product1 = 
"""
H2S2
multiplicity 1
1 S 0 2 {2,S} {3,S}
2 S 0 2 {1,S} {4,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
""",
    product2 = 
"""
S2
multiplicity 1
1 S 0 2 {2,D}
2 S 0 2 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.56, 'cm^3/(mol*s)'),
        n = 3.37,
        Ea = (-1.67, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\Sendt.',
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
H2S2
multiplicity 1
1 S 0 2 {2,S} {3,S}
2 S 0 2 {1,S} {4,S}
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
HSS
multiplicity 2
1 S 0 2 {2,S} {3,S}
2 S 1 2 {1,S}
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
        A = (49900000.0, 'cm^3/(mol*s)'),
        n = 1.933,
        Ea = (-1.41, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\Sendt.',
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
H2S2
multiplicity 1
1 S 0 2 {2,S} {3,S}
2 S 0 2 {1,S} {4,S}
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
H2S
multiplicity 1
1 S 0 2 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product2 = 
"""
SH
multiplicity 2
1 S 1 2 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (366000000.0, 'cm^3/(mol*s)'),
        n = 1.724,
        Ea = (0.47, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\Sendt.',
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
H2S2
multiplicity 1
1 S 0 2 {2,S} {3,S}
2 S 0 2 {1,S} {4,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
""",
    reactant2 = 
"""
SH
multiplicity 2
1 S 1 2 {2,S}
2 H 0 0 {1,S}
""",
    product1 = 
"""
H2S
multiplicity 1
1 S 0 2 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product2 = 
"""
HSS
multiplicity 2
1 S 0 2 {2,S} {3,S}
2 S 1 2 {1,S}
3 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6400, 'cm^3/(mol*s)'),
        n = 2.98,
        Ea = (-1.48, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\Sendt.',
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
H2S2
multiplicity 1
1 S 0 2 {2,S} {3,S}
2 S 0 2 {1,S} {4,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
""",
    reactant2 = 
"""
S
multiplicity 1
1 S 2 2
""",
    product1 = 
"""
HSS
multiplicity 2
1 S 0 2 {2,S} {3,S}
2 S 1 2 {1,S}
3 H 0 0 {1,S}
""",
    product2 = 
"""
SH
multiplicity 2
1 S 1 2 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2850000.0, 'cm^3/(mol*s)'),
        n = 2.31,
        Ea = (1.2, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\Sendt.',
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
H
multiplicity 2
1 H 1 0
""",
    reactant2 = 
"""
S2
multiplicity 1
1 S 0 2 {2,D}
2 S 0 2 {1,D}
""",
    product1 = 
"""
HSS
multiplicity 2
1 S 0 2 {2,S} {3,S}
2 S 1 2 {1,S}
3 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.15e+25, 'cm^6/(mol^2*s)'),
            n = -2.84,
            Ea = (1.66, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'S': 1.1, '[He]': 1.39, 'N#N': 1.0, '[Ar]': 0.88},
        comment = 'Reaction and kinetics from Sulfur\\Sendt.\nPressure dependent reactions from Sendt et al. Proc. Comb. Inst. 2002\nNot including reactions 1, 19, 20, 21',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Pressure dependent reactions from Sendt et al. Proc. Comb. Inst. 2002
Not including reactions 1, 19, 20, 21
""",
)

entry(
    index = 16,
    reactant1 = 
"""
H2S2
multiplicity 1
1 S 0 2 {2,S} {3,S}
2 S 0 2 {1,S} {4,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
""",
    product1 = 
"""
SH
multiplicity 2
1 S 1 2 {2,S}
2 H 0 0 {1,S}
""",
    product2 = 
"""
SH
multiplicity 2
1 S 1 2 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (693000000000000.0, 'cm^3/(mol*s)'),
            n = 1,
            Ea = (57.03, 'kcal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'S': 1.1, '[He]': 1.39, 'N#N': 1.0, '[Ar]': 0.88},
        comment = 'Reaction and kinetics from Sulfur\\Sendt.\nA-factor could also be 2.31E14',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
A-factor could also be 2.31E14
""",
)

