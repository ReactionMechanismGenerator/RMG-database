#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_vdW/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label = "H2O + X <=> H2OX",
    kinetics = StickingCoefficient(
        A = 1.0e-1,
        n = 0,
        Ea = (0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""R5
    test surface mechanism: based upon Olaf Deutschmann's work:
    "Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
    Delgado et al
    Catalysts, 2015, 5, 871-904""",
	metal = "Ni",
)

entry(
    index = 2,
    label = "CO2 + X <=> CO2X",
    kinetics = StickingCoefficient(
        A = 7.0e-6,
        n = 0,
        Ea = (0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""R7
    test surface mechanism: based upon Olaf Deutschmann's work:
    "Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
    Delgado et al
    Catalysts, 2015, 5, 871-904""",
	metal = "Ni",
)

entry(
    index = 3,
    label = "CH4 + X <=> CH4X",
    kinetics = StickingCoefficient(
        A = 8.0e-3,
        n = 0,
        Ea = (0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""R11
    test surface mechanism: based upon Olaf Deutschmann's work:
    "Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
    Delgado et al
    Catalysts, 2015, 5, 871-904""",
	metal = "Ni",
)

entry(
    index = 4,
    label = "H3NX <=> H3N + X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.48e09,'1/s'), n=0, Ea=(60900,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Krahnert_Pt111
Original entry: NH3_X <=> NH3 + X
"Ammonia Oxidation over Polycrystalline Platinum: 
Surface Morphology and Kinetics at Atmospheric Pressure."
Krähnert, Ralph(2005) A Doctoral Thesis.
http://dx.doi.org/10.14279/depositonce-1270

A = k/exp(Ea/RT) = 2.17(1/s)/exp(60900J/mol / 8.314J/molK / 658K) = 1.48E09 (1/s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 5,
    label = "X + N2 <=> N2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.464e21,'cm^3/(mol*s)'), n=0, Ea=(4000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """N2 Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Offermans_Pt111
Original entry: N2 + X <=> N2_X
"Ammonia oxidation on platinum : a density functional theory study of surface reactivity."
Offermans, W. K. (2007). Technische Universiteit Eindhoven. 
https://doi.org/10.6100/IR630067

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 300K from p.62)= 8.6E12(cm/s)/2.483E-9(mol/cm^2) = 3.464E21 cm^3/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 6,
    label = "H3NX <=> H3N + X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.03e17,'1/s'), n=0, Ea=(75200,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Rebrov_Pt111
Original entry: NH3_X <=> NH3 + X
"Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
https://doi.org/10.1016/S1385-8947(02)00068-2

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1E9(mol/cm^2/s)/2.483E-9(mol/cm^2) = 4.03E17 (1/s)

This is R2 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 7,
    label = "H2OX <=> H2O + X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.03e21,'1/s'), n=0, Ea=(40300,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Rebrov_Pt111
Original entry: H2O_X <=> H2O + X
"Development of the kinetic model of platinum catalyzed ammonia oxidation in a microreactor"
Rebrov et al. (2002). Chemical Engineering Journal, 90, 61–76.
https://doi.org/10.1016/S1385-8947(02)00068-2

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1E13(mol/cm^2/s)/2.483E-9(mol/cm^2) = 4.03E21 (1/s)

This is R19 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 8,
    label = "X + H3N <=> H3NX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.00768, n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Scheuer_Pt
Original entry: NH3 + X <=> NH3_X
"Dual layer automotive ammonia oxidation catalysts: Experiments and computer simulation"
Scheuer et al. Applied Catalysis B: Environmental 111–112 (2012) 445–455
https://doi.org/10.1016/j.apcatb.2011.10.032

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = ((19/Pa)/s)*(2.483e-9(mol/cm^2))*sqrt(2*pi*(17(g/mol))*the molar gas constant*(298 kelvin))= 0.00768

This is R1 in Table 1
""",
    metal = "Pt",
)

entry(
    index = 9,
    label = "H2OX <=> H2O + X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.38e24,'1/s'), n=0, Ea=(18333.1,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pt111
Original entry: H2O_X <=> H2O + X
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 5.9E15(1/s)/2.483E-9(mol/cm^2) = 2.38E24 cm^2/(mol*s)
Ea = 0.19eV = 18333.1J/mol

This is R10 in Table S2 and S4
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 10,
    label = "N2OX <=> N2O + X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(5.64e24,'1/s'), n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pt111
Original entry: N2O_X <=> N2O + X
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1.4E16(1/s)/2.483E-9(mol/cm^2) = 5.64E24 cm^2/(mol*s)

This is R15 in Table S2 and S4
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 11,
    label = "H2OX <=> H2O + X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.4e24,'1/s'), n=0, Ea=(24122.5,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pt211
Original entry: H2O_X <=> H2O + X
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt211 = 2.634E-9(mol/cm^2) to calculate the A factor.
A = 3.7E15(1/s)/2.634E-9(mol/cm^2) = 1.40E24 cm^2/(mol*s)
Ea = 0.25eV = 24122.5J/mol

This is R10 in Table S2 and S4
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 12,
    label = "N2OX <=> N2O + X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(5.69e25,'1/s'), n=0, Ea=(9649,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pt211
Original entry: N2O_X <=> N2O + X
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251

This reaction used RMG's surface site density of Pt211 = 2.634E-9(mol/cm^2) to calculate the A factor.
A = 1.5E17(1/s)/2.634E-9(mol/cm^2) = 5.69E25 cm^2/(mol*s)
Ea = 0.1eV = 9649J/mol

This is R15 in Table S2 and S4
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 13,
    label = "X + CO2-2 <=> CO2X-2",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.195, n=0.25, Ea=(0,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Pt111
Original entry: CO2 + X <=> CO2_X
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This is R7 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 14,
    label = "X + H2O <=> H2OX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.108, n=1.162, Ea=(0,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Pt111
Original entry: H2O + X <=> H2O_X
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This is R21 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 15,
    label = "X + CH4O <=> CH4OX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.334, n=0.258, Ea=(0,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Pt111
Original entry: CH3OH + X <=> CH3OH_X
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This is R83 in Table 2
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 16,
    label = "X + CH2O <=> CH2OX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.0877, n=0.098, Ea=(0,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Pt111
Original entry: CH2O + X <=> CH2O_X
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This is R87 in Table 2
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 17,
    label = "X + H3N <=> H3NX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.00015, n=0, Ea=(0,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Ru0001
Original entry: NH3 + X <=> NH3_X
"The role of adsorbate–adsorbate interactions in the rate controlling step 
and the most abundant reaction intermediate of NH3 decomposition on Ru"
D.G. Vlachos et al. (2004). Catalysis Letters 96, 13–22. 
https://doi.org/10.1023/B:CATL.0000029523.22277.e1

This is R11 in Table 2 (set A)
""",
    metal = "Ru",
    facet = "0001",
)

entry(
    index = 18,
    label = "X + H2O <=> H2OX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.0772, n=1.4067, Ea=(0,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Rh
Original entry: H2O + X <=> H2O_X
"Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
Vlachos et al. (2008)
Journal of Catalysis,259(2), 211-222, 0021-9517
DOI: 10.1016/j.jcat.2008.08.008.D.G.

This is R13 in Table 4
""",
    metal = "Rh",
)

entry(
    index = 19,
    label = "X + CO2-2 <=> CO2X-2",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.367, n=-2.3294, Ea=(0,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Rh
Original entry: CO2 + X <=> CO2_X
"Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
Vlachos et al. (2008)
Journal of Catalysis,259(2), 211-222, 0021-9517
DOI: 10.1016/j.jcat.2008.08.008.D.G.

This is R21 in Table 4
""",
    metal = "Rh",
)

entry(
    index = 20,
    label = "X + H4N2 <=> H4N2X",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=1.17e-06, n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Cu111
Original entry: N2H4 + X <=> N2H4_X
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This is R0 in Table 2 at T=300K
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 21,
    label = "X + H3N <=> H3NX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.000188, n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Cu111
Original entry: NH3 + X <=> NH3_X
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This is R3 in Table 2 at T=300K
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 22,
    label = "X + N2 <=> N2X",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=5.5e-05, n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Cu111
Original entry: N2 + X <=> N2_X
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This is R5 in Table 2 at T=300K
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 23,
    label = "H3NX <=> H3N + X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.68e16,'1/s'), n=0, Ea=(88574.8,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Ir111
Original entry: NH3_X <=> NH3 + X
"Kinetic and mechanistic analysis of NH3 decomposition 
on Ru(0001), Ru(111) and Ir(111) surfaces"
Alberto Roldan et al. Nanoscale Adv., 2021, 3, 1624
DOI: 10.1039/d1na00015b

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2) to calculate the A factor.
A = 9.53E7(mol/cm^2/s)/2.587E-9(mol/cm^2) = 3.68E16 (1/s)
Ea was calculated from A factor and k rate constant in Table 3

This is D1 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 24,
    label = "H2X <=> H2 + X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.69e16,'1/s'), n=0, Ea=(30972.4,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """H2 Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Ir111
Original entry: H2_X <=> H2 + X
"Kinetic and mechanistic analysis of NH3 decomposition 
on Ru(0001), Ru(111) and Ir(111) surfaces"
Alberto Roldan et al. Nanoscale Adv., 2021, 3, 1624
DOI: 10.1039/d1na00015b

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2) to calculate the A factor.
A = 9.54E7(mol/cm^2/s)/2.587E-9(mol/cm^2) = 3.69E16 (1/s)
Ea was calculated from A factor and k rate constant in Table 3

This is D3 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 25,
    label = "H3NX <=> H3N + X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.9e16,'1/s'), n=0, Ea=(72149.6,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Ru0001
Original entry: NH3_X <=> NH3 + X
"Kinetic and mechanistic analysis of NH3 decomposition 
on Ru(0001), Ru(111) and Ir(111) surfaces"
Alberto Roldan et al. Nanoscale Adv., 2021, 3, 1624
DOI: 10.1039/d1na00015b

This reaction used RMG's surface site density of Ru0001 = 2.630E-9(mol/cm^2) to calculate the A factor.
A = 1.29E8(mol/cm^2/s)/2.630E-9(mol/cm^2) = 4.90E16 (1/s)
Ea was calculated from A factor and k rate constant in Table 3

This is D1 in Table 3
""",
    metal = "Ru",
    facet = "0001",
)

entry(
    index = 26,
    label = "X + N2 <=> N2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.9e16,'cm^3/(mol*s)'), n=0, Ea=(24483,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Ru0001
Original entry: N2 + X <=> N2_X
"Kinetic and mechanistic analysis of NH3 decomposition 
on Ru(0001), Ru(111) and Ir(111) surfaces"
Alberto Roldan et al. Nanoscale Adv., 2021, 3, 1624
DOI: 10.1039/d1na00015b

This reaction used RMG's surface site density of Ru0001 = 2.630E-9(mol/cm^2) to calculate the A factor.
A = 1.29E8(cm/s)/2.630E-9(mol/cm^2) = 4.90E16 (cm^3/(mol*s))
Ea was calculated from A factor and k rate constant in Table 3

This is A2 in Table 3
""",
    metal = "Ru",
    facet = "0001",
)

