#!/usr/bin/env python
# encoding: utf-8

name = "Cation_Li_Abstraction/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "HLi + CH3 <=> CH4 + Li",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(79732.1,'cm^3/(mol*s)'), n=2.61156, Ea=(12.1363,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=3.39470212956669,B=1.6022203760198037,E=1.4946262264125265,L=10.49010693814182,A=0.4943151788298517,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [CH3] + [Li][H] <=> [Lip] + C
""",
)

entry(
    index = 2,
    label = "FLi + CH3 <=> CH3F + Li",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(4.14134e+06,'cm^3/(mol*s)'), n=2.18948, Ea=(140.779,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.8681935378213759,B=2.373498032935028,E=0.32859248603303737,L=5.004153890392606,A=0.8849787213003473,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [CH3] + [Li]F <=> [Lip] + CF
""",
)

entry(
    index = 3,
    label = "ClLi + CH3 <=> CH3Cl + Li",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(1.57736e+07,'cm^3/(mol*s)'), n=1.91726, Ea=(119.96,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=2.40096476096442,B=0.7611537028291462,E=0.36695032193123533,L=5.182274882516309,A=0.578711830957878,comment='')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [CH3] + [Li]Cl <=> [Lip] + CCl
""",
)

