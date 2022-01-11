#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Bidentate_Dissociation/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "CH2OX2 <=> OX + CH2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(2.827,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTM0NQ==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: OCH2X <=> OX + CH2X
equation : OCH2* -> CH2* + O*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 0.967 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 2,
    label = "C2HOX2 <=> CHX + COX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(0.587563,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI3NDc=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: CHCOX <=> CHX + COX
equation : CHCO* + * -> CH* + CO*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: -0.971622912111 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 3,
    label = "C2X2 <=> CX + CX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.44606,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NTU2""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: CCX <=> CX + CX
equation : CC* + * -> 2.0C*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: -0.6488743204099592 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 4,
    label = "C2H4X2 <=> CH2X-2 + CH2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(2.16968,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NTU4""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: CH2CH2X <=> CH2X + CH2X
equation : CH2CH2* + * -> 2.0CH2*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 1.1759970808634534 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 5,
    label = "C2H3X2 <=> CH2X-2 + CHX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.5494,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NTYx""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: CH2CHX <=> CHX + CH2X
equation : CH2CH* + * -> CH2* + CH*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.34357292045024224 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 6,
    label = "C2H2X2 <=> CHX + CHX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.71709,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NTgw""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: CHCHX <=> CHX + CHX
equation : CHCH* + * -> 2.0CH*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.03997719814651646 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 7,
    label = "C2HX2 <=> CHX + CX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.70036,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NTgz""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pd
Original entry: CHCX <=> CX + CHX
equation : CHC* + * -> CH* + C*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: -0.1582061083172448 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 8,
    label = "C2X2 <=> CX + CX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.74953,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NDg3""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ni
Original entry: CCX <=> CX + CX
equation : CC* + * -> 2.0C*,
dft_code : Quantum ESPRESSO 5.1,
dftFunctional : BEEF-vdW,
pubId: HansenFirst2018,
reactionEnergy: 0.6147098822402768 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 9,
    label = "C2H4X2 <=> CH2X-2 + CH2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.36642,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NDg5""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ni
Original entry: CH2CH2X <=> CH2X + CH2X
equation : CH2CH2* + * -> 2.0CH2*,
dft_code : Quantum ESPRESSO 5.1,
dftFunctional : BEEF-vdW,
pubId: HansenFirst2018,
reactionEnergy: 0.8267307222122326 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 10,
    label = "C2HX2 <=> CHX + CX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.55749,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NTE0""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ni
Original entry: CHCX <=> CX + CHX
equation : CHC* + * -> CH* + C*,
dft_code : Quantum ESPRESSO 5.1,
dftFunctional : BEEF-vdW,
pubId: HansenFirst2018,
reactionEnergy: 0.6411460828967392 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 11,
    label = "C2HOX2 <=> CHX + COX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(0.596339,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI3NDg=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ir
Original entry: CHCOX <=> CHX + COX
equation : CHCO* + * -> CH* + CO*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: -1.13389202037 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 12,
    label = "C2X2 <=> CX + CX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.1588,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NDA0""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ir
Original entry: CCX <=> CX + CX
equation : CC* + * -> 2.0C*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: -0.8858352111710701 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 13,
    label = "C2H4X2 <=> CH2X-2 + CH2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.68979,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NDA2""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ir
Original entry: CH2CH2X <=> CH2X + CH2X
equation : CH2CH2* + * -> 2.0CH2*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.4839631227077916 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 14,
    label = "C2H2X2-2 <=> CH2X-2 + CX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(2.33021,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NDEx""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ir
Original entry: CH2CX <=> CX + CH2X
equation : CH2C* + * -> CH2* + C*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.8390631260117516 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 15,
    label = "C2H2X2 <=> CHX + CHX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.33398,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NDI4""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ir
Original entry: CHCHX <=> CHX + CHX
equation : CHCH* + * -> 2.0CH*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: -0.3669100165425334 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 16,
    label = "C2HX2 <=> CHX + CX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.47737,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NDMx""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ir
Original entry: CHCX <=> CX + CHX
equation : CHC* + * -> CH* + C*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: -0.5147843020968139 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Ir",
    facet = "111",
)

entry(
    index = 17,
    label = "C2HX2 <=> CHX + CX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(2.8,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODU4""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: CCHX <=> CX + CHX
equation : CCH* -> CH* + C*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 1.892 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Cu",
    facet = "211",
)

entry(
    index = 18,
    label = "CH2NX2 <=> NX + CH2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(3.1,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTEwMw==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: CH2NX <=> NX + CH2X
equation : CH2N* -> CH2* + N*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 2.122 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Cu",
    facet = "211",
)