entry(
    index = 27,
    label = "H2X <=> H2 + X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.9e16,'1/s'), n=0, Ea=(24483,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """H2 Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Ru0001
Original entry: H2_X <=> H2 + X
"Kinetic and mechanistic analysis of NH3 decomposition 
on Ru(0001), Ru(111) and Ir(111) surfaces"
Alberto Roldan et al. Nanoscale Adv., 2021, 3, 1624
DOI: 10.1039/d1na00015b

This reaction used RMG's surface site density of Ru0001 = 2.630E-9(mol/cm^2) to calculate the A factor.
A = 1.29E8(mol/cm^2/s)/2.630E-9(mol/cm^2) = 4.90E16 (1/s)
Ea was calculated from A factor and k rate constant in Table 3

This is D3 in Table 3
""",
    metal = "Ru",
    facet = "0001",
)

entry(
    index = 28,
    label = "CO2X-2 <=> CO2-2 + X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4e+21,'1/s'), n=0, Ea=(3.6,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Mhadeshwar_Pt111
Original entry: CO2_X <=> CO2 + X
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E13(1/s)/2.5E-9(mol/cm^2) = 4E21 cm^2/(mol*s)

This is R8 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 29,
    label = "H2OX <=> H2O + X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4e+21,'1/s'), n=0, Ea=(10.3,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Mhadeshwar_Pt111
Original entry: H2O_X <=> H2O + X
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E13(1/s)/2.5E-9(mol/cm^2) = 4E21 cm^2/(mol*s)

This is R16 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 30,
    label = "H3NX <=> H3N + X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4e+21,'1/s'), n=0, Ea=(20.7,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Mhadeshwar_Pt111
Original entry: NH3_X <=> NH3 + X
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E13(1/s)/2.5E-9(mol/cm^2) = 4E21 cm^2/(mol*s)

This is R44 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 31,
    label = "CHNX <=> CHN + X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4e+21,'1/s'), n=0, Ea=(21.3,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Mhadeshwar_Pt111
Original entry: HCN_X <=> HCN + X
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E13(1/s)/2.5E-9(mol/cm^2) = 4E21 cm^2/(mol*s)

This is R82 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 32,
    label = "CH2OX <=> CH2O + X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4e+21,'1/s'), n=0, Ea=(14.7,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Mhadeshwar_Pt111
Original entry: CH2O_X <=> CH2O + X
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E13(1/s)/2.5E-9(mol/cm^2) = 4E21 cm^2/(mol*s)

This is R96 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 33,
    label = "C2N2X <=> C2N2 + X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4e+21,'1/s'), n=0, Ea=(21,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Adsorption_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Mhadeshwar_Pt111
Original entry: C2N2_X <=> C2N2 + X
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E13(1/s)/2.5E-9(mol/cm^2) = 4E21 cm^2/(mol*s)

This is R122 in Appendix A

This reaction is the least important ones for typical DOC conditions.
""",
    metal = "Pt",
    facet = "111",
)

