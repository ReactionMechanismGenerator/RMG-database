#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Abstraction_Single_vdW/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label = "HOX + H3NX <=> H2NX + H2OX",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(6.44e+19,'cm^2/(mol*s)'), n=0, Ea=(73000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_Single_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Offermans_Pt111
Original entry: NH3_X + OH_X <=> NH2_X + H2O_X
"Ammonia oxidation on platinum : a density functional theory study of surface reactivity."
Offermans, W. K. (2007). Technische Universiteit Eindhoven. 
https://doi.org/10.6100/IR630067

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 300K) = 1.6E11(1/s)/2.483E-9(mol/cm^2) = 6.44E19 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 2,
    label = "HOX + H3NX <=> H2NX + H2OX",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(7.27e+20,'cm^2/(mol*s)'), n=0, Ea=(23157.6,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_Single_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Popa_Rh111
Original entry: NH3_X + OH_X <=> NH2_X + H2O_X
Based primarily on 
"Density-functional theory study of NHx oxidation 
and reverse reactions on the Rh (111) surface."
C. Popa, R. A. van Santen, and A. P. J. Jansen.
Phys. Chem. C 2007, 111, 9839– 9852.
https://doi.org/10.1021/jp071072g

This reaction used RMG's surface site density of Rh111 = 2.656E-09(mol/cm^2) to calculate the A factor.
A (at 300K)= 1.93E12(1/s)/2.656E-9(mol/cm^2) = 7.27E20 cm^2/(mol*s)

Ea = 0.24eV = 23157.6J/mol

This is reaction 1a. of TABLE 5.
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 3,
    label = "HOX + H3NX <=> H2NX + H2OX",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(1.97e+22,'cm^2/(mol*s)'), n=0, Ea=(33771.5,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_Single_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Schneider_Pt111
Original entry: NH3_X + OH_X <=> NH2_X + H2O_X
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 4.9E13(1/s)/2.483E-9(mol/cm^2) = 1.97E22 cm^2/(mol*s)
Ea = 0.35eV = 33771.5J/mol

This is R6 in Table S2 and S4
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 4,
    label = "HOX + H3NX <=> H2NX + H2OX",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(3.11e+21,'cm^2/(mol*s)'), n=0, Ea=(80086.7,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_Single_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Schneider_Pt211
Original entry: NH3_X + OH_X <=> NH2_X + H2O_X
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
    index = 5,
    label = "HOX + H3NX <=> H2NX + H2OX",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(1.93e+22,'cm^2/(mol*s)'), n=0, Ea=(44385.4,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_Single_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Schneider_Pd111
Original entry: NH3_X + OH_X <=> NH2_X + H2O_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Pd111
Ea = 0.46eV = 44385.4J/mol

This is reaction (6) in Table S3
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 6,
    label = "HOX + H3NX <=> H2NX + H2OX",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(1.82e+22,'cm^2/(mol*s)'), n=0, Ea=(70437.7,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_Single_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Schneider_Pd211
Original entry: NH3_X + OH_X <=> NH2_X + H2O_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Pd211

Ea = 0.73eV = 70437.7J/mol

This is reaction (6) in Table S2
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 7,
    label = "HOX + H3NX <=> H2NX + H2OX",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(1.84e+22,'cm^2/(mol*s)'), n=0, Ea=(68507.9,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_Single_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Schneider_Rh111
Original entry: NH3_X + OH_X <=> NH2_X + H2O_X
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
    index = 8,
    label = "HOX + H3NX <=> H2NX + H2OX",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(1.74e+21,'cm^2/(mol*s)'), n=0, Ea=(91665.5,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_Single_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Schneider_Rh211
Original entry: NH3_X + OH_X <=> NH2_X + H2O_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Rh211

Ea = 0.95eV = 91665.5J/mol

This is reaction (6) in Table S2
""",
    metal = "Rh",
    facet = "211",
)

