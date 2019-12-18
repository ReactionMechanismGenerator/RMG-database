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
#     # degeneracy = 4,
#     kinetics = SurfaceArrhenius(
#         A = (1.0e13, 'm^2/(mol*s)'),
#         n = 0.,
#         Ea = (0., 'kcal/mol'),
#         Tmin = (298, 'K'),
#         Tmax = (2000, 'K'),
#     ),
#     rank = 1,
#     shortDesc = u"""Default""",
#     longDesc = u"""
# Reaction 12 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
# and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d
# """
# )