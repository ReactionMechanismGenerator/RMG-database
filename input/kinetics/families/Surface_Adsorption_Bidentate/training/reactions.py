#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_Bidentate/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "X + X-2 + CHO2 <=> CHO2X2",
    degeneracy = 2.0,
    kinetics = StickingCoefficient(A=0.146, n=0.201, Ea=(0,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_Bidentate""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Pt111
Original entry: HCOO + X + X <=> HCOO_XX
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This is R39 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 2,
    label = "N2X2 <=> N2 + X + X-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.68e+16,'1/s'), n=0, Ea=(10807,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_Bidentate""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Ir111
Original entry: N2_X <=> N2 + X + X
"Kinetic and mechanistic analysis of NH3 decomposition 
on Ru(0001), Ru(111) and Ir(111) surfaces"
Alberto Roldan et al. Nanoscale Adv., 2021, 3, 1624
DOI: 10.1039/d1na00015b

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2) to calculate the A factor.
A = 9.52E7(mol/cm^2/s)/2.587E-9(mol/cm^2) = 3.68E16 (1/s)
Ea was calculated from A factor and k rate constant in Table 3

This is D2 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