entry(
    index = 19,
    label = "CNX2 <=> NX + CX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(4.04,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTEwNw==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: CNX <=> CX + NX
equation : CN* -> C* + N*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 2.735 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Cu",
    facet = "211",
)

entry(
    index = 20,
    label = "CH3NX2 <=> HNX + CH2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(2.12,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTE0NQ==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: CH2NHX <=> NHX + CH2X
equation : CH2NH* -> CH2* + NH*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 1.327 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Cu",
    facet = "211",
)

entry(
    index = 21,
    label = "CH2NX2-2 <=> HNX + CHX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(2.63,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTE0OQ==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: CHNHX <=> CHX + NHX
equation : CHNH* -> CH* + NH*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 0.832 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Cu",
    facet = "211",
)

entry(
    index = 22,
    label = "CHNX2 <=> HNX + CX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(2.78,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTE1MQ==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: CNHX <=> CX + NHX
equation : CNH* -> NH* + C*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 1.41 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Cu",
    facet = "211",
)

entry(
    index = 23,
    label = "CHOX2 <=> OX + CHX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(2.302,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTMyNQ==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: OCHX <=> OX + CHX
equation : OCH* -> CH* + O*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 0.852 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Cu",
    facet = "211",
)

entry(
    index = 24,
    label = "CH2OX2 <=> OX + CH2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(2.437,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTMyOQ==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: OCH2X <=> OX + CH2X
equation : OCH2* -> CH2* + O*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 0.827 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Cu",
    facet = "211",
)

# entry(
#     index = 25,
#     label = "COX-2 + COX <=> C2O2X2",
#     degeneracy = 1.0,
#     kinetics = SurfaceArrhenius(A=(2.50073e+17,'m^2/(mol*s)'), n=0, Ea=(1.546,'eV/molecule'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """cathub_id:UmVhY3Rpb246MjM2MA==""",
#     longDesc = 
# """
# Training reaction from kinetics library: Surface/cathub/Cu
# Original entry: COX + COX <=> OCCOX
# equation : 2CO* -> OCCO*
# dft_code : DACAPO
# dftFunctional : RPBE
# pubId: MontoyaInsights2013
# reactionEnergy: 1.164 eV

# Could not determine reaction type estimating A = kb/298/h = 6.21e+12
# A/=2.483e-5 mol/m^2 (Pt111 site density)
# """,
#     metal = "Cu",
#     facet = "211",
# )
# poor thermo estimate (4.3 eV)

entry(
    index = 26,
    label = "C2HOX2 <=> CHX + COX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.7766,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI3NTI=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: CHCOX <=> CHX + COX
equation : CHCO* + * -> CH* + CO*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: 1.39871369587 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 27,
    label = "C2H4X2 <=> CH2X-2 + CH2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(2.24624,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4Mjk3""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: CH2CH2X <=> CH2X + CH2X
equation : CH2CH2* + * -> 2.0CH2*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 2.1042981073842384 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 28,
    label = "C2H3X2 <=> CH2X-2 + CHX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(2.02293,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MzAw""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: CHCH2X <=> CHX + CH2X
equation : CH2CH* + * -> CH2* + CH*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 1.7036713479319587 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 29,
    label = "C2H2X2-2 <=> CH2X-2 + CX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(2.93855,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MzAy""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: CCH2X <=> CX + CH2X
equation : CH2C* + * -> CH2* + C*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 2.4225787257310003 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 30,
    label = "C2H2X2 <=> CHX + CHX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(2.22937,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MzE5""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: CHCHX <=> CHX + CHX
equation : CHCH* + * -> 2.0CH*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 1.8374706126051024 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Cu",
    facet = "111",
)

entry(
    index = 31,
    label = "C2X2 <=> CX + CX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.96231,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MjQx""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Co
Original entry: CCX <=> CX + CX
equation : CC* + * -> 2.0C*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.7223596861877013 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Co",
    facet = "111",
)

entry(
    index = 32,
    label = "C2H4X2 <=> CH2X-2 + CH2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.39843,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MjQz""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Co
Original entry: CH2CH2X <=> CH2X + CH2X
equation : CH2CH2* + * -> 2.0CH2*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 1.3649094003485516 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Co",
    facet = "111",
)

entry(
    index = 33,
    label = "C2H2X2-2 <=> CH2X-2 + CX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.91497,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MjQ4""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Co
Original entry: CH2CX <=> CX + CH2X
equation : CH2C* + * -> CH2* + C*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 1.3397184606874362 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Co",
    facet = "111",
)

