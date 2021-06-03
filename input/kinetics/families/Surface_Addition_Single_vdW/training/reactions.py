#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Addition_Single_vdW/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label = "COOH* + X_5 <=> CO2_2* + H*",
    degeneracy = 2,
    kinetics = SurfaceArrhenius(
        A = (8.028e17, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (28.3644741, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 11 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
2.3626e13 1/s / 2.943e‐5 mol/m^2 = 8.028e17 m^2/(mol*s)
""",
    metal = "Cu",
)

#reverse of 1
# entry(
#     index = 2,
#     label = "CO2_2* + H* <=> COOH* + X_5",
#     degeneracy = 2,
#     kinetics = SurfaceArrhenius(
#         A = (6.25e20, 'm^2/(mol*s)'),
#         n = -0.475,
#         Ea = (117200, 'J/mol'),
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     rank = 10,
#     shortDesc = u"""Default""",
#     longDesc = u"""R45
#     test surface mechanism: based upon Olaf Deutschmann's work:
#     "Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
#     Delgado et al
#     Catalysts, 2015, 5, 871-904""",
# 	  metal = "Ni",
# )

entry(
    index = 3,
    label = "CO2* + H* <=> HCOO* + X_5",
    degeneracy = 2,
    kinetics = SurfaceArrhenius(
        A = (1.243e18, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (20.0626768, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 17 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
3.658e13 1/s / 2.943e‐5 mol/m^2 = 1.243e18 m^2/(mol*s)
""", 
    metal = "Cu",
)

entry(
    index = 4,
    label = "HCOOH* + H* <=> CH3O2_2* + X_5",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (2.122e19, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (23.9829699, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 20 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
6.244e14 1/s / 2.943e‐5 mol/m^2 = 2.122e19 m^2/(mol*s)
""", 
    metal = "Cu",
)

entry(
    index = 5,
    label = "CH3O2* + X_5 <=> CH2O* + OH*",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (3.401e17, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (17.0648055, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 23 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
1.001e13 1/s / 2.943e‐5 mol/m^2 = 3.401e17 m^2/(mol*s)
""", 
    metal = "Cu",
)

entry(
    index = 6,
    label = "CH2O* + H* <=> CH3O_1* + X_5",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (6.167e17, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (5.53453152, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 24 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
1.815e13 1/s / 2.943e‐5 mol/m^2 = 6.167e17 m^2/(mol*s)
""", 
    metal = "Cu",
)

entry(
    index = 7,
    label = "CH2O_2* + H* <=> CH2OH* + X_5",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (3.234e19, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (18.9096494, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 31 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
9.518e14 1/s / 2.943e‐5 mol/m^2 = 3.234e19 m^2/(mol*s)
""", 
    metal = "Cu",
)

entry(
    index = 8,
    label = "CH3O_5* + CH2O* <=> H2COOCH3* + X_5",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (2.176e18, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (2.99787124, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 47 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
6.405e13 1/s / 2.943e‐5 mol/m^2 = 2.176e18 m^2/(mol*s)
""", 
    metal = "Cu",
)

entry(
    index = 9,
    label = "HCOOCH3* + H* <=> H2COOCH3_2* + X_5",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (5.219e16, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (21.6769151, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 48 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
1.536e12 1/s / 2.943e‐5 mol/m^2 = 5.219e16 m^2/(mol*s)
""", 
    metal = "Cu",
)

entry(
    index = 10,
    label = "X_5 + CH3O_1* <=> CH2O* + H*",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(5.03e19,'cm^2/(mol*s)'), n=0.192, Ea=(0,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Addition_Single_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Pt111
Original entry: CH3O_X + X <=> CH2O_X + H_X
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1.25E11(1/s)/2.483E-9(mol/cm^2) = 5.03E19 cm^2/(mol*s)

This is R95 in Table 2
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 11,
    label = "X_5 + CH2OH* <=> CH2O_2* + H*",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.59e19,'cm^2/(mol*s)'), n=-0.104, Ea=(7.9,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Addition_Single_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Pt111
Original entry: CH2OH_X + X <=> CH2O_X + H_X
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1.14E11(1/s)/2.483E-9(mol/cm^2) = 4.59E19 cm^2/(mol*s)

This is R103 in Table 2
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 12,
    label = "X_5 + COOH* <=> CO2_2* + H*",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.02e18,'cm^2/(mol*s)'), n=-0.4424, Ea=(7.6,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Addition_Single_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Rh
Original entry: COOH_X + X <=> CO2_X + H_X
"Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
Vlachos et al. (2008)
Journal of Catalysis,259(2), 211-222, 0021-9517
DOI: 10.1016/j.jcat.2008.08.008.D.G.

Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
A = 1.00E+10(1/s)/2.49E-9(mol/cm^2) = 4.02E+18 cm^2/(mol*s)

This is R33 in Table 4
""",
    metal = "Rh",
)

entry(
    index = 13,
    label = "X_5 + COOH* <=> CO2_2* + H*",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.27e19,'cm^2/(mol*s)'), n=0.549, Ea=(1,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Addition_Single_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Pt111
Original entry: COOH_X + X <=> CO2_X + H_X
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1.06E11(1/s)/2.483E-9(mol/cm^2) = 4.27E19 cm^2/(mol*s)

This is R31 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 14,
    label = "H* + CO2_2* <=> COOH* + X_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(4e+19,'cm^2/(mol*s)'), n=0, Ea=(1.3,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Addition_Single_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Mhadeshwar_Pt111
Original entry: CO2_X + H_X <=> COOH_X + X
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R32 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 15,
    label = "X_5 + HN2X <=> N2X + H*",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.87e21,'cm^2/(mol*s)'), n=0, Ea=(126402,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Addition_Single_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Ir111
Original entry: N2H_X + X <=> N2_X + H_X
"Mechanistic study of hydrazine decomposition on Ir(111)"
Alberto Roldan et al. Phys.Chem.Chem.Phys., 2020, 22, 3883
DOI: 10.1039/c9cp06525c

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2)
to estimate a default(1E13) A factor.
A = 1E13(1/s)/2.587E-9(mol/cm^2) = 3.87E21 cm^2/(mol*s)
Ea = 1.31eV = 126401.9J/mol

This is R10 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

