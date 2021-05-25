#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_vdW/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 5,
    label = "H2O + X <=> H2OX",
    kinetics = StickingCoefficient(
        A = 1.0E-1,
        n = 0,
        Ea = (0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""R5
    test surface mechanism: based upon Olaf Deutschmann's work:
    "Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
    Delgado et al
    Catalysts, 2015, 5, 871-904""",
	metal = "Ni",
)

entry(
    index = 7,
    label = "CO2 + X <=> CO2X",
    kinetics = StickingCoefficient(
        A = 7.0E-6,
        n = 0,
        Ea = (0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""R7
    test surface mechanism: based upon Olaf Deutschmann's work:
    "Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
    Delgado et al
    Catalysts, 2015, 5, 871-904""",
	metal = "Ni",
)

entry(
    index = 11,
    label = "CH4 + X <=> CH4X",
    kinetics = StickingCoefficient(
        A = 8.0E-3,
        n = 0,
        Ea = (0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""R11
    test surface mechanism: based upon Olaf Deutschmann's work:
    "Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
    Delgado et al
    Catalysts, 2015, 5, 871-904""",
	metal = "Ni",
)

entry(
    index = 12,
    label = "H3NX <=> H3N + X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.48e+09,'1/s'), n=0, Ea=(60900,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Krahnert_Pt111
Original entry: NH3_X <=> NH3 + X
"Ammonia Oxidation over Polycrystalline Platinum: 
Surface Morphology and Kinetics at Atmospheric Pressure."
Krähnert, Ralph(2005) A Doctoral Thesis.
http://dx.doi.org/10.14279/depositonce-1270

A = k/exp(Ea/RT) = 2.17(1/s)/exp(60900J/mol / 8.314J/molK / 658K) = 1.48E09 (1/s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 13,
    label = "X + N2 <=> N2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.464e+21,'cm^3/(mol*s)'), n=0, Ea=(4000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """N2 Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Offermans_Pt111
Original entry: N2 + X <=> N2_X
"Ammonia oxidation on platinum : a density functional theory study of surface reactivity."
Offermans, W. K. (2007). Technische Universiteit Eindhoven. 
https://doi.org/10.6100/IR630067

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 300K from p.62)= 8.6E12(cm/s)/2.483E-9(mol/cm^2) = 3.464E21 cm^3/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 14,
    label = "H3NX <=> H3N + X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.03e+17,'1/s'), n=0, Ea=(75200,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Rebrov_Pt111
Original entry: NH3_X <=> NH3 + X
"Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
https://doi.org/10.1016/S1385-8947(02)00068-2

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1E9(mol/cm^2/s)/2.483E-9(mol/cm^2) = 4.03E17 (1/s)

This is R2 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 15,
    label = "H2OX <=> H2O + X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.03e+21,'1/s'), n=0, Ea=(40300,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Rebrov_Pt111
Original entry: H2O_X <=> H2O + X
"Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
https://doi.org/10.1016/S1385-8947(02)00068-2

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1E13(mol/cm^2/s)/2.483E-9(mol/cm^2) = 4.03E21 (1/s)

This is R19 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 16,
    label = "X + H3N <=> H3NX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.00768, n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Scheuer_Pt
Original entry: NH3 + X <=> NH3_X
"Dual layer automotive ammonia oxidation catalysts: Experiments and computer simulation"
Scheuer et al. Applied Catalysis B: Environmental 111–112 (2012) 445–455
https://doi.org/10.1016/j.apcatb.2011.10.032

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = ((19/Pa)/s)*(2.483e-9(mol/cm^2))*sqrt(2*pi*(17(g/mol))*the molar gas constant*(298 kelvin))= 0.00768

This is R1 in Table 1
""",
    metal = "Pt",
)

entry(
    index = 17,
    label = "H2OX <=> H2O + X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.38e+24,'1/s'), n=0, Ea=(18333.1,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pt111
Original entry: H2O_X <=> H2O + X
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 5.9E15(1/s)/2.483E-9(mol/cm^2) = 2.38E24 cm^2/(mol*s)
Ea = 0.19eV = 18333.1J/mol

This is R10 in Table S2 and S4
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 18,
    label = "N2OX <=> N2O + X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(5.64e+24,'1/s'), n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_Double/Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pt111
Original entry: N2O_X <=> N2O + X
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1.4E16(1/s)/2.483E-9(mol/cm^2) = 5.64E24 cm^2/(mol*s)

This is R15 in Table S2 and S4
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 19,
    label = "H2OX <=> H2O + X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.4e+24,'1/s'), n=0, Ea=(24122.5,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pt211
Original entry: H2O_X <=> H2O + X
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
    index = 20,
    label = "N2OX <=> N2O + X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(5.69e+25,'1/s'), n=0, Ea=(9649,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_Double/Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pt211
Original entry: N2O_X <=> N2O + X
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

