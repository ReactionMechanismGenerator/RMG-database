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
    label = "OCX_3 + HOX_5 <=> HOCXO_1 + Ni_4",
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
    index = 4,
    label = "HOCXO_1 + Ni_4 <=> OCX_3 + HOX_5",
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
    index = 10,
    label = "OCX_3 + HOX_5 <=> HOCXO_1 + Ni_4",
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
    index = 9,
    label = "NH2_X + Ni_4 <=> NHX_1 + HX_5",
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
    index = 11,
    label = "NHX_2 + Ni_4 <=> NX + HX_5",
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
    index = 16,
    label = "CH2X_3 + HX_5 <=> CH3X_1 + Ni_4",
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
    index = 18,
    label = "CHX_3 + HX_5 <=> CH2X_1 + Ni_4",
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
#    index = 19,
#    label = "CHX_1 + Ni_4 <=> CX_3 + HX_5",
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
    index = 20,
    label = "CX_3 + HX_5 <=> CHX_1 + Ni_4",
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
    index = 28,
    label = "HCOO* + Ni_4 <=> HCO* + OX_3",
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
#     index = 31,
#     label = "HCOH* + HX_5 <=> CH2OH* + Ni_4",
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
    index = 32,
    label = "HOX_1 + Ni_4 <=> OX_3 + HX_5",
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
    index = 15,
    label = "HOX_1 + Ni_4 <=> OX_3 + HX_5",
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
    index = 36,
    label = "CH3O2* + Ni_4 <=> CH2OH*_2 + OX_3",
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
    index = 48,
    label = "CXHO_1 + Ni_4 <=> OCX_3 + HX_5",
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
    index = 26,
    label = "OCX_3 + HX_5 <=> CXHO_1 + Ni_4",
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
    index = 49,
    label = "Ni_4 + C3H7X <=> C3H6X + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.24607e+17,'m^2/(mol*s)'), n=0, Ea=(1.28206,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNTYx""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: X + CH3CHCH3X <=> HX + CH3CCH3X
equation : CH3CHCH3* + * -> CH3CCH3* + H*
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangTheory-aided2020
reactionEnergy: 0.4294684278429486 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C[CH]C from Thermo library: DFT_QCI_thermo and S298=68.90 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 50,
    label = "Ni_4 + C3H7X-2 <=> C3H6X-2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(4.51174e+17,'m^2/(mol*s)'), n=0, Ea=(1.17456,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNjM0""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: X + CH3CH2CH2X <=> HX + CH3CH2CHX
equation : CH3CH2CH2* + * -> CH3CH2CH* + H*
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangTheory-aided2020
reactionEnergy: 0.36504887795308605 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2]CC from Thermo library: DFT_QCI_thermo and S298=69.30 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 51,
    label = "Ni_4 + C3H6X2 <=> C3H5X2 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.9542e+17,'m^2/(mol*s)'), n=0, Ea=(1.30475,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNjM2""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: X + CH3CHCH2X <=> HX + CH3CCH2X
equation : CH3CHCH2* + * -> CH3CCH2* + H*
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangTheory-aided2020
reactionEnergy: 0.4804277306247968 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C=CC from Thermo library: DFT_QCI_thermo and S298=63.63 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 52,
    label = "Ni_4 + C3H6X-3 <=> C3H5X + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.832e+17,'m^2/(mol*s)'), n=0, Ea=(0.509346,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNjM3""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: X + CH3CH2CHX <=> HX + CH3CH2CX
equation : CH3CH2CH* + * -> CH3CH2C* + H*
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangTheory-aided2020
reactionEnergy: -0.47169274036423303 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]CC from Thermo library: DFT_QCI_thermo + radical(CCJ2_triplet) and S298=69.63 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 53,
    label = "Ni_4 + C3H5X2-2 <=> C3H4X2 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.40678e+17,'m^2/(mol*s)'), n=0, Ea=(0.865005,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNjQx""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: X + CH3CHCHX <=> HX + CH3CCHX
equation : CH3CHCH* + * -> CH3CCH* + H*
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangTheory-aided2020
reactionEnergy: -0.032313382282154635 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]=CC from Thermo library: DFT_QCI_thermo and S298=64.88 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 54,
    label = "Ni_4 + C3H5X2-3 <=> C3H4X2-2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.60805e+17,'m^2/(mol*s)'), n=0, Ea=(0.874132,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNjQy""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: X + CH3CCH2X <=> HX + CH3CCHX
equation : CH3CCH2* + * -> CH3CCH* + H*
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangTheory-aided2020
reactionEnergy: 0.005748404830228537 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C=[C]C from Thermo library: DFT_QCI_thermo and S298=65.41 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 55,
    label = "HX_5 + NX <=> NHX_2 + Ni_4",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(A=(1.46209e+16,'m^2/(mol*s)'), n=0, Ea=(1.20085,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyOTk0""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: HX + NX <=> X + NHX
equation : H* + N* - 0* -> NH* + *
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangAchieving2021
reactionEnergy: -0.20887132629286498 eV

A factor estimation:
A factor estimate for association
A factor estimated from gas-phase smiles [NH] from Thermo library: primaryThermoLibrary and S298=43.26 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 56,
    label = "HX_5 + NHX_1 <=> NH2_X + Ni_4",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(A=(6.14127e+16,'m^2/(mol*s)'), n=0, Ea=(1.39259,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyOTk1""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: HX + NHX <=> X + NH2X
equation : NH* + H* - 0* -> NH2* + *
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangAchieving2021
reactionEnergy: -0.5828880041954108 eV

A factor estimation:
A factor estimate for association
A factor estimated from gas-phase smiles [NH2] from Thermo library: primaryThermoLibrary and S298=46.52 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 57,
    label = "Ni_4 + CHX_1 <=> CX_3 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.54179e+16,'m^2/(mol*s)'), n=0, Ea=(1.38,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODEy""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: CHX + X <=> CX + HX
equation : CH* -> C* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 0.389 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH] from Thermo library: DFT_QCI_thermo and S298=43.64 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 58,
    label = "Ni_4 + CH2X_1 <=> CHX_3 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(3.75303e+16,'m^2/(mol*s)'), n=0, Ea=(0.77,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODM3""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: CH2X + X <=> HX + CHX
equation : CH2* -> CH* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: -0.16 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2] from Thermo library: primaryThermoLibrary and S298=46.64 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 59,
    label = "Ni_4 + HOX_1 <=> OX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.13337e+16,'m^2/(mol*s)'), n=0, Ea=(1.41,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTAyMA==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: OHX + X <=> HX + OX
equation : OH* -> H* + O*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 0.787 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [OH] from Thermo library: primaryThermoLibrary and S298=43.96 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 60,
    label = "Ni_4 + CH2OX2 <=> CHOX2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(4.58249e+16,'m^2/(mol*s)'), n=0, Ea=(0.55559,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTA0MQ==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: OCH2X + X <=> HX + HCOX
equation : H2CO* -> HCO* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: Studt et al submitted
reactionEnergy: -0.42032 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C=O from Thermo library: DFT_QCI_thermo and S298=52.16 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 61,
    label = "Ni_4 + NHX_2 <=> NX + HX_5",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(A=(2.13171e+16,'m^2/(mol*s)'), n=0, Ea=(1.54,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTA3OA==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: NHX + X <=> HX + NX
equation : NH* -> H* + N*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 0.24 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [NH] from Thermo library: primaryThermoLibrary and S298=43.26 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 62,
    label = "Ni_4 + NH2_X <=> NHX_1 + HX_5",
    degeneracy = 2.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(A=(3.29883e+16,'m^2/(mol*s)'), n=0, Ea=(1.95,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTE0MQ==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: NH2X + X <=> HX + NHX
equation : NH2* -> NH* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 0.72 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [NH2] from Thermo library: primaryThermoLibrary and S298=46.52 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 63,
    label = "Ni_4 + CH3OX <=> OX + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.27272e+16,'m^2/(mol*s)'), n=0, Ea=(1.792,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTMxMQ==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: OCH3X + X <=> OX + CH3X
equation : OCH3* -> CH3* + O*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 0.682 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C[O] from Thermo library: DFT_QCI_thermo and S298=54.42 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 64,
    label = "Ni_4 + HOCXO_1 <=> OCX_3 + HOX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.09952e+17,'m^2/(mol*s)'), n=0, Ea=(0.99,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MjM5OA==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: COOHX + X <=> COX + OHX
equation : COOH* -> CO* + OH*
dft_code : DACAPO
dftFunctional : RPBE
pubId: YooTheoretical2014
reactionEnergy: -0.17 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles O=[C]O from Thermo library: DFT_QCI_thermo and S298=60.19 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 65,
    label = "Ni_4 + CH2OH* <=> HCOH* + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(1.1079e+17,'m^2/(mol*s)'), n=0, Ea=(1.14806,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI2ODU=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: X + H3COX <=> HX + CHOHX
equation : CH2OH* + * -> CHOH* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: -0.0872325574892 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2]O from Thermo library: DFT_QCI_thermo and S298=58.19 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 66,
    label = "Ni_4 + CH2X_1 <=> CHX_3 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(3.75303e+16,'m^2/(mol*s)'), n=0, Ea=(0.579256,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI3MzU=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: X + CH2X <=> HX + CHX
equation : CH2* + * -> CH* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: -0.38272758649 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2] from Thermo library: primaryThermoLibrary and S298=46.64 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 67,
    label = "Ni_4 + C2H2OX2 <=> C2HOX2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(7.90722e+16,'m^2/(mol*s)'), n=0, Ea=(0.987333,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI3NTk=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: X + CH2COX <=> HX + CHCOX
equation : CH2CO* + * -> CHCO* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: 0.0322436545102 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C=C=O from Thermo library: DFT_QCI_thermo and S298=57.63 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 68,
    label = "Ni_4 + C2H3OX <=> OCX_3 + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.94915e+17,'m^2/(mol*s)'), n=0, Ea=(1.15951,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI4MTk=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: X + CH3COX <=> COX + CH3X
equation : CH3CO* + * -> CH3* + CO*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: -0.531420322484 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C[C]=O from Thermo library: DFT_QCI_thermo and S298=63.74 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 69,
    label = "Ni_4 + CH2OX <=> CHX_3 + HOX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.16208e+17,'m^2/(mol*s)'), n=0, Ea=(1.26775,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI4MjU=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: X + CHOHX <=> CHX + OHX
equation : CHOH* + * -> CH* + OH*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: 0.2931777755 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]O from Thermo library: DFT_QCI_thermo and S298=58.32 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 70,
    label = "Ni_4 + CXHO_1 <=> OCX_3 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(5.78405e+16,'m^2/(mol*s)'), n=0, Ea=(0.123846,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI4NDM=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: X + CHOX <=> HX + COX
equation : CHO* + * -> CO* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: -1.23463251346 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]=O from Thermo library: DFT_QCI_thermo and S298=53.51 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 71,
    label = "Ni_4 + C2H4X2 <=> C2H3X2 + HX_5",
    degeneracy = 4.0,
    kinetics = SurfaceArrhenius(A=(4.91881e+16,'m^2/(mol*s)'), n=0, Ea=(1.41309,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NTU5""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: X + CH2CH2X <=> HX + CH2CHX
equation : CH2CH2* + * -> CH2CH* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.47487574466504157 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C=C from Thermo library: DFT_QCI_thermo and S298=52.25 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 72,
    label = "Ni_4 + C2H3X2-2 <=> C2H2X2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(8.63145e+16,'m^2/(mol*s)'), n=0, Ea=(0.838373,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NTYy""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: X + CH2CHX <=> HX + CHCHX
equation : CH2CH* + * -> CHCH* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: -0.05395269344444387 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]=C from Thermo library: DFT_QCI_thermo and S298=55.78 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 73,
    label = "Ni_4 + C2H2X2-2 <=> C2HX2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(5.94456e+16,'m^2/(mol*s)'), n=0, Ea=(1.54202,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NTY0""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: X + CH2CX <=> HX + CHCX
equation : CH2C* + * -> CHC* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.6825931721250527 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [C]=C from Thermo library: DFT_QCI_thermo and S298=53.10 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 74,
    label = "Ni_4 + C2H5X <=> C2H4X + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(1.34702e+17,'m^2/(mol*s)'), n=0, Ea=(1.12727,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NTY3""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: X + CH3CH2X <=> HX + CH3CHX
equation : CH3CH2* + * -> CH3CH* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.23159290081821382 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C[CH2] from Thermo library: DFT_QCI_thermo and S298=59.12 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 75,
    label = "Ni_4 + C2H4X-2 <=> C2H3X + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.38494e+17,'m^2/(mol*s)'), n=0, Ea=(0.488743,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NTcx""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: X + CH3CHX <=> HX + CH3CX
equation : CH3CH* + * -> CH3C* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: -0.6138357845484279 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]C from Thermo library: DFT_QCI_thermo and S298=59.11 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 76,
    label = "Ni_4 + C2H2X2-3 <=> C2HX2-2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.64307e+16,'m^2/(mol*s)'), n=0, Ea=(1.52152,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NTgx""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: X + CHCHX <=> HX + CHCX
equation : CHCH* + * -> CHC* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.5755292293324601 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C#C from Thermo library: DFT_QCI_thermo and S298=47.73 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 77,
    label = "Ni_4 + C2HX2-3 <=> C2X2 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(9.32934e+16,'m^2/(mol*s)'), n=0, Ea=(1.77467,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NTgy""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: X + CHCX <=> HX + CCX
equation : CHC* + * -> CC* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.8680141349323094 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]=C from Thermo library: DFT_QCI_thermo + radical(Cds_P) and S298=55.86 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 78,
    label = "Ni_4 + C3H7X-2 <=> C3H6X-2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(4.51174e+17,'m^2/(mol*s)'), n=0, Ea=(0.661272,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNTcw""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ni
Original entry: X + CH3CH2CH2X <=> HX + CH3CH2CHX
equation : CH3CH2CH2* + * -> CH3CH2CH* + H*,
dft_code : Quantum Espresso,
dftFunctional : BEEF-vdW,
pubId: WangTheory-aided2020,
reactionEnergy: -0.02355594263644889 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2]CC from Thermo library: DFT_QCI_thermo and S298=69.30 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 79,
    label = "Ni_4 + C3H7X <=> C3H6X + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.24607e+17,'m^2/(mol*s)'), n=0, Ea=(0.866629,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNTcz""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ni
Original entry: X + CH3CHCH3X <=> HX + CH3CCH3X
equation : CH3CHCH3* + * -> CH3CCH3* + H*,
dft_code : Quantum Espresso,
dftFunctional : BEEF-vdW,
pubId: WangTheory-aided2020,
reactionEnergy: 0.16559174715075642 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C[CH]C from Thermo library: DFT_QCI_thermo and S298=68.90 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 80,
    label = "Ni_4 + C3H6X2 <=> C3H5X2 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.9542e+17,'m^2/(mol*s)'), n=0, Ea=(1.0862,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNjY5""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ni
