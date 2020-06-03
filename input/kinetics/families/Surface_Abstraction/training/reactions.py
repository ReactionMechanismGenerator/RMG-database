#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Abstraction/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label = "CH2X_1 + HOX_3 <=> CH3X_4 + OX_5",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(1.39E17, 'm^2/(mol*s)'),
        n = 0.101,
        Ea=(19000.0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Deutschmann Ni""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R24
""",
	metal = "Ni",
)

entry(
    index = 2,
    label = "CHX_1 + HOX_3 <=> CH2X_4 + OX_5",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(4.40E18, 'm^2/(mol*s)'),
        n = 0.101,
        Ea=(42400.0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R26
""",
	metal = "Ni",
)

#Delgado has this reaction as exothermic. However, our own thermo has this reaction as endothermic. removing and replacing with reverse direction, R28.
#entry(
#    index = 27,
#    label = "OX_5 + CHX_4 <=> HOX_3 + CX_1 ",
#    degeneracy = 1,
#    kinetics = SurfaceArrhenius(
#        A=(2.47E17, 'm^2/(mol*s)'),
#        n = 0.312,
#        Ea=(57700.0, 'J/mol'),
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    #rank = 3,
#    shortDesc = u"""Default""",
#    longDesc = u"""
#"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
#Delgado et al
#Catalysts, 2015, 5, 871-904. Reaction R27
#""",
#    metal = "Ni",
#)

