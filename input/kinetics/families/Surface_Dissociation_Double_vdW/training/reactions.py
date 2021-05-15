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
        Ea = (14.9893562, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 9 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
1.195e12 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 4.060e16 m^2/(mol*s)
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
        Ea = (57.65137, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 35 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
4.828e11 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 1.641e16 m^2/(mol*s)
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

