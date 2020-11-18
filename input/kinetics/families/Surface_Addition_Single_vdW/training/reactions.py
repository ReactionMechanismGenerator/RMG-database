#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Addition_Single_vdW/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 11,
    label = "COOH* + X_5 <=> CO2_2* + H*",
    degeneracy = 2,
    kinetics = SurfaceArrhenius(
        A = (8.028e17, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (28.3644741, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 11 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
2.3626e13 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 8.028e17 m^2/(mol*s)
""",
    metal = "Cu",
)

#reverse of 11
# entry(
#     index = 45,
#     label = "CO2_2* + H* <=> COOH* + X_5",
#     degeneracy = 2,
#     kinetics = SurfaceArrhenius(
#         A = (6.25E20, 'm^2/(mol*s)'),
#         n = -0.475,
#         Ea = (117200, 'J/mol'),
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     rank = 10,
#     shortDesc = u"""Default""",
#     longDesc = u"""R45
#     test surface mechanism: based upon Olaf Deutschmann's work:
#     "Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
#     Delgado et al
#     Catalysts, 2015, 5, 871-904""",
# 	  metal = "Ni",
# )

entry(
    index = 17,
    label = "CO2* + H* <=> HCOO* + X_5",
    degeneracy = 2,
    kinetics = SurfaceArrhenius(
        A = (1.243e18, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (20.0626768, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 17 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
3.658e13 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 1.243e18 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 20,
    label = "HCOOH* + H* <=> CH3O2_2* + X_5",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (2.122e19, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (23.9829699, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 20 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
6.244e14 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 2.122e19 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 23,
    label = "CH3O2* + X_5 <=> CH2O* + OH*",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (3.401e17, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (17.0648055, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 23 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
1.001e13 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 3.401e17 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 24,
    label = "CH2O* + H* <=> CH3O_1* + X_5",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (6.167e17, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (5.53453152, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 24 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
1.815e13 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 6.167e17 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 31,
    label = "CH2O_2* + H* <=> CH2OH* + X_5",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (3.234e19, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (18.9096494, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 31 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
9.518e14 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 3.234e19 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 47,
    label = "CH3O_5* + CH2O* <=> H2COOCH3* + X_5",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (2.176e18, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (2.99787124, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 47 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
6.405e13 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 2.176e18 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 48,
    label = "HCOOCH3* + H* <=> H2COOCH3_2* + X_5",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (5.219e16, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (21.6769151, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 48 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
1.536e12 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 5.219e16 m^2/(mol*s)
""",
    metal = "Cu",
)
