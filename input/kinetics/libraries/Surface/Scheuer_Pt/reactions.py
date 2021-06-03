#!/usr/bin/env python
# encoding: utf-8

name = "Scheuer_Pt"
shortDesc = u""
longDesc = u"""
This library is built to import training reactions, based on:
"Dual layer automotive ammonia oxidation catalysts: Experiments and computer simulation"
Scheuer et al. Applied Catalysis B: Environmental 111–112 (2012) 445–455
https://doi.org/10.1016/j.apcatb.2011.10.032
"""

entry(
    index = 1,
    label = "NH3 + X <=> NH3_X",
    kinetics = StickingCoefficient(
        A = 0.00768,
        n = 0,
        Ea = (0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""
"Dual layer automotive ammonia oxidation catalysts: Experiments and computer simulation"
Scheuer et al. Applied Catalysis B: Environmental 111–112 (2012) 445–455
https://doi.org/10.1016/j.apcatb.2011.10.032

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = ((19/Pa)/s)*(2.483e-9(mol/cm^2))*sqrt(2*pi*(17(g/mol))*the molar gas constant*(298 kelvin))= 0.00768

This is R1 in Table 1 
""",
    metal = "Pt",
)

#Reverse reaction of R1
# entry(
#     index = 2,
#     label = "NH3_X <=> NH3 + X",
#     kinetics = SurfaceArrhenius(
#         A = (2.66E13, '1/s'),  
#         n = 0.0,
#         Ea = (116000, 'J/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_vdW""",
#     longDesc = u"""
# "Dual layer automotive ammonia oxidation catalysts: Experiments and computer simulation"
# Scheuer et al. Applied Catalysis B: Environmental 111–112 (2012) 445–455
# https://doi.org/10.1016/j.apcatb.2011.10.032

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = 6.6E4(mol/cm^2/s)/2.483E-9(mol/cm^2) = 2.66E13 (1/s)

# This is R2 in Table 1 
# """,
#     metal = "Pt",
# )

entry(
    index = 3,
    label = "O2 + X + X <=> O_X + O_X",
    kinetics = StickingCoefficient(
        A = 0.1441,
        n = 0,
        Ea = (0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""O2 Surface_Adsorption_Dissociative""",
    longDesc = u"""
"Dual layer automotive ammonia oxidation catalysts: Experiments and computer simulation"
Scheuer et al. Applied Catalysis B: Environmental 111–112 (2012) 445–455
https://doi.org/10.1016/j.apcatb.2011.10.032

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = ((260/Pa)/s)*(2.483e-9(mol/cm^2))*sqrt(2*pi*(32(g/mol))*the molar gas constant*(298 kelvin)) = 0.1441

This is R3 in Table 1 
""",
	metal = "Pt",
)

#Reverse reaction of R3
# entry(
#     index = 4,
#     label = "O_X + O_X <=> O2 + X + X",
#     kinetics = SurfaceArrhenius(
#         A = (4.83E20, 'cm^2/(mol*s)'),  
#         n = 0.0,
#         Ea = (128000, 'J/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""O2 Surface_Adsorption_Dissociative""",
#     longDesc = u"""
# "Dual layer automotive ammonia oxidation catalysts: Experiments and computer simulation"
# Scheuer et al. Applied Catalysis B: Environmental 111–112 (2012) 445–455
# https://doi.org/10.1016/j.apcatb.2011.10.032

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = 1.2E12(1/s)/2.483E-9(mol/cm^2) = 4.83E20 cm^2/(mol*s)

# This is R4 in Table 1 
# """,
# 	metal = "Pt",
# )

#skip R5

#Reverse reaction of R7
# entry(
#     index = 6,
#     label = "NO_X <=> NO + X",
#     kinetics = SurfaceArrhenius(
#         A = (6E17, '1/s'),  
#         n = 0.0,
#         Ea = (126000, 'J/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_Single""",
#     longDesc = u"""
# "Dual layer automotive ammonia oxidation catalysts: Experiments and computer simulation"
# Scheuer et al. Applied Catalysis B: Environmental 111–112 (2012) 445–455
# https://doi.org/10.1016/j.apcatb.2011.10.032

# This is R6 in Table 1 
# """,
#     metal = "Pt",
# )

entry(
    index = 7,
    label = "NO + X <=> NO_X",
    kinetics = StickingCoefficient(
        A = 0.1556,
        n = 0,
        Ea = (0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""
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
    index = 8,
    label = "N_X + N_X <=> N2 + X + X",
    kinetics = SurfaceArrhenius(
        A = (4.83E27, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (181000, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""N2 Surface_Adsorption_Dissociative""",
    longDesc = u"""
"Dual layer automotive ammonia oxidation catalysts: Experiments and computer simulation"
Scheuer et al. Applied Catalysis B: Environmental 111–112 (2012) 445–455
https://doi.org/10.1016/j.apcatb.2011.10.032

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1.2E19(1/s)/2.483E-9(mol/cm^2) = 4.83E27 cm^2/(mol*s)

This is R8 in Table 1 
""",
    metal = "Pt",
)

entry(
    index = 9,
    label = "N_X + O_X <=> NO_X + X",
    kinetics = SurfaceArrhenius(
        A = (1.13E22, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (126000, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Nitrogen/51""",
    longDesc = u"""
"Dual layer automotive ammonia oxidation catalysts: Experiments and computer simulation"
Scheuer et al. Applied Catalysis B: Environmental 111–112 (2012) 445–455
https://doi.org/10.1016/j.apcatb.2011.10.032

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 2.8E13(1/s)/2.483E-9(mol/cm^2) = 1.13E22 cm^2/(mol*s)

This is R9 in Table 1 
""",
    metal = "Pt",
)

entry(
    index = 10,
    label = "N_X + NO_X <=> N2O + X + X",
    kinetics = SurfaceArrhenius(
        A = (4.03E28, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (139000, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""N and NO Association""",
    longDesc = u"""
"Dual layer automotive ammonia oxidation catalysts: Experiments and computer simulation"
Scheuer et al. Applied Catalysis B: Environmental 111–112 (2012) 445–455
https://doi.org/10.1016/j.apcatb.2011.10.032

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1E20(1/s)/2.483E-9(mol/cm^2) = 4.03E28 cm^2/(mol*s)

This is R10 in Table 1 
""",
    metal = "Pt",
)

#Reverse reaction of R12
# entry(
#     index = 11,
#     label = "NO_X + O_X <=> NO2_X + X",
#     kinetics = SurfaceArrhenius(
#         A = (2.74E23, 'cm^2/(mol*s)'),  
#         n = 0.0,
#         Ea = (11500, 'J/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Dissociation""",
#     longDesc = u"""
# "Dual layer automotive ammonia oxidation catalysts: Experiments and computer simulation"
# Scheuer et al. Applied Catalysis B: Environmental 111–112 (2012) 445–455
# https://doi.org/10.1016/j.apcatb.2011.10.032

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = 6.8E14(1/s)/2.483E-9(mol/cm^2) = 2.74E23 cm^2/(mol*s)

# This is R11 in Table 1 
# """,
#     metal = "Pt",
# )

entry(
   index = 12,
   label = "NO2_X + X <=> NO_X + O_X",
   kinetics = SurfaceArrhenius(
       A = (1.29E20, 'cm^2/(mol*s)'),  
       n = 0.0,
       Ea = (83000, 'J/mol'),  
       Tmin = (200, 'K'),
       Tmax = (3000, 'K'),
   ),
   shortDesc = u"""Surface_Dissociation""",
   longDesc = u"""
"Dual layer automotive ammonia oxidation catalysts: Experiments and computer simulation"
Scheuer et al. Applied Catalysis B: Environmental 111–112 (2012) 445–455
https://doi.org/10.1016/j.apcatb.2011.10.032

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 3.2E11(1/s)/2.483E-9(mol/cm^2) = 1.29E20 cm^2/(mol*s)

This is R12 in Table 1 
""",
   metal = "Pt",
)

entry(
   index = 13,
   label = "NO2_X <=> NO2 + X",
   kinetics = SurfaceArrhenius(
       A = (1.3E14, '1/s'),  
       n = 0.0,
       Ea = (100000, 'J/mol'),  
       Tmin = (200, 'K'),
       Tmax = (3000, 'K'),
   ),
   shortDesc = u"""Surface_Adsorption_Single""",
   longDesc = u"""
"Dual layer automotive ammonia oxidation catalysts: Experiments and computer simulation"
Scheuer et al. Applied Catalysis B: Environmental 111–112 (2012) 445–455
https://doi.org/10.1016/j.apcatb.2011.10.032

This is R13 in Table 1 
""",
   metal = "Pt",
)

#skip R14 since sticking coefficient is larger than 1.
# entry(
#     index = 14,
#     label = "NO2 + X <=> NO2_X",
#     kinetics = StickingCoefficient(
#         A = ,
#         n = 0,
#         Ea = (, 'J/mol'),
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_Single""",
#     longDesc = u"""
# "Dual layer automotive ammonia oxidation catalysts: Experiments and computer simulation"
# Scheuer et al. Applied Catalysis B: Environmental 111–112 (2012) 445–455
# https://doi.org/10.1016/j.apcatb.2011.10.032

# This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
# A = ((48000/Pa)/s)*(2.483e-9(mol/cm^2))*sqrt(2*pi*(46(g/mol))*the molar gas constant*(298 kelvin)) = 31.894218
# Sticking coefficient is larger than 1, skip this reaction.

# This is R14 in Table 1 
# """,
#     metal = "Pt",
# )