Original entry: X + CH3CHCH2X <=> HX + CH3CCH2X
equation : CH3CHCH2* + * -> CH3CCH2* + H*,
dft_code : Quantum Espresso,
dftFunctional : BEEF-vdW,
pubId: WangTheory-aided2020,
reactionEnergy: 0.4062395661021583 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C=CC from Thermo library: DFT_QCI_thermo and S298=63.63 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 81,
    label = "Ni_4 + C3H6X-3 <=> C3H5X + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.832e+17,'m^2/(mol*s)'), n=0, Ea=(0.259606,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNjcw""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ni
Original entry: X + CH3CH2CHX <=> HX + CH3CH2CX
equation : CH3CH2CH* + * -> CH3CH2C* + H*,
dft_code : Quantum Espresso,
dftFunctional : BEEF-vdW,
pubId: WangTheory-aided2020,
reactionEnergy: -0.5122143005137332 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]CC from Thermo library: DFT_QCI_thermo + radical(CCJ2_triplet) and S298=69.63 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 82,
    label = "Ni_4 + C3H5X2-2 <=> C3H4X2 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.40678e+17,'m^2/(mol*s)'), n=0, Ea=(0.632666,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNjc0""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ni
Original entry: X + CH3CHCHX <=> HX + CH3CCHX
equation : CH3CHCH* + * -> CH3CCH* + H*,
dft_code : Quantum Espresso,
dftFunctional : BEEF-vdW,
pubId: WangTheory-aided2020,
reactionEnergy: -0.42183345777448267 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]=CC from Thermo library: DFT_QCI_thermo and S298=64.88 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 83,
    label = "Ni_4 + C3H5X2-3 <=> C3H4X2-2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.60805e+17,'m^2/(mol*s)'), n=0, Ea=(0.30254,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNjc1""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ni
Original entry: X + CH3CCH2X <=> HX + CH3CCHX
equation : CH3CCH2* + * -> CH3CCH* + H*,
dft_code : Quantum Espresso,
dftFunctional : BEEF-vdW,
pubId: WangTheory-aided2020,
reactionEnergy: -0.7327017493080348 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C=[C]C from Thermo library: DFT_QCI_thermo and S298=65.41 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 84,
    label = "HX_5 + NX <=> NHX_2 + Ni_4",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(A=(1.46209e+16,'m^2/(mol*s)'), n=0, Ea=(1.37574,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMzMDQy""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ni
Original entry: HX + NX <=> X + NHX
equation : H* + N* - 0* -> NH* + *,
dft_code : Quantum Espresso,
dftFunctional : BEEF-vdW,
pubId: WangAchieving2021,
reactionEnergy: -0.21205641888082027 eV

A factor estimation:
A factor estimate for association
A factor estimated from gas-phase smiles [NH] from Thermo library: primaryThermoLibrary and S298=43.26 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ni",
    facet = "211",
)

entry(
    index = 85,
    label = "HX_5 + NHX_1 <=> NH2_X + Ni_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.14127e+16,'m^2/(mol*s)'), n=0, Ea=(1.26748,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMzMDQz""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ni
Original entry: HX + NHX <=> X + NH2X
equation : NH* + H* - 0* -> NH2* + *,
dft_code : Quantum Espresso,
dftFunctional : BEEF-vdW,
pubId: WangAchieving2021,
reactionEnergy: -0.43229761422844604 eV

A factor estimation:
A factor estimate for association
A factor estimated from gas-phase smiles [NH2] from Thermo library: primaryThermoLibrary and S298=46.52 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ni",
    facet = "211",
)

entry(
    index = 86,
    label = "Ni_4 + C2H4X2 <=> C2H3X2 + HX_5",
    degeneracy = 4.0,
    kinetics = SurfaceArrhenius(A=(4.91881e+16,'m^2/(mol*s)'), n=0, Ea=(0.93575,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NDkw""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ni
Original entry: X + CH2CH2X <=> HX + CH2CHX
equation : CH2CH2* + * -> CH2CH* + H*,
dft_code : Quantum ESPRESSO 5.1,
dftFunctional : BEEF-vdW,
pubId: HansenFirst2018,
reactionEnergy: 0.5508780274540186 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C=C from Thermo library: DFT_QCI_thermo and S298=52.25 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 87,
    label = "Ni_4 + C2H2X2-2 <=> C2HX2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(5.94456e+16,'m^2/(mol*s)'), n=0, Ea=(1.12524,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NDk1""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ni
Original entry: X + CH2CX <=> HX + CHCX
equation : CH2C* + * -> CHC* + H*,
dft_code : Quantum ESPRESSO 5.1,
dftFunctional : BEEF-vdW,
pubId: HansenFirst2018,
reactionEnergy: 0.26397363271098584 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [C]=C from Thermo library: DFT_QCI_thermo and S298=53.10 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 88,
    label = "Ni_4 + C2H4X-2 <=> C2H3X + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.38494e+17,'m^2/(mol*s)'), n=0, Ea=(0.269593,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NTAy""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ni
Original entry: X + CH3CHX <=> HX + CH3CX
equation : CH3CH* + * -> CH3C* + H*,
dft_code : Quantum ESPRESSO 5.1,
dftFunctional : BEEF-vdW,
pubId: HansenFirst2018,
reactionEnergy: -0.4990681626368314 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]C from Thermo library: DFT_QCI_thermo and S298=59.11 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 89,
    label = "Ni_4 + C2H4X-3 <=> CHX_3 + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.38494e+17,'m^2/(mol*s)'), n=0, Ea=(1.03948,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NTAz""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ni
Original entry: X + CH3CHX <=> CHX + CH3X
equation : CH3CH* + * -> CH3* + CH*,
dft_code : Quantum ESPRESSO 5.1,
dftFunctional : BEEF-vdW,
pubId: HansenFirst2018,
reactionEnergy: 0.21834258898161352 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]C from Thermo library: DFT_QCI_thermo and S298=59.11 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 90,
    label = "Ni_4 + C2H3X-2 <=> CX_3 + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.76652e+17,'m^2/(mol*s)'), n=0, Ea=(2.33801,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NTA1""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ni
Original entry: X + CH3CX <=> CX + CH3X
equation : CH3C* + * -> CH3* + C*,
dft_code : Quantum ESPRESSO 5.1,
dftFunctional : BEEF-vdW,
pubId: HansenFirst2018,
reactionEnergy: 1.3264034537714906 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2]C from Thermo library: DFT_QCI_thermo + radical(Cs_P) and S298=60.52 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 91,
    label = "Ni_4 + C2H2X2-3 <=> C2HX2-2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.64307e+16,'m^2/(mol*s)'), n=0, Ea=(1.3239,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NTEy""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ni
Original entry: X + CHCHX <=> HX + CHCX
equation : CHCH* + * -> CHC* + H*,
dft_code : Quantum ESPRESSO 5.1,
dftFunctional : BEEF-vdW,
pubId: HansenFirst2018,
reactionEnergy: 0.460808478994295 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C#C from Thermo library: DFT_QCI_thermo and S298=47.73 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 92,
    label = "Ni_4 + CH2X_1 <=> CHX_3 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(3.75303e+16,'m^2/(mol*s)'), n=0, Ea=(0.34,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODMy""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ni
Original entry: CH2X + X <=> HX + CHX
equation : CH2* -> CH* + H*,
dft_code : DACAPO,
dftFunctional : RPBE,
pubId: WangUniversal2011,
reactionEnergy: -0.351 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2] from Thermo library: primaryThermoLibrary and S298=46.64 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 93,
    label = "Ni_4 + NH2_X <=> NHX_1 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(3.29883e+16,'m^2/(mol*s)'), n=0, Ea=(0.84,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTEyNg==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ni
Original entry: NH2X + X <=> HX + NHX
equation : NH2* -> NH* + H*,
dft_code : DACAPO,
dftFunctional : RPBE,
pubId: WangUniversal2011,
reactionEnergy: -0.271 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [NH2] from Thermo library: primaryThermoLibrary and S298=46.52 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 94,
    label = "Ni_4 + NHX_2 <=> NX + HX_5",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(A=(2.13171e+16,'m^2/(mol*s)'), n=0, Ea=(1.5,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTA3Ng==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ni
Original entry: NHX + X <=> HX + NX
equation : NH* -> H* + N*,
dft_code : DACAPO,
dftFunctional : RPBE,
pubId: WangUniversal2011,
reactionEnergy: 0.295 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [NH] from Thermo library: primaryThermoLibrary and S298=43.26 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ni",
    facet = "211",
)

entry(
    index = 95,
    label = "Ni_4 + CHX_1 <=> CX_3 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.54179e+16,'m^2/(mol*s)'), n=0, Ea=(1.39,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODEz""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ni
Original entry: CHX + X <=> CX + HX
equation : CH* -> C* + H*,
dft_code : DACAPO,
dftFunctional : RPBE,
pubId: WangUniversal2011,
reactionEnergy: 0.593 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH] from Thermo library: DFT_QCI_thermo and S298=43.64 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 96,
    label = "Ni_4 + HOX_1 <=> OX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.13337e+16,'m^2/(mol*s)'), n=0, Ea=(1.174,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTAxNw==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ni
Original entry: OHX + X <=> HX + OX
equation : OH* -> H* + O*,
dft_code : DACAPO,
dftFunctional : RPBE,
pubId: WangUniversal2011,
reactionEnergy: 0.251 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [OH] from Thermo library: primaryThermoLibrary and S298=43.96 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ni",
    facet = "211",
)

entry(
    index = 97,
    label = "Ni_4 + CH3X_1 <=> CH2X_3 + HX_5",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(3.43628e+16,'m^2/(mol*s)'), n=0, Ea=(1.02,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODc4""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ni
Original entry: CH3X + X <=> HX + CH2X
equation : CH3* -> CH2* + H*,
dft_code : DACAPO,
dftFunctional : RPBE,
pubId: WangUniversal2011,
reactionEnergy: 0.325 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH3] from Thermo library: DFT_QCI_thermo and S298=46.44 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ni",
    facet = "211",
)

entry(
    index = 98,
    label = "Ni_4 + C3H7X-2 <=> C3H6X-2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(4.51174e+17,'m^2/(mol*s)'), n=0, Ea=(0.624285,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNTc2""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ir
Original entry: X + CH3CH2CH2X <=> HX + CH3CH2CHX
equation : CH3CH2CH2* + * -> CH3CH2CH* + H*
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangTheory-aided2020
reactionEnergy: 0.19950162136228755 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2]CC from Thermo library: DFT_QCI_thermo and S298=69.30 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 99,
    label = "Ni_4 + C3H7X <=> C3H6X + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.24607e+17,'m^2/(mol*s)'), n=0, Ea=(0.717608,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNTc5""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ir
Original entry: X + CH3CHCH3X <=> HX + CH3CCH3X
equation : CH3CHCH3* + * -> CH3CCH3* + H*
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangTheory-aided2020
reactionEnergy: 0.2957824363547843 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C[CH]C from Thermo library: DFT_QCI_thermo and S298=68.90 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 100,
    label = "Ni_4 + C3H6X2 <=> C3H5X2 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.9542e+17,'m^2/(mol*s)'), n=0, Ea=(0.503287,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNjgw""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ir
Original entry: X + CH3CHCH2X <=> HX + CH3CCH2X
equation : CH3CHCH2* + * -> CH3CCH2* + H*
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangTheory-aided2020
reactionEnergy: 0.07162934209918603 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C=CC from Thermo library: DFT_QCI_thermo and S298=63.63 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 101,
    label = "Ni_4 + C3H6X-3 <=> C3H5X + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.832e+17,'m^2/(mol*s)'), n=0, Ea=(0.0287883,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNjgx""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ir
Original entry: X + CH3CH2CHX <=> HX + CH3CH2CX
equation : CH3CH2CH* + * -> CH3CH2C* + H*
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangTheory-aided2020
reactionEnergy: -0.5600406206503976 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]CC from Thermo library: DFT_QCI_thermo + radical(CCJ2_triplet) and S298=69.63 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 102,
    label = "Ni_4 + C3H5X2-2 <=> C3H4X2 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.40678e+17,'m^2/(mol*s)'), n=0, Ea=(0.458037,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNjg1""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ir
Original entry: X + CH3CHCHX <=> HX + CH3CCHX
equation : CH3CHCH* + * -> CH3CCH* + H*
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangTheory-aided2020
reactionEnergy: -0.19801220629597083 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]=CC from Thermo library: DFT_QCI_thermo and S298=64.88 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 103,
    label = "Ni_4 + C3H5X2-3 <=> C3H4X2-2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.60805e+17,'m^2/(mol*s)'), n=0, Ea=(0.481415,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNjg2""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ir
Original entry: X + CH3CCH2X <=> HX + CH3CCHX
equation : CH3CCH2* + * -> CH3CCH* + H*
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangTheory-aided2020
reactionEnergy: -0.1385119303886313 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C=[C]C from Thermo library: DFT_QCI_thermo and S298=65.41 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 104,
    label = "HX_5 + NX <=> NHX_2 + Ni_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.46209e+16,'m^2/(mol*s)'), n=0, Ea=(1.75397,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyOTcw""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ir
Original entry: HX + NX <=> X + NHX
equation : H* + N* - 0* -> NH* + *
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangAchieving2021
reactionEnergy: 0.05891428131144494 eV

A factor estimation:
A factor estimate for association
A factor estimated from gas-phase smiles [NH] from Thermo library: primaryThermoLibrary and S298=43.26 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ir",
    facet = "211",
)

