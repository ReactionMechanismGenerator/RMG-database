#!/usr/bin/env python
# encoding: utf-8

name = "Schneider_Pt111"
shortDesc = u""
longDesc = u"""
This library is built to import training reactions, based on:
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251
"""

#Commet out since sitcking coefficient ≈ 1
# entry(
#     index = 1,
#     label = "O2 + X + X <=> O_X + O_X",
#     kinetics = StickingCoefficient(
#         A = 0.9975,
#         n = 0,
#         Ea = (0, 'J/mol'),
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""O2 Surface_Adsorption_Dissociative""",
#     longDesc = u"""
# "Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
# DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
# https://doi.org/10.1021/acscatal.8b04251

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = ((1.8E3 /pa) / s) * (2.483E-9 mol/cm2) * sqrt(2 * pi * 32 g/mol * molar gas constant * 298 kelvin)
# """,
# 	metal = "Pt",
#     facet = "111",
# )

#Commet out since sitcking coefficient = 1
# entry(
#     index = 2,
#     label = "NH3 + X <=> NH3_X",
#     kinetics = StickingCoefficient(
#         A = 1,
#         n = 0,
#         Ea = (0, 'J/mol'),
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_vdW""",
#     longDesc = u"""
# "Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
# DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
# https://doi.org/10.1021/acscatal.8b04251
# 
# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = ((2.5E3 /pa) / s) * (2.483E-9 mol/cm2) * sqrt(2 * pi * 17 g/mol * molar gas constant * 298 kelvin)
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
    index = 3,
    label = "NH3_X +O_X <=> NH2_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (1.007E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (67543, 'J/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 5.2E12(1/s)/2.483E-9(mol/cm^2) = 1.007E21 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 4,
    label = "NH2_X +O_X <=> NH_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (2.215E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (78157, 'J/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction""",
    longDesc = u"""
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 5.5E12(1/s)/2.483E-9(mol/cm^2) = 2.215E21 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 5,
    label = "NH_X + O_X <=> N_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (3.141E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (154380, 'J/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction""",
    longDesc = u"""
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 7.8E12(1/s)/2.483E-9(mol/cm^2) = 3.141E21 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 6,
    label = "NH3_X + OH_X <=> NH2_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (1.973E22, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (33772, 'J/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_Single_vdW""",
    longDesc = u"""
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 4.9E13(1/s)/2.483E-9(mol/cm^2) = 1.973E22 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 7,
    label = "NH2_X + OH_X <=> NH_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (6.041E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (965, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1.5E13(1/s)/2.483E-9(mol/cm^2) = 6.041E21 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 8,
    label = "NH_X + OH_X <=> N_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (2.376E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (39561, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 5.9E12(1/s)/2.483E-9(mol/cm^2) = 2.376E21 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 9,
    label = "OH_X + OH_X <=> O_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (1.248E21, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (0, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R95""",
    longDesc = u"""
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 3.1E12(1/s)/2.483E-9(mol/cm^2) = 1.248E21 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

#Commet out since sitcking coefficient ≈ 1
# entry(
#     index = 10,
#     label = "H2O + X <=> H2O_X",
#     kinetics = StickingCoefficient(
#         A = 9.97E-1, 
#         n = 0.0,
#         Ea = (0, 'J/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption""",
#     longDesc = u"""
# "Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
# DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
# https://doi.org/10.1021/acscatal.8b04251

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = ((2.4e3 /Pa) / s) * (2.4e-9 mol/cm2) * sqrt(2 * pi * 18 g/mol * molar gas constant * 298 kelvin)
# """,
#       metal = "Pt",
#       facet = "111",
# )

entry(
    index = 11,
    label = "N2 + X + X <=> N_X + N_X",
    kinetics = StickingCoefficient(
        A = 3.525E-5,  
        n = 0.0,
        Ea = (244119, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""N2 Surface_Adsorption_Dissociative""",
    longDesc = u"""
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = ((6.8E-2 /Pa) / s) * (2.483E-9 mol/cm2) * sqrt(2 * pi * 28 g/mol * molar gas constant * 298 kelvin)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 12,
    label = "N_X + O_X <=> NO_X + X",
    kinetics = SurfaceArrhenius(
        A = (3.343E21, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (213243, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Nitrogen/51""",
    longDesc = u"""
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 8.3E12(1/s)/2.483E-9(mol/cm^2) = 3.343E21 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

#Commet out since sitcking coefficient = 1
# entry(
#     index = 13,
#     label = "NO + X <=> NO_X",
#     kinetics = StickingCoefficient(
#         A = 1,  
#         n = 0.0,
#         Ea = (0, 'J/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_Single""",
#     longDesc = u"""
# "Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
# DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
# https://doi.org/10.1021/acscatal.8b04251

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = ((1.9E3 /Pa) / s) * (2.483E-9 mol/cm2) * sqrt(2 * pi * 30 g/mol * molar gas constant * 298 kelvin)
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
    index = 14,
    label = "N_X + NO_X <=> N2O_X + X",
    kinetics = SurfaceArrhenius(
        A = (1.732E21, 'cm^2/(mol*s)'),   
        n = 0.0,
        Ea = (164998, 'J/mol'), 
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 4.3E12(1/s)/2.483E-9(mol/cm^2) = 1.732E21 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

#Commet out since sitcking coefficient = 1
# entry(
#     index = 15,
#     label = "N2O + X <=> N2O_X",
#     kinetics = StickingCoefficient(
#         A = 1,  
#         n = 0.0,
#         Ea = (0, 'J/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_Double/Surface_Adsorption_vdW""",
#     longDesc = u"""
# "Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
# DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
# https://doi.org/10.1021/acscatal.8b04251
# 
#This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = ((1.6E3 /Pa) / s) * (2.483E-9 mol/cm2) * sqrt(2 * pi * 44 g/mol * molar gas constant * 298 kelvin)
# """,
#     metal = "Pt",
#     facet = "111",
# )