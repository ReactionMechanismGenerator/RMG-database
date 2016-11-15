#!/usr/bin/env python
# encoding: utf-8

name = "2012_Kislov_Phenyl_Propene_w_new_pathway"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "C6H5 + C3H6 <=> i1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (214.5, 'cm^3/(mol*s)'),
        n = 3.05,
        Ea = (0.83, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
From 2012 Kislov
""",
)

entry(
    index = 2,
    label = "C6H5 + C3H6 <=> i2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (32.79, 'cm^3/(mol*s)'),
        n = 3.085,
        Ea = (1.881, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
From 2012 Kislov
""",
)

entry(
    index = 3,
    label = "C6H5 + C3H6 <=> CH3CHCH + C6H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.209, 'cm^3/(mol*s)'),
        n = 3.709,
        Ea = (6.35, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
From 2012 Kislov
""",
)

entry(
    index = 4,
    label = "C6H5 + C3H6 <=> CH3CCH2 + C6H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.949, 'cm^3/(mol*s)'),
        n = 3.696,
        Ea = (4.575, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
From 2012 Kislov
""",
)

entry(
    index = 5,
    label = "C6H5 + C3H6 <=> CH2CHCH2 + C6H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.533, 'cm^3/(mol*s)'),
        n = 3.646,
        Ea = (1.897, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
From 2012 Kislov
""",
)

entry(
    index = 6,
    label = "i2 <=> p4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.848e+10, 's^-1'),
        n = 0.848,
        Ea = (33.958, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
From 2012 Kislov
""",
)

entry(
    index = 7,
    label = "i2 <=> p1 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.603e+12, 's^-1'),
        n = 0.523,
        Ea = (29.345, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
From 2012 Kislov
""",
)

entry(
    index = 8,
    label = "i2 <=> i3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.399e+11, 's^-1'),
        n = 0.121,
        Ea = (15.859, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
From 2012 Kislov
""",
)

entry(
    index = 9,
    label = "i2 <=> i8",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.815e+11, 's^-1'),
        n = 0.121,
        Ea = (32.19, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
From 2012 Kislov
""",
)

entry(
    index = 10,
    label = "i2 <=> i9",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.899e+11, 's^-1'),
        n = 0.486,
        Ea = (31.961, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
From 2012 Kislov
""",
)

entry(
    index = 11,
    label = "i2 <=> i10",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.307e+10, 's^-1'),
        n = 0.713,
        Ea = (42.834, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
From 2012 Kislov
""",
)

entry(
    index = 12,
    label = "i1 <=> i3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.528e+11, 's^-1'),
        n = 0.199,
        Ea = (16.505, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
From 2012 Kislov
""",
)

entry(
    index = 13,
    label = "i1 <=> p2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.935e+11, 's^-1'),
        n = 0.894,
        Ea = (34.903, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
From 2012 Kislov
""",
)

entry(
    index = 14,
    label = "i1 <=> p3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.424e+10, 's^-1'),
        n = 0.914,
        Ea = (34.551, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
From 2012 Kislov
""",
)

entry(
    index = 15,
    label = "i1 <=> i4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.312e+11, 's^-1'),
        n = 0.608,
        Ea = (39.998, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
From 2012 Kislov
""",
)

entry(
    index = 16,
    label = "i1 <=> i7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.148e+11, 's^-1'),
        n = 0.537,
        Ea = (37.159, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
From 2012 Kislov
""",
)

entry(
    index = 17,
    label = "i1 <=> i6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.224e+09, 's^-1'),
        n = 0.668,
        Ea = (40.429, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
From 2012 Kislov
""",
)

entry(
    index = 18,
    label = "i8 <=> p7 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.662e+12, 's^-1'),
        n = 0.757,
        Ea = (48.395, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
From 2012 Kislov
""",
)

entry(
    index = 19,
    label = "i8 <=> p8 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.732e+10, 's^-1'),
        n = 0.856,
        Ea = (26.921, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
From 2012 Kislov
""",
)

entry(
    index = 20,
    label = "i9 <=> p4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.13e+13, 's^-1'),
        n = -0.029,
        Ea = (41.271, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
From 2012 Kislov
""",
)

entry(
    index = 21,
    label = "i10 <=> p4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.715e+10, 's^-1'),
        n = 0.858,
        Ea = (25.452, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
From 2012 Kislov
""",
)

entry(
    index = 22,
    label = "i4 <=> i5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.31e+11, 's^-1'),
        n = 0.001,
        Ea = (17.806, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
From 2012 Kislov
""",
)

entry(
    index = 23,
    label = "i4 <=> p2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.447e+10, 's^-1'),
        n = 0.874,
        Ea = (36.168, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
From 2012 Kislov
""",
)

entry(
    index = 24,
    label = "i5 <=> p5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.417e+10, 's^-1'),
        n = 0.841,
        Ea = (23.191, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
From 2012 Kislov
""",
)

entry(
    index = 25,
    label = "i5 <=> p9 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.124e+12, 's^-1'),
        n = 0.476,
        Ea = (47.412, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
From 2012 Kislov
""",
)

entry(
    index = 26,
    label = "i7 <=> p1 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.59e+12, 's^-1'),
        n = 0.733,
        Ea = (35.918, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
From 2012 Kislov
""",
)

entry(
    index = 27,
    label = "i7 <=> p3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.88e+11, 's^-1'),
        n = 0.972,
        Ea = (40.036, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
From 2012 Kislov
""",
)

entry(
    index = 28,
    label = "i6 <=> p2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.539e+11, 's^-1'),
        n = 0.868,
        Ea = (26.827, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
From 2012 Kislov
""",
)
