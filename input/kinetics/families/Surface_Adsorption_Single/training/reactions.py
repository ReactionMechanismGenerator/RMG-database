#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_Single/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "NO + X <=> NO_X",
    degeneracy = 1,
    kinetics = StickingCoefficient(
        A = 0.85,
        n = 0,
        Ea = (0, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 11,
    shortDesc = u"""NO Adsorption""",
    longDesc = u"""
    Detailed surface reaction mechanism in a three-way catalyst
    Chatterjee, Deutschmann, Warnatz et al.
    doi: 10.1039/b101968f

    This is R48""",
    metal = "Pt",
)

# entry(
#     index = 2,
#     label = "NO_X <=> NO + X",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(2.41e+16,'1/s'), n=0, Ea=(154800,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
#     rank = 3,
#     shortDesc = """Surface_Adsorption_Single""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/Ammonia/Kraehnert_Pt111
# Original entry: NO_X <=> NO + X
# "Kinetics of ammonia oxidation over Pt foil studied in a micro-structured quartz-reactor"
# Kraehnert et al.(2008) 
# Chemical Engineering Journal,137(2), 361-375
# https://doi.org/10.1016/j.cej.2007.05.005

# A = k/exp(-Ea/RT) = 1.24(1/s)/exp(-154800(J/mol)/8.314(J/mol/K)/658K) = 2.41E16 (1/s)

# Table 3, R4
# """,
#     metal = "Pt",
#     facet = "111",
# )

# entry(
#     index = 3,
#     label = "NO_X <=> NO + X",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(1.5e+13,'1/s'), n=0, Ea=(143000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
#     rank = 3,
#     shortDesc = """Surface_Adsorption_Single""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/Ammonia/Rebrov_Pt111
# Original entry: NO_X <=> NO + X
# "Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
# Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
# https://doi.org/10.1016/S1385-8947(02)00068-2

# This is L12 in Table 3
# """,
#     metal = "Pt",
#     facet = "111",
# )

# entry(
#     index = 4,
#     label = "NO_X <=> NO + X",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(2.6e+17,'1/s'), n=0, Ea=(184296,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
#     rank = 3,
#     shortDesc = """Surface_Adsorption_Single""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/Ammonia/Schneider_Pt111
# Original entry: NO_X <=> NO + X
# "Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
# Ma, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
# https://doi.org/10.1021/acscatal.8b04251

# Ea = 1.91eV = 184295.9J/mol

# This is R13 in Table S2 and S4
# """,
#     metal = "Pt",
#     facet = "111",
# )

# entry(
#     index = 5,
#     label = "NO_X <=> NO + X",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(1.3e+17,'1/s'), n=0, Ea=(224822,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
#     rank = 3,
#     shortDesc = """Surface_Adsorption_Single""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/Ammonia/Schneider_Pt211
# Original entry: NO_X <=> NO + X
# "Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
# Ma, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
# https://doi.org/10.1021/acscatal.8b04251

# Ea = 2.33eV = 224821.7J/mol

# This is R13 in Table S2 and S4
# """,
#     metal = "Pt",
#     facet = "211",
# )

# entry(
#     index = 6,
#     label = "NO_X <=> NO + X",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(2.6e+12,'1/s'), n=0, Ea=(221927,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
#     rank = 3,
#     shortDesc = """Surface_Adsorption_Single""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/Ammonia/Schneider_Pd111
# Original entry: NO_X <=> NO + X
# "DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
# Hanyu Ma, and William F.Schneider
# Journal of Catalysis 383 (2020) 322–330
# https://doi.org/10.1016/j.jcat.2020.01.029

# Ea = 2.3eV = 221927J/mol

# This is reaction (13) in Table S3
# """,
#     metal = "Pd",
#     facet = "111",
# )

# entry(
#     index = 7,
#     label = "NO_X <=> NO + X",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(6.55e+13,'1/s'), n=0, Ea=(225787,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
#     rank = 3,
#     shortDesc = """Surface_Adsorption_Single""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/Ammonia/Schneider_Pd211
# Original entry: NO_X <=> NO + X
# "DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
# Hanyu Ma, and William F.Schneider
# Journal of Catalysis 383 (2020) 322–330
# https://doi.org/10.1016/j.jcat.2020.01.029

# A factor from Schneider_Pt211 library and scale up by RMG's surface site density of Pd211
# A factor revised from 3.7E17 =6.55E13 base on the models

# Ea = 2.34eV = 225786.6J/mol

# This is reaction (13) in Table S2
# """,
#     metal = "Pd",
#     facet = "211",
# )

# entry(
#     index = 8,
#     label = "NO_X <=> NO + X",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(6.55e+15,'1/s'), n=0, Ea=(241225,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
#     rank = 3,
#     shortDesc = """Surface_Adsorption_Single""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/Ammonia/Schneider_Rh111
# Original entry: NO_X <=> NO + X
# "DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
# Hanyu Ma, and William F.Schneider
# Journal of Catalysis 383 (2020) 322–330
# https://doi.org/10.1016/j.jcat.2020.01.029

# A factor calculated from the equation proposed by Campbell1 et al. (2013)

# Ea = 2.5eV = 241225J/mol

# This is reaction (13) in Table S3
# """,
#     metal = "Rh",
#     facet = "111",
# )

# entry(
#     index = 9,
#     label = "NO_X <=> NO + X",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(2.6e+12,'1/s'), n=0, Ea=(270172,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
#     rank = 3,
#     shortDesc = """Surface_Adsorption_Single""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/Ammonia/Schneider_Rh211
# Original entry: NO_X <=> NO + X
# "DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
# Hanyu Ma, and William F.Schneider
# Journal of Catalysis 383 (2020) 322–330
# https://doi.org/10.1016/j.jcat.2020.01.029

# A factor from Schneider_Pt111 library and revise from 2.6E17 to 2.6E12 base on the model
# Ea = 2.8eV = 270172J/mol

# This is reaction (13) in Table S2
# """,
#     metal = "Rh",
#     facet = "211",
# )

entry(
    index = 10,
    label = "X + NO <=> NO_X",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=1.4917e-06, n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_Single""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/DOC/Arevalo_Pt111
Original entry: NO + X <=> NO_X
"First-principles study of nitric oxide oxidation on Pt(111) versus Pt overlayer on 3d transition metals"
Ryan Lacdao Arevalo, Mary Clare Sison Escaño, and Hideaki Kasai. J. Vac. Sci. Technol. A 33, 021402 (2015)
https://doi.org/10.1116/1.4903225

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = ((2.78E2/bar)/s)*(2.483E-9(mol/cm^2))*sqrt(2*pi*30(g/mol)*molar gas constant*298 kelvin)

This is R3 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 11,
    label = "X + NO2 <=> NO2X",
    degeneracy = 2.0,
    kinetics = StickingCoefficient(A=1.4884e-06, n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_Single""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/DOC/Arevalo_Pt111
Original entry: NO2 + X  <=> NO2_X
"First-principles study of nitric oxide oxidation on Pt(111) versus Pt overlayer on 3d transition metals"
Ryan Lacdao Arevalo, Mary Clare Sison Escaño, and Hideaki Kasai. J. Vac. Sci. Technol. A 33, 021402 (2015)
https://doi.org/10.1116/1.4903225

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = ((2.24E2/bar)/s)*(2.483E-9(mol/cm^2))*sqrt(2*pi*46(g/mol)*molar gas constant*298 kelvin)

This is R7 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 12,
    label = "X + NO <=> NO_X",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.85, n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = """
    Detailed surface reaction mechanism for Pt-catalyzed abatement of automotive exhaust gases
    Deutschmann et al. (2009)
    doi:10.1016/j.apcatb.2009.05.006
    """,
    metal = "Pt",
)

entry(
    index = 13,
    label = "X + NO2 <=> NO2X",
    degeneracy = 2.0,
    kinetics = StickingCoefficient(A=0.9, n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = """
    Detailed surface reaction mechanism for Pt-catalyzed abatement of automotive exhaust gases
    Deutschmann et al. (2009)
    doi:10.1016/j.apcatb.2009.05.006
    """,
    metal = "Pt",
)
