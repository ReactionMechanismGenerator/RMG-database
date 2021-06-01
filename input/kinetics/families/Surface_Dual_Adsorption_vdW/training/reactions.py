#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dual_Adsorption_vdW/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label = "COOH* + OH* <=> CO2* + H2O*",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (3.398e17, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (0., 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 12 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/c s200055d

A factor from paper / surface site density of Cu
1.0e13 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 3.398e17 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 2,
    label = "H2NX + H3N2X <=> H2N2X + H3NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.87e21,'cm^2/(mol*s)'), n=0, Ea=(22192.7,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dual_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Ir111
Original entry: N2H3_X + NH2_X <=> N2H2_X + NH3_X
"Mechanistic study of hydrazine decomposition on Ir(111)"
Alberto Roldan et al. Phys.Chem.Chem.Phys., 2020, 22, 3883
DOI: 10.1039/c9cp06525c

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2)
to estimate a default(1E13) A factor.
A = 1E13(1/s)/2.587E-9(mol/cm^2) = 3.87E21 cm^2/(mol*s)
Ea = 0.23eV = 22192.7J/mol

This is R17 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 3,
    label = "H2O* + CO2* <=> COOH* + OH*",
    degeneracy = 4.0,
    kinetics = SurfaceArrhenius(A=(7.15e20,'cm^2/(mol*s)'), n=-0.1992, Ea=(13.1,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dual_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Rh
Original entry: CO2_X + H2O_X <=> COOH_X + OH_X
"Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
Vlachos et al. (2008)
Journal of Catalysis,259(2), 211-222, 0021-9517
DOI: 10.1016/j.jcat.2008.08.008.D.G.

Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
A = 1.78E+12(1/s)/2.49E-9(mol/cm^2) = 7.15E+20 cm^2/(mol*s)

This is R39 in Table 4
""",
    metal = "Rh",
)

entry(
    index = 4,
    label = "H2O* + CO2* <=> COOH* + OH*",
    degeneracy = 4.0,
    kinetics = SurfaceArrhenius(A=(3.48e19,'cm^2/(mol*s)'), n=-0.031, Ea=(17.5,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dual_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Pt111
Original entry: CO2_X + H2O_X <=> COOH_X + OH_X
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 8.64E10(1/s)/2.483E-9(mol/cm^2) = 3.48E19 cm^2/(mol*s)

This is R37 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 5,
    label = "OH* + COOH* <=> CO2* + H2O*",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4e+19,'cm^2/(mol*s)'), n=0, Ea=(12.4,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dual_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Mhadeshwar_Pt111
Original entry: COOH_X + OH_X <=> CO2_X + H2O_X
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R38 in Appendix A

This reaction is the least important ones for typical DOC conditions.
""",
    metal = "Pt",
    facet = "111",
)

