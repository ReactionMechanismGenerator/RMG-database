#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_vdW/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
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
    index = 2,
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
    index = 3,
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
    index = 4,
    label = "H3NX <=> H3N + X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.48e+09,'1/s'), n=0, Ea=(60900,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Kraehnert_Pt111
Original entry: NH3_X <=> NH3 + X
"Kinetics of ammonia oxidation over Pt foil studied in a micro-structured quartz-reactor"
Kraehnert et al.(2008) 
Chemical Engineering Journal,137(2), 361-375
https://doi.org/10.1016/j.cej.2007.05.005

A = k/exp(-Ea/RT) = 2.17(1/s)/exp(-60900(J/mol)/8.314(J/mol/K)/658K) = 1.48E09 (1/s)

Table 3, R1
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 5,
    label = "X + H3N <=> H3NX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.79731, n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Rebrov_Pt111
Original entry: NH3 + X <=> NH3_X
"Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
https://doi.org/10.1016/S1385-8947(02)00068-2

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = ((2e8 /atm)/(101325 Pa/atm)/s)*(2.483e-9(mol/cm^2))*sqrt(2*pi*(17(g/mol))*the molar gas constant*(298 kelvin))

This is R1 in Table 3
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 6,
    label = "H3NX <=> H3N + X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.29e+08,'1/s'), n=0, Ea=(72149.6,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Roldan_Ru0001
Original entry: NH3_X <=> NH3 + X
"Kinetic and mechanistic analysis of NH3 decomposition 
on Ru(0001), Ru(111) and Ir(111) surfaces"
Alberto Roldan et al. Nanoscale Adv., 2021, 3, 1624
DOI: 10.1039/d1na00015b

Ea was calculated from A factor and k rate constant in Table 3

This is D1 in Table 3
""",
    metal = "Ru",
    facet = "0001",
)

entry(
    index = 7,
    label = "X + N2 <=> N2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.29e+08,'cm^3/(mol*s)'), n=0, Ea=(24483,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Roldan_Ru0001
Original entry: N2 + X <=> N2_X
"Kinetic and mechanistic analysis of NH3 decomposition 
on Ru(0001), Ru(111) and Ir(111) surfaces"
Alberto Roldan et al. Nanoscale Adv., 2021, 3, 1624
DOI: 10.1039/d1na00015b

Ea was calculated from A factor and k rate constant in Table 3

This is A2 in Table 3
""",
    metal = "Ru",
    facet = "0001",
)

entry(
    index = 8,
    label = "H2X <=> H2 + X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.29e+08,'1/s'), n=0, Ea=(24483,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """H2 Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Roldan_Ru0001
Original entry: H2_X <=> H2 + X
"Kinetic and mechanistic analysis of NH3 decomposition 
on Ru(0001), Ru(111) and Ir(111) surfaces"
Alberto Roldan et al. Nanoscale Adv., 2021, 3, 1624
DOI: 10.1039/d1na00015b

Ea was calculated from A factor and k rate constant in Table 3

This is D3 in Table 3
""",
    metal = "Ru",
    facet = "0001",
)

entry(
    index = 9,
    label = "X + H3N <=> H3NX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=1, n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Schneider_Pt111
Original entry: NH3 + X <=> NH3_X
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = ((2.5E3 /pa) / s) * (2.483E-9 mol/cm2) * sqrt(2 * pi * 17 g/mol * molar gas constant * 298 kelvin) ≈ 1

This is R2 in Table S2 and S4
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 10,
    label = "X + H3N <=> H3NX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=1, n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Schneider_Pt211
Original entry: NH3 + X <=> NH3_X
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt211 = 2.634E-9(mol/cm^2) to calculate the A factor.
A = ((2.5E3 /pa) / s) * (2.634E-9 mol/cm2) * sqrt(2 * pi * 17 g/mol * molar gas constant * 298 kelvin)
 
This is R2 in Table S2 and S4
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 11,
    label = "X + H3N <=> H3NX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=1, n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Schneider_Pd111
Original entry: NH3 + X <=> NH3_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

Scitcking coefficient from Schneider_Pt111

This is reaction (2) in Table S3
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 12,
    label = "X + H3N <=> H3NX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=1, n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Schneider_Pd211
Original entry: NH3 + X <=> NH3_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

Scitcking coefficient from Schneider_Pt111

This is reaction (2) in Table S2
""",
    metal = "Pd",
    facet = "211",
)

