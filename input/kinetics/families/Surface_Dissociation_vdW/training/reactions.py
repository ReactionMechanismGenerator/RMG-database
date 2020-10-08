#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_vdW/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 7,
    label = "NH3_X + X_4 <=> NH2_X + H*",
    degeneracy = 3,
    kinetics = SurfaceArrhenius(
        A = (5.723e22, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (78.99, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
    Micro-kinetic modeling of NH3 decomposition on Ni and its application to solid oxide fuel cells
    Deutschmann et al
    doi: 10.1016/j.ces.2011.07.007

    This is R7
""",
    metal = "Ni",
)

entry(
    index = 12,
    label = "CH4* + X_4 <=> CH3* + H*",
    degeneracy = 4,
    kinetics = SurfaceArrhenius(
        A = (1.54E17,'m^2/(mol*s)'),
        n = 0.087,
        Ea = (55800, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""R13
    test surface mechanism: based upon Olaf Deutschmann's work:
    "Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
    Delgado et al
    Catalysts, 2015, 5, 871-904""",
	metal = "Ni",
)

entry(
    index = 13,
    label = "COOH* + H* <=> HCOOH* + X_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (2.308e18, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (16.8342, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 13 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
6.793e13 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 2.308e18 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 14,
    label = "H2O* + X_4 <=> OH* + H*",
    degeneracy = 2,
    kinetics = SurfaceArrhenius(
        A = (4.879e15, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (4.84271508, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 14 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
1.436e11 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 4.879e15 m^2/(mol*s)
""",
    metal = "Cu",
)

#duplicate of 14
# entry(
#     index = 29,
#     label = "H2O* + X_4 <=> OH* + H*",
#     kinetics = SurfaceArrhenius(
#         A = (3.67E17, 'm^2/(mol*s)'),
#         n = -0.086,
#         Ea = (92.9, 'kJ/mol'),
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     rank = 10,
#     shortDesc = u"""Default""",
#     longDesc = u"""R29
#     test surface mechanism: based upon Olaf Deutschmann's work:
#     "Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
#     Delgado et al
#     Catalysts, 2015, 5, 871-904""",
# 	metal = "Ni",
# )

entry(
    index = 19,
    label = "HCOO* + H* <=> HCOOH_1* + X_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (4.424e18, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (20.9850987, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 19 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
1.302e14 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 4.424e18 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 25,
    label = "CH3O* + H* <=> CH3OH_2* + X_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (4.349e22, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (10.8384576, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 25 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
1.28e18 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 4.349e22 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 30,
    label = "HCO* + H* <=> CH2O* + X_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (1.932e17, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (10.8384576, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 30 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
5.685e12 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 1.932e17 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 33,
    label = "CH2OH* + H* <=> CH3OH_1* + X_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (2.783e17, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (37.5886933, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 33 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
8.189e12 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 2.783e17 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 34,
    label = "HCOOH_2* + X_4 <=> HCO* + OH_2*",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (1.781e17, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (37.5886933, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 34 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
5.242e12 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 1.781e17 m^2/(mol*s)
""",
    metal = "Cu",
)
