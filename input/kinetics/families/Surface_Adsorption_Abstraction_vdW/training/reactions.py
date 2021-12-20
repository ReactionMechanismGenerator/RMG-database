#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_Abstraction_vdW/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

# entry(
#     index = 43,
#     label = "HCOOH* + HCO* <=> CH3O2* + CO*",
#     kinetics = SurfaceArrhenius(
#         A = (1.814e16, 'm^2/(mol*s)'),
#         n = 0,
#         Ea = (0.42, 'eV/molecule'),
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     rank = 10,
#     shortDesc = u"""Default""",
#     longDesc = u"""
# Reaction 43 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
# and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

# A factor from paper / surface site density of Cu
# 5.34e11 1/s / 2.943e‐5 mol/m^2 = 1.814e16 m^2/(mol*s)
# Erxn = -0.68 eV
# """,
#     metal = "Cu",
# )

# entry(
#     index = 44,
#     label = "CH2O* + HCO* <=> CH3O* + CO*",
#     kinetics = SurfaceArrhenius(
#         A = (3.398e17, 'm^2/(mol*s)'),
#         n = 0,
#         Ea = (0.0, 'kcal/mol'),
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     rank = 10,
#     shortDesc = u"""Default""",
#     longDesc = u"""
# Reaction 44 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
# and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

# A factor from paper / surface site density of Cu
# 1.0e13 1/s / 2.943e‐5 mol/m^2 = 3.398e17 m^2/(mol*s)
# Erxn = -1.81 eV
# """,
#     metal = "Cu",
# )
