#!/usr/bin/env python
# encoding: utf-8

name = "Duan_Ni211"
shortDesc = u""
longDesc = u"""
This library is built to import training reactions, based on:
"Structure sensitivity of ammonia decomposition 
over Ni catalysts: A computational and experimental study"
Duan et al. Fuel Processing Technology 108 (2013) 112–117
https://doi.org/10.1016/j.fuproc.2012.05.030
"""

entry(
    index = 1,
    label = "NH3_X + X <=> NH2_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (5.52E19, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (63683.4, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""
"Structure sensitivity of ammonia decomposition 
over Ni catalysts: A computational and experimental study"
Duan et al. Fuel Processing Technology 108 (2013) 112–117
https://doi.org/10.1016/j.fuproc.2012.05.030

This reaction used RMG's surface site density of Ni211 = 3.339E-9(mol/cm^2) to calculate the A factor.
A = k/exp(Ea/RT) = 2.85E7(1/s)/exp(63683.4J/mol / 8.314J/molK/873K) =  1.84E11/s
  = (1.84E11/s)/3.339E-9(mol/cm^2) = 5.52E19 cm^2/mol/s

Ea = 0.66eV = 63683.4J/mol

This is reaction 1 from Table 2
""",
    metal = "Ni",
    facet = "211",
)

entry(
    index = 2,
    label = "NH2_X + X <=> NH_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (2.31E20, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (86841, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"Structure sensitivity of ammonia decomposition 
over Ni catalysts: A computational and experimental study"
Duan et al. Fuel Processing Technology 108 (2013) 112–117
https://doi.org/10.1016/j.fuproc.2012.05.030

This reaction used RMG's surface site density of Ni211 = 3.339E-9(mol/cm^2) to calculate the A factor.
A = k/exp(Ea/RT) = 4.91E6(1/s)/exp(86841J/mol / 8.314J/molK/873K) = 7.71E11/s
  = (7.71E11/s)/3.339E-9(mol/cm^2) = 2.31E20 cm^2/mol/s

Ea = 0.9eV = 86841J/mol

This is reaction 2 from Table 2  
""",
    metal = "Ni",
    facet = "211",
)

entry(
    index = 3,
    label = "NH_X + X <=> N_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (3.36E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (100349.6, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"Structure sensitivity of ammonia decomposition 
over Ni catalysts: A computational and experimental study"
Duan et al. Fuel Processing Technology 108 (2013) 112–117
https://doi.org/10.1016/j.fuproc.2012.05.030

This reaction used RMG's surface site density of Ni211 = 3.339E-9(mol/cm^2) to calculate the A factor.
A = k/exp(Ea/RT) = 1.11E7(1/s)/exp(100349.6J/mol / 8.314J/molK/873K) = 1.12E13/s
  = (1.12E13/s)/3.339E-9(mol/cm^2) = 3.36E21 cm^2/mol/s

Ea = 1.04eV = 100349.6J/mol

This is reaction 3 from Table 2  
""",
    metal = "Ni",
    facet = "211",
)

entry(
    index = 4,
    label = "N_X + N_X <=> N2 + X + X",
    kinetics = SurfaceArrhenius(
        A = (4.90E20, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (285610.4, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""N2 Surface_Adsorption_Dissociative""",
    longDesc = u"""
"Structure sensitivity of ammonia decomposition 
over Ni catalysts: A computational and experimental study"
Duan et al. Fuel Processing Technology 108 (2013) 112–117
https://doi.org/10.1016/j.fuproc.2012.05.030

This reaction used RMG's surface site density of Ni211 = 3.339E-9(mol/cm^2) to calculate the A factor.
A = k/exp(Ea/RT) = 1.33E-5(1/s)/exp(285610.4J/mol / 8.314J/molK/873K) =  1.64E12/s
  = (1.64E12/s)/3.339E-9(mol/cm^2) = 4.90E20 cm^2/mol/s

Ea = 2.96eV = 285610.4J/mol

This is reaction 4 from Table 2   
""",
    metal = "Ni",
    facet = "211",
)
