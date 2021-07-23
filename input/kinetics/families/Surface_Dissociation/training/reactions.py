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
        A=(4.02E14, 'm^2/(mol*s)'),
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
        A=(1.46E20, 'm^2/(mol*s)'),
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
4.667E11 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 1.586e16 m^2/(mol*s)
Erxn = 0.14 eV
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
)

entry(
    index = 6,
    label = "CH2X_3 + HX_5 <=> CH3X_1 + X_4",
    degeneracy = 3,
    kinetics = SurfaceArrhenius(
        A=(3.09E19, 'm^2/(mol*s)'),
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


entry(
    index = 7,
    label = "CHX_3 + HX_5 <=> CH2X_1 + X_4",
    degeneracy = 2,
    kinetics = SurfaceArrhenius(
        A=(9.77E20, 'm^2/(mol*s)'),
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

#Delgado has this reaction as exothermic. However, our own thermo has this reaction as endothermic. removing and replacing with reverse direction, R20.
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
2.570E12 1/s 2.943e‐5 mol/m^2 = 8.733e16 m^2/(mol*s)
Erxn = 2.18 eV
""",
    metal = "Cu",
)

# entry(
#     index = 11,
#     label = "HCOH* + HX_5 <=> CH2OH* + X_4",
#     degeneracy = 1,
#     kinetics = SurfaceArrhenius(
#         A=(1.257e17, 'm^2/(mol*s)'),
#         n = 0.0,
#         Ea=(54.4228933, 'kcal/mol'),
#         Tmin = (298, 'K'),
#         Tmax = (2000, 'K'),
#     ),
#     rank=10,
#     shortDesc = u"""Default""",
#     longDesc = u"""
# Reaction 32 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
# and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

# A factor from paper / surface site density of Cu
# 3.698E12 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 1.257e17 m^2/(mol*s)
# """,
#     metal = "Cu",
# )
# HCOH* is CH2Ovdw and doesn't match this family - David


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
Erxn = 0.72 eV
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
Erxn = 1.39 eV
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
Catalysts, 2015, 5, 871-904. Reaction R8
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
eErxn = 0.78
""",
    metal = "Cu",
)
entry(
    index = 17,
    label = "X_4 + NH2_X <=> NHX_1 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(8.34e+19,'cm^2/(mol*s)'), n=0, Ea=(56929.1,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Duan_Ni111
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
A = k/exp(Ea/RT) = 1.03E8(1/s)/exp(-56929.1(J/mol)/8.314(J/mol/K)/873K) = 2.63E11/s
  = (2.63E11/s)/3.148E-9(mol/cm^2) = 8.34E19cm^2/mol/s

Ea = 0.59eV = 56929.1J/mol

This is reaction 2 from Table 2
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 18,
    label = "X_4 + NHX_2 <=> NX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.46e+19,'cm^2/(mol*s)'), n=0, Ea=(107104,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Duan_Ni111
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
A = k/exp(-Ea/RT) = 3.02E4(1/s)/exp(-107103.9J/mol / 8.314(J/mol/K)/873K) =  7.74E10/s
  = (7.74E10/s)/3.148E-9(mol/cm^2) = 2.46E19 cm^2/mol/s

Ea = 1.11eV = 107103.9J/mol

This is reaction 3 from Table 2
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 19,
    label = "X_4 + NH2_X <=> NHX_1 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.31e+20,'cm^2/(mol*s)'), n=0, Ea=(86841,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Duan_Ni211
Original entry: NH2_X + X <=> NH_X + H_X
"Structure sensitivity of ammonia decomposition 
over Ni catalysts: A computational and experimental study"
Duan et al. Fuel Processing Technology 108 (2013) 112–117
https://doi.org/10.1016/j.fuproc.2012.05.030

This reaction used RMG's surface site density of Ni211 = 3.339E-9(mol/cm^2) to calculate the A factor.
A = k/exp(-Ea/RT) = 4.91E6(1/s)/exp(-86841(J/mol)/8.314(J/mol/K)/873K) = 7.71E11/s
  = (7.71E11/s)/3.339E-9(mol/cm^2) = 2.31E20 cm^2/mol/s

Ea = 0.9eV = 86841J/mol

This is reaction 2 from Table 2
""",
    metal = "Ni",
    facet = "211",
)

entry(
    index = 20,
    label = "X_4 + NHX_2 <=> NX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.36e+21,'cm^2/(mol*s)'), n=0, Ea=(100350,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Duan_Ni211
Original entry: NH_X + X <=> N_X + H_X
"Structure sensitivity of ammonia decomposition 
over Ni catalysts: A computational and experimental study"
Duan et al. Fuel Processing Technology 108 (2013) 112–117
https://doi.org/10.1016/j.fuproc.2012.05.030

This reaction used RMG's surface site density of Ni211 = 3.339E-9(mol/cm^2) to calculate the A factor.
A = k/exp(-Ea/RT) = 1.11E7(1/s)/exp(-100349.6(J/mol)/8.314(J/mol/K)/873K) = 1.12E13/s
  = (1.12E13/s)/3.339E-9(mol/cm^2) = 3.36E21 cm^2/mol/s

Ea = 1.04eV = 100349.6J/mol

This is reaction 3 from Table 2
""",
    metal = "Ni",
    facet = "211",
)

entry(
    index = 21,
    label = "X_4 + NH2_X <=> NHX_1 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(1.8e+19,'cm^2/(mol*s)'), n=0.783, Ea=(86000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Novell_Pd111
Original entry: NH2_X + X <=> NH_X + H_X
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
    index = 22,
    label = "X_4 + NHX_2 <=> NX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(8.14e+17,'cm^2/(mol*s)'), n=1.445, Ea=(113000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Novell_Pd111
Original entry: NH_X + X <=> N_X + H_X
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
    index = 23,
    label = "X_4 + NH2_X <=> NHX_1 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(4.43e+21,'cm^2/(mol*s)'), n=0, Ea=(101000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Novell_Pt111
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
    index = 24,
    label = "X_4 + NHX_2 <=> NX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(5.236e+21,'cm^2/(mol*s)'), n=0, Ea=(116000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Novell_Pt111
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
    index = 25,
    label = "X_4 + NH2_X <=> NHX_1 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(1.23e+19,'cm^2/(mol*s)'), n=0.902, Ea=(84000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Novell_Rh111
Original entry: NH2_X + X <=> NH_X + H_X
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
    index = 26,
    label = "X_4 + NHX_2 <=> NX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.1e+19,'cm^2/(mol*s)'), n=0.965, Ea=(98000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Novell_Rh111
Original entry: NH_X + X <=> N_X + H_X
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
    index = 27,
    label = "X_4 + NH2_X <=> NHX_1 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.01e+21,'cm^2/(mol*s)'), n=0, Ea=(110000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Offermans_Pt111
Original entry: NH2_X + X <=> NH_X + H_X
"Ammonia oxidation on platinum : a density functional theory study of surface reactivity."
Offermans, W. K. (2007). Technische Universiteit Eindhoven. 
https://doi.org/10.6100/IR630067

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 300K) = 5.0E12(1/s)/2.483E-9(mol/cm^2) = 2.01E21 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 28,
    label = "X_4 + NHX_2 <=> NX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.9e+21,'cm^2/(mol*s)'), n=0, Ea=(118000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia/Offermans_Pt111
Original entry: NH_X + X <=> N_X + H_X
"Ammonia oxidation on platinum : a density functional theory study of surface reactivity."
Offermans, W. K. (2007). Technische Universiteit Eindhoven. 
https://doi.org/10.6100/IR630067

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 300K) = 7.2E12(1/s)/2.483E-9(mol/cm^2) = 2.90E21 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

