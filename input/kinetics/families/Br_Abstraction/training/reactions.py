#!/usr/bin/env python
# encoding: utf-8

name = "Br_Abstraction/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "CH3 + C2H5BrO <=> C2H5O + CH3Br",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8089.06,'cm^3/(mol*s)'), n=2.74525, Ea=(36.8683,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.10307, dn = +|- 0.0128876, dEa = +|- 0.0701337 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_abstraction
Original entry: [CH3] + CC(O)Br <=> CBr + C[CH]O
""",
)

entry(
    index = 1,
    label = "H + C2H3BrO <=> C2H3O + BrH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.82335e+09,'cm^3/(mol*s)'), n=1.55333, Ea=(-0.0243267,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.0154, dn = +|- 0.00200734, dEa = +|- 0.0109239 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_abstraction
Original entry: [H] + CDCOBr <=> Br + CDC[O]
""",
)

entry(
    index = 2,
    label = "CH3 + C3H5Br <=> C3H5 + CH3Br",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(71360.1,'cm^3/(mol*s)'), n=2.71607, Ea=(61.4249,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.11667, dn = +|- 0.0144981, dEa = +|- 0.078898 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_abstraction
Original entry: [CH3] + CDC(C)Br <=> CBr + CD[C]C
""",
)

entry(
    index = 3,
    label = "H + CH2BrO <=> CH2O + BrH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.49752e+08,'cm^3/(mol*s)'), n=1.64303, Ea=(27.2099,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.05278, dn = +|- 0.006758, dEa = +|- 0.0367768 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_abstraction
Original entry: [H] + O[CH]Br <=> Br + [CH]O
""",
)

entry(
    index = 4,
    label = "H + CH3BrO <=> CH3O + BrH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.70556e+09,'cm^3/(mol*s)'), n=1.56225, Ea=(0.960606,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.01989, dn = +|- 0.00258766, dEa = +|- 0.0140819 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_abstraction
Original entry: [H] + COBr <=> Br + C[O]
""",
)

entry(
    index = 5,
    label = "H + CH2BrCl <=> CH2Cl + BrH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.71066e+08,'cm^3/(mol*s)'), n=1.71693, Ea=(17.9864,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.08099, dn = +|- 0.0102314, dEa = +|- 0.055679 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_abstraction
Original entry: [H] + ClCBr <=> Br + [CH2]Cl
""",
)

entry(
    index = 6,
    label = "CH3 + CH2BrCl <=> CH2Cl + CH3Br",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5568.38,'cm^3/(mol*s)'), n=2.8146, Ea=(38.4395,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.07781, dn = +|- 0.00984477, dEa = +|- 0.0535749 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_abstraction
Original entry: [CH3] + ClCBr <=> CBr + [CH2]Cl
""",
)

entry(
    index = 7,
    label = "CH3 + CH2BrO <=> CH2O + CH3Br",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(16992.4,'cm^3/(mol*s)'), n=2.72405, Ea=(61.5439,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.10261, dn = +|- 0.012833, dEa = +|- 0.0698367 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_abstraction
Original entry: [CH3] + O[CH]Br <=> CBr + [CH]O
""",
)

entry(
    index = 8,
    label = "H + C2H4Br <=> C2H4 + BrH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.97056e+08,'cm^3/(mol*s)'), n=1.64084, Ea=(25.8924,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.04947, dn = +|- 0.0063437, dEa = +|- 0.0345222 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_abstraction
Original entry: [H] + C[CH]Br <=> Br + [CH]C
""",
)

entry(
    index = 9,
    label = "H + CH2BrO2 <=> CH2O2 + BrH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.79761e+08,'cm^3/(mol*s)'), n=1.67816, Ea=(44.0004,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.06021, dn = +|- 0.00768142, dEa = +|- 0.041802 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_abstraction
Original entry: [H] + O[C](O)Br <=> Br + O[C]O
""",
)

entry(
    index = 10,
    label = "CH3 + C3H3Br <=> C3H3 + CH3Br",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6841.22,'cm^3/(mol*s)'), n=2.86155, Ea=(40.7809,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.0622, dn = +|- 0.0079277, dEa = +|- 0.0431423 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_abstraction
Original entry: [CH3] + CDCDCBr <=> CBr + C#C[CH2]
""",
)

entry(
    index = 11,
    label = "H + C2H2Br <=> C2H2 + BrH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.62575e+09,'cm^3/(mol*s)'), n=1.23946, Ea=(58.7276,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.07686, dn = +|- 0.0097281, dEa = +|- 0.05294 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_abstraction
Original entry: [H] + CD[C]Br <=> Br + [C]DC
""",
)

entry(
    index = 12,
    label = "CH3 + C2H4Br <=> C2H4 + CH3Br",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(29124.5,'cm^3/(mol*s)'), n=2.69164, Ea=(59.2465,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.12363, dn = +|- 0.0153138, dEa = +|- 0.0833369 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_abstraction
Original entry: [CH3] + C[CH]Br <=> CBr + [CH]C
""",
)

entry(
    index = 13,
    label = "CH3 + CH2BrO2 <=> CH2O2 + CH3Br",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(74186.8,'cm^3/(mol*s)'), n=2.6667, Ea=(80.1698,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.12924, dn = +|- 0.0159688, dEa = +|- 0.0869015 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_abstraction
Original entry: [CH3] + O[C](O)Br <=> CBr + O[C]O
""",
)


entry(
    index = 15,
    label = "CH3 + C2H4BrO <=> C2H4O + CH3Br",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(24450.5,'cm^3/(mol*s)'), n=2.62586, Ea=(61.1657,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.13841, dn = +|- 0.017031, dEa = +|- 0.0926819 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_abstraction
Original entry: [CH3] + C[C](O)Br <=> CBr + C[C]O
""",
)

entry(
    index = 16,
    label = "H + C4H9Br <=> C4H9 + BrH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.50121e+08,'cm^3/(mol*s)'), n=1.74726, Ea=(21.8677,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.09108, dn = +|- 0.0114517, dEa = +|- 0.0623198 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_abstraction
Original entry: [H] + CC(C)CBr <=> Br + [CH2]C(C)C
""",
)

entry(
    index = 17,
    label = "H + CH3Br-2 <=> CH3-2 + BrH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.05119e+08,'cm^3/(mol*s)'), n=1.83231, Ea=(22.8571,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.12299, dn = +|- 0.0152394, dEa = +|- 0.0829323 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_abstraction
Original entry: [H] + CBr <=> Br + [CH3]
""",
)

entry(
    index = 18,
    label = "H + C3H7Br <=> C3H7 + BrH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.15712e+10,'cm^3/(mol*s)'), n=0.78916, Ea=(20.2164,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.10457, dn = +|- 0.013066, dEa = +|- 0.0711049 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_abstraction
Original entry: [H] + CCCBr <=> Br + [CH2]CC
""",
)

entry(
    index = 19,
    label = "CH3 + CH3BrO-2 <=> CH3O-2 + CH3Br",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(249400,'cm^3/(mol*s)'), n=1.79792, Ea=(41.307,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.0848, dn = +|- 0.0106935, dEa = +|- 0.0581936 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_abstraction
Original entry: [CH3] + OCBr <=> CBr + [CH2]O
""",
)

entry(
    index = 20,
    label = "H + Br2 <=> BrH + Br",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.28e+11,'cm^3/(mol*s)'), n=1, Ea=(440,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is H + BR2 <=> HBR + BR""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: H + BR2 <=> HBR + BR
""",
)

entry(
    index = 21,
    label = "H + CH3Br-2 <=> BrH + CH3-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.11e+13,'cm^3/(mol*s)'), n=0, Ea=(5840,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is H + CH3BR <=> HBR + CH3""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: H + CH3BR <=> HBR + CH3
""",
)

entry(
    index = 22,
    label = "CH3 + Br2 <=> CH3Br + Br",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.21e+13,'cm^3/(mol*s)'), n=0, Ea=(-390,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is BR2 + CH3 <=> BR + CH3BR""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: BR2 + CH3 <=> BR + CH3BR
""",
)

entry(
    index = 23,
    label = "C2H3-2 + Br2 <=> C2H3Br-2 + Br",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.4e+13,'cm^3/(mol*s)'), n=0, Ea=(-572,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is BR2 + C2H3 <=> BR + C2H3BR""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: BR2 + C2H3 <=> BR + C2H3BR
""",
)

entry(
    index = 24,
    label = "C2H5-2 + Br2 <=> C2H5Br-2 + Br",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.57e+13,'cm^3/(mol*s)'), n=0, Ea=(-820,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is BR2 + C2H5 <=> BR + C2H5BR""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: BR2 + C2H5 <=> BR + C2H5BR
""",
)

entry(
    index = 25,
    label = "CF3-2 + Br2 <=> CBrF3-2 + Br",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.21e+12,'cm^3/(mol*s)'), n=0, Ea=(240,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is BR2 + CF3 <=> BR + CF3BR""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: BR2 + CF3 <=> BR + CF3BR
""",
)

entry(
    index = 26,
    label = "O + CBrF3 <=> BrO + CF3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9e+12,'cm^3/(mol*s)'), n=0, Ea=(13510,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is O + CF3BR <=> BRO + CF3""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: O + CF3BR <=> BRO + CF3
""",
)

entry(
    index = 27,
    label = "O + CH3Br-2 <=> BrO + CH3-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(13500,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is CH3BR + O <=> CH3 + BRO""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: CH3BR + O <=> CH3 + BRO
""",
)

entry(
    index = 28,
    label = "Br-2 + CH2Br <=> Br2-2 + CH2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5e+09,'cm^3/(mol*s)'), n=0, Ea=(10200,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is BR + CH2BR <=> BR2 + CH2""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: BR + CH2BR <=> BR2 + CH2
""",
)

entry(
    index = 29,
    label = "HO + CBrF3 <=> BrHO + CF3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(18000,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is OH + CF3BR <=> CF3 + BROH""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: OH + CF3BR <=> CF3 + BROH
""",
)

entry(
    index = 30,
    label = "HO + C2H3Br <=> BrHO + C2H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+12,'cm^3/(mol*s)'), n=0, Ea=(26000,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is C2H3BR + OH <=> C2H3 + BROH""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: C2H3BR + OH <=> C2H3 + BROH
""",
)

entry(
    index = 31,
    label = "HO + C2H5Br <=> BrHO + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(15000,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is C2H5BR + OH <=> C2H5 + BROH""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: C2H5BR + OH <=> C2H5 + BROH
""",
)

entry(
    index = 32,
    label = "CBrClF2 + Br-2 <=> CClF2 + Br2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.1e+13,'cm^3/(mol*s)'), n=0, Ea=(25167,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CF2BRCL + BR <=> CF2CL + BR2""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: CF2BRCL + BR <=> CF2CL + BR2
""",
)

entry(
    index = 33,
    label = "CBrClF2 + Cl <=> CClF2 + BrCl",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.1e+13,'cm^3/(mol*s)'), n=0, Ea=(25167,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CF2BRCL + CL <=> CF2CL + BRCL""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: CF2BRCL + CL <=> CF2CL + BRCL
""",
)

entry(
    index = 34,
    label = "Br2 + CBrF2 <=> Br + CBr2F2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.3e+12,'cm^3/(mol*s)'), n=0, Ea=(695,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CF2BR + BR2 <=> CF2BR2 + BR""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: CF2BR + BR2 <=> CF2BR2 + BR
""",
)

entry(
    index = 35,
    label = "BrCl-2 + Br-2 <=> Cl-2 + Br2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.7e+14,'cm^3/(mol*s)'), n=0, Ea=(6165,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is BR + BRCL <=> CL + BR2""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: BR + BRCL <=> CL + BR2
""",
)

entry(
    index = 36,
    label = "BrHO-2 + O <=> HO-2 + BrO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.2e+13,'cm^3/(mol*s)'), n=0, Ea=(854,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is O + BROH <=> OH + BRO""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: O + BROH <=> OH + BRO
""",
)

# entry(
#     index = 37,
#     label = "BrCl-2 + CH3 <=> Cl-2 + CH3Br",
#     degeneracy = 1.0,
#     kinetics = Arrhenius(A=(0.91,'cm^3/(mol*s)'), n=0, Ea=(2087,'cal/mol'), T0=(1,'K')),
#     rank = 3,
#     shortDesc = """The chemkin file reaction is BRCL + CH3 <=> CH3BR + CL""",
#     longDesc = 
# """
# Training reaction from kinetics library: CF2BrCl
# Original entry: BRCL + CH3 <=> CH3BR + CL
# """,
# )

entry(
    index = 38,
    label = "BrCl-2 + HO <=> Cl-2 + BrHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.04e+11,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is BRCL + OH <=> BROH + CL""",
    longDesc = 
"""
Training reaction from kinetics library: CF2BrCl
Original entry: BRCL + OH <=> BROH + CL
""",
)

entry(
    index = 39,
    label = "C2H3BrF2 + CH2F <=> CH2BrF + C2H3F2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8164.39,'cm^3/(mol*s)'), n=1.90059, Ea=(34.8483,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.03906, dn = +|- 0.00503368, dEa = +|- 0.0273931 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: FCC(F)Br + [CH2]F <=> F[CH]CF + FCBr
barrier = 38.751722 kJ/mol

Atom XYZ coordinates (angstrom)
Br    -0.710582    -0.06959    0.064548
F    3.427187    0.850492    0.356332
F    -3.078848    1.658661    0.049379
F    1.804671    -1.171257    -0.855546
C    2.058607    0.944221    0.160218
C    -2.894397    0.346752    -0.1346
C    1.458215    -0.421441    0.202163
H    1.637124    1.561835    0.951361
H    1.882072    1.402066    -0.812688
H    -3.099073    0.04249    -1.153675
H    -3.320999    -0.243353    0.667269
H    1.557856    -0.981402    1.12625
""",
)

entry(
    index = 40,
    label = "CHBrF2 + C3H5-2 <=> C3H5Br + CHF2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3010.22,'cm^3/(mol*s)'), n=2.08084, Ea=(18.6135,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.0283, dn = +|- 0.00366696, dEa = +|- 0.0199555 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: FC(F)Br + CD[C]C <=> F[CH]F + CDC(C)Br
barrier = 21.405848 kJ/mol

Atom XYZ coordinates (angstrom)
Br    0.047539    0.069602    0.022431
F    2.498187    0.291458    -1.402698
F    2.565631    -1.247633    0.119321
C    -2.671033    -1.146294    0.806051
C    -2.196443    0.082381    0.142324
C    -2.774808    1.135527    -0.375302
C    2.167667    -0.009219    -0.151657
H    -2.267259    -1.22077    1.815754
H    -3.762731    -1.139619    0.860701
H    -2.350385    -2.030251    0.254763
H    -2.214911    1.941465    -0.82978
H    -3.85913    1.220231    -0.357917
H    2.570426    0.709489    0.557258
""",
)

entry(
    index = 41,
    label = "CHBrF2 + C3H7-2 <=> C3H7Br-2 + CHF2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(29.0405,'cm^3/(mol*s)'), n=2.92564, Ea=(32.027,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.01628, dn = +|- 0.00212125, dEa = +|- 0.0115438 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: FC(F)Br + C[CH]C <=> F[CH]F + CC(C)Br
barrier = 36.109238 kJ/mol

Atom XYZ coordinates (angstrom)
Br    -0.087755    -0.091649    -0.146149
F    -2.382936    -0.795852    1.499977
F    -2.780324    0.937    0.26061
C    2.106182    0.178493    -0.471733
C    2.762228    -0.389817    0.749682
C    2.295231    1.645986    -0.708283
C    -2.249552    -0.27954    0.284296
H    2.203761    -0.436058    -1.361107
H    3.850328    -0.31145    0.649992
H    2.46849    0.166565    1.640172
H    2.509356    -1.43799    0.895073
H    1.721747    1.995792    -1.564147
H    3.354087    1.85192    -0.899219
H    1.997305    2.220225    0.169387
H    -2.662658    -0.925293    -0.486124
""",
)

entry(
    index = 42,
    label = "C4H8BrF + H <=> BrH-2 + C4H8F",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.44736e+08,'cm^3/(mol*s)'), n=1.68578, Ea=(11.5533,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.07457, dn = +|- 0.00944869, dEa = +|- 0.0514194 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: [H] + CC(C)(Br)CF <=> Br + C[C](C)CF
barrier = 14.636080 kJ/mol

Atom XYZ coordinates (angstrom)
Br    1.35261    -0.321232    0.142616
F    -2.732935    -0.753106    -0.097217
C    -0.626808    0.283637    0.092939
C    -0.917271    0.97526    1.403631
C    -0.790917    1.18017    -1.111236
C    -1.371414    -1.028105    -0.051336
H    -1.971745    1.261468    1.419597
H    -0.312338    1.873956    1.509652
H    -0.723785    0.31862    2.25032
H    -0.508874    0.667326    -2.029356
H    -1.840858    1.473795    -1.185634
H    -0.185732    2.079252    -1.010012
H    -1.190621    -1.681394    0.801667
H    -1.10145    -1.536505    -0.976397
H    3.194682    -0.906021    0.206636
""",
)

entry(
    index = 43,
    label = "C2BrClF4 + H <=> BrH-2 + C2ClF4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.90348e+08,'cm^3/(mol*s)'), n=1.65419, Ea=(17.1566,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.06749, dn = +|- 0.00858016, dEa = +|- 0.0466929 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: FC(F)(Cl)C(F)(F)Br + [H] <=> Br + F[C](F)C(F)(F)Cl
barrier = 20.387021 kJ/mol

Atom XYZ coordinates (angstrom)
Br    1.85994    0.145341    0.208508
Cl    -2.670654    0.008868    -0.126027
F    -0.824077    -1.189046    1.140715
F    -0.662561    -1.267403    -1.013813
F    -0.361079    1.509651    1.077226
F    -0.199743    1.431403    -1.077125
C    -0.986463    -0.495487    0.018577
C    -0.06239    0.738455    0.042972
H    3.742979    -0.284742    0.365862
""",
)

entry(
    index = 44,
    label = "C2BrClF4 + CF3-2 <=> CBrF3 + C2ClF4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(586.117,'cm^3/(mol*s)'), n=3.12075, Ea=(32.0311,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.04189, dn = +|- 0.00539196, dEa = +|- 0.0293429 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: FC(F)(Cl)C(F)(F)Br + F[C](F)F <=> FC(F)(F)Br + F[C](F)C(F)(F)Cl
barrier = 33.534214 kJ/mol

Atom XYZ coordinates (angstrom)
Br    0.870891    0.367826    0.149255
Cl    -3.754059    -0.200701    -0.118789
F    -1.643543    -0.951851    -1.319045
F    -1.71019    -1.40323    0.795401
F    -1.547961    1.269896    1.370281
F    -1.478862    1.719668    -0.744502
F    3.414172    -0.391604    1.341113
F    3.244413    -1.082496    -0.694261
F    3.679792    0.99087    -0.29247
C    -2.010346    -0.495298    -0.126751
C    -1.254629    0.803826    0.174306
C    3.043919    -0.077886    0.12326
""",
)

entry(
    index = 45,
    label = "CBrF3 + C2H5-2 <=> C2H5Br + CF3-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(58602.2,'cm^3/(mol*s)'), n=1.72086, Ea=(30.653,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.08491, dn = +|- 0.0107071, dEa = +|- 0.0582678 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: FC(F)(F)Br + C[CH2] <=> F[C](F)F + CCBr
barrier = 34.742622 kJ/mol

Atom XYZ coordinates (angstrom)
Br    -0.342445    0.013133    0.106288
F    2.221952    1.18392    0.771135
F    2.209734    0.357061    -1.218959
F    2.363061    -0.947998    0.489228
C    -3.081585    1.275261    -0.081705
C    -2.558302    -0.097131    0.19166
C    1.82947    0.166648    0.029364
H    -4.175831    1.262165    -0.048018
H    -2.732825    1.988497    0.662925
H    -2.781782    1.625062    -1.067895
H    -2.688081    -0.473277    1.199044
H    -2.737073    -0.844605    -0.571586
""",
)

entry(
    index = 46,
    label = "C2H4BrCl + CHF2 <=> CHBrF2 + C2H4Cl",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(86.845,'cm^3/(mol*s)'), n=3.24053, Ea=(40.4303,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.06873, dn = +|- 0.00873259, dEa = +|- 0.0475224 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: F[CH]F + ClCCBr <=> FC(F)Br + [CH2]CCl
barrier = 43.403285 kJ/mol

Atom XYZ coordinates (angstrom)
Br    0.665257    -0.197974    0.034763
Cl    -4.007259    0.110967    -0.183684
F    2.929561    0.728303    1.565468
F    2.881527    1.593053    -0.418692
C    -2.241107    0.472508    -0.028208
C    -1.475093    -0.79314    -0.17511
C    2.733361    0.478125    0.280191
H    -2.003695    1.190266    -0.806372
H    -2.103895    0.92569    0.947943
H    -1.584907    -1.506089    0.632071
H    -1.483213    -1.236371    -1.162749
H    3.35788    -0.331419    -0.087745
""",
)

entry(
    index = 47,
    label = "C2Br2F4 + CF3-2 <=> CBrF3 + C2BrF4",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(762.873,'cm^3/(mol*s)'), n=3.1179, Ea=(30.4436,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.04141, dn = +|- 0.00533126, dEa = +|- 0.0290125 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: FC(F)(Br)C(F)(F)Br + F[C](F)F <=> FC(F)(F)Br + F[C](F)C(F)(F)Br
barrier = 31.990851 kJ/mol

Atom XYZ coordinates (angstrom)
Br    -3.466707    -0.091823    -0.157186
Br    1.339999    0.212453    0.174858
F    -1.25135    0.049477    -1.679433
F    -1.242999    -1.603232    -0.283528
F    3.738622    -1.244564    -0.610416
F    4.127123    0.106738    1.024815
F    3.934104    0.870572    -0.98263
F    -1.007376    1.810147    0.403723
F    -0.999142    0.15769    1.799628
C    -1.559157    -0.323256    -0.442516
C    3.530224    -0.041853    -0.132686
C    -0.769221    0.524511    0.556459
""",
)

entry(
    index = 48,
    label = "C3H2BrF3 + H <=> BrH-2 + C3H2F3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.90982e+08,'cm^3/(mol*s)'), n=1.65484, Ea=(30.45,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.05692, dn = +|- 0.00727358, dEa = +|- 0.0395826 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: [H] + CDC(Br)C(F)(F)F <=> Br + CD[C]C(F)(F)F
barrier = 33.852678 kJ/mol

Atom XYZ coordinates (angstrom)
Br    -1.585539    -0.095165    0.332933
F    1.421581    -0.826035    1.244223
F    1.195558    -1.213337    -0.860036
F    2.522304    0.346189    -0.190057
C    1.3455    -0.244391    0.045464
C    0.220431    0.744299    -0.014841
C    0.345796    2.029363    -0.247845
H    1.325594    2.453514    -0.432753
H    -0.512358    2.686039    -0.2646
H    -3.034319    -0.767737    1.05323
""",
)

entry(
    index = 49,
    label = "CBr2F2-2 + CClF2-2 <=> CBrClF2 + CBrF2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(172.463,'cm^3/(mol*s)'), n=3.11892, Ea=(30.7055,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.0425, dn = +|- 0.00546859, dEa = +|- 0.0297599 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: FC(F)(Br)Br + F[C](F)Cl <=> FC(F)(Cl)Br + F[C](F)Br
barrier = 32.206879 kJ/mol

Atom XYZ coordinates (angstrom)
Br    0.460087    -0.262915    0.014784
Br    -2.686314    0.883984    -0.330646
Cl    3.264796    1.350126    0.118422
F    3.086125    -0.960169    -0.930648
F    2.98895    -0.928052    1.214929
F    -1.859588    -1.592924    -1.002782
F    -1.976883    -1.279231    1.114545
C    2.665541    -0.281869    0.115457
C    -1.679598    -0.717933    -0.037423
""",
)

entry(
    index = 50,
    label = "CH2BrCl + CHBrF <=> CHBr2F + CH2Cl-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(746.917,'cm^3/(mol*s)'), n=2.18514, Ea=(42.3788,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.05271, dn = +|- 0.00674926, dEa = +|- 0.0367292 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: F[CH]Br + ClCBr <=> FC(Br)Br + [CH2]Cl
barrier = 44.915897 kJ/mol

Atom XYZ coordinates (angstrom)
Br    0.727235    0.591443    0.2105
Br    -2.307938    0.025672    -1.133564
Cl    3.64026    -0.636066    1.030471
F    -1.733313    2.019181    0.584508
C    2.950758    0.634475    0.088297
C    -1.443897    0.733646    0.403101
H    3.1739    1.613879    0.485606
H    3.105265    0.495393    -0.971995
H    -1.654842    0.14328    1.287437
""",
)

entry(
    index = 51,
    label = "CHBr2F + CH3 <=> CH3Br-2 + CHBrF",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(969316,'cm^3/(mol*s)'), n=1.73772, Ea=(31.5183,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.09859, dn = +|- 0.0123528, dEa = +|- 0.0672237 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: FC(Br)Br + [CH3] <=> F[CH]Br + CBr
barrier = 36.933160 kJ/mol

Atom XYZ coordinates (angstrom)
Br    1.063107    2.352526    0.710773
Br    -1.349086    0.147251    0.02247
F    1.175448    -0.286403    1.242837
C    0.738878    0.523435    0.278061
C    -3.536395    -0.434907    -0.217355
H    1.180491    0.272583    -0.679342
H    -3.755592    -0.046184    -1.201183
H    -3.49522    -1.510768    -0.131825
H    -3.988526    0.08918    0.612043
""",
)

entry(
    index = 52,
    label = "CBr2F2-2 + CF3-2 <=> CBrF3 + CBrF2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(278.642,'cm^3/(mol*s)'), n=3.1149, Ea=(23.7221,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.03931, dn = +|- 0.00506557, dEa = +|- 0.0275666 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: FC(F)(Br)Br + F[C](F)F <=> FC(F)(F)Br + F[C](F)Br
barrier = 25.362552 kJ/mol

Atom XYZ coordinates (angstrom)
Br    -0.703747    0.212601    -0.017695
Br    2.439573    -0.552274    -0.825436
F    1.497735    1.931236    -0.382523
F    1.669182    0.753325    1.400087
F    -3.325671    -0.185322    1.267442
F    -3.497697    0.998884    -0.527184
F    -3.234007    -1.138094    -0.666312
C    1.363923    0.721192    0.119495
C    -2.946685    -0.057253    0.019355
""",
)

entry(
    index = 53,
    label = "CHBr2F + CH2F <=> CH2BrF + CHBrF",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(17849.2,'cm^3/(mol*s)'), n=1.86732, Ea=(29.8155,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.04898, dn = +|- 0.00628265, dEa = +|- 0.03419 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: FC(Br)Br + [CH2]F <=> F[CH]Br + FCBr
barrier = 33.737836 kJ/mol

Atom XYZ coordinates (angstrom)
Br    1.106218    -0.236791    -0.262014
Br    -1.85905    -1.423856    0.757452
F    3.5319    1.402498    0.113046
F    -1.115707    -1.118595    -1.81453
C    3.324795    0.089317    -0.004456
C    -1.002387    -0.474606    -0.653796
H    3.721577    -0.312336    -0.928333
H    3.517276    -0.44511    0.917625
H    -1.374834    0.54097    -0.722607
""",
)

entry(
    index = 54,
    label = "C2H3BrClF + CH2F <=> CH2BrF + C2H3ClF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(536.535,'cm^3/(mol*s)'), n=2.88999, Ea=(31.7139,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.0386, dn = +|- 0.00497619, dEa = +|- 0.0270803 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: FC(Br)CCl + [CH2]F <=> F[CH]CCl + FCBr
barrier = 35.499034 kJ/mol

Atom XYZ coordinates (angstrom)
Br    1.050004    -0.073178    -0.006535
Cl    -3.577789    0.313177    -0.318559
F    3.258178    1.874367    -0.045654
F    -1.308134    -1.414758    0.966874
C    -1.820055    0.628302    -0.093424
C    3.204106    0.553617    0.155262
C    -1.066513    -0.652821    -0.110115
H    -1.496982    1.269474    -0.906337
H    -1.698866    1.133235    0.860214
H    3.447306    0.281533    1.174822
H    3.668822    -0.004278    -0.648261
H    -1.107051    -1.239997    -1.021361
""",
)

entry(
    index = 55,
    label = "CHBrF2 + C2H4F <=> C2H4BrF + CHF2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(212.992,'cm^3/(mol*s)'), n=2.83406, Ea=(38.7396,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.06105, dn = +|- 0.00778563, dEa = +|- 0.0423691 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: FC(F)Br + [CH2]CF <=> F[CH]F + FCCBr
barrier = 42.637983 kJ/mol

Atom XYZ coordinates (angstrom)
Br    -0.177837    -0.199931    -0.375829
F    2.621749    0.641765    1.213954
F    -2.963025    -0.894278    -0.597064
F    -2.647876    1.245985    -0.685011
C    2.705906    0.697797    -0.162652
C    2.001519    -0.462309    -0.77346
C    -2.307639    0.126281    -0.062743
H    3.769002    0.675836    -0.427302
H    2.280566    1.646843    -0.491829
H    2.021276    -0.485181    -1.856361
H    2.194682    -1.418585    -0.302009
H    -2.445769    0.191004    1.013076
""",
)

entry(
    index = 56,
    label = "CHBr2F + H <=> BrH-2 + CHBrF",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(9.10139e+08,'cm^3/(mol*s)'), n=1.66953, Ea=(15.6858,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.06744, dn = +|- 0.00857452, dEa = +|- 0.0466622 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: FC(Br)Br + [H] <=> Br + F[CH]Br
barrier = 19.053715 kJ/mol

Atom XYZ coordinates (angstrom)
Br    1.539171    -0.453573    -0.065209
Br    -1.68006    -0.02403    -0.11566
F    0.262691    1.912182    -0.1892
C    0.108915    0.729599    0.412339
H    0.083636    0.847217    1.48892
H    -3.533343    -0.463291    -0.575544
""",
)

entry(
    index = 57,
    label = "CBrClF2 + H <=> BrH-2 + CClF2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.43579e+08,'cm^3/(mol*s)'), n=1.62342, Ea=(14.4047,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.05329, dn = +|- 0.00682123, dEa = +|- 0.0371209 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: FC(F)(Cl)Br + [H] <=> Br + F[C](F)Cl
barrier = 17.143190 kJ/mol

Atom XYZ coordinates (angstrom)
Br    -1.332658    0.163508    -0.01166
Cl    1.53571    -1.032713    -0.00192
F    0.964162    1.19402    -1.068473
F    0.953277    1.185404    1.07663
C    0.648929    0.479777    -0.000343
H    -3.323809    0.136649    -0.019709
""",
)

entry(
    index = 58,
    label = "CBrF3 + C2H3-2 <=> C2H3Br + CF3-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3044.71,'cm^3/(mol*s)'), n=2.97709, Ea=(17.0548,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.00181, dn = +|- 0.000237097, dEa = +|- 0.00129027 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: FC(F)(F)Br + [CH]DC <=> F[C](F)F + CDCBr
barrier = 20.024449 kJ/mol

Atom XYZ coordinates (angstrom)
Br    0.423177    0.134846    0.429115
F    -1.957825    -0.859239    -0.715565
F    -2.283691    0.021081    1.221893
F    -1.983729    1.281933    -0.497145
C    3.413462    0.258826    -0.305221
C    2.648708    0.13804    0.743637
C    -1.63926    0.145606    0.077577
H    4.49493    0.264819    -0.196714
H    3.00987    0.355909    -1.305469
H    2.834242    0.031876    1.801063
""",
)

entry(
    index = 59,
    label = "CBrF3 + C3H2F3 <=> C3H2BrF3 + CF3-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2665.1,'cm^3/(mol*s)'), n=3.02759, Ea=(21.2447,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.01438, dn = +|- 0.00187528, dEa = +|- 0.0102052 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: FC(F)(F)Br + CD[C]C(F)(F)F <=> F[C](F)F + CDC(Br)C(F)(F)F
barrier = 22.599786 kJ/mol

Atom XYZ coordinates (angstrom)
Br    -0.499964    0.203759    0.16925
F    1.975214    0.229851    -2.05905
F    2.241327    -1.452763    -0.744496
F    3.729938    0.105659    -0.812116
F    -2.939053    -0.063517    -1.203497
F    -2.772771    -1.426925    0.453288
F    -3.197412    0.653042    0.809783
C    2.413015    -0.135187    -0.853866
C    1.705486    0.602116    0.232959
C    2.176363    1.396843    1.153991
C    -2.546814    -0.19763    0.044114
H    1.532965    1.867461    1.885363
H    3.242532    1.600567    1.199618
""",
)

entry(
    index = 60,
    label = "CBrClF2 + CH3 <=> CH3Br-2 + CClF2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(33938,'cm^3/(mol*s)'), n=2.67089, Ea=(25.7849,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.11494, dn = +|- 0.0142947, dEa = +|- 0.0777911 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: FC(F)(Cl)Br + [CH3] <=> CBr + F[C](F)Cl
barrier = 31.121172 kJ/mol

Atom XYZ coordinates (angstrom)
Br    0.990686    -0.305098    -0.065486
Cl    -1.886815    -0.235184    -1.478304
F    -1.516204    0.574205    0.901024
F    -1.442396    -1.556554    0.645431
C    3.269403    -0.229655    -0.027364
C    -1.130883    -0.397356    0.091764
H    3.504537    -1.052014    0.631889
H    3.444545    0.76127    0.36475
H    3.49489    -0.376483    -1.07355
""",
)

entry(
    index = 61,
    label = "BrO-2 + CClF2-2 <=> CBrClF2 + O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(66786.7,'cm^3/(mol*s)'), n=1.64401, Ea=(7.72206,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.04581, dn = +|- 0.0058851, dEa = +|- 0.0320265 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: [O]Br + F[C](F)Cl <=> FC(F)(Cl)Br + [O]
barrier = 9.551526 kJ/mol

Atom XYZ coordinates (angstrom)
Br    1.167554    -0.119343    0.050381
Cl    -1.988463    -0.949987    0.060245
F    -1.219943    1.179406    -1.111097
F    -1.240383    1.282349    1.036986
O    2.978383    0.093367    0.058172
C    -1.035885    0.501446    -0.000248
""",
)

entry(
    index = 62,
    label = "C2Br2F4 + H <=> BrH-2 + C2BrF4",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.31827e+09,'cm^3/(mol*s)'), n=1.65584, Ea=(16.5217,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.06821, dn = +|- 0.00866868, dEa = +|- 0.0471746 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: FC(F)(Br)C(F)(F)Br + [H] <=> Br + F[C](F)C(F)(F)Br
barrier = 19.648980 kJ/mol

Atom XYZ coordinates (angstrom)
Br    2.301777    -0.185164    -0.228192
Br    -2.382233    0.078918    0.159984
F    0.213126    -1.393572    1.081215
F    0.02992    -1.475545    -1.07146
F    -0.335751    1.238438    -1.143551
F    -0.152878    1.320129    1.009206
C    0.361556    -0.710252    -0.04313
C    -0.513126    0.556732    -0.016916
H    4.206071    0.184034    -0.405948
""",
)

entry(
    index = 63,
    label = "CH2BrF + C2H5-2 <=> C2H5Br + CH2F",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(654.249,'cm^3/(mol*s)'), n=2.92288, Ea=(42.8924,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.0316, dn = +|- 0.0040868, dEa = +|- 0.0222402 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)/ma-def2-tzvpp//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: C[CH2] + FCBr <=> CCBr + [CH2]F
barrier = 47.747493 kJ/mol
T1 = 0.016798142

Atom XYZ coordinates (angstrom)
Br    0.051798    -0.005787    0.187798
F    2.457409    1.612326    0.5254
C    -2.704663    1.19658    -0.167876
C    2.214976    0.291986    0.495899
C    -2.145444    -0.190126    -0.124112
H    -2.516792    1.727322    0.764108
H    -3.787918    1.159472    -0.321194
H    -2.2708    1.771314    -0.984589
H    2.397347    -0.17149    1.458011
H    2.659186    -0.178656    -0.372978
H    -2.417378    -0.790187    0.735839
H    -2.166966    -0.745604    -1.053901
""",
)

entry(
    index = 64,
    label = "CHBrClF + H <=> BrH-2 + CHClF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.9838e+08,'cm^3/(mol*s)'), n=1.68119, Ea=(16.5265,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.07305, dn = +|- 0.00926235, dEa = +|- 0.0504054 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)/ma-def2-tzvpp//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: FC(Cl)Br + [H] <=> Br + F[CH]Cl
barrier = 19.605450 kJ/mol
T1 = 0.01444153

Atom XYZ coordinates (angstrom)
Br    -1.158433    0.083191    -0.181051
Cl    1.819888    -0.805935    -0.084234
F    1.107544    1.632987    -0.182254
C    0.735911    0.482132    0.385502
H    0.711648    0.576987    1.464535
H    -3.037433    -0.06759    -0.717791
""",
)

entry(
    index = 65,
    label = "BrHO-2 + CH3 <=> CH3Br-2 + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(36695,'cm^3/(mol*s)'), n=2.78053, Ea=(-4.68964,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.08837, dn = +|- 0.0111256, dEa = +|- 0.0605451 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)/ma-def2-tzvpp//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: OBr + [CH3] <=> [OH] + CBr
barrier = 0.452075 kJ/mol
T1 = 0.018846917

Atom XYZ coordinates (angstrom)
Br    -0.118549    -0.069713    0.053594
O    -2.015924    0.013295    0.221347
C    2.268855    0.23243    -0.04214
H    2.502463    -0.81494    -0.159372
H    2.455354    0.68151    0.920006
H    2.34771    0.863433    -0.912829
H    -2.198125    0.960297    0.239498
""",
)

entry(
    index = 66,
    label = "CH2Br2 + CHF2 <=> CHBrF2 + CH2Br-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(124.757,'cm^3/(mol*s)'), n=3.19274, Ea=(34.6101,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.05432, dn = +|- 0.00694908, dEa = +|- 0.0378166 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)/ma-def2-tzvpp//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: F[CH]F + BrCBr <=> FC(F)Br + [CH2]Br
barrier = 37.702315 kJ/mol
T1 = 0.01622502

Atom XYZ coordinates (angstrom)
Br    -0.824332    -0.260567    0.125383
Br    2.486079    0.318812    -0.216333
F    -3.463231    0.89125    0.486877
F    -3.564815    -1.132769    -0.273522
C    -2.954235    0.035303    -0.383247
C    1.220519    -0.655509    0.794202
H    -2.953534    0.41758    -1.40064
H    1.202276    -0.331134    1.824435
H    1.322044    -1.71951    0.636931
""",
)

entry(
    index = 67,
    label = "BrO-2 + H <=> BrH-2 + O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.39048e+10,'cm^3/(mol*s)'), n=1.10058, Ea=(3.20685,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.03651, dn = +|- 0.00471129, dEa = +|- 0.0256386 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)/ma-def2-tzvpp//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: [H] + [O]Br <=> Br + [O]
barrier = 5.161449 kJ/mol
T1 = 0.030783436

Atom XYZ coordinates (angstrom)
Br    0.15652    0.195819    0.0
O    1.870914    -0.058578    -0.0
H    -2.027434    -0.137142    0.0
""",
)

entry(
    index = 68,
    label = "CH2BrF + C3H5-2 <=> C3H5Br + CH2F",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(78.772,'cm^3/(mol*s)'), n=3.16729, Ea=(21.8627,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.05192, dn = +|- 0.00665035, dEa = +|- 0.0361909 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)/ma-def2-tzvpp//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: CD[C]C + FCBr <=> CDC(C)Br + [CH2]F
barrier = 25.049727 kJ/mol
T1 = 0.016521265

Atom XYZ coordinates (angstrom)
Br    0.301351    -0.127294    0.330106
F    2.986525    0.855808    0.037512
C    -2.243082    1.547    -0.045014
C    2.438508    -0.333124    0.344694
C    -2.621291    -0.913473    0.57807
C    -1.911408    0.150614    0.299121
H    -1.812289    2.235319    0.682215
H    -1.841278    1.807919    -1.024146
H    -3.327896    1.679571    -0.059791
H    2.669603    -0.623318    1.363081
H    2.638752    -1.070758    -0.423765
H    -3.70736    -0.854283    0.582063
H    -2.169153    -1.868213    0.809468
""",
)

entry(
    index = 69,
    label = "C2H3BrF2-2 + H <=> BrH-2 + C2H3F2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.98897e+08,'cm^3/(mol*s)'), n=1.67337, Ea=(17.4172,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.0734, dn = +|- 0.00930592, dEa = +|- 0.0506425 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)/ma-def2-tzvpp//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: CC(F)(F)Br + [H] <=> Br + C[C](F)F
barrier = 20.318597 kJ/mol
T1 = 0.014279538999999999

Atom XYZ coordinates (angstrom)
Br    -1.076257    -0.133169    -0.189436
F    1.276764    -0.749048    1.086811
F    1.425347    -0.860042    -1.060352
C    1.488997    1.279994    -0.084972
C    0.961638    -0.120115    -0.049095
H    1.205329    1.751602    -1.02133
H    2.575913    1.232866    -0.007338
H    1.082763    1.84315    0.750179
H    -3.021496    -0.240488    -0.315279
""",
)

entry(
    index = 70,
    label = "C3H6Br + H <=> BrH-2 + C3H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.1918e+08,'cm^3/(mol*s)'), n=1.64765, Ea=(24.1967,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.05647, dn = +|- 0.00721707, dEa = +|- 0.039275 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)/ma-def2-tzvpp//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: [H] + C[C](C)Br <=> Br + C[C]C
barrier = 28.154037 kJ/mol
T1 = 0.017883208

Atom XYZ coordinates (angstrom)
Br    -0.936664    0.184628    -0.182767
C    1.732242    1.413207    0.049091
C    1.654926    -1.207569    -0.005006
C    1.077084    0.12718    -0.277006
H    2.787646    1.36944    -0.230478
H    1.680573    1.630784    1.122759
H    1.266236    2.244497    -0.477649
H    1.141434    -1.987516    -0.565069
H    2.711435    -1.214564    -0.283729
H    1.58912    -1.465838    1.058825
H    -2.753473    0.243138    -0.359323
""",
)

entry(
    index = 71,
    label = "CBr2F2-2 + CH3 <=> CH3Br-2 + CBrF2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(17615.5,'cm^3/(mol*s)'), n=2.67281, Ea=(29.2981,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.11395, dn = +|- 0.0141778, dEa = +|- 0.0771552 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)/ma-def2-tzvpp//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: FC(F)(Br)Br + [CH3] <=> CBr + F[C](F)Br
barrier = 34.811398 kJ/mol
T1 = 0.014947799

Atom XYZ coordinates (angstrom)
Br    -1.470048    0.184605    0.159798
Br    1.715432    -0.374281    1.023417
F    0.688762    1.996931    0.264983
F    0.879547    0.595252    -1.345806
C    0.569609    0.723817    -0.06784
C    -3.72834    -0.190733    0.218831
H    -4.096399    0.763301    0.565769
H    -3.933048    -0.436323    -0.812573
H    -3.773066    -1.007498    0.924392
""",
)

entry(
    index = 72,
    label = "C2H3BrClF + H <=> BrH-2 + C2H3ClF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.01227e+08,'cm^3/(mol*s)'), n=1.6928, Ea=(14.428,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.08012, dn = +|- 0.0101259, dEa = +|- 0.055105 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)/ma-def2-tzvpp//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: FC(Br)CCl + [H] <=> Br + F[CH]CCl
barrier = 17.744476 kJ/mol
T1 = 0.014012159

Atom XYZ coordinates (angstrom)
Br    -1.661717    -0.112732    -0.324181
Cl    2.844511    -0.286668    0.100834
F    0.432244    1.630307    0.180271
C    1.096592    -0.626658    0.27666
C    0.307097    0.435411    -0.425548
H    0.860478    -0.634635    1.336626
H    0.900157    -1.598134    -0.163713
H    0.511285    0.53193    -1.487467
H    -3.527504    -0.579815    -0.193084
""",
)

entry(
    index = 73,
    label = "C3H7Br-2 + CH3 <=> CH3Br-2 + C3H7-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(10506.2,'cm^3/(mol*s)'), n=2.7954, Ea=(47.0911,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.09358, dn = +|- 0.0117533, dEa = +|- 0.063961 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)/ma-def2-tzvpp//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: CC(C)Br + [CH3] <=> C[CH]C + CBr
barrier = 52.604755 kJ/mol
T1 = 0.015607282

Atom XYZ coordinates (angstrom)
Br    0.637664    0.005505    0.112481
C    -1.532644    0.001974    -0.269018
C    -2.056224    1.282617    0.311051
C    -2.058604    -1.260258    0.348064
C    2.8518    0.008778    0.550246
H    -1.510431    -0.013842    -1.354152
H    -3.134727    1.353108    0.132819
H    -1.893211    1.312019    1.388829
H    -1.579652    2.152678    -0.135861
H    -1.895638    -1.258572    1.426249
H    -3.137236    -1.333901    0.171906
H    -1.583652    -2.143845    -0.073305
H    3.288065    -0.007405    -0.43846
H    2.980279    -0.895797    1.127577
H    2.983203    0.930573    1.098976
""",
)

entry(
    index = 74,
    label = "CHBrF2 + C2H5-2 <=> C2H5Br + CHF2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(544.314,'cm^3/(mol*s)'), n=2.81735, Ea=(38.2912,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.06112, dn = +|- 0.0077936, dEa = +|- 0.0424125 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)/ma-def2-tzvpp//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: FC(F)Br + C[CH2] <=> F[CH]F + CCBr
barrier = 42.822491 kJ/mol
T1 = 0.016733689

Atom XYZ coordinates (angstrom)
Br    -0.093202    -0.118338    -0.042938
F    2.519548    0.294977    1.116844
F    2.507739    0.676429    -1.015503
C    -2.654726    1.50501    0.088746
C    -2.323753    0.050303    -0.004533
C    2.091924    -0.145448    -0.059891
H    -2.244746    1.946176    0.995755
H    -2.268237    2.054167    -0.768248
H    -3.740983    1.639213    0.111378
H    -2.566878    -0.442131    -0.93822
H    -2.543969    -0.552515    0.86807
H    2.386392    -1.174961    -0.245688
""",
)

entry(
    index = 75,
    label = "CBr2F2-2 + H <=> BrH-2 + CBrF2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.1581e+09,'cm^3/(mol*s)'), n=1.60333, Ea=(14.9526,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.04394, dn = +|- 0.00564944, dEa = +|- 0.030744 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)/ma-def2-tzvpp//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: FC(F)(Br)Br + [H] <=> Br + F[C](F)Br
barrier = 17.994690 kJ/mol
T1 = 0.012894706

Atom XYZ coordinates (angstrom)
Br    1.208827    -0.778256    0.00902
Br    -1.970661    -0.096701    0.007503
F    -0.018478    1.419161    1.056322
F    -0.023134    1.392733    -1.086821
C    -0.19317    0.650005    -0.005556
H    2.876023    -1.897252    0.019435
""",
)

entry(
    index = 76,
    label = "CHBrF2 + H <=> BrH-2 + CHF2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.53002e+08,'cm^3/(mol*s)'), n=1.6735, Ea=(20.6842,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.0692, dn = +|- 0.00879114, dEa = +|- 0.0478411 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)/ma-def2-tzvpp//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: FC(F)Br + [H] <=> Br + F[CH]F
barrier = 24.252332 kJ/mol
T1 = 0.015330711

Atom XYZ coordinates (angstrom)
Br    0.95282    0.000667    0.46122
F    -1.496169    1.078924    -0.224274
F    -1.49574    -1.082736    -0.217847
C    -1.078812    0.000104    0.42721
H    -1.416961    0.003102    1.459626
H    2.85748    -4e-06    0.38048
""",
)

entry(
    index = 77,
    label = "CBrF3 + CH3 <=> CH3Br-2 + CF3-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(45587.3,'cm^3/(mol*s)'), n=2.62423, Ea=(42.4771,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.13168, dn = +|- 0.0162523, dEa = +|- 0.0884446 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)/ma-def2-tzvpp//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: [CH3] + FC(F)(F)Br <=> CBr + F[C](F)F
barrier = 47.699563 kJ/mol
T1 = 0.016635467

Atom XYZ coordinates (angstrom)
Br    -0.764216    0.32912    0.000342
F    1.923357    1.337944    0.079855
F    1.763598    -0.449377    -1.113198
F    1.75288    -0.584806    1.036894
C    1.379967    0.139761    0.00149
C    -2.9799    0.524795    -0.000844
H    -3.245485    0.144805    0.97547
H    -3.263408    -0.097719    -0.83758
H    -3.116444    1.587447    -0.142177
""",
)

entry(
    index = 78,
    label = "CH2Br2 + H <=> BrH-2 + CH2Br-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.0787e+09,'cm^3/(mol*s)'), n=1.7149, Ea=(17.3615,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.08042, dn = +|- 0.0101622, dEa = +|- 0.0553021 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)/ma-def2-tzvpp//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: BrCBr + [H] <=> Br + [CH2]Br
barrier = 20.565964 kJ/mol
T1 = 0.013339713999999999

Atom XYZ coordinates (angstrom)
Br    1.878469    0.039549    -0.00503
Br    -1.363522    -0.388209    0.025669
C    0.180071    0.913858    0.013705
H    0.067235    1.499003    -0.887752
H    0.0849    1.494594    0.920035
H    -3.024115    -1.332336    0.041325
""",
)

entry(
    index = 79,
    label = "CH2Br + H <=> BrH-2 + CH2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.34604e+08,'cm^3/(mol*s)'), n=1.65014, Ea=(32.1137,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.05114, dn = +|- 0.00655201, dEa = +|- 0.0356558 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)/ma-def2-tzvpp//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: [CH2]Br + [H] <=> [CH2] + Br
barrier = 36.675382 kJ/mol
T1 = 0.02090774

Atom XYZ coordinates (angstrom)
Br    0.310158    0.178487    -0.161511
C    -1.685807    0.063105    -0.048989
H    -2.183971    0.964549    0.26264
H    -2.090916    -0.933641    -0.032599
H    2.035872    0.304512    -0.426476
""",
)

entry(
    index = 80,
    label = "BrO-2 + C2H5-2 <=> C2H5Br + O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3792.02,'cm^3/(mol*s)'), n=2.31694, Ea=(-2.64737,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.05842, dn = +|- 0.00745944, dEa = +|- 0.040594 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)/ma-def2-tzvpp//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: [O]Br + C[CH2] <=> [O] + CCBr
barrier = 2.092202 kJ/mol
T1 = 0.026373221000000002

Atom XYZ coordinates (angstrom)
Br    -0.557105    -0.105406    0.000141
O    -2.290276    0.576081    -0.000252
C    2.461824    0.725543    0.00055
C    1.73812    -0.57393    -0.000651
H    2.224447    1.313575    -0.883994
H    2.224506    1.311912    0.886213
H    3.542417    0.544136    0.000356
H    1.742319    -1.157844    -0.912253
H    1.74223    -1.159482    0.909898
""",
)

entry(
    index = 81,
    label = "BrCl-2 + O <=> BrO-2 + Cl",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.26115e+10,'cm^3/(mol*s)'), n=1.0253, Ea=(7.57907,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.00977, dn = +|- 0.0012773, dEa = +|- 0.006951 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)/ma-def2-tzvpp//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: ClBr + [O] <=> [O]Br + [Cl]
barrier = 8.115829 kJ/mol
T1 = 0.023650134

Atom XYZ coordinates (angstrom)
Br    -0.032586    0.360069    -0.0
Cl    -2.12648    -0.188305    0.0
O    2.159065    -0.171765    -0.0
""",
)

entry(
    index = 82,
    label = "C3H5Br + H <=> BrH-2 + C3H5-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.02859e+08,'cm^3/(mol*s)'), n=1.71519, Ea=(26.2766,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.0804, dn = +|- 0.0101603, dEa = +|- 0.0552921 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)/ma-def2-tzvpp//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: CDC(C)Br + [H] <=> Br + CD[C]C
barrier = 29.674673 kJ/mol
T1 = 0.015057194

Atom XYZ coordinates (angstrom)
Br    -0.940784    0.136844    0.208438
C    1.707215    -1.138346    0.047647
C    1.099256    0.214533    0.065956
C    1.657359    1.402542    0.006603
H    1.335309    -1.715671    -0.79864
H    1.456678    -1.684868    0.956693
H    2.792135    -1.052304    -0.028879
H    2.737089    1.479289    -0.069449
H    1.082451    2.316507    0.030392
H    -2.723511    0.131778    0.334426
""",
)

entry(
    index = 83,
    label = "C4H8Br2 + H <=> BrH-2 + C4H8Br",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.84364e+08,'cm^3/(mol*s)'), n=1.64514, Ea=(6.52837,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.06064, dn = +|- 0.00773462, dEa = +|- 0.0420915 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)/ma-def2-tzvpp//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: [H] + CC(C)(Br)CBr <=> Br + C[C](C)CBr
barrier = 8.674275 kJ/mol
T1 = 0.01167797

Atom XYZ coordinates (angstrom)
Br    -2.294916    -0.160662    0.114744
Br    2.377761    -0.360503    -0.09508
C    -0.353051    0.560241    0.039128
C    -0.261147    1.395392    -1.217234
C    -0.149364    1.359056    1.305921
C    0.447248    -0.720488    -0.014772
H    -0.460657    0.798036    -2.105508
H    0.746749    1.808547    -1.294619
H    -0.971565    2.218778    -1.179671
H    -0.270342    0.73616    2.190813
H    0.861951    1.771094    1.305751
H    -0.859275    2.182274    1.354988
H    0.22332    -1.298309    -0.904751
H    0.302112    -1.323946    0.87453
H    -4.201687    -0.777238    0.193775
""",
)

entry(
    index = 84,
    label = "CHBrClF + CH2Br-2 <=> CH2Br2 + CHClF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(205.056,'cm^3/(mol*s)'), n=2.81796, Ea=(42.2401,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.07093, dn = +|- 0.00900307, dEa = +|- 0.0489944 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)/ma-def2-tzvpp//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: FC(Cl)Br + [CH2]Br <=> F[CH]Cl + BrCBr
barrier = 46.705883 kJ/mol
T1 = 0.016200155

Atom XYZ coordinates (angstrom)
Br    -0.45374    0.342911    0.123605
Br    2.8529    -0.379007    -0.218385
Cl    -3.423087    -0.908979    0.055165
F    -3.017661    1.59539    -0.140186
C    -2.52174    0.435258    -0.563213
C    1.617598    0.450979    0.936811
H    -2.426075    0.405164    -1.642417
H    1.778467    1.516741    1.004937
H    1.51453    -0.081793    1.870745
""",
)

entry(
    index = 85,
    label = "C2H3Br + H <=> BrH-2 + C2H3-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.8008e+08,'cm^3/(mol*s)'), n=1.73104, Ea=(30.5243,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.0785, dn = +|- 0.00992891, dEa = +|- 0.0540327 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)/ma-def2-tzvpp//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: [H] + CDCBr <=> Br + [CH]DC
barrier = 33.873315 kJ/mol
T1 = 0.016516768

Atom XYZ coordinates (angstrom)
Br    -0.762594    0.019534    0.13877
C    2.150995    -0.357142    0.016101
C    1.211078    0.554941    0.057893
H    1.927395    -1.415494    0.0229
H    3.19265    -0.058611    -0.029025
H    1.311523    1.629869    0.062243
H    -2.386986    -0.539657    0.379507
""",
)

entry(
    index = 86,
    label = "C2H5Br + H <=> BrH-2 + C2H5-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.06769e+08,'cm^3/(mol*s)'), n=1.76845, Ea=(19.2025,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.0973, dn = +|- 0.0121989, dEa = +|- 0.0663859 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)/ma-def2-tzvpp//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: [H] + CCBr <=> Br + C[CH2]
barrier = 22.466300 kJ/mol
T1 = 0.014788011

Atom XYZ coordinates (angstrom)
Br    0.663211    0.386968    -0.01197
C    -2.268965    0.422757    0.014555
C    -1.156126    -0.587221    -0.012039
H    -3.230724    -0.096638    0.014511
H    -2.216454    1.041857    0.908091
H    -2.232176    1.071142    -0.858766
H    -1.099097    -1.212747    0.871718
H    -1.114608    -1.18288    -0.917073
H    2.290144    1.29266    -0.008921
""",
)

entry(
    index = 87,
    label = "CH3Br-2 + C3H5-3 <=> C3H5Br-2 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(423.303,'cm^3/(mol*s)'), n=3.19649, Ea=(26.9362,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.05861, dn = +|- 0.00748319, dEa = +|- 0.0407233 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)/ma-def2-tzvpp//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: CBr + [CH]DCC <=> [CH3] + CCDCBr
barrier = 29.579531 kJ/mol
T1 = 0.016196781

Atom XYZ coordinates (angstrom)
Br    -0.854201    -0.266587    -0.000628
C    3.655131    0.16993    2.2e-05
C    -2.934715    0.205655    -0.000482
C    2.159215    0.326515    -0.000169
C    1.317629    -0.676814    -0.000465
H    3.94363    -0.879269    -0.000169
H    4.087199    0.649176    0.879536
H    4.087472    0.649576    -0.879139
H    -2.969204    1.286915    -0.001944
H    -3.313827    -0.24422    0.907504
H    -3.314587    -0.246784    -0.906876
H    1.77003    1.340561    -4.2e-05
H    1.480205    -1.745131    -0.000628
""",
)

entry(
    index = 88,
    label = "CH3Br-2 + C2H5-2 <=> C2H5Br + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(100.514,'cm^3/(mol*s)'), n=3.04176, Ea=(46.6893,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.00697, dn = +|- 0.000912501, dEa = +|- 0.0049658 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)/ma-def2-tzvpp//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: CBr + C[CH2] <=> [CH3] + CCBr
barrier = 52.173802 kJ/mol
T1 = 0.016276514

Atom XYZ coordinates (angstrom)
Br    0.351332    -0.257356    0.357733
C    -2.563439    -0.734074    -0.254162
C    -1.780522    0.25958    0.546415
C    2.508884    -0.783433    0.169958
H    -2.407892    -1.746747    0.114489
H    -3.633096    -0.5116    -0.186511
H    -2.28063    -0.703215    -1.305194
H    -1.909681    0.209799    1.620928
H    -1.77951    1.275727    0.17065
H    2.803097    -0.972115    1.192852
H    2.937802    0.103933    -0.274007
H    2.492376    -1.654266    -0.470359
""",
)

entry(
    index = 89,
    label = "CHBrF2 + CH3 <=> CH3Br-2 + CHF2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(27055.4,'cm^3/(mol*s)'), n=2.71539, Ea=(45.3987,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.10821, dn = +|- 0.0134993, dEa = +|- 0.0734629 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)/ma-def2-tzvpp//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: FC(F)Br + [CH3] <=> F[CH]F + CBr
barrier = 50.926715 kJ/mol
T1 = 0.017312315

Atom XYZ coordinates (angstrom)
Br    -0.562974    0.016579    -0.033522
F    2.070956    -1.071353    0.280429
F    2.079335    1.093378    0.247339
C    -2.768784    0.029414    0.365342
C    1.578813    0.004012    -0.31978
H    -3.14783    0.626121    -0.452171
H    -2.826684    0.487941    1.34211
H    -3.017025    -1.021775    0.32932
H    1.74284    -0.013069    -1.393883
""",
)

entry(
    index = 90,
    label = "C3H6BrF + H <=> BrH-2 + C3H6F",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.74403e+08,'cm^3/(mol*s)'), n=1.67238, Ea=(15.7484,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.06849, dn = +|- 0.00870329, dEa = +|- 0.047363 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)/ma-def2-tzvpp//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: [H] + CC(C)(F)Br <=> Br + C[C](C)F
barrier = 18.565524 kJ/mol
T1 = 0.013736255

Atom XYZ coordinates (angstrom)
Br    -1.033828    0.000348    0.326505
F    1.494806    2.6e-05    1.428164
C    1.022567    9.2e-05    0.150696
C    1.421342    1.276737    -0.533374
C    1.421062    -1.27663    -0.533396
H    2.510877    1.303763    -0.60653
H    0.994199    1.318689    -1.532382
H    1.081552    2.135428    0.040368
H    0.993941    -1.318454    -1.532418
H    1.08105    -2.135254    0.040314
H    2.510593    -1.303916    -0.606518
H    -2.990783    -0.000808    0.553993
""",
)

entry(
    index = 91,
    label = "C2H3BrF2 + H <=> BrH-2 + C2H3F2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.84224e+08,'cm^3/(mol*s)'), n=1.70269, Ea=(14.8001,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.08005, dn = +|- 0.0101174, dEa = +|- 0.0550585 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)/ma-def2-tzvpp//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: FCC(F)Br + [H] <=> Br + F[CH]CF
barrier = 18.155190 kJ/mol
T1 = 0.014705893000000001

Atom XYZ coordinates (angstrom)
Br    -1.266761    -0.345472    0.045805
F    2.85756    -0.42738    -0.14643
F    0.82764    1.464496    0.316364
C    1.56355    -0.767429    0.190976
C    0.639655    0.297108    -0.327265
H    1.489088    -0.82869    1.2764
H    1.322721    -1.72714    -0.262734
H    0.679975    0.454395    -1.401184
H    -3.018251    -0.95058    0.464943
""",
)

entry(
    index = 92,
    label = "Br2 + O <=> BrO-2 + Br-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3.99317e+10,'cm^3/(mol*s)'), n=1.02274, Ea=(10.4443,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.00901, dn = +|- 0.00117892, dEa = +|- 0.00641564 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)/ma-def2-tzvpp//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: [O] + BrBr <=> [O]Br + [Br]
barrier = 11.028615 kJ/mol
T1 = 0.023276291

Atom XYZ coordinates (angstrom)
Br    0.027191    0.418676    -0.0
Br    -2.195333    -0.224603    0.0
O    2.168142    -0.194073    -0.0
""",
)

entry(
    index = 93,
    label = "BrHO-2 + H <=> BrH-2 + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.48676e+09,'cm^3/(mol*s)'), n=1.56674, Ea=(1.03064,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.02146, dn = +|- 0.00278924, dEa = +|- 0.0151789 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)/ma-def2-tzvpp//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: [H] + OBr <=> Br + [OH]
barrier = 2.694816 kJ/mol
T1 = 0.011909873

Atom XYZ coordinates (angstrom)
Br    -0.35781    0.201281    -0.170861
O    1.455407    -0.05391    -0.061992
H    1.780802    0.721645    0.409595
H    -2.520615    0.727558    -0.178844
""",
)

entry(
    index = 94,
    label = "CH3Br-2 + C2H3-2 <=> C2H3Br + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2164.02,'cm^3/(mol*s)'), n=3.18899, Ea=(28.382,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.05315, dn = +|- 0.00680414, dEa = +|- 0.0370279 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)/ma-def2-tzvpp//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: CBr + [CH]DC <=> [CH3] + CDCBr
barrier = 32.172150 kJ/mol
T1 = 0.017121598000000002

Atom XYZ coordinates (angstrom)
Br    -0.366111    0.22785    0.510029
C    2.571463    0.073606    -0.344221
C    1.825611    0.130322    0.727647
C    -2.481997    0.320909    0.222714
H    2.144444    0.073078    -1.339456
H    3.653792    0.024884    -0.262199
H    2.078505    0.140075    1.777222
H    -2.721384    -0.588311    -0.312337
H    -2.636284    1.224278    -0.352074
H    -2.886169    0.361867    1.225392
""",
)

entry(
    index = 95,
    label = "CBrF3 + H <=> BrH-2 + CF3-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.34913e+09,'cm^3/(mol*s)'), n=1.64247, Ea=(20.7613,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.06244, dn = +|- 0.00795771, dEa = +|- 0.0433056 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)/ma-def2-tzvpp//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: [H] + FC(F)(F)Br <=> Br + F[C](F)F
barrier = 23.319205 kJ/mol
T1 = 0.014542824

Atom XYZ coordinates (angstrom)
Br    1.051771    -0.461487    0.002636
F    -1.530782    -0.833131    -0.883632
F    -1.124253    1.199681    -0.313572
F    -1.42662    -0.300279    1.196615
C    -0.926863    -0.064814    0.000324
H    2.922319    -0.840455    0.006198
""",
)

entry(
    index = 96,
    label = "BrCl-2 + H <=> BrH-2 + Cl",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.81135e+11,'cm^3/(mol*s)'), n=0.513067, Ea=(0.995124,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.00484, dn = +|- 0.000634686, dEa = +|- 0.00345394 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)/ma-def2-tzvpp//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: ClBr + [H] <=> Br + [Cl]
barrier = 1.775028 kJ/mol
T1 = 0.008780426

Atom XYZ coordinates (angstrom)
Br    0.070978    0.001027    0.0
Cl    2.228285    0.014328    0.0
H    -2.299263    -0.015355    0.0
""",
)

entry(
    index = 97,
    label = "CH2BrF + H <=> BrH-2 + CH2F",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.49197e+08,'cm^3/(mol*s)'), n=1.7256, Ea=(21.4225,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.08513, dn = +|- 0.0107334, dEa = +|- 0.0584105 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)/ma-def2-tzvpp//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: [H] + FCBr <=> Br + [CH2]F
barrier = 24.940269 kJ/mol
T1 = 0.01582386

Atom XYZ coordinates (angstrom)
Br    -0.518619    0.396675    7e-06
F    2.275225    0.345293    -3e-06
C    1.286687    -0.566516    4e-06
H    1.297338    -1.147755    0.915081
H    1.297332    -1.147761    -0.91507
H    -2.142043    1.324009    1.3e-05
""",
)

entry(
    index = 98,
    label = "C2H5BrO-2 + H <=> BrH-2 + C2H5O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.13795e+09,'cm^3/(mol*s)'), n=1.58633, Ea=(2.31841,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.02389, dn = +|- 0.00310214, dEa = +|- 0.0168817 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)/ma-def2-tzvpp//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: CCOBr + [H] <=> Br + CC[O]
barrier = 4.799421 kJ/mol
T1 = 0.011720162

Atom XYZ coordinates (angstrom)
Br    0.97205    0.272399    0.293989
O    -0.579503    1.081126    -0.258689
C    -2.095437    -0.838367    -0.076253
C    -1.739217    0.559117    0.381138
H    -1.327263    -1.552688    0.217807
H    -2.201754    -0.865557    -1.159683
H    -3.037664    -1.147872    0.3759
H    -1.619554    0.60772    1.466292
H    -2.515051    1.27163    0.09228
H    2.774923    -0.917269    0.96058
""",
)

entry(
    index = 99,
    label = "CH3Br-2 + C3H7-3 <=> C3H7Br + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(54.6688,'cm^3/(mol*s)'), n=3.05096, Ea=(43.8864,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.0079, dn = +|- 0.00103425, dEa = +|- 0.00562837 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)/ma-def2-tzvpp//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: [CH2]CC + CBr <=> CCCBr + [CH3]
barrier = 48.908843 kJ/mol
T1 = 0.015518138

Atom XYZ coordinates (angstrom)
Br    0.731223    -0.11552    0.253409
C    -2.243195    -0.219006    -0.38015
C    -2.499962    1.188011    0.142926
C    2.764154    0.783661    0.048528
C    -1.277819    -1.003685    0.457249
H    -3.187315    -0.777576    -0.403594
H    -1.885493    -0.184108    -1.410904
H    -3.235406    1.705836    -0.470989
H    -2.876981    1.1555    1.166136
H    -1.580716    1.772127    0.142095
H    3.103417    0.855301    1.072314
H    2.565097    1.729277    -0.436049
H    3.286632    0.057876    -0.558664
H    -1.428001    -0.936679    1.529888
H    -1.074338    -2.013555    0.12163
""",
)

entry(
    index = 100,
    label = "Br2 + HO <=> BrHO-2 + Br-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.57257e+07,'cm^3/(mol*s)'), n=1.87634, Ea=(-2.06137,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.04568, dn = +|- 0.00586811, dEa = +|- 0.031934 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)/ma-def2-tzvpp//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: [OH] + BrBr <=> OBr + [Br]
barrier = 1.810130 kJ/mol
T1 = 0.022436781

Atom XYZ coordinates (angstrom)
Br    -0.705028    -0.312761    0.054859
Br    1.561067    0.150814    -0.029413
O    -2.854509    0.408474    -0.15131
H    -2.908265    1.058215    0.568547
""",
)

entry(
    index = 101,
    label = "C2H4BrF-2 + CH3 <=> CH3Br-2 + C2H4F-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(11790.3,'cm^3/(mol*s)'), n=2.75736, Ea=(45.9815,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.09856, dn = +|- 0.0123497, dEa = +|- 0.0672065 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)/ma-def2-tzvpp//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Br_Abstraction
Original entry: CC(F)Br + [CH3] <=> C[CH]F + CBr
barrier = 51.548113 kJ/mol
T1 = 0.016634915

Atom XYZ coordinates (angstrom)
Br    -0.564761    0.117667    0.032233
F    2.033666    1.331195    0.185725
C    2.195371    -1.015778    0.356625
C    -2.784886    0.121932    0.449048
C    1.588076    0.162841    -0.323548
H    1.983231    -0.983127    1.424014
H    1.789477    -1.934885    -0.059499
H    3.278716    -1.005058    0.211568
H    -2.879358    0.904484    1.188258
H    -3.203035    0.346353    -0.521828
H    -2.957387    -0.882136    0.809619
H    1.62212    0.192764    -1.407854
""",
)

