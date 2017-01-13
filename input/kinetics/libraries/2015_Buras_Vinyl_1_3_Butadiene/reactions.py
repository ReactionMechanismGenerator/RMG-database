#!/usr/bin/env python
# encoding: utf-8

name = "2015_Buras_Vinyl_1_3_Butadiene"
shortDesc = u"TST rates from CCSD(T)-F12a/cc-pVTZ-F12 calculations on Vinyl + 1,3-Butadiene PES"
longDesc = u"""
Taken from:

Buras, Z. J.; Dames, E. E.; Merchant, S. S.; Liu, G.; Elsamra, R. M. I.; Green, W. H.,
Kinetics and Products of Vinyl + 1,3-Butadiene, a Potential Route to Benzene. J. Phys. Chem. A 2015, 119, 7325-7338.
"""
entry(
    index = 1,
    label = "C2H3 + C4H6 <=> C6H9",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (39130, 'cm^3/(mol*s)'),
        n = 2.404,
        Ea = (0.42, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2,
    label = "C6H9 <=> C6H8 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.29e+06, 's^-1'), n=2.017, Ea=(40.664, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 3,
    label = "C6H9 <=> c6-C6H9",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.041e+08, 's^-1'), n=0.7, Ea=(20.246, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 4,
    label = "C6H9 <=> c5-C6H9",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.249e+08, 's^-1'), n=0.846, Ea=(19.298, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 5,
    label = "c5-C6H9 <=> H + c5-C6H8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.972e+07, 's^-1'), n=1.802, Ea=(32.304, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 6,
    label = "c6-C6H9 <=> H + C6H8-c6-13",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.487e+08, 's^-1'), n=1.395, Ea=(33.132, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 7,
    label = "c6-C6H9 <=> H + C6H8-c6-14",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.097e+09, 's^-1'), n=1.299, Ea=(33.394, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 8,
    label = "c5-C6H9 <=> c5-C6H9-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.265e-07, 's^-1'), n=5.639, Ea=(24.541, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 9,
    label = "c5-C6H9 <=> c5-C6H9-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.537e-16, 's^-1'), n=8.138, Ea=(14.583, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 10,
    label = "c5-C6H9-2 <=> C5H6 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.961e+11, 's^-1'), n=0.717, Ea=(38.962, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 11,
    label = "c5-C6H9-3 <=> c5-C6H9-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.239e-08, 's^-1'), n=6.224, Ea=(24.481, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 12,
    label = "C2H3 + C4H6 <=> C2H4 + nC4H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0003437, 'cm^3/(mol*s)'),
        n = 4.732,
        Ea = (6.579, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 13,
    label = "C2H3 + C4H6 <=> C2H4 + iC4H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000621, 'cm^3/(mol*s)'),
        n = 4.814,
        Ea = (4.902, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