entry(
    index = 105,
    label = "HX_5 + NHX_1 <=> NH2_X + Ni_4",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(A=(6.14127e+16,'m^2/(mol*s)'), n=0, Ea=(1.3199,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyOTcx""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ir
Original entry: HX + NHX <=> X + NH2X
equation : NH* + H* - 0* -> NH2* + *
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangAchieving2021
reactionEnergy: -0.18279805741622113 eV

A factor estimation:
A factor estimate for association
A factor estimated from gas-phase smiles [NH2] from Thermo library: primaryThermoLibrary and S298=46.52 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ir",
    facet = "211",
)

entry(
    index = 106,
    label = "Ni_4 + HOX_1 <=> OX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.13337e+16,'m^2/(mol*s)'), n=0, Ea=(0.95,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTAwNw==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ir
Original entry: OHX + X <=> HX + OX
equation : OH* -> H* + O*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: -0.39 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [OH] from Thermo library: primaryThermoLibrary and S298=43.96 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ir",
    facet = "211",
)

entry(
    index = 107,
    label = "Ni_4 + NH2_X <=> NHX_1 + HX_5",
    degeneracy = 2.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(A=(3.29883e+16,'m^2/(mol*s)'), n=0, Ea=(2.09,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTE0Mw==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ir
Original entry: NH2X + X <=> HX + NHX
equation : NH2* -> NH* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 0.296 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [NH2] from Thermo library: primaryThermoLibrary and S298=46.52 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ir",
    facet = "211",
)

entry(
    index = 108,
    label = "Ni_4 + CH2X_1 <=> CHX_3 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(3.75303e+16,'m^2/(mol*s)'), n=0, Ea=(0.110985,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI3MzY=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ir
Original entry: X + CH2X <=> HX + CHX
equation : CH2* + * -> CH* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: -0.39909469038 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2] from Thermo library: primaryThermoLibrary and S298=46.64 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 109,
    label = "Ni_4 + CH3X_1 <=> CH2X_3 + HX_5",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(3.43628e+16,'m^2/(mol*s)'), n=0, Ea=(0.615902,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI3NTQ=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ir
Original entry: X + CH3X <=> HX + CH2X
equation : CH3* + * -> CH2* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: 0.309427870423 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH3] from Thermo library: DFT_QCI_thermo and S298=46.44 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 110,
    label = "Ni_4 + C2H2OX2 <=> C2HOX2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(7.90722e+16,'m^2/(mol*s)'), n=0, Ea=(0.538456,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI3NjA=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ir
Original entry: X + CH2COX <=> HX + CHCOX
equation : CH2CO* + * -> CHCO* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: 0.0238096217799 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C=C=O from Thermo library: DFT_QCI_thermo and S298=57.63 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 111,
    label = "Ni_4 + CH2OX <=> CHX_3 + HOX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.16208e+17,'m^2/(mol*s)'), n=0, Ea=(0.534351,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI4MjY=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ir
Original entry: X + CHOHX <=> CHX + OHX
equation : CHOH* + * -> CH* + OH*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: -0.25799263829 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]O from Thermo library: DFT_QCI_thermo and S298=58.32 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 112,
    label = "Ni_4 + CXHO_1 <=> OCX_3 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(5.78405e+16,'m^2/(mol*s)'), n=0, Ea=(0.235587,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI4NDQ=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ir
Original entry: X + CHOX <=> HX + COX
equation : CHO* + * -> CO* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: -1.13453182805 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]=O from Thermo library: DFT_QCI_thermo and S298=53.51 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 113,
    label = "Ni_4 + C2H4X2 <=> C2H3X2 + HX_5",
    degeneracy = 4.0,
    kinetics = SurfaceArrhenius(A=(4.91881e+16,'m^2/(mol*s)'), n=0, Ea=(0.528871,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NDA3""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ir
Original entry: X + CH2CH2X <=> HX + CH2CHX
equation : CH2CH2* + * -> CH2CH* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.0663389757683035 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C=C from Thermo library: DFT_QCI_thermo and S298=52.25 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 114,
    label = "Ni_4 + C2H3X2-3 <=> C2H2X2-4 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(8.63145e+16,'m^2/(mol*s)'), n=0, Ea=(1.40576,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NDA4""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ir
Original entry: X + CH2CHX <=> HX + CH2CX
equation : CH2CH* + * -> CH2C* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: -0.3881636049191002 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]=C from Thermo library: DFT_QCI_thermo and S298=55.78 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 115,
    label = "Ni_4 + C2H3X2-2 <=> C2H2X2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(8.63145e+16,'m^2/(mol*s)'), n=0, Ea=(0.989262,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NDEw""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ir
Original entry: X + CH2CHX <=> HX + CHCHX
equation : CH2CH* + * -> CHCH* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: -0.20538786082761362 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]=C from Thermo library: DFT_QCI_thermo and S298=55.78 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 116,
    label = "Ni_4 + C2H2X2-2 <=> C2HX2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(5.94456e+16,'m^2/(mol*s)'), n=0, Ea=(1.85191,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NDEy""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ir
Original entry: X + CH2CX <=> HX + CHCX
equation : CH2C* + * -> CHC* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.8588864159537479 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [C]=C from Thermo library: DFT_QCI_thermo and S298=53.10 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 117,
    label = "Ni_4 + C2H5X <=> C2H4X + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(1.34702e+17,'m^2/(mol*s)'), n=0, Ea=(0.598188,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NDE1""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ir
Original entry: X + CH3CH2X <=> HX + CH3CHX
equation : CH3CH2* + * -> CH3CH* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.07499675409053452 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C[CH2] from Thermo library: DFT_QCI_thermo and S298=59.12 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 118,
    label = "Ni_4 + C2H5X-2 <=> CH2X_3 + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.34702e+17,'m^2/(mol*s)'), n=0, Ea=(2.24015,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NDE2""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ir
Original entry: X + CH3CH2X <=> CH2X + CH3X
equation : CH3CH2* + * -> CH2* + CH3*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.3020252171845641 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C[CH2] from Thermo library: DFT_QCI_thermo and S298=59.12 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 119,
    label = "Ni_4 + C2H4X-2 <=> C2H3X + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.38494e+17,'m^2/(mol*s)'), n=0, Ea=(0.0948204,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NDE5""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ir
Original entry: X + CH3CHX <=> HX + CH3CX
equation : CH3CH* + * -> CH3C* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: -0.7197727678285446 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]C from Thermo library: DFT_QCI_thermo and S298=59.11 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 120,
    label = "Ni_4 + C2H4X-3 <=> CHX_3 + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.38494e+17,'m^2/(mol*s)'), n=0, Ea=(1.08535,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NDIw""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ir
Original entry: X + CH3CHX <=> CHX + CH3X
equation : CH3CH* + * -> CH3* + CH*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: -0.26793254908989184 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]C from Thermo library: DFT_QCI_thermo and S298=59.11 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 121,
    label = "Ni_4 + C2H3X-2 <=> CX_3 + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.76652e+17,'m^2/(mol*s)'), n=0, Ea=(2.22496,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NDIy""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ir
Original entry: X + CH3CX <=> CX + CH3X
equation : CH3C* + * -> CH3* + C*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.9800766050757375 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2]C from Thermo library: DFT_QCI_thermo + radical(Cs_P) and S298=60.52 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 122,
    label = "Ni_4 + C2H2X2-3 <=> C2HX2-2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.64307e+16,'m^2/(mol*s)'), n=0, Ea=(1.81894,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NDI5""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ir
Original entry: X + CHCHX <=> HX + CHCX
equation : CHCH* + * -> CHC* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.6761106718913652 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C#C from Thermo library: DFT_QCI_thermo and S298=47.73 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 123,
    label = "Ni_4 + C2HX2-3 <=> C2X2 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(9.32934e+16,'m^2/(mol*s)'), n=0, Ea=(1.65809,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NDMw""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ir
Original entry: X + CHCX <=> HX + CCX
equation : CHC* + * -> CC* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.8992872954113409 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]=C from Thermo library: DFT_QCI_thermo + radical(Cds_P) and S298=55.86 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 124,
    label = "HX_5 + NX <=> NHX_2 + Ni_4",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(A=(1.46209e+16,'m^2/(mol*s)'), n=0, Ea=(1.08432,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMzMDE4""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: HX + NX <=> X + NHX
equation : H* + N* - 0* -> NH* + *
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangAchieving2021
reactionEnergy: -1.1145626170327887 eV

A factor estimation:
A factor estimate for association
A factor estimated from gas-phase smiles [NH] from Thermo library: primaryThermoLibrary and S298=43.26 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Cu",
    facet = "211",
)

entry(
    index = 125,
    label = "HX_5 + NHX_1 <=> NH2_X + Ni_4",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(A=(6.14127e+16,'m^2/(mol*s)'), n=0, Ea=(1.31048,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMzMDE5""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: HX + NHX <=> X + NH2X
equation : NH* + H* - 0* -> NH2* + *
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangAchieving2021
reactionEnergy: -1.0981904790969566 eV

A factor estimation:
A factor estimate for association
A factor estimated from gas-phase smiles [NH2] from Thermo library: primaryThermoLibrary and S298=46.52 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Cu",
    facet = "211",
)

entry(
    index = 126,
    label = "Ni_4 + CHX_1 <=> CX_3 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.54179e+16,'m^2/(mol*s)'), n=0, Ea=(2.21,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODE4""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: CHX + X <=> CX + HX
equation : CH* -> C* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 1.426 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH] from Thermo library: DFT_QCI_thermo and S298=43.64 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 127,
    label = "Ni_4 + C2H4X-3 <=> CHX_3 + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.38494e+17,'m^2/(mol*s)'), n=0, Ea=(1.59,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246OTQ2""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: CHCH3X + X <=> CHX + CH3X
equation : CHCH3* -> CH3* + CH*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 0.694 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]C from Thermo library: DFT_QCI_thermo and S298=59.11 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Cu",
    facet = "211",
)

entry(
    index = 128,
    label = "Ni_4 + C2H3X-2 <=> CX_3 + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.76652e+17,'m^2/(mol*s)'), n=0, Ea=(1.59,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246OTQ3""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: CCH3X + X <=> CX + CH3X
equation : CCH3* -> CH3* + C*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 0.762 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2]C from Thermo library: DFT_QCI_thermo + radical(Cs_P) and S298=60.52 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Cu",
    facet = "211",
)

entry(
    index = 129,
    label = "Ni_4 + CH2OX-2 <=> CHOX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.16208e+17,'m^2/(mol*s)'), n=0, Ea=(1.362,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246OTk2""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: HCOHX + X <=> HX + COHX
equation : HCOH* -> COH* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: BehrensThe2012
reactionEnergy: 0.6293 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]O from Thermo library: DFT_QCI_thermo and S298=58.32 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Cu",
    facet = "211",
)

entry(
    index = 130,
    label = "Ni_4 + HOX_1 <=> OX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.13337e+16,'m^2/(mol*s)'), n=0, Ea=(1.729,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTAyMg==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: OHX + X <=> HX + OX
equation : OH* -> H* + O*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 0.679 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [OH] from Thermo library: primaryThermoLibrary and S298=43.96 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 131,
    label = "Ni_4 + CH2OX2 <=> CHOX2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(4.58249e+16,'m^2/(mol*s)'), n=0, Ea=(0.84854,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTA0Mg==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: OCH2X + X <=> HX + OCHX
equation : H2CO* -> HCO* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: BehrensThe2012
reactionEnergy: 0.27833 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C=O from Thermo library: DFT_QCI_thermo and S298=52.16 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Cu",
    facet = "211",
)

entry(
    index = 132,
    label = "Ni_4 + CH2OH* <=> HCOH* + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(1.1079e+17,'m^2/(mol*s)'), n=0, Ea=(0.916,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTA0NQ==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: H3COX + X <=> HX + HCOHX
equation : H2COH* -> HCOH* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: BehrensThe2012
reactionEnergy: 0.49568 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2]O from Thermo library: DFT_QCI_thermo and S298=58.19 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Cu",
    facet = "211",
)

entry(
    index = 133,
    label = "Ni_4 + NHX_2 <=> NX + HX_5",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(A=(2.13171e+16,'m^2/(mol*s)'), n=0, Ea=(2.47,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTA5MA==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: NHX + X <=> HX + NX
equation : NH* -> H* + N*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 1.081 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [NH] from Thermo library: primaryThermoLibrary and S298=43.26 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Cu",
    facet = "211",
)

entry(
    index = 134,
    label = "Ni_4 + NH2_X <=> NHX_1 + HX_5",
    degeneracy = 2.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(A=(3.29883e+16,'m^2/(mol*s)'), n=0, Ea=(2.46,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTE0Nw==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: NH2X + X <=> HX + NHX
equation : NH2* -> NH* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 1.151 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [NH2] from Thermo library: primaryThermoLibrary and S298=46.52 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Cu",
    facet = "211",
)

entry(
    index = 135,
    label = "Ni_4 + CH4NX <=> CH2X_3 + H2NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.21807e+17,'m^2/(mol*s)'), n=0, Ea=(1.25,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTE3OA==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: CH2NH2X + X <=> CH2X + NH2X
equation : CH2NH2* -> CH2* + NH2*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 0.382 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2]N from Thermo library: thermo_DFT_CCSDTF12_BAC and S298=58.64 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Cu",
    facet = "211",
)

entry(
    index = 136,
    label = "Ni_4 + CH2NX <=> CX_3 + H2NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.96407e+15,'m^2/(mol*s)'), n=0, Ea=(1.9,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTE5MA==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: CNH2X + X <=> CX + NH2X
equation : CNH2* -> NH2* + C*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 0.255 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [C-]=[NH2+] from Thermo group additivity estimation: missing(N5dc-C2dcHH) + group(CsJ2_singlet-CsH) + radical(Cs_P) and S298=30.92 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Cu",
    facet = "211",
)

entry(
    index = 137,
    label = "Ni_4 + CH3NX <=> CHX_3 + H2NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.05083e+17,'m^2/(mol*s)'), n=0, Ea=(1.98,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTE5NA==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: CHNH2X + X <=> CHX + NH2X
equation : CHNH2* -> NH2* + CH*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 0.147 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]N from Thermo library: BurcatNS and S298=57.47 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Cu",
    facet = "211",
)

entry(
    index = 138,
    label = "Ni_4 + CH3OX <=> OX + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.27272e+16,'m^2/(mol*s)'), n=0, Ea=(1.802,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTMxMg==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: OCH3X + X <=> OX + CH3X
equation : OCH3* -> CH3* + O*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 0.582 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C[O] from Thermo library: DFT_QCI_thermo and S298=54.42 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Cu",
    facet = "211",
)

entry(
    index = 139,
    label = "CH2OX2-2 + OCX_3 <=> C2H2O2X2 + Ni_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.93935e+20,'m^2/(mol*s)'), n=0, Ea=(0.355,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MjM1Ng==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: COX + OCH2X <=> OCCH2OX + X
equation : CH2O* + CO* -> OCCH2O*
dft_code : DACAPO
dftFunctional : RPBE
pubId: MontoyaInsights2013
reactionEnergy: 0.13 eV

A factor estimation:
A factor estimate for association
A factor estimated from gas-phase smiles [O]C[C]=O from Thermo library: DFT_QCI_thermo + radical(C=OCOJ) + radical(CsCJ=O) and S298=70.49 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Cu",
    facet = "211",
)

entry(
    index = 140,
    label = "HCO* + OCX_3 <=> C2HO2X + Ni_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.2434e+18,'m^2/(mol*s)'), n=0, Ea=(0.675,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MjM1OQ==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: COX + CHOX <=> OCCHOX + X
equation : CHO* + CO* -> OCCHO*
dft_code : DACAPO
dftFunctional : RPBE
pubId: MontoyaInsights2013
reactionEnergy: 0.115 eV

A factor estimation:
A factor estimate for association
A factor estimated from gas-phase smiles O=[C]C=O from Thermo library: DFT_QCI_thermo and S298=67.19 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Cu",
    facet = "211",
)

entry(
    index = 141,
    label = "Ni_4 + HOCXO_1 <=> OCX_3 + HOX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.09952e+17,'m^2/(mol*s)'), n=0, Ea=(0.47,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MjM5NA==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: COOHX + X <=> COX + OHX
equation : COOH* -> CO* + OH*
dft_code : DACAPO
dftFunctional : RPBE
pubId: YooTheoretical2014
reactionEnergy: -0.04 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles O=[C]O from Thermo library: DFT_QCI_thermo and S298=60.19 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 142,
    label = "Ni_4 + CH2OH* <=> HCOH* + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(1.1079e+17,'m^2/(mol*s)'), n=0, Ea=(1.25609,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI2OTA=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: X + H3COX <=> HX + HCOHX
equation : CH2OH* + * -> CHOH* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: 0.794752854956 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2]O from Thermo library: DFT_QCI_thermo and S298=58.19 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 143,
    label = "Ni_4 + C2H2OX2 <=> C2HOX2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(7.90722e+16,'m^2/(mol*s)'), n=0, Ea=(0.817666,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI3NjQ=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: X + CH2COX <=> HX + CHCOX
equation : CH2CO* + * -> CHCO* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: -0.147889523942 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C=C=O from Thermo library: DFT_QCI_thermo and S298=57.63 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 144,
    label = "Ni_4 + C2H3OX <=> OCX_3 + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.94915e+17,'m^2/(mol*s)'), n=0, Ea=(1.3472,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI4MjQ=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: X + CH3COX <=> COX + CH3X
equation : CH3CO* + * -> CH3* + CO*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: 0.456081929442 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C[C]=O from Thermo library: DFT_QCI_thermo and S298=63.74 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 145,
    label = "Ni_4 + CH2OX <=> CHX_3 + HOX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.16208e+17,'m^2/(mol*s)'), n=0, Ea=(1.1699,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI4MzA=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: X + HCOHX <=> CHX + OHX
equation : CHOH* + * -> CH* + OH*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: 0.3749426133 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]O from Thermo library: DFT_QCI_thermo and S298=58.32 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 146,
    label = "Ni_4 + CXHO_1 <=> OCX_3 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(5.78405e+16,'m^2/(mol*s)'), n=0, Ea=(0.291921,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI4NDg=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: X + CHOX <=> HX + COX
equation : CHO* + * -> CO* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: -0.586327319179 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]=O from Thermo library: DFT_QCI_thermo and S298=53.51 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 147,
    label = "Ni_4 + C2H4X2 <=> C2H3X2 + HX_5",
    degeneracy = 4.0,
    kinetics = SurfaceArrhenius(A=(4.91881e+16,'m^2/(mol*s)'), n=0, Ea=(1.82807,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4Mjk4""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: X + CH2CH2X <=> HX + CHCH2X
equation : CH2CH2* + * -> CH2CH* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.8961016586399637 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C=C from Thermo library: DFT_QCI_thermo and S298=52.25 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 148,
    label = "Ni_4 + C2H3X2-3 <=> C2H2X2-4 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(8.63145e+16,'m^2/(mol*s)'), n=0, Ea=(1.66138,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4Mjk5""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: X + CHCH2X <=> HX + CCH2X
equation : CH2CH* + * -> CH2C* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.46204605273669586 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]=C from Thermo library: DFT_QCI_thermo and S298=55.78 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 149,
    label = "Ni_4 + C2H5X <=> C2H4X + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(1.34702e+17,'m^2/(mol*s)'), n=0, Ea=(1.4683,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MzA2""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: X + CH2CH3X <=> HX + CHCH3X
equation : CH3CH2* + * -> CH3CH* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.8888453345280141 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C[CH2] from Thermo library: DFT_QCI_thermo and S298=59.12 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 150,
    label = "Ni_4 + C2H5X-2 <=> CH2X_3 + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.34702e+17,'m^2/(mol*s)'), n=0, Ea=(1.84405,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MzA3""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: X + CH2CH3X <=> CH2X + CH3X
equation : CH3CH2* + * -> CH2* + CH3*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 1.3445733119151555 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C[CH2] from Thermo library: DFT_QCI_thermo and S298=59.12 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 151,
    label = "Ni_4 + C2H4X-2 <=> C2H3X + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.38494e+17,'m^2/(mol*s)'), n=0, Ea=(0.949978,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MzEw""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: X + CHCH3X <=> HX + CCH3X
equation : CH3CH* + * -> CH3C* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.25942545384168625 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]C from Thermo library: DFT_QCI_thermo and S298=59.11 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 152,
    label = "Ni_4 + C2H4X-3 <=> CHX_3 + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.38494e+17,'m^2/(mol*s)'), n=0, Ea=(1.47684,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MzEx""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: X + CHCH3X <=> CHX + CH3X