entry(
    index = 34,
    label = "C2HX2 <=> CHX + CX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.6,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODQ3""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Co
Original entry: CHCX <=> CX + CHX
equation : CCH* -> CH* + C*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: -0.148 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Co",
    facet = "211",
)

entry(
    index = 35,
    label = "C2X2 <=> CX + CX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.85683,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4ODQ5""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ru
Original entry: CCX <=> CX + CX
equation : CC* + * -> 2.0C*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: -0.5588730724994093 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Ru",
    facet = "001",
)

entry(
    index = 36,
    label = "C2HX2 <=> CHX + CX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.88,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODUz""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ru
Original entry: CHCX <=> CX + CHX
equation : CCH* -> CH* + C*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 0.032 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Ru",
    facet = "211",
)

entry(
    index = 37,
    label = "CHOX2 <=> OX + CHX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.1,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODQx""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ru
Original entry: OCHX <=> OX + CHX
equation : OCH* -> CH* + O*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: -0.878 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Ru",
    facet = "211",
)

entry(
    index = 38,
    label = "C2H2X2-2 <=> CH2X-2 + CX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.36,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODgz""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ru
Original entry: CH2CX <=> CX + CH2X
equation : CCH2* -> CH2* + C*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 0.047 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Ru",
    facet = "211",
)

entry(
    index = 39,
    label = "C2H3X2 <=> CH2X-2 + CHX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.45,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODg0""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ru
Original entry: CH2CHX <=> CHX + CH2X
equation : CHCH2* -> CH2* + CH*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: -0.411 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Ru",
    facet = "211",
)

entry(
    index = 40,
    label = "CNX2 <=> NX + CX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.88,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTA4MQ==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: CNX <=> CX + NX
equation : CN* -> C* + N*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 0.115 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 41,
    label = "CH2NX2 <=> NX + CH2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.95,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTA4Mw==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: CH2NX <=> NX + CH2X
equation : CH2N* -> CH2* + N*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: -0.178 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 42,
    label = "CHNX2 <=> HNX + CX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.5,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTEzMg==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: CNHX <=> CX + NHX
equation : CNH* -> NH* + C*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 0.16 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 43,
    label = "CH2NX2-2 <=> HNX + CHX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.54,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTEzMw==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: CHNHX <=> CHX + NHX
equation : CHNH* -> CH* + NH*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: -0.658 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 44,
    label = "CH3NX2 <=> HNX + CH2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.91,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTE0MA==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: CH2NHX <=> NHX + CH2X
equation : CH2NH* -> CH2* + NH*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 0.017 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 45,
    label = "CHOX2 <=> OX + CHX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.532,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTMwNA==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: OCHX <=> OX + CHX
equation : OCH* -> CH* + O*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: -0.458 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 46,
    label = "CH2OX2 <=> OX + CH2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.737,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTMwOA==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: OCH2X <=> OX + CH2X
equation : OCH2* -> CH2* + O*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: -0.373 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Rh",
    facet = "211",
)

