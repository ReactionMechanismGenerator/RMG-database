#!/usr/bin/env python
# encoding: utf-8

name = "Popa_Rh111"
shortDesc = u""
longDesc = u"""
Based primarily on 
"Ab initio density-functional theory study of 
NHx dehydrogenation and reverse reactions on the Rh(111) surface"
C. Popa, W. K. Offermans, R. A. van Santen, and A. P. J. Jansen
American Physical Society 2006, Vol. 74, Iss. 15—15
https://doi.org/10.1103/PhysRevB.74.155428

and

"Density-functional theory study of NHx oxidation 
and reverse reactions on the Rh (111) surface."
C. Popa, R. A. van Santen, and A. P. J. JansenJ.
Phys. Chem. C 2007, 111, 9839– 9852.
https://doi.org/10.1021/jp071072g
"""

#top <=> bridge + hcp
entry(
    index = 1,
    label = "NH3_X + X <=> NH2_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (8.21E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (109033.7, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""
Based primarily on "Ab initio density-functional theory study of 
NHx dehydrogenation and reverse reactions on the Rh(111) surface"
C. Popa, W. K. Offermans, R. A. van Santen, and A. P. J. Jansen
American Physical Society Vol. 74, Iss. 15—15, 2006
https://doi.org/10.1103/PhysRevB.74.155428

This is reaction 1 in TABLE VI.

This reaction used RMG's surface site density of Rh111 = 2.656E-09(mol/cm^2) to calculate the A factor.
A (at 300K)= 2.18E13(1/s)/2.656E-9(mol/cm^2) = 8.21E21 cm^2/(mol*s)
Ea = 1.13eV = 109033.7J/mol
""",
    metal = "Rh",
    facet = "111",
)

#bridge <=> fcc + fcc
entry(
    index = 2,
    label = "NH2_X + X <=> NH_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (6.33E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (92630.4, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
Based primarily on "Ab initio density-functional theory study of 
NHx dehydrogenation and reverse reactions on the Rh(111) surface"
C. Popa, W. K. Offermans, R. A. van Santen, and A. P. J. Jansen
American Physical Society Vol. 74, Iss. 15—15, 2006
https://doi.org/10.1103/PhysRevB.74.155428

This is reaction 3 in TABLE VI.

This reaction used RMG's surface site density of Rh111 = 2.656E-09(mol/cm^2) to calculate the A factor.
A (at 300K)= 1.68E13(1/s)/2.656E-9(mol/cm^2) = 6.33E21 cm^2/(mol*s)
Ea = 0.86eV = 92630.4J/mol
""",
    metal = "Rh",
    facet = "111",
)
#hcp <=> hcp + hcp
entry(
    index = 3,
    label = "NH_X + X <=> N_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (7.94E21, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (97454.9, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
Based primarily on "Ab initio density-functional theory study of 
NHx dehydrogenation and reverse reactions on the Rh(111) surface"
C. Popa, W. K. Offermans, R. A. van Santen, and A. P. J. Jansen
American Physical Society Vol. 74, Iss. 15—15, 2006
https://doi.org/10.1103/PhysRevB.74.155428

This is reaction 7 in TABLE VI.

This reaction used RMG's surface site density of Rh111 = 2.656E-09(mol/cm^2) to calculate the A factor.
A (at 300K)= 2.11E13(1/s)/2.656E-9(mol/cm^2) = 7.94E21 cm^2/(mol*s)
Ea = 1.91eV = 97454.9J/mol
""",
    metal = "Rh",
    facet = "111",
)

# top + hcp <=> bridge + top
entry(
    index = 4,
    label = "NH3_X +O_X <=> NH2_X + OH_X",
    kinetics = SurfaceArrhenius(
        A=(6.40E20, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (92630.4, 'J/mol'),   
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
Based primarily on 
"Density-functional theory study of NHx oxidation 
and reverse reactions on the Rh (111) surface."
C. Popa, R. A. van Santen, and A. P. J. JansenJ.
Phys. Chem. C 2007, 111, 9839– 9852.
https://doi.org/10.1021/jp071072g

This is reaction 2a. in TABLE 4.

This reaction used RMG's surface site density of Rh111 = 2.656E-09(mol/cm^2) to calculate the A factor.
A (at 300K)= 1.7E12(1/s)/2.656E-9(mol/cm^2) = 6.40E20 cm^2/(mol*s)
Ea = 0.96eV = 92630.4J/mol
""",
    metal = "Rh",
    facet = "111",
)

