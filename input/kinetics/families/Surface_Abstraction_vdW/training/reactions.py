#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Abstraction_vdW/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

#reverse of 2, below
entry(
    index = 1,
    label = "H2O* + O* <=> OH_2* + OH_4*",
    degeneracy = 2,
    kinetics = SurfaceArrhenius(
        A = (8.14E20, 'm^2/(mol*s)'),
        n = -0.274,
        Ea = (218400, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""R34
    test surface mechanism: based upon Olaf Deutschmann's work:
    "Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
    Delgado et al
    Catalysts, 2015, 5, 871-904""",
	  metal = "Ni",
)

# reverse of 1, above
# This entry is in reverse direction for family
# entry(
#     index = 2,
#     label = "OH_2* + OH_4* <=> H2O* + O*",
#     degeneracy = 2,
#     kinetics = SurfaceArrhenius(
#         A = (5.691e16, 'm^2/(mol*s)'),
#         n = 0.,
#         Ea = (14.0669343, 'kcal/mol'),
#         Tmin = (298, 'K'),
#         Tmax = (2000, 'K'),
#     ),
#     rank = 10,
#     shortDesc = u"""Default""",
#     longDesc = u"""
# Reaction 16 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
# and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

# A factor from paper / surface site density of Cu
# 1.675e12 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 5.691e16 m^2/(mol*s)
# """,
#     metal = "Cu",
# )

entry(
    index = 3,
    label = "CH4* + O* <=> CH3* + OH_4*",
    degeneracy = 4,
    kinetics = SurfaceArrhenius(
        A = (5.62E20, 'm^2/(mol*s)'),
        n = -0.101,
        Ea = (92700, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""R21
    test surface mechanism: based upon Olaf Deutschmann's work:
    "Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
    Delgado et al
    Catalysts, 2015, 5, 871-904""",
	metal = "Ni",
)

entry(
    index = 4,
    label = "OH_2* + HCO* <=> H2O* + CO*",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (3.261e17, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (0.30, 'eV/molecule'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 40 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
9.597e12 1/s / 2.943e‐5 mol/m^2 = 3.261e17 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 5,
    label = "HCOO_1* + HCO* <=> HCOOH* + CO*",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (7.475e18, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (0.60, 'eV/molecule'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 41 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
2.2e14 1/s / 2.943e‐5 mol/m^2 = 7.475e18 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 6,
    label = "CH3O* + HCO* <=> CH3OH* + CO*",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (6.572e16, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (0.38, 'eV/molecule'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 45 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
1.934e12 1/s / 2.943e‐5 mol/m^2 = 6.572e16 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 7,
    label = "CH3O* + HCOO_5* <=> HCOOCH3* + O*",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (2.356e16, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (1.24, 'eV/molecule'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 46 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
6.934e11 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 2.356e16 m^2/(mol*s)
""",
    metal = "Cu",
)
entry(
    index = 8,
    label = "O* + H3NX <=> H2NX + OH_4*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(4.83e+20,'cm^2/(mol*s)'), n=0, Ea=(42000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Offermans_Pt111
Original entry: NH3_X +O_X <=> NH2_X + OH_X
"Ammonia oxidation on platinum : a density functional theory study of surface reactivity."
Offermans, W. K. (2007). Technische Universiteit Eindhoven. 
https://doi.org/10.6100/IR630067

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 300K) = 1.2E12(1/s)/2.483E-9(mol/cm^2) = 4.83E20 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 9,
    label = "H2NX-2 + OH_2* <=> H2O* + HNX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.37e+21,'cm^2/(mol*s)'), n=0, Ea=(22000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Offermans_Pt111
Original entry: NH2_X + OH_X <=> NH_X + H2O_X
"Ammonia oxidation on platinum : a density functional theory study of surface reactivity."
Offermans, W. K. (2007). Technische Universiteit Eindhoven. 
https://doi.org/10.6100/IR630067

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 300K) = 3.4E12(1/s)/2.483E-9(mol/cm^2) = 1.37E21 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 10,
    label = "HNX-2 + OH_2* <=> H2O* + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.05e+20,'cm^2/(mol*s)'), n=0, Ea=(35000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_AbstractionvdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Offermans_Pt111
Original entry: NH_X + OH_X <=> N_X + H2O_X
"Ammonia oxidation on platinum : a density functional theory study of surface reactivity."
Offermans, W. K. (2007). Technische Universiteit Eindhoven. 
https://doi.org/10.6100/IR630067

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 300K) = 5.1E11(1/s)/2.483E-9(mol/cm^2) = 2.05E20 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 11,
    label = "O* + H3NX <=> H2NX + OH_4*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(6.4e+20,'cm^2/(mol*s)'), n=0, Ea=(92630.4,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Popa_Rh111
Original entry: NH3_X +O_X <=> NH2_X + OH_X
Based primarily on 
"Density-functional theory study of NHx oxidation 
and reverse reactions on the Rh (111) surface."
C. Popa, R. A. van Santen, and A. P. J. JansenJ.
Phys. Chem. C 2007, 111, 9839– 9852.
https://doi.org/10.1021/jp071072g

This reaction used RMG's surface site density of Rh111 = 2.656E-09(mol/cm^2) to calculate the A factor.
A (at 300K)= 1.7E12(1/s)/2.656E-9(mol/cm^2) = 6.40E20 cm^2/(mol*s)

Ea = 0.96eV = 92630.4J/mol

This is reaction 2a. of TABLE 4.
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 12,
    label = "H2NX-2 + OH_2* <=> H2O* + HNX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.5e+21,'cm^2/(mol*s)'), n=0, Ea=(13508.6,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Popa_Rh111
Original entry: NH2_X + OH_X <=> NH_X + H2O_X
Based primarily on 
"Density-functional theory study of NHx oxidation 
and reverse reactions on the Rh (111) surface."
C. Popa, R. A. van Santen, and A. P. J. JansenJ.
Phys. Chem. C 2007, 111, 9839– 9852.
https://doi.org/10.1021/jp071072g

This reaction used RMG's surface site density of Rh111 = 2.656E-09(mol/cm^2) to calculate the A factor.
A (at 300K)= 3.98E12(1/s)/2.656E-9(mol/cm^2) = 1.50E21 cm^2/(mol*s)

Ea = 0.14eV = 13508.6J/mol

This is reaction 3a. of TABLE 5.
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 13,
    label = "HNX-2 + OH_2* <=> H2O* + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.52e+20,'cm^2/(mol*s)'), n=0, Ea=(22192.7,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Popa_Rh111
Original entry: NH_X + OH_X <=> N_X + H2O_X
Based primarily on 
"Density-functional theory study of NHx oxidation 
and reverse reactions on the Rh (111) surface."
C. Popa, R. A. van Santen, and A. P. J. JansenJ.
Phys. Chem. C 2007, 111, 9839– 9852.
https://doi.org/10.1021/jp071072g

This reaction used RMG's surface site density of Rh111 = 2.656E-09(mol/cm^2) to calculate the A factor.
A (at 300K)= 1.2E12(1/s)/2.656E-9(mol/cm^2) = 4.52E20 cm^2/(mol*s)

Ea = 0.23eV = 22192.7J/mol

This is reaction 6a. of TABLE 5.
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 14,
    label = "O* + H3NX <=> H2NX + OH_4*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(6.85e+23,'cm^2/(mol*s)'), n=0, Ea=(157000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Rebrov_Pt111
Original entry: NH3_X + O_X <=> NH2_X + OH_X
"Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
https://doi.org/10.1016/S1385-8947(02)00068-2

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1.7E15(1/s)/2.483E-9(mol/cm^2) = 6.85E23 cm^2/(mol*s)

This is R5 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 15,
    label = "O* + HNOX <=> NOX + OH_4*",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(8.05e+23,'cm^2/(mol*s)'), n=0, Ea=(118000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Rebrov_Pt111
Original entry: NHO_X + O_X <=> NO_X + OH_X
"Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
https://doi.org/10.1016/S1385-8947(02)00068-2

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 2E15(1/s)/2.483E-9(mol/cm^2) = 8.05E23 cm^2/(mol*s)

This is R10 in Table 1, it's from ref[52] where metal = Pt100.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 16,
    label = "HNX-2 + OH_2* <=> H2O* + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.03e+21,'cm^2/(mol*s)'), n=0, Ea=(46000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Rebrov_Pt111
Original entry: NH_X + OH_X <=> N_X + H2O_X
"Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
https://doi.org/10.1016/S1385-8947(02)00068-2

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1E13(1/s)/2.483E-9(mol/cm^2) = 4.03E21 cm^2/(mol*s)

This is R16 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 17,
    label = "O* + H2O* <=> OH_2* + OH_4*",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(4.03e+19,'cm^2/(mol*s)'), n=0, Ea=(52700,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Rebrov_Pt111
Original entry: O_X + H2O_X <=> OH_X + OH_X
"Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
https://doi.org/10.1016/S1385-8947(02)00068-2
This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1E11(1/s)/2.483E-9(mol/cm^2) = 4.03E19 cm^2/(mol*s)
This is R18 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

