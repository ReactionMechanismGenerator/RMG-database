#!/usr/bin/env python
# encoding: utf-8

name = "Roldan_Ru0001"
shortDesc = u""
longDesc = u"""
Based primarily on 
"Kinetic and mechanistic analysis of NH3 decomposition 
on Ru(0001), Ru(111) and Ir(111) surfaces"
Alberto Roldan et al. Nanoscale Adv., 2021, 3, 1624
DOI: 10.1039/d1na00015b
"""
#skip R1

entry(
    index = 1,
    label = "NH3_X <=> NH3 + X",
    kinetics = SurfaceArrhenius(
        A = (1.29E8, '1/s'),  
        n = 0.0,
        Ea = (72149.60, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""
"Kinetic and mechanistic analysis of NH3 decomposition 
on Ru(0001), Ru(111) and Ir(111) surfaces"
Alberto Roldan et al. Nanoscale Adv., 2021, 3, 1624
DOI: 10.1039/d1na00015b

Ea was calculated from A factor and k rate constant in Table 3

This is D1 in Table 3
""",
    metal = "Ru",
    facet = "0001",
)

entry(
    index = 2,
    label = "NH3_X + X <=> NH2_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (4.14E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (117240.82, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""
"Kinetic and mechanistic analysis of NH3 decomposition 
on Ru(0001), Ru(111) and Ir(111) surfaces"
Alberto Roldan et al. Nanoscale Adv., 2021, 3, 1624
DOI: 10.1039/d1na00015b

This reaction used RMG's surface site density of Ru0001 = 2.630E-9(mol/cm^2) to calculate the A factor.
A = 1.09E13(1/s)/2.630E-9(mol/cm^2) = 4.14E21 cm^2/(mol*s)
Ea was calculated from A factor and k rate constant in Table 3

This is R1 in Table 3
""",
    metal = "Ru",
    facet = "0001",
)

#skip R2 (reverse reaction of R1)

entry(
    index = 3,
    label = "NH2_X + X <=> NH_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (1.52E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (62155.01, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"Kinetic and mechanistic analysis of NH3 decomposition 
on Ru(0001), Ru(111) and Ir(111) surfaces"
Alberto Roldan et al. Nanoscale Adv., 2021, 3, 1624
DOI: 10.1039/d1na00015b

This reaction used RMG's surface site density of Ru0001 = 2.630E-9(mol/cm^2) to calculate the A factor.
A = 4.01E12(1/s)/2.630E-9(mol/cm^2) = 1.52E21 cm^2/(mol*s)
Ea was calculated from A factor and k rate constant in Table 3

This is R3 in Table 3
""",
    metal = "Ru",
    facet = "0001",
)

#skip R4 (reverse reaction of R3)

entry(
    index = 4,
    label = "NH_X + X <=> N_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (2.71E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (99817.13, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"Kinetic and mechanistic analysis of NH3 decomposition 
on Ru(0001), Ru(111) and Ir(111) surfaces"
Alberto Roldan et al. Nanoscale Adv., 2021, 3, 1624
DOI: 10.1039/d1na00015b

This reaction used RMG's surface site density of Ru0001 = 2.630E-9(mol/cm^2) to calculate the A factor.
A = 7.13E12(1/s)/2.630E-9(mol/cm^2) = 2.71E21 cm^2/(mol*s)
Ea was calculated from A factor and k rate constant in Table 3

This is R5 in Table 3
""",
    metal = "Ru",
    facet = "0001",
)

#skip R6 (reverse reaction of R5)

entry(
    index = 5,
    label = "N_X + N_X <=> N2_X + X",
    kinetics = SurfaceArrhenius(
        A = (4.03E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (233750.36, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u""" Surface_Adsorption_vdW""",
    longDesc = u"""
"Kinetic and mechanistic analysis of NH3 decomposition 
on Ru(0001), Ru(111) and Ir(111) surfaces"
Alberto Roldan et al. Nanoscale Adv., 2021, 3, 1624
DOI: 10.1039/d1na00015b

This reaction used RMG's surface site density of Ru0001 = 2.630E-9(mol/cm^2) to estimate A factor.
A = 1.06E13(1/s)/2.630E-9(mol/cm^2) = 4.03E21 cm^2/(mol*s)
Ea was calculated from A factor and k rate constant in Table 3

This is R7 in Table 3
""",
    metal = "Ru",
    facet = "0001",
)

#skip R8 (reverse reaction of R7)
#skip D2 (reverse reaction of A2) 

entry(
    index = 6,
    label = "N2 + X <=> N2_X",
    kinetics = SurfaceArrhenius(
        A = (1.29E8, 'cm^3/(mol*s)'),  
        n = 0.0,
        Ea = (24482.97, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_vdW""",
    longDesc = u"""
"Kinetic and mechanistic analysis of NH3 decomposition 
on Ru(0001), Ru(111) and Ir(111) surfaces"
Alberto Roldan et al. Nanoscale Adv., 2021, 3, 1624
DOI: 10.1039/d1na00015b

Ea was calculated from A factor and k rate constant in Table 3

This is A2 in Table 3
""",
    metal = "Ru",
    facet = "0001",
)

entry(
    index = 7,
    label = "H_X + H_X <=> H2_X + X",
    kinetics = SurfaceArrhenius(
        A = (5.48E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (52021.02, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""
"Kinetic and mechanistic analysis of NH3 decomposition 
on Ru(0001), Ru(111) and Ir(111) surfaces"
Alberto Roldan et al. Nanoscale Adv., 2021, 3, 1624
DOI: 10.1039/d1na00015b

This reaction used RMG's surface site density of Ru0001 = 2.630E-9(mol/cm^2) to estimate A factor.
A = 1.33E13(1/s)/2.630E-9(mol/cm^2) = 5.48E21 cm^2/(mol*s)
Ea was calculated from A factor and k rate constant in Table 3

This is R9 in Table 3
""",
    metal = "Ru",
    facet = "0001",
)

#skip R10 (reverse reaction of R9) 
#skip A3 (reverse reaction of D3) 

entry(
    index = 8,
    label = "H2_X <=> H2 + X",
    kinetics = SurfaceArrhenius(
        A = (1.29E8, '1/s'),  
        n = 0.0,
        Ea = (24482.97, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""H2 Surface_Adsorption_vdW""",
    longDesc = u"""
"Kinetic and mechanistic analysis of NH3 decomposition 
on Ru(0001), Ru(111) and Ir(111) surfaces"
Alberto Roldan et al. Nanoscale Adv., 2021, 3, 1624
DOI: 10.1039/d1na00015b

Ea was calculated from A factor and k rate constant in Table 3

This is D3 in Table 3
""",
    metal = "Ru",
    facet = "0001",
)
