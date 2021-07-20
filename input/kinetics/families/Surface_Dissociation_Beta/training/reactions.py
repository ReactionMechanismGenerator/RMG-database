#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_Beta/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 27,
    label = "CO* + H* <=> COH* + Cu",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (3.799e17, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (2.26, 'eV/molecule'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 27 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/c s200055d

A factor from paper / surface site density of Cu
1.118e13 1/s / 2.943e‐5 mol/m^2 = 3.799e17 m^2/(mol*s)
Erxn = 1.15 eV
""",
    metal = "Cu",
)

entry(
    index = 29,
    label = "HCO* + H* <=> HCOH* + Cu",
    degeneracy = 4,
    kinetics = SurfaceArrhenius(
        A = (3.048e17, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (0.91, 'eV/molecule'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 29 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/c s200055d

A factor from paper / surface site density of Cu
8.971e12 1/s / 2.943e‐5 mol/m^2 = 3.048e17 m^2/(mol*s)
Erxn = 0.09 eV
""",
    metal = "Cu",
)
entry(
    index = 30,
    label = "Cu + COH* <=> CO* + H*",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(8.82294e+16,'m^2/(mol*s)'), n=0, Ea=(0.73658,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246OTgz""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Cu
Original entry: COHX + X <=> HX + COX
equation : COH* -> CO* + H*
dft_code : DACAPO
dftFunctional : RPBE
pubId: BehrensThe2012
reactionEnergy: -1.38782 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [C-]=[OH+] from Thermo library: DFT_QCI_thermo + radical(Cs_P) and S298=56.31 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Cu",
    facet = "211",
)

entry(
    index = 31,
    label = "Cu + COH* <=> CO* + H*",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(8.82294e+16,'m^2/(mol*s)'), n=0, Ea=(1.21464,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDA5Nw==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: X + COHX <=> HX + COX
equation : COH* + * -> CO* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: YangIntrinsic2016
reactionEnergy: -0.733560028253 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [C-]=[OH+] from Thermo library: DFT_QCI_thermo + radical(Cs_P) and S298=56.31 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 32,
    label = "Cu + HCOH* <=> HCO* + H*",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.16208e+17,'m^2/(mol*s)'), n=0, Ea=(0.833567,'eV/molecule'), T0=(1,'K')),
    rank = 3,
    shortDesc = """cathub_id:UmVhY3Rpb246NDEyNw==""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/cathub/Rh
Original entry: X + CHOHX <=> HX + CHOX
equation : CHOH* + * -> CHO* + H*
dft_code : Quantum ESPRESSO 5.1
dftFunctional : BEEF-vdW
pubId: YangIntrinsic2016
reactionEnergy: -0.44748272351 eV

A factor estimation:
A factor estimate for dissociation
A factor estimated from gas-phase smiles [CH]O from Thermo library: DFT_QCI_thermo and S298=58.32 cal/mol/K
A/=2.483e-5 mol/m^2 (Pt111 site density)
""",
    metal = "Rh",
    facet = "111",
)