# brigde + fcc <=> hcp + top
entry(
    index = 5,
    label = "NH2_X +O_X <=> NH_X + OH_X",
    kinetics = SurfaceArrhenius(
        A=(6.29E21, 'cm^2/(mol*s)'),
        n = 0.0,
        Ea = (71402.6, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction""",
    longDesc = u"""
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

# hcp + hcp <=> hcp + top
entry(
    index = 6,
    label = "NH_X +O_X <=> N_X + OH_X",
    kinetics = SurfaceArrhenius(
        A=(28.32E21 , 'cm^2/(mol*s)'),
        n = 0.0,
        Ea = (84911.2, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction""",
    longDesc = u"""
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

# top + top <=> bridge + top
entry(
    index = 7,
    label = "NH3_X + OH_X <=> NH2_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A=(17.27E20, 'cm^2/(mol*s)'),
        n = 0.0,
        Ea = (23157.6, 'J/mol'), 
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_Single_vdW""",
    longDesc = u"""
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

# bridge + top + hcp + top
entry(
    index = 8,
    label = "NH2_X + OH_X <=> NH_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A=(1.50E21, 'cm^2/(mol*s)'),
        n = 0.0,
        Ea = (13508.6, 'J/mol'), 
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
Based primarily on 
"Density-functional theory study of NHx oxidation 
and reverse reactions on the Rh (111) surface."
C. Popa, R. A. van Santen, and A. P. J. JansenJ.
Phys. Chem. C 2007, 111, 9839– 9852.
https://doi.org/10.1021/jp071072g

This is reaction 3a. in TABLE 5.

This reaction used RMG's surface site density of Rh111 = 2.656E-09(mol/cm^2) to calculate the A factor.
A (at 300K)= 3.98E12(1/s)/2.656E-9(mol/cm^2) = 1.50E21 cm^2/(mol*s)
Ea = 0.14eV = 13508.6J/mol
""",
    metal = "Rh",
    facet = "111",
)

# hcp + top <=> hcp + top
entry(
    index = 9,
    label = "NH_X + OH_X <=> N_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A=(4.52E20, 'cm^2/(mol*s)'),
        n = 0.0,
        Ea = (22192.7, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Abstraction_vdW""",
    longDesc = u"""
Based primarily on 
"Density-functional theory study of NHx oxidation 
and reverse reactions on the Rh (111) surface."
C. Popa, R. A. van Santen, and A. P. J. JansenJ.
Phys. Chem. C 2007, 111, 9839– 9852.
https://doi.org/10.1021/jp071072g

This is reaction 6a. in TABLE 5.

This reaction used RMG's surface site density of Rh111 = 2.656E-09(mol/cm^2) to calculate the A factor.
A (at 300K)= 1.2E12(1/s)/2.656E-9(mol/cm^2) = 4.52E20 cm^2/(mol*s)
Ea = 0.23eV = 22192.7J/mol
""",
    metal = "Rh",
    facet = "111",
)

# hcp + fcc <=> top
entry(
    index = 10,
    label = "N_X + N_X  <=>  N2_X + X",
    kinetics = SurfaceArrhenius(
        A=(1.69E22, 'cm^2/(mol*s)'),
        n = 0.0,
        Ea = (1147629.7, 'J/mol'), 
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Based primarily on 
"Density-functional theory study of NHx oxidation 
and reverse reactions on the Rh (111) surface."
C. Popa, R. A. van Santen, and A. P. J. JansenJ.
Phys. Chem. C 2007, 111, 9839– 9852.
https://doi.org/10.1021/jp071072g

This is reaction 3a. in TABLE 6.

This reaction used RMG's surface site density of Rh111 = 2.656E-09(mol/cm^2) to calculate the A factor.
A (at 300K)= 4.48E13(1/s)/2.656E-9(mol/cm^2) = 1.69E22 cm^2/(mol*s)
Ea = 1.53eV = 147629.7J/mol
""",
    metal = "Rh",
    facet = "111",
)