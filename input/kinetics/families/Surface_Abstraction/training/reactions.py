#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Abstraction/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "CH2X_1 + HOX_3 <=> CH3X_4 + OX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1.39e+17, 'm^2/(mol*s)'),
        n = 0.101,
        Ea = (19000, 'J/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Deutschmann Ni""",
    longDesc = 
u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R24
""",
)

entry(
    index = 1,
    label = "CHX_1 + HOX_3 <=> CH2X_4 + OX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (4.4e+18, 'm^2/(mol*s)'),
        n = 0.101,
        Ea = (42400, 'J/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = 
u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R26
""",
)

entry(
    index = 2,
    label = "HOX_3 + CX_1 <=> OX_5 + CHX_4 ",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (2.43e+17, 'm^2/(mol*s)'),
        n = -0.312,
        Ea = (118900, 'J/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = 
u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R28
""",
)

