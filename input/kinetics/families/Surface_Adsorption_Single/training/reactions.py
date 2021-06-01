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
    facet="111"
)

entry(
    index = 2,
    label = "NO_X <=> NO + X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.41e16,'1/s'), n=0, Ea=(154800,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_Single""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Krahnert_Pt111
Original entry: NO_X <=> NO + X
"Ammonia Oxidation over Polycrystalline Platinum: 
Surface Morphology and Kinetics at Atmospheric Pressure."
Krähnert, Ralph(2005) A Doctoral Thesis.
http://dx.doi.org/10.14279/depositonce-1270

A = k/exp(Ea/RT) = 1.24(1/s)/exp(154800J/mol / 8.314J/molK / 658K) = 2.41E16 (1/s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 3,
    label = "X + NO <=> NO_X",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=1.4917e-06, n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_Single""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Arevalo_Pt111
Original entry: NO + X <=> NO_X
"First-principles study of nitric oxide oxidation on Pt(111) versus Pt overlayer on 3d transition metals"
Ryan Lacdao Arevalo, Mary Clare Sison Escaño, and Hideaki Kasai. J. Vac. Sci. Technol. A 33, 021402 (2015)
https://doi.org/10.1116/1.4903225

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = ((2.78E2 /bar) / s) * (2.483E-9 mol/cm2) * sqrt(2 * pi * 30 g/mol * molar gas constant * 298 kelvin)

This is R3 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 4,
    label = "X + NO2 <=> NO2X",
    degeneracy = 2.0,
    kinetics = StickingCoefficient(A=1.4884e-06, n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_Single""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Arevalo_Pt111
Original entry: NO2 + X  <=> NO2_X
"First-principles study of nitric oxide oxidation on Pt(111) versus Pt overlayer on 3d transition metals"
Ryan Lacdao Arevalo, Mary Clare Sison Escaño, and Hideaki Kasai. J. Vac. Sci. Technol. A 33, 021402 (2015)
https://doi.org/10.1116/1.4903225

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = ((2.24E2 /bar) / s) * (2.483E-9 mol/cm2) * sqrt(2 * pi * 46 g/mol * molar gas constant * 298 kelvin)

This is R7 in Table 1
""",
    metal = "Pt",
    facet = "111",
)
# entry(
#     index = 2,
#     label = "NO_X <=> NO + Pt",
#     degeneracy = 1,
#     kinetics = SurfaceArrhenius(
#         A=(1.9864e+20, 'm^2/(mol*s)'),
#         n = 0.,
#         Ea = (163.0, 'kJ/mol'),
#         Tmin = (298, 'K'),
#         Tmax = (2000, 'K'),
#     ),
#     rank = 9,
#     shortDesc = u"""NO desorption""",
#     longDesc = u"""
#     Reaction 12 in "Modeling ammonia oxidation over a Pt (533) surface"
#     https://doi.org/10.1016/j.susc.2011.08.014

#     A factor from paper / surface site density of Pt
#     8e14 1/s / 2.483e05 mol/m^2 = 1.9864e+20 m^2/(mol*s)
#     """,
#     metal="Pt",
#     facet="533"
# )

entry(
    index = 5,
    label = "NO_X <=> NO + X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.03e24,'1/s'), n=0, Ea=(140000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
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
    index = 6,
    label = "X + NO <=> NO_X",
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
    index = 7,
    label = "NO2X <=> NO2 + X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(5.24e22,'1/s'), n=0, Ea=(100000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
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

entry(
    index = 8,
    label = "NO_X <=> NO + X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.05e26,'1/s'), n=0, Ea=(184296,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_Single""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pt111
Original entry: NO_X <=> NO + X
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 2.6E17(1/s)/2.483E-9(mol/cm^2) = 1.05E26 cm^2/(mol*s)
Ea = 1.91eV = 184295.9J/mol

This is R13 in Table S2 and S4
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 9,
    label = "NO_X <=> NO + X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.94e25,'1/s'), n=0, Ea=(224822,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_Single""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pt211
Original entry: NO_X <=> NO + X
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt211 = 2.634E-9(mol/cm^2) to calculate the A factor.
A = 1.3E17(1/s)/2.634E-9(mol/cm^2) = 4.94E25 cm^2/(mol*s)
Ea = 2.33eV = 224821.7J/mol

This is R13 in Table S2 and S4
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 10,
    label = "X + HO <=> HOX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.999, n=2, Ea=(0,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_Single""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Pt111
Original entry: OH + X <=> OH_X
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This is R19 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 11,
    label = "X + H <=> HX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.384, n=1.832, Ea=(0,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_Single""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Pt111
Original entry: H + X <=> H_X
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This is R23 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 12,
    label = "X + CH <=> CHX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.0135, n=0.051, Ea=(0,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_Single""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Pt111
Original entry: CH + X <=> CH_X
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This is R49 in Table 2
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 13,
    label = "X + CH3 <=> CH3X",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.16, n=-0.099, Ea=(0,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_Single""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Pt111
Original entry: CH3 + X <=> CH3_X
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This is R53 in Table 2
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 14,
    label = "X + CH3O <=> CH3OX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.149, n=0.054, Ea=(0,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_Single""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Pt111
Original entry: CH3O + X <=> CH3O_X
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This is R85 in Table 2
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 15,
    label = "X + CHO <=> CHOX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.0114, n=0.096, Ea=(0,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_Single""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Pt111
Original entry: HCO + X <=> HCO_X
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This is R89 in Table 2
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 16,
    label = "X + CH3O-2 <=> CH3OX-2",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.0526, n=0.233, Ea=(0,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_Single""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Pt111
Original entry: CH2OH + X <=> CH2OH_X
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This is R91 in Table 2
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 17,
    label = "X + CHO2 <=> CHO2X",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.0634, n=-0.089, Ea=(0,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_Single""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Pt111
Original entry: COOH + X <=> COOH_X
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This is R27 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