entry(
    index = 47,
    label = "C2HOX2 <=> CHX + COX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(0.385454,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI3NTA=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: CHCOX <=> CHX + COX
equation : CHCO* + * -> CH* + CO*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: -0.957455644646 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 48,
    label = "C2X2 <=> CX + CX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.53126,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4ODA1""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: CCX <=> CX + CX
equation : CC* + * -> 2.0C*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: -0.20608154707588255 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 49,
    label = "C2H4X2 <=> CH2X-2 + CH2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.54306,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4ODA3""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: CH2CH2X <=> CH2X + CH2X
equation : CH2CH2* + * -> 2.0CH2*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.6322633344680071 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 50,
    label = "C2H3X2 <=> CH2X-2 + CHX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.0664,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4ODEw""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: CHCH2X <=> CHX + CH2X
equation : CH2CH* + * -> CH2* + CH*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: -0.0399247482419014 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 51,
    label = "C2H2X2-2 <=> CH2X-2 + CX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(2.18214,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4ODEy""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: CCH2X <=> CX + CH2X
equation : CH2C* + * -> CH2* + C*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 0.9910055136424489 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 52,
    label = "C2H2X2 <=> CHX + CHX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.30823,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4ODI5""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: CHCHX <=> CHX + CHX
equation : CHCH* + * -> 2.0CH*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: -0.1761777995270677 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 53,
    label = "C2HX2 <=> CHX + CX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.23943,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4ODMy""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: CCHX <=> CX + CHX
equation : CHC* + * -> CH* + C*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: -0.11343780157039873 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 54,
    label = "CH2NX2 <=> NX + CH2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(2.78,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTA5Ng==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: CH2NX <=> NX + CH2X
equation : CH2N* -> CH2* + N*,
dft_code : DACAPO,
dftFunctional : RPBE,
pubId: WangUniversal2011,
reactionEnergy: 0.632 eV
Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 55,
    label = "CNX2 <=> NX + CX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(2.89,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTA5Nw==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: CNX <=> CX + NX
equation : CN* -> C* + N*,
dft_code : DACAPO,
dftFunctional : RPBE,
pubId: WangUniversal2011,
reactionEnergy: 1.025 eV
Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 56,
    label = "CH3NX2 <=> HNX + CH2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.96,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTE0Mg==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: CH2NHX <=> NHX + CH2X
equation : CH2NH* -> CH2* + NH*,
dft_code : DACAPO,
dftFunctional : RPBE,
pubId: WangUniversal2011,
reactionEnergy: 0.307 eV
Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 57,
    label = "CH2NX2-2 <=> HNX + CHX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(2.74,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTE1MA==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: CHNHX <=> CHX + NHX
equation : CHNH* -> CH* + NH*,
dft_code : DACAPO,
dftFunctional : RPBE,
pubId: WangUniversal2011,
reactionEnergy: 0.062 eV
Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 58,
    label = "CHNX2 <=> HNX + CX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(2.95,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTE1Mg==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: CNHX <=> CX + NHX
equation : CNH* -> NH* + C*,
dft_code : DACAPO,
dftFunctional : RPBE,
pubId: WangUniversal2011,
reactionEnergy: 1.16 eV
Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 59,
    label = "CH2OX2 <=> OX + CH2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.937,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTMxOA==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: OCH2X <=> OX + CH2X
equation : OCH2* -> CH2* + O*,
dft_code : DACAPO,
dftFunctional : RPBE,
pubId: WangUniversal2011,
reactionEnergy: 0.337 eV
Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 60,
    label = "CHOX2 <=> OX + CHX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(3.112,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTM1Mw==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: OCHX <=> OX + CHX
equation : OCH* -> CH* + O*,
dft_code : DACAPO,
dftFunctional : RPBE,
pubId: WangUniversal2011,
reactionEnergy: 0.862 eV
Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 61,
    label = "C2HOX2 <=> CHX + COX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(0.924194,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI3NDk=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: CHCOX <=> CHX + COX
equation : CHCO* + * -> CH* + CO*,
dft_code : Quantum ESPRESSO 5.1,
dftFunctional : BEEF-vdW,
pubId: SchumannSelectivity2018,
reactionEnergy: -0.702005298022 eV
Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 62,
    label = "C2H4X2 <=> CH2X-2 + CH2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(2.29865,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NzE2""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: CH2CH2X <=> CH2X + CH2X
equation : CH2CH2* + * -> 2.0CH2*,
dft_code : Quantum ESPRESSO 5.1,
dftFunctional : BEEF-vdW,
pubId: HansenFirst2018,
reactionEnergy: 0.7757300559314899 eV
Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 63,
    label = "C2H3X2 <=> CH2X-2 + CHX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.6561,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NzE5""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: CH2CHX <=> CHX + CH2X
equation : CH2CH* + * -> CH2* + CH*,
dft_code : Quantum ESPRESSO 5.1,
dftFunctional : BEEF-vdW,
pubId: HansenFirst2018,
reactionEnergy: 0.045708800229476765 eV
Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 64,
    label = "C2H2X2-2 <=> CH2X-2 + CX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(2.51988,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NzIx""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: CCH2X <=> CX + CH2X
equation : CH2C* + * -> CH2* + C*,
dft_code : Quantum ESPRESSO 5.1,
dftFunctional : BEEF-vdW,
pubId: HansenFirst2018,
reactionEnergy: 0.8273730469809379 eV
Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 65,
    label = "C2H2X2 <=> CHX + CHX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.61237,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NzM4""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: CHCHX <=> CHX + CHX
equation : CHCH* + * -> 2.0CH*,
dft_code : Quantum ESPRESSO 5.1,
dftFunctional : BEEF-vdW,
pubId: HansenFirst2018,
reactionEnergy: -0.46949537354521453 eV
Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 66,
    label = "C2HX2 <=> CHX + CX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(1.37959,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4NzQx""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Pt
Original entry: CCHX <=> CX + CHX
equation : CHC* + * -> CH* + C*,
dft_code : Quantum ESPRESSO 5.1,
dftFunctional : BEEF-vdW,
pubId: HansenFirst2018,
reactionEnergy: -0.6997383855632506 eV
Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 67,
    label = "C2HX2 <=> CHX + CX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(4.16,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODY0""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: CCHX <=> CX + CHX
equation : CCH* -> CH* + C*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 3.412 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Ag",
    facet = "211",
)

