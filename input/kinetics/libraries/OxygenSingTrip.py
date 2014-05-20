#!/usr/bin/env python
# encoding: utf-8

name = "OxygenSingTrip"
shortDesc = u""
longDesc = u"""

"""
entry(
    index        = 1,
    reactant1 = 
"""
O2_(S)
multiplicity 1
1 O U0 L2 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    reversible = False,
    kinetics = Arrhenius(
        A = (0.00023, 's^-1'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from OxygenSingTrip.',
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
O2_(S)
multiplicity 1
1 O U0 L2 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    reversible = False,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4.05, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
        efficiencies = {'[O][O]': 5.43, 'O=C=O': 4.29},
        comment = 'Reaction and kinetics from OxygenSingTrip.',
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
O2_(S)
multiplicity 1
1 O U0 L2 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(3000000.0, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
        efficiencies = {'c1ccccc1': 1.067, 'O': 1.783, '[H][H]': 1.0, '[O][O]': 0.34, 'N#N': 0.028, '[C]=O': 14.0, '[Ar]': 0.00166},
        comment = 'Reaction and kinetics from OxygenSingTrip.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

