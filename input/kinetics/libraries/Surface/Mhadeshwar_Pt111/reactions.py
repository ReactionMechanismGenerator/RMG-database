#!/usr/bin/env python
# encoding: utf-8

name = "Mhadeshwar_Pt111"
shortDesc = u""
longDesc = u"""
Primarily based on:
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021
"""

#---------------------O2 adsorption/desorption------------------------

entry(
    index = 1,
    label = "O + X <=> O_X",
    kinetics = StickingCoefficient(
        A = 1,
        n = 0.0,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Double""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

This is R1 in Appendix A

This reaction is the least important ones for typical DOC conditions.
""",
    metal = "Pt",
    facet = "111",
)

#Reverse reaction of R1
# entry(
#     index = 2,
#     label = "O_X <=> O + X",
#     kinetics = SurfaceArrhenius(
#         A = (1E13, '1/s'),  
#         n = 0.0,
#         Ea = (86, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_Double""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# This is R2 in Appendix A

# This reaction is the least important ones for typical DOC conditions.
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
   index = 3,
   label = "O2 + X + X <=> O_X + O_X",
   kinetics = StickingCoefficient(
       A = 0.05,
       n = 0.0,
       Ea = (0, 'kcal/mol'),
       Tmin = (200, 'K'),
       Tmax = (3000, 'K'),
   ),
   shortDesc = u"""O2 Surface_Adsorption_Dissociative""",
   longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

This is R3 in Appendix A
""",
	metal = "Pt",
   facet = "111",
)

# Reverse reaction of R3
# entry(
#    index = 4,
#    label = "O_X + O_X <=> O2 + X + X",
#    kinetics = SurfaceArrhenius(
#        A = (4E19, 'cm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (52.9, 'kcal/mol'),  
#        Tmin = (200, 'K'),
#        Tmax = (3000, 'K'),
#    ),
#    shortDesc = u"""O2 Surface_Adsorption_Dissociative""",
#    longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E13(1/s)/2.5E-9(mol/cm^2) = 4E21 cm^2/(mol*s)

# This is R4 in Appendix A
# """,
# 	metal = "Pt",
#    facet = "111",
# )

#---------------------CO oxidation-----------------------------------

entry(
    index = 5,
    label = "CO + X <=> CO_X",
    kinetics = StickingCoefficient(
        A = 0.5,
        n = 0.0,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Double""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

This is R5 in Appendix A
""",
	metal = "Pt",
    facet = "111",
)

# Reverse reaction of R5
# entry(
#     index = 6,
#     label = "CO_X <=> CO + X",
#     kinetics = SurfaceArrhenius(
#         A = (2.28E25, '1/s'),  
#         n = 0.0,
#         Ea = (40, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_Double""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 5.7E16(1/s)/2.5E-9(mol/cm^2) = 2.28E25 cm^2/(mol*s)

# This is R6 in Appendix A
# """,
# 	metal = "Pt",
#     facet = "111",
# )


entry(
    index = 7,
    label = "CO2 + X <=> CO2_X",
    kinetics = StickingCoefficient(
        A = 1,
        n = 0.0,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

This is R7 in Appendix A
""",
	metal = "Pt",
    facet = "111",
)

# Reverse reaction of R7
# entry(
#     index = 8,
#     label = "CO2_X <=> CO2 + X",
#     kinetics = SurfaceArrhenius(
#         A = (1E13, '1/s'),  
#         n = 0.0,
#         Ea = (3.6, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_vdW""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# This is R8 in Appendix A
# """,
# 	metal = "Pt",
#     facet = "111",
# )

# Reverse reaction of R9
# entry(
#     index = 9,
#     label = "CO2_X + X <=> CO_X + O_X",
#     kinetics = SurfaceArrhenius(
#         A = (4E19, 'cm^2/(mol*s)'),  
#         n = 0.0,
#         Ea = (23.4, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Dissociation_Double_vdW""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

# This is R9 in Appendix A
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 10,
    label = "CO_X + O_X <=> CO2_X + X",
    kinetics = SurfaceArrhenius(
        A = (4E18, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (18.6, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_Double_vdW""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E10(1/s)/2.5E-9(mol/cm^2) = 4E18 cm^2/(mol*s)

This is R10 in Appendix A
""",
	metal = "Pt",
    facet = "111",
)

#---------------------H2 oxidation-----------------------------------

entry(
    index = 11,
    label = "H + X <=> H_X",
    kinetics = StickingCoefficient(
        A = 1,
        n = 0.0,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

This is R11 in Appendix A

This reaction is the least important ones for typical DOC conditions.
""",
	metal = "Pt",
    facet = "111",
)

# Reverse reaction of R11
# entry(
#     index = 12,
#     label = "H_X <=> H + X",
#     kinetics = SurfaceArrhenius(
#         A = (1E13, '1/s'),  
#         n = 0.0,
#         Ea = (60.9, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_Single""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# This is R12 in Appendix A

# This reaction is the least important ones for typical DOC conditions.
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 13,
    label = "H2 + X + X <=> H_X + H_X",
    kinetics = StickingCoefficient(
        A = 1,
        n = 0.0,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""H2 Surface_Adsorption_Dissociative""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

This is R13 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

# Reverse reaction of R13
# entry(
#     index = 14,
#     label = "H_X + H_X <=> H2 + X + X",
#     kinetics = SurfaceArrhenius(
#         A = (4E21, 'cm^2/(mol*s)'),  
#         n = 0.0,
#         Ea = (17.6, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""H2 Surface_Adsorption_Dissociative""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E13(1/s)/2.5E-9(mol/cm^2) = 4E21 cm^2/(mol*s)

# This is R14 in Appendix A
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
    index = 15,
    label = "H2O + X <=> H2O_X",
    kinetics = StickingCoefficient(
        A = 1,
        n = 0.0,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

This is R15 in Appendix A
""",
	metal = "Pt",
    facet = "111",
)

# Reverse reaction of R15
# entry(
#     index = 16,
#     label = "H2O_X <=> H2O + X",
#     kinetics = SurfaceArrhenius(
#         A = (1E13, '1/s'),  
#         n = 0.0,
#         Ea = (10.3, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# This is R16 in Appendix A
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 17,
    label = "OH + X <=> OH_X",
    kinetics = StickingCoefficient(
        A = 1,
        n = 0.0,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

This is R17 in Appendix A

This reaction is the least important ones for typical DOC conditions.
""",
	metal = "Pt",
    facet = "111",
)

# Reverse reaction of R17
# entry(
#     index = 18,
#     label = "OH_X <=> OH + X",
#     kinetics = SurfaceArrhenius(
#         A = (1E13, '1/s'),  
#         n = 0.0,
#         Ea = (63, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_Single""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# This is R18 in Appendix A

# This reaction is the least important ones for typical DOC conditions.
# """,
# 	metal = "Pt",
#     facet = "111",
# )

# Reverse reaction of R20
# entry(
#     index = 19,
#     label = "OH_X + X <=> H_X + O_X",
#     kinetics = SurfaceArrhenius(
#         A = (4E19, 'cm^2/(mol*s)'), 
#         n = 0.0,
#         Ea = (27, 'kcal/mol'),
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Dissociation""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

# This is R19 in Appendix A
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
    index = 20,
    label = "H_X + O_X <=> OH_X + X",
    kinetics = SurfaceArrhenius(
        A = (4E19, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (8.6, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R20 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

# Reverse reaction of R22
# entry(
#     index = 21,
#     label = "H2O_X + X <=> H_X + OH_X",
#     kinetics = SurfaceArrhenius(
#         A = (4E19, 'cm^2/(mol*s)'), 
#         n = 0.0,
#         Ea = (18.3, 'kcal/mol'),
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Dissociation""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

# This is R21 in Appendix A
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
    index = 22,
    label = "H_X + OH_X <=> H2O_X + X",
    kinetics = SurfaceArrhenius(
        A = (4E19, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (12.6, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R22 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

# Reverse reaction of R24
# entry(
#     index = 23,
#     label = "O_X + H2O_X <=> OH_X + OH_X",
#     kinetics = SurfaceArrhenius(
#         A = (4E19, 'cm^2/(mol*s)'),  
#         n = 0.0,
#         Ea = (9.4, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Abstraction_vdW""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

# This is R23 in Appendix A
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
    index = 24,
    label = "OH_X + OH_X <=> O_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (4E19, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (22.1, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R24 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

#-----------------Water promoted CO oxidation------------------------

entry(
    index = 25,
    label = "COOH + X <=> COOH_X",
    kinetics = StickingCoefficient(
        A = 1,
        n = 0.0,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

This is R25 in Appendix A

This reaction is the least important ones for typical DOC conditions.
""",
	metal = "Pt",
    facet = "111",
)

# Reverse reaction of R25
# entry(
#     index = 26,
#     label = "COOH_X <=> COOH + X",
#     kinetics = SurfaceArrhenius(
#         A = (1E13, '1/s'),  
#         n = 0.0,
#         Ea = (56.3, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_Single""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# This is R26 in Appendix A

# This reaction is the least important ones for typical DOC conditions.
# """,
# 	metal = "Pt",
#     facet = "111",
# )

# Reverse reaction of R28
# entry(
#     index = 27,
#     label = "CO2_X + H_X <=> CO_X + OH_X",
#     kinetics = SurfaceArrhenius(
#         A = (4E19, 'cm^2/(mol*s)'),  
#         n = 0.0,
#         Ea = (5.4, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Deutschmann_Pt/19""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

# This is R27 in Appendix A
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
    index = 28,
    label = "CO_X + OH_X <=> CO2_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (4E19, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (19, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Deutschmann_Pt/19""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R28 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

# Reverse reaction of R30
# entry(
#     index = 29,
#     label = "COOH_X + X <=> CO_X + OH_X",
#     kinetics = SurfaceArrhenius(
#         A = (4E19, 'cm^2/(mol*s)'),  
#         n = 0.0,
#         Ea = (5.8, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Dissociation""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

# This is R29 in Appendix A
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 30,
    label = "CO_X + OH_X <=> COOH_X + X",
    kinetics = SurfaceArrhenius(
        A = (4E19, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (18.7, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R30 in Appendix A
""",
	metal = "Pt",
    facet = "111",
)

# Reverse reaction of R32
# entry(
#     index = 31,
#     label = "COOH_X + X <=> CO2_X + H_X",
#     kinetics = SurfaceArrhenius(
#         A = (4E19, 'cm^2/(mol*s)'),  
#         n = 0.0,
#         Ea = (2.1, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Addition_Single_vdW""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

# This is R31 in Appendix A
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 32,
    label = "CO2_X + H_X <=> COOH_X + X",
    kinetics = SurfaceArrhenius(
        A = (4E19, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (1.3, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Addition_Single_vdW""",
    longDesc = u"""
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

# Reverse reaction of R34
# entry(
#     index = 33,
#     label = "CO_X + H2O_X <=> COOH_X + H_X",
#     kinetics = SurfaceArrhenius(
#         A = (4E19, 'cm^2/(mol*s)'),  
#         n = 0.0,
#         Ea = (23.9, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Abstraction_vdW""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

# This is R33 in Appendix A

# This reaction is the least important ones for typical DOC conditions.
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 34,
    label = "COOH_X + H_X <=> CO_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (4E19, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (5.4, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R34 in Appendix A

This reaction is the least important ones for typical DOC conditions.
""",
	metal = "Pt",
    facet = "111",
)

# Reverse reaction of R36
# entry(
#     index = 35,
#     label = "CO2_X + OH_X <=> COOH_X + O_X",
#     kinetics = SurfaceArrhenius(
#         A = (4E19, 'cm^2/(mol*s)'),  
#         n = 0.0,
#         Ea = (25.8, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_Abstraction_vdW""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

# This is R35 in Appendix A

# This reaction is the least important ones for typical DOC conditions.
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 36,
    label = "COOH_X + O_X <=> CO2_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (4E19, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (8.2, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Abstraction_vdW""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R36 in Appendix A

This reaction is the least important ones for typical DOC conditions.
""",
	metal = "Pt",
    facet = "111",
)

# Reverse reaction of R38
# entry(
#     index = 37,
#     label = "CO2_X + H2O_X <=> COOH_X + OH_X",
#     kinetics = SurfaceArrhenius(
#         A = (4E19, 'cm^2/(mol*s)'),  
#         n = 0.0,
#         Ea = (17.3, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Dual_Adsorption_vdW""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

# This is R37 in Appendix A

# This reaction is the least important ones for typical DOC conditions.
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 38,
    label = "COOH_X + OH_X <=> CO2_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (4E19, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (12.4, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dual_Adsorption_vdW""",
    longDesc = u"""
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

#---------------------NH3 oxidation----------------------------------

entry(
    index = 39,
    label = "N + X <=> N_X",
    kinetics = StickingCoefficient(
        A = 1,
        n = 0.0,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Triple""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

This is R39 in Appendix A

This reaction is the least important ones for typical DOC conditions.
""",
    metal = "Pt",
    facet = "111",
)

# Reverse reaction of R39
# entry(
#     index = 40,
#     label = "N_X <=> N + X",
#     kinetics = SurfaceArrhenius(
#         A = (1E13, '1/s'),  
#         n = 0.0,
#         Ea = (107.4, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_Triple""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# This is R40 in Appendix A

# This reaction is the least important ones for typical DOC conditions.
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
    index = 41,
    label = "N2 + X + X <=> N_X + N_X",
    kinetics = StickingCoefficient(
        A = 1,
        n = 0.0,
        Ea = (27.9, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""N2 Surface_Adsorption_Dissociative""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

This is R41 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

# Reverse reaction of R41
# entry(
#     index = 42,
#     label = "N_X + N_X <=> N2 + X + X",
#     kinetics = SurfaceArrhenius(
#         A = (4E21, 'cm^2/(mol*s)'),  
#         n = 0.0,
#         Ea = (16.7, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""N2 Surface_Adsorption_Dissociative""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E13(1/s)/2.5E-9(mol/cm^2) = 4E21 cm^2/(mol*s)

# This is R42 in Appendix A
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
    index = 43,
    label = "NH3 + X <=> NH3_X",
    kinetics = StickingCoefficient(
        A = 1,
        n = 0.0,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

This is R43 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

# Reverse reaction of R43
# entry(
#     index = 44,
#     label = "NH3_X <=> NH3 + X",
#     kinetics = SurfaceArrhenius(
#         A = (1E13, '1/s'),  
#         n = 0.0,
#         Ea = (20.7, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_vdW""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# This is R44 in Appendix A
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
    index = 45,
    label = "NH2 + X <=> NH2_X",
    kinetics = StickingCoefficient(
        A = 1,
        n = 0.0,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

This is R45 in Appendix A

This reaction is the least important ones for typical DOC conditions.
""",
    metal = "Pt",
    facet = "111",
)

# Reverse reaction of R45
# entry(
#     index = 46,
#     label = "NH2_X <=> NH2 + X",
#     kinetics = SurfaceArrhenius(
#         A = (1E13, '1/s'),  
#         n = 0.0,
#         Ea = (54.6, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_Single""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# This is R46 in Appendix A

# This reaction is the least important ones for typical DOC conditions.
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
    index = 47,
    label = "NH + X <=> NH_X",
    kinetics = StickingCoefficient(
        A = 1,
        n = 0.0,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Double""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

This is R47 in Appendix A

This reaction is the least important ones for typical DOC conditions.
""",
    metal = "Pt",
    facet = "111",
)

# Reverse reaction of R47
# entry(
#     index = 48,
#     label = "NH_X <=> NH + X",
#     kinetics = SurfaceArrhenius(
#         A = (1E13, '1/s'),  
#         n = 0.0,
#         Ea = (83, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_Double""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# This is R48 in Appendix A

# This reaction is the least important ones for typical DOC conditions.
# """,
#     metal = "Pt",
#     facet = "111",
# )

# Reverse reaction of R50
# entry(
#     index = 49,
#     label = "NH3_X + X <=> NH2_X + H_X",
#     kinetics = SurfaceArrhenius(
#         A = (4E19, 'cm^2/(mol*s)'), 
#         n = 0.0,
#         Ea = (21.5, 'kcal/mol'),
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Dissociation_vdW""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

# This is R49 in Appendix A
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
    index = 50,
    label = "NH2_X + H_X <=> NH3_X + X",
    kinetics = SurfaceArrhenius(
        A = (4E19, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (7.3, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R50 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

# Reverse reaction of R52
# entry(
#     index = 51,
#     label = "NH2_X + X <=> NH_X + H_X",
#     kinetics = SurfaceArrhenius(
#         A = (4E19, 'cm^2/(mol*s)'), 
#         n = 0.0,
#         Ea = (18.7, 'kcal/mol'),
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Dissociation""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

# This is R51 in Appendix A
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
    index = 52,
    label = "NH_X + H_X <=> NH2_X + X",
    kinetics = SurfaceArrhenius(
        A = (4E19, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (16.5, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R52 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

# Reverse reaction of R54
# entry(
#     index = 53,
#     label = "NH_X + X <=> N_X + H_X",
#     kinetics = SurfaceArrhenius(
#         A = (4E19, 'cm^2/(mol*s)'), 
#         n = 0.0,
#         Ea = (19, 'kcal/mol'),
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Dissociation""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

# This is R53 in Appendix A
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
    index = 54,
    label = "N_X + H_X <=> NH_X + X",
    kinetics = SurfaceArrhenius(
        A = (4E19, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (24.5, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R54 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

# Reverse reaction of R56
# entry(
#     index = 55,
#     label = "NH3_X + O_X <=> NH2_X + OH_X",
#     kinetics = SurfaceArrhenius(
#         A = (4E19, 'cm^2/(mol*s)'), 
#         n = 0.0,
#         Ea = (12.5, 'kcal/mol'),   
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Abstraction_vdW""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

# This is R55 in Appendix A
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
    index = 56,
    label = "NH2_X + OH_X <=> NH3_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (4E19, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (16.7, 'kcal/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R56 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

# Reverse reaction of R58
# entry(
#     index = 57,
#     label = "NH_X + OH_X <=> NH2_X + O_X",
#     kinetics = SurfaceArrhenius(
#         A = (4E19, 'cm^2/(mol*s)'), 
#         n = 0.0,
#         Ea = (24.8, 'kcal/mol'),   
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Abstraction""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

# This is R57 in Appendix A
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
    index = 58,
    label = "NH2_X + O_X <=> NH_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (4E19, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (8.6, 'kcal/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R58 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

# Reverse reaction of R60
# entry(
#     index = 59,
#     label = "N_X + OH_X <=> NH_X + O_X",
#     kinetics = SurfaceArrhenius(
#         A = (4E19, 'cm^2/(mol*s)'), 
#         n = 0.0,
#         Ea = (39.6, 'kcal/mol'),   
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Abstraction""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

# This is R59 in Appendix A
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
    index = 60,
    label = "NH_X + O_X <=> N_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (4E19, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (15.8, 'kcal/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R60 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

# Reverse reaction of R62
# entry(
#     index = 61,
#     label = "NH2_X + H2O_X <=> NH3_X + OH_X",
#     kinetics = SurfaceArrhenius(
#         A = (4E19, 'cm^2/(mol*s)'), 
#         n = 0.0,
#         Ea = (3.5, 'kcal/mol'),   
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Abstraction_Single_vdW""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

# This is R61 in Appendix A
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
    index = 62,
    label = "NH3_X + OH_X <=> NH2_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (4E19, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (12, 'kcal/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_Single_vdW""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R62 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

# Reverse reaction of R64
# entry(
#     index = 63,
#     label = "NH_X + H2O_X <=> NH2_X + OH_X",
#     kinetics = SurfaceArrhenius(
#         A = (4E19, 'cm^2/(mol*s)'), 
#         n = 0.0,
#         Ea = (16.4, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Abstraction_vdW""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

# This is R63 in Appendix A
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
    index = 64,
    label = "NH2_X + OH_X <=> NH_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (4E19, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (12.9, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R64 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

# Reverse reaction of R66
# entry(
#     index = 65,
#     label = "N_X + H2O_X <=> NH_X + OH_X",
#     kinetics = SurfaceArrhenius(
#         A = (4E19, 'cm^2/(mol*s)'), 
#         n = 0.0,
#         Ea = (33.4, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Abstraction_vdW""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

# This is R65 in Appendix A
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
    index = 66,
    label = "NH_X + OH_X <=> N_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (4E19, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (22.2, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R66 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

#---------------------NO oxidation----------------------------------

entry(
    index = 67,
    label = "NO + X <=> NO_X",
    kinetics = StickingCoefficient(
        A = 0.88,
        n = 0.0,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

This is R67 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

# Reverse reaction of R67
# entry(
#     index = 68,
#     label = "NO_X <=> NO + X",
#     kinetics = SurfaceArrhenius(
#         A = (1E16, '1/s'),  
#         n = 0.0,
#         Ea = (30.5, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_Single""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# This is R68 in Appendix A
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
    index = 69,
    label = "NO2 + X <=> NO2_X",
    kinetics = StickingCoefficient(
        A = 1,
        n = 0.0,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

This is R69 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

# Reverse reaction of R69
# entry(
#     index = 70,
#     label = "NO2_X <=> NO2 + X",
#     kinetics = SurfaceArrhenius(
#         A = (1E13, '1/s'),  
#         n = 0.0,
#         Ea = (23.5, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_Single""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# This is R70 in Appendix A
# """,
#     metal = "Pt",
#     facet = "111",
# )

# Reverse reaction of R72
# entry(
#     index = 71,
#     label = "NO_X + X <=> N_X + O_X",
#     kinetics = SurfaceArrhenius(
#         A = (4E19, 'cm^2/(mol*s)'),  
#         n = 0.0,
#         Ea = (31.7, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Nitrogen/51""",
#    longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

# This is R71 in Appendix A
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
    index = 72,
    label = "N_X + O_X <=> NO_X + X",
    kinetics = SurfaceArrhenius(
        A = (4E19, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (43.8, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Nitrogen/51""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R72 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

# Reverse reaction of R74
# entry(
#     index = 73,
#     label = "NO_X + H_X <=> N_X + OH_X",
#     kinetics = SurfaceArrhenius(
#         A = (4E19, 'cm^2/(mol*s)'),  
#         n = 0.0,
#         Ea = (4.6, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

# This is R73 in Appendix A
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
    index = 74,
    label = "N_X + OH_X <=> NO_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (4E19, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (35.1, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R74 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

# Reverse reaction of R76
# entry(
#     index = 75,
#     label = "NO_X + H_X <=> NH_X + O_X",
#     kinetics = SurfaceArrhenius(
#         A = (4E19, 'cm^2/(mol*s)'),  
#         n = 0.0,
#         Ea = (8.2, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

# This is R75 in Appendix A
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
    index = 76,
    label = "NH_X + O_X <=> NO_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (4E19, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (14.9, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R76 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 77,
    label = "NO_X + OH_X <=> NO2_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (4E19, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (38.2, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R77 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

# Reverse reaction of R77
# entry(
#     index = 78,
#     label = "NO2_X + H_X <=> NO_X + OH_X",
#     kinetics = SurfaceArrhenius(
#         A = (4E19, 'cm^2/(mol*s)'),  
#         n = 0.0,
#         Ea = (0, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

# This is R78 in Appendix A
# """,
#     metal = "Pt",
#     facet = "111",
# )

# Reverse reaction of R80
# entry(
#     index = 79,
#     label = "NO2_X + X <=> NO_X + O_X",
#     kinetics = SurfaceArrhenius(
#         A = (4E19, 'cm^2/(mol*s)'),  
#         n = -0.93,
#         Ea = (1.4, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Dissociation""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

# This is R79 in Appendix A
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
    index = 80,
    label = "NO_X + O_X <=> NO2_X + X",
    kinetics = SurfaceArrhenius(
        A = (1.2E21, 'cm^2/(mol*s)'),  
        n = 0.93,
        Ea = (21.2, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 3E12(1/s)/2.5E-9(mol/cm^2) = 1.2E21 cm^2/(mol*s)

This is R80 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

#---------------------HCN oxidation----------------------------------


entry(
    index = 81,
    label = "HCN + X <=> HCN_X",
    kinetics = StickingCoefficient(
        A = 1,
        n = 0.0,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

This is R81 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

# Reverse reaction of R81
# entry(
#     index = 82,
#     label = "HCN_X <=> HCN + X",
#     kinetics = SurfaceArrhenius(
#         A = (1E13, '1/s'),  
#         n = 0.0,
#         Ea = (21.3, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_vdW""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# This is R82 in Appendix A
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
    index = 83,
    label = "CN + X <=> CN_X",
    kinetics = StickingCoefficient(
        A = 1,
        n = 0.0,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

This is R83 in Appendix A

This reaction is the least important ones for typical DOC conditions.
""",
    metal = "Pt",
    facet = "111",
)

# Reverse reaction of R83
# entry(
#     index = 84,
#     label = "CN_X <=> CN + X",
#     kinetics = SurfaceArrhenius(
#         A = (1E13, '1/s'),  
#         n = 0.0,
#         Ea = (78.2, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_Single""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# This is R84 in Appendix A

# This reaction is the least important ones for typical DOC conditions.
# """,
#     metal = "Pt",
#     facet = "111",
# )

# Reverse reaction of R86
# entry(
#     index = 85,
#     label = "HCN_X + X <=> CN_X + H_X",
#     kinetics = SurfaceArrhenius(
#         A = (4E19, 'cm^2/(mol*s)'),  
#         n = 0.0,
#         Ea = (21.1, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Dissociation_vdW""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

# This is R85 in Appendix A
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
    index = 86,
    label = "CN_X + H_X <=> HCN_X + X",
    kinetics = SurfaceArrhenius(
        A = (4E19, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (13.2, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R86 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

# Reverse reaction of R88
# entry(
#     index = 87,
#     label = "HCN_X + O_X <=> CN_X + OH_X",
#     kinetics = SurfaceArrhenius(
#         A = (4E19, 'cm^2/(mol*s)'),  
#         n = 0.0,
#         Ea = (17.1, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Abstraction_vdW""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

# This is R87 in Appendix A
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
    index = 88,
    label = "CN_X + OH_X <=> HCN_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (4E19, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (27.6, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R88 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

# Reverse reaction of R90
# entry(
#     index = 89,
#     label = "HCN_X + OH_X <=> CN_X + H2O_X",
#     kinetics = SurfaceArrhenius(
#         A = (4E19, 'cm^2/(mol*s)'),  
#         n = 0.0,
#         Ea = (5.7, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Abstraction_Single_vdW""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

# This is R89 in Appendix A
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
    index = 90,
    label = "CN_X + H2O_X <=> HCN_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (4E19, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (3.4, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_Single_vdW""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R90 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

# Reverse reaction of R92
# entry(
#     index = 91,
#     label = "CN_X + O_X <=> C_X + NO_X",
#     kinetics = SurfaceArrhenius(
#         A = (4E19, 'cm^2/(mol*s)'),  
#         n = 0.0,
#         Ea = (8.9, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

# This is R91 in Appendix A
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
    index = 92,
    label = "C_X + NO_X <=> CN_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (4E19, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (4.7, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R92 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

# Reverse reaction of R94
# entry(
#     index = 93,
#     label = "CO_X + N_X <=> CN_X + O_X",
#     kinetics = SurfaceArrhenius(
#         A = (4E19, 'cm^2/(mol*s)'),  
#         n = 0.0,
#         Ea = (76.5, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

# This is R93 in Appendix A
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
    index = 94,
    label = "CN_X + O_X <=> CO_X + N_X",
    kinetics = SurfaceArrhenius(
        A = (4E19, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (15.4, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R94 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

#---------------------CH2O oxidation---------------------------------

entry(
    index = 95,
    label = "CH2O + X <=> CH2O_X",
    kinetics = StickingCoefficient(
        A = 1,  
        n = 0.0,
        Ea = (0, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

This is R95 in Appendix A
""",
	metal = "Pt",
    facet = "111",
)

# Reverse reaction of R95
# entry(
#     index = 96,
#     label = "CH2O_X <=> CH2O + X",
#     kinetics = SurfaceArrhenius(
#         A = (1E13, '1/s'),  
#         n = 0.0,
#         Ea = (14.7, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_vdW""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# This is R96 in Appendix A
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 97,
    label = "HCO + X <=> HCO_X",
    kinetics = StickingCoefficient(
        A = 1,  
        n = 0.0,
        Ea = (0, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

This is R97 in Appendix A

This reaction is the least important ones for typical DOC conditions.
""",
	metal = "Pt",
    facet = "111",
)

# Reverse reaction of R97
# entry(
#     index = 98,
#     label = "HCO_X <=> HCO + X",
#     kinetics = SurfaceArrhenius(
#         A = (1E13, '1/s'),  
#         n = 0.0,
#         Ea = (54.4, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_Single""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# This is R98 in Appendix A

# This reaction is the least important ones for typical DOC conditions.
# """,
# 	metal = "Pt",
#     facet = "111",
# )

# Reverse reaction of R100
# entry(
#     index = 99,
#     label = "CH2O_X + X <=> HCO_X + H_X",
#     kinetics = SurfaceArrhenius(
#         A = (4E19, 'cm^2/(mol*s)'),   
#         n = 0.0,
#         Ea = (8.1, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Dissociation_vdW""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

# This is R99 in Appendix A
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 100,
    label = "HCO_X + H_X <=> CH2O_X + X",
    kinetics = SurfaceArrhenius(
        A = (4E19, 'cm^2/(mol*s)'),   
        n = 0.0,
        Ea = (20.7, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R100 in Appendix A
""",
	metal = "Pt",
    facet = "111",
)

entry(
    index = 101,
    label = "HCO_X + OH_X <=> CH2O_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (4E19, 'cm^2/(mol*s)'),   
        n = 0.0,
        Ea = (30.9, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R101 in Appendix A
""",
	metal = "Pt",
    facet = "111",
)

# Reverse reaction of R101
# entry(
#     index = 102,
#     label = "CH2O_X + O_X <=> HCO_X + OH_X",
#     kinetics = SurfaceArrhenius(
#         A = (4E19, 'cm^2/(mol*s)'),   
#         n = 0.0,
#         Ea = (0, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Abstraction_vdW""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

# This is R102 in Appendix A
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 103,
    label = "HCO_X + H2O_X <=> CH2O_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (4E19, 'cm^2/(mol*s)'),   
        n = 0.0,
        Ea = (18.3, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_Single_vdW""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R103 in Appendix A
""",
	metal = "Pt",
    facet = "111",
)

# Reverse reaction of R103
# entry(
#     index = 104,
#     label = "CH2O_X + OH_X <=> HCO_X + H2O_X",
#     kinetics = SurfaceArrhenius(
#         A = (4E19, 'cm^2/(mol*s)'),   
#         n = 0.0,
#         Ea = (0, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Abstraction_Single_vdW""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

# This is R104 in Appendix A
# """,
# 	metal = "Pt",
#     facet = "111",
# )

# Reverse reaction of R106
# entry(
#     index = 105,
#     label = "HCO_X + X <=> CO_X + H_X",
#     kinetics = SurfaceArrhenius(
#         A = (4E19, 'cm^2/(mol*s)'),   
#         n = 0.0,
#         Ea = (0, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Dissociation_vdW""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

# This is R105 in Appendix A
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 106,
    label = "CO_X + H_X <=> HCO_X + X",
    kinetics = SurfaceArrhenius(
        A = (4E19, 'cm^2/(mol*s)'),   
        n = 0.0,
        Ea = (30.8, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R106 in Appendix A
""",
	metal = "Pt",
    facet = "111",
)

entry(
    index = 107,
    label = "CO_X + OH_X <=> HCO_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (4E19, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (49.2, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R107 in Appendix A
""",
	metal = "Pt",
    facet = "111",
)

# Reverse reaction of R107
# entry(
#     index = 108,
#     label = "HCO_X + O_X <=> CO_X + OH_X",
#     kinetics = SurfaceArrhenius(
#         A = (6E20, 'cm^2/(mol*s)'),  
#         n = 0.0,
#         Ea = (0, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Abstraction""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1.5E12(1/s)/2.5E-9(mol/cm^2) = 6E20 cm^2/(mol*s)

# This is R108 in Appendix A
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 109,
    label = "CO_X + H2O_X <=> HCO_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (4E19, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (36.5, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R109 in Appendix A
""",
	metal = "Pt",
    facet = "111",
)

# Reverse reaction of R109
# entry(
#     index = 110,
#     label = "HCO_X + OH_X <=> CO_X + H2O_X",
#     kinetics = SurfaceArrhenius(
#         A = (4E19, 'cm^2/(mol*s)'),  
#         n = 0.0,
#         Ea = (0, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Abstraction_vdW""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

# This is R110 in Appendix A
# """,
# 	metal = "Pt",
#     facet = "111",
# )

#---------------------C foramtion and oxidation----------------------

entry(
    index = 111,
    label = "C + X <=> C_X",
    kinetics = StickingCoefficient(
        A = 1,
        n = 0.0,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Quadruple bonds""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

This is R111 in Appendix A

This reaction is the least important ones for typical DOC conditions.
""",
	metal = "Pt",
    facet = "111",
)

# Reverse reaction of R111
# entry(
#     index = 112,
#     label = "C_X <=> C + X",
#     kinetics = SurfaceArrhenius(
#         A = (1E13, '1/s'),  
#         n = 0.0,
#         Ea = (158.2, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_Quadruple bonds""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# This is R112 in Appendix A

# This reaction is the least important ones for typical DOC conditions.
# """,
# 	metal = "Pt",
#     facet = "111",
# )

# Reverse reaction of R114
# entry(
#     index = 113,
#     label = "CO_X + X <=> C_X + O_X",
#     kinetics = SurfaceArrhenius(
#         A = (4E19, 'cm^2/(mol*s)'),  
#         n = 0.0,
#         Ea = (54.4, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Deutschmann libraries""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

# This is R113 in Appendix A
# """,
# 	metal = "Pt",
#     facet = "111",
# )

entry(
    index = 114,
    label = "C_X + O_X <=> CO_X + X",
    kinetics = SurfaceArrhenius(
        A = (4E19, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (1.3, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Deutschmann libraries""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R114 in Appendix A
""",
	metal = "Pt",
    facet = "111",
)

entry(
    index = 115,
    label = "CO_X + CO_X <=> C_X + CO2_X",
    kinetics = SurfaceArrhenius(
        A = (4E19, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (48.3, 'kcal/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Deutschmann libraries""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R115 in Appendix A
""",
	metal = "Pt",
    facet = "111",
)

# Reverse reaction of R115
# entry(
#     index = 116,
#     label = "C_X + CO2_X <=> CO_X + CO_X",
#     kinetics = SurfaceArrhenius(
#         A = (4E19, 'cm^2/(mol*s)'),  
#         n = 0.0,
#         Ea = (0, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Deutschmann libraries""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

# This is R116 in Appendix A
# """,
# 	metal = "Pt",
#     facet = "111",
# )

#---------------------N2O and C2N2 formation/decomposition-----------

entry(
    index = 117,
    label = "N2O + X <=> N2O_X",
    kinetics = StickingCoefficient(
        A = 1,
        n = 0.0,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Double""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

This is R117 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

# Reverse reaction of R117
# entry(
#     index = 118,
#     label = "N2O_X <=> N2O + X",
#     kinetics = SurfaceArrhenius(
#         A = (1E13, '1/s'),  
#         n = 0.0,
#         Ea = (6.7, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_Double""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# This is R118 in Appendix A
# """,
#     metal = "Pt",
#     facet = "111",
# )

# Reverse reaction of R120
# entry(
#     index = 119,
#     label = "N2O_X + X <=> N_X + NO_X",
#     kinetics = SurfaceArrhenius(
#         A = (4E19, 'cm^2/(mol*s)'),   
#         n = 0.0,
#         Ea = (3.9, 'kcal/mol'), 
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Dissociation""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

# This is R119 in Appendix A
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
    index = 120,
    label = "N_X + NO_X <=> N2O_X + X",
    kinetics = SurfaceArrhenius(
        A = (4E19, 'cm^2/(mol*s)'),   
        n = 0.0,
        Ea = (19.8, 'kcal/mol'), 
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R120 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 121,
    label = "C2N2 + X <=> C2N2_X",
    kinetics = StickingCoefficient(
        A = 1,
        n = 0.0,
        Ea = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

This is R121 in Appendix A

This reaction is the least important ones for typical DOC conditions.
""",
    metal = "Pt",
    facet = "111",
)

# Reverse reaction of R121
# entry(
#     index = 122,
#     label = "C2N2_X <=> C2N2 + X",
#     kinetics = SurfaceArrhenius(
#         A = (1E13, '1/s'),  
#         n = 0.0,
#         Ea = (21, 'kcal/mol'),  
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Adsorption_vdW""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# This is R122 in Appendix A

# This reaction is the least important ones for typical DOC conditions.
# """,
#     metal = "Pt",
#     facet = "111",
# )

# Reverse reaction of R124
# entry(
#     index = 123,
#     label = "C2N2_X + X <=> CN_X + CN_X",
#     kinetics = SurfaceArrhenius(
#         A = (4E19, 'cm^2/(mol*s)'),   
#         n = 0.0,
#         Ea = (29.6, 'kcal/mol'), 
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Surface_Dissociation_vdW""",
#     longDesc = u"""
# "A detailed microkinetic model for diesel engine emissions oxidation 
# on platinum based diesel oxidation catalysts (DOC)"
# Hom Sharma & Ashish Mhadeshwar. (2012). 
# Applied Catalysis B: Environmental, 127, 190-204
# DOI: 10.1016/j.apcatb.2012.08.021

# Surface site density used in this paper is 2.5E-9 mol/cm^2
# A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

# This is R123 in Appendix A

# This reaction is the least important ones for typical DOC conditions.
# """,
#     metal = "Pt",
#     facet = "111",
# )

entry(
    index = 124,
    label = "CN_X + CN_X <=> C2N2_X + X",
    kinetics = SurfaceArrhenius(
        A = (4E19, 'cm^2/(mol*s)'),   
        n = 0.0,
        Ea = (28.1, 'kcal/mol'), 
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R124 in Appendix A

This reaction is the least important ones for typical DOC conditions.
""",
    metal = "Pt",
    facet = "111",
)