equation : CH3CH* + * -> CH3* + CH*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.9512028765748255 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]C from Thermo library: DFT_QCI_thermo and S298=59.11 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 153,
    label = "Ni_4 + C2H3X-2 <=> CX_3 + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.76652e+17,'m^2/(mol*s)'), n=0, Ea=(2.44767,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MzEz""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: X + CCH3X <=> CX + CH3X
equation : CH3C* + * -> CH3* + C*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 1.8727308532688767 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2]C from Thermo library: DFT_QCI_thermo + radical(Cs_P) and S298=60.52 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 154,
    label = "Ni_4 + C2H2X2-3 <=> C2HX2-2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.64307e+16,'m^2/(mol*s)'), n=0, Ea=(1.81452,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MzIw""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: X + CHCHX <=> HX + CCHX
equation : CHCH* + * -> CHC* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.6426848868140951 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C#C from Thermo library: DFT_QCI_thermo and S298=47.73 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 155,
    label = "Ni_4 + C2HX2-3 <=> C2X2 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(9.32934e+16,'m^2/(mol*s)'), n=0, Ea=(1.61752,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MzIx""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: X + CCHX <=> HX + CCX
equation : CHC* + * -> CC* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.6985681600053795 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]=C from Thermo library: DFT_QCI_thermo + radical(Cds_P) and S298=55.86 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 156,
    label = "HX_5 + NX <=> NHX_2 + Ni_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.46209e+16,'m^2/(mol*s)'), n=0, Ea=(0.921125,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMzMDc4""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Co
Original entry: HX + NX <=> X + NHX
equation : H* + N* - 0* -> NH* + *
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangAchieving2021
reactionEnergy: -0.4187509703915566 eV

A factor estimation:
A factor estimate for association
A factor estimated from gas-phase smiles [NH] from Thermo library: primaryThermoLibrary and S298=43.26 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Co",
    facet = "211",
)

entry(
    index = 157,
    label = "HX_5 + NHX_1 <=> NH2_X + Ni_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.14127e+16,'m^2/(mol*s)'), n=0, Ea=(1.23393,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMzMDc5""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Co
Original entry: HX + NHX <=> X + NH2X
equation : NH* + H* - 0* -> NH2* + *
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangAchieving2021
reactionEnergy: -0.27656216360628605 eV

A factor estimation:
A factor estimate for association
A factor estimated from gas-phase smiles [NH2] from Thermo library: primaryThermoLibrary and S298=46.52 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Co",
    facet = "211",
)

entry(
    index = 158,
    label = "Ni_4 + C2H4X2 <=> C2H3X2 + HX_5",
    degeneracy = 4.0,
    kinetics = SurfaceArrhenius(A=(4.91881e+16,'m^2/(mol*s)'), n=0, Ea=(0.774714,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MjQ0""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Co
Original entry: X + CH2CH2X <=> HX + CH2CHX
equation : CH2CH2* + * -> CH2CH* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.8032294734730385 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C=C from Thermo library: DFT_QCI_thermo and S298=52.25 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Co",
    facet = "111",
)

entry(
    index = 159,
    label = "Ni_4 + C2H2X2-2 <=> C2HX2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(5.94456e+16,'m^2/(mol*s)'), n=0, Ea=(0.97601,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MjQ5""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Co
Original entry: X + CH2CX <=> HX + CHCX
equation : CH2C* + * -> CHC* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.06677680695429444 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [C]=C from Thermo library: DFT_QCI_thermo and S298=53.10 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Co",
    facet = "111",
)

entry(
    index = 160,
    label = "Ni_4 + C2H4X-2 <=> C2H3X + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.38494e+17,'m^2/(mol*s)'), n=0, Ea=(0.301346,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MjU2""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Co
Original entry: X + CH3CHX <=> HX + CH3CX
equation : CH3CH* + * -> CH3C* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: -0.38336460501886904 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]C from Thermo library: DFT_QCI_thermo and S298=59.11 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Co",
    facet = "111",
)

entry(
    index = 161,
    label = "Ni_4 + C2H2X2-3 <=> C2HX2-2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.64307e+16,'m^2/(mol*s)'), n=0, Ea=(1.28321,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MjY2""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Co
Original entry: X + CHCHX <=> HX + CHCX
equation : CHCH* + * -> CHC* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.4539271958929021 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C#C from Thermo library: DFT_QCI_thermo and S298=47.73 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Co",
    facet = "111",
)

entry(
    index = 162,
    label = "Ni_4 + C3H7X-2 <=> C3H6X-2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(4.51174e+17,'m^2/(mol*s)'), n=0, Ea=(0.361299,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNTY2""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ru
Original entry: X + CH3CH2CH2X <=> HX + CH3CH2CHX
equation : CH3CH2CH2* + * -> CH3CH2CH* + H*
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangTheory-aided2020
reactionEnergy: -0.58390704516205 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2]CC from Thermo library: DFT_QCI_thermo and S298=69.30 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ru",
    facet = "111",
)

entry(
    index = 163,
    label = "Ni_4 + C3H7X <=> C3H6X + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.24607e+17,'m^2/(mol*s)'), n=0, Ea=(0.409265,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNTY5""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ru
Original entry: X + CH3CHCH3X <=> HX + CH3CCH3X
equation : CH3CHCH3* + * -> CH3CCH3* + H*
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangTheory-aided2020
reactionEnergy: -0.22707831807201728 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C[CH]C from Thermo library: DFT_QCI_thermo and S298=68.90 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ru",
    facet = "111",
)

entry(
    index = 164,
    label = "Ni_4 + C3H6X2 <=> C3H5X2 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.9542e+17,'m^2/(mol*s)'), n=0, Ea=(0.832106,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNjU4""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ru
Original entry: X + CH3CHCH2X <=> HX + CH3CCH2X
equation : CH3CHCH2* + * -> CH3CCH2* + H*
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangTheory-aided2020
reactionEnergy: -0.16400872496888041 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C=CC from Thermo library: DFT_QCI_thermo and S298=63.63 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ru",
    facet = "111",
)

entry(
    index = 165,
    label = "Ni_4 + C3H6X-3 <=> C3H5X + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.832e+17,'m^2/(mol*s)'), n=0, Ea=(0.301372,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNjU5""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ru
Original entry: X + CH3CH2CHX <=> HX + CH3CH2CX
equation : CH3CH2CH* + * -> CH3CH2C* + H*
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangTheory-aided2020
reactionEnergy: -0.78489073459059 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]CC from Thermo library: DFT_QCI_thermo + radical(CCJ2_triplet) and S298=69.63 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ru",
    facet = "111",
)

entry(
    index = 166,
    label = "Ni_4 + C3H5X2-2 <=> C3H4X2 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.40678e+17,'m^2/(mol*s)'), n=0, Ea=(0.502499,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNjYz""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ru
Original entry: X + CH3CHCHX <=> HX + CH3CCHX
equation : CH3CHCH* + * -> CH3CCH* + H*
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangTheory-aided2020
reactionEnergy: -0.5163428117230069 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]=CC from Thermo library: DFT_QCI_thermo and S298=64.88 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ru",
    facet = "111",
)

entry(
    index = 167,
    label = "Ni_4 + C3H5X2-3 <=> C3H4X2-2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.60805e+17,'m^2/(mol*s)'), n=0, Ea=(0.35563,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNjY0""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ru
Original entry: X + CH3CCH2X <=> HX + CH3CCHX
equation : CH3CCH2* + * -> CH3CCH* + H*
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangTheory-aided2020
reactionEnergy: -0.6554065889795311 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C=[C]C from Thermo library: DFT_QCI_thermo and S298=65.41 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ru",
    facet = "111",
)

entry(
    index = 168,
    label = "HX_5 + NX <=> NHX_2 + Ni_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.46209e+16,'m^2/(mol*s)'), n=0, Ea=(1.63202,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMzMDA2""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ru
Original entry: HX + NX <=> X + NHX
equation : H* + N* - 0* -> NH* + *
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangAchieving2021
reactionEnergy: 0.2800821603741497 eV

A factor estimation:
A factor estimate for association
A factor estimated from gas-phase smiles [NH] from Thermo library: primaryThermoLibrary and S298=43.26 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ru",
    facet = "211",
)

entry(
    index = 169,
    label = "HX_5 + NHX_1 <=> NH2_X + Ni_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.14127e+16,'m^2/(mol*s)'), n=0, Ea=(1.55264,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMzMDA3""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ru
Original entry: HX + NHX <=> X + NH2X
equation : NH* + H* - 0* -> NH2* + *
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangAchieving2021
reactionEnergy: 0.09356947685591877 eV

A factor estimation:
A factor estimate for association
A factor estimated from gas-phase smiles [NH2] from Thermo library: primaryThermoLibrary and S298=46.52 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ru",
    facet = "211",
)

entry(
    index = 170,
    label = "Ni_4 + C2H4X2 <=> C2H3X2 + HX_5",
    degeneracy = 4.0,
    kinetics = SurfaceArrhenius(A=(4.91881e+16,'m^2/(mol*s)'), n=0, Ea=(0.487823,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4ODUy""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ru
Original entry: X + CH2CH2X <=> HX + CH2CHX
equation : CH2CH2* + * -> CH2CH* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: -0.14671644114423543 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C=C from Thermo library: DFT_QCI_thermo and S298=52.25 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ru",
    facet = "001",
)

entry(
    index = 171,
    label = "Ni_4 + C2H4X-2 <=> C2H3X + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.38494e+17,'m^2/(mol*s)'), n=0, Ea=(0.245878,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4ODY0""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ru
Original entry: X + CH3CHX <=> HX + CH3CX
equation : CH3CH* + * -> CH3C* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: -0.45064788387389854 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]C from Thermo library: DFT_QCI_thermo and S298=59.11 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ru",
    facet = "001",
)

entry(
    index = 172,
    label = "Ni_4 + C2HX2-3 <=> C2X2 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(9.32934e+16,'m^2/(mol*s)'), n=0, Ea=(1.48519,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4ODc1""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ru
Original entry: X + CHCX <=> HX + CCX
equation : CHC* + * -> CC* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.5423622925300151 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]=C from Thermo library: DFT_QCI_thermo + radical(Cds_P) and S298=55.86 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ru",
    facet = "001",
)

entry(
    index = 173,
    label = "Ni_4 + C2H5X-2 <=> CH2X_3 + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.34702e+17,'m^2/(mol*s)'), n=0, Ea=(1.27,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246OTQx""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ru
Original entry: CH3CH2X + X <=> CH2X + CH3X
equation : CH2CH3* -> CH2* + CH3*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: -0.311 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C[CH2] from Thermo library: DFT_QCI_thermo and S298=59.12 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ru",
    facet = "211",
)

entry(
    index = 174,
    label = "Ni_4 + CHX_1 <=> CX_3 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.54179e+16,'m^2/(mol*s)'), n=0, Ea=(1.03,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODA5""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ru
Original entry: CHX + X <=> CX + HX
equation : CH* -> C* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 0.031 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH] from Thermo library: DFT_QCI_thermo and S298=43.64 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ru",
    facet = "211",
)

