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
    rank = 3,
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
    rank = 3,
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
#    index = 3,
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
    index = 4,
    label = "HOX_3 + CX_1 <=> OX_5 + CHX_4 ",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(2.43E17, 'm^2/(mol*s)'),
        n = -0.312,
        Ea=(118900.0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R28
""",
	metal = "Ni",
)

entry(
    index = 5,
    label = "O* + HCO* <=> OH* + CO*",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(3.298e17, 'm^2/(mol*s)'),
        n = 0.,
        Ea=(0., 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 1,
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
    index = 6,
    label = "H2NX + O* <=> OH* + HNX",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.46e+21,'cm^2/(mol*s)'), n=0, Ea=(87000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Offermans_Pt111
Original entry: NH2_X +O_X <=> NH_X + OH_X
"Ammonia oxidation on platinum : a density functional theory study of surface reactivity."
Offermans, W. K. (2007). Technische Universiteit Eindhoven. 
https://doi.org/10.6100/IR630067

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 300K) = 6.1E12(1/s)/2.483E-9(mol/cm^2) = 2.46E21 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 7,
    label = "HNX-2 + O* <=> OH* + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.06e+21,'cm^2/(mol*s)'), n=0, Ea=(84000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Offermans_Pt111
Original entry: NH_X + O_X <=> N_X + OH_X
"Ammonia oxidation on platinum : a density functional theory study of surface reactivity."
Offermans, W. K. (2007). Technische Universiteit Eindhoven. 
https://doi.org/10.6100/IR630067

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 300K) = 7.6E12(1/s)/2.483E-9(mol/cm^2) = 3.06E21 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 8,
    label = "H2NX + O* <=> OH* + HNX",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(6.29e+21,'cm^2/(mol*s)'), n=0, Ea=(71402.6,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Popa_Rh111
Original entry: NH2_X +O_X <=> NH_X + OH_X
Based primarily on 
"Density-functional theory study of NHx oxidation 
and reverse reactions on the Rh (111) surface."
C. Popa, R. A. van Santen, and A. P. J. JansenJ.
Phys. Chem. C 2007, 111, 9839– 9852.
https://doi.org/10.1021/jp071072g

This reaction used RMG's surface site density of Rh111 = 2.656E-09(mol/cm^2) to calculate the A factor.
A (at 300K)= 1.67E13(1/s)/2.656E-9(mol/cm^2) = 6.29E21 cm^2/(mol*s)

Ea = 0.74eV = 71402.6J/mol

This is reaction 4a. of TABLE 4.
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 9,
    label = "HNX-2 + O* <=> OH* + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(8.32e+21,'cm^2/(mol*s)'), n=0, Ea=(84911.2,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Popa_Rh111
Original entry: NH_X +O_X <=> N_X + OH_X
Based primarily on 
"Density-functional theory study of NHx oxidation 
and reverse reactions on the Rh (111) surface."
C. Popa, R. A. van Santen, and A. P. J. JansenJ.
Phys. Chem. C 2007, 111, 9839– 9852.
https://doi.org/10.1021/jp071072g

This reaction used RMG's surface site density of Rh111 = 2.656E-09(mol/cm^2) to calculate the A factor.
A (at 300K)= 2.21E13(1/s)/2.656E-9(mol/cm^2) = 8.32E21 cm^2/(mol*s)

Ea = 0.88eV = 84911.2J/mol

This is reaction 2a. of TABLE 4.
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 10,
    label = "H2NX + O* <=> OH* + HNX",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(4.03e+21,'cm^2/(mol*s)'), n=0, Ea=(96490,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Rebrov_Pt111
Original entry: NH2_X + O_X <=> NH_X + OH_X
"Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
https://doi.org/10.1016/S1385-8947(02)00068-2

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1E13(1/s)/2.483E-9(mol/cm^2) = 4.03E21 cm^2/(mol*s)

This is R6 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 11,
    label = "HNX-2 + O* <=> OH* + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.03e+21,'cm^2/(mol*s)'), n=0, Ea=(58500,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Rebrov_Pt111
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
    index = 12,
    label = "H2NX + O* <=> OH* + HNX",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.22e+21,'cm^2/(mol*s)'), n=0, Ea=(78156.9,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Schneider_Pt111
Original entry: NH2_X +O_X <=> NH_X + OH_X
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 5.5E12(1/s)/2.483E-9(mol/cm^2) = 2.22E21 cm^2/(mol*s)
Ea = 0.81eV = 78156.9J/mol

This is R4 in Table S2 and S4
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 13,
    label = "HNX-2 + O* <=> OH* + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.14e+21,'cm^2/(mol*s)'), n=0, Ea=(154384,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Schneider_Pt111
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
    index = 14,
    label = "H2NX + O* <=> OH* + HNX",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(1.78e+21,'cm^2/(mol*s)'), n=0, Ea=(139910,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Schneider_Pt211
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
    index = 15,
    label = "HNX-2 + O* <=> OH* + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.29e+21,'cm^2/(mol*s)'), n=0, Ea=(45350.3,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Schneider_Pt211
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

