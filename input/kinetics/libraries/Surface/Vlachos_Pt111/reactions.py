#!/usr/bin/env python
# encoding: utf-8

name = "Vlachos_Pt111"
shortDesc = u""
longDesc = u"""
Primarily based on:
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c
"""

entry(
    index = 1,
    label = "O2 + X + X <=> O_X + O_X",
    kinetics = StickingCoefficient(
        A = 0.0542,
        n = 0.766,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""O2 Surface_Adsorption_Dissociative""",
    longDesc = u"""
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This is R1 in Table 1
""",
	metal = "Pt",
    facet = "111",
)

# entry(
#     index = 2,
#     label = "O_X + O_X <=> O2 + X + X",
#     kinetics = SurfaceArrhenius(
#         A = (3.39E21, 'cm^2/(mol*s)'),  
#         n = -0.796,
#         Ea = (50.9, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""O2 Surface_Adsorption_Dissociative""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = 8.41E12(1/s)/2.483E-9(mol/cm^2) = 3.39E21 cm^2/(mol*s)

# This is R2 in Table 1
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 3,
    label = "O + X <=> O_X",
    kinetics = StickingCoefficient(
        A = 0.0491,
        n = 0.250,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Double""",
    longDesc = u"""
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This is R3 in Table 1
""",
	metal = "Pt",
    facet = "111",
)

# entry(
#     index = 4,
#     label = "O_X <=> O + X",
#     kinetics = SurfaceArrhenius(
#         A = (1.44E13, '1/s'),  
#         n = -0.250,
#         Ea = (85.0, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_Double""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This is R4 in Table 1
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 5,
    label = "CO + X <=> CO_X",
    kinetics = StickingCoefficient(
        A = 1,
        n = 0,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Double""",
    longDesc = u"""
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This is R5 in Table 1
""",
	metal = "Pt",
    facet = "111",
)

# entry(
#     index = 6,
#     label = "CO_X <=> CO + X",
#     kinetics = SurfaceArrhenius(
#         A = (5.66E15, '1/s'),  
#         n = -0.500,
#         Ea = (40, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_Double""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This is R6 in Table 1
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 7,
    label = "CO2 + X <=> CO2_X",
    kinetics = StickingCoefficient(
        A = 0.195,
        n = 0.250,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This is R7 in Table 1
""",
	metal = "Pt",
    facet = "111",
)

# entry(
#     index = 8,
#     label = "CO2_X <=> CO2 + X",
#     kinetics = SurfaceArrhenius(
#         A = (3.63E12, '1/s'),  
#         n = -0.250,
#         Ea = (3.6, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_vdW""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This is R8 in Table 1
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 9,
    label = "CO2_X + X <=> CO_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (1.68E19, 'cm^2/(mol*s)'),  
        n = 0.177,
        Ea = (26.3, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_Double_vdW""",
    longDesc = u"""
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

# entry(
#     index = 10,
#     label = "CO_X + O_X <=> CO2_X + X",
#     kinetics = SurfaceArrhenius(
#         A = (9.63E19, 'cm^2/(mol*s)'),  
#         n = -0.177,
#         Ea = (20.6, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Dissociation_Double_vdW""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = 2.39E11(1/s)/2.483E-9(mol/cm^2) = 9.63E19 cm^2/(mol*s)

# This is R10 in Table 1
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 11,
    label = "H2 + X + X <=> H_X + H_X",
    kinetics = StickingCoefficient(
        A = 0.129,
        n = 0.858,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""H2 Surface_Adsorption_Dissociative""",
    longDesc = u"""
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This is R11 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

# entry(
#     index = 12,
#     label = "H_X + H_X <=> H2 + X + X",
#     kinetics = SurfaceArrhenius(
#         A = (3.20E21, 'cm^2/(mol*s)'),  
#         n = -0.001,
#         Ea = (19.8, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""H2 Surface_Adsorption_Dissociative""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = 7.95E12(1/s)/2.483E-9(mol/cm^2) = 3.20E21 cm^2/(mol*s)

# This is R12 in Table 1
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
    index = 13,
    label = "OH_X + X <=> H_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (7.85E20, 'cm^2/(mol*s)'), 
        n = 1.872,
        Ea = (27.1, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1.95E12(1/s)/2.483E-9(mol/cm^2) = 7.85E20 cm^2/(mol*s)

This is R13 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

# entry(
#    index = 14,
#    label = "H_X + O_X <=> OH_X + X",
#    kinetics = SurfaceArrhenius(
#        A = (2.55E21, 'cm^2/(mol*s)'), 
#        n = 0.624,
#        Ea = (8.8, 'kcal/mol'),
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""Surface_Dissociation""",
#    longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = 6.33E12(1/s)/2.483E-9(mol/cm^2) = 2.55E21 cm^2/(mol*s)

# This is R14 in Table 1
# """,
#    metal = "Pt",
#    facet = "111",
# )

entry(
   index = 15,
   label = "H2O_X + X <=> H_X + OH_X",
   kinetics = SurfaceArrhenius(
       A = (3.77E21, 'cm^2/(mol*s)'), 
       n = -0.118,
       Ea = (17.8, 'kcal/mol'),
       Tmin = (200, 'K'),
       Tmax = (3000, 'K'),
   ),
   shortDesc = u"""Surface_Dissociation_vdW""",
   longDesc = u"""
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 9.36E12(1/s)/2.483E-9(mol/cm^2) = 3.77E21 cm^2/(mol*s)

This is R15 in Table 1
""",
   metal = "Pt",
   facet = "111",
)

# entry(
#     index = 16,
#     label = "H_X + OH_X <=> H2O_X + X",
#     kinetics = SurfaceArrhenius(
#         A = (4.02E21, 'cm^2/(mol*s)'), 
#         n = -1.049,
#         Ea = (13.5, 'kcal/mol'),
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Dissociation_vdW""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = 9.99E12(1/s)/2.483E-9(mol/cm^2) = 4.02E21 cm^2/(mol*s)

# This is R16 in Table 1
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
    index = 17,
    label = "O_X + H2O_X <=> OH_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (1.74E19, 'cm^2/(mol*s)'),  
        n = 0.082,
        Ea = (8.8, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 4.32E10(1/s)/2.483E-9(mol/cm^2) = 1.74E19 cm^2/(mol*s)

This is R17 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

# entry(
#     index = 18,
#     label = "OH_X + OH_X <=> O_X + H2O_X",
#     kinetics = SurfaceArrhenius(
#         A = (6.85E18, 'cm^2/(mol*s)'),  
#         n = 0.325,
#         Ea = (22.7, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Abstraction_vdW""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = 1.70E10(1/s)/2.483E-9(mol/cm^2) = 6.85E18 cm^2/(mol*s)

# This is R18 in Table 1
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
    index = 19,
    label = "OH + X <=> OH_X",
    kinetics = StickingCoefficient(
        A = 0.999,
        n = 2.000,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""
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

# entry(
#     index = 20,
#     label = "OH_X <=> OH + X",
#     kinetics = SurfaceArrhenius(
#         A = (1.44E14, '1/s'),  
#         n = 2.000,
#         Ea = (63.0, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_Single""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This is R20 in Table 1
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 21,
    label = "H2O + X <=> H2O_X",
    kinetics = StickingCoefficient(
        A = 0.108,
        n = 1.162,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This is R21 in Table 1
""",
	metal = "Pt",
    facet = "111",
)

# entry(
#     index = 22,
#     label = "H2O_X <=> H2O + X",
#     kinetics = SurfaceArrhenius(
#         A = (2.03E12, '1/s'),  
#         n = 1.372,
#         Ea = (10, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_vdW""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This is R22 in Table 1
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 23,
    label = "H + X <=> H_X",
    kinetics = StickingCoefficient(
        A = 0.384,
        n = 1.832,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""
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

# entry(
#     index = 24,
#     label = "H_X <=> H + X",
#     kinetics = SurfaceArrhenius(
#         A = (4.37E13, '1/s'),  
#         n = 1.890,
#         Ea = (62.0, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_Single""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This is R24 in Table 1
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 25,
    label = "CO2_X + H_X <=> CO_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (3.23E17, 'cm^2/(mol*s)'),  
        n = -0.531,
        Ea = (6.0, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Deutschmann_Pt/19""",
    longDesc = u"""
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 8.03E08(1/s)/2.483E-9(mol/cm^2) = 3.23E17 cm^2/(mol*s)

This is R25 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

# entry(
#     index = 26,
#     label = "CO_X + OH_X <=> CO2_X + H_X",
#     kinetics = SurfaceArrhenius(
#         A = (5.03E17, 'cm^2/(mol*s)'),  
#         n = 0.531,
#         Ea = (18.5, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Deutschmann_Pt/19""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = 1.25E09(1/s)/2.483E-9(mol/cm^2) = 5.03E17 cm^2/(mol*s)

# This is R26 in Table 1
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
    index = 27,
    label = "COOH + X <=> COOH_X",
    kinetics = StickingCoefficient(
        A = 0.0634,
        n = -0.089,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""
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

# entry(
#     index = 28,
#     label = "COOH_X <=> COOH + X",
#     kinetics = SurfaceArrhenius(
#         A = (1.12E13, '1/s'),  
#         n = 0.089,
#         Ea = (55.3, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_Single""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This is R28 in Table 1
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 29,
    label = "COOH_X + X <=> CO_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (3.40E17, 'cm^2/(mol*s)'),  
        n = 0.024,
        Ea = (5.3, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 8.43E08(1/s)/2.483E-9(mol/cm^2) = 3.40E17 cm^2/(mol*s)

This is R29 in Table 1
""",
	metal = "Pt",
    facet = "111",
)

# entry(
#     index = 30,
#     label = "CO_X + OH_X <=> COOH_X + X",
#     kinetics = SurfaceArrhenius(
#         A = (4.79E17, 'cm^2/(mol*s)'),  
#         n = -0.024,
#         Ea = (19.1, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Dissociation""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = 1.19E09(1/s)/2.483E-9(mol/cm^2) = 4.79E17 cm^2/(mol*s)

# This is R30 in Table 1
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 31,
    label = "COOH_X + X <=> CO2_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (4.27E19, 'cm^2/(mol*s)'),  
        n = 0.549,
        Ea = (1.0, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Addition_Single_vdW""",
    longDesc = u"""
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

# entry(
#     index = 32,
#     label = "CO2_X + H_X <=> COOH_X + X",
#     kinetics = SurfaceArrhenius(
#         A = (3.81E19, 'cm^2/(mol*s)'),  
#         n = -0.549,
#         Ea = (2.4, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Addition_Single_vdW""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = 9.45E10(1/s)/2.483E-9(mol/cm^2) = 3.81E19 cm^2/(mol*s)

# This is R32 in Table 1
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 33,
    label = "CO_X + H2O_X <=> COOH_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (4.43E19, 'cm^2/(mol*s)'),  
        n = 0.492,
        Ea = (23.7, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1.10E11(1/s)/2.483E-9(mol/cm^2) = 4.43E19 cm^2/(mol*s)

This is R33 in Table 1
""",
	metal = "Pt",
    facet = "111",
)

# entry(
#     index = 34,
#     label = "COOH_X + H_X <=> CO_X + H2O_X",
#     kinetics = SurfaceArrhenius(
#         A = (3.65E19, 'cm^2/(mol*s)'),  
#         n = -0.492,
#         Ea = (5.6, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Abstraction_vdW""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = 9.07E10(1/s)/2.483E-9(mol/cm^2) = 3.65E19 cm^2/(mol*s)

# This is R34 in Table 1
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 35,
    label = "CO2_X + OH_X <=> COOH_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (2.15E19, 'cm^2/(mol*s)'),  
        n = 0.097,
        Ea = (26.5, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Abstraction_vdW""",
    longDesc = u"""
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

# entry(
#     index = 36,
#     label = "COOH_X + O_X <=> CO2_X + OH_X",
#     kinetics = SurfaceArrhenius(
#         A = (7.53E19, 'cm^2/(mol*s)'),  
#         n = -0.097,
#         Ea = (7.0, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_Abstraction_vdW""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = 1.87E11(1/s)/2.483E-9(mol/cm^2) = 7.53E19 cm^2/(mol*s)

# This is R36 in Table 1
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 37,
    label = "CO2_X + H2O_X <=> COOH_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (3.48E19, 'cm^2/(mol*s)'),  
        n = -0.031,
        Ea = (17.5, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dual_Adsorption_vdW""",
    longDesc = u"""
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

# entry(
#     index = 38,
#     label = "COOH_X + OH_X <=> CO2_X + H2O_X",
#     kinetics = SurfaceArrhenius(
#         A = (4.67E19, 'cm^2/(mol*s)'),  
#         n = 0.031,
#         Ea = (11.9, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Dual_Adsorption_vdW""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = 1.16E11(1/s)/2.483E-9(mol/cm^2) = 4.67E19 cm^2/(mol*s)

# This is R38 in Table 1
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 39,
    label = "HCOO + X + X <=> HCOO_XX",
    kinetics = StickingCoefficient(
        A = 0.146,
        n = 0.201,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Bidentate""",
    longDesc = u"""
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

# entry(
#     index = 40,
#     label = "HCOO_XX <=> HCOO + X + X",
#     kinetics = SurfaceArrhenius(
#         A = (4.83E12, '1/s'),  
#         n = -0.201,
#         Ea = (53.0, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_Bidentate""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This is R40 in Table 1
# """,
#     metal = "Pt",
#     facet = "111",
# )

#R41 in the paper was a bidentate HCOO_XX, which might cause the issue of an adsorbate vdW species.
#This might cause an UndeterminableKineticsError, maybe we don't want to include this reaction.
entry(
    index = 41,
    label = "CO2_X + H_X <=> HCOO_XX",
    kinetics = SurfaceArrhenius(
        A = (4.51E19, 'cm^2/(mol*s)'),  
        n = -0.422,
        Ea = (18.5, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1.12E11(1/s)/2.483E-9(mol/cm^2) = 4.51E19 cm^2/(mol*s)

This is R41 in Table 1
""",
	metal = "Pt",
    facet = "111",
)

#Same issue as R41
# entry(
#     index = 42,
#     label = "HCOO_XX <=> CO2_X + H_X",
#     kinetics = SurfaceArrhenius(
#         A = (3.61E19, 'cm^2/(mol*s)'),  
#         n = 0.422,
#         Ea = (0, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = 8.96E10(1/s)/2.483E-9(mol/cm^2) = 3.61E19 cm^2/(mol*s)

# This is R42 in Table 1
# """,
# 	metal = "Pt",
#     facet = "111",
# )

#R43 in the paper was a bidentate HCOO_XX, which might cause the issue of an adsorbate vdW species.
#This might cause an UndeterminableKineticsError, maybe we don't want to include this reaction.
entry(
    index = 43,
    label = "CO2_X + OH_X + X <=> HCOO_XX + O_X",
    kinetics = SurfaceArrhenius(
        A = (2.48E19, 'cm^4/(mol^2*s)'),  
        n = 0.236,
        Ea = (36.8, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 6.17E10(cm^2/mol/s)/2.483E-9(mol/cm^2) = 2.48E19 cm^4/(mol^2*s)

This is R43 in Table 1
""",
	metal = "Pt",
    facet = "111",
)

#Same issue as R43
# entry(
#     index = 44,
#     label = "HCOO_XX + O_X <=> CO2_X + OH_X + X",
#     kinetics = SurfaceArrhenius(
#         A = (6.52E19, 'cm^2/(mol*s)'),  
#         n = -0.236,
#         Ea = (0, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = 1.62E11(1/s)/2.483E-9(mol/cm^2) = 6.52E19 cm^2/(mol*s)

# This is R44 in Table 1
# """,
# 	metal = "Pt",
#     facet = "111",
# )

#Skip R45 and R46, which might cause a bidentate CO2 with a radical 
# on surface site.(if match Surface_Dissociation family)

entry(
    index = 47,
    label = "C + X <=> C_X",
    kinetics = StickingCoefficient(
        A = 0.0164,
        n = 0.156,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Quadruple bonds""",
    longDesc = u"""
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This is R47 in Table 2
""",
	metal = "Pt",
    facet = "111",
)

# entry(
#     index = 48,
#     label = "C_X <=> C + X",
#     kinetics = SurfaceArrhenius(
#         A = (4.30E13, '1/s'),  
#         n = -0.156,
#         Ea = (157.7, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_Quadruple bonds""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This is R48 in Table 2
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 49,
    label = "CH + X <=> CH_X",
    kinetics = StickingCoefficient(
        A = 0.0135,
        n = 0.051,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""
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

# entry(
#     index = 50,
#     label = "CH_X <=> CH + X",
#     kinetics = SurfaceArrhenius(
#         A = (5.22E13, '1/s'),  
#         n = -0.051,
#         Ea = (157.1, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_Single""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This is R50 in Table 2
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 51,
    label = "CH2 + X <=> CH2_X",
    kinetics = StickingCoefficient(
        A = 0.045,
        n = 0.118,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Double""",
    longDesc = u"""
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This is R51 in Table 2
""",
	metal = "Pt",
    facet = "111",
)

# entry(
#     index = 52,
#     label = "CH2_X <=> CH2 + X",
#     kinetics = SurfaceArrhenius(
#         A = (1.57E13, '1/s'),  
#         n = -0.118,
#         Ea = (91.6, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_Double""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This is R52 in Table 2
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 53,
    label = "CH3 + X <=> CH3_X",
    kinetics = StickingCoefficient(
        A = 0.16,
        n = -0.099,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""
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

# entry(
#     index = 54,
#     label = "CH3_X <=> CH3 + X",
#     kinetics = SurfaceArrhenius(
#         A = (4.42E12, '1/s'),  
#         n = 0.099,
#         Ea = (45.3, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_Single""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This is R54 in Table 2
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 55,
    label = "CH4 + X + X <=> CH3_X + H_X",
    kinetics = StickingCoefficient(
        A = 0.116,
        n = 0.154,
        Ea = (9, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Dissociative""",
    longDesc = u"""
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This is R55 in Table 2
""",
	metal = "Pt",
    facet = "111",
)

# entry(
#     index = 56,
#     label = "CH3_X + H_X <=> CH4 + X + X",
#     kinetics = SurfaceArrhenius(
#         A = (2.46E19, 'cm^2/(mol*s)'),  
#         n = -0.154,
#         Ea = (11.3, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_Dissociative""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = 6.12E10(1/s)/2.483E-9(mol/cm^2) = 2.46E19 cm^2/(mol*s)

# This is R56 in Table 2
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 57,
    label = "CH3_X + X <=> CH2_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (4.47E19, 'cm^2/(mol*s)'),  
        n = 0.419,
        Ea = (15.8, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1.11E11(1/s)/2.483E-9(mol/cm^2) = 4.47E19 cm^2/(mol*s)

This is R57 in Table 2
""",
	metal = "Pt",
    facet = "111",
)

# entry(
#     index = 58,
#     label = "CH2_X + H_X <=> CH3_X + X",
#     kinetics = SurfaceArrhenius(
#         A = (3.62E19, 'cm^2/(mol*s)'),  
#         n = -0.419,
#         Ea = (13.3, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Dissociation""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = 8.99E10(1/s)/2.483E-9(mol/cm^2) = 3.62E19 cm^2/(mol*s)

# This is R58 in Table 2
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 59,
    label = "CH2_X + X <=> CH_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (2.10E19, 'cm^2/(mol*s)'),  
        n = 0.222,
        Ea = (9.0, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 5.22E10(1/s)/2.483E-9(mol/cm^2) = 2.10E19 cm^2/(mol*s)

This is R59 in Table 2
""",
	metal = "Pt",
    facet = "111",
)

# entry(
#     index = 60,
#     label = "CH_X + H_X <=> CH2_X + X",
#     kinetics = SurfaceArrhenius(
#         A = (7.73E19, 'cm^2/(mol*s)'),  
#         n = -0.222,
#         Ea = (35.4, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Dissociation""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = 1.92E11(1/s)/2.483E-9(mol/cm^2) = 7.73E19 cm^2/(mol*s)

# This is R60 in Table 2
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 61,
    label = "CH_X + X <=> C_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (3.67E19, 'cm^2/(mol*s)'),  
        n = 0.398,
        Ea = (31.3, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 9.11E10(1/s)/2.483E-9(mol/cm^2) = 3.67E19 cm^2/(mol*s)

This is R61 in Table 2
""",
	metal = "Pt",
    facet = "111",
)

# entry(
#     index = 62,
#     label = "C_X + H_X <=> CH_X + X",
#     kinetics = SurfaceArrhenius(
#         A = (4.43E19, 'cm^2/(mol*s)'),  
#         n = 0.414,
#         Ea = (44.7, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Dissociation""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = 1.10E11(1/s)/2.483E-9(mol/cm^2) = 4.43E19 cm^2/(mol*s)

# This is R62 in Table 2
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 63,
    label = "CH3_X + O_X <=> CH2_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (7.93E19, 'cm^2/(mol*s)'),  
        n = -0.230,
        Ea = (10.8, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction""",
    longDesc = u"""
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1.97E11(1/s)/2.483E-9(mol/cm^2) = 7.93E19 cm^2/(mol*s)

This is R63 in Table 2
""",
	metal = "Pt",
    facet = "111",
)

# entry(
#     index = 64,
#     label = "CH2_X + OH_X <=> CH3_X + O_X",
#     kinetics = SurfaceArrhenius(
#         A = (2.05E19, 'cm^2/(mol*s)'),  
#         n = 0.230,
#         Ea = (26.6, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Abstraction""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = 5.08E10(1/s)/2.483E-9(mol/cm^2) = 2.05E19 cm^2/(mol*s)

# This is R64 in Table 2
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 65,
    label = "CH_X + OH_X <=> CH2_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (4.43E19, 'cm^2/(mol*s)'),  
        n = 0.414,
        Ea = (44.7, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction""",
    longDesc = u"""
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1.10E11(1/s)/2.483E-9(mol/cm^2) = 4.43E19 cm^2/(mol*s)

This is R65 in Table 2
""",
	metal = "Pt",
    facet = "111",
)

# entry(
#     index = 66,
#     label = "CH2_X + O_X <=> CH_X + OH_X",
#     kinetics = SurfaceArrhenius(
#         A = (3.66E19, 'cm^2/(mol*s)'),  
#         n = -0.414,
#         Ea = (0, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Abstraction""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = 9.10E10(1/s)/2.483E-9(mol/cm^2) = 3.66E19 cm^2/(mol*s)

# This is R66 in Table 2
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 67,
    label = "C_X + OH_X <=> CH_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (2.57E19, 'cm^2/(mol*s)'),  
        n = 0.225,
        Ea = (27.7, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction""",
    longDesc = u"""
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 6.37E10(1/s)/2.483E-9(mol/cm^2) = 2.57E19 cm^2/(mol*s)

This is R67 in Table 2
""",
	metal = "Pt",
    facet = "111",
)

# entry(
#     index = 68,
#     label = "CH_X + O_X <=> C_X + OH_X",
#     kinetics = SurfaceArrhenius(
#         A = (6.32E19, 'cm^2/(mol*s)'),  
#         n = -0.225,
#         Ea = (27.5, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Abstraction""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = 1.57E11(1/s)/2.483E-9(mol/cm^2) = 6.32E19 cm^2/(mol*s)

# This is R68 in Table 2
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 69,
    label = "CH2_X + H2O_X <=> CH3_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (3.30E19, 'cm^2/(mol*s)'),  
        n = 0.099,
        Ea = (14.1, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 8.19E10(1/s)/2.483E-9(mol/cm^2) = 3.30E19 cm^2/(mol*s)

This is R69 in Table 2
""",
	metal = "Pt",
    facet = "111",
)

# entry(
#     index = 70,
#     label = "CH3_X + OH_X <=> CH2_X + H2O_X",
#     kinetics = SurfaceArrhenius(
#         A = (4.91E19, 'cm^2/(mol*s)'),  
#         n = -0.099,
#         Ea = (12.3, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Abstraction_vdW""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = 1.22E11(1/s)/2.483E-9(mol/cm^2) = 4.91E19 cm^2/(mol*s)

# This is R70 in Table 2
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 71,
    label = "CH_X + H2O_X <=> CH2_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (7.29E19, 'cm^2/(mol*s)'),  
        n = 0.269,
        Ea = (34.0, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1.81E11(1/s)/2.483E-9(mol/cm^2) = 7.29E19 cm^2/(mol*s)

This is R71 in Table 2
""",
	metal = "Pt",
    facet = "111",
)

# entry(
#     index = 72,
#     label = "CH2_X + OH_X <=> CH_X + H2O_X",
#     kinetics = SurfaceArrhenius(
#         A = (2.23E19, 'cm^2/(mol*s)'),  
#         n = -0.269,
#         Ea = (3.3, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Abstraction_vdW""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = 5.53E10(1/s)/2.483E-9(mol/cm^2) = 2.23E19 cm^2/(mol*s)

# This is R72 in Table 2
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 73,
    label = "C_X + H2O_X <=> CH_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (4.19E19, 'cm^2/(mol*s)'),  
        n = 0.090,
        Ea = (15.6, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1.04E11(1/s)/2.483E-9(mol/cm^2) = 4.19E19 cm^2/(mol*s)

This is R73 in Table 2
""",
	metal = "Pt",
    facet = "111",
)

# entry(
#     index = 74,
#     label = "CH_X + OH_X <=> C_X + H2O_X",
#     kinetics = SurfaceArrhenius(
#         A = (3.87E19, 'cm^2/(mol*s)'),  
#         n = -0.090,
#         Ea = (29.3, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Abstraction_vdW""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = 9.61E10(1/s)/2.483E-9(mol/cm^2) = 3.87E19 cm^2/(mol*s)

# This is R74 in Table 2
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 75,
    label = "CO_X + X <=> C_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (1.15E20, 'cm^2/(mol*s)'),  
        n = 0.468,
        Ea = (76.8, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Deutschmann libraries""",
    longDesc = u"""
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 2.85E11(1/s)/2.483E-9(mol/cm^2) = 1.15E20 cm^2/(mol*s)

This is R75 in Table 2
""",
	metal = "Pt",
    facet = "111",
)

# entry(
#     index = 76,
#     label = "C_X + O_X <=> CO_X + X",
#     kinetics = SurfaceArrhenius(
#         A = (1.41E19, 'cm^2/(mol*s)'),  
#         n = -0.468,
#         Ea = (22.3, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Deutschmann libraries""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = 3.51E10(1/s)/2.483E-9(mol/cm^2) = 1.41E19 cm^2/(mol*s)

# This is R76 in Table 2
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 77,
    label = "CO_X + H_X <=> CH_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (1.26E20, 'cm^2/(mol*s)'),  
        n = 0.073,
        Ea = (45.8, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 3.12E11(1/s)/2.483E-9(mol/cm^2) = 1.26E20 cm^2/(mol*s)

This is R77 in Table 2
""",
	metal = "Pt",
    facet = "111",
)

# entry(
#     index = 78,
#     label = "CH_X + O_X <=> CO_X + H_X",
#     kinetics = SurfaceArrhenius(
#         A = (1.29E19, 'cm^2/(mol*s)'),  
#         n = -0.073,
#         Ea = (9.3, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = 3.21E10(1/s)/2.483E-9(mol/cm^2) = 1.29E19 cm^2/(mol*s)

# This is R78 in Table 2
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 79,
    label = "CO_X + H_X <=> C_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (2.00E20, 'cm^2/(mol*s)'),  
        n = -0.168,
        Ea = (40.7, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Deutschmann libraries""",
    longDesc = u"""
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 4.97E11(1/s)/2.483E-9(mol/cm^2) = 2.00E20 cm^2/(mol*s)

This is R79 in Table 2
""",
	metal = "Pt",
    facet = "111",
)

# entry(
#     index = 80,
#     label = "C_X + OH_X <=> CO_X + H_X",
#     kinetics = SurfaceArrhenius(
#         A = (8.10E18, 'cm^2/(mol*s)'),  
#         n = 0.168,
#         Ea = (4.4, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Deutschmann libraries""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = 2.01E10(1/s)/2.483E-9(mol/cm^2) = 8.10E18 cm^2/(mol*s)

# This is R80 in Table 2
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 81,
    label = "CO_X + CO_X <=> C_X + CO2_X",
    kinetics = SurfaceArrhenius(
        A = (2.39E20, 'cm^2/(mol*s)'),  
        n = 0.393,
        Ea = (48.8, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Deutschmann libraries""",
    longDesc = u"""
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 5.94E11(1/s)/2.483E-9(mol/cm^2) = 2.39E20 cm^2/(mol*s)

This is R81 in Table 2
""",
	metal = "Pt",
    facet = "111",
)

# entry(
#     index = 82,
#     label = "C_X + CO2_X <=> CO_X + CO_X",
#     kinetics = SurfaceArrhenius(
#         A = (6.77E18, 'cm^2/(mol*s)'),  
#         n = -0.393,
#         Ea = (0, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Deutschmann libraries""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = 1.68E10(1/s)/2.483E-9(mol/cm^2) = 6.77E18 cm^2/(mol*s)

# This is R82 in Table 2
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 83,
    label = "CH3OH + X <=> CH3OH_X",
    kinetics = StickingCoefficient(
        A = 0.334,  
        n = 0.258,
        Ea = (0, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This is R83 in Table 2
""",
	metal = "Pt",
    facet = "111",
)

# entry(
#     index = 84,
#     label = "CH3OH_X <=> CH3OH + X",
#     kinetics = SurfaceArrhenius(
#         A = (2.11E12, '1/s'),  
#         n = -0.258,
#         Ea = (9.5, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_vdW""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This is R84 in Table 2
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 85,
    label = "CH3O + X <=> CH3O_X",
    kinetics = StickingCoefficient(
        A = 0.149,  
        n = 0.054,
        Ea = (0, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""
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

# entry(
#     index = 86,
#     label = "CH3O_X <=> CH3O + X",
#     kinetics = SurfaceArrhenius(
#         A = (4.73E12, '1/s'),  
#         n = -0.054,
#         Ea = (37.0, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_Single""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This is R86 in Table 2
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 87,
    label = "CH2O + X <=> CH2O_X",
    kinetics = StickingCoefficient(
        A = 0.0877,  
        n = 0.098,
        Ea = (0, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This is R87 in Table 2
""",
	metal = "Pt",
    facet = "111",
)

# entry(
#     index = 88,
#     label = "CH2O_X <=> CH2O + X",
#     kinetics = SurfaceArrhenius(
#         A = (8.06E12, '1/s'),  
#         n = -0.098,
#         Ea = (12.0, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_vdW""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This is R88 in Table 2
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 89,
    label = "HCO + X <=> HCO_X",
    kinetics = StickingCoefficient(
        A = 0.0114,  
        n = 0.096,
        Ea = (0, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""
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

# entry(
#     index = 90,
#     label = "HCO_X <=> HCO + X",
#     kinetics = SurfaceArrhenius(
#         A = (6.21E13, '1/s'),  
#         n = -0.096,
#         Ea = (55.5, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_Single""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This is R90 in Table 2
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 91,
    label = "CH2OH + X <=> CH2OH_X",
    kinetics = StickingCoefficient(
        A = 0.0526,  
        n = 0.233,
        Ea = (0, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""
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

# entry(
#     index = 92,
#     label = "CH2OH_X <=> CH2OH + X",
#     kinetics = SurfaceArrhenius(
#         A = (1.35E13, '1/s'),  
#         n = -0.233,
#         Ea = (50.0, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_Single""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This is R92 in Table 2
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 93,
    label = "CH3OH_X + X <=> CH3O_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (3.15E19, 'cm^2/(mol*s)'),   
        n = 0.102,
        Ea = (18.8, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 7.82E10(1/s)/2.483E-9(mol/cm^2) = 3.15E19 cm^2/(mol*s)

This is R93 in Table 2
""",
	metal = "Pt",
    facet = "111",
)

# entry(
#     index = 94,
#     label = "CH3O_X + H_X <=> CH3OH_X + X",
#     kinetics = SurfaceArrhenius(
#         A = (5.16E19, 'cm^2/(mol*s)'),   
#         n = -0.102,
#         Ea = (4.3, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Dissociation_vdW""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = 1.28E11(1/s)/2.483E-9(mol/cm^2) = 5.16E19 cm^2/(mol*s)

# This is R94 in Table 2
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 95,
    label = "CH3O_X + X <=> CH2O_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (5.03E19, 'cm^2/(mol*s)'),   
        n = 0.192,
        Ea = (0, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Addition_Single_vdW""",
    longDesc = u"""
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

# entry(
#     index = 96,
#     label = "CH2O_X + H_X <=> CH3O_X + X",
#     kinetics = SurfaceArrhenius(
#         A = (3.23E19, 'cm^2/(mol*s)'),   
#         n = -0.192,
#         Ea = (14.7, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Addition_Single_vdW""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = 8.03E10(1/s)/2.483E-9(mol/cm^2) = 3.23E19 cm^2/(mol*s)

# This is R96 in Table 2
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 97,
    label = "CH2O_X + X <=> HCO_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (2.88E19, 'cm^2/(mol*s)'),   
        n = 0.270,
        Ea = (3.6, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 7.14E10(1/s)/2.483E-9(mol/cm^2) = 2.88E19 cm^2/(mol*s)

This is R97 in Table 2
""",
	metal = "Pt",
    facet = "111",
)

# entry(
#     index = 98,
#     label = "HCO_X + H_X <=> CH2O_X + X",
#     kinetics = SurfaceArrhenius(
#         A = (5.64E19, 'cm^2/(mol*s)'),   
#         n = -0.270,
#         Ea = (21.0, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Dissociation""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = 1.40E11(1/s)/2.483E-9(mol/cm^2) = 5.64E19 cm^2/(mol*s)

# This is R98 in Table 2
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 99,
    label = "HCO_X + X <=> CO_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (2.86E19, 'cm^2/(mol*s)'),   
        n = 0.330,
        Ea = (0, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 7.11E10(1/s)/2.483E-9(mol/cm^2) = 2.86E19 cm^2/(mol*s)

This is R99 in Table 2
""",
	metal = "Pt",
    facet = "111",
)

# entry(
#     index = 100,
#     label = "CO_X + H_X <=> HCO_X + X",
#     kinetics = SurfaceArrhenius(
#         A = (5.68E19, 'cm^2/(mol*s)'),   
#         n = -0.330,
#         Ea = (30.8, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Dissociation""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = 1.41E11(1/s)/2.483E-9(mol/cm^2) = 5.68E19 cm^2/(mol*s)

# This is R100 in Table 2
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 101,
    label = "CH3OH_X + X <=> CH2OH_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (3.42E19, 'cm^2/(mol*s)'),   
        n = 0.403,
        Ea = (8.7, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 8.48E10(1/s)/2.483E-9(mol/cm^2) = 3.42E19 cm^2/(mol*s)

This is R101 in Table 2
""",
	metal = "Pt",
    facet = "111",
)

# entry(
#     index = 102,
#     label = "CH2OH_X + H_X <=> CH3OH_X + X",
#     kinetics = SurfaceArrhenius(
#         A = (4.75E19, 'cm^2/(mol*s)'),   
#         n = -0.403,
#         Ea = (14.6, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Dissociation_vdW""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = 1.18E11(1/s)/2.483E-9(mol/cm^2) = 4.75E19 cm^2/(mol*s)

# This is R102 in Table 2
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 103,
    label = "CH2OH_X + X <=> CH2O_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (4.59E19, 'cm^2/(mol*s)'),   
        n = -0.104,
        Ea = (7.9, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Addition_Single_vdW""",
    longDesc = u"""
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

# entry(
#     index = 104,
#     label = "CH2O_X + H_X <=> CH2OH_X + X",
#     kinetics = SurfaceArrhenius(
#         A = (3.53E19, 'cm^2/(mol*s)'),   
#         n = 0.104,
#         Ea = (2.2, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Addition_Single_vdW""",
#     longDesc = u"""
# "A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
# Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
# D.G. Vlachos et al. (2007)
# Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
# DOI: 10.1021/ie070322c

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = 8.77E10(1/s)/2.483E-9(mol/cm^2) = 3.53E19 cm^2/(mol*s)

# This is R104 in Table 2
# """,
# 	metal = "Pt",
#     facet = "111",
# )
