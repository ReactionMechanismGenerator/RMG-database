#!/usr/bin/env python
# encoding: utf-8

name = "New_Phenyl_Propene_Pathway"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "i1 <=> inew",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.153e+12, 's^-1'),
        n = 0.0,
        Ea = (29.608, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'CBS-QB3',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
CBS-QB3
""",
)

entry(
    index = 2,
    label = "inew <=> i4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.978e+11, 's^-1'),
        n = 0.0,
        Ea = (7.048, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'CBS-QB3',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
CBS-QB3
""",
)

entry(
    index = 3,
    label = "i4 <=> C2H4 + Benzyl",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.717e+13, 's^-1'),
        n = 0.0,
        Ea = (22.905, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'CBS-QB3',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
CBS-QB3
""",
)

