#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "CH2X_3 + HX_5 <=> CH3X_1 + Ni_4",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(
        A = (3.09e+19, 'm^2/(mol*s)'),
        n = -0.087,
        Ea = (57200, 'J/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = 
u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R16
""",
)

entry(
    index = 1,
    label = "CHX_3 + HX_5 <=> CH2X_1 + Ni_4",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(
        A = (9.77e+20, 'm^2/(mol*s)'),
        n = -0.087,
        Ea = (81000, 'J/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = 
u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R18
""",
)

entry(
    index = 2,
    label = "CX_3 + HX_5 <=> CHX_1 + Ni_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1.7e+20, 'm^2/(mol*s)'),
        n = -0.5,
        Ea = (157900, 'J/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = 
u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R20
""",
)

entry(
    index = 3,
    label = "HOX_1 + Ni_4 <=> OX_3 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (2.25e+16, 'm^2/(mol*s)'),
        n = 0.188,
        Ea = (29600, 'J/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = 
u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R32
""",
)

entry(
    index = 4,
    label = "HOCXO_1 + Ni_4 <=> OCX_3 + HOX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1.46e+20, 'm^2/(mol*s)'),
        n = -0.213,
        Ea = (54300, 'J/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = 
u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R4
""",
)

entry(
    index = 5,
    label = "CXHO_1 + Ni_4 <=> OCX_3 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (3.71e+17, 'm^2/(mol*s)'),
        n = 0,
        Ea = (0, 'J/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = 
u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R8
""",
)

