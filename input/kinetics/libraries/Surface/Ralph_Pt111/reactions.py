#!/usr/bin/env python
# encoding: utf-8

name = "Ralph_Pt111"
shortDesc = u""
longDesc = u"""
Based primarily on 
"Ammonia Oxidation over Polycrystalline Platinum: 
Surface Morphology and Kinetics at Atmospheric Pressure."
Krähnert, Ralph(2005) A Doctoral Thesis.
http://dx.doi.org/10.14279/depositonce-1270
"""

entry(
    index = 24,
    label = "N_X + O_X <=> NO_X + X",
    kinetics = SurfaceArrhenius(
        A = (4.91E16, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (135300, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Nitrogen/51""",
    longDesc = u"""
"Ammonia Oxidation over Polycrystalline Platinum: 
Surface Morphology and Kinetics at Atmospheric Pressure."
Krähnert, Ralph(2005) A Doctoral Thesis.
http://dx.doi.org/10.14279/depositonce-1270

A = k/exp(Ea/RT) = 9.34(mol/m^2/s)/exp(135300J/mol / 8.314J/molK / 298K) = 4.91E16 cm^2/mol/s
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 49,
    label = "N_X + N_X <=> N2 + X + X",
    kinetics = SurfaceArrhenius(
        A = (7.06E17, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (139000, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""N2 Surface_Adsorption_Dissociative""",
    longDesc = u"""
"Ammonia Oxidation over Polycrystalline Platinum: 
Surface Morphology and Kinetics at Atmospheric Pressure."
Krähnert, Ralph(2005) A Doctoral Thesis.
http://dx.doi.org/10.14279/depositonce-1270

A = k/exp(Ea/RT) = 64.2(mol/m^2/s)/exp(139000J/mol / 8.314J/molK / 298K) = 7.06E17 cm^2/mol/s
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 50,
    label = "O_X + O_X <=> O2 + X + X",
    kinetics = SurfaceArrhenius(
        A = (5.21E9, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (181000, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""O2 Surface_Adsorption_Dissociative""",
    longDesc = u"""
"Ammonia Oxidation over Polycrystalline Platinum: 
Surface Morphology and Kinetics at Atmospheric Pressure."
Krähnert, Ralph(2005) A Doctoral Thesis.
http://dx.doi.org/10.14279/depositonce-1270

A = k/exp(Ea/RT) = 1.09E-10(mol/m^2/s)/exp(181000J/mol / 8.314J/molK / 298K) = 5.21E9 cm^2/mol/s
""",
	metal = "Pt",
    facet = "111",
)

entry(
    index = 58,
    label = "NH3_X <=> NH3 + X",
    kinetics = SurfaceArrhenius(
        A = (3.09E9, '1/s'),  
        n = 0.0,
        Ea = (60900, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""
"Ammonia Oxidation over Polycrystalline Platinum: 
Surface Morphology and Kinetics at Atmospheric Pressure."
Krähnert, Ralph(2005) A Doctoral Thesis.
http://dx.doi.org/10.14279/depositonce-1270

A = k/exp(Ea/RT) = 2.17(mol/m^2/s)/exp(60900J/mol / 8.314J/molK / 298K) = 4.09E9 cm^2/mol/s
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 76,
    label = "NO_X <=> NO + X",
    kinetics = SurfaceArrhenius(
        A = (3.19E17, '1/s'),  
        n = 0.0,
        Ea = (154800, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""
"Ammonia Oxidation over Polycrystalline Platinum: 
Surface Morphology and Kinetics at Atmospheric Pressure."
Krähnert, Ralph(2005) A Doctoral Thesis.
http://dx.doi.org/10.14279/depositonce-1270

A = k/exp(Ea/RT) = 1.24(mol/m^2/s)/exp(154800J/mol / 8.314J/molK / 298K) = 3.19E17 cm^2/mol/s
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 80,
    label = "N_X + NO_X <=> N2O + X + X",
    kinetics = SurfaceArrhenius(
        A = (1.45E18, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (155200, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
"Ammonia Oxidation over Polycrystalline Platinum: 
Surface Morphology and Kinetics at Atmospheric Pressure."
Krähnert, Ralph(2005) A Doctoral Thesis.
http://dx.doi.org/10.14279/depositonce-1270

A = k/exp(Ea/RT) = 5.2(mol/m^2/s)/exp(155200J/mol / 8.314J/molK / 298K) = 1.45E18 cm^2/mol/s
""",
    metal = "Pt",
    facet = "111",
)