entry(
    index = 68,
    label = "C2H3X2 <=> CH2X-2 + CHX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(3.98,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246OTA3""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: CHCH2X <=> CHX + CH2X
equation : CHCH2* -> CH2* + CH*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 3.329 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Ag",
    facet = "211",
)

entry(
    index = 69,
    label = "CH2NX2 <=> NX + CH2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(4.34,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTExMQ==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: CH2NX <=> NX + CH2X
equation : CH2N* -> CH2* + N*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 3.582 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Ag",
    facet = "211",
)

entry(
    index = 70,
    label = "CNX2 <=> NX + CX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(6.3,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTExNA==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: CNX <=> CX + NX
equation : CN* -> C* + N*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 5.335 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Ag",
    facet = "211",
)

entry(
    index = 71,
    label = "CH3NX2 <=> HNX + CH2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(3.48,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTE1NA==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: CH2NHX <=> NHX + CH2X
equation : CH2NH* -> CH2* + NH*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 2.877 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Ag",
    facet = "211",
)

entry(
    index = 72,
    label = "CH2NX2-2 <=> HNX + CHX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(3.81,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTE1NQ==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: CHNHX <=> CHX + NHX
equation : CHNH* -> CH* + NH*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 2.742 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Ag",
    facet = "211",
)

entry(
    index = 73,
    label = "CHNX2 <=> HNX + CX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(4.85,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTE1Ng==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: CNHX <=> CX + NHX
equation : CNH* -> NH* + C*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 3.64 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Ag",
    facet = "211",
)

entry(
    index = 74,
    label = "CH2OX2 <=> OX + CH2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(3.727,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTM1OQ==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: OCH2X <=> OX + CH2X
equation : OCH2* -> CH2* + O*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 2.607 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Ag",
    facet = "211",
)

entry(
    index = 75,
    label = "CHOX2 <=> OX + CHX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(3.882,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTM2MA==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: OCHX <=> OX + CHX
equation : OCH* -> CH* + O*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 2.952 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Ag",
    facet = "211",
)

entry(
    index = 76,
    label = "C2HOX2 <=> CHX + COX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(2.84156,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246ODI3NTE=""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: CHCOX <=> CHX + COX
equation : CHCO* + * -> CH* + CO*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: SchumannSelectivity2018
reactionEnergy: 2.66161965474 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 77,
    label = "C2H2X2-2 <=> CH2X-2 + CX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(4.16572,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MTQ3""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Ag
Original entry: CCH2X <=> CX + CH2X
equation : CH2C* + * -> CH2* + C*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 3.7010112287825905 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 78,
    label = "C2H3X2 <=> CH2X-2 + CHX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(3.61,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246OTA1""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Au
Original entry: CHCH2X <=> CHX + CH2X
equation : CHCH2* -> CH2* + CH*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 2.379 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Au",
    facet = "211",
)

entry(
    index = 79,
    label = "CHOX2 <=> OX + CHX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(4.622,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MTM2MQ==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Au
Original entry: OCHX <=> OX + CHX
equation : OCH* -> CH* + O*
dft_code : DACAPO
dftFunctional : RPBE
pubId: WangUniversal2011
reactionEnergy: 3.382 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Au",
    facet = "211",
)

entry(
    index = 80,
    label = "C2X2 <=> CX + CX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(3.98702,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MTg0""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Au
Original entry: CCX <=> CX + CX
equation : CC* + * -> 2.0C*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 3.026444802977494 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Au",
    facet = "111",
)

entry(
    index = 81,
    label = "C2H2X2-2 <=> CH2X-2 + CX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(3.68195,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MTkx""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Au
Original entry: CCH2X <=> CX + CH2X
equation : CH2C* + * -> CH2* + C*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 2.9649712228710996 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Au",
    facet = "111",
)

entry(
    index = 82,
    label = "C2H2X2 <=> CHX + CHX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(2.90466,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MjA4""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Au
Original entry: CHCHX <=> CHX + CHX
equation : CHCH* + * -> 2.0CH*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 2.211042316397652 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Au",
    facet = "111",
)

entry(
    index = 83,
    label = "C2HX2 <=> CHX + CX-2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.20932e+12,'s^-1'), n=0, Ea=(3.69633,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246MzM4MjEx""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Au
Original entry: CCHX <=> CX + CHX
equation : CHC* + * -> CH* + C*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: HansenFirst2018
reactionEnergy: 2.85651099588722 eV

Could not determine reaction type estimating A = kb/298/h = 6.21e+12
""",
    metal = "Au",
    facet = "111",
)

