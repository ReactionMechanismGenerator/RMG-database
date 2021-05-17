#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Abstraction_vdW/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

#reverse of 16, below
entry(
    index = 34,
    label = "H2O* + O* <=> OH_2* + OH_4*",
    degeneracy = 2,
    kinetics = SurfaceArrhenius(
        A = (8.14E20, 'm^2/(mol*s)'),
        n = -0.274,
        Ea = (218400, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""R34
    test surface mechanism: based upon Olaf Deutschmann's work:
    "Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
    Delgado et al
    Catalysts, 2015, 5, 871-904""",
	  metal = "Ni",
)

# reverse of 34, above
# This entry is in reverse direction for family
# entry(
#     index = 16,
#     label = "OH_2* + OH_4* <=> H2O* + O*",
#     degeneracy = 2,
#     kinetics = SurfaceArrhenius(
#         A = (5.691e16, 'm^2/(mol*s)'),
#         n = 0.,
#         Ea = (14.0669343, 'kcal/mol'),
#         Tmin = (298, 'K'),
#         Tmax = (2000, 'K'),
#     ),
#     rank = 10,
#     shortDesc = u"""Default""",
#     longDesc = u"""
# Reaction 16 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
# and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

# A factor from paper / surface site density of Cu
# 1.675e12 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 5.691e16 m^2/(mol*s)
# """,
#     metal = "Cu",
# )

entry(
    index = 21,
    label = "CH4* + O* <=> CH3* + OH_4*",
    degeneracy = 4,
    kinetics = SurfaceArrhenius(
        A = (5.62E20, 'm^2/(mol*s)'),
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
    index = 40,
    label = "OH_2* + HCO* <=> H2O* + CO*",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (3.261e17, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (0.30, 'eV/molecule'),
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
""",
    metal = "Cu",
)

entry(
    index = 41,
    label = "HCOO_1* + HCO* <=> HCOOH* + CO*",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (7.475e18, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (0.60, 'eV/molecule'),
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
""",
    metal = "Cu",
)

entry(
    index = 45,
    label = "CH3O* + HCO* <=> CH3OH* + CO*",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (6.572e16, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (0.38, 'eV/molecule'),
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
""",
    metal = "Cu",
)

entry(
    index = 46,
    label = "CH3O* + HCOO_5* <=> HCOOCH3* + O*",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (2.356e16, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (1.24, 'eV/molecule'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 46 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
6.934e11 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 2.356e16 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 47,
    label = "O* + H3NX <=> H2NX + OH_4*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(1.007e+21,'cm^2/(mol*s)'), n=0, Ea=(67543,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
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
A = 5.2E12(1/s)/2.483E-9(mol/cm^2) = 1.007E21 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 48,
    label = "H2NX-2 + OH_2* <=> H2O* + HNX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.041e+21,'cm^2/(mol*s)'), n=0, Ea=(965,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
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
A = 1.5E13(1/s)/2.483E-9(mol/cm^2) = 6.041E21 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 49,
    label = "HNX-2 + OH_2* <=> H2O* + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.376e+21,'cm^2/(mol*s)'), n=0, Ea=(39561,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
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
A = 5.9E12(1/s)/2.483E-9(mol/cm^2) = 2.376E21 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 50,
    label = "OH_2* + OH_4* <=> H2O* + O*",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.248e+21,'cm^2/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Reverse R95""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pt111
Original entry: OH_X + OH_X <=> O_X + H2O_X
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 3.1E12(1/s)/2.483E-9(mol/cm^2) = 1.248E21 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 51,
    label = "O* + H3NX <=> H2NX + OH_4*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(4.833e+20,'cm^2/(mol*s)'), n=0, Ea=(42000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
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
    index = 52,
    label = "H2NX-2 + OH_2* <=> H2O* + HNX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.369e+21,'cm^2/(mol*s)'), n=0, Ea=(22000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_Single_vdW""",
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
    index = 53,
    label = "HNX-2 + OH_2* <=> H2O* + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.054e+20,'cm^2/(mol*s)'), n=0, Ea=(35000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_Single_vdW""",
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
    index = 54,
    label = "O* + H3NX <=> H2NX + OH_4*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(2.47e+21,'cm^2/(mol*s)'), n=0, Ea=(86841,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
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
    index = 55,
    label = "H2NX-2 + OH_2* <=> H2O* + HNX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.47e+21,'cm^2/(mol*s)'), n=0, Ea=(25087.4,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
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
    index = 56,
    label = "HNX-2 + OH_2* <=> H2O* + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.47e+21,'cm^2/(mol*s)'), n=0, Ea=(39561,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
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
    index = 57,
    label = "OH_2* + OH_4* <=> H2O* + O*",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.47e+21,'cm^2/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
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
    index = 58,
    label = "O* + H3NX <=> H2NX + OH_4*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(2.44e+21,'cm^2/(mol*s)'), n=0, Ea=(39560.9,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
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
    index = 59,
    label = "H2NX-2 + OH_2* <=> H2O* + HNX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.44e+21,'cm^2/(mol*s)'), n=0, Ea=(73332.4,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
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
    index = 60,
    label = "HNX-2 + OH_2* <=> H2O* + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.44e+21,'cm^2/(mol*s)'), n=0, Ea=(41490.7,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
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
    index = 61,
    label = "OH_2* + OH_4* <=> H2O* + O*",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.44e+21,'cm^2/(mol*s)'), n=0, Ea=(71402.6,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
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
    index = 62,
    label = "O* + H3NX <=> H2NX + OH_4*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(2.47e+21,'cm^2/(mol*s)'), n=0, Ea=(69472.8,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
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
    index = 63,
    label = "H2NX-2 + OH_2* <=> H2O* + HNX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.47e+21,'cm^2/(mol*s)'), n=0, Ea=(7719.2,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
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
    index = 64,
    label = "HNX-2 + OH_2* <=> H2O* + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.47e+21,'cm^2/(mol*s)'), n=0, Ea=(46315.2,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
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
    index = 65,
    label = "OH_2* + OH_4* <=> H2O* + O*",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.47e+21,'cm^2/(mol*s)'), n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
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
    index = 66,
    label = "O* + H3NX <=> H2NX + OH_4*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(6.4e+20,'cm^2/(mol*s)'), n=0, Ea=(92630.4,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
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
    index = 67,
    label = "H2NX-2 + OH_2* <=> H2O* + HNX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.5e+21,'cm^2/(mol*s)'), n=0, Ea=(13508.6,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_Single_vdW""",
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
    index = 68,
    label = "HNX-2 + OH_2* <=> H2O* + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.52e+20,'cm^2/(mol*s)'), n=0, Ea=(22192.7,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_Single_vdW""",
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
    index = 69,
    label = "O* + H3NX <=> H2NX + OH_4*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(6.85e+23,'cm^2/(mol*s)'), n=0, Ea=(157,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
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
    index = 70,
    label = "O* + HNOX <=> NOX + OH_4*",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(8.05e+23,'cm^2/(mol*s)'), n=0, Ea=(11800,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
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
    index = 71,
    label = "HNX-2 + OH_2* <=> H2O* + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.03e+19,'cm^2/(mol*s)'), n=0, Ea=(79000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_Single_vdW""",
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
    index = 72,
    label = "O* + H2O* <=> OH_2* + OH_4*",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(4.03e+19,'cm^2/(mol*s)'), n=0, Ea=(52700,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
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

