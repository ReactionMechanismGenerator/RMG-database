#!/usr/bin/env python
# encoding: utf-8

name = "Cation_Addition_MultipleBond_Disprop/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "C3H4LiO3 + Li <=> CLi2O3 + C2H4",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(2.23949e+06,'cm^3/(mol*s)'), n=2.34337, Ea=(16.2698,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=-1.3791416734787092,B=0.9825775784337702,E=1.344561385839825,L=1.6867692078977448,A=2.9918711355986547,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Li]OC(=O)OC[CH2] + [Lip] <=> C=C + [Li]OC(=O)O[Li]
""",
)

entry(
    index = 2,
    label = "C4H6N + Li <=> C2H2LiN + C2H4",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(162517,'cm^3/(mol*s)'), n=2.55635, Ea=(59.4607,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: N#CCC[CH2] + [Lip] <=> C=C + [Li]N=C=C
""",
)

entry(
    index = 3,
    label = "C3H5O2 + Li <=> CHLiO2 + C2H4",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(419384,'cm^3/(mol*s)'), n=2.21898, Ea=(48.2832,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=2.0247091484586592,B=2.5777645372278832,E=0.3431344611927818,L=9.346538089381045,A=0.8860009592023523,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: O=COC[CH2] + [Lip] <=> C=C + [Li]OC=O
""",
)

entry(
    index = 4,
    label = "C3H5O2-2 + Li <=> C2H3LiO + CH2O",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(1.74272e+07,'cm^3/(mol*s)'), n=2.05933, Ea=(-27.3358,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=3.2490249849978214,B=2.6960753668589854,E=2.1706425235190108,L=14.985510873166351,A=0.7334126588566799,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: O=CCC[O] + [Lip] <=> O=C + [Li]OC=C
""",
)

entry(
    index = 5,
    label = "C3H7N2 + Li <=> C2H4LiN + CH3N",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(2.45437e+09,'cm^3/(mol*s)'), n=0.869935, Ea=(-36.817,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: N=CCN[CH2] + [Lip] <=> N=C + [Li]NC=C
""",
)

entry(
    index = 6,
    label = "C4H9O2S + Li <=> C2H5LiO2S + C2H4",
    degeneracy = 2.0,
    kinetics = ArrheniusChargeTransfer(A=(312580,'cm^3/(mol*s)'), n=2.72776, Ea=(68.0852,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: O=S(=O)(C)CC[CH2] + [Lip] <=> C=C + [Li]OS(=O)(=C)C
""",
)

entry(
    index = 7,
    label = "C5H9O3 + Li <=> C3H5LiO3 + C2H4",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(9.5603e+07,'cm^3/(mol*s)'), n=1.70021, Ea=(38.7352,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.1943783976602214,B=0.894154843812189,E=5.394280864555017,L=8.956244842828797,A=0.23494209646668668,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: CCOC(=O)OC[CH2] + [Lip] <=> C=C + [Li]OC(=O)OCC
""",
)

