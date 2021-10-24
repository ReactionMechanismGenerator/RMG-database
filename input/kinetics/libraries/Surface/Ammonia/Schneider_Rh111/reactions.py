#!/usr/bin/env python
# encoding: utf-8

name = "Schneider_Rh111"
shortDesc = u""
longDesc = u"""
Primarily based on:
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029
"""

entry(
    index = 1,
    label = "O2 + X + X <=> O_X + O_X",
    kinetics = StickingCoefficient(
        A = 0.9975,
        n = 0,
        Ea = (0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""O2 Surface_Adsorption_Dissociative""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

Scitcking coefficient from Schneider_Pt111

This is reaction (1) in Table S3
""",
	metal = "Rh",
    facet = "111",
)

entry(
    index = 2,
    label = "NH3 + X <=> NH3_X",
    kinetics = StickingCoefficient(
        A = 1,
        n = 0,
        Ea = (0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

Scitcking coefficient from Schneider_Pt111

This is reaction (2) in Table S3
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 3,
    label = "NH3_X +O_X <=> NH2_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (1.96E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (86841, 'J/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Rh111

Ea = 0.9eV = 86841J/mol

This is reaction (3) in Table S3
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 4,
    label = "NH2_X +O_X <=> NH_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (2.07E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (106139, 'J/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Rh111

Ea = 1.1eV = 106139J/mol

This is reaction (4) in Table S3
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 5,
    label = "NH_X + O_X <=> N_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (2.94E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (142805.2, 'J/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Rh111

Ea = 1.48eV = 142805.2J/mol

This is reaction (5) in Table S3
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 6,
    label = "NH3_X + OH_X <=> NH2_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (1.84E22, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (68507.9, 'J/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_Single_vdW""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Rh111

Ea = 0.71eV = 68507.9J/mol

This is reaction (6) in Table S3
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 7,
    label = "NH2_X + OH_X <=> NH_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (5.65E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (25087.4, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Rh111

Ea = 0.26eV = 25087.4J/mol

This is reaction (7) in Table S3
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 8,
    label = "NH_X + OH_X <=> N_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (2.22E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (63683.4, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Rh111

Ea = 0.66eV = 63683.4J/mol

This is reaction (8) in Table S3
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 9,
    label = "OH_X + OH_X <=> O_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (1.17E21, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (0, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Rh111

This is reaction (9) in Table S3
""",
    metal = "Rh",
    facet = "111",
)

#Endothermic, Deutschmann's paper: A=4.5E8, n=0, Ea=41800J/mol
# entry(
#     index = 10,
#     label = "H2O_X <=> H2O + X",
#     kinetics = SurfaceArrhenius(
#         A = (5.9E15, '1/s'), 
#         n = 0.0,
#         Ea = (27017.2, 'J/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_vdW""",
#     longDesc = u"""
# "DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
# Hanyu Ma, and William F.Schneider
# Journal of Catalysis 383 (2020) 322–330
# https://doi.org/10.1016/j.jcat.2020.01.029
#
# A factor from Schneider_Pt111 library
#
# Ea = 0.28eV = 27017.2J/mol
#
# This is reaction (10) in Table S3
# """,
#       metal = "Rh",
#       facet = "111",
# )

entry(
    index = 11,
    label = "N_X + N_X <=> N2 + X + X",
    kinetics = SurfaceArrhenius(
        A = (3.46E21, 'cm^2/(mol*s)'),
        n = 0.0,
        Ea = (246049.5, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""N2 Surface_Adsorption_Dissociative""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Rh111
A factor revise from 3.46E21 to 3.46E22 base on the ammonia model
Ea = 2.55eV = 246049.5J/mol

This is reaction (11) in Table S3
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 12,
    label = "N_X + O_X <=> NO_X + X",
    kinetics = SurfaceArrhenius(
        A = (3.13E22, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (226751.5, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Nitrogen/51""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Rh111
A factor revise from 3.13E21 to 3.13E22 base on the ammonia model

Ea = 2.35eV = 226751.5J/mol

This is reaction (12) in Table S3
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 13,
    label = "NO_X <=> NO + X",
    kinetics = SurfaceArrhenius(
        A = (6.55E15, '1/s'),  
        n = 0.0,
        Ea = (241225, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor calculated from the equation proposed by Campbell1 et al. (2013)

Ea = 2.5eV = 241225J/mol

This is reaction (13) in Table S3
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 14,
    label = "N_X + NO_X <=> N2O_X + X",
    kinetics = SurfaceArrhenius(
        A = (1.62E22, 'cm^2/(mol*s)'),   
        n = 0.0,
        Ea = (206488.6, 'J/mol'), 
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Rh111
A factor revise from 1.62E21 to 1.62E22 base on the ammonia model

Ea = 2.14eV = 206488.6J/mol

This is reaction (14) in Table S3
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 15,
    label = "N2O_X <=> N2O + X",
    kinetics = SurfaceArrhenius(
        A = (1.4E16, '1/s'),
        n = 0.0,
        Ea = (32806.6, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Double/Surface_Adsorption_vdW""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library

Ea = 0.34eV = 32806.6J/mol

This is reaction (15) in Table S3
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 16,
    label = "NH3_X + X <=> NH2_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (3.57E20, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (100349.6, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Rh111

Ea = 1.04eV = 100349.6J/mol

This is reaction (1) in Table S5
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 17,
    label = "NH2_X + X <=> NH_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (3.23E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (83946.3, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Rh111

Ea = 0.87eV = 83946.3J/mol

This is reaction (2) in Table S5
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 18,
    label = "NH_X + X <=> N_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (3.4E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (98419.8, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Rh111

Ea = 1.02eV = 98419.8J/mol

This is reaction (3) in Table S5
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 19,
    label = "H_X + O_X <=> OH_X + X",
    kinetics = SurfaceArrhenius(
        A = (1.2E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (61753.6, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Rh111

Ea = 0.64eV = 61753.6J/mol

This is reaction (4) in Table S5
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 20,
    label = "H_X + OH_X <=> H2O_X + X",
    kinetics = SurfaceArrhenius(
        A = (1.91E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (63683.4, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Rh111

Ea = 0.66eV = 63683.4J/mol

This is reaction (5) in Table S5
""",
    metal = "Rh",
    facet = "111",
)
