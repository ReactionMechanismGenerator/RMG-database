#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Abstraction_vdW/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

# reverse of 2, below
# entry(
#     index = 1,
#     label = "H2O* + O* <=> OH_2* + OH_4*",
#     degeneracy = 2,
#     kinetics = SurfaceArrhenius(
#         A = (8.14e20, 'm^2/(mol*s)'),
#         n = -0.274,
#         Ea = (218400, 'J/mol'),
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     rank = 10,
#     shortDesc = u"""Default""",
#     longDesc = u"""R34
#     test surface mechanism: based upon Olaf Deutschmann's work:
#     "Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
#     Delgado et al
#     Catalysts, 2015, 5, 871-904""",
# 	  metal = "Ni",
# )

# reverse of 1, above
entry(
    index = 2,
    label = "OH_2* + OH_4* <=> H2O* + O*",
    degeneracy = 2,
    kinetics = SurfaceArrhenius(
        A = (5.691e16, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (14.0669343, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 16 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
1.675e12 1/s / 2.943e‐5 mol/m^2 = 5.691e16 m^2/(mol*s)
""", #Ting-Chen: I think the unit of the A factor in the paper is 1/s rather than m^4/(mol^2 * s)
    metal = "Cu",
)

entry(
    index = 3,
    label = "CH4* + O* <=> CH3* + OH_4*",
    degeneracy = 4,
    kinetics = SurfaceArrhenius(
        A = (5.62e20, 'm^2/(mol*s)'),
        n = -0.101,
        Ea = (92700, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""R21
    test surface mechanism: based upon Olaf Deutschmann's work:
    "Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
    Delgado et al
    Catalysts, 2015, 5, 871-904""",
	metal = "Ni",
)

entry(
    index = 4,
    label = "OH_2* + HCO* <=> H2O* + CO*",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (3.261e17, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (6.9181644, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 40 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
9.597e12 1/s / 2.943e‐5 mol/m^2 = 3.261e17 m^2/(mol*s)
""", #Ting-Chen: I think the unit of the A factor in the paper is 1/s rather than m^4/(mol^2 * s)
    metal = "Cu",
)

entry(
    index = 5,
    label = "HCOO_1* + HCO* <=> HCOOH* + CO*",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (7.475E18, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (13.8363288, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 41 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
2.2e14 1/s / 2.943e‐5 mol/m^2 = 7.475e18 m^2/(mol*s)
""", #Ting-Chen: I think the unit of the A factor in the paper is 1/s rather than m^4/(mol^2 * s)
    metal = "Cu",
)

entry(
    index = 6,
    label = "CH3O* + HCO* <=> CH3OH* + CO*",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (6.572e16, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (8.76300824, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 45 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
1.934e12 1/s / 2.943e‐5 mol/m^2 = 6.572e16 m^2/(mol*s)
""", #Ting-Chen: I think the unit of the A factor in the paper is 1/s rather than m^4/(mol^2 * s)
    metal = "Cu",
)

entry(
    index = 7,
    label = "CH3O* + HCOO_5* <=> HCOOCH3* + O*",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (2.356e16, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (28.5950795, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 46 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
6.934e11 1/s / 2.943e‐5 mol/m^2 = 2.356e16 m^2/(mol*s)
""", #Ting-Chen: I think the unit of the A factor in the paper is 1/s rather than m^4/(mol^2 * s)
    metal = "Cu",
)


entry(
    index = 8,
    label = "O* + H3NX <=> H2NX + OH_4*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(1.01e21,'cm^2/(mol*s)'), n=0, Ea=(67543,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pt111
Original entry: NH3_X +O_X <=> NH2_X + OH_X
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 5.2E12(1/s)/2.483E-9(mol/cm^2) = 1.01E21 cm^2/(mol*s)
Ea = 0.7eV = 67543J/mol

This is R3 in Table S2 and S4
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 9,
    label = "H2NX-2 + OH_2* <=> H2O* + HNX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.04e21,'cm^2/(mol*s)'), n=0, Ea=(964.9,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pt111
Original entry: NH2_X + OH_X <=> NH_X + H2O_X
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1.5E13(1/s)/2.483E-9(mol/cm^2) = 6.04E21 cm^2/(mol*s)
Ea = 0.01eV = 964.9J/mol

This is R7 in Table S2 and S4
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 10,
    label = "HNX-2 + OH_2* <=> H2O* + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.38e21,'cm^2/(mol*s)'), n=0, Ea=(39560.9,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pt111
Original entry: NH_X + OH_X <=> N_X + H2O_X
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 5.9E12(1/s)/2.483E-9(mol/cm^2) = 2.38E21 cm^2/(mol*s)
Ea = 0.41eV = 39560.9J/mol

This is R8 in Table S2 and S4
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 11,
    label = "OH_2* + OH_4* <=> H2O* + O*",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.25e21,'cm^2/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pt111
Original entry: OH_X + OH_X <=> O_X + H2O_X
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 3.1E12(1/s)/2.483E-9(mol/cm^2) = 1.25E21 cm^2/(mol*s)

This is R9 in Table S2 and S4
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 12,
    label = "O* + H3NX <=> H2NX + OH_4*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(4.833e20,'cm^2/(mol*s)'), n=0, Ea=(42000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Offermans_Pt111
Original entry: NH3_X +O_X <=> NH2_X + OH_X
"Ammonia oxidation on platinum : a density functional theory study of surface reactivity."
Offermans, W. K. (2007). Technische Universiteit Eindhoven. 
https://doi.org/10.6100/IR630067

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 300K) = 1.2E12(1/s)/2.483E-9(mol/cm^2) = 4.833E20 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 13,
    label = "H2NX-2 + OH_2* <=> H2O* + HNX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.369e21,'cm^2/(mol*s)'), n=0, Ea=(22000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Offermans_Pt111
Original entry: NH2_X + OH_X <=> NH_X + H2O_X
"Ammonia oxidation on platinum : a density functional theory study of surface reactivity."
Offermans, W. K. (2007). Technische Universiteit Eindhoven. 
https://doi.org/10.6100/IR630067

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 300K) = 3.4E12(1/s)/2.483E-9(mol/cm^2) = 1.369E21 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 14,
    label = "HNX-2 + OH_2* <=> H2O* + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.054e20,'cm^2/(mol*s)'), n=0, Ea=(35000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Offermans_Pt111
Original entry: NH_X + OH_X <=> N_X + H2O_X
"Ammonia oxidation on platinum : a density functional theory study of surface reactivity."
Offermans, W. K. (2007). Technische Universiteit Eindhoven. 
https://doi.org/10.6100/IR630067

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 300K) = 5.1E11(1/s)/2.483E-9(mol/cm^2) = 2.054E20 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 15,
    label = "O* + H3NX <=> H2NX + OH_4*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(2.47e21,'cm^2/(mol*s)'), n=0, Ea=(86841,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Rh111
Original entry: NH3_X +O_X <=> NH2_X + OH_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Rh111 = 2.656E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 0.9eV = 86841J/mol

This is reaction (3) in Table S3
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 16,
    label = "H2NX-2 + OH_2* <=> H2O* + HNX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.47e21,'cm^2/(mol*s)'), n=0, Ea=(25087.4,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Rh111
Original entry: NH2_X + OH_X <=> NH_X + H2O_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Rh111 = 2.656E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 0.26eV = 25087.4J/mol

This is reaction (7) in Table S3
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 17,
    label = "HNX-2 + OH_2* <=> H2O* + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.47e21,'cm^2/(mol*s)'), n=0, Ea=(39561,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Rh111
Original entry: NH_X + OH_X <=> N_X + H2O_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Rh111 = 2.656E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 0.66eV = 63683.4J/mol

This is reaction (8) in Table S3
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 18,
    label = "OH_2* + OH_4* <=> H2O* + O*",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.47e21,'cm^2/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Rh111
Original entry: OH_X + OH_X <=> O_X + H2O_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Rh111 = 2.656E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1

This is reaction (9) in Table S3
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 19,
    label = "O* + H3NX <=> H2NX + OH_4*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(2.44e21,'cm^2/(mol*s)'), n=0, Ea=(39560.9,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pd211
Original entry: NH3_X +O_X <=> NH2_X + OH_X
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
    index = 20,
    label = "H2NX-2 + OH_2* <=> H2O* + HNX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.44e21,'cm^2/(mol*s)'), n=0, Ea=(73332.4,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pd211
Original entry: NH2_X + OH_X <=> NH_X + H2O_X
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
    index = 21,
    label = "HNX-2 + OH_2* <=> H2O* + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.44e21,'cm^2/(mol*s)'), n=0, Ea=(41490.7,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pd211
Original entry: NH_X + OH_X <=> N_X + H2O_X
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
    index = 22,
    label = "OH_2* + OH_4* <=> H2O* + O*",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.44e21,'cm^2/(mol*s)'), n=0, Ea=(71402.6,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pd211
Original entry: OH_X + OH_X <=> O_X + H2O_X
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
    index = 23,
    label = "O* + H3NX <=> H2NX + OH_4*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(2.47e21,'cm^2/(mol*s)'), n=0, Ea=(69472.8,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pd111
Original entry: NH3_X +O_X <=> NH2_X + OH_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd111 = 2.534E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 0.72eV = 69472.8J/mol

This is reaction (3) in Table S3
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 24,
    label = "H2NX-2 + OH_2* <=> H2O* + HNX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.47e21,'cm^2/(mol*s)'), n=0, Ea=(7719.2,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pd111
Original entry: NH2_X + OH_X <=> NH_X + H2O_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd111 = 2.534E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 0.08eV = 7719.2J/mol

This is reaction (7) in Table S3
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 25,
    label = "HNX-2 + OH_2* <=> H2O* + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.47e21,'cm^2/(mol*s)'), n=0, Ea=(46315.2,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pd111
Original entry: NH_X + OH_X <=> N_X + H2O_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd111 = 2.534E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 0.48eV = 46315.2J/mol

This is reaction (8) in Table S3
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 26,
    label = "OH_2* + OH_4* <=> H2O* + O*",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.47e21,'cm^2/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pd111
Original entry: OH_X + OH_X <=> O_X + H2O_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd111 = 2.534E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1

This is reaction (9) in Table S3
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 27,
    label = "O* + H3NX <=> H2NX + OH_4*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(6.4e20,'cm^2/(mol*s)'), n=0, Ea=(92630.4,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Popa_Rh111
Original entry: NH3_X +O_X <=> NH2_X + OH_X
Based primarily on 
"Density-functional theory study of NHx oxidation 
and reverse reactions on the Rh (111) surface."
C. Popa, R. A. van Santen, and A. P. J. JansenJ.
Phys. Chem. C 2007, 111, 9839– 9852.
https://doi.org/10.1021/jp071072g

This is reaction 2a. in TABLE 4.

This reaction used RMG's surface site density of Rh111 = 2.656E-09(mol/cm^2) to calculate the A factor.
A (at 300K)= 1.7E12(1/s)/2.656E-9(mol/cm^2) = 6.40E20 cm^2/(mol*s)
Ea = 0.96eV = 92630.4J/mol
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 28,
    label = "H2NX-2 + OH_2* <=> H2O* + HNX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.5e21,'cm^2/(mol*s)'), n=0, Ea=(13508.6,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Popa_Rh111
Original entry: NH2_X + OH_X <=> NH_X + H2O_X
Based primarily on 
"Density-functional theory study of NHx oxidation 
and reverse reactions on the Rh (111) surface."
C. Popa, R. A. van Santen, and A. P. J. JansenJ.
Phys. Chem. C 2007, 111, 9839– 9852.
https://doi.org/10.1021/jp071072g

This is reaction 3a. in TABLE 5.

This reaction used RMG's surface site density of Rh111 = 2.656E-09(mol/cm^2) to calculate the A factor.
A (at 300K)= 3.98E12(1/s)/2.656E-9(mol/cm^2) = 1.50E21 cm^2/(mol*s)
Ea = 0.14eV = 13508.6J/mol
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 29,
    label = "HNX-2 + OH_2* <=> H2O* + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.52e20,'cm^2/(mol*s)'), n=0, Ea=(22192.7,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Popa_Rh111
Original entry: NH_X + OH_X <=> N_X + H2O_X
Based primarily on 
"Density-functional theory study of NHx oxidation 
and reverse reactions on the Rh (111) surface."
C. Popa, R. A. van Santen, and A. P. J. JansenJ.
Phys. Chem. C 2007, 111, 9839– 9852.
https://doi.org/10.1021/jp071072g

This is reaction 6a. in TABLE 5.

This reaction used RMG's surface site density of Rh111 = 2.656E-09(mol/cm^2) to calculate the A factor.
A (at 300K)= 1.2E12(1/s)/2.656E-9(mol/cm^2) = 4.52E20 cm^2/(mol*s)
Ea = 0.23eV = 22192.7J/mol
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 30,
    label = "O* + H3NX <=> H2NX + OH_4*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(6.85e23,'cm^2/(mol*s)'), n=0, Ea=(157,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Rebrov_Pt111
Original entry: NH3_X +O_X <=> NH2_X + OH_X
"Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
https://doi.org/10.1016/S1385-8947(02)00068-2

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1.7E15(1/s)/2.483E-9(mol/cm^2) = 6.85E23 cm^2/(mol*s)

This is R5 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 31,
    label = "O* + HNOX <=> NOX + OH_4*",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(8.05e23,'cm^2/(mol*s)'), n=0, Ea=(11800,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Rebrov_Pt111
Original entry: NHO_X + O_X <=> NO_X + OH_X
"Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
https://doi.org/10.1016/S1385-8947(02)00068-2

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 2E15(1/s)/2.483E-9(mol/cm^2) = 8.05E23 cm^2/(mol*s)

This is R10 in Table 1, it's from ref[52] where metal = Pt100.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 32,
    label = "HNX-2 + OH_2* <=> H2O* + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.03e19,'cm^2/(mol*s)'), n=0, Ea=(79000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Rebrov_Pt111
Original entry: NH_X + OH_X <=> N_X + H2O_X
"Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
https://doi.org/10.1016/S1385-8947(02)00068-2

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1E11(1/s)/2.483E-9(mol/cm^2) = 4.03E19 cm^2/(mol*s)

This is R2 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 33,
    label = "O* + H2O* <=> OH_2* + OH_4*",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(4.03e19,'cm^2/(mol*s)'), n=0, Ea=(52700,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Rebrov_Pt111
Original entry: O_X + H2O_X <=> OH_X + OH_X
"Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
https://doi.org/10.1016/S1385-8947(02)00068-2

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1E11(1/s)/2.483E-9(mol/cm^2) = 4.03E19 cm^2/(mol*s)

This is R18 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 34,
    label = "O* + H3NX <=> H2NX + OH_4*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(1.56e21,'cm^2/(mol*s)'), n=0, Ea=(55964.2,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pt211
Original entry: NH3_X +O_X <=> NH2_X + OH_X
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
    index = 35,
    label = "H2NX-2 + OH_2* <=> H2O* + HNX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.48e21,'cm^2/(mol*s)'), n=0, Ea=(76227.1,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pt211
Original entry: NH2_X + OH_X <=> NH_X + H2O_X
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
    index = 36,
    label = "HNX-2 + OH_2* <=> H2O* + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.01e21,'cm^2/(mol*s)'), n=0, Ea=(81051.6,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pt211
Original entry: NH_X + OH_X <=> N_X + H2O_X
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
    index = 37,
    label = "OH_2* + OH_4* <=> H2O* + O*",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.59e21,'cm^2/(mol*s)'), n=0, Ea=(81051.6,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pt211
Original entry: OH_X + OH_X <=> O_X + H2O_X
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
    index = 38,
    label = "O* + H2O* <=> OH_2* + OH_4*",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(1.74e19,'cm^2/(mol*s)'), n=0.082, Ea=(8.8,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Pt111
Original entry: O_X + H2O_X <=> OH_X + OH_X
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 4.32E10(1/s)/2.483E-9(mol/cm^2) = 1.74E19 cm^2/(mol*s)

This is R17 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 39,
    label = "CH2X + H2O* <=> OH_2* + CH3X",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(3.3e19,'cm^2/(mol*s)'), n=0.099, Ea=(14.1,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Pt111
Original entry: CH2_X + H2O_X <=> CH3_X + OH_X
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 8.19E10(1/s)/2.483E-9(mol/cm^2) = 3.30E19 cm^2/(mol*s)

This is R69 in Table 2
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 40,
    label = "CHX + H2O* <=> OH_2* + CH2X-2",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(7.29e19,'cm^2/(mol*s)'), n=0.269, Ea=(34,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Pt111
Original entry: CH_X + H2O_X <=> CH2_X + OH_X
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1.81E11(1/s)/2.483E-9(mol/cm^2) = 7.29E19 cm^2/(mol*s)

This is R71 in Table 2
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 41,
    label = "CH2X + H2O* <=> OH_2* + CH3X",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.3e19,'cm^2/(mol*s)'), n=-0.7208, Ea=(20.3,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Rh
Original entry: CH2_X + H2O_X <=> CH3_X + OH_X
"Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
Vlachos et al. (2008)
Journal of Catalysis,259(2), 211-222, 0021-9517
DOI: 10.1016/j.jcat.2008.08.008.D.G.

Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
A = 5.73E+10(1/s)/2.49E-9(mol/cm^2) = 2.30E+19 cm^2/(mol*s)

This is R69 in Table 4
""",
    metal = "Rh",
)

entry(
    index = 42,
    label = "H2NX + H2NX-2 <=> H3NX + HNX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.16e20,'cm^2/(mol*s)'), n=0.667, Ea=(43420,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Cu111
Original entry: NH2_X + NH2_X <=> NH_X + NH3_X
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This reaction used RMG's surface site density of Cu111 = 2.943E-9(mol/cm^2) to estimate A factor.
A and n was calculated by numpy.linalg.lstsq from Table 1

This is R36 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 43,
    label = "H3N2X + H2NX <=> H3NX + H2N2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.02e19,'cm^2/(mol*s)'), n=1.073, Ea=(51140,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Cu111
Original entry: N2H3_X + NH2_X <=> NN=[Pt] + NH3_X
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This reaction used RMG's surface site density of Cu111 = 2.943E-9(mol/cm^2) to estimate A factor.
A and n was calculated by numpy.linalg.lstsq from Table 1

This is R42 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 44,
    label = "H2N2X2 + H2NX <=> H3NX + HN2X2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.94e20,'cm^2/(mol*s)'), n=0.577, Ea=(24122,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Cu111
Original entry: [Pt]NN[Pt] + NH2_X <=> [Pt]NN=[Pt] + NH3_X
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This reaction used RMG's surface site density of Cu111 = 2.943E-9(mol/cm^2) to estimate A factor.
A and n was calculated by numpy.linalg.lstsq from Table 1

This is R44 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 45,
    label = "HN2X2-2 + H2NX <=> H3NX + N2X2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.04e19,'cm^2/(mol*s)'), n=0.86, Ea=(7719,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Cu111
Original entry: [Pt]NN=[Pt] + NH2_X <=> [Pt]=NN=[Pt] + NH3_X
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This reaction used RMG's surface site density of Cu111 = 2.943E-9(mol/cm^2) to estimate A factor.
A and n was calculated by numpy.linalg.lstsq from Table 1

This is R48 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 46,
    label = "H2N2X2 + H2NX <=> H3NX + HN2X2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.87e21,'cm^2/(mol*s)'), n=0, Ea=(18333.1,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Ir111
Original entry: [Pt]NN[Pt] + NH2_X <=> [Pt]NN=[Pt] + NH3_X
"Mechanistic study of hydrazine decomposition on Ir(111)"
Alberto Roldan et al. Phys.Chem.Chem.Phys., 2020, 22, 3883
DOI: 10.1039/c9cp06525c

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2)
to estimate a default(1E13) A factor.
A = 1E13(1/s)/2.587E-9(mol/cm^2) = 3.87E21 cm^2/(mol*s)
Ea = 0.19eV = 18333.1J/mol

This is R18 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 47,
    label = "H3N2X + H2NX <=> H3NX + H2N2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.87e21,'cm^2/(mol*s)'), n=0, Ea=(35701.3,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Ir111
Original entry: N2H3_X + NH2_X <=> NN=[Pt] + NH3_X
"Mechanistic study of hydrazine decomposition on Ir(111)"
Alberto Roldan et al. Phys.Chem.Chem.Phys., 2020, 22, 3883
DOI: 10.1039/c9cp06525c

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2)
to estimate a default(1E13) A factor.
A = 1E13(1/s)/2.587E-9(mol/cm^2) = 3.87E21 cm^2/(mol*s)
Ea = 0.37eV = 35701.3J/mol

This is R19 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 48,
    label = "HN2X2-2 + H2NX <=> H3NX + N2X2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.87e21,'cm^2/(mol*s)'), n=0, Ea=(53069.5,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Ir111
Original entry: [Pt]NN=[Pt] + NH2_X <=> N2_X + NH3_X
"Mechanistic study of hydrazine decomposition on Ir(111)"
Alberto Roldan et al. Phys.Chem.Chem.Phys., 2020, 22, 3883
DOI: 10.1039/c9cp06525c

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2)
to estimate a default(1E13) A factor.
A = 1E13(1/s)/2.587E-9(mol/cm^2) = 3.87E21 cm^2/(mol*s)
Ea = 0.55eV = 53069.5J/mol

This is R21 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 49,
    label = "H2NX + H2NX-2 <=> H3NX + HNX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.87e21,'cm^2/(mol*s)'), n=0, Ea=(32806.6,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Ir111
Original entry: NH2_X + NH2_X <=> NH_X + NH3_X
"Mechanistic study of hydrazine decomposition on Ir(111)"
Alberto Roldan et al. Phys.Chem.Chem.Phys., 2020, 22, 3883
DOI: 10.1039/c9cp06525c

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2)
to estimate a default(1E13) A factor.
A = 1E13(1/s)/2.587E-9(mol/cm^2) = 3.87E21 cm^2/(mol*s)
Ea = 0.34eV = 32806.6J/mol

This is R25 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 50,
    label = "HNX-2 + H2NX <=> H3NX + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.87e21,'cm^2/(mol*s)'), n=0, Ea=(94560.2,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Ir111
Original entry: NH_X + NH2_X <=> N_X + NH3_X
"Mechanistic study of hydrazine decomposition on Ir(111)"
Alberto Roldan et al. Phys.Chem.Chem.Phys., 2020, 22, 3883
DOI: 10.1039/c9cp06525c

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2)
to estimate a default(1E13) A factor.
A = 1E13(1/s)/2.587E-9(mol/cm^2) = 3.87E21 cm^2/(mol*s)
Ea = 0.98eV = 94560.2J/mol

This is R26 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 6,
    label = "H3NX + O* <=> H2NX + OH_4*",
    degeneracy = 3,
    kinetics = SurfaceArrhenius(
        A = (1.49013e+16, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (55.0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 3 in "Modeling ammonia oxidation over a Pt (533) surface"
https://doi.org/10.1016/j.susc.2011.08.014

A factor from paper / surface site density of Pt
3.7e11 1/s / 2.483e-05 mol/m^2 = 8.4422e+16 m^2/(mol*s)
""",
    metal="Pt",
    facet="533"
)

entry(
    index = 7,
    label = "H3NX + HOr_Pt <=> H2NX + H2O_Pt",
    degeneracy = 3,
    kinetics = SurfaceArrhenius(
        A = (1.5706e+17, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (73.0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 6 in "Modeling ammonia oxidation over a Pt (533) surface"
https://doi.org/10.1016/j.susc.2011.08.014

A factor from paper / surface site density of Pt
3.9e12 1/s / 2.483e-05 mol/m^2 = 9.6837e+17 m^2/(mol*s)
""",
    metal="Pt",
    facet="533"
)

entry(
    index = 8,
    label = "H2NX-2 + OH_2*  <=> HNX + H2O*",
    degeneracy = 2,
    kinetics = SurfaceArrhenius(
        A = (1.36931e+17, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (22.0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 7 in "Modeling ammonia oxidation over a Pt (533) surface"
https://doi.org/10.1016/j.susc.2011.08.014

A factor from paper / surface site density of Pt
3.4e12 1/s / 2.483e-05 mol/m^2 = 9.6837e+17 m^2/(mol*s)
""",
    metal="Pt",
    facet="533"
)

entry(
    index = 9,
    label = "HNX-2 + OH_2*  <=> NX + H2O*",
    degeneracy = 2,
    kinetics = SurfaceArrhenius(
        A= (2.0540e+16, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (22.0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 8 in "Modeling ammonia oxidation over a Pt (533) surface"
https://doi.org/10.1016/j.susc.2011.08.014

A factor from paper / surface site density of Pt
5.1e11 1/s / 2.483e-05 mol/m^2 = 9.6837e+17 m^2/(mol*s)
""",
    metal="Pt",
    facet="533"
)

entry(
    index = 10,
    label = "HNX-2 + OH_2*  <=> NX + H2O*",
    degeneracy = 2,
    kinetics = SurfaceArrhenius(
        A=(1.26633e+17, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (22.0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 8 in "Modeling ammonia oxidation over a Pt (533) surface"
https://doi.org/10.1016/j.susc.2011.08.014

A factor from paper / surface site density of Pt
5.1e11 1/s / 2.483e-05 mol/m^2 = 9.6837e+17 m^2/(mol*s)
""",
    metal="Pt",
    facet="533"
)

entry(
    index = 11,
    label = "HOr_Pt + HO123_Pt  <=> O* + H2O*",
    degeneracy = 2,
    kinetics = SurfaceArrhenius(
        A= (4.02739e+17, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (75.0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 9 in "Modeling ammonia oxidation over a Pt (533) surface"
https://doi.org/10.1016/j.susc.2011.08.014

A factor from paper / surface site density of Pt
1e13 1/s / 2.483e-05 mol/m^2 = 9.6837e+17 m^2/(mol*s)
""",
    metal="Pt",
    facet="533"
)
entry(
    index = 51,
    label = "CO* + H2OX <=> HX + CHO2X",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(1.34e20,'cm^2/(mol*s)'), n=-0.2222, Ea=(19.5,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Rh
Original entry: CO_X + H2O_X <=> COOH_X + H_X
"Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
Vlachos et al. (2008)
Journal of Catalysis,259(2), 211-222, 0021-9517
DOI: 10.1016/j.jcat.2008.08.008.D.G.

Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
A = 3.34E+11(1/s)/2.49E-9(mol/cm^2) = 1.34E+20 cm^2/(mol*s)

This is R35 in Table 4
""",
    metal = "Rh",
)

entry(
    index = 52,
    label = "CX + H2O* <=> OH_2* + CHX-2",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(3.91e20,'cm^2/(mol*s)'), n=-0.3882, Ea=(17,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Rh
Original entry: C_X + H2O_X <=> CH_X + OH_X
"Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
Vlachos et al. (2008)
Journal of Catalysis,259(2), 211-222, 0021-9517
DOI: 10.1016/j.jcat.2008.08.008.D.G.

Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
A = 9.74E+11(1/s)/2.49E-9(mol/cm^2) = 3.91E+20 cm^2/(mol*s)

This is R73 in Table 4
""",
    metal = "Rh",
)

entry(
    index = 53,
    label = "CO* + H2OX <=> HX + CHO2X",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(4.43e19,'cm^2/(mol*s)'), n=0.492, Ea=(23.7,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Pt111
Original entry: CO_X + H2O_X <=> COOH_X + H_X
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1.10E11(1/s)/2.483E-9(mol/cm^2) = 4.43E19 cm^2/(mol*s)

This is R33 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 54,
    label = "CX + H2O* <=> OH_2* + CHX-2",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(4.19e19,'cm^2/(mol*s)'), n=0.09, Ea=(15.6,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Pt111
Original entry: C_X + H2O_X <=> CH_X + OH_X
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1.04E11(1/s)/2.483E-9(mol/cm^2) = 4.19E19 cm^2/(mol*s)

This is R73 in Table 2
""",
    metal = "Pt",
    facet = "111",
)

