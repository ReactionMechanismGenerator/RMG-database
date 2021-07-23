#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_Single/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "NO + X <=> NO_X",
    degeneracy = 1,
    kinetics = StickingCoefficient(
        A = 0.85,
        n = 0,
        Ea = (0, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 11,
    shortDesc = u"""NO Adsorption""",
    longDesc = u"""
    Detailed surface reaction mechanism in a three-way catalyst
    Chatterjee, Deutschmann, Warnatz et al.
    doi: 10.1039/b101968f

    This is R48""",
    metal = "Pt",
)
entry(
    index = 2,
    label = "NO_X <=> NO + X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.41e+16,'1/s'), n=0, Ea=(154800,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_Single""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Kraehnert_Pt111
Original entry: NO_X <=> NO + X
"Kinetics of ammonia oxidation over Pt foil studied in a micro-structured quartz-reactor"
Kraehnert et al.(2008) 
Chemical Engineering Journal,137(2), 361-375
https://doi.org/10.1016/j.cej.2007.05.005

A = k/exp(-Ea/RT) = 1.24(1/s)/exp(-154800(J/mol)/8.314(J/mol/K)/658K) = 2.41E16 (1/s)

Table 3, R4
""",
    metal = "Pt",
    facet = "111",
)

