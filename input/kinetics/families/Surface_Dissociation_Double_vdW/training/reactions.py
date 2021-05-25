#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_Double_vdW/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 9,
    label = "CO* + O* <=> CO2* + X_4",
    degeneracy = 2,
    kinetics = SurfaceArrhenius(
        A = (4.060e16, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (0.65, 'eV/molecule'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 9 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
1.195e12 1/s / 2.943e‐5 mol/m^2 = 4.060e16 m^2/(mol*s)
Erxn= -1.12 eV
""",
    metal = "Cu",
)

# duplicate of 9
# entry(
#     index = 42,
#     label = "CO2* + X_4 <=> CO* + O*",
#     kinetics = SurfaceArrhenius(
#         A = (4.64E19, 'm^2/(mol*s)'),
#         n = -1.0,
#         Ea = (89300.0, 'J/mol'),
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     rank = 10,
#     shortDesc = u"""Default""",
#     longDesc = u"""R42
#     test surface mechanism: based upon Olaf Deutschmann's work:
#     "Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
#     Delgado et al
#     Catalysts, 2015, 5, 871-904""",
# 	  metal = "Ni",
# )

entry(
    index = 35,
    label = "HCOOH* + X_4 <=> HCOH* + O*",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (1.641e16, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (2.50, 'eV/molecule'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 35 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
4.828e11 1/s / 2.943e‐5 mol/m^2 = 1.641e16 m^2/(mol*s)
Erxn = 2.04 eV
""",
    metal = "Cu",
)

entry(
    index = 36,
    label = "X_4 + N2OX <=> O* + N2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(9.12e+19,'cm^2/(mol*s)'), n=1.004, Ea=(63657,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Addition_Single_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ishikawa_Rh111
Original entry: N2O_X + X <=> N2_X + O_X
"First-Principles Microkinetic Analysis of NO + CO Reactions on
Rh(111) Surface toward Understanding NOx Reduction Pathways"
Atsushi Ishikawa and Yoshitaka Tateyama
J. Phys. Chem. C 2018, 122, 30, 17378–17388
https://doi.org/10.1021/acs.jpcc.8b05906

This reaction used RMG's surface site density of Rh111 = 2.656E-09(mol/cm^2) to calculate the A factor.
The modified Arrhenius parameters is calculed from 
Table 2. Activation Energy (Ea) 
and 
Table S3. Reaction rate constant at different temperatures
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 37,
    label = "CO* + O* <=> CO2* + X_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.73e+20,'cm^2/(mol*s)'), n=1.001, Ea=(119598,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_Double_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ishikawa_Rh111
Original entry: CO_X + O_X <=> CO2_X + X
"First-Principles Microkinetic Analysis of NO + CO Reactions on
Rh(111) Surface toward Understanding NOx Reduction Pathways"
Atsushi Ishikawa and Yoshitaka Tateyama
J. Phys. Chem. C 2018, 122, 30, 17378–17388
https://doi.org/10.1021/acs.jpcc.8b05906

This reaction used RMG's surface site density of Rh111 = 2.656E-09(mol/cm^2) to calculate the A factor.
The modified Arrhenius parameters is calculed from 
Table 2. Activation Energy (Ea) 
and 
Table S3. Reaction rate constant at different temperatures
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 38,
    label = "HNX + O* <=> HNOX + X_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.03e+21,'cm^2/(mol*s)'), n=0, Ea=(73000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_Double_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Rebrov_Pt111
Original entry: NH_X + O_X <=> NHO_X + X
"Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
https://doi.org/10.1016/S1385-8947(02)00068-2

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1E13(1/s)/2.483E-9(mol/cm^2) = 4.03E21 cm^2/(mol*s)

This is R9 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 39,
    label = "X_4 + N2OX <=> O* + N2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.01e+17,'cm^2/(mol*s)'), n=0, Ea=(72200,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Addition_Single_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Rebrov_Pt111
Original entry: N2O_X + X <=> N2_X + O_X
"Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
https://doi.org/10.1016/S1385-8947(02)00068-2

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 2.5E8(1/s)/2.483E-9(mol/cm^2) = 1.01E17 cm^2/(mol*s)

This is R14 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 40,
    label = "X_4 + CO2* <=> O* + CO*",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(1.68e+19,'cm^2/(mol*s)'), n=0.177, Ea=(26.3,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_Double_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Pt111
Original entry: CO2_X + X <=> CO_X + O_X
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 4.18E10(1/s)/2.483E-9(mol/cm^2) = 1.68E19 cm^2/(mol*s)

This is R9 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 41,
    label = "X_4 + H2N2X <=> HNX-2 + HNX",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(3.87e+21,'cm^2/(mol*s)'), n=0, Ea=(70437.7,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_Double_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Ir111
Original entry: N2H2_X + X <=> NH_X + NH_X
"Mechanistic study of hydrazine decomposition on Ir(111)"
Alberto Roldan et al. Phys.Chem.Chem.Phys., 2020, 22, 3883
DOI: 10.1039/c9cp06525c

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2)
to estimate a default(1E13) A factor.
A = 1E13(1/s)/2.587E-9(mol/cm^2) = 3.87E21 cm^2/(mol*s)
Ea = 0.73eV = 70437.7J/mol

This is R14 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

