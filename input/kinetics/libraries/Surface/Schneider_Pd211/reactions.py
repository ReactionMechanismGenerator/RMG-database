#!/usr/bin/env python
# encoding: utf-8

name = "Schneider_Pd211"
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
        A = 1,
        n = 0,
        Ea = (28947, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""O2 Surface_Adsorption_Dissociative""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

Ea = 0.3eV = 28947J/mol
This is reaction (1) in Table S2
""",
    metal = "Pd",
    facet = "211",
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

This is reaction (2) in Table S2
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 3,
    label = "NH3_X +O_X <=> NH2_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (2.44E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (39560.9, 'J/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd211 = 2.688E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 0.41eV = 39560.9J/mol

This is reaction (3) in Table S2
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 4,
    label = "NH2_X +O_X <=> NH_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (2.44E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (104209.2, 'J/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd211 = 2.688E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 1.08eV = 104209.2J/mol

This is reaction (4) in Table S2
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 5,
    label = "NH_X + O_X <=> N_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (2.44E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (23157.6, 'J/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd211 = 2.688E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 0.24eV = 23157.6J/mol

This is reaction (5) in Table S2
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 6,
    label = "NH3_X + OH_X <=> NH2_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (2.44E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (70437.7, 'J/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_Single_vdW""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd211 = 2.688E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 0.73eV = 70437.7J/mol

This is reaction (6) in Table S2
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 7,
    label = "NH2_X + OH_X <=> NH_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (2.44E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (73332.4, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd211 = 2.688E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 0.76eV = 73332.4J/mol

This is reaction (7) in Table S2
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 8,
    label = "NH_X + OH_X <=> N_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (2.44E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (41490.7, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd211 = 2.688E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 0.43eV = 41490.7J/mol

This is reaction (8) in Table S2
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 9,
    label = "OH_X + OH_X <=> O_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (2.44E21, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (71402.6, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd211 = 2.688E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 0.74eV = 71402.6J/mol

This is reaction (9) in Table S2
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 10,
    label = "H2O + X <=> H2O_X",
    kinetics = StickingCoefficient(
        A = 1,
        n = 0.0,
        Ea = (30876.8, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029
Ea = 0.32eV = 30876.8J/mol

This is reaction (10) in Table S2
""",
      metal = "Pd",
      facet = "211",
)

entry(
    index = 11,
    label = "N2 + X + X <=> N_X + N_X",
    kinetics = StickingCoefficient(
        A = 1,
        n = 0.0,
        Ea = (119647.6, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""N2 Surface_Adsorption_Dissociative""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

Ea = 1.24eV = 119647.6J/mol

This is reaction (11) in Table S2
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 12,
    label = "N_X + O_X <=> NO_X + X",
    kinetics = SurfaceArrhenius(
        A = (2.44E21, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (82981.4, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Nitrogen/51""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd211 = 2.688E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 0.86eV = 82981.4J/mol

This is reaction (12) in Table S2
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 13,
    label = "NO_X <=> NO + X",
    kinetics = SurfaceArrhenius(
        A = (6.55E14, '1/s'),  
        n = 0.0,
        Ea = (225786.6, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

Ea = 2.34eV = 225786.6J/mol

This is reaction (13) in Table S2
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 14,
    label = "N_X + NO_X <=> N2O_X + X",
    kinetics = SurfaceArrhenius(
        A = (2.44E21, 'cm^2/(mol*s)'),   
        n = 0.0,
        Ea = (191050.2, 'J/mol'), 
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd211 = 2.688E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 1.98eV = 191050.2J/mol

This is reaction (14) in Table S2
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 15,
    label = "N2O_X <=> N2O + X",
    kinetics = SurfaceArrhenius(
        A = (1.69E13, '1/s'), 
        n = 0.0,
        Ea = (36666.2, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Double/Surface_Adsorption_vdW""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

Ea = 0.38eV = 36666.2J/mol

This is reaction (15) in Table S2
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 16,
    label = "NH3_X + X <=> NH2_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (2.06E23, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (97454.9, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd211 = 2.688E-9(mol/cm^2) to calculate the A factor.
Using the method proposed by Campbell et al. to calculate A actor.
Ea = 1.01eV = 97454.9/mol
This is reaction (1) in Table S4
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 17,
    label = "NH2_X + X <=> NH_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (2.23E23, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (152454.2, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd211 = 2.688E-9(mol/cm^2) to calculate the A factor.
Using the method proposed by Campbell et al. to calculate A actor.
Ea = 1.58eV = 152454.2J/mol

This is reaction (2) in Table S4
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 18,
    label = "NH_X + X <=> N_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (2.23E23, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (118682.7, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd211 = 2.688E-9(mol/cm^2) to calculate the A factor.
Using the method proposed by Campbell et al. to calculate A actor.
Ea = 1.23eV = 118682.7J/mol

This is reaction (3) in Table S4
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 19,
    label = "H_X + O_X <=> OH_X + X",
    kinetics = SurfaceArrhenius(
        A = (2.44E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (123507.2, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd211 = 2.688E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 1.28eV = 123507.2J/mol

This is reaction (4) in Table S4
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 20,
    label = "H_X + OH_X <=> H2O_X + X",
    kinetics = SurfaceArrhenius(
        A = (2.44E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (91665.5, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd211 = 2.688E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 0.95eV = 91665.5J/mol

This is reaction (5) in Table S4
""",
    metal = "Pd",
    facet = "211",
)