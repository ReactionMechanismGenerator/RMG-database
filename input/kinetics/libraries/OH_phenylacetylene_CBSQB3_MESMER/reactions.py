#!/usr/bin/env python
# encoding: utf-8

name = "OH_phenylacetylene_CBSQB3_MESMER"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "OH + phenylacetylene <=> i1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.658e+12, 'cm^3/(mol*s)'),
        n = 0.497,
        Ea = (0.666, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2,
    label = "OH + phenylacetylene <=> ic1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.541e+12, 'cm^3/(mol*s)'),
        n = 0.512,
        Ea = (3.163, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 3,
    label = "phenyl + ketene <=> ic2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.669e+08, 'cm^3/(mol*s)'),
        n = 1.387,
        Ea = (4.755, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 4,
    label = "phenyl + ketene <=> i20",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.852e+09, 'cm^3/(mol*s)'),
        n = 1.414,
        Ea = (4.793, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

