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
        A = (4.555e-01, 's^-1'),
        n = 3.436,
        Ea = (23.613, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'G3(CC,MP2)//B3LYP/6-311G**',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
G3(CC,MP2)//B3LYP/6-311G** method of Mebel
""",
)

entry(
    index = 2,
    label = "inew <=> i4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.419e+02, 's^-1'),
        n = 2.452,
        Ea = (3.561, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'G3(CC,MP2)//B3LYP/6-311G**',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
G3(CC,MP2)//B3LYP/6-311G** method of Mebel
""",
)

entry(
    index = 3,
    label = "i4 <=> C2H4 + Benzyl",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.836e+09, 's^-1'),
        n = 1.093,
        Ea = (22.805, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'G3(CC,MP2)//B3LYP/6-311G**',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
G3(CC,MP2)//B3LYP/6-311G** method of Mebel
""",
)