entry(
    index = 175,
    label = "Ni_4 + CH2X_1 <=> CHX_3 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(3.75303e+16,'m^2/(mol*s)'), n=0, Ea=(0.38,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODMz""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ru
Original entry: CH2X + X <=> HX + CHX
equation : CH2* -> CH* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: -0.512 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2] from Thermo library: primaryThermoLibrary and S298=46.64 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ru",
    facet = "211",
)

entry(
    index = 176,
    label = "Ni_4 + CH3X_1 <=> CH2X_3 + HX_5",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(3.43628e+16,'m^2/(mol*s)'), n=0, Ea=(0.7,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODcy""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ru
Original entry: CH3X + X <=> HX + CH2X
equation : CH3* -> CH2* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 0.001 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH3] from Thermo library: DFT_QCI_thermo and S298=46.44 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ru",
    facet = "111",
)

entry(
    index = 177,
    label = "Ni_4 + C2H4X-3 <=> CHX_3 + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.38494e+17,'m^2/(mol*s)'), n=0, Ea=(0.97,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246OTMw""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ru
Original entry: CH3CHX + X <=> CHX + CH3X
equation : CHCH3* -> CH3* + CH*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: -0.816 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]C from Thermo library: DFT_QCI_thermo and S298=59.11 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ru",
    facet = "211",
)

entry(
    index = 178,
    label = "Ni_4 + HOX_1 <=> OX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.13337e+16,'m^2/(mol*s)'), n=0, Ea=(1.119,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTAxNA==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ru
Original entry: OHX + X <=> HX + OX
equation : OH* -> H* + O*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: -0.698 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [OH] from Thermo library: primaryThermoLibrary and S298=43.96 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ru",
    facet = "111",
)

entry(
    index = 179,
    label = "Ni_4 + NHX_2 <=> NX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.13171e+16,'m^2/(mol*s)'), n=0, Ea=(1.1,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTA1OQ==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ru
Original entry: NHX + X <=> HX + NX
equation : NH* -> H* + N*
dft_code : DACAPO
dftFunctional : RPBE
pubId: LogadottirAmmonia2003
reactionEnergy: 0.0 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [NH] from Thermo library: primaryThermoLibrary and S298=43.26 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ru",
    facet = "0001step",
)

entry(
    index = 180,
    label = "Ni_4 + C2H3X-2 <=> CX_3 + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.76652e+17,'m^2/(mol*s)'), n=0, Ea=(1.12,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246OTM1""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ru
Original entry: CH3CX + X <=> CX + CH3X
equation : CCH3* -> CH3* + C*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: -0.308 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2]C from Thermo library: DFT_QCI_thermo + radical(Cs_P) and S298=60.52 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ru",
    facet = "211",
)

entry(
    index = 181,
    label = "Ni_4 + NH2_X <=> NHX_1 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(3.29883e+16,'m^2/(mol*s)'), n=0, Ea=(0.43,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTEyMw==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ru
Original entry: NH2X + X <=> HX + NHX
equation : NH2* -> NH* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: LogadottirAmmonia2003
reactionEnergy: -0.87 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [NH2] from Thermo library: primaryThermoLibrary and S298=46.52 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ru",
    facet = "1",
)

entry(
    index = 182,
    label = "Ni_4 + C3H7X-2 <=> C3H6X-2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(4.51174e+17,'m^2/(mol*s)'), n=0, Ea=(0.550722,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNTU0""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: X + CH3CH2CH2X <=> HX + CH3CH2CHX
equation : CH3CH2CH2* + * -> CH3CH2CH* + H*
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangTheory-aided2020
reactionEnergy: 0.026360075717093423 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2]CC from Thermo library: DFT_QCI_thermo and S298=69.30 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 183,
    label = "Ni_4 + C3H7X <=> C3H6X + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.24607e+17,'m^2/(mol*s)'), n=0, Ea=(0.682596,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNjIy""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: X + CH3CHCH3X <=> HX + CH3CCH3X
equation : CH3CHCH3* + * -> CH3CCH3* + H*
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangTheory-aided2020
reactionEnergy: 0.12046479637501761 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C[CH]C from Thermo library: DFT_QCI_thermo and S298=68.90 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 184,
    label = "Ni_4 + C3H6X2 <=> C3H5X2 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.9542e+17,'m^2/(mol*s)'), n=0, Ea=(0.54571,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNjI0""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: X + CH3CHCH2X <=> HX + CH3CCH2X
equation : CH3CHCH2* + * -> CH3CCH2* + H*
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangTheory-aided2020
reactionEnergy: 0.04435387544799596 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C=CC from Thermo library: DFT_QCI_thermo and S298=63.63 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 185,
    label = "Ni_4 + C3H6X-3 <=> C3H5X + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.832e+17,'m^2/(mol*s)'), n=0, Ea=(0.0503398,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNjI1""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: X + CH3CH2CHX <=> HX + CH3CH2CX
equation : CH3CH2CH* + * -> CH3CH2C* + H*
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangTheory-aided2020
reactionEnergy: -0.6454775631427765 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]CC from Thermo library: DFT_QCI_thermo + radical(CCJ2_triplet) and S298=69.63 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 186,
    label = "Ni_4 + C3H5X2-2 <=> C3H4X2 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.40678e+17,'m^2/(mol*s)'), n=0, Ea=(0.368631,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNjI5""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: X + CH3CHCHX <=> HX + CH3CCHX
equation : CH3CHCH* + * -> CH3CCH* + H*
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangTheory-aided2020
reactionEnergy: -0.3678347794339061 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]=CC from Thermo library: DFT_QCI_thermo and S298=64.88 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 187,
    label = "Ni_4 + C3H5X2-3 <=> C3H4X2-2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.60805e+17,'m^2/(mol*s)'), n=0, Ea=(0.332235,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNjMw""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: X + CH3CCH2X <=> HX + CH3CCHX
equation : CH3CCH2* + * -> CH3CCH* + H*
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangTheory-aided2020
reactionEnergy: -0.2876458244572859 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C=[C]C from Thermo library: DFT_QCI_thermo and S298=65.41 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 188,
    label = "HX_5 + NX <=> NHX_2 + Ni_4",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(A=(1.46209e+16,'m^2/(mol*s)'), n=0, Ea=(1.46328,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMzMTAy""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: HX + NX <=> X + NHX
equation : H* + N* - 0* -> NH* + *
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangAchieving2021
reactionEnergy: 0.08934354869415984 eV

A factor estimation:
A factor estimate for association
A factor estimated from gas-phase smiles [NH] from Thermo library: primaryThermoLibrary and S298=43.26 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 189,
    label = "HX_5 + NHX_1 <=> NH2_X + Ni_4",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(A=(6.14127e+16,'m^2/(mol*s)'), n=0, Ea=(1.17609,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMzMTAz""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: HX + NHX <=> X + NH2X
equation : NH* + H* - 0* -> NH2* + *
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangAchieving2021
reactionEnergy: -0.28173117034020834 eV

A factor estimation:
A factor estimate for association
A factor estimated from gas-phase smiles [NH2] from Thermo library: primaryThermoLibrary and S298=46.52 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 190,
    label = "Ni_4 + HOX_1 <=> OX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.13337e+16,'m^2/(mol*s)'), n=0, Ea=(1.27244,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDA5NQ==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: X + OHX <=> HX + OX
equation : OH* + * -> H* + O*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: YangIntrinsic2016
reactionEnergy: -0.0285929070378 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [OH] from Thermo library: primaryThermoLibrary and S298=43.96 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 191,
    label = "Ni_4 + CHOX-2 <=> CX_3 + HOX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(8.82294e+16,'m^2/(mol*s)'), n=0, Ea=(1.21464,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDExOQ==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: X + COHX <=> CX + OHX
equation : COH* + * -> OH* + C*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: YangIntrinsic2016
reactionEnergy: 0.676739118877 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [C-]=[OH+] from Thermo library: DFT_QCI_thermo + radical(Cs_P) and S298=56.31 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 192,
    label = "Ni_4 + CH2X_1 <=> CHX_3 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(3.75303e+16,'m^2/(mol*s)'), n=0, Ea=(0.78,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODM4""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: CH2X + X <=> HX + CHX
equation : CH2* -> CH* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: -0.242 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2] from Thermo library: primaryThermoLibrary and S298=46.64 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 193,
    label = "Ni_4 + C2H5X-2 <=> CH2X_3 + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.34702e+17,'m^2/(mol*s)'), n=0, Ea=(1.13325,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246OTM4""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: CH2CH3X + X <=> CH2X + CH3X
equation : CH2CH3* -> CH2* + CH3*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: -0.13775 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C[CH2] from Thermo library: DFT_QCI_thermo and S298=59.12 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 194,
    label = "Ni_4 + C2H3X-2 <=> CX_3 + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.76652e+17,'m^2/(mol*s)'), n=0, Ea=(1.15,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246OTM5""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: CCH3X + X <=> CX + CH3X
equation : CCH3* -> CH3* + C*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: -0.138 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2]C from Thermo library: DFT_QCI_thermo + radical(Cs_P) and S298=60.52 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 195,
    label = "Ni_4 + C2H4X-3 <=> CHX_3 + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.38494e+17,'m^2/(mol*s)'), n=0, Ea=(1.57,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246OTQ1""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: CHCH3X + X <=> CHX + CH3X
equation : CHCH3* -> CH3* + CH*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: -0.116 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]C from Thermo library: DFT_QCI_thermo and S298=59.11 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 196,
    label = "Ni_4 + HOX_1 <=> OX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.13337e+16,'m^2/(mol*s)'), n=0, Ea=(1.094,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTAxMw==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: OHX + X <=> HX + OX
equation : OH* -> H* + O*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 0.153 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [OH] from Thermo library: primaryThermoLibrary and S298=43.96 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 197,
    label = "Ni_4 + CH2OX2 <=> CHOX2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(4.58249e+16,'m^2/(mol*s)'), n=0, Ea=(0.41239,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTA0MA==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: OCH2X + X <=> HX + OCHX
equation : H2CO* -> HCO* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: Studt et al submitted
reactionEnergy: -0.04926 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C=O from Thermo library: DFT_QCI_thermo and S298=52.16 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 198,
    label = "Ni_4 + NHX_2 <=> NX + HX_5",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(A=(2.13171e+16,'m^2/(mol*s)'), n=0, Ea=(1.35,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTA2OA==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: NHX + X <=> HX + NX
equation : NH* -> H* + N*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: -0.142 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [NH] from Thermo library: primaryThermoLibrary and S298=43.26 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 199,
    label = "Ni_4 + NH2_X <=> NHX_1 + HX_5",
    degeneracy = 2.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(A=(3.29883e+16,'m^2/(mol*s)'), n=0, Ea=(1.66,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTEzNQ==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: NH2X + X <=> HX + NHX
equation : NH2* -> NH* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 0.288 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [NH2] from Thermo library: primaryThermoLibrary and S298=46.52 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 200,
    label = "Ni_4 + CH4NX <=> CH2X_3 + H2NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.21807e+17,'m^2/(mol*s)'), n=0, Ea=(1.06,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTE3MA==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: CH2NH2X + X <=> CH2X + NH2X
equation : CH2NH2* -> CH2* + NH2*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: -0.458 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2]N from Thermo library: thermo_DFT_CCSDTF12_BAC and S298=58.64 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 201,
    label = "Ni_4 + CH2NX <=> CX_3 + H2NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.96407e+15,'m^2/(mol*s)'), n=0, Ea=(1.2,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTE3Mg==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: CNH2X + X <=> CX + NH2X
equation : CNH2* -> NH2* + C*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: -0.365 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [C-]=[NH2+] from Thermo group additivity estimation: missing(N5dc-C2dcHH) + group(CsJ2_singlet-CsH) + radical(Cs_P) and S298=30.92 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 202,
    label = "Ni_4 + CH3NX <=> CHX_3 + H2NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.05083e+17,'m^2/(mol*s)'), n=0, Ea=(1.45,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTE4Ng==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: CHNH2X + X <=> CHX + NH2X
equation : CHNH2* -> NH2* + CH*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: -0.803 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]N from Thermo library: BurcatNS and S298=57.47 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 203,
    label = "Ni_4 + CH3OX <=> OX + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.27272e+16,'m^2/(mol*s)'), n=0, Ea=(1.302,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTI5Mw==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: OCH3X + X <=> OX + CH3X
equation : OCH3* -> CH3* + O*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: -0.378 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C[O] from Thermo library: DFT_QCI_thermo and S298=54.42 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 204,
    label = "Ni_4 + HOCXO_1 <=> OCX_3 + HOX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.09952e+17,'m^2/(mol*s)'), n=0, Ea=(0.81,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MjM5Ng==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: COOHX + X <=> COX + OHX
equation : COOH* -> CO* + OH*
dft_code : DACAPO
dftFunctional : RPBE
pubId: YooTheoretical2014
reactionEnergy: -0.75 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles O=[C]O from Thermo library: DFT_QCI_thermo and S298=60.19 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 205,
    label = "Ni_4 + CH2OH* <=> HCOH* + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(1.1079e+17,'m^2/(mol*s)'), n=0, Ea=(0.709407,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI2ODg=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: X + H3COX <=> HX + CHOHX
equation : CH2OH* + * -> CHOH* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: -0.0182726491184 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2]O from Thermo library: DFT_QCI_thermo and S298=58.19 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 206,
    label = "Ni_4 + CH2X_1 <=> CHX_3 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(3.75303e+16,'m^2/(mol*s)'), n=0, Ea=(0.166615,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI3Mzg=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: X + CH2X <=> HX + CHX
equation : CH2* + * -> CH* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: -0.462197484158 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2] from Thermo library: primaryThermoLibrary and S298=46.64 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 207,
    label = "Ni_4 + C2H2OX2 <=> C2HOX2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(7.90722e+16,'m^2/(mol*s)'), n=0, Ea=(0.488103,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI3NjI=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: X + CH2COX <=> HX + CHCOX
equation : CH2CO* + * -> CHCO* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: -0.155870691146 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C=C=O from Thermo library: DFT_QCI_thermo and S298=57.63 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 208,
    label = "Ni_4 + C2H3OX <=> OCX_3 + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.94915e+17,'m^2/(mol*s)'), n=0, Ea=(1.20669,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI4MjI=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: X + CH3COX <=> COX + CH3X
equation : CH3CO* + * -> CH3* + CO*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: -0.264534255286 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C[C]=O from Thermo library: DFT_QCI_thermo and S298=63.74 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 209,
    label = "Ni_4 + CH2OX <=> CHX_3 + HOX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.16208e+17,'m^2/(mol*s)'), n=0, Ea=(0.744287,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI4Mjg=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: X + CHOHX <=> CHX + OHX
equation : CHOH* + * -> CH* + OH*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: -0.47260447836 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]O from Thermo library: DFT_QCI_thermo and S298=58.32 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 210,
    label = "Ni_4 + CXHO_1 <=> OCX_3 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(5.78405e+16,'m^2/(mol*s)'), n=0, Ea=(0.350006,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI4NDY=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: X + CHOX <=> HX + COX
