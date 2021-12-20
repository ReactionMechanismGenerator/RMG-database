#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dual_Adsorption_vdW/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

# entry(
#     index = 12,
#     label = "COOH* + OH* <=> CO2* + H2O*",
#     degeneracy = 1,
#     kinetics = SurfaceArrhenius(
#         A = (3.398e17, 'm^2/(mol*s)'),
#         n = 0.,
#         Ea = (0., 'kcal/mol'),
#         Tmin = (298, 'K'),
#         Tmax = (2000, 'K'),
#     ),
#     rank = 10,
#     shortDesc = u"""Default""",
#     longDesc = u"""
# Reaction 12 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
# and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/c s200055d

# A factor from paper / surface site density of Cu
# 1.0e13 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 3.398e17 m^2/(mol*s)
# """,
#     metal = "Cu",
# )
