#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_vdW/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 7,
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
    index = 12,
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
    index = 13,
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
    index = 14,
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

#duplicate of 14
# entry(
#     index = 29,
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
    index = 19,
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
    index = 25,
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
    index = 30,
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
    index = 33,
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
    index = 34,
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
    index = 35,
    label = "X_4 + C3H8X <=> C3H7X + H*",
    degeneracy = 6.0,
    kinetics = SurfaceArrhenius(A=(2.71485e+17,'m^2/(mol*s)'), n=0, Ea=(1.26699,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNTI4""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: X + CH3CH2CH3X <=> HX + CH3CH2CH2X
equation : CH3CH2CH3* + * -> CH3CH2CH2* + H*
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangTheory-aided2020
reactionEnergy: 0.575621450872859 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles CCC from Thermo library: DFT_QCI_thermo and S298=66.07 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 36,
    label = "X_4 + C3H8X-2 <=> C3H7X-2 + H*",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.71485e+17,'m^2/(mol*s)'), n=0, Ea=(1.20054,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNTI5""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: X + CH3CH2CH3X <=> HX + CH3CHCH3X
equation : CH3CH2CH3* + * -> CH3CHCH3* + H*
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangTheory-aided2020
reactionEnergy: 0.5531115138728637 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles CCC from Thermo library: DFT_QCI_thermo and S298=66.07 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 37,
    label = "H* + NH2_X <=> NH3_X + X_4",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(A=(1.70555e+18,'m^2/(mol*s)'), n=0, Ea=(1.13868,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyOTk2""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: HX + NH2X <=> X + NH3X
equation : NH2* + H* - 0* -> NH3* + *
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangAchieving2021
reactionEnergy: -0.24122035686741583 eV

A factor estimation:
A factor estimate for association
A factor estimated from gas-phase smiles N from Thermo library: primaryThermoLibrary and S298=45.99 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 38,
    label = "X_4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(A=(2.89421e+16,'m^2/(mol*s)'), n=0, Ea=(1.86,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTE4OQ==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: NH3X + X <=> HX + NH2X
equation : NH3* -> NH2* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 0.14 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles N from Thermo library: primaryThermoLibrary and S298=45.99 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 39,
    label = "X_4 + H2O* <=> OH* + H*",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.4102e+16,'m^2/(mol*s)'), n=0, Ea=(1.263,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTQwMQ==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: H2OX + X <=> HX + OHX
equation : H2O* -> OH* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 0.623 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles O from Thermo library: primaryThermoLibrary and S298=45.08 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 40,
    label = "X_4 + C2H6OX <=> C2H5OX + H*",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.91245e+17,'m^2/(mol*s)'), n=0, Ea=(0.905763,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI3NDE=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: X + CH3CH2OHX <=> HX + CH3CHOHX
equation : CH3CH2OH* + * -> CH3CHOH* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: 0.159325992863 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles CCO from Thermo library: DFT_QCI_thermo and S298=66.77 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 41,
    label = "X_4 + C3H8X <=> C3H7X + H*",
    degeneracy = 6.0,
    kinetics = SurfaceArrhenius(A=(2.71485e+17,'m^2/(mol*s)'), n=0, Ea=(1.26059,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNTM0""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ni
Original entry: X + CH3CH2CH3X <=> HX + CH3CH2CH2X
equation : CH3CH2CH3* + * -> CH3CH2CH2* + H*,
dft_code : Quantum Espresso,
dftFunctional : BEEF-vdW,
pubId: WangTheory-aided2020,
reactionEnergy: 0.7517773376312107 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles CCC from Thermo library: DFT_QCI_thermo and S298=66.07 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 42,
    label = "X_4 + C3H8X-2 <=> C3H7X-2 + H*",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.71485e+17,'m^2/(mol*s)'), n=0, Ea=(1.26435,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNTM1""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ni
Original entry: X + CH3CH2CH3X <=> HX + CH3CHCH3X
equation : CH3CH2CH3* + * -> CH3CHCH3* + H*,
dft_code : Quantum Espresso,
dftFunctional : BEEF-vdW,
pubId: WangTheory-aided2020,
reactionEnergy: 0.7864103543106467 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles CCC from Thermo library: DFT_QCI_thermo and S298=66.07 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 43,
    label = "H* + NH2_X <=> NH3_X + X_4",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(A=(1.70555e+18,'m^2/(mol*s)'), n=0, Ea=(1.2876,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMzMDQ0""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ni
Original entry: HX + NH2X <=> X + NH3X
equation : NH2* + H* - 0* -> NH3* + *,
dft_code : Quantum Espresso,
dftFunctional : BEEF-vdW,
pubId: WangAchieving2021,
reactionEnergy: 0.2404461249243468 eV

A factor estimation:
A factor estimate for association
A factor estimated from gas-phase smiles N from Thermo library: primaryThermoLibrary and S298=45.99 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ni",
    facet = "211",
)

entry(
    index = 44,
    label = "X_4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(A=(2.89421e+16,'m^2/(mol*s)'), n=0, Ea=(1.34,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTE4Mw==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ni
Original entry: NH3X + X <=> HX + NH2X
equation : NH3* -> NH2* + H*,
dft_code : DACAPO,
dftFunctional : RPBE,
pubId: WangUniversal2011,
reactionEnergy: -0.445 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles N from Thermo library: primaryThermoLibrary and S298=45.99 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ni",
    facet = "211",
)

entry(
    index = 45,
    label = "X_4 + H2O* <=> OH* + H*",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.4102e+16,'m^2/(mol*s)'), n=0, Ea=(0.67,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTM4MA==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ni
Original entry: H2OX + X <=> HX + OHX
equation : H2O* -> OH* + H*,
dft_code : DACAPO,
dftFunctional : RPBE,
pubId: WangUniversal2011,
reactionEnergy: -0.6 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles O from Thermo library: primaryThermoLibrary and S298=45.08 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ni",
    facet = "211",
)

entry(
    index = 46,
    label = "X_4 + C3H8X <=> C3H7X + H*",
    degeneracy = 6.0,
    kinetics = SurfaceArrhenius(A=(2.71485e+17,'m^2/(mol*s)'), n=0, Ea=(1.06909,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNTM2""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ir
Original entry: X + CH3CH2CH3X <=> HX + CH3CH2CH2X
equation : CH3CH2CH3* + * -> CH3CH2CH2* + H*
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangTheory-aided2020
reactionEnergy: 0.3886408756370656 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles CCC from Thermo library: DFT_QCI_thermo and S298=66.07 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 47,
    label = "X_4 + C3H8X-2 <=> C3H7X-2 + H*",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.71485e+17,'m^2/(mol*s)'), n=0, Ea=(1.0236,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNTM3""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ir
Original entry: X + CH3CH2CH3X <=> HX + CH3CHCH3X
equation : CH3CH2CH3* + * -> CH3CHCH3* + H*
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangTheory-aided2020
reactionEnergy: 0.4265471497201361 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles CCC from Thermo library: DFT_QCI_thermo and S298=66.07 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 48,
    label = "H* + NH2_X <=> NH3_X + X_4",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(A=(1.70555e+18,'m^2/(mol*s)'), n=0, Ea=(1.57614,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyOTcy""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ir
Original entry: HX + NH2X <=> X + NH3X
equation : NH2* + H* - 0* -> NH3* + *
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangAchieving2021
reactionEnergy: 0.38782822457142174 eV

A factor estimation:
A factor estimate for association
A factor estimated from gas-phase smiles N from Thermo library: primaryThermoLibrary and S298=45.99 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ir",
    facet = "211",
)

entry(
    index = 49,
    label = "X_4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(A=(2.89421e+16,'m^2/(mol*s)'), n=0, Ea=(1.26,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTE3OQ==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ir
Original entry: NH3X + X <=> HX + NH2X
equation : NH3* -> NH2* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: -0.624 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles N from Thermo library: primaryThermoLibrary and S298=45.99 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ir",
    facet = "211",
)

entry(
    index = 50,
    label = "X_4 + H2O* <=> OH* + H*",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.4102e+16,'m^2/(mol*s)'), n=0, Ea=(0.77,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTM4Ng==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ir
Original entry: H2OX + X <=> HX + OHX
equation : H2O* -> OH* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 0.353 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles O from Thermo library: primaryThermoLibrary and S298=45.08 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 51,
    label = "X_4 + C2H6OX <=> C2H5OX + H*",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.91245e+17,'m^2/(mol*s)'), n=0, Ea=(0.919243,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI3NDI=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ir
Original entry: X + CH3CH2OHX <=> HX + CH3CHOHX
equation : CH3CH2OH* + * -> CH3CHOH* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: 0.319209274894 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles CCO from Thermo library: DFT_QCI_thermo and S298=66.77 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 52,
    label = "H* + NH2_X <=> NH3_X + X_4",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(A=(1.70555e+18,'m^2/(mol*s)'), n=0, Ea=(1.35876,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMzMDIw""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: HX + NH2X <=> X + NH3X
equation : NH2* + H* - 0* -> NH3* + *
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangAchieving2021
reactionEnergy: -0.28039760841056705 eV

A factor estimation:
A factor estimate for association
A factor estimated from gas-phase smiles N from Thermo library: primaryThermoLibrary and S298=45.99 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Cu",
    facet = "211",
)

entry(
    index = 53,
    label = "X_4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(A=(2.89421e+16,'m^2/(mol*s)'), n=0, Ea=(1.65,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTE4OA==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: NH3X + X <=> HX + NH2X
equation : NH3* -> NH2* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 0.261 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles N from Thermo library: primaryThermoLibrary and S298=45.99 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Cu",
    facet = "211",
)

entry(
    index = 54,
    label = "X_4 + H2O* <=> OH* + H*",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.4102e+16,'m^2/(mol*s)'), n=0, Ea=(1.344,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTQwMw==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: H2OX + X <=> HX + OHX
equation : H2O* -> OH* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 0.256 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles O from Thermo library: primaryThermoLibrary and S298=45.08 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 55,
    label = "X_4 + C2H6OX <=> C2H5OX + H*",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.91245e+17,'m^2/(mol*s)'), n=0, Ea=(1.83774,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI3NDY=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: X + CH3CH2OHX <=> HX + CH3CHOHX
equation : CH3CH2OH* + * -> CH3CHOH* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: 1.43196893361 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles CCO from Thermo library: DFT_QCI_thermo and S298=66.77 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 56,
    label = "H* + NH2_X <=> NH3_X + X_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.70555e+18,'m^2/(mol*s)'), n=0, Ea=(1.02141,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMzMDgw""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Co
Original entry: HX + NH2X <=> X + NH3X
equation : NH2* + H* - 0* -> NH3* + *
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangAchieving2021
reactionEnergy: 0.10108553350437433 eV

A factor estimation:
A factor estimate for association
A factor estimated from gas-phase smiles N from Thermo library: primaryThermoLibrary and S298=45.99 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Co",
    facet = "211",
)

entry(
    index = 57,
    label = "X_4 + C3H8X <=> C3H7X + H*",
    degeneracy = 6.0,
    kinetics = SurfaceArrhenius(A=(2.71485e+17,'m^2/(mol*s)'), n=0, Ea=(1.11028,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNTMy""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ru
Original entry: X + CH3CH2CH3X <=> HX + CH3CH2CH2X
equation : CH3CH2CH3* + * -> CH3CH2CH2* + H*
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangTheory-aided2020
reactionEnergy: 0.4599756545503624 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles CCC from Thermo library: DFT_QCI_thermo and S298=66.07 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ru",
    facet = "111",
)

entry(
    index = 58,
    label = "X_4 + C3H8X-2 <=> C3H7X-2 + H*",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.71485e+17,'m^2/(mol*s)'), n=0, Ea=(1.06968,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNTMz""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ru
Original entry: X + CH3CH2CH3X <=> HX + CH3CHCH3X
equation : CH3CH2CH3* + * -> CH3CHCH3* + H*
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangTheory-aided2020
reactionEnergy: 0.5354069711756893 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles CCC from Thermo library: DFT_QCI_thermo and S298=66.07 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ru",
    facet = "111",
)

entry(
    index = 59,
    label = "H* + NH2_X <=> NH3_X + X_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.70555e+18,'m^2/(mol*s)'), n=0, Ea=(1.45343,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMzMDA4""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ru
Original entry: HX + NH2X <=> X + NH3X
equation : NH2* + H* - 0* -> NH3* + *
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangAchieving2021
reactionEnergy: 0.42841903946828097 eV

A factor estimation:
A factor estimate for association
A factor estimated from gas-phase smiles N from Thermo library: primaryThermoLibrary and S298=45.99 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ru",
    facet = "211",
)

entry(
    index = 60,
    label = "X_4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(2.89421e+16,'m^2/(mol*s)'), n=0, Ea=(0.75,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTE2Ng==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ru
Original entry: NH3X + X <=> HX + NH2X
equation : NH3* -> NH2* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: LogadottirAmmonia2003
reactionEnergy: -0.45 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles N from Thermo library: primaryThermoLibrary and S298=45.99 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ru",
    facet = "0001step",
)

entry(
    index = 61,
    label = "X_4 + H2O* <=> OH* + H*",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.4102e+16,'m^2/(mol*s)'), n=0, Ea=(0.946,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTM5NQ==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ru
Original entry: H2OX + X <=> HX + OHX
equation : H2O* -> OH* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: -0.043 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles O from Thermo library: primaryThermoLibrary and S298=45.08 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ru",
    facet = "111",
)

entry(
    index = 62,
    label = "X_4 + C3H8X-2 <=> C3H7X-2 + H*",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.71485e+17,'m^2/(mol*s)'), n=0, Ea=(0.974198,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNTI3""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: X + CH3CH2CH3X <=> HX + CH3CHCH3X
equation : CH3CH2CH3* + * -> CH3CHCH3* + H*
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangTheory-aided2020
reactionEnergy: 0.484577874885872 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles CCC from Thermo library: DFT_QCI_thermo and S298=66.07 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 63,
    label = "X_4 + C3H8X <=> C3H7X + H*",
    degeneracy = 6.0,
    kinetics = SurfaceArrhenius(A=(2.71485e+17,'m^2/(mol*s)'), n=0, Ea=(1.00171,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNTc0""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: X + CH3CH2CH3X <=> HX + CH3CH2CH2X
equation : CH3CH2CH3* + * -> CH3CH2CH2* + H*
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangTheory-aided2020
reactionEnergy: 0.4830551258346531 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles CCC from Thermo library: DFT_QCI_thermo and S298=66.07 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 64,
    label = "H* + NH2_X <=> NH3_X + X_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.70555e+18,'m^2/(mol*s)'), n=0, Ea=(1.24014,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMzMTA0""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: HX + NH2X <=> X + NH3X
equation : NH2* + H* - 0* -> NH3* + *
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangAchieving2021
reactionEnergy: 0.19994272661278956 eV

A factor estimation:
A factor estimate for association
A factor estimated from gas-phase smiles N from Thermo library: primaryThermoLibrary and S298=45.99 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 65,
    label = "X_4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(2.89421e+16,'m^2/(mol*s)'), n=0, Ea=(1.41,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTE4NQ==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: NH3X + X <=> HX + NH2X
equation : NH3* -> NH2* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 0.29 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles N from Thermo library: primaryThermoLibrary and S298=45.99 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 66,
    label = "X_4 + H2O* <=> OH* + H*",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.4102e+16,'m^2/(mol*s)'), n=0, Ea=(0.95,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTM5Ng==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: H2OX + X <=> HX + OHX
equation : H2O* -> OH* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 0.216 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles O from Thermo library: primaryThermoLibrary and S298=45.08 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 67,
    label = "X_4 + C2H6OX <=> C2H5OX + H*",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.91245e+17,'m^2/(mol*s)'), n=0, Ea=(0.957171,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI3NDQ=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: X + CH3CH2OHX <=> HX + CH3CHOHX
equation : CH3CH2OH* + * -> CH3CHOH* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: 0.23590161957 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles CCO from Thermo library: DFT_QCI_thermo and S298=66.77 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 68,
    label = "X_4 + C3H8X <=> C3H7X + H*",
    degeneracy = 6.0,
    kinetics = SurfaceArrhenius(A=(2.71485e+17,'m^2/(mol*s)'), n=0, Ea=(0.999417,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNTIw""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: X + CH3CH2CH3X <=> HX + CH3CH2CH2X
equation : CH3CH2CH3* + * -> CH3CH2CH2* + H*,
dft_code : Quantum Espresso,
dftFunctional : BEEF-vdW,
pubId: WangTheory-aided2020,
reactionEnergy: 0.219812198280124 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles CCC from Thermo library: DFT_QCI_thermo and S298=66.07 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 69,
    label = "X_4 + C3H8X-2 <=> C3H7X-2 + H*",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.71485e+17,'m^2/(mol*s)'), n=0, Ea=(0.930462,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMyNTIx""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: X + CH3CH2CH3X <=> HX + CH3CHCH3X
equation : CH3CH2CH3* + * -> CH3CHCH3* + H*,
dft_code : Quantum Espresso,
dftFunctional : BEEF-vdW,
pubId: WangTheory-aided2020,
reactionEnergy: 0.2048776384035591 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles CCC from Thermo library: DFT_QCI_thermo and S298=66.07 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 70,
    label = "H* + NH2_X <=> NH3_X + X_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.70555e+18,'m^2/(mol*s)'), n=0, Ea=(1.36714,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMzMDky""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: HX + NH2X <=> X + NH3X
equation : NH2* + H* - 0* -> NH3* + *,
dft_code : Quantum Espresso,
dftFunctional : BEEF-vdW,
pubId: WangAchieving2021,
reactionEnergy: -0.037949881923850626 eV
A factor estimation:
A factor estimate for association
A factor estimated from gas-phase smiles N from Thermo library: primaryThermoLibrary and S298=45.99 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 71,
    label = "X_4 + H2O* <=> OH* + H*",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.4102e+16,'m^2/(mol*s)'), n=0, Ea=(0.9,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTM5Mw==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: H2OX + X <=> HX + OHX
equation : H2O* -> OH* + H*,
dft_code : DACAPO,
dftFunctional : RPBE,
pubId: WangUniversal2011,
reactionEnergy: 0.656 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles O from Thermo library: primaryThermoLibrary and S298=45.08 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 72,
    label = "X_4 + C2H6OX <=> C2H5OX + H*",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.91245e+17,'m^2/(mol*s)'), n=0, Ea=(0.864556,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI3NDM=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: X + CH3CH2OHX <=> HX + CH3CHOHX
equation : CH3CH2OH* + * -> CH3CHOH* + H*,
dft_code : Quantum ESPRESSO 5.1,
dftFunctional : BEEF-vdW,
pubId: SchumannSelectivity2018,
reactionEnergy: 0.0430737177376 eV
A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles CCO from Thermo library: DFT_QCI_thermo and S298=66.77 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 73,
    label = "H* + NH2_X <=> NH3_X + X_4",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(A=(1.70555e+18,'m^2/(mol*s)'), n=0, Ea=(1.18523,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMzMDY4""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: HX + NH2X <=> X + NH3X
equation : NH2* + H* - 0* -> NH3* + *
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangAchieving2021
reactionEnergy: -1.195591727097053 eV

A factor estimation:
A factor estimate for association
A factor estimated from gas-phase smiles N from Thermo library: primaryThermoLibrary and S298=45.99 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "211",
)

entry(
    index = 74,
    label = "X_4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(A=(2.89421e+16,'m^2/(mol*s)'), n=0, Ea=(2.53,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTE5Nw==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: NH3X + X <=> HX + NH2X
equation : NH3* -> NH2* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 1.107 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles N from Thermo library: primaryThermoLibrary and S298=45.99 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "211",
)

entry(
    index = 75,
    label = "X_4 + H2O* <=> OH* + H*",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.4102e+16,'m^2/(mol*s)'), n=0, Ea=(1.824,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTQwOA==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: H2OX + X <=> HX + OHX
equation : H2O* -> OH* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 0.955 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles O from Thermo library: primaryThermoLibrary and S298=45.08 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 76,
    label = "X_4 + C2H6OX <=> C2H5OX + H*",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.91245e+17,'m^2/(mol*s)'), n=0, Ea=(2.3661,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI3NDU=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: X + CH3CH2OHX <=> HX + CH3CHOHX
equation : CH3CH2OH* + * -> CH3CHOH* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: 2.03992916786 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles CCO from Thermo library: DFT_QCI_thermo and S298=66.77 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 77,
    label = "H* + NH2_X <=> NH3_X + X_4",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(A=(1.70555e+18,'m^2/(mol*s)'), n=0, Ea=(0.925966,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDMzMDMy""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Au
Original entry: HX + NH2X <=> X + NH3X
equation : NH2* + H* - 0* -> NH3* + *
dft_code : Quantum Espresso
dftFunctional : BEEF-vdW
pubId: WangAchieving2021
reactionEnergy: -1.2162486377928872 eV

A factor estimation:
A factor estimate for association
A factor estimated from gas-phase smiles N from Thermo library: primaryThermoLibrary and S298=45.99 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Au",
    facet = "211",
)

entry(
    index = 78,
    label = "X_4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    duplicate = True,
    kinetics = SurfaceArrhenius(A=(2.89421e+16,'m^2/(mol*s)'), n=0, Ea=(2.24,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTE5NQ==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Au
Original entry: NH3X + X <=> HX + NH2X
equation : NH3* -> NH2* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 1.02 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles N from Thermo library: primaryThermoLibrary and S298=45.99 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Au",
    facet = "211",
)

entry(
    index = 79,
    label = "X_4 + H2O* <=> OH* + H*",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.4102e+16,'m^2/(mol*s)'), n=0, Ea=(2.023,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTQxMQ==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Au
Original entry: H2OX + X <=> HX + OHX
equation : H2O* -> OH* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 1.584 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles O from Thermo library: primaryThermoLibrary and S298=45.08 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Au",
    facet = "111",
)