equation : CHO* + * -> CO* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: -0.984073141182 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]=O from Thermo library: DFT_QCI_thermo and S298=53.51 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 211,
    label = "Ni_4 + C2H4X2 <=> C2H3X2 + HX_5",
    degeneracy = 4.0,
    kinetics = SurfaceArrhenius(A=(4.91881e+16,'m^2/(mol*s)'), n=0, Ea=(0.738977,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4ODA4""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: X + CH2CH2X <=> HX + CHCH2X
equation : CH2CH2* + * -> CH2CH* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.20771620294544846 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C=C from Thermo library: DFT_QCI_thermo and S298=52.25 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 212,
    label = "Ni_4 + C2H3X2-2 <=> C2H2X2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(8.63145e+16,'m^2/(mol*s)'), n=0, Ea=(0.663536,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4ODEx""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: X + CHCH2X <=> HX + CHCHX
equation : CH2CH* + * -> CHCH* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: -0.3282188284501899 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]=C from Thermo library: DFT_QCI_thermo and S298=55.78 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 213,
    label = "Ni_4 + C2H5X <=> C2H4X + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(1.34702e+17,'m^2/(mol*s)'), n=0, Ea=(0.629995,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4ODE2""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: X + CH2CH3X <=> HX + CHCH3X
equation : CH3CH2* + * -> CH3CH* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.034086953703081235 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C[CH2] from Thermo library: DFT_QCI_thermo and S298=59.12 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 214,
    label = "Ni_4 + C2H5X-2 <=> CH2X_3 + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.34702e+17,'m^2/(mol*s)'), n=0, Ea=(1.90247,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4ODE3""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: X + CH2CH3X <=> CH2X + CH3X
equation : CH3CH2* + * -> CH2* + CH3*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.4621752388193272 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C[CH2] from Thermo library: DFT_QCI_thermo and S298=59.12 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 215,
    label = "Ni_4 + C2H4X-2 <=> C2H3X + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.38494e+17,'m^2/(mol*s)'), n=0, Ea=(0.373539,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4ODIw""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: X + CHCH3X <=> HX + CCH3X
equation : CH3CH* + * -> CH3C* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: -0.6520108407130465 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]C from Thermo library: DFT_QCI_thermo and S298=59.11 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 216,
    label = "Ni_4 + C2H4X-3 <=> CHX_3 + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.38494e+17,'m^2/(mol*s)'), n=0, Ea=(1.37393,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4ODIx""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: X + CHCH3X <=> CHX + CH3X
equation : CH3CH* + * -> CH3* + CH*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: -0.03638359461911023 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]C from Thermo library: DFT_QCI_thermo and S298=59.11 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 217,
    label = "Ni_4 + C2H3X-2 <=> CX_3 + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.76652e+17,'m^2/(mol*s)'), n=0, Ea=(2.60937,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4ODIz""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: X + CCH3X <=> CX + CH3X
equation : CH3C* + * -> CH3* + C*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 1.1658626766584348 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2]C from Thermo library: DFT_QCI_thermo + radical(Cs_P) and S298=60.52 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 218,
    label = "Ni_4 + C2HX2-3 <=> C2X2 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(9.32934e+16,'m^2/(mol*s)'), n=0, Ea=(1.51219,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4ODMx""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: X + CCHX <=> HX + CCX
equation : CHC* + * -> CC* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.6428791760408785 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]=C from Thermo library: DFT_QCI_thermo + radical(Cds_P) and S298=55.86 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 219,
    label = "Ni_4 + C3H7X-2 <=> C3H6X-2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(4.51174e+17,'m^2/(mol*s)'), n=0, Ea=(0.904654,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNTQy""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: X + CH3CH2CH2X <=> HX + CH3CH2CHX
equation : CH3CH2CH2* + * -> CH3CH2CH* + H*,
dft_code : Quantum Espresso,
dftFunctional : BEEF-vdW,
pubId: WangTheory-aided2020,
reactionEnergy: 0.22193808763404377 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2]CC from Thermo library: DFT_QCI_thermo and S298=69.30 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 220,
    label = "Ni_4 + C3H7X <=> C3H6X + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.24607e+17,'m^2/(mol*s)'), n=0, Ea=(1.03353,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNTQ1""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: X + CH3CHCH3X <=> HX + CH3CCH3X
equation : CH3CHCH3* + * -> CH3CCH3* + H*,
dft_code : Quantum Espresso,
dftFunctional : BEEF-vdW,
pubId: WangTheory-aided2020,
reactionEnergy: 0.31443420733558014 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C[CH]C from Thermo library: DFT_QCI_thermo and S298=68.90 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 221,
    label = "Ni_4 + C3H6X2 <=> C3H5X2 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.9542e+17,'m^2/(mol*s)'), n=0, Ea=(0.87615,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNTg5""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: X + CH3CHCH2X <=> HX + CH3CCH2X
equation : CH3CHCH2* + * -> CH3CCH2* + H*,
dft_code : Quantum Espresso,
dftFunctional : BEEF-vdW,
pubId: WangTheory-aided2020,
reactionEnergy: 0.16410069941775873 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C=CC from Thermo library: DFT_QCI_thermo and S298=63.63 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 222,
    label = "Ni_4 + C3H6X-3 <=> C3H5X + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.832e+17,'m^2/(mol*s)'), n=0, Ea=(0.384566,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNTkw""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: X + CH3CH2CHX <=> HX + CH3CH2CX
equation : CH3CH2CH* + * -> CH3CH2C* + H*,
dft_code : Quantum Espresso,
dftFunctional : BEEF-vdW,
pubId: WangTheory-aided2020,
reactionEnergy: -0.6691781342378817 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]CC from Thermo library: DFT_QCI_thermo + radical(CCJ2_triplet) and S298=69.63 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 223,
    label = "Ni_4 + C3H5X2-2 <=> C3H4X2 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.40678e+17,'m^2/(mol*s)'), n=0, Ea=(0.846223,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNTk0""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: X + CH3CHCHX <=> HX + CH3CCHX
equation : CH3CHCH* + * -> CH3CCH* + H*,
dft_code : Quantum Espresso,
dftFunctional : BEEF-vdW,
pubId: WangTheory-aided2020,
reactionEnergy: -0.09019417266245 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]=CC from Thermo library: DFT_QCI_thermo and S298=64.88 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 224,
    label = "Ni_4 + C3H5X2-3 <=> C3H4X2-2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.60805e+17,'m^2/(mol*s)'), n=0, Ea=(0.844055,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNTk1""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: X + CH3CCH2X <=> HX + CH3CCHX
equation : CH3CCH2* + * -> CH3CCH* + H*,
dft_code : Quantum Espresso,
dftFunctional : BEEF-vdW,
pubId: WangTheory-aided2020,
reactionEnergy: 0.037358100729761645 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C=[C]C from Thermo library: DFT_QCI_thermo and S298=65.41 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 225,
    label = "HX_5 + NX <=> NHX_2 + Ni_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.46209e+16,'m^2/(mol*s)'), n=0, Ea=(1.22211,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMzMDkw""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: HX + NX <=> X + NHX
equation : H* + N* - 0* -> NH* + *,
dft_code : Quantum Espresso,
dftFunctional : BEEF-vdW,
pubId: WangAchieving2021,
reactionEnergy: -0.16545209198375233 eV
A factor estimation:
A factor estimate for association
A factor estimated from gas-phase smiles [NH] from Thermo library: primaryThermoLibrary and S298=43.26 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 226,
    label = "HX_5 + NHX_1 <=> NH2_X + Ni_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.14127e+16,'m^2/(mol*s)'), n=0, Ea=(1.40603,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMzMDkx""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: HX + NHX <=> X + NH2X
equation : NH* + H* - 0* -> NH2* + *,
dft_code : Quantum Espresso,
dftFunctional : BEEF-vdW,
pubId: WangAchieving2021,
reactionEnergy: -0.7814711139653809 eV
A factor estimation:
A factor estimate for association
A factor estimated from gas-phase smiles [NH2] from Thermo library: primaryThermoLibrary and S298=46.52 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 227,
    label = "Ni_4 + CHX_1 <=> CX_3 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.54179e+16,'m^2/(mol*s)'), n=0, Ea=(1.87,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODE2""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: CHX + X <=> CX + HX
equation : CH* -> C* + H*,
dft_code : DACAPO,
dftFunctional : RPBE,
pubId: WangUniversal2011,
reactionEnergy: 0.582 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH] from Thermo library: DFT_QCI_thermo and S298=43.64 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 228,
    label = "Ni_4 + CH2X_1 <=> CHX_3 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(3.75303e+16,'m^2/(mol*s)'), n=0, Ea=(1.59,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODQ2""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: CH2X + X <=> HX + CHX
equation : CH2* -> CH* + H*,
dft_code : DACAPO,
dftFunctional : RPBE,
pubId: WangUniversal2011,
reactionEnergy: -0.07 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2] from Thermo library: primaryThermoLibrary and S298=46.64 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 229,
    label = "Ni_4 + C2H5X-2 <=> CH2X_3 + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.34702e+17,'m^2/(mol*s)'), n=0, Ea=(1.42325,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246OTQ0""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: CH2CH3X + X <=> CH2X + CH3X
equation : CH2CH3* -> CH2* + CH3*,
dft_code : DACAPO,
dftFunctional : RPBE,
pubId: WangUniversal2011,
reactionEnergy: 0.00225 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C[CH2] from Thermo library: DFT_QCI_thermo and S298=59.12 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 230,
    label = "Ni_4 + C2H3X-2 <=> CX_3 + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.76652e+17,'m^2/(mol*s)'), n=0, Ea=(1.75,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246OTUx""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: CCH3X + X <=> CX + CH3X
equation : CCH3* -> CH3* + C*,
dft_code : DACAPO,
dftFunctional : RPBE,
pubId: WangUniversal2011,
reactionEnergy: 0.242 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2]C from Thermo library: DFT_QCI_thermo + radical(Cs_P) and S298=60.52 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 231,
    label = "Ni_4 + C2H4X-3 <=> CHX_3 + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.38494e+17,'m^2/(mol*s)'), n=0, Ea=(2.07,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246OTU4""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: CHCH3X + X <=> CHX + CH3X
equation : CHCH3* -> CH3* + CH*,
dft_code : DACAPO,
dftFunctional : RPBE,
pubId: WangUniversal2011,
reactionEnergy: 0.294 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]C from Thermo library: DFT_QCI_thermo and S298=59.11 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 232,
    label = "Ni_4 + HOX_1 <=> OX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.13337e+16,'m^2/(mol*s)'), n=0, Ea=(1.238,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTAxOQ==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: OHX + X <=> HX + OX
equation : OH* -> H* + O*,
dft_code : DACAPO,
dftFunctional : RPBE,
pubId: WangUniversal2011,
reactionEnergy: 0.458 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [OH] from Thermo library: primaryThermoLibrary and S298=43.96 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 233,
    label = "Ni_4 + CH2OX2 <=> CHOX2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(4.58249e+16,'m^2/(mol*s)'), n=0, Ea=(0.35519,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTAzOQ==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: OCH2X + X <=> HX + OCHX
equation : H2CO* -> HCO* + H*,
dft_code : DACAPO,
dftFunctional : RPBE,
pubId: Studt et al submitted,
reactionEnergy: -0.52383 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C=O from Thermo library: DFT_QCI_thermo and S298=52.16 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 234,
    label = "Ni_4 + NHX_2 <=> NX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.13171e+16,'m^2/(mol*s)'), n=0, Ea=(4.1,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTEwOA==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: NHX + X <=> HX + NX
equation : NH* -> H* + N*,
dft_code : DACAPO,
dftFunctional : RPBE,
pubId: WangUniversal2011,
reactionEnergy: 0.498 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [NH] from Thermo library: primaryThermoLibrary and S298=43.26 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 235,
    label = "Ni_4 + CH4NX <=> CH2X_3 + H2NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.21807e+17,'m^2/(mol*s)'), n=0, Ea=(1.3,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTE4Mg==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: CH2NH2X + X <=> CH2X + NH2X
equation : CH2NH2* -> CH2* + NH2*,
dft_code : DACAPO,
dftFunctional : RPBE,
pubId: WangUniversal2011,
reactionEnergy: -0.218 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2]N from Thermo library: thermo_DFT_CCSDTF12_BAC and S298=58.64 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 236,
    label = "Ni_4 + CH3NX <=> CHX_3 + H2NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.05083e+17,'m^2/(mol*s)'), n=0, Ea=(1.98,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTE5Mw==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: CHNH2X + X <=> CHX + NH2X
equation : CHNH2* -> NH2* + CH*,
dft_code : DACAPO,
dftFunctional : RPBE,
pubId: WangUniversal2011,
reactionEnergy: -0.213 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]N from Thermo library: BurcatNS and S298=57.47 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 237,
    label = "Ni_4 + CH2NX <=> CX_3 + H2NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.96407e+15,'m^2/(mol*s)'), n=0, Ea=(2.62,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTE5OA==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: CNH2X + X <=> CX + NH2X
equation : CNH2* -> NH2* + C*,
dft_code : DACAPO,
dftFunctional : RPBE,
pubId: WangUniversal2011,
reactionEnergy: 0.465 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [C-]=[NH2+] from Thermo group additivity estimation: missing(N5dc-C2dcHH) + group(CsJ2_singlet-CsH) + radical(Cs_P) and S298=30.92 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 238,
    label = "Ni_4 + CH3OX <=> OX + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.27272e+16,'m^2/(mol*s)'), n=0, Ea=(1.632,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTMwNg==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: OCH3X + X <=> OX + CH3X
equation : OCH3* -> CH3* + O*,
dft_code : DACAPO,
dftFunctional : RPBE,
pubId: WangUniversal2011,
reactionEnergy: 0.272 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C[O] from Thermo library: DFT_QCI_thermo and S298=54.42 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 239,
    label = "Ni_4 + HOCXO_1 <=> OCX_3 + HOX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.09952e+17,'m^2/(mol*s)'), n=0, Ea=(1.18,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MjQwMA==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: COOHX + X <=> COX + OHX
equation : COOH* -> CO* + OH*,
dft_code : DACAPO,
dftFunctional : RPBE,
pubId: YooTheoretical2014,
reactionEnergy: -0.18 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles O=[C]O from Thermo library: DFT_QCI_thermo and S298=60.19 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 240,
    label = "Ni_4 + CH2OH* <=> HCOH* + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(1.1079e+17,'m^2/(mol*s)'), n=0, Ea=(1.17409,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI2ODc=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: X + H3COX <=> HX + CHOHX
equation : CH2OH* + * -> CHOH* + H*,
dft_code : Quantum ESPRESSO 5.1,
dftFunctional : BEEF-vdW,
pubId: SchumannSelectivity2018,
reactionEnergy: 0.0920782929024 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2]O from Thermo library: DFT_QCI_thermo and S298=58.19 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 241,
    label = "Ni_4 + CH2X_1 <=> CHX_3 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(3.75303e+16,'m^2/(mol*s)'), n=0, Ea=(0.488189,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI3Mzc=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: X + CH2X <=> HX + CHX
