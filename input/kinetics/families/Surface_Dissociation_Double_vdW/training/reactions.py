#!/usr/bin/env python
# encoding: utf-8

# name = "Surface_Dissociation_Double_vdW/training"
# shortDesc = u"Reaction kinetics used to generate rate rules"
# longDesc = u"""
# Put kinetic parameters for specific reactions in this file to use as a
# training set for generating rate rules to populate this kinetics family.
# """

# entry(
#     index = 9,
#     label = "CO* + O* <=> CO2* + X_4",
#     degeneracy = 2,
#     kinetics = SurfaceArrhenius(
#         A = (4.060e16, 'm^2/(mol*s)'),
#         n = 0.,
#         Ea = (0.65, 'eV/molecule'),
#         Tmin = (298, 'K'),
#         Tmax = (2000, 'K'),
#     ),
#     rank = 10,
#     shortDesc = u"""Default""",
#     longDesc = u"""
# Reaction 9 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
# and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

# A factor from paper / surface site density of Cu
# 1.195e12 1/s / 2.943e‐5 mol/m^2 = 4.060e16 m^2/(mol*s)
# Erxn= -1.12 eV
# """,
#     metal = "Cu",
# )

# # duplicate of 9
# # entry(
# #     index = 42,
# #     label = "CO2* + X_4 <=> CO* + O*",
# #     kinetics = SurfaceArrhenius(
# #         A = (4.64E19, 'm^2/(mol*s)'),
# #         n = -1.0,
# #         Ea = (89300.0, 'J/mol'),
# #         Tmin = (200, 'K'),
# #         Tmax = (3000, 'K'),
# #     ),
# #     rank = 10,
# #     shortDesc = u"""Default""",
# #     longDesc = u"""R42
# #     test surface mechanism: based upon Olaf Deutschmann's work:
# #     "Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
# #     Delgado et al
# #     Catalysts, 2015, 5, 871-904""",
# # 	  metal = "Ni",
# # )

# entry(
#     index = 35,
#     label = "HCOOH* + X_4 <=> HCOH* + O*",
#     degeneracy = 1,
#     kinetics = SurfaceArrhenius(
#         A = (1.641e16, 'm^2/(mol*s)'),
#         n = 0.,
#         Ea = (2.50, 'eV/molecule'),
#         Tmin = (298, 'K'),
#         Tmax = (2000, 'K'),
#     ),
#     rank = 10,
#     shortDesc = u"""Default""",
#     longDesc = u"""
# Reaction 35 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
# and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

# A factor from paper / surface site density of Cu
# 4.828e11 1/s / 2.943e‐5 mol/m^2 = 1.641e16 m^2/(mol*s)
# Erxn = 2.04 eV
# """,
#     metal = "Cu",
# )
