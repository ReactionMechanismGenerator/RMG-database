#!/usr/bin/env python
# encoding: utf-8

name = "Vlachos_Rh"
shortDesc = u""
longDesc = u"""
Primarily based on:
"Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
Vlachos et al. (2008)
Journal of Catalysis,259(2), 211-222, 0021-9517
DOI: 10.1016/j.jcat.2008.08.008.D.G.
"""

entry(
    index = 1,
    label = "H2 + X + X <=> H_X + H_X",
    kinetics = StickingCoefficient(
        A = 0.773,
        n = 0.9387,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""H2 Surface_Adsorption_Dissociative""",
    longDesc = u"""
"Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
Vlachos et al. (2008)
Journal of Catalysis,259(2), 211-222, 0021-9517
DOI: 10.1016/j.jcat.2008.08.008.D.G.

This is R1 in Table 4
""",
	metal = "Rh",
)

# entry(
#    index = 2,
#    label = "H_X + H_X <=> H2 + X + X",
#    kinetics = SurfaceArrhenius(
#        A = (2.23E20, 'cm^2/(mol*s)'),  
#        n = -0.4347,
#        Ea = (12.3, 'kcal/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""H2 Surface_Adsorption_Dissociative""",
#    longDesc = u"""
# "Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
# Vlachos et al. (2008)
# Journal of Catalysis,259(2), 211-222, 0021-9517
# DOI: 10.1016/j.jcat.2008.08.008.D.G.

# Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
# A = 5.56E11(1/s)/2.49E-9(mol/cm^2) =  2.23E20cm^2/(mol*s)

# This is R2 in Table 4
# """,
#    metal = "Rh",
# )

entry(
   index = 3,
   label = "H2O_X + X <=> H_X + OH_X",
   kinetics = SurfaceArrhenius(
       A = (2.31E20, 'cm^2/(mol*s)'), 
       n = 0.0281,
       Ea = (18.6, 'kcal/mol'),
       Tmin = (200, 'K'),
       Tmax = (3000, 'K'),
   ),
   shortDesc = u"""Surface_Dissociation_vdW""",
   longDesc = u"""
"Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
Vlachos et al. (2008)
Journal of Catalysis,259(2), 211-222, 0021-9517
DOI: 10.1016/j.jcat.2008.08.008.D.G.

Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
A = 5.74E11(1/s)/2.49E-9(mol/cm^2) = 2.31E20 cm^2/(mol*s)

This is R7 in Table 4
""",
   metal = "Rh",
)

# entry(
#     index = 4,
#     label = "H_X + OH_X <=> H2O_X + X",
#     kinetics = SurfaceArrhenius(
#         A = (7.23E17, 'cm^2/(mol*s)'), 
#         n = 1.2972,
#         Ea = (16.3, 'kcal/mol'),
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Dissociation_vdW""",
#     longDesc = u"""
# "Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
# Vlachos et al. (2008)
# Journal of Catalysis,259(2), 211-222, 0021-9517
# DOI: 10.1016/j.jcat.2008.08.008.D.G.

# Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
# A = 1.80E09(1/s)/2.49E-9(mol/cm^2) = 7.23E17 cm^2/(mol*s)

# This is R8 in Table 4
# """,
#     metal = "Rh",
# )

entry(
    index = 5,
    label = "H2O + X <=> H2O_X",
    kinetics = StickingCoefficient(
        A = 0.0772,
        n = 1.4067,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""
"Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
Vlachos et al. (2008)
Journal of Catalysis,259(2), 211-222, 0021-9517
DOI: 10.1016/j.jcat.2008.08.008.D.G.

This is R13 in Table 4
""",
	metal = "Rh",
)

# entry(
#     index = 6,
#     label = "H2O_X <=> H2O + X",
#     kinetics = SurfaceArrhenius(
#         A = (2.06E13, '1/s'),  
#         n = -1.8613,
#         Ea = (7.5, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_vdW""",
#     longDesc = u"""
# "Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
# Vlachos et al. (2008)
# Journal of Catalysis,259(2), 211-222, 0021-9517
# DOI: 10.1016/j.jcat.2008.08.008.D.G.

# This is R14 in Table 4
# """,
# 	metal = "Rh",
# )

entry(
    index = 7,
    label = "CO + X <=> CO_X",
    kinetics = StickingCoefficient(
        A = 0.5,
        n = -2.00,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Double""",
    longDesc = u"""
"Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
Vlachos et al. (2008)
Journal of Catalysis,259(2), 211-222, 0021-9517
DOI: 10.1016/j.jcat.2008.08.008.D.G.

This is R19 in Table 4
""",
	metal = "Rh",
)

# entry(
#     index = 8,
#     label = "CO_X <=> CO + X",
#     kinetics = SurfaceArrhenius(
#         A = (5.65E12, '1/s'),  
#         n = 1.9879,
#         Ea = (32.8, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_Double""",
#     longDesc = u"""
# "Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
# Vlachos et al. (2008)
# Journal of Catalysis,259(2), 211-222, 0021-9517
# DOI: 10.1016/j.jcat.2008.08.008.D.G.

# This is R20 in Table 4
# """,
# 	metal = "Rh",
# )

entry(
    index = 9,
    label = "CO2 + X <=> CO2_X",
    kinetics = StickingCoefficient(
        A = 0.367,
        n = -2.3294,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""
"Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
Vlachos et al. (2008)
Journal of Catalysis,259(2), 211-222, 0021-9517
DOI: 10.1016/j.jcat.2008.08.008.D.G.

This is R21 in Table 4
""",
	metal = "Rh",
)

# entry(
#     index = 10,
#     label = "CO2_X <=> CO2 + X",
#     kinetics = SurfaceArrhenius(
#         A = (7.54E10, '1/s'),  
#         n = 2.1831,
#         Ea = (2.8, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_vdW""",
#     longDesc = u"""
# "Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
# Vlachos et al. (2008)
# Journal of Catalysis,259(2), 211-222, 0021-9517
# DOI: 10.1016/j.jcat.2008.08.008.D.G.

# This is R22 in Table 4
# """,
# 	metal = "Rh",
# )

entry(
    index = 11,
    label = "CO2_X + H_X <=> CO_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (1.61E23, 'cm^2/(mol*s)'),  
        n = 0.0301,
        Ea = (5.2, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Deutschmann_Pt/19""",
    longDesc = u"""
"Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
Vlachos et al. (2008)
Journal of Catalysis,259(2), 211-222, 0021-9517
DOI: 10.1016/j.jcat.2008.08.008.D.G.

Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
A = 4.00E14(1/s)/2.49E-9(mol/cm^2) = 1.61E23 cm^2/(mol*s)

This is R29 in Table 4
""",
    metal = "Rh",
)

# entry(
#     index = 12,
#     label = "CO_X + OH_X <=> CO2_X + H_X",
#     kinetics = SurfaceArrhenius(
#         A = (1.41E23, 'cm^2/(mol*s)'),  
#         n = -0.0301,
#         Ea = (19.9, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Deutschmann_Pt/19""",
#     longDesc = u"""
# "Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
# Vlachos et al. (2008)
# Journal of Catalysis,259(2), 211-222, 0021-9517
# DOI: 10.1016/j.jcat.2008.08.008.D.G.

# Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
# A = 3.51E14(1/s)/2.49E-9(mol/cm^2) = 1.41E23 cm^2/(mol*s)

# This is R30 in Table 4
# """,
#     metal = "Rh",
# )

entry(
    index = 13,
    label = "COOH_X + X <=> CO_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (4.30E20, 'cm^2/(mol*s)'),  
        n = -0.4123,
        Ea = (7.5, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
Vlachos et al. (2008)
Journal of Catalysis,259(2), 211-222, 0021-9517
DOI: 10.1016/j.jcat.2008.08.008.D.G.

Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
A = 1.07E12(1/s)/2.49E-9(mol/cm^2) = 4.30E20 cm^2/(mol*s)

This is R31 in Table 4
""",
	metal = "Rh",
)

# entry(
#     index = 14,
#     label = "CO_X + OH_X <=> COOH_X + X",
#     kinetics = SurfaceArrhenius(
#         A = (3.76E20, 'cm^2/(mol*s)'),  
#         n = 0.4123,
#         Ea = (14.6, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Dissociation""",
#     longDesc = u"""
# "Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
# Vlachos et al. (2008)
# Journal of Catalysis,259(2), 211-222, 0021-9517
# DOI: 10.1016/j.jcat.2008.08.008.D.G.

# Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
# A = 9.37E11(1/s)/2.49E-9(mol/cm^2) = 3.76E20 cm^2/(mol*s)

# This is R32 in Table 4
# """,
# 	metal = "Rh",
# )

entry(
    index = 15,
    label = "COOH_X + X <=> CO2_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (4.02E18, 'cm^2/(mol*s)'),  
        n = -0.4424,
        Ea = (7.6, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Addition_Single_vdW""",
    longDesc = u"""
"Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
Vlachos et al. (2008)
Journal of Catalysis,259(2), 211-222, 0021-9517
DOI: 10.1016/j.jcat.2008.08.008.D.G.

Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
A = 1.00E10(1/s)/2.49E-9(mol/cm^2) = 4.02E18 cm^2/(mol*s)

This is R33 in Table 4
""",
	metal = "Rh",
)

# entry(
#     index = 16,
#     label = "CO2_X + H_X <=> COOH_X + X",
#     kinetics = SurfaceArrhenius(
#         A = (4.01E18, 'cm^2/(mol*s)'),  
#         n = 0.4424,
#         Ea = (0, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Addition_Single_vdW""",
#     longDesc = u"""
# "Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
# Vlachos et al. (2008)
# Journal of Catalysis,259(2), 211-222, 0021-9517
# DOI: 10.1016/j.jcat.2008.08.008.D.G.

# Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
# A = 9.99E09(1/s)/2.49E-9(mol/cm^2) = 4.01E18 cm^2/(mol*s)

# This is R34 in Table 4
# """,
# 	metal = "Rh",
# )

entry(
    index = 17,
    label = "CO_X + H2O_X <=> COOH_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (1.34E20, 'cm^2/(mol*s)'),  
        n = -0.2222,
        Ea = (19.5, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
Vlachos et al. (2008)
Journal of Catalysis,259(2), 211-222, 0021-9517
DOI: 10.1016/j.jcat.2008.08.008.D.G.

Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
A = 3.34E11(1/s)/2.49E-9(mol/cm^2) = 1.34E20 cm^2/(mol*s)

This is R35 in Table 4
""",
	metal = "Rh",
)

#R36 in the table 4 has a typo of the reactant H_X
# entry(
#     index = 18,
#     label = "COOH_X + H_X <=> CO_X + H2O_X",
#     kinetics = SurfaceArrhenius(
#         A = (4.82E17, 'cm^2/(mol*s)'),  
#         n = 0.2223,
#         Ea = (0, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Abstraction_vdW""",
#     longDesc = u"""
# "Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
# Vlachos et al. (2008)
# Journal of Catalysis,259(2), 211-222, 0021-9517
# DOI: 10.1016/j.jcat.2008.08.008.D.G.

# Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
# A = 1.20E09(1/s)/2.49E-9(mol/cm^2) = 4.82E17 cm^2/(mol*s)

# This is R36 in Table 4
# """,
# 	metal = "Rh",
# )

entry(
    index = 19,
    label = "CO2_X + H2O_X <=> COOH_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (7.15E20, 'cm^2/(mol*s)'),  
        n = -0.1992,
        Ea = (13.1, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dual_Adsorption_vdW""",
    longDesc = u"""
"Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
Vlachos et al. (2008)
Journal of Catalysis,259(2), 211-222, 0021-9517
DOI: 10.1016/j.jcat.2008.08.008.D.G.

Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
A = 1.78E12(1/s)/2.49E-9(mol/cm^2) = 7.15E20 cm^2/(mol*s)

This is R39 in Table 4
""",
	metal = "Rh",
)

# entry(
#     index = 20,
#     label = "COOH_X + OH_X <=> CO2_X + H2O_X",
#     kinetics = SurfaceArrhenius(
#         A = (2.25E18, 'cm^2/(mol*s)'),  
#         n = 0.1922,
#         Ea = (18.3, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Dual_Adsorption_vdW""",
#     longDesc = u"""
# "Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
# Vlachos et al. (2008)
# Journal of Catalysis,259(2), 211-222, 0021-9517
# DOI: 10.1016/j.jcat.2008.08.008.D.G.

# Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
# A = 5.60E09(1/s)/2.49E-9(mol/cm^2) = 2.25E18 cm^2/(mol*s)

# This is R40 in Table 4
# """,
# 	metal = "Rh",
# )

entry(
    index = 21,
    label = "CH4 + X + X <=> CH3_X + H_X",
    kinetics = StickingCoefficient(
        A = 0.572,
        n = 0.7883,
        Ea = (14.7, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
Vlachos et al. (2008)
Journal of Catalysis,259(2), 211-222, 0021-9517
DOI: 10.1016/j.jcat.2008.08.008.D.G.

This is R55 in Table 4
""",
	metal = "Rh",
)

# entry(
#     index = 22,
#     label = "CH3_X + H_X <=> CH4 + X + X",
#     kinetics = SurfaceArrhenius(
#         A = (3.10E19, 'cm^2/(mol*s)'),  
#         n = -0.7883,
#         Ea = (5.5, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Dissociation""",
#     longDesc = u"""
# "Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
# Vlachos et al. (2008)
# Journal of Catalysis,259(2), 211-222, 0021-9517
# DOI: 10.1016/j.jcat.2008.08.008.D.G.

# Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
# A = 7.72E10(1/s)/2.49E-9(mol/cm^2) = 3.10E19 cm^2/(mol*s)

# This is R56 in Table 4
# """,
# 	metal = "Rh",
# )

entry(
    index = 23,
    label = "CH3_X + X <=> CH2_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (1.00E19, 'cm^2/(mol*s)'),  
        n = 0.0862,
        Ea = (12.2, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Dissociative""",
    longDesc = u"""
"Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
Vlachos et al. (2008)
Journal of Catalysis,259(2), 211-222, 0021-9517
DOI: 10.1016/j.jcat.2008.08.008.D.G.

Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
A = 2.49E10(1/s)/2.49E-9(mol/cm^2) = 1.00E19 cm^2/(mol*s)

This is R57 in Table 4
""",
	metal = "Rh",
)

# entry(
#     index = 24,
#     label = "CH2_X + H_X <=> CH3_X + X",
#     kinetics = SurfaceArrhenius(
#         A = (1.03E18, 'cm^2/(mol*s)'),  
#         n = -0.0862,
#         Ea = (25.7, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_Dissociative""",
#     longDesc = u"""
# "Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
# Vlachos et al. (2008)
# Journal of Catalysis,259(2), 211-222, 0021-9517
# DOI: 10.1016/j.jcat.2008.08.008.D.G.

# Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
# A = 2.57E09(1/s)/2.49E-9(mol/cm^2) = 1.03E18 cm^2/(mol*s)

# This is R58 in Table 4
# """,
# 	metal = "Rh",
# )

entry(
    index = 25,
    label = "CH2_X + X <=> CH_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (2.21E19, 'cm^2/(mol*s)'),  
        n = -0.1312,
        Ea = (21.7, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
Vlachos et al. (2008)
Journal of Catalysis,259(2), 211-222, 0021-9517
DOI: 10.1016/j.jcat.2008.08.008.D.G.

Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
A = 5.50E10(1/s)/2.49E-9(mol/cm^2) = 2.21E19 cm^2/(mol*s)

This is R59 in Table 4
""",
	metal = "Rh",
)

# entry(
#     index = 26,
#     label = "CH_X + H_X <=> CH2_X + X",
#     kinetics = SurfaceArrhenius(
#         A = (2.92E18, 'cm^2/(mol*s)'),  
#         n = 0.1312,
#         Ea = (20.6, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Dissociation""",
#     longDesc = u"""
# "Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
# Vlachos et al. (2008)
# Journal of Catalysis,259(2), 211-222, 0021-9517
# DOI: 10.1016/j.jcat.2008.08.008.D.G.

# Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
# A = 7.27E09(1/s)/2.49E-9(mol/cm^2) = 2.92E18 cm^2/(mol*s)

# This is R60 in Table 4
# """,
# 	metal = "Rh",
# )

entry(
    index = 27,
    label = "CH_X + X <=> C_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (1.84E21, 'cm^2/(mol*s)'),  
        n = -0.2464,
        Ea = (28.9, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
Vlachos et al. (2008)
Journal of Catalysis,259(2), 211-222, 0021-9517
DOI: 10.1016/j.jcat.2008.08.008.D.G.

Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
A = 4.58E12(1/s)/2.49E-9(mol/cm^2) = 1.84E21 cm^2/(mol*s)

This is R61 in Table 4
""",
	metal = "Rh",
)

# entry(
#     index = 28,
#     label = "C_X + H_X <=> CH_X + X",
#     kinetics = SurfaceArrhenius(
#         A = (8.76E19, 'cm^2/(mol*s)'),  
#         n = 0.2464,
#         Ea = (14.1, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Dissociation""",
#     longDesc = u"""
# "Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
# Vlachos et al. (2008)
# Journal of Catalysis,259(2), 211-222, 0021-9517
# DOI: 10.1016/j.jcat.2008.08.008.D.G.

# Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
# A = 2.18E11(1/s)/2.49E-9(mol/cm^2) = 8.76E19 cm^2/(mol*s)

# This is R62 in Table 4
# """,
# 	metal = "Rh",
# )

entry(
    index = 29,
    label = "CH3_X + O_X <=> CH2_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (1.19E20, 'cm^2/(mol*s)'),  
        n = -0.1906,
        Ea = (6.7, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction""",
    longDesc = u"""
"Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
Vlachos et al. (2008)
Journal of Catalysis,259(2), 211-222, 0021-9517
DOI: 10.1016/j.jcat.2008.08.008.D.G.

Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
A = 2.96E11(1/s)/2.49E-9(mol/cm^2) = 1.19E20 cm^2/(mol*s)

This is R63 in Table 4
""",
	metal = "Rh",
)

# entry(
#     index = 30,
#     label = "CH2_X + OH_X <=> CH3_X + O_X",
#     kinetics = SurfaceArrhenius(
#         A = (1.36E19, 'cm^2/(mol*s)'),  
#         n = 0.1906,
#         Ea = (34.5, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Abstraction""",
#     longDesc = u"""
# "Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
# Vlachos et al. (2008)
# Journal of Catalysis,259(2), 211-222, 0021-9517
# DOI: 10.1016/j.jcat.2008.08.008.D.G.

# Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
# A = 3.38E10(1/s)/2.49E-9(mol/cm^2) = 1.36E19 cm^2/(mol*s)

# This is R64 in Table 4
# """,
# 	metal = "Rh",
# )

entry(
    index = 31,
    label = "CH2_X + H2O_X <=> CH3_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (2.30E19, 'cm^2/(mol*s)'),  
        n = -0.7208,
        Ea = (20.3, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
Vlachos et al. (2008)
Journal of Catalysis,259(2), 211-222, 0021-9517
DOI: 10.1016/j.jcat.2008.08.008.D.G.

Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
A = 5.73E10(1/s)/2.49E-9(mol/cm^2) = 2.30E19 cm^2/(mol*s)

This is R69 in Table 4
""",
	metal = "Rh",
)

# entry(
#     index = 32,
#     label = "CH3_X + OH_X <=> CH2_X + H2O_X",
#     kinetics = SurfaceArrhenius(
#         A = (6.99E17, 'cm^2/(mol*s)'),  
#         n = 0.7208,
#         Ea = (4.4, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Abstraction_vdW""",
#     longDesc = u"""
# "Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
# Vlachos et al. (2008)
# Journal of Catalysis,259(2), 211-222, 0021-9517
# DOI: 10.1016/j.jcat.2008.08.008.D.G.

# Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
# A = 1.74E09(1/s)/2.49E-9(mol/cm^2) = 6.99E17 cm^2/(mol*s)

# This is R70 in Table 4
# """,
# 	metal = "Rh",
# )

entry(
    index = 33,
    label = "CH_X + H2O_X <=> CH2_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (2.61E20, 'cm^2/(mol*s)'),  
        n = -0.5033,
        Ea = (21.2, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
Vlachos et al. (2008)
Journal of Catalysis,259(2), 211-222, 0021-9517
DOI: 10.1016/j.jcat.2008.08.008.D.G.

Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
A = 6.49E11(1/s)/2.49E-9(mol/cm^2) = 2.61E20 cm^2/(mol*s)

This is R71 in Table 4
""",
	metal = "Rh",
)

# entry(
#     index = 34,
#     label = "CH2_X + OH_X <=> CH_X + H2O_X",
#     kinetics = SurfaceArrhenius(
#         A = (6.18E18, 'cm^2/(mol*s)'),  
#         n = 0.5033,
#         Ea = (19.9, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Abstraction_vdW""",
#     longDesc = u"""
# "Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
# Vlachos et al. (2008)
# Journal of Catalysis,259(2), 211-222, 0021-9517
# DOI: 10.1016/j.jcat.2008.08.008.D.G.

# Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
# A = 1.54E10(1/s)/2.49E-9(mol/cm^2) = 6.18E18 cm^2/(mol*s)

# This is R72 in Table 4
# """,
# 	metal = "Rh",
# )

entry(
    index = 35,
    label = "C_X + H2O_X <=> CH_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (3.91E20, 'cm^2/(mol*s)'),  
        n = -0.3882,
        Ea = (17.0, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
Vlachos et al. (2008)
Journal of Catalysis,259(2), 211-222, 0021-9517
DOI: 10.1016/j.jcat.2008.08.008.D.G.

Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
A = 9.74E11(1/s)/2.49E-9(mol/cm^2) = 3.91E20 cm^2/(mol*s)

This is R73 in Table 4
""",
	metal = "Rh",
)

# entry(
#     index = 36,
#     label = "CH_X + OH_X <=> C_X + H2O_X",
#     kinetics = SurfaceArrhenius(
#         A = (2.57E19, 'cm^2/(mol*s)'),  
#         n = 0.3882,
#         Ea = (29.3, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Abstraction_vdW""",
#     longDesc = u"""
# "Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
# Vlachos et al. (2008)
# Journal of Catalysis,259(2), 211-222, 0021-9517
# DOI: 10.1016/j.jcat.2008.08.008.D.G.

# Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
# A = 6.41E10(1/s)/2.49E-9(mol/cm^2) = 2.57E19 cm^2/(mol*s)

# This is R74 in Table 4
# """,
# 	metal = "Rh",
# )

entry(
    index = 37,
    label = "CO_X + H_X <=> C_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (4.74E20, 'cm^2/(mol*s)'),  
        n = 0.2944,
        Ea = (22.6, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Deutschmann libraries""",
    longDesc = u"""
"Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
Vlachos et al. (2008)
Journal of Catalysis,259(2), 211-222, 0021-9517
DOI: 10.1016/j.jcat.2008.08.008.D.G.

Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
A = 1.18E12(1/s)/2.49E-9(mol/cm^2) = 4.74E20 cm^2/(mol*s)

This is R79 in Table 4
""",
	metal = "Rh",
)

# entry(
#     index = 38,
#     label = "C_X + OH_X <=> CO_X + H_X",
#     kinetics = SurfaceArrhenius(
#         A = (3.05E21, 'cm^2/(mol*s)'),  
#         n = -0.2944,
#         Ea = (0, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Deutschmann libraries""",
#     longDesc = u"""
# "Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
# Vlachos et al. (2008)
# Journal of Catalysis,259(2), 211-222, 0021-9517
# DOI: 10.1016/j.jcat.2008.08.008.D.G.

# Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
# A = 7.60E12(1/s)/2.49E-9(mol/cm^2) = 3.0521 cm^2/(mol*s)

# This is R80 in Table 4
# """,
# 	metal = "Rh",
# )
