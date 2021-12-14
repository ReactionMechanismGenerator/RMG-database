#!/usr/bin/env python
# encoding: utf-8

name = "Cation_NO_Ring_Opening/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "C2H4LiO <=> C2H4O + Li",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(7.79548e+09,'s^-1'), n=0.676137, Ea=(127.392,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=0.9429002183123382,B=0.4142522035781646,E=0.9271382422782674,L=0.5080999191526422,A=1.2701035125702795,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Li]OC[CH2] <=> [Lip] + O1CC1
""",
)

entry(
    index = 2,
    label = "C4H9LiN <=> C4H9N + Li",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(1.41052e+13,'s^-1'), n=-0.0966111, Ea=(37.9728,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=0.7063184659079954,B=0.6546888841685338,E=1.4167685288377097,L=7.086460323740072,A=0.6763993010322846,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Li]NCCC[CH2] <=> [Lip] + N1CCCC1
""",
)

entry(
    index = 3,
    label = "C6H12LiO <=> C6H12O + Li",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(685907,'s^-1'), n=0.809304, Ea=(91.8794,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.8745309700808286,B=0.6489379258617733,E=0.27349172242979114,L=6.280608540134562,A=0.35178208431790287,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Li]OCCCCC[CH2] <=> [Lip] + O1CCCCCC1
""",
)

entry(
    index = 4,
    label = "C4H8LiO <=> C4H8O + Li",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(9.68382e+12,'s^-1'), n=-0.0538311, Ea=(99.5874,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.975919765798433,B=0.5933221434562257,E=0.10249027371088437,L=4.734916369654065,A=0.4382337255257122,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Li]OCCC[CH2] <=> [Lip] + O1CCCC1
""",
)

