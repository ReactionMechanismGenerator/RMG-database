#!/usr/bin/env python
# encoding: utf-8

name = "Schneider_Pt211"
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
#         A = 1,
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

# This reaction used RMG's surface site density of Pt211 = 2.634E-9(mol/cm^2) to calculate the A factor.
# A = ((1.8E3 /pa) / s) * (2.634E-9 mol/cm2) * sqrt(2 * pi * 32 g/mol * molar gas constant * 298 kelvin)
# 
# This is R1 in Table S2 and S4
# """,
# 	  metal = "Pt",
#     facet = "211",
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
# This reaction used RMG's surface site density of Pt211 = 2.634E-9(mol/cm^2) to calculate the A factor.
# A = ((2.5E3 /pa) / s) * (2.634E-9 mol/cm2) * sqrt(2 * pi * 17 g/mol * molar gas constant * 298 kelvin)
#  
# This is R2 in Table S2 and S4
# """,
#     metal = "Pt",
#     facet = "211",
# )

entry(
    index = 3,
    label = "NH3_X +O_X <=> NH2_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (1.56E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (55964.2, 'J/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt211 = 2.634E-9(mol/cm^2) to calculate the A factor.
A = 4.1E12(1/s)/2.634E-9(mol/cm^2) = 1.56E21 cm^2/(mol*s)
Ea = 0.58eV = 55964.2J/mol

This is R3 in Table S2 and S4
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 4,
    label = "NH2_X +O_X <=> NH_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (1.78E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (139910.5, 'J/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction""",
    longDesc = u"""
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt211 = 2.634E-9(mol/cm^2) to calculate the A factor.
A = 4.7E12(1/s)/2.634E-9(mol/cm^2) = 1.78E21 cm^2/(mol*s)
Ea = 1.45eV = 139910.5J/mol

This is R4 in Table S2 and S4
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 5,
    label = "NH_X + O_X <=> N_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (1.29E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (45350.3, 'J/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction""",
    longDesc = u"""
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt211 = 2.634E-9(mol/cm^2) to calculate the A factor.
A = 3.4E12(1/s)/2.634E-9(mol/cm^2) = 1.29E21 cm^2/(mol*s)
Ea = 0.47eV = 45350.3J/mol

This is R5 in Table S2 and S4
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 6,
    label = "NH3_X + OH_X <=> NH2_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (3.11E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (80086.7, 'J/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_Single_vdW""",
    longDesc = u"""
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt211 = 2.634E-9(mol/cm^2) to calculate the A factor.
A = 8.2E12(1/s)/2.634E-9(mol/cm^2) = 3.11E21 cm^2/(mol*s)
Ea = 0.83eV = 80086.7J/mol

This is R6 in Table S2 and S4
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 7,
    label = "NH2_X + OH_X <=> NH_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (1.48E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (76227.1, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt211 = 2.634E-9(mol/cm^2) to calculate the A factor.
A = 3.9E12(1/s)/2.634E-9(mol/cm^2) = 1.48E21 cm^2/(mol*s)
Ea = 0.79eV = 76227.1J/mol

This is R7 in Table S2 and S4
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 8,
    label = "NH_X + OH_X <=> N_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (2.01E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (81051.6, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt211 = 2.634E-9(mol/cm^2) to calculate the A factor.
A = 5.3E12(1/s)/2.634E-9(mol/cm^2) = 2.01E21 cm^2/(mol*s)
Ea = 0.84eV = 81051.6J/mol

This is R8 in Table S2 and S4
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 9,
    label = "OH_X + OH_X <=> O_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (1.59E21, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (81051.6, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Reverse R95""",
    longDesc = u"""
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt211 = 2.634E-9(mol/cm^2) to calculate the A factor.
A = 4.2E12(1/s)/2.634E-9(mol/cm^2) = 1.59E21 cm^2/(mol*s)
Ea = 0.84eV = 81051.6J/mol

This is R9 in Table S2 and S4
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 10,
    label = "H2O_X <=> H2O + X",
    kinetics = SurfaceArrhenius(
        A = (1.40E24, '1/s'), 
        n = 0.0,
        Ea = (24122.5, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption""",
    longDesc = u"""
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt211 = 2.634E-9(mol/cm^2) to calculate the A factor.
A = 3.7E15(1/s)/2.634E-9(mol/cm^2) = 1.40E24 cm^2/(mol*s)
Ea = 0.25eV = 24122.5J/mol

This is R10 in Table S2 and S4
""",
      metal = "Pt",
      facet = "211",
)

entry(
    index = 11,
    label = "N_X + N_X <=> N2 + X + X",
    kinetics = SurfaceArrhenius(
        A = (2.01E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (113858.2, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""N2 Surface_Adsorption_Dissociative""",
    longDesc = u"""
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt211 = 2.634E-9(mol/cm^2) to calculate the A factor.
A = 5.3E12(1/s)/2.634E-9(mol/cm^2) = 2.01E21 cm^2/(mol*s)
Ea = 1.18eV = 113858.2J/mol

This is R11 in Table S2 and S4
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 12,
    label = "N_X + O_X <=> NO_X + X",
    kinetics = SurfaceArrhenius(
        A = (1.44E21, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (140875.4, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Nitrogen/51""",
    longDesc = u"""
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt211 = 2.634E-9(mol/cm^2) to calculate the A factor.
A = 3.8E12(1/s)/2.634E-9(mol/cm^2) = 1.44E21 cm^2/(mol*s)
Ea = 1.46eV = 140875.4J/mol

This is R12 in Table S2 and S4
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 13,
    label = "NO_X <=> NO + X",
    kinetics = SurfaceArrhenius(
        A = (4.94E25, '1/s'),   
        n = 0.0,
        Ea = (224821.7, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt211 = 2.634E-9(mol/cm^2) to calculate the A factor.
A = 1.3E17(1/s)/2.634E-9(mol/cm^2) = 4.94E25 cm^2/(mol*s)
Ea = 2.33eV = 224821.7J/mol

This is R13 in Table S2 and S4
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 14,
    label = "N_X + NO_X <=> N2O_X + X",
    kinetics = SurfaceArrhenius(
        A = (2.32E21, 'cm^2/(mol*s)'),   
        n = 0.0,
        Ea = (156313.8, 'J/mol'), 
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt211 = 2.634E-9(mol/cm^2) to calculate the A factor.
A = 6.1E12(1/s)/2.634E-9(mol/cm^2) = 2.32E21 cm^2/(mol*s)
Ea = 1.62eV = 156313.8J/mol

This is R14 in Table S2 and S4
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 15,
    label = "N2O_X <=> N2O + X",
    kinetics = SurfaceArrhenius(
        A = (5.69E25, '1/s'), 
        n = 0.0,
        Ea = (9649, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Double/Surface_Adsorption_vdW""",
    longDesc = u"""
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt211 = 2.634E-9(mol/cm^2) to calculate the A factor.
A = 1.5E17(1/s)/2.634E-9(mol/cm^2) = 5.69E25 cm^2/(mol*s)
Ea = 0.1eV = 9649J/mol

This is R15 in Table S2 and S4
""",
    metal = "Pt",
    facet = "211",
)
