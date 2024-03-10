#!/usr/bin/env python
# encoding: utf-8

name = "Cation_Addition_MultipleBond/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "CH3N + Li <=> CH3LiN",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(1.6042e+10,'cm^3/(mol*s)'), n=1.52384, Ea=(2.76381,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=-2.65419313965326,B=1.2542197583042969,E=-0.21990942778263972,L=-9.14111680402368,A=3.645314481406821,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.04604, dn = +|- 0.00586241, dEa = +|- 0.0335255 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Lip] + N=C <=> [Li]N[CH2]
""",
)

entry(
    index = 2,
    label = "CH2O + Li <=> CH2LiO",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(5.0006e+11,'cm^3/(mol*s)'), n=1.50675, Ea=(-0.985354,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=-0.4735938637413528,B=2.67486764340657,E=-5.09678040094995,L=-4.876934525239067,A=3.9944267641274602,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.03252, dn = +|- 0.00416775, dEa = +|- 0.0238342 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Lip] + C=O <=> [Li]O[CH2]
""",
)

entry(
    index = 3,
    label = "C3H4O3 + Li <=> C3H4LiO3",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(3.0368e+08,'cm^3/(mol*s)'), n=1.59181, Ea=(-29.6323,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=-2.018725993417632,B=4.93569039446143,E=-4.315782362402726,L=-1.68464261284562,A=3.5698295734222367,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.03673, dn = +|- 0.0046983, dEa = +|- 0.0268683 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Lip] + O=C1OCCO1 <=> [Li]O[C]1OCCO1
""",
)

