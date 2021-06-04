#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label = "OCX_3 + HOX_5 <=> HOCXO_1 + X_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(4.02e14, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(11.5, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
    Experimental and microkinetic modeling of steady-state NO reduction by H2 on Pt/BaO/Al2O3 monolith catalysts
    Xu, Clayton, Balakotaiah, Harold et al.
    doi: 10.1016.j.apcatb.2007.08.008
""",
    metal = "Pt",
)

entry(
    index = 2,
    label = "HOCXO_1 + X_4 <=> OCX_3 + HOX_5",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(1.46e20, 'm^2/(mol*s)'),
        n = -0.213,
        Ea=(54300.0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=10,
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R44
""", 
    metal = 'Ni',
)

entry(
    index = 3,
    label = "OCX_3 + HOX_5 <=> HOCXO_1 + X_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(1.586e16, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(0.56, 'eV/molecule'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 10 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
4.667E11 1/s / 2.943e‐5 mol/m^2 = 1.586e16 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 4,
    label = "NH2_X + X_4 <=> NHX_1 + HX_5",
    degeneracy = 2,
    kinetics = SurfaceArrhenius(
        A = (2.718e22, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (75.74, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""NH2 Surface Dissociation""",
    longDesc = u"""
    Micro-kinetic modeling of NH3 decomposition on Ni and its application to solid oxide fuel cells
    Deutschmann et al
    doi: 10.1016/j.ces.2011.07.007

    This is R9
    """,
    metal = "Ni",
)

entry(
    index = 5,
    label = "NH2_X + X_4 <=> NHX_2 + HX_5",
    degeneracy = 2,
    kinetics = SurfaceArrhenius(
        A = (1.2415e+18, 'm^2/(mol*s)'),
        n = 0,
        Ea = (110, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""NH2 Surface Dissociation on Pt""",
    longDesc = u"""
    "Ammonia activation on platinum {1 1 1}: A density functional theory study"
    https://doi.org/10.1016/j.susc.2006.01.031

    A factor from paper / surface site density of Pt
    5e12 1/s / 2.483e-05 mol/m^2 = 1.2415e+18 m^2/(mol*s)
    """, 
    metal="Pt",
    facet="111"
)

entry(
    index = 6,
    label = "NHX_2 + X_4 <=> NX + HX_5",
    kinetics = SurfaceArrhenius(
        A = (1.78776e+18, 'm^2/(mol*s)'),
        n = 0,
        Ea = (118.0, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""NH Surface Dissociation Pt""",
    longDesc = u"""
    "Ammonia activation on platinum {1 1 1}: A density functional theory study"
    https://doi.org/10.1016/j.susc.2006.01.031

    A factor from paper / surface site density of Pt
    7.2e12 1/s / 2.483e-05 mol/m^2 = 1.78776e+18 m^2/(mol*s)
    """,
    metal = "Pt",
    facet="111"
)

entry(
    index = 11,
    label = "NHX_2 + X_4 <=> NX + HX_5",
    kinetics = SurfaceArrhenius(
        A = (6.213e19, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (22.93, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""NH Surface Dissociation""",
    longDesc = u"""
    Micro-kinetic modeling of NH3 decomposition on Ni and its application to solid oxide fuel cells
    Deutschmann et al
    doi: 10.1016/j.ces.2011.07.007

    This is R11
    """,
    metal = "Ni",
    facet="111"
)

entry(
    index = 7,
    label = "CHX_3 + HX_5 <=> CH2X_1 + X_4",
    degeneracy = 2,
    kinetics = SurfaceArrhenius(
        A=(9.77e20, 'm^2/(mol*s)'),
        n = -0.087,
        Ea=(81000.0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=10,
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R18
""",
    metal = "Ni",
)

entry(
    index = 8,
    label = "CH2X_3 + HX_5 <=> CH3X_1 + X_4",
    degeneracy = 3,
    kinetics = SurfaceArrhenius(
        A=(3.09e19, 'm^2/(mol*s)'),
        n = -0.087,
        Ea=(57200.0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=10,
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R16
""",
    metal = "Ni",
)
#Delgado has this reaction as exothermic. However, our own thermo has this reaction as endothermic. removing and replacing with reverse direction, R9.
#entry(
#    index = 8,
#    label = "CHX_1 + X_4 <=> CX_3 + HX_5",
#    degeneracy = 1,
#    kinetics = SurfaceArrhenius(
#        A=(9.88E16, 'm^2/(mol*s)'),
#        n = 0.5,
#        Ea=(21900.0, 'J/mol'),
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    rank = 10,
#    shortDesc = u"""Default""",
#    longDesc = u"""
#"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
#Delgado et al
#Catalysts, 2015, 5, 871-904. Reaction R19
#""",
#    metal = "Ni"
#)

entry(
    index = 9,
    label = "CX_3 + HX_5 <=> CHX_1 + X_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(1.70E20, 'm^2/(mol*s)'),
        n = -0.5,
        Ea=(157900., 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=10,
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R20
""",
    metal = "Ni",
)

entry(
    index = 10,
    label = "HCOO* + X_4 <=> HCO* + OX_3",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(8.733e16, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(2.36, 'eV/molecule'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 28 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
2.570E12 1/s / 2.943e‐5 mol/m^2 = 8.733e16 m^2/(mol*s)
""", 
    metal = "Cu",
)

entry(
    index = 74,
    label = "HCOH* + HX_5 <=> CH2OH* + X_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(1.257e17, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(54.4228933, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 32 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
3.698E12 1/s / 2.943e‐5 mol/m^2 = 1.257e17 m^2/(mol*s)
""", 
    metal = "Cu",
)

entry(
    index = 12,
    label = "HOX_1 + X_4 <=> OX_3 + HX_5",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(2.25E16, 'm^2/(mol*s)'),
        n = 0.188,
        Ea=(29600.0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=10,
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R32
""",
    metal = "Ni",
)

entry(
    index = 13,
    label = "HOX_1 + X_4 <=> OX_3 + HX_5",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(7.452e17, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(1.68, 'eV/molecule'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 15 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
2.193E13 1/s / 2.943e‐5 mol/m^2 = 7.452e17 m^2/(mol*s)
""", 
    metal = "Cu",
)

entry(
    index = 14,
    label = "CH3O2* + X_4 <=> CH2OH*_2 + OX_3",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(1.864e18, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(2.01, 'eV/molecule'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 36 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
5.485E13 1/s / 2.943e‐5 mol/m^2 = 1.864e18 m^2/(mol*s)
""", 
    metal = "Cu",
)

entry(
    index = 15,
    label = "CXHO_1 + X_4 <=> OCX_3 + HX_5",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(3.71E17, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(0.0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=10,
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R48
""", 
    metal = "Ni",
)

entry(
    index = 16,
    label = "OCX_3 + HX_5 <=> CXHO_1 + X_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(3.140e17, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(0.99, 'eV/molecule'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 26 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
9.240E12 1/s / 2.943e‐5 mol/m^2 = 3.140e17 m^2/(mol*s)
""", 
    metal = "Cu",
)

entry(
    index = 17,
    label = "NOX + OX <=> NO2X + X_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.776e22,'cm^2/(mol*s)'), n=0, Ea=(115788,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Arevalo_Pt111
Original entry: NO_X + O_X <=> NO2_X + X
"First-principles study of nitric oxide oxidation on Pt(111) versus Pt overlayer on 3d transition metals"
Ryan Lacdao Arevalo, Mary Clare Sison Escaño, and Hideaki Kasai. J. Vac. Sci. Technol. A 33, 021402 (2015)
https://doi.org/10.1116/1.4903225

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 300K) = 4.41E13(1/s)/2.483E-9(mol/cm^2) = 1.776E22 cm^2/(mol*s)
Ea = 1.2eV * 96490J/eV mol = 115788J/mol

This is R5 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 18,
    label = "X_4 + NH2_X <=> NHX_1 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.014e21,'cm^2/(mol*s)'), n=0, Ea=(110000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Offermans_Pt111
Original entry: NH2_X + X <=> NH_X + H_X
"Ammonia oxidation on platinum : a density functional theory study of surface reactivity."
Offermans, W. K. (2007). Technische Universiteit Eindhoven. 
https://doi.org/10.6100/IR630067

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 300K) = 5.0E12(1/s)/2.483E-9(mol/cm^2) = 2.014E21 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 19,
    label = "X_4 + NHX_2 <=> NX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.08997e21,'cm^2/(mol*s)'), n=0, Ea=(118000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Offermans_Pt111
Original entry: NH_X + X <=> N_X + H_X
"Ammonia oxidation on platinum : a density functional theory study of surface reactivity."
Offermans, W. K. (2007). Technische Universiteit Eindhoven. 
https://doi.org/10.6100/IR630067

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 300K) = 7.2E12(1/s)/2.483E-9(mol/cm^2) = 2.8997E21 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 20,
    label = "X_4 + NH2_X <=> NHX_1 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(4.43e21,'cm^2/(mol*s)'), n=0, Ea=(101000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Novell_Pt111
Original entry: NH2_X + X <=> NH_X + H_X
"Ammonia Dehydrogenation over Platinum-Group Metal Surfaces. Structure, Stability, and Reactivity of Adsorbed NHx Species"
Gerard Novell-Leruth et al. J. Phys. Chem. C 2007, 111, 2, 860–868
https://doi.org/10.1021/jp064742b

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 500K) = 1.1E13(1/s)/2.483E-9(mol/cm^2) = 4.430E21 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 21,
    label = "X_4 + NHX_2 <=> NX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(5.236e21,'cm^2/(mol*s)'), n=0, Ea=(116000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Novell_Pt111
Original entry: NH_X + X <=> N_X + H_X
"Ammonia Dehydrogenation over Platinum-Group Metal Surfaces. Structure, Stability, and Reactivity of Adsorbed NHx Species"
Gerard Novell-Leruth et al. J. Phys. Chem. C 2007, 111, 2, 860–868
https://doi.org/10.1021/jp064742b

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 500K) = 1.3E13(1/s)/2.483E-9(mol/cm^2) = 5.236E21 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 22,
    label = "X_4 + NH2_X <=> NHX_1 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.33e23,'cm^2/(mol*s)'), n=0, Ea=(83946.3,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Rh111
Original entry: NH2_X + X <=> NH_X + H_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Rh111 = 2.656E-9(mol/cm^2) to calculate the A factor.
Using the method proposed by Campbell et al. to calculate A actor.
Ea = 0.87eV = 83946.3J/mol

This is reaction (2) in Table S5
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 23,
    label = "X_4 + NHX_2 <=> NX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.33e23,'cm^2/(mol*s)'), n=0, Ea=(98419.8,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Rh111
Original entry: NH_X + X <=> N_X + H_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Rh111 = 2.656E-9(mol/cm^2) to calculate the A factor.
Using the method proposed by Campbell et al. to calculate A actor.
Ea = 1.02eV = 98419.8J/mol

This is reaction (3) in Table S5
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 24,
    label = "HX_5 + OX <=> HOX_1 + X_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.47e21,'cm^2/(mol*s)'), n=0, Ea=(61753.6,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Rh111
Original entry: H_X + O_X <=> OH_X + X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Rh111 = 2.656E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 0.64eV = 61753.6J/mol

This is reaction (4) in Table S5
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 25,
    label = "X_4 + NH2_X <=> NHX_1 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.23e23,'cm^2/(mol*s)'), n=0, Ea=(152454,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pd211
Original entry: NH2_X + X <=> NH_X + H_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd211 = 2.688E-9(mol/cm^2) to calculate the A factor.
Using the method proposed by Campbell et al. to calculate A actor.
Ea = 1.58eV = 152454.2J/mol

This is reaction (2) in Table S4
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 26,
    label = "X_4 + NHX_2 <=> NX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.23e23,'cm^2/(mol*s)'), n=0, Ea=(118683,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pd211
Original entry: NH_X + X <=> N_X + H_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd211 = 2.688E-9(mol/cm^2) to calculate the A factor.
Using the method proposed by Campbell et al. to calculate A actor.
Ea = 1.23eV = 118682.7J/mol

This is reaction (3) in Table S4
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 27,
    label = "HX_5 + OX <=> HOX_1 + X_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.44e21,'cm^2/(mol*s)'), n=0, Ea=(123507,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pd211
Original entry: H_X + O_X <=> OH_X + X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd211 = 2.688E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 1.28eV = 123507.2J/mol

This is reaction (4) in Table S4
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 28,
    label = "X_4 + NH2_X <=> NHX_1 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.44e23,'cm^2/(mol*s)'), n=0, Ea=(85876.1,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pd111
Original entry: NH2_X + X <=> NH_X + H_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd111 = 2.534E-9(mol/cm^2) to calculate the A factor.
Using the method proposed by Campbell et al. to calculate A actor.
Ea = 0.89eV = 85876.1J/mol

This is reaction (2) in Table S5
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 29,
    label = "X_4 + NHX_2 <=> NX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.44e23,'cm^2/(mol*s)'), n=0, Ea=(113858,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pd111
Original entry: NH_X + X <=> N_X + H_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd111 = 2.534E-9(mol/cm^2) to calculate the A factor.
Using the method proposed by Campbell et al. to calculate A actor.
Ea = 1.18eV = 113858.2J/mol

This is reaction (3) in Table S5
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 30,
    label = "HX_5 + OX <=> HOX_1 + X_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.47e21,'cm^2/(mol*s)'), n=0, Ea=(97454.9,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pd111
Original entry: H_X + O_X <=> OH_X + X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd111 = 2.534E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 1.01eV = 97454.9J/mol

This is reaction (4) in Table S5
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 31,
    label = "X_4 + NH2_X <=> NHX_1 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(6.33e21,'cm^2/(mol*s)'), n=0, Ea=(92630.4,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Popa_Rh111
Original entry: NH2_X + X <=> NH_X + H_X
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

entry(
    index = 32,
    label = "X_4 + NHX_2 <=> NX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(7.94e21,'cm^2/(mol*s)'), n=0, Ea=(97454.9,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Popa_Rh111
Original entry: NH_X + X <=> N_X + H_X
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

entry(
    index = 33,
    label = "NOX + OX <=> NO2X + X_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.52e19,'cm^2/(mol*s)'), n=1.015, Ea=(155285,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ishikawa_Rh111
Original entry: NO_X + O_X <=> NO2_X + X
"First-Principles Microkinetic Analysis of NO + CO Reactions on
Rh(111) Surface toward Understanding NOx Reduction Pathways"
Atsushi Ishikawa and Yoshitaka Tateyama
J. Phys. Chem. C 2018, 122, 30, 17378–17388
https://doi.org/10.1021/acs.jpcc.8b05906
This reaction used RMG's surface site density of Rh111 = 2.656E-09(mol/cm^2) to calculate the A factor.
The modified Arrhenius parameters is calculed from 
Table 2. Activation Energy (Ea) 
and 
Table S3. Reaction rate constant at different temperatures
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 34,
    label = "X_4 + NO2X <=> OX + NOX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.29e20,'cm^2/(mol*s)'), n=0, Ea=(83000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Scheuer_Pt
Original entry: NO2_X + X <=> NO_X + O_X
"Dual layer automotive ammonia oxidation catalysts: Experiments and computer simulation"
Scheuer et al. Applied Catalysis B: Environmental 111–112 (2012) 445–455
https://doi.org/10.1016/j.apcatb.2011.10.032

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 3.2E11(1/s)/2.483E-9(mol/cm^2) = 1.29E20 cm^2/(mol*s)

This is R12 in Table 1
""",
    metal = "Pt",
)

entry(
    index = 35,
    label = "X_4 + NH2_X <=> NHX_1 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(8.34e19,'cm^2/(mol*s)'), n=0, Ea=(56929.1,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Duan_Ni111
Original entry: NH2_X + X <=> NH_X + H_X
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
    index = 36,
    label = "X_4 + NHX_2 <=> NX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.46e19,'cm^2/(mol*s)'), n=0, Ea=(107104,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Duan_Ni111
Original entry: NH_X + X <=> N_X + H_X
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
    index = 37,
    label = "X_4 + NH2_X <=> NHX_1 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.31e20,'cm^2/(mol*s)'), n=0, Ea=(86841,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Duan_Ni211
Original entry: NH2_X + X <=> NH_X + H_X
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
    index = 38,
    label = "X_4 + NHX_2 <=> NX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.36e21,'cm^2/(mol*s)'), n=0, Ea=(100350,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Duan_Ni211
Original entry: NH_X + X <=> N_X + H_X
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
    index = 39,
    label = "X_4 + HOX_1 <=> OX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(7.85e20,'cm^2/(mol*s)'), n=1.872, Ea=(27.1,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Pt111
Original entry: OH_X + X <=> H_X + O_X
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1.95E12(1/s)/2.483E-9(mol/cm^2) = 7.85E20 cm^2/(mol*s)

This is R13 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 40,
    label = "X_4 + CH3X_1 <=> CH2X_3 + HX_5",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(4.47e19,'cm^2/(mol*s)'), n=0.419, Ea=(15.8,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Pt111
Original entry: CH3_X + X <=> CH2_X + H_X
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 1.11E11(1/s)/2.483E-9(mol/cm^2) = 4.47E19 cm^2/(mol*s)

This is R57 in Table 2
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 41,
    label = "X_4 + CH2X_1 <=> CHX_3 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.1e19,'cm^2/(mol*s)'), n=0.222, Ea=(9,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Pt111
Original entry: CH2_X + X <=> CH_X + H_X
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 5.22E10(1/s)/2.483E-9(mol/cm^2) = 2.10E19 cm^2/(mol*s)

This is R59 in Table 2
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 42,
    label = "X_4 + CHX_1 <=> CX_3 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.67e19,'cm^2/(mol*s)'), n=0.398, Ea=(31.3,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Pt111
Original entry: CH_X + X <=> C_X + H_X
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 9.11E10(1/s)/2.483E-9(mol/cm^2) = 3.67E19 cm^2/(mol*s)

This is R61 in Table 2
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 43,
    label = "X_4 + CXHO_1 <=> OCX_3 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.86e19,'cm^2/(mol*s)'), n=0.33, Ea=(0,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Pt111
Original entry: HCO_X + X <=> CO_X + H_X
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 7.11E10(1/s)/2.483E-9(mol/cm^2) = 2.86E19 cm^2/(mol*s)

This is R99 in Table 2
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 44,
    label = "X_4 + NHX_2 <=> NX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(7.22e20,'cm^2/(mol*s)'), n=0, Ea=(5.3,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Ru0001
Original entry: NH_X + X <=> N_X + H_X
"The role of adsorbate–adsorbate interactions in the rate controlling step 
and the most abundant reaction intermediate of NH3 decomposition on Ru"
D.G. Vlachos et al. (2004). Catalysis Letters 96, 13–22. 
https://doi.org/10.1023/B:CATL.0000029523.22277.e1

This reaction used RMG's surface site density of Ru0001 = 2.630E-9(mol/cm^2) to calculate the A factor.
A = 1.9E12(1/s)/2.630E-9(mol/cm^2) = 7.22E20 cm^2/(mol*s)

This is R5 in Table 2 (set A)
""",
    metal = "Ru",
    facet = "0001",
)

entry(
    index = 45,
    label = "X_4 + NH2_X <=> NHX_1 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(7.6e20,'cm^2/(mol*s)'), n=0, Ea=(20.1,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Ru0001
Original entry: NH2_X + X <=> NH_X + H_X
"The role of adsorbate–adsorbate interactions in the rate controlling step 
and the most abundant reaction intermediate of NH3 decomposition on Ru"
D.G. Vlachos et al. (2004). Catalysis Letters 96, 13–22. 
https://doi.org/10.1023/B:CATL.0000029523.22277.e1

This reaction used RMG's surface site density of Ru0001 = 2.630E-9(mol/cm^2) to calculate the A factor.
A = 2E12(1/s)/2.630E-9(mol/cm^2) = 7.60E20 cm^2/(mol*s)

This is R7 in Table 2 (set A)
""",
    metal = "Ru",
    facet = "0001",
)

entry(
    index = 46,
    label = "X_4 + CH3X_1 <=> CH2X_3 + HX_5",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(1e19,'cm^2/(mol*s)'), n=0.0862, Ea=(12.2,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Rh
Original entry: CH3_X + X <=> CH2_X + H_X
"Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
Vlachos et al. (2008)
Journal of Catalysis,259(2), 211-222, 0021-9517
DOI: 10.1016/j.jcat.2008.08.008.D.G.

Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
A = 2.49E+10(1/s)/2.49E-9(mol/cm^2) = 1.00E+19 cm^2/(mol*s)

This is R57 in Table 4
""",
    metal = "Rh",
)

entry(
    index = 47,
    label = "X_4 + CH2X_1 <=> CHX_3 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.21e19,'cm^2/(mol*s)'), n=-0.1312, Ea=(21.7,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Rh
Original entry: CH2_X + X <=> CH_X + H_X
"Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
Vlachos et al. (2008)
Journal of Catalysis,259(2), 211-222, 0021-9517
DOI: 10.1016/j.jcat.2008.08.008.D.G.

Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
A = 5.50E+10(1/s)/2.49E-9(mol/cm^2) = 2.21E+19 cm^2/(mol*s)

This is R59 in Table 4
""",
    metal = "Rh",
)

entry(
    index = 48,
    label = "X_4 + CHX_1 <=> CX_3 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.84e21,'cm^2/(mol*s)'), n=-0.2464, Ea=(28.9,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Rh
Original entry: CH_X + X <=> C_X + H_X
"Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
Vlachos et al. (2008)
Journal of Catalysis,259(2), 211-222, 0021-9517
DOI: 10.1016/j.jcat.2008.08.008.D.G.

Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
A = 4.58E+12(1/s)/2.49E-9(mol/cm^2) = 1.84E+21 cm^2/(mol*s)

This is R61 in Table 4
""",
    metal = "Rh",
)

entry(
    index = 49,
    label = "X_4 + H3N2X <=> H2N2X + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.34e17,'cm^2/(mol*s)'), n=1.942, Ea=(121577,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Cu111
Original entry: N2H3_X + X <=> NN=[Pt] + H_X
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This reaction used RMG's surface site density of Cu111 = 2.943E-9(mol/cm^2) to estimate A factor.
A and n was calculated by numpy.linalg.lstsq from Table 1

This is R10 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 50,
    label = "X_4 + H2N2X2 <=> HN2X2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(1.07e19,'cm^2/(mol*s)'), n=1.134, Ea=(141840,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Cu111
Original entry: [Pt]NN[Pt] + X <=> [Pt]NN=[Pt] + H_X
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This reaction used RMG's surface site density of Cu111 = 2.943E-9(mol/cm^2) to estimate A factor.
A and n was calculated by numpy.linalg.lstsq from Table 1

This is R16 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 51,
    label = "X_4 + HN2X2-2 <=> N2X2 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.43e18,'cm^2/(mol*s)'), n=1.285, Ea=(16403,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Cu111
Original entry: [Pt]NN=[Pt] + X <=> [Pt]=NN=[Pt] + H_X
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This reaction used RMG's surface site density of Cu111 = 2.943E-9(mol/cm^2) to estimate A factor.
A and n was calculated by numpy.linalg.lstsq from Table 1

This is R18 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 52,
    label = "X_4 + H3N2X-2 <=> NHX_1 + H2NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.87e16,'cm^2/(mol*s)'), n=2.065, Ea=(86841,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Cu111
Original entry: N2H3_X + X <=> NH2_X + NH_X
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This reaction used RMG's surface site density of Cu111 = 2.943E-9(mol/cm^2) to estimate A factor.
A and n was calculated by numpy.linalg.lstsq from Table 1

This is R22 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 53,
    label = "X_4 + H2N2X-2 <=> NX + H2NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.03e19,'cm^2/(mol*s)'), n=0.559, Ea=(130262,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Cu111
Original entry: NN=[Pt] + X <=> NH2_X + N_X
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This reaction used RMG's surface site density of Cu111 = 2.943E-9(mol/cm^2) to estimate A factor.
A and n was calculated by numpy.linalg.lstsq from Table 1

This is R24 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 54,
    label = "X_4 + NH2_X <=> NHX_1 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(5.67e19,'cm^2/(mol*s)'), n=0.513, Ea=(135086,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Cu111
Original entry: NH2_X + X <=> NH_X + H_X
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This reaction used RMG's surface site density of Cu111 = 2.943E-9(mol/cm^2) to estimate A factor.
A and n was calculated by numpy.linalg.lstsq from Table 1

This is R32 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 55,
    label = "X_4 + NHX_2 <=> NX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.66e19,'cm^2/(mol*s)'), n=0.853, Ea=(172717,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Cu111
Original entry: NH_X + X <=> N_X + H_X
"Micro-kinetic simulations of the catalytic decomposition 
of hydrazine on the Cu(111) surface"
Tafreshi, S. S., Roldan, A. & de Leeuw, N. H. (2017). Faraday Discussions, 197, 41-57. 
DOI:10.1039/C6FD00186F

This reaction used RMG's surface site density of Cu111 = 2.943E-9(mol/cm^2) to estimate A factor.
A and n was calculated by numpy.linalg.lstsq from Table 1

This is R34 in Table 1
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 56,
    label = "X_4 + H3N2X <=> H2N2X + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.87e21,'cm^2/(mol*s)'), n=0, Ea=(98419.8,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Ir111
Original entry: N2H3_X + X <=> NN=[Pt] + H_X
"Mechanistic study of hydrazine decomposition on Ir(111)"
Alberto Roldan et al. Phys.Chem.Chem.Phys., 2020, 22, 3883
DOI: 10.1039/c9cp06525c

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2)
to estimate a default(1E13) A factor.
A = 1E13(1/s)/2.587E-9(mol/cm^2) = 3.87E21 cm^2/(mol*s)
Ea = 1.02eV = 98419.8J/mol

This is R6 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 57,
    label = "HX_5 + OCX_3 <=> CXHO_1 + X_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4e19,'cm^2/(mol*s)'), n=0, Ea=(30.8,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Mhadeshwar_Pt111
Original entry: CO_X + H_X <=> HCO_X + X
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R106 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 58,
    label = "NOX + NX <=> N2OX + X_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4e19,'cm^2/(mol*s)'), n=0, Ea=(19.8,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Mhadeshwar_Pt111
Original entry: N_X + NO_X <=> N2O_X + X
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R120 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 59,
    label = "X_4 + H3N2X-2 <=> NHX_1 + H2NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.87e21,'cm^2/(mol*s)'), n=0, Ea=(75262.2,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Ir111
Original entry: N2H3_X + X <=> NH2_X + NH_X
"Mechanistic study of hydrazine decomposition on Ir(111)"
Alberto Roldan et al. Phys.Chem.Chem.Phys., 2020, 22, 3883
DOI: 10.1039/c9cp06525c

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2)
to estimate a default(1E13) A factor.
A = 1E13(1/s)/2.587E-9(mol/cm^2) = 3.87E21 cm^2/(mol*s)
Ea = 0.78eV = 75262.2J/mol

This is R12 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 60,
    label = "X_4 + H2N2X-2 <=> NX + H2NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.87e21,'cm^2/(mol*s)'), n=0, Ea=(70437.7,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Ir111
Original entry: NN=[Pt] + X <=> NH2_X + N_X
"Mechanistic study of hydrazine decomposition on Ir(111)"
Alberto Roldan et al. Phys.Chem.Chem.Phys., 2020, 22, 3883
DOI: 10.1039/c9cp06525c

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2)
to estimate a default(1E13) A factor.
A = 1E13(1/s)/2.587E-9(mol/cm^2) = 3.87E21 cm^2/(mol*s)
Ea = 0.73eV = 70437.7J/mol

This is R13 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 61,
    label = "X_4 + NH2_X <=> NHX_1 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(1.43e21,'cm^2/(mol*s)'), n=0, Ea=(151613,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Ir111
Original entry: NH2_X + X <=> NH_X + H_X
"Kinetic and mechanistic analysis of NH3 decomposition 
on Ru(0001), Ru(111) and Ir(111) surfaces"
Alberto Roldan et al. Nanoscale Adv., 2021, 3, 1624
DOI: 10.1039/d1na00015b

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2) to calculate the A factor.
A = 3.71E12(1/s)/2.587E-9(mol/cm^2) = 1.43E21 cm^2/(mol*s)
Ea was calculated from A factor and k rate constant in Table 3

This is R3 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 62,
    label = "X_4 + NHX_2 <=> NX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.68e21,'cm^2/(mol*s)'), n=0, Ea=(88354.1,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Ir111
Original entry: NH_X + X <=> N_X + H_X
"Kinetic and mechanistic analysis of NH3 decomposition 
on Ru(0001), Ru(111) and Ir(111) surfaces"
Alberto Roldan et al. Nanoscale Adv., 2021, 3, 1624
DOI: 10.1039/d1na00015b

This reaction used RMG's surface site density of Ir111 = 2.587E-9(mol/cm^2) to calculate the A factor.
A = 6.93E12(1/s)/2.587E-9(mol/cm^2) = 2.68E21 cm^2/(mol*s)
Ea was calculated from A factor and k rate constant in Table 3

This is R5 in Table 3
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 63,
    label = "X_4 + NH2_X <=> NHX_1 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(1.52e21,'cm^2/(mol*s)'), n=0, Ea=(62155,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Ru0001
Original entry: NH2_X + X <=> NH_X + H_X
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

entry(
    index = 64,
    label = "X_4 + NHX_2 <=> NX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.71e21,'cm^2/(mol*s)'), n=0, Ea=(99817.1,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Roldan_Ru0001
Original entry: NH_X + X <=> N_X + H_X
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

entry(
    index = 65,
    label = "X_4 + HOCXO_1 <=> OCX_3 + HOX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.3e20,'cm^2/(mol*s)'), n=-0.4123, Ea=(7.5,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Rh
Original entry: COOH_X + X <=> CO_X + OH_X
"Steam and dry reforming of methane on Rh: Microkinetic analysis and hierarchy of kinetic models"
Vlachos et al. (2008)
Journal of Catalysis,259(2), 211-222, 0021-9517
DOI: 10.1016/j.jcat.2008.08.008.D.G.

Surface site density of Rh from the paper = 2.49E-9(mol/cm^2).
A = 1.07E+12(1/s)/2.49E-9(mol/cm^2) = 4.30E+20 cm^2/(mol*s)

This is R31 in Table 4
""",
    metal = "Rh",
)

entry(
    index = 66,
    label = "X_4 + HOCXO_1 <=> OCX_3 + HOX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.4e17,'cm^2/(mol*s)'), n=0.024, Ea=(5.3,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Vlachos_Pt111
Original entry: COOH_X + X <=> CO_X + OH_X
"A Catalytic Reaction Mechanism for Methane Partial Oxidation at Short Contact Times, 
Reforming, and Combustion, and for Oxygenate Decomposition and Oxidation on Platinum"
D.G. Vlachos et al. (2007)
Industrial & Engineering Chemistry Research, 46(16), 5310-5324.
DOI: 10.1021/ie070322c

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 8.43E08(1/s)/2.483E-9(mol/cm^2) = 3.40E17 cm^2/(mol*s)

This is R29 in Table 1
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 67,
    label = "HX_5 + OX <=> HOX_1 + X_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4e19,'cm^2/(mol*s)'), n=0, Ea=(8.6,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Mhadeshwar_Pt111
Original entry: H_X + O_X <=> OH_X + X
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R20 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 68,
    label = "HOX_5 + OCX_3 <=> HOCXO_1 + X_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4e19,'cm^2/(mol*s)'), n=0, Ea=(18.7,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Mhadeshwar_Pt111
Original entry: CO_X + OH_X <=> COOH_X + X
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R30 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 69,
    label = "HX_5 + NHX_1 <=> NH2_X + X_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4e19,'cm^2/(mol*s)'), n=0, Ea=(16.5,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Mhadeshwar_Pt111
Original entry: NH_X + H_X <=> NH2_X + X
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R52 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 70,
    label = "HX_5 + NX <=> NHX_2 + X_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4e19,'cm^2/(mol*s)'), n=0, Ea=(24.5,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Mhadeshwar_Pt111
Original entry: N_X + H_X <=> NH_X + X
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 1E11(1/s)/2.5E-9(mol/cm^2) = 4E19 cm^2/(mol*s)

This is R54 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 71,
    label = "NOX + OX <=> NO2X + X_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.2e21,'cm^2/(mol*s)'), n=0.93, Ea=(21.2,'kcal/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Mhadeshwar_Pt111
Original entry: NO_X + O_X <=> NO2_X + X
"A detailed microkinetic model for diesel engine emissions oxidation 
on platinum based diesel oxidation catalysts (DOC)"
Hom Sharma & Ashish Mhadeshwar. (2012). 
Applied Catalysis B: Environmental, 127, 190-204
DOI: 10.1016/j.apcatb.2012.08.021

Surface site density used in this paper is 2.5E-9 mol/cm^2
A = 3E12(1/s)/2.5E-9(mol/cm^2) = 1.2E21 cm^2/(mol*s)

This is R80 in Appendix A
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 72,
    label = "X_4 + NH2_X <=> NHX_1 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.19e23,'cm^2/(mol*s)'), n=0, Ea=(117718,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Rh211
Original entry: NH2_X + X <=> NH_X + H_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Rh211 = 2.817E-9(mol/cm^2) to calculate the A factor.
Using the method proposed by Campbell et al. to calculate A actor.
Ea = 1.22eV = 117717.8J/mol

This is reaction (2) in Table S4
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 73,
    label = "X_4 + NHX_2 <=> NX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.19e23,'cm^2/(mol*s)'), n=0, Ea=(88770.8,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Rh211
Original entry: NH_X + X <=> N_X + H_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Rh211 = 2.817E-9(mol/cm^2) to calculate the A factor.
Using the method proposed by Campbell et al. to calculate A actor.
Ea = 0.92eV = 88770.8J/mol

This is reaction (3) in Table S4
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 74,
    label = "HX_5 + OX <=> HOX_1 + X_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.33e21,'cm^2/(mol*s)'), n=0, Ea=(85876.1,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Rh211
Original entry: H_X + O_X <=> OH_X + X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Rh211 = 2.817E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 0.89eV = 85876.1J/mol

This is reaction (4) in Table S4
""",
    metal = "Rh",
    facet = "211",
)

