#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_Abstraction_vdW/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label = "HCOOH* + HCO* <=> CH3O2* + CO*",
    kinetics = SurfaceArrhenius(
        A = (1.814e16, 'm^2/(mol*s)'),
        n = 0,
        Ea = (0.42, 'eV/molecule'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 43 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
5.34e11 1/s / 2.943e‐5 mol/m^2 = 1.814e16 m^2/(mol*s)
""", #Ting-Chen: I think the unit of the A factor in the paper is 1/s rather than m^4/(mol^2 * s)
    metal = "Cu",
)

entry(
    index = 2,
    label = "CH2O* + HCO* <=> CH3O* + CO*",
    kinetics = SurfaceArrhenius(
        A = (3.398e17, 'm^2/(mol*s)'),
        n = 0,
        Ea = (0.0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 44 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
1.0e13 1/s / 2.943e‐5 mol/m^2 = 3.398e17 m^2/(mol*s)
""", #Ting-Chen: I think the unit of the A factor in the paper is 1/s rather than m^4/(mol^2 * s)
    metal = "Cu",
)

entry(
    index = 3,
    label = "HOX + CO2X <=> CHO2X + OX",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.15e19,'cm^2/(mol*s)'), n=0.097, Ea=(26.5,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Pt111
Original entry: CO2_X + OH_X <=> COOH_X + O_X
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 5.35E10(1/s)/2.483E-9(mol/cm^2) = 2.15E19 cm^2/(mol*s)

This is R35 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

