#!/usr/bin/env python
# encoding: utf-8

name = "Schneider_Rh211"
shortDesc = u""
longDesc = u"""
Primarily based on:
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029
"""

entry(
    index = 1.0,
    label = "O2 + X + X <=> O_X + O_X",
    kinetics = StickingCoefficient(
        A = 1,
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

This is reaction (1) in Table S2
""",
	metal = "Rh",
    facet = "211",
)

entry(
    index = 2,
    label = "NH3 + X <=> NH3_X",
    kinetics = StickingCoefficient(
        A = 1.0,
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

This is reaction (2) in Table S2
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 3,
    label = "NH3_X +O_X <=> NH2_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (2.33E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (62718.5, 'J/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Rh211 = 2.817E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 0.65eV = 62718.5J/mol

This is reaction (3) in Table S2
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 4,
    label = "NH2_X +O_X <=> NH_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (2.33E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (143770.1, 'J/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Rh211 = 2.817E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 1.49eV = 143770.1J/mol

This is reaction (4) in Table S2
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 5,
    label = "NH_X + O_X <=> N_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (2.33E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (60788.7, 'J/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Rh211 = 2.817E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 0.63eV = 60788.7J/mol

This is reaction (5) in Table S2
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 6,
    label = "NH3_X + OH_X <=> NH2_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (2.33E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (91665.5, 'J/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_Single_vdW""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Rh211 = 2.817E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 0.95eV = 91665.5J/mol

This is reaction (6) in Table S2
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 7,
    label = "NH2_X + OH_X <=> NH_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (2.33E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (97454.9, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Rh211 = 2.817E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 1.01eV = 97454.9J/mol

This is reaction (7) in Table S2
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 8,
    label = "NH_X + OH_X <=> N_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (2.33E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (85876.1, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Rh211 = 2.817E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 0.89eV = 85876.1J/mol

This is reaction (8) in Table S2
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 9,
    label = "OH_X + OH_X <=> O_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (2.33E21, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (92630.4, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Rh211 = 2.817E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 0.96eV = 92630.4J/mol

This is reaction (9) in Table S2
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 10,
    label = "H2O + X <=> H2O_X",
    kinetics = StickingCoefficient(
        A = 1.0,
        n = 0.0,
        Ea = (43420.5, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

Ea = 0.45eV = 43420.5J/mol

This is reaction (10) in Table S2
""",
      metal = "Rh",
      facet = "211",
)

entry(
    index = 11,
    label = "N2 + X + X <=> N_X + N_X",
    kinetics = StickingCoefficient(
        A = 1.0,
        n = 0.0,
        Ea = (169822.4, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""N2 Surface_Adsorption_Dissociative""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

Ea = 1.76eV = 169822.4J/mol

This is reaction (11) in Table S2
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 12,
    label = "N_X + O_X <=> NO_X + X",
    kinetics = SurfaceArrhenius(
        A = (2.33E21, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (166927.7, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Nitrogen/51""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Rh211 = 2.817E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 1.73eV = 166927.7J/mol

This is reaction (12) in Table S2
""",
    metal = "Rh",
    facet = "211",
)


entry(
    index = 13,
    label = "NO_X <=> NO + X",
    kinetics = SurfaceArrhenius(
        A = (6.55E14, '1/s'),   
        n = 0.0,
        Ea = (270172, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

Ea = 2.8eV = 270172J/mol

This is reaction (13) in Table S2
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 14,
    label = "N_X + NO_X <=> N2O_X + X",
    kinetics = SurfaceArrhenius(
        A = (2.33E21, 'cm^2/(mol*s)'),   
        n = 0.0,
        Ea = (211313.1, 'J/mol'), 
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Rh211 = 2.817E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 2.19eV = 211313.1J/mol

This is reaction (14) in Table S2
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 15,
    label = "N2O_X <=> N2O + X",
    kinetics = SurfaceArrhenius(
        A = (1.69E13, '1/s'),   
        n = 0.0,
        Ea = (54999.3, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Double/Surface_Adsorption_vdW""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

Ea = 0.57eV = 54999.3J/mol

This is reaction (15) in Table S2
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 16,
    label = "NH3_X + X <=> NH2_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (1.96E23, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (88770.8, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Rh211 = 2.817E-9(mol/cm^2) to calculate the A factor.
Using the method proposed by Campbell et al. to calculate A actor.
Ea = 0.92eV = 88770.8J/mol

This is reaction (1) in Table S4
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 17,
    label = "NH2_X + X <=> NH_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (2.19E23, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (117717.8, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Rh211 = 2.817E-9(mol/cm^2) to calculate the A factor.
Using the method proposed by Campbell et al. to calculate A actor.
Ea = 1.22eV = 117717.8J/mol

This is reaction (2) in Table S4
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 18,
    label = "NH_X + X <=> N_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (2.19E23, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (88770.8, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Rh211 = 2.817E-9(mol/cm^2) to calculate the A factor.
Using the method proposed by Campbell et al. to calculate A actor.
Ea = 0.92eV = 88770.8J/mol

This is reaction (3) in Table S4
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 19,
    label = "H_X + O_X <=> OH_X + X",
    kinetics = SurfaceArrhenius(
        A = (2.33E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (85876.1, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Rh211 = 2.817E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 0.89eV = 85876.1J/mol

This is reaction (4) in Table S4
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 20,
    label = "H_X + OH_X <=> H2O_X + X",
    kinetics = SurfaceArrhenius(
        A = (2.33E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (96490, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Rh211 = 2.817E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 1eV = 96490J/mol

This is reaction (5) in Table S4
""",
    metal = "Rh",
    facet = "211",
)
