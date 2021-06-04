#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Abstraction_Single_vdW/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label = "HOX + H3NX <=> H2NX + H2OX",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(1.97e22,'cm^2/(mol*s)'), n=0, Ea=(33771.5,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_Single_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pt111
Original entry: NH3_X + OH_X <=> NH2_X + H2O_X
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 4.9E13(1/s)/2.483E-9(mol/cm^2) = 1.97E22 cm^2/(mol*s)
Ea = 0.35eV = 33771.5J/mol

This is R6 in Table S2 and S4
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 2,
    label = "HOX + H3NX <=> H2NX + H2OX",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(6.444e19,'cm^2/(mol*s)'), n=0, Ea=(73000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_Single_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Offermans_Pt111
Original entry: NH3_X + OH_X <=> NH2_X + H2O_X
"Ammonia oxidation on platinum : a density functional theory study of surface reactivity."
Offermans, W. K. (2007). Technische Universiteit Eindhoven. 
https://doi.org/10.6100/IR630067

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 300K) = 1.6E11(1/s)/2.483E-9(mol/cm^2) = 6.444E19 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 3,
    label = "HOX + H3NX <=> H2NX + H2OX",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(2.47e21,'cm^2/(mol*s)'), n=0, Ea=(68507.9,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_Single_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Rh111
Original entry: NH3_X + OH_X <=> NH2_X + H2O_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Rh111 = 2.656E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 0.71eV = 68507.9J/mol

This is reaction (6) in Table S3
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 4,
    label = "HOX + H3NX <=> H2NX + H2OX",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(2.44e21,'cm^2/(mol*s)'), n=0, Ea=(70437.7,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_Single_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pd211
Original entry: NH3_X + OH_X <=> NH2_X + H2O_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd211 = 2.688E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 0.73eV = 70437.7J/mol

This is reaction (6) in Table S2
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 5,
    label = "HOX + H3NX <=> H2NX + H2OX",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(2.47e21,'cm^2/(mol*s)'), n=0, Ea=(44385.4,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_Single_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pd111
Original entry: NH3_X + OH_X <=> NH2_X + H2O_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd111 = 2.534E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 0.46eV = 44385.4J/mol

This is reaction (6) in Table S3
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 6,
    label = "HOX + H3NX <=> H2NX + H2OX",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(1.727e21,'cm^2/(mol*s)'), n=0, Ea=(23157.6,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_Single_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Popa_Rh111
Original entry: NH3_X + OH_X <=> NH2_X + H2O_X
Based primarily on 
"Density-functional theory study of NHx oxidation 
and reverse reactions on the Rh (111) surface."
C. Popa, R. A. van Santen, and A. P. J. JansenJ.
Phys. Chem. C 2007, 111, 9839– 9852.
https://doi.org/10.1021/jp071072g

This is reaction 1a. in TABLE 5.

This reaction used RMG's surface site density of Rh111 = 2.656E-09(mol/cm^2) to calculate the A factor.
A (at 300K)= 1.93E12(1/s)/2.656E-9(mol/cm^2) = 7.27E20 cm^2/(mol*s)
Ea = 0.24eV = 23157.6J/mol
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 7,
    label = "HOX + H3NX <=> H2NX + H2OX",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(3.11e21,'cm^2/(mol*s)'), n=0, Ea=(80086.7,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_Single_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pt211
Original entry: NH3_X + OH_X <=> NH2_X + H2O_X
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt211 = 2.634E-9(mol/cm^2) to calculate the A factor.
A = 8.2E12(1/s)/2.634E-9(mol/cm^2) = 3.11E21 cm^2/(mol*s)
Ea = 0.83eV = 80086.7J/mol

This is R6 in Table S2 and S4
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 8,
    label = "H2NX-2 + H4N2X <=> H3N2X + H3NX-2",
    degeneracy = 4.0,
    kinetics = SurfaceArrhenius(A=(3.38e20,'cm^2/(mol*s)'), n=0.156, Ea=(40526,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_Single_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Cu111
Original entry: N2H4_X + NH2_X <=> N2H3_X + NH3_X
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This reaction used RMG's surface site density of Cu111 = 2.943E-9(mol/cm^2) to estimate A factor.
A and n was calculated by numpy.linalg.lstsq from Table 1

This is R38 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 9,
    label = "H2NX-2 + H4N2X <=> H3N2X + H3NX-2",
    degeneracy = 4.0,
    kinetics = SurfaceArrhenius(A=(3.87e21,'cm^2/(mol*s)'), n=0, Ea=(19298,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_Single_vdW""",    
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Ir111
Original entry: N2H4_X + NH2_X <=> N2H3_X + NH3_X
"Mechanistic study of hydrazine decomposition on Ir(111)"
Alberto Roldan et al. Phys.Chem.Chem.Phys., 2020, 22, 3883
DOI: 10.1039/c9cp06525c

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2)
to estimate a default(1E13) A factor.
A = 1E13(1/s)/2.587E-9(mol/cm^2) = 3.87E21 cm^2/(mol*s)
Ea = 0.2eV = 19298J/mol

This is R16 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 10,
    label = "H2NX-2 + H2N2X <=> HN2X + H3NX-2",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(3.87e21,'cm^2/(mol*s)'), n=0, Ea=(98419.8,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_Single_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Ir111
Original entry: N2H2_X + NH2_X <=> N2H_X + NH3_X
"Mechanistic study of hydrazine decomposition on Ir(111)"
Alberto Roldan et al. Phys.Chem.Chem.Phys., 2020, 22, 3883
DOI: 10.1039/c9cp06525c

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2)
to estimate a default(1E13) A factor.
A = 1E13(1/s)/2.587E-9(mol/cm^2) = 3.87E21 cm^2/(mol*s)
Ea = 1.02eV = 98419.8J/mol

This is R20 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 11,
    label = "HOX + H3NX <=> H2NX + H2OX",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(4e+19,'cm^2/(mol*s)'), n=0, Ea=(12,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_Single_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Mhadeshwar_Pt111
Original entry: NH3_X + OH_X <=> NH2_X + H2O_X
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

entry(
    index = 12,
    label = "CNX + H2OX-2 <=> HOX-2 + CHNX",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(4e+19,'cm^2/(mol*s)'), n=0, Ea=(3.4,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_Single_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Mhadeshwar_Pt111
Original entry: CN_X + H2O_X <=> HCN_X + OH_X
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

entry(
    index = 13,
    label = "CHOX + H2OX-2 <=> HOX-2 + CH2OX",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(4e+19,'cm^2/(mol*s)'), n=0, Ea=(18.3,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_Single_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Mhadeshwar_Pt111
Original entry: HCO_X + H2O_X <=> CH2O_X + OH_X
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

entry(
    index = 14,
    label = "HOX + H3NX <=> H2NX + H2OX",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(2.33e21,'cm^2/(mol*s)'), n=0, Ea=(91665.5,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_Single_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Rh211
Original entry: NH3_X + OH_X <=> NH2_X + H2O_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Rh211 = 2.817E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 0.95eV = 91665.5J/mol

This is reaction (6) in Table S2
""",
    metal = "Rh",
    facet = "211",
)

