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
    kinetics = SurfaceArrhenius(A=(1.973e+22,'cm^2/(mol*s)'), n=0, Ea=(33772,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_Single_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pt111
Original entry: NH3_X + OH_X <=> NH2_X + H2O_X
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
    index = 2,
    label = "HOX + H3NX <=> H2NX + H2OX",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(6.444e+19,'cm^2/(mol*s)'), n=0, Ea=(73000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_Single_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Offermans_Pt111
Original entry: NH3_X + OH_X <=> NH2_X + H2O_X
"Ammonia oxidation on platinum : a density functional theory study of surface reactivity."
Offermans, W. K. (2007). Technische Universiteit Eindhoven. 
https://doi.org/10.6100/IR630067
This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 300K) = 1.6E11(1/s)/2.483E-9(mol/cm^2) = 6.444E19 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

