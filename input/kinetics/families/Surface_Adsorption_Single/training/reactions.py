#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_Single/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 48,
    label = "NO + Pt <=> NO_X",
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

entry(
    index = 49,
    label = "NO_X <=> NO + Pt",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.19e+17,'1/s'), n=0, Ea=(154800,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_Single""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ralph_Pt111
Original entry: NO_X <=> NO + X
"Ammonia Oxidation over Polycrystalline Platinum: 
Surface Morphology and Kinetics at Atmospheric Pressure."
Krähnert, Ralph(2005) A Doctoral Thesis.
http://dx.doi.org/10.14279/depositonce-1270

A = k/exp(Ea/RT) = 1.24(mol/m^2/s)/exp(154800J/mol / 8.314J/molK / 298K) = 3.19E17 cm^2/mol/s
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 50,
    label = "Pt + NO <=> NO_X",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=1.4917e-06, n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_Single""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ryan_Pt111
Original entry: NO + X <=> NO_X
"First-principles study of nitric oxide oxidation on Pt(111) versus Pt overlayer on 3d transition metals"
Ryan Lacdao Arevalo, Mary Clare Sison Escaño, and Hideaki Kasai. J. Vac. Sci. Technol. A 33, 021402 (2015)
https://doi.org/10.1116/1.4903225

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = ((2.78E2 /bar) / s) * (2.483E-9 mol/cm2) * sqrt(2 * pi * 30 g/mol * molar gas constant * 298 kelvin)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 51,
    label = "Pt + NO2 <=> NO2X",
    degeneracy = 2.0,
    kinetics = StickingCoefficient(A=1.4884e-06, n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ryan_Pt111
Original entry: NO2 + X  <=> NO2_X
"First-principles study of nitric oxide oxidation on Pt(111) versus Pt overlayer on 3d transition metals"
Ryan Lacdao Arevalo, Mary Clare Sison Escaño, and Hideaki Kasai. J. Vac. Sci. Technol. A 33, 021402 (2015)
https://doi.org/10.1116/1.4903225

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = ((2.24E2 /bar) / s) * (2.483E-9 mol/cm2) * sqrt(2 * pi * 46 g/mol * molar gas constant * 298 kelvin)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 52,
    label = "NO_X <=> NO + Pt",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.03e+24,'1/s'), n=0, Ea=(140000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_Single""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Rebrov_Pt111
Original entry: NO_X <=> NO + X
"Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
https://doi.org/10.1016/S1385-8947(02)00068-2

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1E16(1/s)/2.483E-9(mol/cm^2) = 4.03E24 cm^2/(mol*s)

This is R15 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 53,
    label = "Pt + NO <=> NO_X",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.1556, n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_Single""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Scheuer_Pt
Original entry: NO + X <=> NO_X
"Dual layer automotive ammonia oxidation catalysts: Experiments and computer simulation"
Scheuer et al. Applied Catalysis B: Environmental 111–112 (2012) 445–455
https://doi.org/10.1016/j.apcatb.2011.10.032

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = ((290/Pa)/s)*(2.483e-9(mol/cm^2))*sqrt(2*pi*(30(g/mol))*the molar gas constant*(298 kelvin)) = 0.1556

This is R7 in Table 1
""",
    metal = "Pt",
)

entry(
    index = 54,
    label = "NO2X <=> NO2 + Pt",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(5.24e+22,'1/s'), n=0, Ea=(100000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_Single""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Scheuer_Pt
Original entry: NO2_X <=> NO2 + X
"Dual layer automotive ammonia oxidation catalysts: Experiments and computer simulation"
Scheuer et al. Applied Catalysis B: Environmental 111–112 (2012) 445–455
https://doi.org/10.1016/j.apcatb.2011.10.032

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1.3E14(mol/cm^2/s)/2.483E-9(mol/cm^2) = 5.24E22 (1/s)

This is R13 in Table 1
""",
    metal = "Pt",
)

