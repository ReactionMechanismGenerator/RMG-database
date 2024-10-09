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
    label = "C2H4O + Li <=> C2H4LiO",
    degeneracy = 2.0,
    kinetics = ArrheniusChargeTransfer(A=(8.85706e+08,'cm^3/(mol*s)'), n=1.77542, Ea=(-0.0494826,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=0.9429002183123382,B=0.4142522035781646,E=0.9271382422782674,L=0.5080999191526422,A=1.2701035125702795,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.16129, dn = +|- 0.0194768, dEa = +|- 0.111383 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Lip] + O1CC1 <=> [Li]OC[CH2]
""",
)

entry(
    index = 2,
    label = "C4H9N + Li <=> C4H9LiN",
    degeneracy = 2.0,
    kinetics = ArrheniusChargeTransfer(A=(7.84401e+06,'cm^3/(mol*s)'), n=2.34419, Ea=(76.6884,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=0.7063184659079954,B=0.6546888841685338,E=1.4167685288377097,L=7.086460323740072,A=0.6763993010322846,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.4264, dn = +|- 0.0462593, dEa = +|- 0.264544 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Lip] + N1CCCC1 <=> [Li]NCCC[CH2]
""",
)

entry(
    index = 3,
    label = "C6H12O + Li <=> C6H12LiO",
    degeneracy = 2.0,
    kinetics = ArrheniusChargeTransfer(A=(1.42961e+12,'cm^3/(mol*s)'), n=0.521642, Ea=(61.8184,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.8745309700808286,B=0.6489379258617733,E=0.27349172242979114,L=6.280608540134562,A=0.35178208431790287,comment=''), comment="""Fitted to 50 data points; dA = *|/ 3.24532, dn = +|- 0.153333, dEa = +|- 0.876872 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Lip] + O1CCCCCC1 <=> [Li]OCCCCC[CH2]
""",
)

entry(
    index = 4,
    label = "C4H8O + Li <=> C4H8LiO",
    degeneracy = 2.0,
    kinetics = ArrheniusChargeTransfer(A=(1.83813e+16,'cm^3/(mol*s)'), n=0.232048, Ea=(63.9513,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.975919765798433,B=0.5933221434562257,E=0.10249027371088437,L=4.734916369654065,A=0.4382337255257122,comment=''), comment="""Fitted to 50 data points; dA = *|/ 2.45172, dn = +|- 0.116808, dEa = +|- 0.667992 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Lip] + O1CCCC1 <=> [Li]OCCC[CH2]
""",
)

