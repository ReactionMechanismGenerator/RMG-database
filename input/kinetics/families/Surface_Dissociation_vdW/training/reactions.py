#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_vdW/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label = "NH3_X + X_4 <=> NH2_X + H*",
    degeneracy = 3,
    kinetics = SurfaceArrhenius(
        A = (5.723e22, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (78.99, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
    Micro-kinetic modeling of NH3 decomposition on Ni and its application to solid oxide fuel cells
    Deutschmann et al
    doi: 10.1016/j.ces.2011.07.007

    This is R7
""",
    metal = "Ni",
)

entry(
    index = 2,
    label = "CH4* + X_4 <=> CH3* + H*",
    degeneracy = 4,
    kinetics = SurfaceArrhenius(
        A = (1.54E21,'cm^2/(mol*s)'),
        n = 0.087,
        Ea = (55.8, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""R13
    test surface mechanism: based upon Olaf Deutschmann's work:
    "Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
    Delgado et al
    Catalysts, 2015, 5, 871-904""",
	metal = "Ni",
)

entry(
    index = 5,
    label = "NH3_X + X_4 <=> NH2_X + H*",
    degeneracy = 3,
    kinetics = SurfaceArrhenius(
        A = (2.13538e+17, 'm^2/(mol*s)'),
        n = 0,
        Ea = (93.0, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
    "Ammonia activation on platinum {1 1 1}: A density functional theory study"
    https://doi.org/10.1016/j.susc.2006.01.031

    A factor from paper / surface site density of Pt
    8.6e11 1/s / 2.483e-05 mol/m^2 = 2.13538e+17 m^2/(mol*s)
""",
    metal="Pt",
    facet="111",
)

entry(
    index = 3,
    label = "COOH* + H* <=> HCOOH* + X_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (2.308e18, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (0.73, 'eV/molecule'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 13 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
6.793e13 1/s / 2.943e‐5 mol/m^2 = 2.308e18 m^2/(mol*s)
""", 
    metal = "Cu",
)

entry(
    index = 4,
    label = "H2O* + X_4 <=> OH* + H*",
    degeneracy = 2,
    kinetics = SurfaceArrhenius(
        A = (4.879e15, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (1.39, 'eV/molecule'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 14 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
1.436e11 1/s / 2.943e‐5 mol/m^2 = 4.879e15 m^2/(mol*s)
""", 
    metal = "Cu",
)

#duplicate of 4
# entry(
#     index = 5,
#     label = "H2O* + X_4 <=> OH* + H*",
#     kinetics = SurfaceArrhenius(
#         A = (3.67E17, 'm^2/(mol*s)'),
#         n = -0.086,
#         Ea = (92.9, 'kJ/mol'),
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     rank = 10,
#     shortDesc = u"""Default""",
#     longDesc = u"""R29
#     test surface mechanism: based upon Olaf Deutschmann's work:
#     "Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
#     Delgado et al
#     Catalysts, 2015, 5, 871-904""",
# 	metal = "Ni",
# )

entry(
    index = 6,
    label = "HCOO* + H* <=> HCOOH_1* + X_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (4.424e18, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (0.91, 'eV/molecule'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 19 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
1.302e14 1/s / 2.943e‐5 mol/m^2 = 4.424e18 m^2/(mol*s)
""", 
    metal = "Cu",
)

entry(
    index = 7,
    label = "CH3O* + H* <=> CH3OH_2* + X_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (4.349e17, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (1.17, 'eV/molecule'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 25 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
1.28e13 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 4.349e17 m^2/(mol*s)
""", 
    metal = "Cu",
)

entry(
    index = 8,
    label = "HCO* + H* <=> CH2O* + X_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (1.932e17, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (0.47, 'eV/molecule'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 30 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
5.685e12 1/s / 2.943e‐5 mol/m^2 = 1.932e17 m^2/(mol*s)
""", 
    metal = "Cu",
)

entry(
    index = 9,
    label = "CH2OH* + H* <=> CH3OH_1* + X_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (2.783e17, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (0.51, 'eV/molecule'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 33 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
8.189e12 1/s / 2.943e‐5 mol/m^2 = 2.783e17 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 10,
    label = "HCOOH_2* + X_4 <=> HCO* + OH_2*",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (1.781e17, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (1.63, 'eV/molecule'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 34 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
5.242e12 1/s / 2.943e‐5 mol/m^2 = 1.781e17 m^2/(mol*s)
""", 
    metal = "Cu",
)

entry(
    index = 11,
    label = "X_4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(2.255e20,'cm^2/(mol*s)'), n=0, Ea=(93000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Offermans_Pt111
Original entry: NH3_X + X <=> NH2_X + H_X
"Ammonia oxidation on platinum : a density functional theory study of surface reactivity."
Offermans, W. K. (2007). Technische Universiteit Eindhoven. 
https://doi.org/10.6100/IR630067

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 300K)= 5.6E11(1/s)/2.483E-9(mol/cm^2) = 2.255E20 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 12,
    label = "X_4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(2.859e20,'cm^2/(mol*s)'), n=0, Ea=(91000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Novell_Pt111
Original entry: NH3_X + X <=> NH2_X + H_X
"Ammonia Dehydrogenation over Platinum-Group Metal Surfaces. Structure, Stability, and Reactivity of Adsorbed NHx Species"
Gerard Novell-Leruth et al. J. Phys. Chem. C 2007, 111, 2, 860–868
https://doi.org/10.1021/jp064742b

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 500K) = 7.1E11(1/s)/2.483E-9(mol/cm^2) = 2.859E20 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 13,
    label = "X_4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(2.08e23,'cm^2/(mol*s)'), n=0, Ea=(100350,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Rh111
Original entry: NH3_X + X <=> NH2_X + H_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Rh111 = 2.656E-9(mol/cm^2) to calculate the A factor.
Using the method proposed by Campbell et al. to calculate A actor.
Ea = 1.04eV = 100349.6J/mol

This is reaction (1) in Table S5
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 14,
    label = "H* + OH* <=> H2O* + X_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.47e21,'cm^2/(mol*s)'), n=0, Ea=(63683.4,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Rh111
Original entry: H_X + OH_X <=> H2O_X + X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Rh111 = 2.656E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 0.66eV = 63683.4J/mol

This is reaction (5) in Table S5
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 15,
    label = "X_4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(2.06e23,'cm^2/(mol*s)'), n=0, Ea=(97454.9,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pd211
Original entry: NH3_X + X <=> NH2_X + H_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd211 = 2.688E-9(mol/cm^2) to calculate the A factor.
Using the method proposed by Campbell et al. to calculate A actor.
Ea = 1.01eV = 97454.9/mol

This is reaction (1) in Table S4
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 16,
    label = "H* + OH* <=> H2O* + X_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.44e21,'cm^2/(mol*s)'), n=0, Ea=(91665.5,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pd211
Original entry: H_X + OH_X <=> H2O_X + X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd211 = 2.688E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 0.95eV = 91665.5J/mol

This is reaction (5) in Table S4
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 17,
    label = "X_4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(2.18e23,'cm^2/(mol*s)'), n=0, Ea=(104209,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pd111
Original entry: NH3_X + X <=> NH2_X + H_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd111 = 2.534E-9(mol/cm^2) to calculate the A factor.
Using the method proposed by Campbell et al. to calculate A actor.
Ea = 1.08eV = 104209.2J/mol

This is reaction (1) in Table S5
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 18,
    label = "H* + OH* <=> H2O* + X_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.47e21,'cm^2/(mol*s)'), n=0, Ea=(64648.3,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pd111
Original entry: H_X + OH_X <=> H2O_X + X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd111 = 2.534E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 0.67eV = 64648.3J/mol

This is reaction (5) in Table S5
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 19,
    label = "X_4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(8.21e21,'cm^2/(mol*s)'), n=0, Ea=(109034,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Popa_Rh111
Original entry: NH3_X + X <=> NH2_X + H_X
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

entry(
    index = 20,
    label = "X_4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(4.35e15,'cm^2/(mol*s)'), n=0, Ea=(107104,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Duan_Ni111
Original entry: NH3_X + X <=> NH2_X + H_X
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
    index = 21,
    label = "X_4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(5.52e19,'cm^2/(mol*s)'), n=0, Ea=(63683.4,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Duan_Ni211
Original entry: NH3_X + X <=> NH2_X + H_X
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
    index = 22,
    label = "X_4 + H2O* <=> OH* + H*",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(3.77e21,'cm^2/(mol*s)'), n=-0.118, Ea=(17.8,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Pt111
Original entry: H2O_X + X <=> H_X + OH_X
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 9.36E12(1/s)/2.483E-9(mol/cm^2) = 3.77E21 cm^2/(mol*s)

This is R15 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 23,
    label = "X_4 + CH3OH_2* <=> CH3O* + H*",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.15e19,'cm^2/(mol*s)'), n=0.102, Ea=(18.8,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Pt111
Original entry: CH3OH_X + X <=> CH3O_X + H_X
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 7.82E10(1/s)/2.483E-9(mol/cm^2) = 3.15E19 cm^2/(mol*s)

This is R93 in Table 2
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 24,
    label = "X_4 + CH2O* <=> HCO* + H*",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.88e19,'cm^2/(mol*s)'), n=0.27, Ea=(3.6,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Pt111
Original entry: CH2O_X + X <=> HCO_X + H_X
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 7.14E10(1/s)/2.483E-9(mol/cm^2) = 2.88E19 cm^2/(mol*s)

This is R97 in Table 2
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 25,
    label = "X_4 + CH3OH_1* <=> CH2OH* + H*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(3.42e19,'cm^2/(mol*s)'), n=0.403, Ea=(8.7,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Pt111
Original entry: CH3OH_X + X <=> CH2OH_X + H_X
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 8.48E10(1/s)/2.483E-9(mol/cm^2) = 3.42E19 cm^2/(mol*s)

This is R101 in Table 2
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 26,
    label = "X_4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(7.6e20,'cm^2/(mol*s)'), n=0, Ea=(18.7,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Ru0001
Original entry: NH3_X + X <=> NH2_X + H_X
"The role of adsorbate–adsorbate interactions in the rate controlling step 
and the most abundant reaction intermediate of NH3 decomposition on Ru"
D.G. Vlachos et al. (2004). Catalysis Letters 96, 13–22. 
https://doi.org/10.1023/B:CATL.0000029523.22277.e1

This reaction used RMG's surface site density of Ru0001 = 2.630E-9(mol/cm^2) to calculate the A factor.
A = 2E12(1/s)/2.630E-9(mol/cm^2) = 7.60E20 cm^2/(mol*s)

This is R9 in Table 2 (set A)
""",
    metal = "Ru",
    facet = "0001",
)

entry(
    index = 27,
    label = "X_4 + H2O* <=> OH* + H*",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.31e20,'cm^2/(mol*s)'), n=0.0281, Ea=(18.6,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Rh
Original entry: H2O_X + X <=> H_X + OH_X
"Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
Vlachos et al. (2008)
Journal of Catalysis,259(2), 211-222, 0021-9517
DOI: 10.1016/j.jcat.2008.08.008.D.G.

Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
A = 5.74E+11(1/s)/2.49E-9(mol/cm^2) = 2.31E+20 cm^2/(mol*s)

This is R7 in Table 4
""",
    metal = "Rh",
)

entry(
    index = 28,
    label = "X_4 + H4N2X <=> H3N2X + H*",
    degeneracy = 4.0,
    kinetics = SurfaceArrhenius(A=(2.69e18,'cm^2/(mol*s)'), n=1.22, Ea=(125437,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Cu111
Original entry: N2H4_X + X <=> N2H3_X + H_X
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This reaction used RMG's surface site density of Cu111 = 2.943E-9(mol/cm^2) to estimate A factor.
A and n was calculated by numpy.linalg.lstsq from Table 1

This is R8 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 29,
    label = "X_4 + H4N2X-2 <=> NH2_X + H2NX",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(6.61e17,'cm^2/(mol*s)'), n=1.589, Ea=(66578,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Cu111
Original entry: N2H4_X + X <=> NH2_X + NH2_X
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This reaction used RMG's surface site density of Cu111 = 2.943E-9(mol/cm^2) to estimate A factor.
A and n was calculated by numpy.linalg.lstsq from Table 1

This is R20 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 30,
    label = "X_4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(5.93e17,'cm^2/(mol*s)'), n=1.321, Ea=(136051,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Cu111
Original entry: NH3_X + X <=> NH2_X + H_X
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This reaction used RMG's surface site density of Cu111 = 2.943E-9(mol/cm^2) to estimate A factor.
A and n was calculated by numpy.linalg.lstsq from Table 1

This is R30 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 31,
    label = "X_4 + H4N2X <=> H3N2X + H*",
    degeneracy = 4.0,
    kinetics = SurfaceArrhenius(A=(3.87e21,'cm^2/(mol*s)'), n=0, Ea=(104209,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Ir111
Original entry: N2H4_X + X <=> N2H3_X + H_X
"Mechanistic study of hydrazine decomposition on Ir(111)"
Alberto Roldan et al. Phys.Chem.Chem.Phys., 2020, 22, 3883
DOI: 10.1039/c9cp06525c

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2)
to estimate a default(1E13) A factor.
A = 1E13(1/s)/2.587E-9(mol/cm^2) = 3.87E21 cm^2/(mol*s)
Ea = 1.08eV = 104209.2J/mol

This is R5 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 32,
    label = "X_4 + H4N2X-2 <=> NH2_X + H2NX",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(3.87e21,'cm^2/(mol*s)'), n=0, Ea=(68507.9,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Ir111
Original entry: N2H4_X + X <=> NH2_X + NH2_X
"Mechanistic study of hydrazine decomposition on Ir(111)"
Alberto Roldan et al. Phys.Chem.Chem.Phys., 2020, 22, 3883
DOI: 10.1039/c9cp06525c

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2)
to estimate a default(1E13) A factor.
A = 1E13(1/s)/2.587E-9(mol/cm^2) = 3.87E21 cm^2/(mol*s)
Ea = 0.71eV = 68507.9J/mol

This is R11 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 33,
    label = "X_4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(1.22e21,'cm^2/(mol*s)'), n=0, Ea=(147114,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Ir111
Original entry: NH3_X + X <=> NH2_X + H_X
"Kinetic and mechanistic analysis of NH3 decomposition 
on Ru(0001), Ru(111) and Ir(111) surfaces"
Alberto Roldan et al. Nanoscale Adv., 2021, 3, 1624
DOI: 10.1039/d1na00015b

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2) to calculate the A factor.
A = 3.15E12(1/s)/2.587E-9(mol/cm^2) = 1.22E21 cm^2/(mol*s)
Ea was calculated from A factor and k rate constant in Table 3

This is R1 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 34,
    label = "X_4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(4.14e21,'cm^2/(mol*s)'), n=0, Ea=(117241,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Ru0001
Original entry: NH3_X + X <=> NH2_X + H_X
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

entry(
    index = 35,
    label = "H* + OH* <=> H2O* + X_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4e+19,'cm^2/(mol*s)'), n=0, Ea=(12.6,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Mhadeshwar_Pt111
Original entry: H_X + OH_X <=> H2O_X + X
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

entry(
    index = 36,
    label = "H* + NH2_X <=> NH3_X + X_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4e+19,'cm^2/(mol*s)'), n=0, Ea=(7.3,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Mhadeshwar_Pt111
Original entry: NH2_X + H_X <=> NH3_X + X
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

entry(
    index = 37,
    label = "H* + CNX <=> CHNX + X_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4e+19,'cm^2/(mol*s)'), n=0, Ea=(13.2,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Mhadeshwar_Pt111
Original entry: CN_X + H_X <=> HCN_X + X
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

entry(
    index = 38,
    label = "H* + HCO* <=> CH2O* + X_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4e+19,'cm^2/(mol*s)'), n=0, Ea=(20.7,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Mhadeshwar_Pt111
Original entry: HCO_X + H_X <=> CH2O_X + X
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
    index = 39,
    label = "CNX + CNX-2 <=> C2N2X + X_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4e+19,'cm^2/(mol*s)'), n=0, Ea=(28.1,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Mhadeshwar_Pt111
Original entry: CN_X + CN_X <=> C2N2_X + X
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

