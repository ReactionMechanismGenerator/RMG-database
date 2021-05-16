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
    kinetics = SurfaceArrhenius(A=(3.09e+09,'1/s'), n=0, Ea=(60900,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ralph_Pt111
Original entry: NH3_X <=> NH3 + X
"Ammonia Oxidation over Polycrystalline Platinum: 
Surface Morphology and Kinetics at Atmospheric Pressure."
Krähnert, Ralph(2005) A Doctoral Thesis.
http://dx.doi.org/10.14279/depositonce-1270

A = k/exp(Ea/RT) = 2.17(mol/m^2/s)/exp(60900J/mol / 8.314J/molK / 298K) = 4.09E9 cm^2/mol/s
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
A (at 300K from p.62)= 8.6E12(1/s)/2.483E-9(mol/cm^2) = 3.464E21 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)entry(
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
    shortDesc = """Surface_Adsorption""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Rebrov_Pt111
Original entry: H2O_X <=> H2O + X
"Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
https://doi.org/10.1016/S1385-8947(02)00068-2

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1E13(1/s)/2.483E-9(mol/cm^2) = 4.03E21 cm^2/(mol*s)

This is R19 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

