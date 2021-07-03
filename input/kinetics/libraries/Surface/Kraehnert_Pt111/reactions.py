#!/usr/bin/env python
# encoding: utf-8

name = "Kraehnert_Pt111"
shortDesc = u""
longDesc = u"""
Based primarily on 
"Kinetics of ammonia oxidation over Pt foil studied in a micro-structured quartz-reactor"
Kraehnert et al.(2008) 
Chemical Engineering Journal,137(2), 361-375
https://doi.org/10.1016/j.cej.2007.05.005
"""

entry(
    index = 1,
    label = "NH3_X <=> NH3 + X",
    kinetics = SurfaceArrhenius(
        A = (1.48E9, '1/s'),  
        n = 0.0,
        Ea = (60900, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""
"Kinetics of ammonia oxidation over Pt foil studied in a micro-structured quartz-reactor"
Kraehnert et al.(2008) 
Chemical Engineering Journal,137(2), 361-375
https://doi.org/10.1016/j.cej.2007.05.005

A = k/exp(-Ea/RT) = 2.17(1/s)/exp(-60900(J/mol)/8.314(J/mol/K)/658K) = 1.48E09 (1/s)

Table 3, R1
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 2,
    label = "O2 + X + X <=> O_X + O_X",
    kinetics = StickingCoefficient(
        A = 0.16293,  
        n = 0.0,
        Ea = (181000, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""O2 Surface_Adsorption_Dissociative""",
    longDesc = u"""
"Kinetics of ammonia oxidation over Pt foil studied in a micro-structured quartz-reactor"
Kraehnert et al.(2008) 
Chemical Engineering Journal,137(2), 361-375
https://doi.org/10.1016/j.cej.2007.05.005

A = ((2.94e2/Pa)/s)*(2.483e-9(mol/cm^2))*sqrt(2*pi*(32(g/mol))*the molar gas constant*(298 kelvin)) =0.16293
Table 3, R2
""",
	metal = "Pt",
    facet = "111",
)

entry(
    index = 3,
    label = "NO_X <=> NO + X",
    kinetics = SurfaceArrhenius(
        A = (2.41E16, '1/s'),  
        n = 0.0,
        Ea = (154800, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""
"Kinetics of ammonia oxidation over Pt foil studied in a micro-structured quartz-reactor"
Kraehnert et al.(2008) 
Chemical Engineering Journal,137(2), 361-375
https://doi.org/10.1016/j.cej.2007.05.005

A = k/exp(-Ea/RT) = 1.24(1/s)/exp(-154800(J/mol)/8.314(J/mol/K)/658K) = 2.41E16 (1/s)

Table 3, R4
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 4,
    label = "N_X + N_X <=> N2 + X + X",
    kinetics = SurfaceArrhenius(
        A = (6.96E16, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (139000, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""N2 Surface_Adsorption_Dissociative""",
    longDesc = u"""
"Kinetics of ammonia oxidation over Pt foil studied in a micro-structured quartz-reactor"
Kraehnert et al.(2008) 
Chemical Engineering Journal,137(2), 361-375
https://doi.org/10.1016/j.cej.2007.05.005

A = k/exp(-Ea/RT) = 64.2(m^2/mol/s)/exp(-139000(J/mol)/8.314(J/mol/K)/658K) = 6.96E16 cm^2/mol/s

Table 3, R5
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 5,
    label = "N_X + O_X <=> NO_X + X",
    kinetics = SurfaceArrhenius(
        A = (5.14E15, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (135300, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Nitrogen/51""",
    longDesc = u"""
"Kinetics of ammonia oxidation over Pt foil studied in a micro-structured quartz-reactor"
Kraehnert et al.(2008) 
Chemical Engineering Journal,137(2), 361-375
https://doi.org/10.1016/j.cej.2007.05.005

A = k/exp(-Ea/RT) = 9.34(cm^2/mol/s)/exp(-135300(J/mol)/8.314(J/mol/K)/658K) = 5.14E15 cm^2/mol/s

Table 3, R6
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 6,
    label = "N_X + NO_X <=> N2O + X + X",
    kinetics = SurfaceArrhenius(
        A = (1.09E17, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (155200, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
"Kinetics of ammonia oxidation over Pt foil studied in a micro-structured quartz-reactor"
Kraehnert et al.(2008) 
Chemical Engineering Journal,137(2), 361-375
https://doi.org/10.1016/j.cej.2007.05.005

A = k/exp(-Ea/RT) = 5.2(m^2/mol/s)/exp(-155200(J/mol)/8.314(J/mol*K)/658K) = 1.09E17 (cm^2/mol/s)

Table 3, R7
""",
    metal = "Pt",
    facet = "111",
)