equation : CH2* + * -> CH* + H*,
dft_code : Quantum ESPRESSO 5.1,
dftFunctional : BEEF-vdW,
pubId: SchumannSelectivity2018,
reactionEnergy: -0.233971175883 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2] from Thermo library: primaryThermoLibrary and S298=46.64 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 242,
    label = "Ni_4 + CH3X_1 <=> CH2X_3 + HX_5",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(3.43628e+16,'m^2/(mol*s)'), n=0, Ea=(1.07538,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI3NTU=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: X + CH3X <=> HX + CH2X
equation : CH3* + * -> CH2* + H*,
dft_code : Quantum ESPRESSO 5.1,
dftFunctional : BEEF-vdW,
pubId: SchumannSelectivity2018,
reactionEnergy: 0.447704836493 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH3] from Thermo library: DFT_QCI_thermo and S298=46.44 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 243,
    label = "Ni_4 + C2H2OX2 <=> C2HOX2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(7.90722e+16,'m^2/(mol*s)'), n=0, Ea=(1.09126,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI3NjE=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: X + CH2COX <=> HX + CHCOX
equation : CH2CO* + * -> CHCO* + H*,
dft_code : Quantum ESPRESSO 5.1,
dftFunctional : BEEF-vdW,
pubId: SchumannSelectivity2018,
reactionEnergy: 0.282531048972 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C=C=O from Thermo library: DFT_QCI_thermo and S298=57.63 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 244,
    label = "Ni_4 + C2H3OX <=> OCX_3 + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.94915e+17,'m^2/(mol*s)'), n=0, Ea=(1.7264,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI4MjE=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: X + CH3COX <=> COX + CH3X
equation : CH3CO* + * -> CH3* + CO*,
dft_code : Quantum ESPRESSO 5.1,
dftFunctional : BEEF-vdW,
pubId: SchumannSelectivity2018,
reactionEnergy: -0.304254714007 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C[C]=O from Thermo library: DFT_QCI_thermo and S298=63.74 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 245,
    label = "Ni_4 + CH2OX <=> CHX_3 + HOX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.16208e+17,'m^2/(mol*s)'), n=0, Ea=(1.33159,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI4Mjc=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: X + CHOHX <=> CHX + OHX
equation : CHOH* + * -> CH* + OH*,
dft_code : Quantum ESPRESSO 5.1,
dftFunctional : BEEF-vdW,
pubId: SchumannSelectivity2018,
reactionEnergy: 0.608222143812 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]O from Thermo library: DFT_QCI_thermo and S298=58.32 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 246,
    label = "Ni_4 + CXHO_1 <=> OCX_3 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(5.78405e+16,'m^2/(mol*s)'), n=0, Ea=(0.119445,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI4NDU=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: X + CHOX <=> HX + COX
equation : CHO* + * -> CO* + H*,
dft_code : Quantum ESPRESSO 5.1,
dftFunctional : BEEF-vdW,
pubId: SchumannSelectivity2018,
reactionEnergy: -1.01473261691 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]=O from Thermo library: DFT_QCI_thermo and S298=53.51 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 247,
    label = "Ni_4 + C2H4X2 <=> C2H3X2 + HX_5",
    degeneracy = 4.0,
    kinetics = SurfaceArrhenius(A=(4.91881e+16,'m^2/(mol*s)'), n=0, Ea=(1.348,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NzE3""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: X + CH2CH2X <=> HX + CH2CHX
equation : CH2CH2* + * -> CH2CH* + H*,
dft_code : Quantum ESPRESSO 5.1,
dftFunctional : BEEF-vdW,
pubId: HansenFirst2018,
reactionEnergy: 0.2779333453217987 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C=C from Thermo library: DFT_QCI_thermo and S298=52.25 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 248,
    label = "Ni_4 + C2H3X2-3 <=> C2H2X2-4 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(8.63145e+16,'m^2/(mol*s)'), n=0, Ea=(1.75296,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NzE4""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: X + CH2CHX <=> HX + CCH2X
equation : CH2CH* + * -> CH2C* + H*,
dft_code : Quantum ESPRESSO 5.1,
dftFunctional : BEEF-vdW,
pubId: HansenFirst2018,
reactionEnergy: -0.16063724149717018 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]=C from Thermo library: DFT_QCI_thermo and S298=55.78 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 249,
    label = "Ni_4 + C2H3X2-2 <=> C2H2X2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(8.63145e+16,'m^2/(mol*s)'), n=0, Ea=(1.2408,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NzIw""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: X + CH2CHX <=> HX + CHCHX
equation : CH2CH* + * -> CHCH* + H*,
dft_code : Quantum ESPRESSO 5.1,
dftFunctional : BEEF-vdW,
pubId: HansenFirst2018,
reactionEnergy: 0.06311626339447685 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]=C from Thermo library: DFT_QCI_thermo and S298=55.78 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 250,
    label = "Ni_4 + C2H2X2-2 <=> C2HX2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(5.94456e+16,'m^2/(mol*s)'), n=0, Ea=(2.12687,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NzIy""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: X + CCH2X <=> HX + CCHX
equation : CH2C* + * -> CHC* + H*,
dft_code : Quantum ESPRESSO 5.1,
dftFunctional : BEEF-vdW,
pubId: HansenFirst2018,
reactionEnergy: 1.075023522193078 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [C]=C from Thermo library: DFT_QCI_thermo and S298=53.10 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 251,
    label = "Ni_4 + C2H5X <=> C2H4X + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(1.34702e+17,'m^2/(mol*s)'), n=0, Ea=(1.02577,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NzI1""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: X + CH2CH3X <=> HX + CHCH3X
equation : CH3CH2* + * -> CH3CH* + H*,
dft_code : Quantum ESPRESSO 5.1,
dftFunctional : BEEF-vdW,
pubId: HansenFirst2018,
reactionEnergy: 0.23460662973229773 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C[CH2] from Thermo library: DFT_QCI_thermo and S298=59.12 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 252,
    label = "Ni_4 + C2H4X-2 <=> C2H3X + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.38494e+17,'m^2/(mol*s)'), n=0, Ea=(0.666298,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NzI5""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: X + CHCH3X <=> HX + CCH3X
equation : CH3CH* + * -> CH3C* + H*,
dft_code : Quantum ESPRESSO 5.1,
dftFunctional : BEEF-vdW,
pubId: HansenFirst2018,
reactionEnergy: -0.6720497808419168 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]C from Thermo library: DFT_QCI_thermo and S298=59.11 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 253,
    label = "Ni_4 + C2H4X-3 <=> CHX_3 + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.38494e+17,'m^2/(mol*s)'), n=0, Ea=(1.56912,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NzMw""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: X + CHCH3X <=> CHX + CH3X
equation : CH3CH* + * -> CH3* + CH*,
dft_code : Quantum ESPRESSO 5.1,
dftFunctional : BEEF-vdW,
pubId: HansenFirst2018,
reactionEnergy: -0.2865575856412761 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]C from Thermo library: DFT_QCI_thermo and S298=59.11 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 254,
    label = "Ni_4 + C2H3X-2 <=> CX_3 + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.76652e+17,'m^2/(mol*s)'), n=0, Ea=(2.92687,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NzMy""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: X + CCH3X <=> CX + CH3X
equation : CH3C* + * -> CH3* + C*,
dft_code : Quantum ESPRESSO 5.1,
dftFunctional : BEEF-vdW,
pubId: HansenFirst2018,
reactionEnergy: 1.0065192004840355 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2]C from Thermo library: DFT_QCI_thermo + radical(Cs_P) and S298=60.52 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 255,
    label = "Ni_4 + C2H2X2-3 <=> C2HX2-2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.64307e+16,'m^2/(mol*s)'), n=0, Ea=(1.9186,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NzM5""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: X + CHCHX <=> HX + CCHX
equation : CHCH* + * -> CHC* + H*,
dft_code : Quantum ESPRESSO 5.1,
dftFunctional : BEEF-vdW,
pubId: HansenFirst2018,
reactionEnergy: 0.8512700173305348 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C#C from Thermo library: DFT_QCI_thermo and S298=47.73 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 256,
    label = "Ni_4 + C2HX2-3 <=> C2X2 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(9.32934e+16,'m^2/(mol*s)'), n=0, Ea=(1.81259,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NzQw""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: X + CCHX <=> HX + CCX
equation : CHC* + * -> CC* + H*,
dft_code : Quantum ESPRESSO 5.1,
dftFunctional : BEEF-vdW,
pubId: HansenFirst2018,
reactionEnergy: 1.0157081451034173 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]=C from Thermo library: DFT_QCI_thermo + radical(Cds_P) and S298=55.86 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 257,
    label = "HX_5 + NX <=> NHX_2 + Ni_4",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(A=(1.46209e+16,'m^2/(mol*s)'), n=0, Ea=(0.732214,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMzMDY2""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: HX + NX <=> X + NHX
equation : H* + N* - 0* -> NH* + *
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangAchieving2021
reactionEnergy: -2.040384142252151 eV

A factor estimation:
A factor estimate for association
A factor estimated from gas-phase smiles [NH] from Thermo library: primaryThermoLibrary and S298=43.26 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "211",
)

entry(
    index = 258,
    label = "HX_5 + NHX_1 <=> NH2_X + Ni_4",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(A=(6.14127e+16,'m^2/(mol*s)'), n=0, Ea=(0.822109,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMzMDY3""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: HX + NHX <=> X + NH2X
equation : NH* + H* - 0* -> NH2* + *
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangAchieving2021
reactionEnergy: -1.970278634573333 eV

A factor estimation:
A factor estimate for association
A factor estimated from gas-phase smiles [NH2] from Thermo library: primaryThermoLibrary and S298=46.52 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "211",
)

entry(
    index = 259,
    label = "Ni_4 + CHX_1 <=> CX_3 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.54179e+16,'m^2/(mol*s)'), n=0, Ea=(2.57,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODIw""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: CHX + X <=> CX + HX
equation : CH* -> C* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 1.858 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH] from Thermo library: DFT_QCI_thermo and S298=43.64 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 260,
    label = "Ni_4 + CH2X_1 <=> CHX_3 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(3.75303e+16,'m^2/(mol*s)'), n=0, Ea=(1.87,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODUy""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: CH2X + X <=> HX + CHX
equation : CH2* -> CH* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 1.327 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2] from Thermo library: primaryThermoLibrary and S298=46.64 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "211",
)

entry(
    index = 261,
    label = "Ni_4 + C2H3X-2 <=> CX_3 + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.76652e+17,'m^2/(mol*s)'), n=0, Ea=(2.02,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246OTU3""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: CCH3X + X <=> CX + CH3X
equation : CCH3* -> CH3* + C*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 1.472 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2]C from Thermo library: DFT_QCI_thermo + radical(Cs_P) and S298=60.52 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "211",
)

entry(
    index = 262,
    label = "Ni_4 + C2H4X-3 <=> CHX_3 + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.38494e+17,'m^2/(mol*s)'), n=0, Ea=(2.27,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246OTYy""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: CHCH3X + X <=> CHX + CH3X
equation : CHCH3* -> CH3* + CH*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 1.674 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]C from Thermo library: DFT_QCI_thermo and S298=59.11 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "211",
)

entry(
    index = 263,
    label = "Ni_4 + C2H5X-2 <=> CH2X_3 + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.34702e+17,'m^2/(mol*s)'), n=0, Ea=(2.33325,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246OTYz""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: CH2CH3X + X <=> CH2X + CH3X
equation : CH2CH3* -> CH2* + CH3*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 1.96225 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C[CH2] from Thermo library: DFT_QCI_thermo and S298=59.12 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "211",
)

entry(
    index = 264,
    label = "Ni_4 + HOX_1 <=> OX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.13337e+16,'m^2/(mol*s)'), n=0, Ea=(2.422,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTAyNg==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: OHX + X <=> HX + OX
equation : OH* -> H* + O*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 1.624 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [OH] from Thermo library: primaryThermoLibrary and S298=43.96 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 265,
    label = "Ni_4 + CH2OX2 <=> CHOX2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(4.58249e+16,'m^2/(mol*s)'), n=0, Ea=(1.33812,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTA0NA==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: OCH2X + X <=> HX + OCHX
equation : H2CO* -> HCO* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: Studt et al submitted
reactionEnergy: 1.12588 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C=O from Thermo library: DFT_QCI_thermo and S298=52.16 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "211",
)

entry(
    index = 266,
    label = "Ni_4 + NHX_2 <=> NX + HX_5",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(A=(2.13171e+16,'m^2/(mol*s)'), n=0, Ea=(2.95,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTA5OQ==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: NHX + X <=> HX + NX
equation : NH* -> H* + N*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 1.737 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [NH] from Thermo library: primaryThermoLibrary and S298=43.26 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "211",
)

entry(
    index = 267,
    label = "Ni_4 + NH2_X <=> NHX_1 + HX_5",
    degeneracy = 2.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(A=(3.29883e+16,'m^2/(mol*s)'), n=0, Ea=(3.07,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTE1Mw==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: NH2X + X <=> HX + NHX
equation : NH2* -> NH* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 1.967 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [NH2] from Thermo library: primaryThermoLibrary and S298=46.52 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "211",
)

entry(
    index = 268,
    label = "Ni_4 + CH4NX <=> CH2X_3 + H2NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.21807e+17,'m^2/(mol*s)'), n=0, Ea=(1.96,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTE5Mg==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: CH2NH2X + X <=> CH2X + NH2X
equation : CH2NH2* -> CH2* + NH2*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 1.182 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2]N from Thermo library: thermo_DFT_CCSDTF12_BAC and S298=58.64 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "211",
)

entry(
    index = 269,
    label = "Ni_4 + CH3NX <=> CHX_3 + H2NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.05083e+17,'m^2/(mol*s)'), n=0, Ea=(2.67,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTE5OQ==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: CHNH2X + X <=> CHX + NH2X
equation : CHNH2* -> NH2* + CH*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 1.417 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]N from Thermo library: BurcatNS and S298=57.47 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "211",
)

entry(
    index = 270,
    label = "Ni_4 + CH2NX <=> CX_3 + H2NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.96407e+15,'m^2/(mol*s)'), n=0, Ea=(2.82,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTIwMA==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: CNH2X + X <=> CX + NH2X
equation : CNH2* -> NH2* + C*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 1.655 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [C-]=[NH2+] from Thermo group additivity estimation: missing(N5dc-C2dcHH) + group(CsJ2_singlet-CsH) + radical(Cs_P) and S298=30.92 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "211",
)

entry(
    index = 271,
    label = "Ni_4 + CH3OX <=> OX + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.27272e+16,'m^2/(mol*s)'), n=0, Ea=(2.332,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTMyNg==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: OCH3X + X <=> OX + CH3X
equation : OCH3* -> CH3* + O*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 1.632 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C[O] from Thermo library: DFT_QCI_thermo and S298=54.42 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "211",
)

entry(
    index = 272,
    label = "Ni_4 + HOCXO_1 <=> OCX_3 + HOX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.09952e+17,'m^2/(mol*s)'), n=0, Ea=(0.71,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MjM5NQ==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: COOHX + X <=> COX + OHX
equation : COOH* -> CO* + OH*
dft_code : DACAPO
dftFunctional : RPBE
pubId: YooTheoretical2014
reactionEnergy: 0.43 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles O=[C]O from Thermo library: DFT_QCI_thermo and S298=60.19 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "211",
)

entry(
    index = 273,
    label = "Ni_4 + CH2OH* <=> HCOH* + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(1.1079e+17,'m^2/(mol*s)'), n=0, Ea=(1.91489,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI2ODk=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: X + H3COX <=> HX + CHOHX
equation : CH2OH* + * -> CHOH* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: 1.61846352162 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2]O from Thermo library: DFT_QCI_thermo and S298=58.19 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 274,
    label = "Ni_4 + CH2X_1 <=> CHX_3 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(3.75303e+16,'m^2/(mol*s)'), n=0, Ea=(2.08112,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI3Mzk=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: X + CH2X <=> HX + CHX
equation : CH2* + * -> CH* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: 1.71752473214 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2] from Thermo library: primaryThermoLibrary and S298=46.64 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 275,
    label = "Ni_4 + C2H2OX2 <=> C2HOX2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(7.90722e+16,'m^2/(mol*s)'), n=0, Ea=(1.86132,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI3NjM=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: X + CH2COX <=> HX + CHCOX
equation : CH2CO* + * -> CHCO* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: 1.13913361341 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C=C=O from Thermo library: DFT_QCI_thermo and S298=57.63 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 276,
    label = "Ni_4 + C2H3OX <=> OCX_3 + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.94915e+17,'m^2/(mol*s)'), n=0, Ea=(1.61146,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI4MjM=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: X + CH3COX <=> COX + CH3X
equation : CH3CO* + * -> CH3* + CO*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: 0.743970628013 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C[C]=O from Thermo library: DFT_QCI_thermo and S298=63.74 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 277,
    label = "Ni_4 + CH2OX <=> CHX_3 + HOX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.16208e+17,'m^2/(mol*s)'), n=0, Ea=(1.83906,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI4Mjk=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: X + CHOHX <=> CHX + OHX
equation : CHOH* + * -> CH* + OH*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: 1.40617070382 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]O from Thermo library: DFT_QCI_thermo and S298=58.32 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 278,
    label = "Ni_4 + CXHO_1 <=> OCX_3 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(5.78405e+16,'m^2/(mol*s)'), n=0, Ea=(0.418512,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI4NDc=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: X + CHOX <=> HX + COX
