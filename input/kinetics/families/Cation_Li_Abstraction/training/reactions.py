#!/usr/bin/env python
# encoding: utf-8

name = "Cation_Li_Abstraction/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "CH4 + Li <=> CH3 + HLi",
    degeneracy = 4.0,
    kinetics = ArrheniusChargeTransfer(A=(678680,'cm^3/(mol*s)'), n=3.09275, Ea=(215.149,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=3.39470212956669,B=1.6022203760198037,E=1.4946262264125265,L=10.49010693814182,A=0.4943151788298517,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.37586, dn = +|- 0.0415605, dEa = +|- 0.237673 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Lip] + C <=> [CH3] + [Li][H]
""",
)

entry(
    index = 2,
    label = "CH3F + Li <=> CH3 + FLi",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(3.29871e+08,'cm^3/(mol*s)'), n=2.2276, Ea=(25.9849,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=1.8681935378213759,B=2.373498032935028,E=0.32859248603303737,L=5.004153890392606,A=0.8849787213003473,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.4013, dn = +|- 0.043947, dEa = +|- 0.251321 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Lip] + CF <=> [CH3] + [Li]F
""",
)

entry(
    index = 3,
    label = "CH3Cl + Li <=> CH3 + ClLi",
    degeneracy = 1.0,
    kinetics = ArrheniusChargeTransfer(A=(4.26472e+09,'cm^3/(mol*s)'), n=1.78731, Ea=(-2.88557,'kJ/mol'), V0=(0,'V'), alpha=0.5, electrons=1, T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K'), solute=SoluteData(S=2.40096476096442,B=0.7611537028291462,E=0.36695032193123533,L=5.182274882516309,A=0.578711830957878,comment=''), comment="""Fitted to 50 data points; dA = *|/ 1.33939, dn = +|- 0.0380613, dEa = +|- 0.217662 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: LithiumPrimaryChargedKinetics
Original entry: [Lip] + CCl <=> [CH3] + [Li]Cl
""",
)

