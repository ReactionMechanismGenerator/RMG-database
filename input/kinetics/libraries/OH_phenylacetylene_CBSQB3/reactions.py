#!/usr/bin/env python
# encoding: utf-8

name = "OH_phenylacetylene_CBSQB3"
shortDesc = u""
longDesc = u"""
Isomerizations calculated with CBS-QB3. OH+phenylacetylene and phenyl+ketene entrances fitted to match 2014 Goulay and
2004 Lin experiments.
"""
entry(
    index = 1,
    label = "phenyl + ketene <=> ic2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2364, 'cm^3/(mol*s)'),
        n = 2.565,
        Ea = (0.552, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2,
    label = "phenyl + ketene <=> i20",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (19210, 'cm^3/(mol*s)'),
        n = 2.549,
        Ea = (0.743, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 3,
    label = "OH + phenylacetylene <=> i1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.744e+06, 'cm^3/(mol*s)'),
        n = 1.886,
        Ea = (-2.895, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 4,
    label = "OH + phenylacetylene <=> ic1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (111000, 'cm^3/(mol*s)'),
        n = 2.135,
        Ea = (-0.967, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 5,
    label = "i5 <=> i2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.502e+11, 's^-1'), n=0.754, Ea=(55.452, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 6,
    label = "i1 <=> i11",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.292e+08, 's^-1'), n=1.29, Ea=(47.708, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 7,
    label = "i1 <=> i4_9",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.181, 's^-1'), n=3.889, Ea=(26.006, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 8,
    label = "i1 <=> i2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(33630, 's^-1'), n=1.988, Ea=(38.093, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 9,
    label = "i4_9 <=> i5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(99500, 's^-1'), n=2.125, Ea=(41.444, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 10,
    label = "i5 <=> i11",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1450, 's^-1'), n=2.44, Ea=(29.47, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 11,
    label = "p3 + H <=> i5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.595e+08, 'cm^3/(mol*s)'),
        n = 1.566,
        Ea = (4.155, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 12,
    label = "p3 + H <=> i4_9",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.179e+08, 'cm^3/(mol*s)'),
        n = 1.544,
        Ea = (3.763, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 13,
    label = "i4_9 <=> i6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1405e+11, 's^-1'), n=0.213, Ea=(30.11, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 14,
    label = "p3 + H <=> i11",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2959, 'cm^3/(mol*s)'),
        n = 2.968,
        Ea = (13.101, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 15,
    label = "p2 + H <=> i6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.878e+07, 'cm^3/(mol*s)'),
        n = 1.697,
        Ea = (5.96, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 16,
    label = "ic1 <=> ic2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.757e-06, 's^-1'), n=5.242, Ea=(15.739, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 17,
    label = "phenyl + hocch <=> ic1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (285.3, 'cm^3/(mol*s)'),
        n = 3.079,
        Ea = (-0.295, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 18,
    label = "H + p1 <=> i1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.164e+09, 'cm^3/(mol*s)'),
        n = 1.529,
        Ea = (4.393, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc =
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 19,
    label = "i4_9 <=> i20",
    degeneracy = 1,
    kinetics = Arrhenius(A=(89.7, 's^-1'), n=3.07, Ea=(38.56, 'kcal/mol'), T0=(1, 'K')),
    longDesc =
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 20,
    label = "benzyl + CO <=> i20",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (73810, 'cm^3/(mol*s)'),
        n = 2.309,
        Ea = (10.738, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 21,
    label = "i20 <=> i21",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.725e+10, 's^-1'), n=0.547, Ea=(34.586, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 22,
    label = "ic2 <=> i21",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.831e+11, 's^-1'), n=0.359, Ea=(33.014, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

