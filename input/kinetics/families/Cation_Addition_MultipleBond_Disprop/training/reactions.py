#!/usr/bin/env python
# encoding: utf-8

name = "Cation_Addition_MultipleBond_Disprop/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "C2H4 + CLi2O3 <=> C3H4LiO3 + Li",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(6661.95,'cm^3/(mol*s)'), n=3.71305, Ea=(388.332,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.45971, dn = +|- 0.0492658, dEa = +|- 0.281738 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: C=C + [Li]OC(=O)O[Li] <=> [Li]OC(=O)OC[CH2] + [Lip]
""",
)

entry(
    index = 2,
    label = "C2H4 + C2H2LiN <=> C4H6N + Li",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(1.4351e+11,'cm^3/(mol*s)'), n=0.390187, Ea=(78.6676,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.50455, dn = +|- 0.053207, dEa = +|- 0.304276 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: C=C + [Li]N=C=C <=> N#CCC[CH2] + [Lip]
""",
)

entry(
    index = 3,
    label = "C2H4 + CHLiO2 <=> C3H5O2 + Li",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(22436.6,'cm^3/(mol*s)'), n=2.86799, Ea=(369.908,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.21068, dn = +|- 0.0249013, dEa = +|- 0.142403 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: C=C + [Li]OC=O <=> O=COC[CH2] + [Lip]
""",
)

entry(
    index = 4,
    label = "CH2O + C2H3LiO <=> C3H5O2-2 + Li",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(5.09692e+06,'cm^3/(mol*s)'), n=2.38467, Ea=(267.373,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.45221, dn = +|- 0.0485949, dEa = +|- 0.277901 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: O=C + [Li]OC=C <=> O=CCC[O] + [Lip]
""",
)

entry(
    index = 5,
    label = "CH3N + C2H4LiN <=> C3H7N2 + Li",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(42161.9,'cm^3/(mol*s)'), n=1.95149, Ea=(71.888,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.23386, dn = +|- 0.0273716, dEa = +|- 0.156531 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: N=C + [Li]NC=C <=> N=CCN[CH2] + [Lip]
""",
)

entry(
    index = 6,
    label = "C2H4 + C2H5LiO2S <=> C4H9O2S + Li",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(3.35882e+07,'cm^3/(mol*s)'), n=2.16634, Ea=(158.755,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.12791, dn = +|- 0.0156776, dEa = +|- 0.089656 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: C=C + [Li]OS(=O)(=C)C <=> O=S(=O)(C)CC[CH2] + [Lip]
""",
)

entry(
    index = 7,
    label = "C2H4 + C3H5LiO3 <=> C5H9O3 + Li",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(129163,'cm^3/(mol*s)'), n=3.08128, Ea=(410.714,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.46068, dn = +|- 0.049352, dEa = +|- 0.282231 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: C=C + [Li]OC(=O)OCC <=> CCOC(=O)OC[CH2] + [Lip]
""",
)