entry(
    index = 3,
    label = "HOX_3 + CX_1 <=> OX_5 + CHX_4 ",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(2.43E17, 'm^2/(mol*s)'),
        n = -0.312,
        Ea=(118900.0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R28
""",
	metal = "Ni",
)

entry(
    index = 4,
    label = "O* + HCO* <=> OH* + CO*",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(3.298e17, 'm^2/(mol*s)'),
        n = 0.,
        Ea=(0., 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 39 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
1.0e13 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 3.298e17 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 40,
    label = "H2NX + O* <=> OH* + HNX",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(
        A=(2.22e+21,'cm^2/(mol*s)'), 
        n=0, Ea=(78156.9,'J/mol'), 
        T0=(1,'K'), Tmin=(200,'K'), 
        Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pt111
Original entry: NH2_X +O_X <=> NH_X + OH_X
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 5.5E12(1/s)/2.483E-9(mol/cm^2) = 2.22E21 cm^2/(mol*s)
Ea = 0.81eV = 78156.9J/mol

This is R4 in Table S2 and S4""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 41,
    label = "HNX-2 + O* <=> OH* + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.14e+21,'cm^2/(mol*s)'), n=0, Ea=(154384,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pt111
Original entry: NH_X + O_X <=> N_X + OH_X
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 7.8E12(1/s)/2.483E-9(mol/cm^2) = 3.14E21 cm^2/(mol*s)
Ea = 1.6eV = 154384J/mol

This is R5 in Table S2 and S4
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 42,
    label = "H2NX + O* <=> OH* + HNX",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.457e+21,'cm^2/(mol*s)'), n=0, Ea=(87000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Offermans_Pt111
Original entry: NH2_X +O_X <=> NH_X + OH_X
"Ammonia oxidation on platinum : a density functional theory study of surface reactivity."
Offermans, W. K. (2007). Technische Universiteit Eindhoven. 
https://doi.org/10.6100/IR630067

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 300K) = 6.1E12(1/s)/2.483E-9(mol/cm^2) = 2.457E21 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 43,
    label = "HNX-2 + O* <=> OH* + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.061e+21,'cm^2/(mol*s)'), n=0, Ea=(84000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Offermans_Pt111
Original entry: NH_X + O_X <=> N_X + OH_X
"Ammonia oxidation on platinum : a density functional theory study of surface reactivity."
Offermans, W. K. (2007). Technische Universiteit Eindhoven. 
https://doi.org/10.6100/IR630067

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 300K) = 7.6E12(1/s)/2.483E-9(mol/cm^2) = 3.061E21 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 44,
    label = "H2NX + O* <=> OH* + HNX",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.47e+21,'cm^2/(mol*s)'), n=0, Ea=(106139,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Rh111
Original entry: NH2_X +O_X <=> NH_X + OH_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Rh111 = 2.656E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 1.1eV = 106139J/mol

This is reaction (4) in Table S3
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 45,
    label = "HNX-2 + O* <=> OH* + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.47e+21,'cm^2/(mol*s)'), n=0, Ea=(142805,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Rh111
Original entry: NH_X + O_X <=> N_X + OH_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Rh111 = 2.656E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 1.48eV = 142805.2J/mol

This is reaction (5) in Table S3
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 46,
    label = "H2NX + O* <=> OH* + HNX",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.44e+21,'cm^2/(mol*s)'), n=0, Ea=(104209,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pd211
Original entry: NH2_X +O_X <=> NH_X + OH_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd211 = 2.688E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 1.08eV = 104209.2J/mol

This is reaction (4) in Table S2
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 47,
    label = "HNX-2 + O* <=> OH* + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.44e+21,'cm^2/(mol*s)'), n=0, Ea=(23157.6,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pd211
Original entry: NH_X + O_X <=> N_X + OH_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd211 = 2.688E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 0.24eV = 23157.6J/mol

This is reaction (5) in Table S2
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 48,
    label = "H2NX + O* <=> OH* + HNX",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.47e+21,'cm^2/(mol*s)'), n=0, Ea=(85876.1,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pd111
Original entry: NH2_X +O_X <=> NH_X + OH_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd111 = 2.534E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 0.89eV = 85876.1J/mol

This is reaction (4) in Table S3
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 49,
    label = "HNX-2 + O* <=> OH* + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.47e+21,'cm^2/(mol*s)'), n=0, Ea=(133156,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pd111
Original entry: NH_X + O_X <=> N_X + OH_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd111 = 2.534E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 1.38eV = 133156.2J/mol

This is reaction (5) in Table S3
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 50,
    label = "H2NX + O* <=> OH* + HNX",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(6.29e+21,'cm^2/(mol*s)'), n=0, Ea=(71402.6,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Popa_Rh111
Original entry: NH2_X +O_X <=> NH_X + OH_X
Based primarily on 
"Density-functional theory study of NHx oxidation 
and reverse reactions on the Rh (111) surface."
C. Popa, R. A. van Santen, and A. P. J. JansenJ.
Phys. Chem. C 2007, 111, 9839– 9852.
https://doi.org/10.1021/jp071072g

This is reaction 4a. in TABLE 4.

This reaction used RMG's surface site density of Rh111 = 2.656E-09(mol/cm^2) to calculate the A factor.
A (at 300K)= 1.67E13(1/s)/2.656E-9(mol/cm^2) = 6.29E21 cm^2/(mol*s)
Ea = 0.74eV = 71402.6J/mol
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 51,
    label = "HNX-2 + O* <=> OH* + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.832e+22,'cm^2/(mol*s)'), n=0, Ea=(84911.2,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Popa_Rh111
Original entry: NH_X +O_X <=> N_X + OH_X
Based primarily on 
"Density-functional theory study of NHx oxidation 
and reverse reactions on the Rh (111) surface."
C. Popa, R. A. van Santen, and A. P. J. JansenJ.
Phys. Chem. C 2007, 111, 9839– 9852.
https://doi.org/10.1021/jp071072g

This is reaction 2a. in TABLE 4.

This reaction used RMG's surface site density of Rh111 = 2.656E-09(mol/cm^2) to calculate the A factor.
A (at 300K)= 2.21E13(1/s)/2.656E-9(mol/cm^2) = 8.32E21 cm^2/(mol*s)
Ea = 0.88eV = 84911.2J/mol
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 52,
    label = "HNX-2 + O* <=> OH* + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.03e+21,'cm^2/(mol*s)'), n=0, Ea=(58500,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Rebrov_Pt111
Original entry: NH_X + O_X <=> N_X + OH_X
"Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
https://doi.org/10.1016/S1385-8947(02)00068-2

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1E13(1/s)/2.483E-9(mol/cm^2) = 4.03E21 cm^2/(mol*s)

This is R7 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 53,
    label = "H2NX + O* <=> OH* + HNX",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(1.78e+21,'cm^2/(mol*s)'), n=0, Ea=(139910,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pt211
Original entry: NH2_X +O_X <=> NH_X + OH_X
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt211 = 2.634E-9(mol/cm^2) to calculate the A factor.
A = 4.7E12(1/s)/2.634E-9(mol/cm^2) = 1.78E21 cm^2/(mol*s)
Ea = 1.45eV = 139910.5J/mol

This is R4 in Table S2 and S4
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 54,
    label = "HNX-2 + O* <=> OH* + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.29e+21,'cm^2/(mol*s)'), n=0, Ea=(45350.3,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pt211
Original entry: NH_X + O_X <=> N_X + OH_X
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt211 = 2.634E-9(mol/cm^2) to calculate the A factor.
A = 3.4E12(1/s)/2.634E-9(mol/cm^2) = 1.29E21 cm^2/(mol*s)
Ea = 0.47eV = 45350.3J/mol

This is R5 in Table S2 and S4
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 55,
    label = "CH3X + O* <=> OH* + CH2X",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(7.93e+19,'cm^2/(mol*s)'), n=-0.23, Ea=(10.8,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Pt111
Original entry: CH3_X + O_X <=> CH2_X + OH_X
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

entry(
    index = 56,
    label = "HOX_3 + CHX_1 <=> CH2X_4 + OX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.43e+19,'cm^2/(mol*s)'), n=0.414, Ea=(44.7,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Pt111
Original entry: CH_X + OH_X <=> CH2_X + O_X
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

entry(
    index = 57,
    label = "HOX_3 + CX <=> CHX + OX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.57e+19,'cm^2/(mol*s)'), n=0.225, Ea=(27.7,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Pt111
Original entry: C_X + OH_X <=> CH_X + O_X
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

entry(
    index = 58,
    label = "CH3X + O* <=> OH* + CH2X",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(1.19e+20,'cm^2/(mol*s)'), n=-0.1906, Ea=(6.7,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Rh
Original entry: CH3_X + O_X <=> CH2_X + OH_X
"Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
Vlachos et al. (2008)
Journal of Catalysis,259(2), 211-222, 0021-9517
DOI: 10.1016/j.jcat.2008.08.008.D.G.

Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
A = 2.96E+11(1/s)/2.49E-9(mol/cm^2) = 1.19E+20 cm^2/(mol*s)

This is R63 in Table 4
""",
    metal = "Rh",
)



entry(
    index = 59,
    label = "H2NX + O_Pt <=> HNX + HO_Pt",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (2.4567e+17, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (87.0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 4 in "Modeling ammonia oxidation over a Pt (533) surface"
https://doi.org/10.1016/j.susc.2011.08.014

A factor from paper / surface site density of Pt
6.1e12 1/s / 2.483e-05 mol/m^2 = 1.51463e+18 m^2/(mol*s)
"""
)

entry(
    index = 60,
    label = "HNX-2 + O_Pt <=> NX + HO_Pt",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (4.027e+17, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (84.0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 5 in "Modeling ammonia oxidation over a Pt (533) surface"
https://doi.org/10.1016/j.susc.2011.08.014

A factor from paper / surface site density of Pt
1e13 1/s / 2.483e05 mol/m^2 = 2.483e+18 m^2/(mol*s)
"""
)
