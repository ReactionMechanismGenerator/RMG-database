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
    label = "CH3F + H <=> CH3_p1 + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.73e+08,'cm^3/(mol*s)'), n=1.77, Ea=(31000,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 1,
    label = "CH2F2 + H <=> CH2F_p1 + HF",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(4.9e+08,'cm^3/(mol*s)'), n=1.73, Ea=(35370,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 2,
    label = "CHF3 + H <=> CHF2_p1 + HF",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(2.11e+08,'cm^3/(mol*s)'), n=1.77, Ea=(39800,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 3,
    label = "CF4 + H <=> CF3_p1 + HF",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(3.07e+09,'cm^3/(mol*s)'), n=1.58, Ea=(41330,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 4,
    label = "CF4 + CH3 <=> CH3F_p23 + CF3_p1",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(96400,'cm^3/(mol*s)'), n=2.41, Ea=(26130,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 5,
    label = "CF3-CF3 + H <=> CF3-CF2_p1 + HF",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(1e+15,'cm^3/(mol*s)'), n=0, Ea=(30000,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 6,
    label = "CF3-CF3 + CF3 <=> CF4_p23 + CF3-CF2_p1",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(3e+12,'cm^3/(mol*s)'), n=0, Ea=(11300,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 7,
    label = "CF3COF + H <=> CF3CO_p1 + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'cm^3/(mol*s)'), n=0, Ea=(3000,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 8,
    label = "CF3COF + CF3 <=> CF3CO_p1 + CF4_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+12,'cm^3/(mol*s)'), n=0, Ea=(9000,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 9,
    label = "CF3COF + CF3-CF2 <=> CF3CO_p1 + CF3-CF3_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+11,'cm^3/(mol*s)'), n=0, Ea=(14000,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 10,
    label = "F2 + H <=> F_p1 + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.9e+09,'cm^3/(mol*s)'), n=1.4, Ea=(1330,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 11,
    label = "F2 + CF3 <=> CF4_p23 + F_p1",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.65e+12,'cm^3/(mol*s)'), n=0, Ea=(2500,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 12,
    label = "CH3 + F2 <=> CH3F_p23 + F_p1",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+12,'cm^3/(mol*s)'), n=0, Ea=(1100,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 13,
    label = "CFO + F2 <=> CF2O + F_p1",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+12,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 14,
    label = "[OH]_r3 + FC(Cl)(Cl)Cl_r12 <=> Cl[C](Cl)Cl_p1 + OF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(30810.5,'cm^3/(mol*s)'), n=2.88761, Ea=(284.829,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.22877, dn = +|- 0.0270661, dEa = +|- 0.147293 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 15,
    label = "[OH]_r3 + [CH2]F_r12 <=> [CH2]_p1 + OF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2264.98,'cm^3/(mol*s)'), n=3.15133, Ea=(325.669,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.25436, dn = +|- 0.0297737, dEa = +|- 0.162027 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 16,
    label = "OOF_r12 + CH3 <=> [O]O_p1 + CH3F_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(849.095,'cm^3/(mol*s)'), n=3.17369, Ea=(16.5921,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.07688, dn = +|- 0.00973066, dEa = +|- 0.0529539 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 17,
    label = "[O]O_r3 + HF <=> [H]_p1 + OOF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(19265.8,'cm^3/(mol*s)'), n=3.05869, Ea=(427.112,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.08156, dn = +|- 0.0103003, dEa = +|- 0.056054 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 18,
    label = "C[C](C)F_r12 + CH3 <=> C[C]C_p1 + CH3F_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(44.7723,'cm^3/(mol*s)'), n=3.46134, Ea=(198.066,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.33304, dn = +|- 0.0377664, dEa = +|- 0.205523 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 19,
    label = "CDC(C)F_r12 + CH3 <=> CD[C]C_p1 + CH3F_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(25.027,'cm^3/(mol*s)'), n=3.59925, Ea=(209.739,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.41534, dn = +|- 0.0456373, dEa = +|- 0.248357 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 20,
    label = "CDCF_r12 + CH3 <=> [CH]DC_p1 + CH3F_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.7299,'cm^3/(mol*s)'), n=3.76087, Ea=(211.861,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.50616, dn = +|- 0.0538082, dEa = +|- 0.292822 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 21,
    label = "COF_r12 + CH3 <=> C[O]_p1 + CH3F_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(476.496,'cm^3/(mol*s)'), n=3.27616, Ea=(30.5726,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.1197, dn = +|- 0.0148542, dEa = +|- 0.0808358 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 22,
    label = "OD[C]F_r12 + CH3 <=> [C]DO_p1 + CH3F_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.28573,'cm^3/(mol*s)'), n=3.56699, Ea=(285.117,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.47481, dn = +|- 0.0510453, dEa = +|- 0.277787 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 23,
    label = "[OH]_r3 + FCCl_r12 <=> [CH2]Cl_p1 + OF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3819.03,'cm^3/(mol*s)'), n=3.24993, Ea=(296.719,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.30163, dn = +|- 0.0346344, dEa = +|- 0.188479 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 24,
    label = "CC(C)F_r12 + CH3 <=> C[CH]C_p1 + CH3F_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(12.1333,'cm^3/(mol*s)'), n=3.66599, Ea=(177.696,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.43808, dn = +|- 0.0477313, dEa = +|- 0.259752 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 25,
    label = "[O]_r3 + CDC(C)F_r12 <=> CD[C]C_p1 + [O]F_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.30096e+06,'cm^3/(mol*s)'), n=2.36151, Ea=(340.16,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.32769, dn = +|- 0.0372388, dEa = +|- 0.202652 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 26,
    label = "O[CH]F_r12 + CH3 <=> [CH]O_p1 + CH3F_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(22.5043,'cm^3/(mol*s)'), n=3.69111, Ea=(210.267,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.47535, dn = +|- 0.0510929, dEa = +|- 0.278045 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 27,
    label = "[O]_r3 + O[CH]F_r12 <=> [CH]O_p1 + [O]F_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.32859e+06,'cm^3/(mol*s)'), n=2.43214, Ea=(338.639,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.36874, dn = +|- 0.0412392, dEa = +|- 0.224422 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 28,
    label = "CCF_r12 + CH3 <=> C[CH2]_p1 + CH3F_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.55252,'cm^3/(mol*s)'), n=3.81157, Ea=(177.558,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.51478, dn = +|- 0.054558, dEa = +|- 0.296903 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 29,
    label = "C[CH]F_r12 + CH3 <=> [CH]C_p1 + CH3F_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(573.04,'cm^3/(mol*s)'), n=2.60489, Ea=(198.39,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.40606, dn = +|- 0.0447736, dEa = +|- 0.243656 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 30,
    label = "[O]O_r3 + [O]F_r12 <=> [O]_p1 + OOF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1110.26,'cm^3/(mol*s)'), n=2.89721, Ea=(154.45,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.14664, dn = +|- 0.0179773, dEa = +|- 0.0978319 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 31,
    label = "OCF_r12 + CH3 <=> [CH2]O_p1 + CH3F_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.29538,'cm^3/(mol*s)'), n=3.74, Ea=(187.567,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.45152, dn = +|- 0.048954, dEa = +|- 0.266406 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 32,
    label = "[O]O_r3 + O[CH]F_r12 <=> [CH]O_p1 + OOF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.55718,'cm^3/(mol*s)'), n=3.53988, Ea=(393.383,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.12198, dn = +|- 0.0151213, dEa = +|- 0.0822898 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 33,
    label = "[OH]_r3 + CDCDCF_r12 <=> [CH]DCDC_p1 + OF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(377.996,'cm^3/(mol*s)'), n=3.50982, Ea=(274.491,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.51727, dn = +|- 0.0547737, dEa = +|- 0.298076 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 34,
    label = "[OH]_r3 + C[C](C)F_r12 <=> C[C]C_p1 + OF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(95239.3,'cm^3/(mol*s)'), n=2.75763, Ea=(322.353,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.09238, dn = +|- 0.0116086, dEa = +|- 0.0631737 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 35,
    label = "C[C](O)F_r12 + CH3 <=> C[C]O_p1 + CH3F_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(35.032,'cm^3/(mol*s)'), n=3.5135, Ea=(211.783,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.38305, dn = +|- 0.0426058, dEa = +|- 0.231859 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 36,
    label = "[O]O_r3 + C[C](C)F_r12 <=> C[C]C_p1 + OOF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(115.787,'cm^3/(mol*s)'), n=3.43806, Ea=(384.463,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.10975, dn = +|- 0.0136817, dEa = +|- 0.0744553 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 37,
    label = "[OH]_r3 + CD[C]F_r12 <=> [C]DC_p1 + OF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(38723.5,'cm^3/(mol*s)'), n=2.8378, Ea=(400.231,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.12789, dn = +|- 0.0158118, dEa = +|- 0.0860473 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 38,
    label = "[O]_r3 + COF_r12 <=> C[O]_p1 + [O]F_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(640932,'cm^3/(mol*s)'), n=2.39839, Ea=(106.019,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.45066, dn = +|- 0.048876, dEa = +|- 0.265982 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 39,
    label = "[O]O_r3 + FCCl_r12 <=> [CH2]Cl_p1 + OOF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.65995,'cm^3/(mol*s)'), n=3.94804, Ea=(353.81,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.32684, dn = +|- 0.0371544, dEa = +|- 0.202193 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 40,
    label = "[OH]_r3 + CCCF_r12 <=> [CH2]CC_p1 + OF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1525.14,'cm^3/(mol*s)'), n=3.216, Ea=(295.362,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.25443, dn = +|- 0.0297815, dEa = +|- 0.16207 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 41,
    label = "[O]O_r3 + CDC(C)F_r12 <=> CD[C]C_p1 + OOF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(83.8302,'cm^3/(mol*s)'), n=3.60203, Ea=(402.485,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.16775, dn = +|- 0.0203741, dEa = +|- 0.110875 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 42,
    label = "[O]O_r3 + CCCF_r12 <=> [CH2]CC_p1 + OOF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.69582,'cm^3/(mol*s)'), n=3.94767, Ea=(359.86,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.31489, dn = +|- 0.0359654, dEa = +|- 0.195722 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 43,
    label = "CCCF_r12 + CH3 <=> [CH2]CC_p1 + CH3F_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.51365,'cm^3/(mol*s)'), n=3.78897, Ea=(180.153,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.50469, dn = +|- 0.05368, dEa = +|- 0.292125 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 44,
    label = "[OH]_r3 + CC(C)CF_r12 <=> [CH2]C(C)C_p1 + OF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1858.43,'cm^3/(mol*s)'), n=3.22261, Ea=(297.595,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.26549, dn = +|- 0.0309346, dEa = +|- 0.168345 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 45,
    label = "[OH]_r3 + CC(C)F_r12 <=> C[CH]C_p1 + OF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(84232.2,'cm^3/(mol*s)'), n=3.00838, Ea=(296.124,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.17169, dn = +|- 0.0208173, dEa = +|- 0.113287 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 46,
    label = "[OH]_r3 + C#CF_r12 <=> [C]#C_p1 + OF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.72013e+06,'cm^3/(mol*s)'), n=2.4493, Ea=(387.834,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.21764, dn = +|- 0.0258702, dEa = +|- 0.140785 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 47,
    label = "CC(O)F_r12 + CH3 <=> C[CH]O_p1 + CH3F_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(33.8922,'cm^3/(mol*s)'), n=3.5758, Ea=(187.056,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.36885, dn = +|- 0.0412495, dEa = +|- 0.224478 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 48,
    label = "[OH]_r3 + CDC(C)F_r12 <=> CD[C]C_p1 + OF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(37912.1,'cm^3/(mol*s)'), n=2.90824, Ea=(340.726,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.14025, dn = +|- 0.017243, dEa = +|- 0.093836 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 49,
    label = "[OH]_r3 + O[CH]F_r12 <=> [CH]O_p1 + OF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4745.79,'cm^3/(mol*s)'), n=2.96408, Ea=(334.468,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.16288, dn = +|- 0.0198253, dEa = +|- 0.107889 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 50,
    label = "[OH]_r3 + OCF_r12 <=> [CH2]O_p1 + OF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6788.58,'cm^3/(mol*s)'), n=3.1372, Ea=(304.788,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.23148, dn = +|- 0.027355, dEa = +|- 0.148865 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 51,
    label = "[OH]_r3 + O[C](O)F_r12 <=> O[C]O_p1 + OF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(44601.2,'cm^3/(mol*s)'), n=2.65475, Ea=(354.674,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.03298, dn = +|- 0.00426297, dEa = +|- 0.0231989 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 52,
    label = "[O]O_r3 + CDCF_r12 <=> [CH]DC_p1 + OOF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(25.7682,'cm^3/(mol*s)'), n=3.82266, Ea=(406.027,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.25384, dn = +|- 0.0297197, dEa = +|- 0.161733 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 53,
    label = "[O]O_r3 + CCF_r12 <=> C[CH2]_p1 + OOF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.27349,'cm^3/(mol*s)'), n=3.9638, Ea=(356.126,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.31123, dn = +|- 0.0355991, dEa = +|- 0.193729 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 54,
    label = "O[C](O)F_r12 + CH3 <=> O[C]O_p1 + CH3F_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(17.1639,'cm^3/(mol*s)'), n=3.56319, Ea=(226.133,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.41562, dn = +|- 0.0456631, dEa = +|- 0.248497 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 55,
    label = "[OH]_r3 + C#COF_r12 <=> C#C[O]_p1 + OF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(48753.5,'cm^3/(mol*s)'), n=3.06244, Ea=(13.9612,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.20559, dn = +|- 0.0245637, dEa = +|- 0.133675 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

entry(
    index = 56,
    label = "[OH]_r3 + C[CH]F_r12 <=> [CH]C_p1 + OF_p23",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6632.77,'cm^3/(mol*s)'), n=2.95236, Ea=(324.109,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.1674, dn = +|- 0.0203347, dEa = +|- 0.110661 kJ/mol"""),
    rank = 10,
    shortDesc = """Calculated at m062x/cc-pVTZ level with AutoTST""",
)

