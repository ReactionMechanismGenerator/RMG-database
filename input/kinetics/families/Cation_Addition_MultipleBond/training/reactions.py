#!/usr/bin/env python
# encoding: utf-8

name = "Cation_Addition_MultipleBond/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "CH3LiN <=> CH3N + Li",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(5.3493e+15,'s^-1'), n=-0.259789, Ea=(57.8699,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=-2.65419313965326,B=1.2542197583042969,E=-0.21990942778263972,L=-9.14111680402368,A=3.645314481406821,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Li]N[CH2] <=> [Lip] + N=C
""",
)

entry(
    index = 2,
    label = "CH2LiO <=> CH2O + Li",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(5.12946e+16,'s^-1'), n=-0.125312, Ea=(91.4067,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=-0.4735938637413528,B=2.67486764340657,E=-5.09678040094995,L=-4.876934525239067,A=3.9944267641274602,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Li]O[CH2] <=> [Lip] + C=O
""",
)

entry(
    index = 3,
    label = "C3H4LiO3 <=> C3H4O3 + Li",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(1.54076e+14,'s^-1'), n=-0.182294, Ea=(23.9219,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=-2.018725993417632,B=4.93569039446143,E=-4.315782362402726,L=-1.68464261284562,A=3.5698295734222367,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Li]O[C]1OCCO1 <=> [Lip] + O=C1OCCO1
""",
)

