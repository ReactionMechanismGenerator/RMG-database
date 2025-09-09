#!/usr/bin/env python
# encoding: utf-8

name = "F_Abstraction/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "[OH]_r3 + FC(Cl)(Cl)Cl_r12 <=> Cl[C](Cl)Cl_p1 + OF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(30810.5,'cm^3/(mol*s)'), n=2.88761, Ea=(284.829,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.22877, dn = +|- 0.0270661, dEa = +|- 0.147293 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 1,
    label = "[OH]_r3 + [CH2]F_r12 <=> [CH2]_p1 + OF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2264.98,'cm^3/(mol*s)'), n=3.15133, Ea=(325.669,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.25436, dn = +|- 0.0297737, dEa = +|- 0.162027 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 2,
    label = "OOF_r12 + CH3 <=> [O]O_p1 + CH3F_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(849.095,'cm^3/(mol*s)'), n=3.17369, Ea=(16.5921,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.07688, dn = +|- 0.00973066, dEa = +|- 0.0529539 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 3,
    label = "C[C](C)F_r12 + CH3 <=> C[C]C_p1 + CH3F_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(44.7723,'cm^3/(mol*s)'), n=3.46134, Ea=(198.066,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.33304, dn = +|- 0.0377664, dEa = +|- 0.205523 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 4,
    label = "CDC(C)F_r12 + CH3 <=> CD[C]C_p1 + CH3F_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(25.027,'cm^3/(mol*s)'), n=3.59925, Ea=(209.739,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.41534, dn = +|- 0.0456373, dEa = +|- 0.248357 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 5,
    label = "CDCF_r12 + CH3 <=> [CH]DC_p1 + CH3F_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.7299,'cm^3/(mol*s)'), n=3.76087, Ea=(211.861,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.50616, dn = +|- 0.0538082, dEa = +|- 0.292822 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 6,
    label = "COF_r12 + CH3 <=> C[O]_p1 + CH3F_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(476.496,'cm^3/(mol*s)'), n=3.27616, Ea=(30.5726,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.1197, dn = +|- 0.0148542, dEa = +|- 0.0808358 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 7,
    label = "OD[C]F_r12 + CH3 <=> [C]DO_p1 + CH3F_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.28573,'cm^3/(mol*s)'), n=3.56699, Ea=(285.117,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.47481, dn = +|- 0.0510453, dEa = +|- 0.277787 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 8,
    label = "[OH]_r3 + FCCl_r12 <=> [CH2]Cl_p1 + OF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3819.03,'cm^3/(mol*s)'), n=3.24993, Ea=(296.719,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.30163, dn = +|- 0.0346344, dEa = +|- 0.188479 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 9,
    label = "CC(C)F_r12 + CH3 <=> C[CH]C_p1 + CH3F_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(12.1333,'cm^3/(mol*s)'), n=3.66599, Ea=(177.696,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.43808, dn = +|- 0.0477313, dEa = +|- 0.259752 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 10,
    label = "[O]_r3 + CDC(C)F_r12 <=> CD[C]C_p1 + [O]F_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.30096e+06,'cm^3/(mol*s)'), n=2.36151, Ea=(340.16,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.32769, dn = +|- 0.0372388, dEa = +|- 0.202652 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 11,
    label = "O[CH]F_r12 + CH3 <=> [CH]O_p1 + CH3F_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(22.5043,'cm^3/(mol*s)'), n=3.69111, Ea=(210.267,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.47535, dn = +|- 0.0510929, dEa = +|- 0.278045 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 12,
    label = "[O]_r3 + O[CH]F_r12 <=> [CH]O_p1 + [O]F_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.32859e+06,'cm^3/(mol*s)'), n=2.43214, Ea=(338.639,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.36874, dn = +|- 0.0412392, dEa = +|- 0.224422 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 13,
    label = "CCF_r12 + CH3 <=> C[CH2]_p1 + CH3F_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.55252,'cm^3/(mol*s)'), n=3.81157, Ea=(177.558,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.51478, dn = +|- 0.054558, dEa = +|- 0.296903 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 14,
    label = "C[CH]F_r12 + CH3 <=> [CH]C_p1 + CH3F_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(573.04,'cm^3/(mol*s)'), n=2.60489, Ea=(198.39,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.40606, dn = +|- 0.0447736, dEa = +|- 0.243656 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 15,
    label = "[O]O_r3 + [O]F_r12 <=> [O]_p1 + OOF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1110.26,'cm^3/(mol*s)'), n=2.89721, Ea=(154.45,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.14664, dn = +|- 0.0179773, dEa = +|- 0.0978319 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 16,
    label = "OCF_r12 + CH3 <=> [CH2]O_p1 + CH3F_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.29538,'cm^3/(mol*s)'), n=3.74, Ea=(187.567,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.45152, dn = +|- 0.048954, dEa = +|- 0.266406 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 17,
    label = "[O]O_r3 + O[CH]F_r12 <=> [CH]O_p1 + OOF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.55718,'cm^3/(mol*s)'), n=3.53988, Ea=(393.383,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.12198, dn = +|- 0.0151213, dEa = +|- 0.0822898 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 18,
    label = "[OH]_r3 + CDCDCF_r12 <=> [CH]DCDC_p1 + OF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(377.996,'cm^3/(mol*s)'), n=3.50982, Ea=(274.491,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.51727, dn = +|- 0.0547737, dEa = +|- 0.298076 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 19,
    label = "[OH]_r3 + C[C](C)F_r12 <=> C[C]C_p1 + OF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(95239.3,'cm^3/(mol*s)'), n=2.75763, Ea=(322.353,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.09238, dn = +|- 0.0116086, dEa = +|- 0.0631737 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 20,
    label = "C[C](O)F_r12 + CH3 <=> C[C]O_p1 + CH3F_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(35.032,'cm^3/(mol*s)'), n=3.5135, Ea=(211.783,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.38305, dn = +|- 0.0426058, dEa = +|- 0.231859 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 21,
    label = "[O]O_r3 + C[C](C)F_r12 <=> C[C]C_p1 + OOF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(115.787,'cm^3/(mol*s)'), n=3.43806, Ea=(384.463,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.10975, dn = +|- 0.0136817, dEa = +|- 0.0744553 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 22,
    label = "[OH]_r3 + CD[C]F_r12 <=> [C]DC_p1 + OF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(38723.5,'cm^3/(mol*s)'), n=2.8378, Ea=(400.231,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.12789, dn = +|- 0.0158118, dEa = +|- 0.0860473 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 23,
    label = "[O]_r3 + COF_r12 <=> C[O]_p1 + [O]F_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(640932,'cm^3/(mol*s)'), n=2.39839, Ea=(106.019,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.45066, dn = +|- 0.048876, dEa = +|- 0.265982 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 24,
    label = "[O]O_r3 + FCCl_r12 <=> [CH2]Cl_p1 + OOF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.65995,'cm^3/(mol*s)'), n=3.94804, Ea=(353.81,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.32684, dn = +|- 0.0371544, dEa = +|- 0.202193 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 25,
    label = "[OH]_r3 + CCCF_r12 <=> [CH2]CC_p1 + OF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1525.14,'cm^3/(mol*s)'), n=3.216, Ea=(295.362,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.25443, dn = +|- 0.0297815, dEa = +|- 0.16207 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 26,
    label = "[O]O_r3 + CDC(C)F_r12 <=> CD[C]C_p1 + OOF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(83.8302,'cm^3/(mol*s)'), n=3.60203, Ea=(402.485,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.16775, dn = +|- 0.0203741, dEa = +|- 0.110875 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 27,
    label = "[O]O_r3 + CCCF_r12 <=> [CH2]CC_p1 + OOF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.69582,'cm^3/(mol*s)'), n=3.94767, Ea=(359.86,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.31489, dn = +|- 0.0359654, dEa = +|- 0.195722 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 28,
    label = "CCCF_r12 + CH3 <=> [CH2]CC_p1 + CH3F_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.51365,'cm^3/(mol*s)'), n=3.78897, Ea=(180.153,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.50469, dn = +|- 0.05368, dEa = +|- 0.292125 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 29,
    label = "[OH]_r3 + CC(C)CF_r12 <=> [CH2]C(C)C_p1 + OF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1858.43,'cm^3/(mol*s)'), n=3.22261, Ea=(297.595,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.26549, dn = +|- 0.0309346, dEa = +|- 0.168345 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 30,
    label = "[OH]_r3 + CC(C)F_r12 <=> C[CH]C_p1 + OF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(84232.2,'cm^3/(mol*s)'), n=3.00838, Ea=(296.124,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.17169, dn = +|- 0.0208173, dEa = +|- 0.113287 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 31,
    label = "[OH]_r3 + C#CF_r12 <=> [C]#C_p1 + OF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.72013e+06,'cm^3/(mol*s)'), n=2.4493, Ea=(387.834,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.21764, dn = +|- 0.0258702, dEa = +|- 0.140785 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 32,
    label = "CC(O)F_r12 + CH3 <=> C[CH]O_p1 + CH3F_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(33.8922,'cm^3/(mol*s)'), n=3.5758, Ea=(187.056,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.36885, dn = +|- 0.0412495, dEa = +|- 0.224478 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 33,
    label = "[OH]_r3 + CDC(C)F_r12 <=> CD[C]C_p1 + OF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(37912.1,'cm^3/(mol*s)'), n=2.90824, Ea=(340.726,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.14025, dn = +|- 0.017243, dEa = +|- 0.093836 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 34,
    label = "[OH]_r3 + O[CH]F_r12 <=> [CH]O_p1 + OF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4745.79,'cm^3/(mol*s)'), n=2.96408, Ea=(334.468,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.16288, dn = +|- 0.0198253, dEa = +|- 0.107889 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 35,
    label = "[OH]_r3 + OCF_r12 <=> [CH2]O_p1 + OF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6788.58,'cm^3/(mol*s)'), n=3.1372, Ea=(304.788,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.23148, dn = +|- 0.027355, dEa = +|- 0.148865 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 36,
    label = "[OH]_r3 + O[C](O)F_r12 <=> O[C]O_p1 + OF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(44601.2,'cm^3/(mol*s)'), n=2.65475, Ea=(354.674,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.03298, dn = +|- 0.00426297, dEa = +|- 0.0231989 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 37,
    label = "[O]O_r3 + CDCF_r12 <=> [CH]DC_p1 + OOF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(25.7682,'cm^3/(mol*s)'), n=3.82266, Ea=(406.027,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.25384, dn = +|- 0.0297197, dEa = +|- 0.161733 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 38,
    label = "[O]O_r3 + CCF_r12 <=> C[CH2]_p1 + OOF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.27349,'cm^3/(mol*s)'), n=3.9638, Ea=(356.126,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.31123, dn = +|- 0.0355991, dEa = +|- 0.193729 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 39,
    label = "O[C](O)F_r12 + CH3 <=> O[C]O_p1 + CH3F_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(17.1639,'cm^3/(mol*s)'), n=3.56319, Ea=(226.133,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.41562, dn = +|- 0.0456631, dEa = +|- 0.248497 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 40,
    label = "[OH]_r3 + C#COF_r12 <=> C#C[O]_p1 + OF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(48753.5,'cm^3/(mol*s)'), n=3.06244, Ea=(13.9612,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.20559, dn = +|- 0.0245637, dEa = +|- 0.133675 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 41,
    label = "[OH]_r3 + C[CH]F_r12 <=> [CH]C_p1 + OF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6632.77,'cm^3/(mol*s)'), n=2.95236, Ea=(324.109,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.1674, dn = +|- 0.0203347, dEa = +|- 0.110661 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 42,
    label = "H2CCFCF3+ CF3 <=> H2CCFCF2 + CF4_p23",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(1.15503,'cm^3/(mol*s)'), n=3.92844, Ea=(168.206,'kJ/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """M062X-D3/Jun-cc-pvtz Gaussian16""",
    longDesc = 
"""
Fitted to 50 data points; dA = *|/ 1.53415, dn = +|- 0.0562276, dEa = +|- 0.305988 kJ/mol
""",
)

entry(
    index = 43,
    label = "C2H4F2 + H <=> HF + C2H4F",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(0.000369729,'cm^3/(mol*s)'), n=5.13872, Ea=(109.875,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 17.0502, dn = +|- 0.372615, dEa = +|- 2.02776 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/F_Abstraction
Original entry: [H] + CC(F)F <=> F + C[CH]F
barrier = 144.785929 kJ/mol
T1 = 0.019873555

Atom XYZ coordinates (angstrom)
F    -1.276037    -0.422824    -0.092604
F    0.207995    1.425564    -0.114026
C    1.228187    -0.700299    -0.151436
C    0.201452    0.202675    0.415724
H    1.125246    -0.736197    -1.234468
H    1.104975    -1.700255    0.257123
H    2.227811    -0.33496    0.096224
H    0.044071    0.238085    1.486035
H    -2.372446    -0.802889    -0.494631
""",
)

entry(
    index = 44,
    label = "C2F4O + H <=> HF + C2F3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.80067e-14,'cm^3/(mol*s)'), n=8.17077, Ea=(92.4857,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 166.8, dn = +|- 0.672245, dEa = +|- 3.65833 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/F_Abstraction
Original entry: ODC(F)C(F)(F)F + [H] <=> F + OD[C]C(F)(F)F
barrier = 152.724171 kJ/mol
T1 = 0.020227394

Atom XYZ coordinates (angstrom)
F    -1.502967    -1.004692    -0.229658
F    -0.994061    1.005821    -0.812777
F    -0.838614    0.415951    1.255472
F    1.668863    0.868287    0.081303
O    1.231694    -1.494261    -0.207348
C    -0.687893    0.010399    0.002105
C    0.772994    -0.430347    -0.215057
H    2.300698    1.710332    0.754304
""",
)

entry(
    index = 45,
    label = "FCCl_r12 + H <=> HF + CH2Cl",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.57367e-05,'cm^3/(mol*s)'), n=5.32561, Ea=(91.9755,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 17.9751, dn = +|- 0.379556, dEa = +|- 2.06553 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/F_Abstraction
Original entry: [H] + FCCl <=> F + [CH2]Cl
barrier = 128.611746 kJ/mol
T1 = 0.020854513999999998

Atom XYZ coordinates (angstrom)
Cl    1.298753    -0.003353    -0.013216
F    -1.396283    -0.437233    0.003567
C    -0.253375    0.741845    0.000452
H    -0.458488    1.260827    0.923657
H    -0.471132    1.268239    -0.915623
H    -2.294781    -1.312539    0.001159
""",
)

entry(
    index = 46,
    label = "FHO + C2H5 <=> CCF_r12 + [OH]_r3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.5246,'cm^3/(mol*s)'), n=3.31308, Ea=(11.0929,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.1113, dn = +|- 0.0138643, dEa = +|- 0.075449 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/F_Abstraction
Original entry: OF + C[CH2] <=> [OH] + CCF
barrier = 18.858000 kJ/mol
T1 = 0.02348946

Atom XYZ coordinates (angstrom)
F    0.804599    -0.100085    0.170951
O    2.278491    0.356019    0.212016
C    -1.797113    0.76033    -0.047691
C    -1.234276    -0.600387    0.102201
H    -1.437062    1.235778    -0.958657
H    -2.8916    0.725455    -0.105134
H    -1.534317    1.389427    0.80126
H    -1.243823    -1.083263    1.067112
H    -1.143047    -1.242828    -0.759924
H    2.657662    -0.528205    0.31025
""",
)

entry(
    index = 47,
    label = "F2 + H <=> HF + F",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(5.87291e+10,'cm^3/(mol*s)'), n=0.785655, Ea=(4.07732,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.09714, dn = +|- 0.0121793, dEa = +|- 0.066279 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/F_Abstraction
Original entry: FF + [H] <=> F + [F]
barrier = 8.292720 kJ/mol
T1 = 0.025998498

Atom XYZ coordinates (angstrom)
F    -0.099421    -0.000828    -0.0
F    -1.518443    -0.016082    0.0
H    1.617864    0.01691    -0.0
""",
)

entry(
    index = 48,
    label = "OCF_r12 + CH2F <=> CH2F2 + CH3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.219252,'cm^3/(mol*s)'), n=3.91175, Ea=(165.902,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.52273, dn = +|- 0.0552462, dEa = +|- 0.300648 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/F_Abstraction
Original entry: OCF + [CH2]F <=> FCF + [CH2]O
barrier = 177.344590 kJ/mol
T1 = 0.020983436

Atom XYZ coordinates (angstrom)
F    -0.002711    0.025473    0.358744
F    -1.727391    0.696884    -1.214299
O    2.256137    0.237664    -0.746115
C    1.741943    -0.464422    0.278985
C    -1.659059    0.597359    0.115796
H    2.104025    -0.125747    1.236464
H    1.585925    -1.525563    0.137642
H    -1.654315    1.556598    0.611413
H    -2.258104    -0.210174    0.509886
H    1.884412    -0.072476    -1.577222
""",
)

entry(
    index = 49,
    label = "CH2F2 + C3H6F <=> C3H6F2 + CH2F",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(0.0262173,'cm^3/(mol*s)'), n=4.12499, Ea=(167.866,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.66336, dn = +|- 0.0668515, dEa = +|- 0.363804 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/F_Abstraction
Original entry: CC[CH]F + FCF <=> CCC(F)F + [CH2]F
barrier = 178.864314 kJ/mol
T1 = 0.018259453000000002

Atom XYZ coordinates (angstrom)
F    0.65184    0.457502    0.390608
F    2.360251    -1.115367    -0.297629
F    -1.174894    1.903745    -0.366389
C    -1.57919    -0.427431    -0.542486
C    -1.414685    -1.739752    0.21358
C    2.367239    0.07392    0.30678
C    -1.112898    0.725337    0.261061
H    -1.00719    -0.440128    -1.472749
H    -2.628589    -0.265982    -0.814518
H    -0.364752    -1.919458    0.436668
H    -1.968162    -1.721246    1.153227
H    -1.789194    -2.572529    -0.378014
H    2.753768    0.865061    -0.318316
H    2.65605    0.018204    1.345982
H    -1.37519    0.810484    1.30853
""",
)

entry(
    index = 50,
    label = "COF_r12 + C2H3 <=> CDCF_r12 + CH3O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(28.2278,'cm^3/(mol*s)'), n=3.44719, Ea=(10.5481,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.16431, dn = +|- 0.0199864, dEa = +|- 0.108765 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/F_Abstraction
Original entry: [CH]DC + COF <=> CDCF + C[O]
barrier = 16.460094 kJ/mol
T1 = 0.024369475

Atom XYZ coordinates (angstrom)
F    -0.165037    -0.477846    -0.673418
O    -1.711016    -0.536175    -0.724349
C    -2.087265    -0.006889    0.510432
C    2.262686    0.142644    0.622832
C    1.870573    -0.358316    -0.50785
H    -1.722906    -0.618254    1.337778
H    -3.180129    -0.040927    0.490927
H    -1.761394    1.028885    0.620007
H    1.547334    0.453862    1.376742
H    3.317863    0.268113    0.854656
H    2.267163    -0.748855    -1.426998
""",
)

entry(
    index = 51,
    label = "OCF_r12 + CHF2 <=> CHF3 + CH3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0632707,'cm^3/(mol*s)'), n=4.09227, Ea=(155.795,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.59478, dn = +|- 0.0613198, dEa = +|- 0.3337 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/F_Abstraction
Original entry: OCF + F[CH]F <=> FC(F)F + [CH2]O
barrier = 165.745185 kJ/mol
T1 = 0.020513744

Atom XYZ coordinates (angstrom)
F    -0.253832    -0.38139    0.239176
F    2.086192    -0.775974    -0.401164
F    1.524255    1.27555    0.014983
O    -2.554458    0.61192    -0.097506
C    -2.010817    -0.616874    -0.109852
C    1.45188    0.025771    0.433052
H    -1.901422    -1.112289    -1.065377
H    -2.310611    -1.210181    0.739218
H    1.72863    -0.10841    1.472028
H    -2.27769    1.1059    -0.874693
""",
)

entry(
    index = 52,
    label = "OCF_r12 + C2H4F <=> C2H4F2 + CH3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0411856,'cm^3/(mol*s)'), n=4.0381, Ea=(156.944,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.58012, dn = +|- 0.0601061, dEa = +|- 0.327095 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/F_Abstraction
Original entry: OCF + C[CH]F <=> CC(F)F + [CH2]O
barrier = 167.211341 kJ/mol
T1 = 0.019755943

Atom XYZ coordinates (angstrom)
F    -0.279479    0.283748    -0.553053
F    1.505263    -1.339215    -0.220277
O    -2.3145    -0.165602    0.855416
C    1.937397    0.810383    0.663678
C    -2.081922    0.346037    -0.368654
C    1.482601    -0.020159    -0.469831
H    2.978973    0.597294    0.921864
H    1.314298    0.606538    1.535142
H    1.84741    1.863172    0.404919
H    -2.341264    -0.259661    -1.226613
H    -2.271352    1.406454    -0.416994
H    1.784515    0.198258    -1.484806
H    -2.107224    -1.104813    0.860549
""",
)

entry(
    index = 53,
    label = "CCF_r12 + H <=> HF + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.00518265,'cm^3/(mol*s)'), n=4.74784, Ea=(92.3732,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 10.6934, dn = +|- 0.311322, dEa = +|- 1.6942 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/F_Abstraction
Original entry: CCF + [H] <=> F + C[CH2]
barrier = 123.490179 kJ/mol
T1 = 0.021647543999999998

Atom XYZ coordinates (angstrom)
F    -1.257558    -0.090257    -0.059463
C    1.246104    -0.351206    -0.010289
C    0.207014    0.715441    -0.028545
H    1.142488    -0.979901    0.871945
H    2.243241    0.097813    0.010036
H    1.177087    -0.976458    -0.898342
H    0.096924    1.299507    0.875201
H    0.132789    1.303475    -0.933365
H    -2.338491    -0.685124    -0.084445
""",
)

entry(
    index = 54,
    label = "OOF_r12 + C3H7 <=> CC(C)F_r12 + [O]O_r3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(41.1983,'cm^3/(mol*s)'), n=3.20075, Ea=(2.44607,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.07615, dn = +|- 0.00964146, dEa = +|- 0.0524685 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/F_Abstraction
Original entry: OOF + C[CH]C <=> CC(C)F + [O]O
barrier = 6.579862 kJ/mol

Atom XYZ coordinates (angstrom)
F    0.652517    0.162893    -0.414314
O    2.440983    -0.200078    0.966236
O    2.170238    0.309475    -0.251034
C    -1.863695    1.453345    -0.179548
C    -1.676752    -0.937661    0.740143
C    -1.593996    0.011279    -0.396754
H    -1.554561    2.054707    -1.03236
H    -1.336052    1.812034    0.706491
H    -2.933172    1.636273    -0.01255
H    -1.295909    -1.922341    0.474602
H    -1.105234    -0.561725    1.592139
H    -2.712656    -1.06273    1.080582
H    -1.64663    -0.379059    -1.402864
H    2.525117    -1.152859    0.808864
""",
)

entry(
    index = 55,
    label = "OCF_r12 + H <=> HF + CH3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0331829,'cm^3/(mol*s)'), n=4.48236, Ea=(100.723,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 8.92149, dn = +|- 0.28752, dEa = +|- 1.56468 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/F_Abstraction
Original entry: OCF + [H] <=> F + [CH2]O
barrier = 129.951334 kJ/mol
T1 = 0.023364632000000003

Atom XYZ coordinates (angstrom)
F    -1.205248    -0.191272    0.071702
O    1.244228    -0.36335    -0.133039
C    0.311733    0.577024    0.076559
H    0.207836    1.23872    -0.769353
H    0.26894    1.024149    1.061538
H    1.371964    -0.894623    0.658318
H    -2.294241    -0.780252    0.044176
""",
)

entry(
    index = 56,
    label = "C2F4O + C2F5 <=> C2F6 + C2F3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.95992,'cm^3/(mol*s)'), n=3.05765, Ea=(179.705,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.65026, dn = +|- 0.0658128, dEa = +|- 0.358151 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/F_Abstraction
Original entry: ODC(F)C(F)(F)F + F[C](F)C(F)(F)F <=> FC(F)(F)C(F)(F)F + OD[C]C(F)(F)F
barrier = 188.011650 kJ/mol

Atom XYZ coordinates (angstrom)
F    -2.739262    -1.201907    -0.327388
F    -3.769185    0.620114    0.182391
F    -2.096818    -0.046806    1.376715
F    2.572011    0.919065    -0.97456
F    1.846864    1.166505    1.048548
F    3.48761    -0.174045    0.643859
F    -0.135148    -0.050218    -0.618248
F    0.986028    -1.433417    1.053681
F    1.682328    -1.661175    -0.984795
O    -1.625697    1.941025    -1.031857
C    -2.58833    0.023585    0.14714
C    2.334053    0.302347    0.171168
C    1.340589    -0.82463    -0.044628
C    -1.607749    0.820571    -0.740089
""",
)

entry(
    index = 57,
    label = "COF_r12 + [OH]_r3 <=> FHO + CH3O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4986.4,'cm^3/(mol*s)'), n=3.19625, Ea=(104.62,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.366, dn = +|- 0.0409756, dEa = +|- 0.222988 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/F_Abstraction
Original entry: [OH] + COF <=> OF + C[O]
barrier = 113.402921 kJ/mol

Atom XYZ coordinates (angstrom)
F    0.566363    -0.161798    0.136018
O    -1.103679    -0.634639    0.207768
O    2.223839    0.345708    0.084764
C    -1.754509    0.566338    0.001682
H    -1.543971    0.986362    -0.982841
H    -2.815916    0.281702    0.041967
H    -1.556981    1.28479    0.798507
H    2.535716    -0.537096    0.339306
""",
)

entry(
    index = 58,
    label = "F2 + CFO <=> CF2O + F",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(9337.54,'cm^3/(mol*s)'), n=2.7407, Ea=(1.59476,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.07704, dn = +|- 0.00975049, dEa = +|- 0.0530618 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/F_Abstraction
Original entry: OD[C]F + FF <=> ODC(F)F + [F]
barrier = 5.229848 kJ/mol
T1 = 0.027186917999999997

Atom XYZ coordinates (angstrom)
F    -1.071995    0.155481    0.003107
F    1.290207    -1.217077    0.019216
F    -2.517918    0.160946    -0.003875
O    1.771833    0.963845    -0.021043
C    1.04825    0.062577    -0.001094
""",
)

entry(
    index = 59,
    label = "CCCF_r12 + CH2F <=> CH2F2 + C3H7-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0780562,'cm^3/(mol*s)'), n=3.96948, Ea=(152.853,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.56523, dn = +|- 0.0588623, dEa = +|- 0.320327 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/F_Abstraction
Original entry: [CH2]F + CCCF <=> FCF + [CH2]CC
barrier = 164.931367 kJ/mol
T1 = 0.01835972

Atom XYZ coordinates (angstrom)
F    0.657336    -0.19457    0.447099
F    1.578398    0.398962    -1.720486
C    -1.846426    -0.480813    -0.030854
C    -1.964543    0.964271    -0.500565
C    -0.930398    -0.634688    1.132232
C    2.081487    0.270891    -0.491597
H    -2.836627    -0.863126    0.245173
H    -1.490895    -1.114735    -0.846118
H    -2.332572    1.602343    0.304299
H    -2.653177    1.050117    -1.339795
H    -0.99211    1.339642    -0.81517
H    -0.707557    -1.636934    1.470179
H    -1.000257    0.104144    1.920252
H    2.727149    -0.587968    -0.385188
H    2.361578    1.214767    -0.048001
""",
)

entry(
    index = 60,
    label = "C2H4F2-2 + CH2F <=> CH2F2 + C2H4F-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(0.206542,'cm^3/(mol*s)'), n=3.97927, Ea=(151.975,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.58146, dn = +|- 0.0602183, dEa = +|- 0.327706 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/F_Abstraction
Original entry: [CH2]F + FCCF <=> FCF + [CH2]CF
barrier = 164.199766 kJ/mol
T1 = 0.018860778

Atom XYZ coordinates (angstrom)
F    0.402708    0.087328    -0.314187
F    -2.082254    -0.958742    0.857201
F    1.827396    0.607191    1.591349
C    -1.23725    0.396082    -0.866069
C    -2.017803    0.341741    0.390763
C    1.961454    -0.145589    0.501953
H    -1.122585    1.375434    -1.308843
H    -1.388915    -0.418779    -1.559857
H    -3.046366    0.685084    0.238244
H    -1.549461    0.955492    1.163035
H    1.945506    -1.204715    0.710254
H    2.662448    0.259431    -0.212552
""",
)

entry(
    index = 61,
    label = "[O]F_r12 + CH3O <=> OCF_r12 + [O]_r3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(576.508,'cm^3/(mol*s)'), n=2.8908, Ea=(21.561,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.16878, dn = +|- 0.0204899, dEa = +|- 0.111505 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/F_Abstraction
Original entry: [CH2]O + [O]F <=> OCF + [O]
barrier = 28.932754 kJ/mol

Atom XYZ coordinates (angstrom)
F    -0.908476    0.199098    -0.012355
O    1.783707    -0.635967    -0.104791
O    -2.352588    -0.149484    -0.02351
C    1.22714    0.577242    0.01615
H    1.273492    1.174655    -0.878198
H    1.170521    1.038865    0.990222
H    1.734185    -1.116077    0.726531
""",
)

entry(
    index = 62,
    label = "CCF_r12 + CH2F <=> CH2F2 + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.135777,'cm^3/(mol*s)'), n=3.96896, Ea=(156.525,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.57046, dn = +|- 0.0593008, dEa = +|- 0.322713 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/F_Abstraction
Original entry: [CH2]F + CCF <=> FCF + C[CH2]
barrier = 168.533751 kJ/mol
T1 = 0.019506969

Atom XYZ coordinates (angstrom)
F    -1.961769    0.928113    -0.626329
F    -0.191656    -0.575111    0.096485
C    1.93255    0.838197    -0.091662
C    -1.918385    -0.33618    -0.205719
C    1.575517    -0.546272    0.315774
H    1.429307    1.568744    0.540323
H    3.010489    1.007616    -0.007907
H    1.644555    1.022914    -1.125732
H    -2.122107    -1.051075    -0.988979
H    -2.350658    -0.472264    0.774432
H    1.854853    -1.352701    -0.347327
H    1.632984    -0.791009    1.366897
""",
)

entry(
    index = 63,
    label = "CF2 + H <=> HF + CF",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.08514e-36,'cm^3/(mol*s)'), n=14.3629, Ea=(28.7199,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1087.21, dn = +|- 0.918527, dEa = +|- 4.99859 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/F_Abstraction
Original entry: [H] + F[C]F <=> F + [C]F
barrier = 153.465402 kJ/mol

Atom XYZ coordinates (angstrom)
F    -1.068255    -0.000581    -0.142797
F    1.026537    -0.361944    -0.001483
C    0.22657    0.6491    0.1072
H    -1.720517    -0.745746    0.592873
""",
)

entry(
    index = 64,
    label = "COF_r12 + H <=> HF + CH3O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.04105e+06,'cm^3/(mol*s)'), n=2.3137, Ea=(11.5771,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.40006, dn = +|- 0.0442111, dEa = +|- 0.240595 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/F_Abstraction
Original entry: [H] + COF <=> F + C[O]
barrier = 23.212090 kJ/mol
T1 = 0.02344863

Atom XYZ coordinates (angstrom)
F    1.092066    0.258695    -0.002018
O    -0.13638    -0.613436    -0.004237
C    -1.19673    0.300823    0.001168
H    -1.192414    0.920592    -0.895437
H    -2.081826    -0.340279    -0.000764
H    -1.190363    0.912365    0.903394
H    2.358711    1.163876    -0.002106
""",
)

entry(
    index = 65,
    label = "FHO + C2H4O <=> C[C](O)F_r12 + [OH]_r3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(34.878,'cm^3/(mol*s)'), n=3.33904, Ea=(-1.9829,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.09217, dn = +|- 0.0115834, dEa = +|- 0.0630363 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/F_Abstraction
Original entry: OF + C[C]O <=> [OH] + C[C](O)F
barrier = 2.145507 kJ/mol
T1 = 0.02333748

Atom XYZ coordinates (angstrom)
F    -0.994392    -0.157019    -0.149549
O    1.107953    1.398025    0.054567
O    -2.469147    -0.192056    0.244033
C    1.686417    -1.023815    0.146718
C    1.109534    0.18377    -0.474697
H    1.535679    -1.883681    -0.50132
H    2.760878    -0.892294    0.307492
H    1.212478    -1.22472    1.112591
H    0.227918    1.614676    0.398067
H    -2.808661    -0.455206    -0.622983
""",
)

entry(
    index = 66,
    label = "C2F6 + H <=> HF + C2F5",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(1.06547e-07,'cm^3/(mol*s)'), n=6.28933, Ea=(117.804,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 49.9733, dn = +|- 0.513892, dEa = +|- 2.79658 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/F_Abstraction
Original entry: FC(F)(F)C(F)(F)F + [H] <=> F + F[C](F)C(F)(F)F
barrier = 162.851115 kJ/mol
T1 = 0.016654017

Atom XYZ coordinates (angstrom)
F    1.63471    0.951969    0.001168
F    0.982711    -1.03957    -1.082699
F    0.982534    -1.042668    1.079202
F    -1.607392    -0.902636    -0.001839
F    -0.98506    0.858927    -1.080297
F    -0.985285    0.855717    1.081973
C    0.674677    -0.376791    -0.000821
C    -0.76295    0.128413    -0.000221
H    2.425379    1.907618    0.002506
""",
)

entry(
    index = 67,
    label = "FHO + C4H9 <=> C4H9F + [OH]_r3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(166.381,'cm^3/(mol*s)'), n=3.31384, Ea=(-1.84829,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.09474, dn = +|- 0.0118927, dEa = +|- 0.0647194 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/F_Abstraction
Original entry: OF + C[C](C)C <=> [OH] + CC(C)(C)F
barrier = 1.412500 kJ/mol
T1 = 0.018614728

Atom XYZ coordinates (angstrom)
F    1.255815    -0.3214    0.209324
O    2.738647    -0.520046    0.484306
C    -0.87776    -0.035557    -0.18637
C    -1.37227    -1.164853    0.645062
C    -0.826209    -0.215012    -1.661737
C    -1.001919    1.345179    0.352325
H    -0.971807    -2.116136    0.29556
H    -2.467959    -1.231521    0.59797
H    -1.098652    -1.034857    1.692052
H    -0.446658    -1.201815    -1.925728
H    -1.829626    -0.120515    -2.099573
H    -0.193745    0.538814    -2.13022
H    -0.36246    2.040566    -0.191689
H    -0.742486    1.381766    1.410632
H    -2.034372    1.708952    0.257677
H    2.901958    0.35851    0.85335
""",
)

entry(
    index = 68,
    label = "COF_r12 + CH2Cl <=> FCCl_r12 + CH3O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.19658,'cm^3/(mol*s)'), n=3.30549, Ea=(14.6127,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.11724, dn = +|- 0.0145653, dEa = +|- 0.0792638 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/F_Abstraction
Original entry: [CH2]Cl + COF <=> FCCl + C[O]
barrier = 23.162146 kJ/mol
T1 = 0.025357931

Atom XYZ coordinates (angstrom)
Cl    -2.167263    -0.422016    -0.00506
F    0.560641    0.736143    -0.048105
O    2.083878    0.329317    -0.036261
C    2.024979    -1.062241    0.011695
C    -1.437363    1.110884    -0.058228
H    1.538999    -1.41522    0.922865
H    3.07503    -1.370272    0.020642
H    1.536201    -1.476928    -0.871555
H    -1.444527    1.605142    -1.013699
H    -1.442053    1.668997    0.861421
""",
)

entry(
    index = 69,
    label = "C2H3F3 + CH2F <=> CH2F2 + C2H3F2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(0.700958,'cm^3/(mol*s)'), n=3.85832, Ea=(170.202,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.5478, dn = +|- 0.0573912, dEa = +|- 0.312321 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/F_Abstraction
Original entry: FCC(F)F + [CH2]F <=> F[CH]CF + FCF
barrier = 181.546052 kJ/mol
T1 = 0.018937824

Atom XYZ coordinates (angstrom)
F    -2.902071    -0.598747    0.55683
F    0.749275    0.117521    -0.187431
F    2.303911    -1.764391    -0.084943
F    -1.249355    0.983112    -1.279779
C    -1.537078    -0.728677    0.329141
C    2.407603    -0.482891    -0.423039
C    -0.94583    0.574145    -0.050228
H    -1.393274    -1.446989    -0.4774
H    -1.069149    -1.090019    1.243191
H    2.96531    0.104005    0.291454
H    2.547088    -0.328643    -1.482466
H    -0.910102    1.389116    0.659403
""",
)

entry(
    index = 70,
    label = "COF_r12 + C3H7-2 <=> CCCF_r12 + CH3O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.20903,'cm^3/(mol*s)'), n=3.28294, Ea=(7.36724,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.09983, dn = +|- 0.0125013, dEa = +|- 0.0680315 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/F_Abstraction
Original entry: [CH2]CC + COF <=> CCCF + C[O]
barrier = 14.117448 kJ/mol
T1 = 0.021105737000000003

Atom XYZ coordinates (angstrom)
F    0.63725    -0.755181    -0.22421
O    2.096024    -0.260885    -0.450804
C    -1.80516    0.15889    0.591916
C    -1.830073    1.155158    -0.561832
C    2.233212    0.738614    0.511293
C    -1.384391    -1.198108    0.169494
H    -2.800499    0.102413    1.052456
H    -1.135626    0.507848    1.383095
H    -2.531881    0.832957    -1.331939
H    -0.843744    1.229525    -1.018443
H    -2.133173    2.144946    -0.223578
H    3.247646    1.119033    0.362191
H    1.51984    1.55056    0.353643
H    2.143026    0.339916    1.523552
H    -1.170524    -1.954809    0.908493
H    -1.603749    -1.538999    -0.831871
""",
)

entry(
    index = 71,
    label = "CCF_r12 + CHO <=> CHFO + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0911574,'cm^3/(mol*s)'), n=4.14961, Ea=(160.609,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.82008, dn = +|- 0.078681, dEa = +|- 0.428179 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/F_Abstraction
Original entry: [CH]DO + CCF <=> ODCF + C[CH2]
barrier = 174.923532 kJ/mol
T1 = 0.044551614

Atom XYZ coordinates (angstrom)
F    0.254421    -0.422932    0.945447
O    1.498641    -1.318882    -0.892619
C    -1.742614    0.560901    -0.244477
C    -1.518969    -0.353247    0.898541
C    1.399101    -0.370014    -0.201378
H    -1.292817    1.53608    -0.055915
H    -1.318704    0.146979    -1.159985
H    -2.811858    0.713405    -0.412633
H    -1.723842    -1.404655    0.761045
H    -1.686295    0.020805    1.897989
H    1.400613    0.699171    -0.461247
""",
)

entry(
    index = 72,
    label = "C2F4O + CF3 <=> CF4 + C2F3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.47232,'cm^3/(mol*s)'), n=3.97637, Ea=(171.25,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.56352, dn = +|- 0.0587191, dEa = +|- 0.319547 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/F_Abstraction
Original entry: ODC(F)C(F)(F)F + F[C](F)F <=> FC(F)(F)F + OD[C]C(F)(F)F
barrier = 179.214366 kJ/mol
T1 = 0.019712905

Atom XYZ coordinates (angstrom)
F    -1.464385    -1.186864    0.636442
F    -1.551096    -0.857431    -1.493107
F    -3.152172    -0.156616    -0.234107
F    1.983348    -1.266483    0.622518
F    2.635766    0.719654    1.16131
F    2.86374    0.022707    -0.869369
F    0.540244    0.580456    -0.174268
O    -1.461693    1.965066    0.411778
C    -1.843512    -0.33912    -0.311216
C    2.152734    -0.0391    0.219825
C    -1.099295    0.998794    -0.116414
""",
)

entry(
    index = 73,
    label = "OOF_r12 + CH2 <=> [CH2]F_r12 + [O]O_r3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(178.698,'cm^3/(mol*s)'), n=3.25898, Ea=(11.1651,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.10437, dn = +|- 0.0130431, dEa = +|- 0.0709798 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/F_Abstraction
Original entry: OOF + [CH2] <=> [O]O + [CH2]F
barrier = 18.309197 kJ/mol
T1 = 0.032551678

Atom XYZ coordinates (angstrom)
F    0.408093    -0.222131    0.026151
O    -1.795151    0.476396    0.00244
O    -1.09148    -0.661308    0.045592
C    2.428516    0.382705    0.014036
H    2.502103    0.951334    0.922708
H    2.93043    -0.490136    -0.361131
H    -1.847622    0.690738    -0.942166
""",
)

entry(
    index = 74,
    label = "[O]F_r12 + CH2 <=> [CH2]F_r12 + [O]_r3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(996.795,'cm^3/(mol*s)'), n=2.97758, Ea=(41.2332,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.22333, dn = +|- 0.0264834, dEa = +|- 0.144122 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/F_Abstraction
Original entry: [CH2] + [O]F <=> [CH2]F + [O]
barrier = 50.921070 kJ/mol
T1 = 0.034509599

Atom XYZ coordinates (angstrom)
F    -0.162871    0.01046    -0.03683
O    -1.66844    -0.017333    0.022329
C    1.833628    0.056661    -0.187559
H    2.09082    1.002313    0.252983
H    2.11872    -0.959717    0.012899
""",
)

entry(
    index = 75,
    label = "ClF + H <=> HF + Cl",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.5029e+08,'cm^3/(mol*s)'), n=1.25799, Ea=(20.8614,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.43321, dn = +|- 0.0472857, dEa = +|- 0.257327 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/F_Abstraction
Original entry: FCl + [H] <=> F + [Cl]
barrier = 30.442571 kJ/mol
T1 = 0.017758711

Atom XYZ coordinates (angstrom)
Cl    1.664711    0.007038    -0.0
F    -0.046358    0.000227    -0.0
H    -1.618353    -0.007265    -0.0
""",
)

entry(
    index = 76,
    label = "C2F6 + CF3 <=> CF4 + C2F5",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(4.09875,'cm^3/(mol*s)'), n=3.8806, Ea=(187.286,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.49477, dn = +|- 0.0528108, dEa = +|- 0.287394 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/F_Abstraction
Original entry: FC(F)(F)C(F)(F)F + F[C](F)F <=> FC(F)(F)F + F[C](F)C(F)(F)F
barrier = 194.632063 kJ/mol

Atom XYZ coordinates (angstrom)
F    0.649991    -0.277452    0.008276
F    -1.148938    -1.508684    -1.050161
F    -1.154464    -1.457013    1.115066
F    -1.543141    1.248625    1.048057
F    -3.12264    0.233176    -0.013635
F    -1.537454    1.197206    -1.114074
F    2.434368    1.428792    -0.027594
F    2.868914    -0.415189    -1.062644
F    2.863645    -0.364297    1.095324
C    -0.99935    -0.767817    0.015777
C    -1.817893    0.511352    -0.016818
C    2.35147    0.12849    0.002867
""",
)

entry(
    index = 77,
    label = "FC(Cl)(Cl)Cl_r12 + H <=> HF + CCl3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.71142e-06,'cm^3/(mol*s)'), n=5.47558, Ea=(94.535,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 23.6983, dn = +|- 0.415871, dEa = +|- 2.26315 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/F_Abstraction
Original entry: FC(Cl)(Cl)Cl + [H] <=> F + Cl[C](Cl)Cl
barrier = 133.615455 kJ/mol

Atom XYZ coordinates (angstrom)
Cl    1.632862    -0.342674    -0.380254
Cl    -0.520155    1.590506    -0.355124
Cl    -1.118032    -1.24058    -0.37207
F    0.009825    -0.012981    1.706115
C    0.000636    -0.000731    0.080578
H    0.018124    -0.02539    3.008515
""",
)

entry(
    index = 78,
    label = "CH3F + H <=> CH3 + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(13.6,'cm^3/(mol*s)'), n=3.72, Ea=(94.3,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """ANL0 method from Brown""",
    longDesc = 
"""
Electronic structures done using ANL0 compound method. 
Torsional scans with  M06-2X/cc-pVTZ.
""",
)

entry(
    index = 79,
    label = "CHF3 + H <=> CHF2 + HF",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(1.92,'cm^3/(mol*s)'), n=4.04, Ea=(137.8,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """ANL0 method from Brown""",
    longDesc = 
"""
Electronic structures done using ANL0 compound method. 
Torsional scans with  M06-2X/cc-pVTZ.
""",
)

entry(
    index = 80,
    label = "CF4 + H <=> CF3 + HF",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(2.58,'cm^3/(mol*s)'), n=4.04, Ea=(150.5,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """ANL0 method from Brown""",
    longDesc = 
"""
Electronic structures done using ANL0 compound method. 
Torsional scans with  M06-2X/cc-pVTZ.
""",
)

entry(
    index = 81,
    label = "CH3 + [O]F_r12 <=> CH3F + [O]_r3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1540,'cm^3/(mol*s)'), n=2.64, Ea=(25.9,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """ANL0 method from Brown""",
    longDesc = 
"""
Electronic structures done using ANL0 compound method. 
Torsional scans with  M06-2X/cc-pVTZ.
""",
)

entry(
    index = 82,
    label = "CH2F + [O]F_r12 <=> CH2F2 + [O]_r3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(831,'cm^3/(mol*s)'), n=2.7, Ea=(32.5,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """ANL0 method from Brown""",
    longDesc = 
"""
Electronic structures done using ANL0 compound method. 
Torsional scans with  M06-2X/cc-pVTZ.
""",
)

entry(
    index = 83,
    label = "CHF2 + [O]F_r12 <=> CHF3 + [O]_r3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(591,'cm^3/(mol*s)'), n=2.76, Ea=(32.1,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """ANL0 method from Brown""",
    longDesc = 
"""
Electronic structures done using ANL0 compound method. 
Torsional scans with  M06-2X/cc-pVTZ.
""",
)

entry(
    index = 84,
    label = "CF3 + [O]F_r12 <=> CF4 + [O]_r3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(214,'cm^3/(mol*s)'), n=2.82, Ea=(37,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """ANL0 method from Brown""",
    longDesc = 
"""
Electronic structures done using ANL0 compound method. 
Torsional scans with  M06-2X/cc-pVTZ.
""",
)

entry(
    index = 85,
    label = "CH3 + F2 <=> CH3F + F",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(94100,'cm^3/(mol*s)'), n=2.52, Ea=(17.3,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """ANL0 method from Brown""",
    longDesc = 
"""
Electronic structures done using ANL0 compound method. 
Torsional scans with  M06-2X/cc-pVTZ.
""",
)

entry(
    index = 86,
    label = "CH2F + F2 <=> CH2F2 + F",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(51800,'cm^3/(mol*s)'), n=2.55, Ea=(-7.1,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """ANL0 method from Brown""",
    longDesc = 
"""
Electronic structures done using ANL0 compound method. 
Torsional scans with  M06-2X/cc-pVTZ.
""",
)

entry(
    index = 87,
    label = "CHF2 + F2 <=> CHF3 + F",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(36700,'cm^3/(mol*s)'), n=2.58, Ea=(-4.2,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """ANL0 method from Brown""",
    longDesc = 
"""
Electronic structures done using ANL0 compound method. 
Torsional scans with  M06-2X/cc-pVTZ.
""",
)

entry(
    index = 88,
    label = "CF3 + F2 <=> CF4 + F",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(19300,'cm^3/(mol*s)'), n=2.58, Ea=(-2.9,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """ANL0 method from Brown""",
    longDesc = 
"""
Electronic structures done using ANL0 compound method. 
Torsional scans with  M06-2X/cc-pVTZ.
""",
)

entry(
    index = 89,
    label = "CH3 + FHO <=> CH3F + [OH]_r3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1610,'cm^3/(mol*s)'), n=3.17, Ea=(19.5,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """ANL0 method from Brown""",
    longDesc = 
"""
Electronic structures done using ANL0 compound method. 
Torsional scans with  M06-2X/cc-pVTZ.
""",
)

entry(
    index = 90,
    label = "CH2F + FHO <=> CH2F2 + [OH]_r3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2750,'cm^3/(mol*s)'), n=2.71, Ea=(14.3,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """ANL0 method from Brown""",
    longDesc = 
"""
Electronic structures done using ANL0 compound method. 
Torsional scans with  M06-2X/cc-pVTZ.
""",
)

entry(
    index = 91,
    label = "CHF2 + FHO <=> CHF3 + [OH]_r3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2120,'cm^3/(mol*s)'), n=2.75, Ea=(15.6,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """ANL0 method from Brown""",
    longDesc = 
"""
Electronic structures done using ANL0 compound method. 
Torsional scans with  M06-2X/cc-pVTZ.
""",
)

entry(
    index = 92,
    label = "CF3 + FHO <=> CF4 + [OH]_r3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1750,'cm^3/(mol*s)'), n=2.74, Ea=(8.1,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """ANL0 method from Brown""",
    longDesc = 
"""
Electronic structures done using ANL0 compound method. 
Torsional scans with  M06-2X/cc-pVTZ.
""",
)

entry(
    index = 93,
    label = "CH3 + F2O <=> CH3F_p23 + OF",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(34900,'cm^3/(mol*s)'), n=2.59, Ea=(14.5,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """ANL0 method from Brown""",
    longDesc = 
"""
Electronic structures done using ANL0 compound method. 
Torsional scans with  M06-2X/cc-pVTZ.
""",
)

entry(
    index = 94,
    label = "CH2F + F2O <=> CH2F2 + OF",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(18300,'cm^3/(mol*s)'), n=2.61, Ea=(9.2,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """ANL0 method from Brown""",
    longDesc = 
"""
Electronic structures done using ANL0 compound method. 
Torsional scans with  M06-2X/cc-pVTZ.
""",
)

entry(
    index = 95,
    label = "CHF2 + F2O <=> CHF3 + OF",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(14100,'cm^3/(mol*s)'), n=2.66, Ea=(8.4,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """ANL0 method from Brown""",
    longDesc = 
"""
Electronic structures done using ANL0 compound method. 
Torsional scans with  M06-2X/cc-pVTZ.
""",
)

entry(
    index = 96,
    label = "CF3 + F2O <=> CF4 + OF",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(8840,'cm^3/(mol*s)'), n=2.67, Ea=(13.7,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """ANL0 method from Brown""",
    longDesc = 
"""
Electronic structures done using ANL0 compound method. 
Torsional scans with  M06-2X/cc-pVTZ.
""",
)

entry(
    index = 97,
    label = "CH2F + CH3F <=> CH2F2 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(24.3,'cm^3/(mol*s)'), n=3.25, Ea=(157.6,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """ANL0 method from Brown""",
    longDesc = 
"""
Electronic structures done using ANL0 compound method. 
Torsional scans with  M06-2X/cc-pVTZ.
""",
)

entry(
    index = 98,
    label = "CH3F + CHF2 <=> CH3 + CHF3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(13.5,'cm^3/(mol*s)'), n=3.34, Ea=(146.4,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """ANL0 method from Brown""",
    longDesc = 
"""
Electronic structures done using ANL0 compound method. 
Torsional scans with  M06-2X/cc-pVTZ.
""",
)

entry(
    index = 99,
    label = "CF3 + CH3F <=> CF4 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(33.4,'cm^3/(mol*s)'), n=3.35, Ea=(144.6,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """ANL0 method from Brown""",
    longDesc = 
"""
Electronic structures done using ANL0 compound method. 
Torsional scans with  M06-2X/cc-pVTZ.
""",
)

entry(
    index = 100,
    label = "CH2F2 + CHF2 <=> CH2F + CHF3",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(35.8,'cm^3/(mol*s)'), n=3.31, Ea=(174.3,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """ANL0 method from Brown""",
    longDesc = 
"""
Electronic structures done using ANL0 compound method. 
Torsional scans with  M06-2X/cc-pVTZ.
""",
)

entry(
    index = 101,
    label = "CF3 + CH2F2 <=> CF4 + CH2F",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(98.3,'cm^3/(mol*s)'), n=3.31, Ea=(175.6,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """ANL0 method from Brown""",
    longDesc = 
"""
Electronic structures done using ANL0 compound method. 
Torsional scans with  M06-2X/cc-pVTZ.
""",
)

entry(
    index = 102,
    label = "CF3 + CHF3 <=> CF4 + CHF2",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(88.8,'cm^3/(mol*s)'), n=3.23, Ea=(198.7,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """ANL0 method from Brown""",
    longDesc = 
"""
Electronic structures done using ANL0 compound method. 
Torsional scans with  M06-2X/cc-pVTZ.
""",
)

entry(
    index = 103,
    label = "CHFO + H <=> CHO + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.87,'cm^3/(mol*s)'), n=3.88, Ea=(124.4,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """ANL0 method from Brown""",
    longDesc = 
"""
Electronic structures done using ANL0 compound method. 
Torsional scans with  M06-2X/cc-pVTZ.
""",
)

entry(
    index = 104,
    label = "CF2O + H <=> CFO + HF",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.23,'cm^3/(mol*s)'), n=4.14, Ea=(134.9,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """ANL0 method from Brown""",
    longDesc = 
"""
Electronic structures done using ANL0 compound method. 
Torsional scans with  M06-2X/cc-pVTZ.
""",
)

entry(
    index = 105,
    label = "CHO + [O]F_r12 <=> CHFO + [O]_r3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1710,'cm^3/(mol*s)'), n=2.75, Ea=(107.2,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """ANL0 method from Brown""",
    longDesc = 
"""
Electronic structures done using ANL0 compound method. 
Torsional scans with  M06-2X/cc-pVTZ.
""",
)

entry(
    index = 106,
    label = "CFO + [O]F_r12 <=> CF2O + [O]_r3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(778,'cm^3/(mol*s)'), n=2.78, Ea=(45.3,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """ANL0 method from Brown""",
    longDesc = 
"""
Electronic structures done using ANL0 compound method. 
Torsional scans with  M06-2X/cc-pVTZ.
""",
)

entry(
    index = 107,
    label = "FHO + CHO <=> CHFO + [OH]_r3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6560,'cm^3/(mol*s)'), n=2.75, Ea=(14.9,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """ANL0 method from Brown""",
    longDesc = 
"""
Electronic structures done using ANL0 compound method. 
Torsional scans with  M06-2X/cc-pVTZ.
""",
)

entry(
    index = 108,
    label = "CFO + FHO <=> CF2O + [OH]_r3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3030,'cm^3/(mol*s)'), n=2.77, Ea=(24.2,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """ANL0 method from Brown""",
    longDesc = 
"""
Electronic structures done using ANL0 compound method. 
Torsional scans with  M06-2X/cc-pVTZ.
""",
)

entry(
    index = 109,
    label = "F2O + CHO <=> CHFO + OF",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(41300,'cm^3/(mol*s)'), n=2.64, Ea=(7.3,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """ANL0 method from Brown""",
    longDesc = 
"""
Electronic structures done using ANL0 compound method. 
Torsional scans with  M06-2X/cc-pVTZ.
""",
)

entry(
    index = 110,
    label = "F2O + CFO <=> CF2O + OF",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(15300,'cm^3/(mol*s)'), n=2.68, Ea=(18.8,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """ANL0 method from Brown""",
    longDesc = 
"""
Electronic structures done using ANL0 compound method. 
Torsional scans with  M06-2X/cc-pVTZ.
""",
)

entry(
    index = 111,
    label = "OOF_r12 + CHO <=> CHFO + [O]O_r3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3570,'cm^3/(mol*s)'), n=2.6, Ea=(0.3,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """ANL0 method from Brown""",
    longDesc = 
"""
Electronic structures done using ANL0 compound method. 
Torsional scans with  M06-2X/cc-pVTZ.
""",
)

entry(
    index = 112,
    label = "CH3F + CHO <=> CH3 + CHFO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(39.5,'cm^3/(mol*s)'), n=3.43, Ea=(162.6,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """ANL0 method from Brown""",
    longDesc = 
"""
Electronic structures done using ANL0 compound method. 
Torsional scans with  M06-2X/cc-pVTZ.
""",
)

entry(
    index = 113,
    label = "CH3F + CFO <=> CF2O + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(83.5,'cm^3/(mol*s)'), n=3.36, Ea=(157.1,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """ANL0 method from Brown""",
    longDesc = 
"""
Electronic structures done using ANL0 compound method. 
Torsional scans with  M06-2X/cc-pVTZ.
""",
)

entry(
    index = 114,
    label = "CH2F2 + CHO <=> CH2F + CHFO",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(63.5,'cm^3/(mol*s)'), n=3.43, Ea=(183.6,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """ANL0 method from Brown""",
    longDesc = 
"""
Electronic structures done using ANL0 compound method. 
Torsional scans with  M06-2X/cc-pVTZ.
""",
)

entry(
    index = 115,
    label = "CH2F2 + CFO <=> CF2O + CH2F",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(227,'cm^3/(mol*s)'), n=3.32, Ea=(190.5,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """ANL0 method from Brown""",
    longDesc = 
"""
Electronic structures done using ANL0 compound method. 
Torsional scans with  M06-2X/cc-pVTZ.
""",
)

entry(
    index = 116,
    label = "CHF2 + CHFO <=> CHF3 + CHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(36.3,'cm^3/(mol*s)'), n=3.37, Ea=(183.4,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """ANL0 method from Brown""",
    longDesc = 
"""
Electronic structures done using ANL0 compound method. 
Torsional scans with  M06-2X/cc-pVTZ.
""",
)

entry(
    index = 117,
    label = "CF4 + H <=> FH + CF3-2",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(65100,'cm^3/(mol*s)'), n=2.95, Ea=(40266.5,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CF4+H <=> CF3+HF""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CF4+H <=> CF3+HF
""",
)

entry(
    index = 118,
    label = "C2F6 + H <=> FH + C2F5-2",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(12600,'cm^3/(mol*s)'), n=3.06, Ea=(36033.6,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C2F6+H <=> CF3CF2+HF""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C2F6+H <=> CF3CF2+HF
""",
)

entry(
    index = 119,
    label = "C3F8 + H <=> FH + C3F7",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(7650,'cm^3/(mol*s)'), n=3.12, Ea=(35260.6,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C3F8+H <=> C2F5CF2+HF""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C3F8+H <=> C2F5CF2+HF
""",
)

entry(
    index = 120,
    label = "C4F10 + H <=> FH + C4F9",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(629000,'cm^3/(mol*s)'), n=2.12, Ea=(35197.3,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is C4F10+H <=> C3F7CF2+HF""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C4F10+H <=> C3F7CF2+HF
""",
)

