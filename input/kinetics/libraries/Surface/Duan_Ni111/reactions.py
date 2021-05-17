#!/usr/bin/env python
# encoding: utf-8

name = "Duan_Ni111"
shortDesc = u""
longDesc = u"""
This library is built to import training reactions, based on:
"Ammonia decomposition on Fe(1 1 0), Co(1 1 1) and 
Ni(1 1 1) surfaces: A density functional theory study"
Duan et al. Journal of Molecular Catalysis A: Chemical 357 (2012) 81–86
https://doi.org/10.1016/j.molcata.2012.01.023

and

"Structure sensitivity of ammonia decomposition 
over Ni catalysts: A computational and experimental study"
Duan et al. Fuel Processing Technology 108 (2013) 112–117
https://doi.org/10.1016/j.fuproc.2012.05.030
"""

entry(
    index = 1,
    label = "NH3_X + X <=> NH2_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (4.35E15, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (107103.9, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""
"Ammonia decomposition on Fe(1 1 0), Co(1 1 1) and 
Ni(1 1 1) surfaces: A density functional theory study"
Duan et al. Journal of Molecular Catalysis A: Chemical 357 (2012) 81–86
https://doi.org/10.1016/j.molcata.2012.01.023

and

"Structure sensitivity of ammonia decomposition 
over Ni catalysts: A computational and experimental study"
Duan et al. Fuel Processing Technology 108 (2013) 112–117
https://doi.org/10.1016/j.fuproc.2012.05.030

This reaction used RMG's surface site density of Ni111 = 3.148E-9(mol/cm^2) to calculate the A factor.
A = k/exp(Ea/RT) = 5.35(1/s)/exp(107103.9J/mol / 8.314J/molK/873K) =  1.37E7/s
  = (1.37E7/s)/3.148E-9(mol/cm^2) = 4.35E15 cm^2/mol/s

Ea = 1.11eV = 107103.9J/mol

This is reaction 1 from Table 2
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 2,
    label = "NH2_X + X <=> NH_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (8.34E19, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (56929.1, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"Ammonia decomposition on Fe(1 1 0), Co(1 1 1) and 
Ni(1 1 1) surfaces: A density functional theory study"
Duan et al. Journal of Molecular Catalysis A: Chemical 357 (2012) 81–86
https://doi.org/10.1016/j.molcata.2012.01.023

and

"Structure sensitivity of ammonia decomposition 
over Ni catalysts: A computational and experimental study"
Duan et al. Fuel Processing Technology 108 (2013) 112–117
https://doi.org/10.1016/j.fuproc.2012.05.030

This reaction used RMG's surface site density of Ni111 = 3.148E-9(mol/cm^2) to calculate the A factor.
A = k/exp(Ea/RT) = 1.03E8(1/s)/exp(56929.1JJ/mol / 8.314J/molK/873K) = 2.63E11/s
  = (2.63E11/s)/3.148E-9(mol/cm^2) = 8.34E19cm^2/mol/s

Ea = 0.59eV = 56929.1J/mol

This is reaction 2 from Table 2  
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 3,
    label = "NH_X + X <=> N_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (2.46E19, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (107103.9, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"Ammonia decomposition on Fe(1 1 0), Co(1 1 1) and 
Ni(1 1 1) surfaces: A density functional theory study"
Duan et al. Journal of Molecular Catalysis A: Chemical 357 (2012) 81–86
https://doi.org/10.1016/j.molcata.2012.01.023

and

"Structure sensitivity of ammonia decomposition 
over Ni catalysts: A computational and experimental study"
Duan et al. Fuel Processing Technology 108 (2013) 112–117
https://doi.org/10.1016/j.fuproc.2012.05.030

This reaction used RMG's surface site density of Ni111 = 3.148E-9(mol/cm^2) to calculate the A factor.
A = k/exp(Ea/RT) = 3.02E4(1/s)/exp(107103.9J/mol / 8.314J/molK/873K) =  7.74E10/s
  = (7.74E10/s)/3.148E-9(mol/cm^2) = 2.46E19 cm^2/mol/s

Ea = 1.11eV = 107103.9J/mol

This is reaction 3 from Table 2  
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 4,
    label = "N_X + N_X <=> N2 + X + X",
    kinetics = SurfaceArrhenius(
        A = (3.62E20, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (179471.4, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""N2 Surface_Adsorption_Dissociative""",
    longDesc = u"""
"Ammonia decomposition on Fe(1 1 0), Co(1 1 1) and 
Ni(1 1 1) surfaces: A density functional theory study"
Duan et al. Journal of Molecular Catalysis A: Chemical 357 (2012) 81–86
https://doi.org/10.1016/j.molcata.2012.01.023

and

"Structure sensitivity of ammonia decomposition 
over Ni catalysts: A computational and experimental study"
Duan et al. Fuel Processing Technology 108 (2013) 112–117
https://doi.org/10.1016/j.fuproc.2012.05.030

This reaction used RMG's surface site density of Ni111 = 3.148E-9(mol/cm^2) to calculate the A factor.
A = k/exp(Ea/RT) = 2.08E1(1/s)/exp(179471.4J/mol / 8.314J/molK/873K) = 1.14E12/s
  = (1.14E12/s)/3.148E-9(mol/cm^2) = 3.62E20 cm^2/mol/s

Ea = 1.86eV = 179471.4J/mol

This is reaction 4 from Table 2   
""",
    metal = "Ni",
    facet = "111",
)
