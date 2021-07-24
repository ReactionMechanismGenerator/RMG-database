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
1.28e13 1/s / 2.943e‐5 mol/m^2 = 4.349e22 m^2/(mol*s)
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
    kinetics = SurfaceArrhenius(A=(4.35e+15,'cm^2/(mol*s)'), n=0, Ea=(107104,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Duan_Ni111
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
A = k/exp(-Ea/RT) = 5.35(1/s)/exp(-107103.9(J/mol)/8.314(J/mol/K)/873K) =  1.37E7/s
  = (1.37E7/s)/3.148E-9(mol/cm^2) = 4.35E15 cm^2/mol/s

Ea = 1.11eV = 107103.9J/mol

This is reaction 1 from Table 2
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 12,
    label = "X_4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(5.52e+19,'cm^2/(mol*s)'), n=0, Ea=(63683.4,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Duan_Ni211
Original entry: NH3_X + X <=> NH2_X + H_X
"Structure sensitivity of ammonia decomposition 
over Ni catalysts: A computational and experimental study"
Duan et al. Fuel Processing Technology 108 (2013) 112–117
https://doi.org/10.1016/j.fuproc.2012.05.030

This reaction used RMG's surface site density of Ni211 = 3.339E-9(mol/cm^2) to calculate the A factor.
A = k/exp(-Ea/RT) = 2.85E7(1/s)/exp(-63683.4(J/mol)/8.314(J/mol/K)/873K) =  1.84E11/s
  = (1.84E11/s)/3.339E-9(mol/cm^2) = 5.52E19 cm^2/mol/s

Ea = 0.66eV = 63683.4J/mol

This is reaction 1 from Table 2
""",
    metal = "Ni",
    facet = "211",
)

entry(
    index = 13,
    label = "X_4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(2.78e+17,'cm^2/(mol*s)'), n=1.146, Ea=(104000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Novell_Pd111
Original entry: NH3_X + X <=> NH2_X + H_X
"Ammonia Dehydrogenation over Platinum-Group Metal Surfaces. Structure, Stability, and Reactivity of Adsorbed NHx Species"
Gerard Novell-Leruth et al. J. Phys. Chem. C 2007, 111, 2, 860–868
https://doi.org/10.1021/jp064742b

This reaction used RMG's surface site density of Pd111 = 2.534E-09(mol/cm^2) to calculate the A factor.
The modified Arrhenius parameter is calculated from TABLE 4.
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 14,
    label = "X_4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(2.859e+20,'cm^2/(mol*s)'), n=0, Ea=(91000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Novell_Pt111
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
    index = 15,
    label = "X_4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(1.31e+23,'cm^2/(mol*s)'), n=-0.791, Ea=(100000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Novell_Rh111
Original entry: NH3_X + X <=> NH2_X + H_X
"Ammonia Dehydrogenation over Platinum-Group Metal Surfaces. Structure, Stability, and Reactivity of Adsorbed NHx Species"
Gerard Novell-Leruth et al. J. Phys. Chem. C 2007, 111, 2, 860–868
https://doi.org/10.1021/jp064742b

This reaction used RMG's surface site density of Rh111 = 2.656E-9(mol/cm^2) to calculate the A factor.
The modified Arrhenius parameter is calculated from TABLE 4.
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 16,
    label = "X_4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(2.26e+20,'cm^2/(mol*s)'), n=0, Ea=(93000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Offermans_Pt111
Original entry: NH3_X + X <=> NH2_X + H_X
"Ammonia oxidation on platinum : a density functional theory study of surface reactivity."
Offermans, W. K. (2007). Technische Universiteit Eindhoven. 
https://doi.org/10.6100/IR630067

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 300K)= 5.6E11(1/s)/2.483E-9(mol/cm^2) = 2.25E20 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 17,
    label = "X_4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(8.21e+21,'cm^2/(mol*s)'), n=0, Ea=(109034,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Popa_Rh111
Original entry: NH3_X + X <=> NH2_X + H_X
Based primarily on "Ab initio density-functional theory study of 
NHx dehydrogenation and reverse reactions on the Rh(111) surface"
C. Popa, W. K. Offermans, R. A. van Santen, and A. P. J. Jansen
American Physical Society Vol. 74, Iss. 15—15, 2006
https://doi.org/10.1103/PhysRevB.74.155428

This reaction used RMG's surface site density of Rh111 = 2.656E-09(mol/cm^2) to calculate the A factor.
A (at 300K)= 2.18E13(1/s)/2.656E-9(mol/cm^2) = 8.21E21 cm^2/(mol*s)

Ea = 1.13eV = 109033.7J/mol

This is reaction 1 of TABLE VI.
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 18,
    label = "X_4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(4.14e+21,'cm^2/(mol*s)'), n=0, Ea=(117241,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Roldan_Ru0001
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
    index = 19,
    label = "X_4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(3.82e+20,'cm^2/(mol*s)'), n=0, Ea=(111928,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Schneider_Pt111
Original entry: NH3_X + X <=> NH2_X + H_X
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

A factor is a mean value from other Pt111 libraries
Ea = 1.16eV = 111928.4J/mol

This is reaction (1) in Table S3
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 20,
    label = "H* + OH* <=> H2O* + X_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.04e+21,'cm^2/(mol*s)'), n=0, Ea=(20262.9,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Schneider_Pt111
Original entry: H_X + OH_X <=> H2O_X + X
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

A factor from CPOX/Deutschmann 
Ea = 0.21eV = 20262.9J/mol

This is reaction (5) in Table S3
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 21,
    label = "X_4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(3.6e+20,'cm^2/(mol*s)'), n=0, Ea=(110964,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Schneider_Pt211
Original entry: NH3_X + X <=> NH2_X + H_X
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Pt211
Ea = 1.15eV = 110963.5J/mol

This is reaction (1) in Table S3
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 22,
    label = "H* + OH* <=> H2O* + X_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.92e+21,'cm^2/(mol*s)'), n=0, Ea=(92630.4,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Schneider_Pt211
Original entry: H_X + OH_X <=> H2O_X + X
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Pt211
Ea = 0.96eV = 92630.4J/mol

This is reaction (5) in Table S3
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 23,
    label = "X_4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(3.74e+20,'cm^2/(mol*s)'), n=0, Ea=(104209,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Schneider_Pd111
Original entry: NH3_X + X <=> NH2_X + H_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Pd111

Ea = 1.08eV = 104209.2J/mol

This is reaction (1) in Table S5
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 24,
    label = "H* + OH* <=> H2O* + X_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2e+21,'cm^2/(mol*s)'), n=0, Ea=(64648.3,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Schneider_Pd111
Original entry: H_X + OH_X <=> H2O_X + X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Pd111

Ea = 0.67eV = 64648.3J/mol

This is reaction (5) in Table S5
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 25,
    label = "X_4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(3.52e+20,'cm^2/(mol*s)'), n=0, Ea=(97454.9,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Schneider_Pd211
Original entry: NH3_X + X <=> NH2_X + H_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Pd211
Ea = 1.01eV = 97454.9/mol

This is reaction (1) in Table S4
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 26,
    label = "H* + OH* <=> H2O* + X_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.88e+21,'cm^2/(mol*s)'), n=0, Ea=(91665.5,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Schneider_Pd211
Original entry: H_X + OH_X <=> H2O_X + X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Pd211

Ea = 0.95eV = 91665.5J/mol

This is reaction (5) in Table S4
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 27,
    label = "X_4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(3.57e+20,'cm^2/(mol*s)'), n=0, Ea=(100350,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Schneider_Rh111
Original entry: NH3_X + X <=> NH2_X + H_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Rh111

Ea = 1.04eV = 100349.6J/mol

This is reaction (1) in Table S5
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 28,
    label = "H* + OH* <=> H2O* + X_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.91e+21,'cm^2/(mol*s)'), n=0, Ea=(63683.4,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Schneider_Rh111
Original entry: H_X + OH_X <=> H2O_X + X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

A factor from Schneider_Pt111 library and scale up by RMG's surface site density of Rh111

Ea = 0.66eV = 63683.4J/mol

This is reaction (5) in Table S5
""",
    metal = "Rh",
    facet = "111",
)