equation : CHO* + * -> CO* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: -0.233916753103 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]=O from Thermo library: DFT_QCI_thermo and S298=53.51 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 279,
    label = "Ni_4 + C2H4X2 <=> C2H3X2 + HX_5",
    degeneracy = 4.0,
    kinetics = SurfaceArrhenius(A=(4.91881e+16,'m^2/(mol*s)'), n=0, Ea=(2.60592,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MTQz""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: X + CH2CH2X <=> HX + CHCH2X
equation : CH2CH2* + * -> CH2CH* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 1.8325415423023514 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C=C from Thermo library: DFT_QCI_thermo and S298=52.25 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 280,
    label = "Ni_4 + C2H3X2-3 <=> C2H2X2-4 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(8.63145e+16,'m^2/(mol*s)'), n=0, Ea=(2.02521,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MTQ0""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: X + CHCH2X <=> HX + CCH2X
equation : CH2CH* + * -> CH2C* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 1.3043633203487843 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]=C from Thermo library: DFT_QCI_thermo and S298=55.78 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 281,
    label = "Ni_4 + C2H3X2-2 <=> C2H2X2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(8.63145e+16,'m^2/(mol*s)'), n=0, Ea=(1.83628,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MTQ2""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: X + CHCH2X <=> HX + CHCHX
equation : CH2CH* + * -> CHCH* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.959932424913859 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]=C from Thermo library: DFT_QCI_thermo and S298=55.78 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 282,
    label = "Ni_4 + C2H5X <=> C2H4X + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(1.34702e+17,'m^2/(mol*s)'), n=0, Ea=(2.2717,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MTUx""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: X + CH2CH3X <=> HX + CHCH3X
equation : CH3CH2* + * -> CH3CH* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 1.8489720487850718 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C[CH2] from Thermo library: DFT_QCI_thermo and S298=59.12 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 283,
    label = "Ni_4 + C2H4X-2 <=> C2H3X + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.38494e+17,'m^2/(mol*s)'), n=0, Ea=(1.75595,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MTU1""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: X + CHCH3X <=> HX + CCH3X
equation : CH3CH* + * -> CH3C* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 1.197035699209664 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]C from Thermo library: DFT_QCI_thermo and S298=59.11 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 284,
    label = "Ni_4 + C2H4X-3 <=> CHX_3 + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.38494e+17,'m^2/(mol*s)'), n=0, Ea=(2.17162,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MTU2""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: X + CHCH3X <=> CHX + CH3X
equation : CH3CH* + * -> CH3* + CH*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 1.7711963999608997 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]C from Thermo library: DFT_QCI_thermo and S298=59.11 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 285,
    label = "Ni_4 + C2H3X-2 <=> CX_3 + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.76652e+17,'m^2/(mol*s)'), n=0, Ea=(2.8211,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MTU4""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: X + CCH3X <=> CX + CH3X
equation : CH3C* + * -> CH3* + C*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 2.2393908652011305 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2]C from Thermo library: DFT_QCI_thermo + radical(Cs_P) and S298=60.52 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 286,
    label = "Ni_4 + C2H2X2-3 <=> C2HX2-2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.64307e+16,'m^2/(mol*s)'), n=0, Ea=(1.9515,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MTY1""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: X + CHCHX <=> HX + CCHX
equation : CHCH* + * -> CHC* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.838547606341308 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C#C from Thermo library: DFT_QCI_thermo and S298=47.73 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 287,
    label = "Ni_4 + C2HX2-3 <=> C2X2 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(9.32934e+16,'m^2/(mol*s)'), n=0, Ea=(2.52272,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MTY2""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: X + CCHX <=> HX + CCX
equation : CHC* + * -> CC* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 1.6599072774115484 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]=C from Thermo library: DFT_QCI_thermo + radical(Cds_P) and S298=55.86 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 288,
    label = "HX_5 + NX <=> NHX_2 + Ni_4",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(A=(1.46209e+16,'m^2/(mol*s)'), n=0, Ea=(0.548958,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMzMDMw""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Au
Original entry: HX + NX <=> X + NHX
equation : H* + N* - 0* -> NH* + *
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangAchieving2021
reactionEnergy: -1.913205135409953 eV

A factor estimation:
A factor estimate for association
A factor estimated from gas-phase smiles [NH] from Thermo library: primaryThermoLibrary and S298=43.26 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Au",
    facet = "211",
)

entry(
    index = 289,
    label = "HX_5 + NHX_1 <=> NH2_X + Ni_4",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(A=(6.14127e+16,'m^2/(mol*s)'), n=0, Ea=(0.825864,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMzMDMx""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Au
Original entry: HX + NHX <=> X + NH2X
equation : NH* + H* - 0* -> NH2* + *
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangAchieving2021
reactionEnergy: -1.9715859375428408 eV

A factor estimation:
A factor estimate for association
A factor estimated from gas-phase smiles [NH2] from Thermo library: primaryThermoLibrary and S298=46.52 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Au",
    facet = "211",
)

entry(
    index = 290,
    label = "Ni_4 + CHX_1 <=> CX_3 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.54179e+16,'m^2/(mol*s)'), n=0, Ea=(2.58,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODIx""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Au
Original entry: CHX + X <=> CX + HX
equation : CH* -> C* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 1.714 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH] from Thermo library: DFT_QCI_thermo and S298=43.64 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Au",
    facet = "111",
)

entry(
    index = 291,
    label = "Ni_4 + CH2X_1 <=> CHX_3 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(3.75303e+16,'m^2/(mol*s)'), n=0, Ea=(2.35,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODU2""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Au
Original entry: CH2X + X <=> HX + CHX
equation : CH2* -> CH* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 1.3 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2] from Thermo library: primaryThermoLibrary and S298=46.64 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Au",
    facet = "211",
)

entry(
    index = 292,
    label = "Ni_4 + CH3X_1 <=> CH2X_3 + HX_5",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(3.43628e+16,'m^2/(mol*s)'), n=0, Ea=(2.1,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODkz""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Au
Original entry: CH3X + X <=> HX + CH2X
equation : CH3* -> CH2* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 1.47 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH3] from Thermo library: DFT_QCI_thermo and S298=46.44 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Au",
    facet = "111",
)

entry(
    index = 293,
    label = "Ni_4 + C2H5X-2 <=> CH2X_3 + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.34702e+17,'m^2/(mol*s)'), n=0, Ea=(2.11325,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246OTU5""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Au
Original entry: CH2CH3X + X <=> CH2X + CH3X
equation : CH2CH3* -> CH2* + CH3*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 1.39225 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C[CH2] from Thermo library: DFT_QCI_thermo and S298=59.12 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Au",
    facet = "211",
)

entry(
    index = 294,
    label = "Ni_4 + C2H4X-3 <=> CHX_3 + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.38494e+17,'m^2/(mol*s)'), n=0, Ea=(2.5,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246OTY2""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Au
Original entry: CHCH3X + X <=> CHX + CH3X
equation : CHCH3* -> CH3* + CH*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 1.534 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]C from Thermo library: DFT_QCI_thermo and S298=59.11 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Au",
    facet = "211",
)

entry(
    index = 295,
    label = "Ni_4 + C2H3X-2 <=> CX_3 + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.76652e+17,'m^2/(mol*s)'), n=0, Ea=(2.53,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246OTY3""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Au
Original entry: CCH3X + X <=> CX + CH3X
equation : CCH3* -> CH3* + C*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 1.592 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2]C from Thermo library: DFT_QCI_thermo + radical(Cs_P) and S298=60.52 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Au",
    facet = "211",
)

entry(
    index = 296,
    label = "Ni_4 + HOX_1 <=> OX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.13337e+16,'m^2/(mol*s)'), n=0, Ea=(2.236,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTAyNA==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Au
Original entry: OHX + X <=> HX + OX
equation : OH* -> H* + O*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 1.771 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [OH] from Thermo library: primaryThermoLibrary and S298=43.96 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Au",
    facet = "211",
)

entry(
    index = 297,
    label = "Ni_4 + NHX_2 <=> NX + HX_5",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(A=(2.13171e+16,'m^2/(mol*s)'), n=0, Ea=(2.59,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTA5NA==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Au
Original entry: NHX + X <=> HX + NX
equation : NH* -> H* + N*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 1.66 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [NH] from Thermo library: primaryThermoLibrary and S298=43.26 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Au",
    facet = "211",
)

entry(
    index = 298,
    label = "Ni_4 + NH2_X <=> NHX_1 + HX_5",
    degeneracy = 2.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(A=(3.29883e+16,'m^2/(mol*s)'), n=0, Ea=(2.6,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTE0OA==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Au
Original entry: NH2X + X <=> HX + NHX
equation : NH2* -> NH* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 1.79 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [NH2] from Thermo library: primaryThermoLibrary and S298=46.52 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Au",
    facet = "211",
)

entry(
    index = 299,
    label = "Ni_4 + C2H4X2 <=> C2H3X2 + HX_5",
    degeneracy = 4.0,
    kinetics = SurfaceArrhenius(A=(4.91881e+16,'m^2/(mol*s)'), n=0, Ea=(2.1934,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MTg3""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Au
Original entry: X + CH2CH2X <=> HX + CHCH2X
equation : CH2CH2* + * -> CH2CH* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 1.5931408107862808 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C=C from Thermo library: DFT_QCI_thermo and S298=52.25 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Au",
    facet = "111",
)

entry(
    index = 300,
    label = "Ni_4 + C2H3X2-3 <=> C2H2X2-4 + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(8.63145e+16,'m^2/(mol*s)'), n=0, Ea=(1.99526,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MTg4""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Au
Original entry: X + CHCH2X <=> HX + CCH2X
equation : CH2CH* + * -> CH2C* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 1.275880687404424 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]=C from Thermo library: DFT_QCI_thermo and S298=55.78 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Au",
    facet = "111",
)

entry(
    index = 301,
    label = "Ni_4 + C2H3X2-2 <=> C2H2X2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(8.63145e+16,'m^2/(mol*s)'), n=0, Ea=(1.96171,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MTkw""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Au
Original entry: X + CHCH2X <=> HX + CHCHX
equation : CH2CH* + * -> CHCH* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 1.2384102700452786 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]=C from Thermo library: DFT_QCI_thermo and S298=55.78 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Au",
    facet = "111",
)

entry(
    index = 302,
    label = "Ni_4 + C2H5X <=> C2H4X + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(1.34702e+17,'m^2/(mol*s)'), n=0, Ea=(2.16988,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MTk1""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Au
Original entry: X + CH2CH3X <=> HX + CHCH3X
equation : CH3CH2* + * -> CH3CH* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 1.7260147522902116 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C[CH2] from Thermo library: DFT_QCI_thermo and S298=59.12 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Au",
    facet = "111",
)

entry(
    index = 303,
    label = "Ni_4 + C2H5X-2 <=> CH2X_3 + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.34702e+17,'m^2/(mol*s)'), n=0, Ea=(3.68796,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MTk2""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Au
Original entry: X + CH2CH3X <=> CH2X + CH3X
equation : CH3CH2* + * -> CH2* + CH3*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 1.9160877734830137 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C[CH2] from Thermo library: DFT_QCI_thermo and S298=59.12 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Au",
    facet = "111",
)

entry(
    index = 304,
    label = "Ni_4 + C2H4X-2 <=> C2H3X + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.38494e+17,'m^2/(mol*s)'), n=0, Ea=(1.46076,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MTk5""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Au
Original entry: X + CHCH3X <=> HX + CCH3X
equation : CH3CH* + * -> CH3C* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.8861924286175054 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]C from Thermo library: DFT_QCI_thermo and S298=59.11 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Au",
    facet = "111",
)

entry(
    index = 305,
    label = "Ni_4 + C2H3X-2 <=> CX_3 + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.76652e+17,'m^2/(mol*s)'), n=0, Ea=(2.80423,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MjAy""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Au
Original entry: X + CCH3X <=> CX + CH3X
equation : CH3C* + * -> CH3* + C*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 2.1216980193566997 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH2]C from Thermo library: DFT_QCI_thermo + radical(Cs_P) and S298=60.52 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Au",
    facet = "111",
)

entry(
    index = 306,
    label = "Ni_4 + C2H2X2-3 <=> C2HX2-2 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.64307e+16,'m^2/(mol*s)'), n=0, Ea=(2.11764,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MjA5""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Au
Original entry: X + CHCHX <=> HX + CCHX
equation : CHCH* + * -> CHC* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 1.159139695810154 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles C#C from Thermo library: DFT_QCI_thermo and S298=47.73 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Au",
    facet = "111",
)

