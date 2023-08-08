#!/usr/bin/env python
# encoding: utf-8

name = "Cl_Abstraction/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "O + CH2Cl2O2 <=> CH2ClO2 + ClO",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(5.80916e+08,'cm^3/(mol*s)'), n=1.65322, Ea=(84.8088,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.05841, dn = +|- 0.00745814, dEa = +|- 0.0405869 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [O] + OC(O)(Cl)Cl <=> [O]Cl + O[C](O)Cl
""",
)

entry(
    index = 1,
    label = "HO + C3H5Cl3 <=> C3H5Cl2 + ClHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(186883,'cm^3/(mol*s)'), n=2.60235, Ea=(107.458,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.02615, dn = +|- 0.00339129, dEa = +|- 0.0184553 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [OH] + CC(Cl)C(Cl)Cl <=> OCl + C[CH]C(Cl)Cl
""",
)

entry(
    index = 2,
    label = "O + C2H3ClO <=> C2H3O + ClO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.20761e+08,'cm^3/(mol*s)'), n=1.59458, Ea=(13.1811,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.02896, dn = +|- 0.00375086, dEa = +|- 0.020412 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [O] + CDCOCl <=> [O]Cl + CDC[O]
""",
)

entry(
    index = 3,
    label = "O + C3H5Cl3-2 <=> C3H5Cl2-2 + ClO",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.06755e+08,'cm^3/(mol*s)'), n=1.79071, Ea=(97.425,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.09809, dn = +|- 0.0122931, dEa = +|- 0.0668984 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [O] + CC(Cl)(Cl)CCl <=> [O]Cl + C[C](Cl)CCl
""",
)

entry(
    index = 4,
    label = "O + C3H7Cl <=> C3H7 + ClO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.56273e+07,'cm^3/(mol*s)'), n=1.9359, Ea=(104.338,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.13532, dn = +|- 0.0166741, dEa = +|- 0.0907397 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [O] + CC(C)Cl <=> [O]Cl + C[CH]C
""",
)

entry(
    index = 5,
    label = "CH3 + CH2Cl2O <=> CH2ClO + CH3Cl",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(7117.49,'cm^3/(mol*s)'), n=2.81981, Ea=(59.0669,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.06185, dn = +|- 0.00788423, dEa = +|- 0.0429057 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [CH3] + OC(Cl)Cl <=> CCl + O[CH]Cl
""",
)

entry(
    index = 6,
    label = "H + C2H4ClO <=> C2H4O + ClH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.40466e+07,'cm^3/(mol*s)'), n=1.832, Ea=(49.2095,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.1682, dn = +|- 0.0204253, dEa = +|- 0.111154 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [H] + C[C](O)Cl <=> Cl + C[C]O
""",
)

entry(
    index = 7,
    label = "O + C3H3Cl5 <=> C3H3Cl4 + ClO",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.52699e+10,'cm^3/(mol*s)'), n=0.772422, Ea=(90.8516,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.09973, dn = +|- 0.0124894, dEa = +|- 0.0679669 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [O] + CC(Cl)(Cl)C(Cl)(Cl)Cl <=> [O]Cl + C[C](Cl)C(Cl)(Cl)Cl
""",
)

entry(
    index = 8,
    label = "CH3 + CH3ClO <=> CH3O + CH3Cl",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5493.93,'cm^3/(mol*s)'), n=2.84052, Ea=(4.63057,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.06391, dn = +|- 0.0081395, dEa = +|- 0.0442949 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [CH3] + COCl <=> CCl + C[O]
""",
)

entry(
    index = 9,
    label = "HO + C2HClO <=> C2HO + ClHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(89835.9,'cm^3/(mol*s)'), n=2.42885, Ea=(-3.00753,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.03257, dn = +|- 0.00421021, dEa = +|- 0.0229118 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [OH] + C#COCl <=> OCl + C#C[O]
""",
)

entry(
    index = 10,
    label = "H + C3H6Cl2 <=> C3H6Cl + ClH",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3.57471e+07,'cm^3/(mol*s)'), n=1.94617, Ea=(33.763,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.21532, dn = +|- 0.0256201, dEa = +|- 0.139424 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [H] + CCC(Cl)Cl <=> Cl + CC[CH]Cl
""",
)

entry(
    index = 11,
    label = "HO + Cl2O <=> ClO-2 + ClHO",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(119473,'cm^3/(mol*s)'), n=2.3895, Ea=(2.97331,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.04011, dn = +|- 0.00516678, dEa = +|- 0.0281174 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [OH] + ClOCl <=> OCl + [O]Cl
""",
)

entry(
    index = 12,
    label = "H + C2H4Cl <=> C2H4 + ClH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.00158e+07,'cm^3/(mol*s)'), n=1.87664, Ea=(50.0411,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.17686, dn = +|- 0.0213956, dEa = +|- 0.116434 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [H] + C[CH]Cl <=> Cl + [CH]C
""",
)

entry(
    index = 13,
    label = "H + C3H3Cl2 <=> C3H3Cl + ClH",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(4.70933e+07,'cm^3/(mol*s)'), n=1.8421, Ea=(44.8005,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.17557, dn = +|- 0.0212508, dEa = +|- 0.115646 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [H] + CDC[C](Cl)Cl <=> Cl + [CH2]CD[C]Cl
""",
)

entry(
    index = 14,
    label = "O + C3HCl2 <=> C3HCl + ClO",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.42164e+08,'cm^3/(mol*s)'), n=1.78047, Ea=(113.245,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.09522, dn = +|- 0.0119502, dEa = +|- 0.0650327 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [O] + [CH]DCDC(Cl)Cl <=> [O]Cl + C#C[C]Cl
""",
)

entry(
    index = 15,
    label = "CH3 + C2H4Cl2 <=> C2H4Cl + CH3Cl",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(9454.61,'cm^3/(mol*s)'), n=2.8542, Ea=(64.2418,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.05531, dn = +|- 0.00707308, dEa = +|- 0.0384914 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [CH3] + CC(Cl)Cl <=> CCl + C[CH]Cl
""",
)

entry(
    index = 16,
    label = "CH3 + C3HCl2 <=> C3HCl + CH3Cl",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(28353.7,'cm^3/(mol*s)'), n=2.76355, Ea=(65.434,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.07927, dn = +|- 0.0100225, dEa = +|- 0.0545422 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [CH3] + [CH]DCDC(Cl)Cl <=> CCl + C#C[C]Cl
""",
)

entry(
    index = 17,
    label = "H + CH2ClO2-2 <=> CH2O2 + ClH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.23604e+07,'cm^3/(mol*s)'), n=1.89796, Ea=(61.7352,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.19534, dn = +|- 0.0234424, dEa = +|- 0.127573 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [H] + O[C](O)Cl <=> Cl + O[C]O
""",
)

entry(
    index = 18,
    label = "H + CH3ClO <=> CH3O + ClH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38374e+09,'cm^3/(mol*s)'), n=1.70653, Ea=(6.57711,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.07914, dn = +|- 0.0100071, dEa = +|- 0.0544581 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [H] + COCl <=> Cl + C[O]
""",
)

entry(
    index = 19,
    label = "HO + CH2Cl2O <=> CH2ClO + ClHO",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(353242,'cm^3/(mol*s)'), n=2.47253, Ea=(99.9309,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.01034, dn = +|- 0.00135126, dEa = +|- 0.00735351 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [OH] + OC(Cl)Cl <=> OCl + O[CH]Cl
""",
)

entry(
    index = 20,
    label = "O + CH2Cl <=> CH2 + ClO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.81832e+06,'cm^3/(mol*s)'), n=1.87825, Ea=(142.476,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.10803, dn = +|- 0.013478, dEa = +|- 0.073347 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [O] + [CH2]Cl <=> [O]Cl + [CH2]
""",
)

entry(
    index = 21,
    label = "CH3 + CH3ClO-2 <=> CH3O-2 + CH3Cl",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4356.66,'cm^3/(mol*s)'), n=2.88851, Ea=(70.5677,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.04626, dn = +|- 0.00594149, dEa = +|- 0.0323334 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [CH3] + OCCl <=> CCl + [CH2]O
""",
)

entry(
    index = 22,
    label = "HO + C2H4Cl2 <=> C2H4Cl + ClHO",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(397568,'cm^3/(mol*s)'), n=2.54536, Ea=(100.601,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.01018, dn = +|- 0.00133064, dEa = +|- 0.00724129 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [OH] + CC(Cl)Cl <=> OCl + C[CH]Cl
""",
)

entry(
    index = 23,
    label = "H + C3H7Cl-2 <=> C3H7-2 + ClH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.68467e+07,'cm^3/(mol*s)'), n=2.0298, Ea=(38.3868,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.2407, dn = +|- 0.0283358, dEa = +|- 0.154202 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [H] + CCCCl <=> Cl + [CH2]CC
""",
)

entry(
    index = 24,
    label = "CH3 + CH2Cl2O2 <=> CH2ClO2 + CH3Cl",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(23591.7,'cm^3/(mol*s)'), n=2.7472, Ea=(52.1474,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.08573, dn = +|- 0.0108058, dEa = +|- 0.0588047 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [CH3] + OC(O)(Cl)Cl <=> CCl + O[C](O)Cl
""",
)

entry(
    index = 25,
    label = "CH3 + C4H9Cl <=> C4H9 + CH3Cl",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2839.94,'cm^3/(mol*s)'), n=2.94646, Ea=(77.8123,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.03603, dn = +|- 0.00465072, dEa = +|- 0.025309 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [CH3] + CC(C)CCl <=> CCl + [CH2]C(C)C
""",
)

entry(
    index = 26,
    label = "HO + CCl3 <=> CCl2 + ClHO",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(2.93311e+06,'cm^3/(mol*s)'), n=2.24188, Ea=(122.935,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.07305, dn = +|- 0.00926323, dEa = +|- 0.0504102 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [OH] + Cl[C](Cl)Cl <=> OCl + Cl[C]Cl
""",
)

entry(
    index = 27,
    label = "H + C3H3Cl-2 <=> C3H3 + ClH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.05257e+07,'cm^3/(mol*s)'), n=2.04125, Ea=(38.0124,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.26689, dn = +|- 0.03108, dEa = +|- 0.169136 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [H] + CDCDCCl <=> Cl + C#C[CH2]
""",
)

entry(
    index = 28,
    label = "O + CH3ClO <=> CH3O + ClO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.61815e+08,'cm^3/(mol*s)'), n=1.58988, Ea=(13.9429,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.02819, dn = +|- 0.00365281, dEa = +|- 0.0198784 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [O] + COCl <=> [O]Cl + C[O]
""",
)

entry(
    index = 29,
    label = "CH3 + C2H3Cl2 <=> C2H3Cl + CH3Cl",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(23789.9,'cm^3/(mol*s)'), n=2.70774, Ea=(80.0709,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.09808, dn = +|- 0.0122924, dEa = +|- 0.0668949 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [CH3] + C[C](Cl)Cl <=> CCl + C[C]Cl
""",
)

entry(
    index = 30,
    label = "CH3 + C3H4Cl4 <=> C3H4Cl3 + CH3Cl",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(336166,'cm^3/(mol*s)'), n=1.8024, Ea=(51.3079,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.06368, dn = +|- 0.00811105, dEa = +|- 0.0441401 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [CH3] + CC(Cl)(Cl)C(Cl)Cl <=> CCl + C[C](Cl)C(Cl)Cl
""",
)

entry(
    index = 31,
    label = "O + C2H4Cl <=> C2H4 + ClO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.81035e+07,'cm^3/(mol*s)'), n=1.82655, Ea=(134.177,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.09378, dn = +|- 0.0117774, dEa = +|- 0.0640924 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [O] + C[CH]Cl <=> [O]Cl + [CH]C
""",
)

entry(
    index = 32,
    label = "CH3 + C2H2Cl <=> C2H2 + CH3Cl",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(171123,'cm^3/(mol*s)'), n=2.55484, Ea=(132.466,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.16304, dn = +|- 0.0198437, dEa = +|- 0.107988 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [CH3] + CD[C]Cl <=> CCl + [C]DC
""",
)

entry(
    index = 33,
    label = "CH3 + C3H7Cl-2 <=> C3H7-2 + CH3Cl",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4483.29,'cm^3/(mol*s)'), n=2.95719, Ea=(77.2828,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.03106, dn = +|- 0.00401835, dEa = +|- 0.0218677 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [CH3] + CCCCl <=> CCl + [CH2]CC
""",
)

entry(
    index = 34,
    label = "O + CH3Cl-2 <=> CH3-2 + ClO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.05404e+07,'cm^3/(mol*s)'), n=2.14943, Ea=(120.991,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.21693, dn = +|- 0.025794, dEa = +|- 0.14037 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [O] + CCl <=> [O]Cl + [CH3]
""",
)

entry(
    index = 35,
    label = "CH3 + C3H6Cl2 <=> C3H6Cl + CH3Cl",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(11212.4,'cm^3/(mol*s)'), n=2.84217, Ea=(65.0652,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.05834, dn = +|- 0.00744956, dEa = +|- 0.0405402 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [CH3] + CCC(Cl)Cl <=> CCl + CC[CH]Cl
""",
)

entry(
    index = 36,
    label = "CH3 + C2H3Cl-2 <=> C2H3 + CH3Cl",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8975.81,'cm^3/(mol*s)'), n=2.87801, Ea=(99.8098,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.05584, dn = +|- 0.00713907, dEa = +|- 0.0388505 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [CH3] + CDCCl <=> CCl + [CH]DC
""",
)

entry(
    index = 37,
    label = "CH3 + C3H6Cl2-2 <=> C3H6Cl-2 + CH3Cl",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(236052,'cm^3/(mol*s)'), n=1.87159, Ea=(62.8581,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.04224, dn = +|- 0.00543552, dEa = +|- 0.0295799 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [CH3] + CC(Cl)CCl <=> CCl + C[CH]CCl
""",
)

entry(
    index = 38,
    label = "CH3 + C3H5Cl3 <=> C3H5Cl2 + CH3Cl",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3561.02,'cm^3/(mol*s)'), n=2.88661, Ea=(68.6462,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.04637, dn = +|- 0.00595485, dEa = +|- 0.0324061 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [CH3] + CC(Cl)C(Cl)Cl <=> CCl + C[CH]C(Cl)Cl
""",
)

entry(
    index = 39,
    label = "H + C3H6Cl2-3 <=> C3H6Cl-3 + ClH",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.16865e+08,'cm^3/(mol*s)'), n=1.86734, Ea=(30.6689,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.17371, dn = +|- 0.0210434, dEa = +|- 0.114518 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [H] + CC(C)(Cl)Cl <=> Cl + C[C](C)Cl
""",
)

entry(
    index = 40,
    label = "H + C3H4Cl4-2 <=> C3H4Cl3-2 + ClH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.03495e+07,'cm^3/(mol*s)'), n=1.95189, Ea=(34.5865,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.21456, dn = +|- 0.0255375, dEa = +|- 0.138974 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [H] + CC(Cl)C(Cl)(Cl)Cl <=> Cl + C[CH]C(Cl)(Cl)Cl
""",
)

entry(
    index = 41,
    label = "O + C3H3Cl2 <=> C3H3Cl + ClO",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3.14461e+08,'cm^3/(mol*s)'), n=1.7152, Ea=(130.056,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.07254, dn = +|- 0.00920088, dEa = +|- 0.0500709 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [O] + CDC[C](Cl)Cl <=> [O]Cl + [CH2]CD[C]Cl
""",
)

entry(
    index = 42,
    label = "CH3 + C2HCl <=> C2H + CH3Cl",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.25803e+08,'cm^3/(mol*s)'), n=1.0218, Ea=(128.126,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.17209, dn = +|- 0.0208614, dEa = +|- 0.113527 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [CH3] + C#CCl <=> CCl + [C]#C
""",
)

entry(
    index = 43,
    label = "O + C3H5Cl3-3 <=> C3H5Cl2-3 + ClO",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(1.89034e+08,'cm^3/(mol*s)'), n=1.7261, Ea=(86.9051,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.08692, dn = +|- 0.0109501, dEa = +|- 0.05959 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [O] + CCC(Cl)(Cl)Cl <=> [O]Cl + CC[C](Cl)Cl
""",
)

entry(
    index = 44,
    label = "O + C2HClO <=> C2HO + ClO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.34788e+08,'cm^3/(mol*s)'), n=1.5918, Ea=(2.60586,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.0294, dn = +|- 0.0038065, dEa = +|- 0.0207148 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [O] + C#COCl <=> [O]Cl + C#C[O]
""",
)

entry(
    index = 45,
    label = "CH3 + CH2ClO2-2 <=> CH2O2 + CH3Cl",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(34330.4,'cm^3/(mol*s)'), n=2.71102, Ea=(105.393,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.10497, dn = +|- 0.0131137, dEa = +|- 0.0713642 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [CH3] + O[C](O)Cl <=> CCl + O[C]O
""",
)

entry(
    index = 46,
    label = "CH3 + C2H5Cl <=> C2H5 + CH3Cl",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1608.05,'cm^3/(mol*s)'), n=2.95327, Ea=(77.1245,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.03068, dn = +|- 0.00397063, dEa = +|- 0.021608 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [CH3] + CCCl <=> CCl + C[CH2]
""",
)

entry(
    index = 47,
    label = "CH3 + C2H4ClO <=> C2H4O + CH3Cl",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(11146.4,'cm^3/(mol*s)'), n=2.7136, Ea=(92.8747,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.0988, dn = +|- 0.0123784, dEa = +|- 0.067363 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [CH3] + C[C](O)Cl <=> CCl + C[C]O
""",
)

entry(
    index = 48,
    label = "CH3 + C3H4Cl4-2 <=> C3H4Cl3-2 + CH3Cl",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(210390,'cm^3/(mol*s)'), n=1.87409, Ea=(63.6314,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.04775, dn = +|- 0.0061287, dEa = +|- 0.0333522 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [CH3] + CC(Cl)C(Cl)(Cl)Cl <=> CCl + C[CH]C(Cl)(Cl)Cl
""",
)

entry(
    index = 49,
    label = "O + C3H5Cl3 <=> C3H5Cl2 + ClO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.89307e+07,'cm^3/(mol*s)'), n=1.947, Ea=(109.429,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.14813, dn = +|- 0.0181481, dEa = +|- 0.0987615 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [O] + CC(Cl)C(Cl)Cl <=> [O]Cl + C[CH]C(Cl)Cl
""",
)

entry(
    index = 50,
    label = "HO + C3H6Cl2 <=> C3H6Cl + ClHO",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(114704,'cm^3/(mol*s)'), n=2.53406, Ea=(100.726,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.00517, dn = +|- 0.000677194, dEa = +|- 0.00368527 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [OH] + CCC(Cl)Cl <=> OCl + CC[CH]Cl
""",
)

entry(
    index = 51,
    label = "CH3 + C3H5Cl <=> C3H5 + CH3Cl",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7177.19,'cm^3/(mol*s)'), n=2.80408, Ea=(93.3484,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.0772, dn = +|- 0.00976965, dEa = +|- 0.0531661 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [CH3] + CDC(C)Cl <=> CCl + CD[C]C
""",
)

entry(
    index = 52,
    label = "H + CHCl2O <=> CHClO + ClH",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(7.26429e+07,'cm^3/(mol*s)'), n=1.83646, Ea=(47.659,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.184, dn = +|- 0.0221901, dEa = +|- 0.120758 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [H] + O[C](Cl)Cl <=> Cl + O[C]Cl
""",
)

entry(
    index = 53,
    label = "HO + C3H4Cl4 <=> C3H4Cl3 + ClHO",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(192123,'cm^3/(mol*s)'), n=2.39913, Ea=(87.1348,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.02694, dn = +|- 0.00349211, dEa = +|- 0.0190039 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [OH] + CC(Cl)(Cl)C(Cl)Cl <=> OCl + C[C](Cl)C(Cl)Cl
""",
)

entry(
    index = 54,
    label = "HO + CHCl3O <=> CHCl2O + ClHO",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(472078,'cm^3/(mol*s)'), n=2.34331, Ea=(77.8439,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.03741, dn = +|- 0.00482477, dEa = +|- 0.0262562 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [OH] + OC(Cl)(Cl)Cl <=> OCl + O[C](Cl)Cl
""",
)

entry(
    index = 55,
    label = "HO + CH3ClO <=> CH3O + ClHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(70323.5,'cm^3/(mol*s)'), n=2.34313, Ea=(12.464,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.05809, dn = +|- 0.00741885, dEa = +|- 0.0403731 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [OH] + COCl <=> OCl + C[O]
""",
)

entry(
    index = 56,
    label = "H + CH2ClO-2 <=> CH2O + ClH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.64852e+07,'cm^3/(mol*s)'), n=1.87563, Ea=(51.6952,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.18225, dn = +|- 0.021996, dEa = +|- 0.119702 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [H] + O[CH]Cl <=> Cl + [CH]O
""",
)

entry(
    index = 57,
    label = "H + C2H5ClO <=> C2H5O + ClH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.37292e+07,'cm^3/(mol*s)'), n=1.85998, Ea=(31.3569,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.16586, dn = +|- 0.0201613, dEa = +|- 0.109717 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [H] + CC(O)Cl <=> Cl + C[CH]O
""",
)

entry(
    index = 58,
    label = "CH3 + C2H4Cl <=> C2H4 + CH3Cl",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(19807.9,'cm^3/(mol*s)'), n=2.78529, Ea=(92.1915,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.08308, dn = +|- 0.010485, dEa = +|- 0.0570592 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [CH3] + C[CH]Cl <=> CCl + [CH]C
""",
)

entry(
    index = 59,
    label = "O + C3H6Cl-4 <=> C3H6 + ClO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.27701e+07,'cm^3/(mol*s)'), n=1.64048, Ea=(127.582,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.03537, dn = +|- 0.00456635, dEa = +|- 0.0248499 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [O] + C[C](C)Cl <=> [O]Cl + C[C]C
""",
)

entry(
    index = 60,
    label = "CH3 + CH2ClO-2 <=> CH2O + CH3Cl",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(11610.3,'cm^3/(mol*s)'), n=2.81056, Ea=(94.0144,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.06431, dn = +|- 0.00818791, dEa = +|- 0.0445583 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [CH3] + O[CH]Cl <=> CCl + [CH]O
""",
)

entry(
    index = 61,
    label = "H + CH2Cl2O2 <=> CH2ClO2 + ClH",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3.71747e+08,'cm^3/(mol*s)'), n=1.75948, Ea=(27.3761,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.11835, dn = +|- 0.0146956, dEa = +|- 0.0799727 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [H] + OC(O)(Cl)Cl <=> Cl + O[C](O)Cl
""",
)

entry(
    index = 62,
    label = "H + C2H3ClO <=> C2H3O + ClH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.8674e+08,'cm^3/(mol*s)'), n=1.69184, Ea=(5.09994,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.06991, dn = +|- 0.00887856, dEa = +|- 0.0483168 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [H] + CDCOCl <=> Cl + CDC[O]
""",
)

entry(
    index = 63,
    label = "HO + C3H6Cl2-3 <=> C3H6Cl-3 + ClHO",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3.15903e+06,'cm^3/(mol*s)'), n=2.43229, Ea=(93.219,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.02763, dn = +|- 0.00358107, dEa = +|- 0.019488 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [OH] + CC(C)(Cl)Cl <=> OCl + C[C](C)Cl
""",
)

entry(
    index = 64,
    label = "HO + C3H3Cl5 <=> C3H3Cl4 + ClHO",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(422964,'cm^3/(mol*s)'), n=2.3853, Ea=(87.78,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.03095, dn = +|- 0.00400448, dEa = +|- 0.0217923 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [OH] + CC(Cl)(Cl)C(Cl)(Cl)Cl <=> OCl + C[C](Cl)C(Cl)(Cl)Cl
""",
)

entry(
    index = 65,
    label = "HO + C3H3Cl-2 <=> C3H3 + ClHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(31828.9,'cm^3/(mol*s)'), n=2.73518, Ea=(101.33,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.07274, dn = +|- 0.00922502, dEa = +|- 0.0502022 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [OH] + CDCDCCl <=> OCl + C#C[CH2]
""",
)

entry(
    index = 66,
    label = "CH3 + C2H3Cl3 <=> C2H3Cl2 + CH3Cl",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(1.80659e+06,'cm^3/(mol*s)'), n=1.79841, Ea=(50.2703,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.0638, dn = +|- 0.00812597, dEa = +|- 0.0442212 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [CH3] + CC(Cl)(Cl)Cl <=> CCl + C[C](Cl)Cl
""",
)

entry(
    index = 67,
    label = "H + CH2Cl2O <=> CH2ClO + ClH",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.04071e+08,'cm^3/(mol*s)'), n=1.85451, Ea=(31.171,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.16739, dn = +|- 0.0203335, dEa = +|- 0.110654 kJ/mol"""),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_abstraction
Original entry: [H] + OC(Cl)Cl <=> Cl + O[CH]Cl
""",
)

entry(
    index = 68,
    label = "C2H2Cl4 + H <=> ClH-2 + C2H2Cl3",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(1.46201e+08,'cm^3/(mol*s)'), n=1.87317, Ea=(15.8216,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.16351, dn = +|- 0.0198965, dEa = +|- 0.108276 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ClC(Cl)C(Cl)Cl + [H] <=> Cl + Cl[CH]C(Cl)Cl
barrier = 21.502064 kJ/mol
T1 = 0.01547416

Atom XYZ coordinates (angstrom)
Cl    -2.136781    -0.369475    -0.80123
Cl    -0.579985    1.586226    0.862398
Cl    0.53119    -1.504203    0.932777
Cl    2.19344    0.339684    -0.611326
C    -0.487216    0.562725    -0.543472
C    0.61364    -0.474896    -0.498061
H    -0.397634    1.174827    -1.433376
H    0.527332    -1.117276    -1.367385
H    -3.579319    -1.260357    -1.098574
""",
)

entry(
    index = 69,
    label = "Cl2 + CFO <=> CClFO + Cl",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(141671,'cm^3/(mol*s)'), n=2.5177, Ea=(0.0383549,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.00866, dn = +|- 0.00113339, dEa = +|- 0.00616788 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: [Cl][Cl] + OD[C]F <=> ODC(F)Cl + [Cl]
barrier = 2.301919 kJ/mol
T1 = 0.021258407000000003

Atom XYZ coordinates (angstrom)
Cl    -0.577435    -0.173193    0.031136
Cl    -2.634078    -0.00447    -0.022336
F    2.107991    1.230513    0.006449
O    2.489662    -0.965014    -0.021403
C    1.797314    -0.036564    0.007158
""",
)

entry(
    index = 70,
    label = "ClO-3 + C2H2Cl-2 <=> C2H2Cl2 + O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(210425,'cm^3/(mol*s)'), n=1.63892, Ea=(8.63391,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.04912, dn = +|- 0.00630039, dEa = +|- 0.0342865 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: CD[C]Cl + [O]Cl <=> CDC(Cl)Cl + [O]
barrier = 11.547192 kJ/mol
T1 = 0.03204388

Atom XYZ coordinates (angstrom)
Cl    1.844587    -0.789892    0.004869
Cl    -1.280852    -0.220242    0.034529
O    -2.950508    -0.238829    0.047359
C    0.950273    1.799361    0.018752
C    0.763206    0.504076    0.017575
H    0.098562    2.464715    0.028193
H    1.948493    2.22086    0.010338
""",
)

entry(
    index = 71,
    label = "CH2Cl2 + C2H4Cl-2 <=> C2H4Cl2 + CH2Cl-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(53.106,'cm^3/(mol*s)'), n=3.17583, Ea=(58.13,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.05888, dn = +|- 0.00751639, dEa = +|- 0.0409039 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: C[CH]Cl + ClCCl <=> CC(Cl)Cl + [CH2]Cl
barrier = 62.960045 kJ/mol
T1 = 0.018000942

Atom XYZ coordinates (angstrom)
Cl    -0.309644    0.588878    0.550733
Cl    -3.145333    1.172857    -0.674529
Cl    2.528414    -0.627964    0.858266
C    2.012158    1.32469    -0.96911
C    -2.384683    0.333819    0.632807
C    1.747685    0.871466    0.42849
H    1.713273    0.555595    -1.679238
H    3.07708    1.527783    -1.101773
H    1.448758    2.234053    -1.171578
H    -2.628423    0.762878    1.593613
H    -2.48058    -0.738417    0.544417
H    1.884427    1.598126    1.218233
""",
)

entry(
    index = 72,
    label = "C4H6Cl2 + H <=> ClH-2 + C4H6Cl",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(8.23139e+07,'cm^3/(mol*s)'), n=1.86255, Ea=(33.7223,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.17796, dn = +|- 0.021518, dEa = +|- 0.1171 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: CC(C)DC(Cl)Cl + [H] <=> Cl + CC(C)D[C]Cl
barrier = 39.772135 kJ/mol
T1 = 0.016332087

Atom XYZ coordinates (angstrom)
Cl    0.002603    -1.899507    0.343386
Cl    -1.905443    0.377511    0.079452
C    0.739951    2.129762    -0.101722
C    2.355753    0.194369    0.122607
C    0.923743    0.649777    0.064203
C    -0.086032    -0.199004    0.153421
H    1.232924    2.457556    -1.018972
H    -0.303095    2.423777    -0.140065
H    1.223583    2.652012    0.726031
H    2.861282    0.689045    0.954145
H    2.451786    -0.879697    0.242717
H    2.870701    0.494635    -0.791934
H    -3.374651    1.028587    -0.000534
""",
)

entry(
    index = 73,
    label = "C2H2ClF + H <=> ClH-2 + C2H2F",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.39935e+10,'cm^3/(mol*s)'), n=0.953042, Ea=(47.9115,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.20246, dn = +|- 0.0242226, dEa = +|- 0.131818 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: FCDCCl + [H] <=> Cl + [CH]DCF
barrier = 52.771390 kJ/mol
T1 = 0.018886298

Atom XYZ coordinates (angstrom)
Cl    -1.382507    -0.064861    0.199891
F    1.537454    -0.934642    0.064598
C    1.389385    0.389535    0.024985
C    0.219334    0.978172    0.069193
H    2.331022    0.919364    -0.048034
H    0.043567    2.039627    0.04332
H    -2.604982    -1.012514    0.356975
""",
)

entry(
    index = 74,
    label = "CH2ClF + C2H4F <=> C2H4ClF + CH2F",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(30.9108,'cm^3/(mol*s)'), n=3.22093, Ea=(61.1732,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.07445, dn = +|- 0.00943393, dEa = +|- 0.0513391 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: FCCl + C[CH]F <=> [CH2]F + CC(F)Cl
barrier = 65.687914 kJ/mol
T1 = 0.018550063999999998

Atom XYZ coordinates (angstrom)
Cl    0.415436    -0.274506    0.180906
F    2.954983    0.895858    0.092478
F    -2.132592    -0.737718    -0.782891
C    -1.971717    1.343889    0.320387
C    2.492887    -0.357263    -0.022088
C    -1.652765    -0.108595    0.307639
H    -1.583106    1.817674    -0.57981
H    -3.054444    1.487637    0.356118
H    -1.521228    1.813484    1.191883
H    2.626821    -0.750167    -1.022339
H    2.799603    -0.980293    0.809112
H    -1.855917    -0.691212    1.200032
""",
)

entry(
    index = 75,
    label = "ClO-3 + C6H12Cl <=> C6H12Cl2 + O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(151.446,'cm^3/(mol*s)'), n=2.66819, Ea=(17.48,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.07726, dn = +|- 0.0097768, dEa = +|- 0.053205 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: [O]Cl + C[C](Cl)C(C)(C)C <=> CC(C)(C)C(C)(Cl)Cl + [O]
barrier = 21.304028 kJ/mol

Atom XYZ coordinates (angstrom)
Cl    -1.840609    0.179565    -0.159803
Cl    0.714097    1.872945    -0.402312
O    -3.475105    -0.33019    -0.656052
C    0.990017    -0.847172    -0.073414
C    0.255551    0.395191    0.420655
C    2.490283    -0.675799    0.236774
C    0.820305    -1.053411    -1.580314
C    0.476861    -2.087445    0.667047
C    0.084648    0.616905    1.894315
H    2.665941    -0.510871    1.299844
H    3.012487    -1.58853    -0.050992
H    2.916368    0.155304    -0.322562
H    1.14716    -0.18036    -2.142471
H    1.427173    -1.903977    -1.891093
H    -0.217425    -1.262679    -1.83383
H    0.721419    -2.055953    1.728422
H    -0.601013    -2.200356    0.555689
H    0.956185    -2.970453    0.244695
H    1.064136    0.743318    2.364026
H    -0.419085    -0.231276    2.352045
H    -0.4992    1.51556    2.076341
""",
)

entry(
    index = 76,
    label = "CCl3F + CH2F <=> CH2ClF + CCl2F",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(4943.94,'cm^3/(mol*s)'), n=2.87921, Ea=(42.9159,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.02916, dn = +|- 0.0037765, dEa = +|- 0.0205516 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: FC(Cl)(Cl)Cl + [CH2]F <=> FCCl + F[C](Cl)Cl
barrier = 47.380536 kJ/mol

Atom XYZ coordinates (angstrom)
Cl    0.963908    -0.187869    0.189017
Cl    -1.669062    -0.111326    -1.349103
Cl    -1.424043    1.505418    1.058996
F    3.365402    -0.907159    -1.13925
F    -1.452095    -1.023612    1.000985
C    3.087531    -0.523363    0.103236
C    -1.032021    -0.000848    0.269866
H    3.463317    0.46535    0.333194
H    3.208519    -1.318402    0.827395
""",
)

entry(
    index = 77,
    label = "ClF + CCl3-2 <=> CCl4 + F",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1355.02,'cm^3/(mol*s)'), n=2.64458, Ea=(2.92583,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.04442, dn = +|- 0.00570987, dEa = +|- 0.0310729 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: FCl + Cl[C](Cl)Cl <=> ClC(Cl)(Cl)Cl + [F]
barrier = 5.843741 kJ/mol

Atom XYZ coordinates (angstrom)
Cl    -1.296531    -0.377669    1.535066
Cl    -0.797063    1.870901    -0.212858
Cl    -1.431763    -0.720996    -1.336932
Cl    1.2905    -0.420643    -0.172674
F    2.994188    -0.510998    0.199365
C    -0.759232    0.159505    -0.011966
""",
)

entry(
    index = 78,
    label = "ClHO-2 + CClF2 <=> CCl2F2 + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(46.0523,'cm^3/(mol*s)'), n=3.14472, Ea=(-2.20466,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.03956, dn = +|- 0.00509662, dEa = +|- 0.0277356 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: OCl + F[C](F)Cl <=> FC(F)(Cl)Cl + [OH]
barrier = 0.936422 kJ/mol
T1 = 0.020627762

Atom XYZ coordinates (angstrom)
Cl    1.183216    0.463722    0.361572
Cl    -1.960449    1.030433    0.399905
F    -0.930816    -0.554075    -1.313346
F    -1.054876    -1.336489    0.685232
O    2.933445    0.537645    0.543658
C    -0.895479    -0.256056    -0.037209
H    3.254942    0.293203    -0.333649
""",
)

entry(
    index = 79,
    label = "CClF3 + H <=> ClH-2 + CF3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.34575e+07,'cm^3/(mol*s)'), n=1.82774, Ea=(33.4417,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.17094, dn = +|- 0.0207323, dEa = +|- 0.112825 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: FC(F)(F)Cl + [H] <=> Cl + F[C](F)F
barrier = 39.363802 kJ/mol
T1 = 0.017441538

Atom XYZ coordinates (angstrom)
Cl    -1.376232    0.307558    0.0
F    0.864196    -0.602201    -1.075815
F    0.864212    -0.602096    1.075878
F    1.097698    1.246606    -6.2e-05
C    0.515675    0.067974    1e-06
H    -3.022376    0.516201    -1e-06
""",
)

entry(
    index = 80,
    label = "C3H5Cl3-3 + CH3 <=> CH3Cl-2 + C3H5Cl2-4",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(4002.48,'cm^3/(mol*s)'), n=2.78212, Ea=(36.8458,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.07036, dn = +|- 0.00893322, dEa = +|- 0.0486142 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: [CH3] + CCC(Cl)(Cl)Cl <=> CCl + CC[C](Cl)Cl
barrier = 43.252461 kJ/mol
T1 = 0.016261305

Atom XYZ coordinates (angstrom)
Cl    -1.67874    0.197788    -0.327516
Cl    0.86766    -1.019286    0.779007
Cl    0.672076    -0.577847    -2.077387
C    0.841014    1.487011    -0.30085
C    2.357959    1.611495    -0.385499
C    0.332307    0.078014    -0.483762
C    -3.83591    0.377541    -0.151641
H    0.359544    2.095582    -1.066733
H    0.478442    1.827274    0.669464
H    2.647503    2.651522    -0.244607
H    2.722697    1.283478    -1.357358
H    2.842035    1.014186    0.385237
H    -4.031599    -0.266804    0.692453
H    -4.155779    0.011742    -1.115925
H    -3.952271    1.437327    0.019587
""",
)

entry(
    index = 81,
    label = "CH2Cl2 + CH3 <=> CH3Cl-2 + CH2Cl-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(7897.61,'cm^3/(mol*s)'), n=2.90196, Ea=(59.4349,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.03983, dn = +|- 0.00513163, dEa = +|- 0.0279261 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ClCCl + [CH3] <=> CCl + [CH2]Cl
barrier = 66.453607 kJ/mol
T1 = 0.019281844

Atom XYZ coordinates (angstrom)
Cl    -0.740193    0.027837    0.146761
Cl    2.160507    0.176502    -0.968159
C    -2.67189    -0.814609    0.0767
C    1.118842    0.861683    0.239161
H    -3.303541    0.051465    -0.059488
H    -2.601853    -1.476457    -0.774601
H    -2.752792    -1.301839    1.037786
H    0.926918    1.908619    0.05352
H    1.448517    0.614572    1.237972
""",
)

entry(
    index = 82,
    label = "ClHO-2 + CHClF <=> CHCl2F + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(88.1678,'cm^3/(mol*s)'), n=3.09314, Ea=(2.84185,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.02552, dn = +|- 0.00331091, dEa = +|- 0.0180179 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: OCl + F[CH]Cl <=> [OH] + FC(Cl)Cl
barrier = 6.474267 kJ/mol

Atom XYZ coordinates (angstrom)
Cl    -1.208364    -0.182107    0.064374
Cl    1.914777    -0.721643    -0.139707
F    0.990904    1.647773    -0.154867
O    -2.963766    -0.332642    -0.236973
C    0.870945    0.489824    0.465019
H    0.831681    0.573113    1.54394
H    -3.10822    0.306021    -0.946802
""",
)

entry(
    index = 83,
    label = "ClO-3 + C5H10Cl <=> C5H10Cl2 + O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(130.695,'cm^3/(mol*s)'), n=2.65639, Ea=(15.9082,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.07162, dn = +|- 0.00908798, dEa = +|- 0.0494565 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: C[C](Cl)C(C)C + [O]Cl <=> CC(C)C(C)(Cl)Cl + [O]
barrier = 19.986841 kJ/mol

Atom XYZ coordinates (angstrom)
Cl    0.751323    1.40744    -1.004815
Cl    -1.778504    -0.091166    -0.007927
O    -3.423367    -0.764003    -0.190309
C    1.014724    -0.963262    0.356273
C    2.466353    -0.798708    0.829022
C    0.969646    -1.699748    -0.97676
C    0.214455    1.136359    1.627898
C    0.322378    0.379167    0.340305
H    0.472364    -1.549411    1.103169
H    3.01622    -0.149713    0.146127
H    2.95516    -1.772225    0.838532
H    2.526362    -0.380776    1.832634
H    1.573288    -1.183008    -1.722433
H    1.374983    -2.702841    -0.850557
H    -0.047851    -1.784118    -1.353197
H    -0.120456    0.467803    2.420453
H    -0.485169    1.963598    1.533952
H    1.19233    1.544056    1.895786
""",
)

entry(
    index = 84,
    label = "C2H4Cl2O + H <=> ClH-2 + C2H4ClO-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.35321e+08,'cm^3/(mol*s)'), n=1.76471, Ea=(16.4016,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.11963, dn = +|- 0.014846, dEa = +|- 0.0807914 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: CC(O)(Cl)Cl + [H] <=> Cl + C[C](O)Cl
barrier = 21.652637 kJ/mol
T1 = 0.01671829

Atom XYZ coordinates (angstrom)
Cl    1.283655    -0.955573    0.164873
Cl    -1.611673    -0.304999    0.005481
O    0.343745    0.943157    -1.362619
C    0.321441    1.484994    0.925543
C    0.181445    0.425212    -0.126541
H    0.144928    1.0617    1.909293
H    -0.40296    2.271376    0.724295
H    1.329822    1.894724    0.874904
H    0.263008    0.248216    -2.027131
H    -3.289537    -0.886809    0.080914
""",
)

entry(
    index = 85,
    label = "BrCl + HO <=> ClHO-2 + Br",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.50529e+06,'cm^3/(mol*s)'), n=1.86514, Ea=(19.8882,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.04247, dn = +|- 0.00546506, dEa = +|- 0.0297407 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ClBr + [OH] <=> OCl + [Br]
barrier = 24.495676 kJ/mol

Atom XYZ coordinates (angstrom)
Br    -1.260981    -0.100818    -0.010531
Cl    0.899048    0.368284    0.048051
O    2.813607    -0.241153    -0.153231
H    2.893162    -0.825429    0.617448
""",
)

entry(
    index = 86,
    label = "C2H2Cl2-2 + H <=> ClH-2 + C2H2Cl-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(8.77662e+07,'cm^3/(mol*s)'), n=1.96458, Ea=(46.0239,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.22029, dn = +|- 0.0261562, dEa = +|- 0.142341 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ClCDCCl + [H] <=> Cl + [CH]DCCl
barrier = 51.421303 kJ/mol
T1 = 0.017999656

Atom XYZ coordinates (angstrom)
Cl    2.156897    -0.040661    0.192673
Cl    -2.279257    0.022507    -0.138532
C    0.332791    0.526309    0.05785
C    -0.598634    -0.390491    -0.014153
H    0.234529    1.599601    0.053652
H    -0.402545    -1.45185    -0.002398
H    3.655664    -0.508042    0.30965
""",
)

entry(
    index = 87,
    label = "CCl4 + H <=> ClH-2 + CCl3-2",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(7.16026e+08,'cm^3/(mol*s)'), n=1.73491, Ea=(10.5432,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.103, dn = +|- 0.0128798, dEa = +|- 0.0700913 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ClC(Cl)(Cl)Cl + [H] <=> Cl + Cl[C](Cl)Cl
barrier = 15.292379 kJ/mol
T1 = 0.015590988

Atom XYZ coordinates (angstrom)
Cl    1.722674    0.018469    -0.067891
Cl    -0.777083    1.529236    -0.442599
Cl    -0.544286    -0.29664    1.784782
Cl    -0.758841    -1.322575    -0.908107
C    -0.151321    -0.018575    0.097241
H    3.522435    0.055633    -0.221624
""",
)

entry(
    index = 88,
    label = "ClHO2 + HO <=> ClHO-2 + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(29011.1,'cm^3/(mol*s)'), n=2.3822, Ea=(7.07246,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.04159, dn = +|- 0.00535411, dEa = +|- 0.0291369 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: OOCl + [OH] <=> [O]O + OCl
barrier = 12.399729 kJ/mol

Atom XYZ coordinates (angstrom)
Cl    -0.397891    -0.278581    -0.215333
O    2.01852    0.542299    -0.127132
O    -2.318599    0.439526    0.087207
O    1.227565    -0.523048    0.302918
H    2.027305    1.12642    0.644368
H    -2.609055    -0.122172    0.823192
""",
)

entry(
    index = 89,
    label = "CH3Cl-2 + C5H11 <=> C5H11Cl + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(10.1836,'cm^3/(mol*s)'), n=3.29456, Ea=(59.6588,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.09803, dn = +|- 0.0122864, dEa = +|- 0.0668622 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: C[CH]C(C)C + CCl <=> CC(C)C(C)Cl + [CH3]
barrier = 65.093817 kJ/mol
T1 = 0.015743536000000002

Atom XYZ coordinates (angstrom)
Cl    -1.270727    0.128605    -0.108156
C    1.612806    -0.486258    -0.117965
C    1.623047    -0.717235    1.390998
C    1.296271    -1.776878    -0.867214
C    0.908807    1.979286    0.12364
C    -3.258784    -0.384765    0.368844
C    0.719461    0.651969    -0.547757
H    2.624927    -0.169799    -0.41279
H    0.621684    -0.97119    1.74051
H    1.964416    0.16128    1.937139
H    2.290228    -1.542929    1.638209
H    2.051533    -2.534871    -0.65965
H    1.265576    -1.611768    -1.944937
H    0.326305    -2.165816    -0.557971
H    1.943752    2.317143    -0.000397
H    0.250374    2.731823    -0.305089
H    0.702964    1.916005    1.191398
H    -3.610274    0.482372    0.910037
H    -3.710736    -0.533379    -0.601735
H    -3.146828    -1.280618    0.963372
H    0.622467    0.717275    -1.627971
""",
)

entry(
    index = 90,
    label = "C2Cl2F4 + H <=> ClH-2 + C2ClF4",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.30852e+08,'cm^3/(mol*s)'), n=1.83086, Ea=(23.8083,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.16832, dn = +|- 0.0204385, dEa = +|- 0.111226 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: FC(F)(Cl)C(F)(F)Cl + [H] <=> Cl + F[C](F)C(F)(F)Cl
barrier = 29.867126 kJ/mol
T1 = 0.016112592

Atom XYZ coordinates (angstrom)
Cl    2.053338    0.564536    -0.00634
Cl    -2.257452    -0.448018    0.009247
F    0.462482    -1.241082    1.066329
F    0.449427    -1.219741    -1.095354
F    -0.711865    1.259123    -1.063711
F    -0.699037    1.237149    1.098309
C    0.455893    -0.472366    -0.007017
C    -0.754218    0.476866    0.00975
H    3.530416    1.38587    -0.005602
""",
)

entry(
    index = 91,
    label = "CH3Cl-2 + C4H9-2 <=> C4H9Cl-2 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.98204,'cm^3/(mol*s)'), n=3.27477, Ea=(61.9954,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.09755, dn = +|- 0.0122283, dEa = +|- 0.0665461 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: CCl + C[CH]CC <=> [CH3] + CCC(C)Cl
barrier = 68.061272 kJ/mol
T1 = 0.016399748999999998

Atom XYZ coordinates (angstrom)
Cl    1.10178    0.059591    -0.141354
C    -1.617561    -0.839151    -0.617333
C    -1.737937    -1.588128    0.704601
C    -1.33103    1.428422    0.563374
C    3.12041    -0.396507    0.262525
C    -0.915289    0.488645    -0.527934
H    -1.103774    -1.45844    -1.353728
H    -2.621324    -0.651352    -1.02045
H    -2.18809    -2.567398    0.549104
H    -0.755866    -1.731377    1.154835
H    -2.362153    -1.046781    1.415091
H    -2.395654    1.668889    0.465087
H    -1.178786    0.983582    1.546121
H    -0.765813    2.356924    0.517565
H    3.074898    -1.415982    0.61896
H    3.392003    0.337575    1.008019
H    3.594975    -0.269065    -0.700238
H    -0.787386    0.965849    -1.494177
""",
)

entry(
    index = 92,
    label = "CH3Cl-2 + C6H13 <=> C6H13Cl + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.26597,'cm^3/(mol*s)'), n=3.28359, Ea=(59.382,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.09852, dn = +|- 0.012345, dEa = +|- 0.0671808 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: CCl + C[CH]C(C)(C)C <=> [CH3] + CC(Cl)C(C)(C)C
barrier = 64.635637 kJ/mol
T1 = 0.015218757

Atom XYZ coordinates (angstrom)
Cl    1.594109    0.120695    -0.0544
C    -1.314514    -0.461761    0.025898
C    -0.959689    -1.722219    -0.765695
C    -1.239894    -0.756533    1.524359
C    -2.755931    -0.057032    -0.335744
C    -0.513802    1.991923    0.352599
C    3.595753    -0.453854    0.29782
C    -0.405569    0.686094    -0.379487
H    -0.964303    -1.520476    -1.83874
H    0.027468    -2.091178    -0.493752
H    -1.690507    -2.507104    -0.565274
H    -1.584706    0.090521    2.118074
H    -1.87721    -1.609178    1.763394
H    -0.219393    -0.996041    1.822567
H    -3.08778    0.806392    0.240323
H    -2.842403    0.180996    -1.39746
H    -3.433147    -0.884771    -0.118618
H    0.211187    2.706035    -0.032499
H    -1.510542    2.425293    0.227253
H    -0.330193    1.864936    1.418786
H    3.595096    -1.50748    0.056354
H    4.149265    0.172685    -0.387301
H    3.734582    -0.2232    1.344636
H    -0.357748    0.798827    -1.460277
""",
)

entry(
    index = 93,
    label = "CCl2O + CH3 <=> CH3Cl-2 + CClO",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(18027.8,'cm^3/(mol*s)'), n=2.78658, Ea=(49.3742,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.06168, dn = +|- 0.00786303, dEa = +|- 0.0427903 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ODC(Cl)Cl + [CH3] <=> CCl + OD[C]Cl
barrier = 55.344088 kJ/mol
T1 = 0.021910653999999998

Atom XYZ coordinates (angstrom)
Cl    0.966335    0.01584    0.165249
Cl    -1.809674    0.783884    1.283802
O    -1.413114    0.304939    -1.261188
C    3.049089    -0.384746    0.466433
C    -0.951323    0.370497    -0.198836
H    3.011038    -1.21944    1.151081
H    3.379711    -0.608581    -0.537067
H    3.390904    0.552359    0.881044
""",
)

entry(
    index = 94,
    label = "C2H3Cl3-2 + H <=> ClH-2 + C2H3Cl2-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(6.13449e+07,'cm^3/(mol*s)'), n=1.87455, Ea=(19.0965,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.16815, dn = +|- 0.0204196, dEa = +|- 0.111123 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ClCC(Cl)Cl + [H] <=> Cl + Cl[CH]CCl
barrier = 24.951209 kJ/mol
T1 = 0.016063817

Atom XYZ coordinates (angstrom)
Cl    -2.368621    -0.334444    0.048552
Cl    1.990742    -0.866949    -0.221576
Cl    0.370622    1.630836    0.134495
C    -0.689692    -0.868322    0.343636
C    0.278657    -0.020945    -0.431802
H    -0.614873    -1.900573    0.015738
H    -0.495345    -0.796357    1.409428
H    0.111126    -0.026621    -1.501666
H    3.498248    -1.685499    -0.067801
""",
)

entry(
    index = 95,
    label = "ClHO-2 + CFO <=> CClFO + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(506.611,'cm^3/(mol*s)'), n=3.06943, Ea=(1.9381,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.01551, dn = +|- 0.00202179, dEa = +|- 0.0110025 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: OCl + OD[C]F <=> ODC(F)Cl + [OH]
barrier = 5.561046 kJ/mol
T1 = 0.023054992000000003

Atom XYZ coordinates (angstrom)
Cl    -0.895004    0.552523    0.007025
F    1.556726    -1.02906    0.559299
O    -2.628109    0.449846    0.026522
O    2.135891    0.862664    -0.455318
C    1.353222    0.143127    0.011049
H    -2.812795    -0.166066    0.746814
""",
)

entry(
    index = 96,
    label = "CHCl3 + CH3 <=> CH3Cl-2 + CHCl2",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(14081,'cm^3/(mol*s)'), n=2.82615, Ea=(43.1118,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.05798, dn = +|- 0.00740526, dEa = +|- 0.0402991 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ClC(Cl)Cl + [CH3] <=> CCl + Cl[CH]Cl
barrier = 49.684630 kJ/mol
T1 = 0.018110925

Atom XYZ coordinates (angstrom)
Cl    1.303686    0.000516    0.305932
Cl    -1.33839    1.446918    -0.219726
Cl    -1.333083    -1.463217    -0.195757
C    -0.698751    -0.001222    0.499581
C    3.445039    0.001174    0.120518
H    -0.835447    0.007364    1.571266
H    3.612978    0.91603    -0.428362
H    3.757237    0.004038    1.154429
H    3.613778    -0.916436    -0.423497
""",
)

entry(
    index = 97,
    label = "C2Cl3F3 + CF3 <=> CClF3 + C2Cl2F3",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(482.31,'cm^3/(mol*s)'), n=3.1849, Ea=(39.6176,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.06825, dn = +|- 0.00867427, dEa = +|- 0.047205 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: FC(F)(F)C(Cl)(Cl)Cl + F[C](F)F <=> FC(F)(F)Cl + FC(F)(F)[C](Cl)Cl
barrier = 41.853057 kJ/mol

Atom XYZ coordinates (angstrom)
Cl    0.8337    -0.246399    -0.10114
Cl    -1.711624    -0.830998    -1.623961
Cl    -1.638661    -1.37348    1.223917
F    -1.162949    1.946261    -0.729514
F    -1.108337    1.543368    1.386209
F    -2.92106    1.213957    0.27334
F    3.382449    -0.255147    -1.33441
F    3.438775    -1.023965    0.681575
F    3.283518    1.101578    0.341127
C    -1.593834    1.131482    0.223395
C    -1.159709    -0.315938    -0.063409
C    2.970547    -0.087697    -0.10371
""",
)

entry(
    index = 98,
    label = "C3H4Cl2 + H <=> ClH-2 + C3H4Cl",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(4.96546e+07,'cm^3/(mol*s)'), n=1.88378, Ea=(35.054,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.19142, dn = +|- 0.0230108, dEa = +|- 0.125224 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: CCDC(Cl)Cl + [H] <=> Cl + CCD[C]Cl
barrier = 41.325672 kJ/mol
T1 = 0.016980927

Atom XYZ coordinates (angstrom)
Cl    0.342043    1.519125    0.010991
Cl    -1.843795    -0.548688    0.08888
C    2.375067    -0.998698    -0.009807
C    0.887512    -1.145363    0.028623
C    0.016881    -0.157661    0.038564
H    2.82211    -1.474106    0.864088
H    2.778873    -1.496064    -0.892477
H    2.674433    0.045708    -0.030221
H    0.474192    -2.14665    0.050555
H    -3.382228    -1.022439    0.133555
""",
)

entry(
    index = 99,
    label = "CCl4 + C2Cl5 <=> C2Cl6 + CCl3-2",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(684.52,'cm^3/(mol*s)'), n=2.22654, Ea=(61.792,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.08575, dn = +|- 0.0108083, dEa = +|- 0.0588181 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ClC(Cl)(Cl)Cl + Cl[C](Cl)C(Cl)(Cl)Cl <=> ClC(Cl)(Cl)C(Cl)(Cl)Cl + Cl[C](Cl)Cl
barrier = 64.091942 kJ/mol

Atom XYZ coordinates (angstrom)
Cl    1.526913    1.964368    -0.545925
Cl    1.336064    0.712421    2.046413
Cl    3.734644    0.398057    0.465674
Cl    -3.303018    0.068625    -1.819863
Cl    -2.787482    1.615551    0.571001
Cl    -3.49315    -1.18315    0.781201
Cl    -0.716189    -0.457992    -0.275438
Cl    1.647968    -2.17123    0.674134
Cl    1.838459    -0.921292    -1.914012
C    1.957522    0.534724    0.400846
C    -2.742346    0.051595    -0.178365
C    1.381808    -0.738329    -0.256353
""",
)

entry(
    index = 100,
    label = "C2H3Cl2 + H <=> ClH-2 + C2H3Cl-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(8.49186e+07,'cm^3/(mol*s)'), n=1.81356, Ea=(42.8431,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.1583, dn = +|- 0.0193073, dEa = +|- 0.10507 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: [H] + C[C](Cl)Cl <=> Cl + C[C]Cl
barrier = 49.274494 kJ/mol
T1 = 0.021702628999999998

Atom XYZ coordinates (angstrom)
Cl    1.572705    -0.249454    -0.207284
Cl    -1.395013    -0.753966    0.003638
C    -0.372608    1.823026    0.051393
C    -0.192558    0.402366    -0.323223
H    0.406721    2.425617    -0.411436
H    -0.31323    1.955552    1.136422
H    -1.347426    2.176283    -0.285547
H    3.112945    -0.74913    -0.388065
""",
)

entry(
    index = 101,
    label = "C2H5Cl + C2H3-2 <=> C2H3Cl-2 + C2H5-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4238.21,'cm^3/(mol*s)'), n=2.23356, Ea=(44.97,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.07245, dn = +|- 0.0091898, dEa = +|- 0.0500105 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: [CH]DC + CCCl <=> CDCCl + C[CH2]
barrier = 49.537821 kJ/mol
T1 = 0.018502292

Atom XYZ coordinates (angstrom)
Cl    -0.075129    0.303808    0.183422
C    2.388109    -1.144683    0.042522
C    1.950555    0.282233    0.167522
C    -2.740656    -0.903447    -0.101574
C    -2.154531    0.229923    0.181346
H    2.015183    -1.587808    -0.879635
H    2.02751    -1.738387    0.881091
H    3.480027    -1.204659    0.029621
H    2.186075    0.761489    1.110671
H    2.173735    0.914816    -0.683772
H    -3.823684    -0.984692    -0.113601
H    -2.168924    -1.794486    -0.332148
H    -2.553298    1.201416    0.431001
""",
)

entry(
    index = 102,
    label = "CCl3F + CF3 <=> CClF3 + CCl2F",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(919.182,'cm^3/(mol*s)'), n=3.18453, Ea=(40.4886,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.07059, dn = +|- 0.00896101, dEa = +|- 0.0487655 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: FC(Cl)(Cl)Cl + F[C](F)F <=> FC(F)(F)Cl + F[C](Cl)Cl
barrier = 42.733656 kJ/mol

Atom XYZ coordinates (angstrom)
Cl    -0.417626    0.028526    0.156338
Cl    2.191417    1.563386    -0.026028
Cl    2.11062    -0.866856    1.571373
F    1.872354    -0.771006    -0.944245
F    -2.947718    1.269364    -0.047615
F    -3.006888    -0.533376    1.137373
F    -2.895363    -0.65938    -1.013986
C    1.576103    -0.056269    0.12815
C    -2.547387    0.02585    0.045841
""",
)

entry(
    index = 103,
    label = "ClO-3 + C3H6F <=> C3H6ClF + O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(447.245,'cm^3/(mol*s)'), n=2.63852, Ea=(5.21239,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.06424, dn = +|- 0.00817923, dEa = +|- 0.0445111 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: C[C](C)F + [O]Cl <=> CC(C)(F)Cl + [O]
barrier = 9.086073 kJ/mol
T1 = 0.025102903

Atom XYZ coordinates (angstrom)
Cl    1.162108    0.010425    -0.066516
F    -1.227547    -0.04036    1.462118
O    2.922483    0.029603    -0.189161
C    -1.408796    -1.304295    -0.511173
C    -1.434678    1.288517    -0.465401
C    -1.039892    -0.015055    0.133595
H    -0.925932    -2.135255    -0.001185
H    -1.114202    -1.300143    -1.557569
H    -2.493464    -1.437407    -0.446916
H    -1.14254    1.326215    -1.511816
H    -0.966492    2.110399    0.072237
H    -2.521516    1.398612    -0.394661
""",
)

entry(
    index = 104,
    label = "CBrClF2 + CF3 <=> CClF3 + CBrF2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(181.5,'cm^3/(mol*s)'), n=3.18568, Ea=(48.5657,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.07145, dn = +|- 0.009067, dEa = +|- 0.0493423 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: FC(F)(Cl)Br + F[C](F)F <=> FC(F)(F)Cl + F[C](F)Br
barrier = 50.892617 kJ/mol

Atom XYZ coordinates (angstrom)
Br    1.713078    2.291071    0.010033
Cl    -0.81681    0.298027    0.01007
F    1.602805    -0.17212    1.097297
F    1.613553    -0.185947    -1.046437
F    -3.500283    1.035855    -0.221091
F    -3.200612    -0.584783    1.171039
F    -3.120609    -0.958059    -0.95184
C    1.185305    0.453623    0.019229
C    -2.874248    -0.093919    0.001176
""",
)

entry(
    index = 105,
    label = "CH2Cl2 + C3H7-3 <=> C3H7Cl + CH2Cl-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(667.183,'cm^3/(mol*s)'), n=2.13101, Ea=(43.1979,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.05236, dn = +|- 0.00670443, dEa = +|- 0.0364853 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ClCCl + C[CH]C <=> [CH2]Cl + CC(C)Cl
barrier = 48.577624 kJ/mol
T1 = 0.017090429

Atom XYZ coordinates (angstrom)
Cl    -0.005481    -0.447628    0.160235
Cl    -3.012904    0.237286    -0.392757
C    1.998554    0.237728    0.324599
C    1.892202    1.724638    0.199057
C    2.736994    -0.480876    -0.760064
C    -1.959271    -1.098967    -0.048356
H    2.202017    -0.120933    1.328041
H    1.485626    1.999049    -0.774859
H    2.885937    2.176849    0.287298
H    1.255575    2.148474    0.973013
H    3.79404    -0.194065    -0.742758
H    2.335784    -0.214493    -1.738442
H    2.676808    -1.560801    -0.640479
H    -1.898087    -1.786189    -0.879689
H    -2.17163    -1.539472    0.914985
""",
)

entry(
    index = 106,
    label = "ClHO-2 + O <=> ClO-3 + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.3409e+08,'cm^3/(mol*s)'), n=1.5809, Ea=(2.96803,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.01859, dn = +|- 0.00242037, dEa = +|- 0.0131715 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: OCl + [O] <=> [O]Cl + [OH]
barrier = 5.568481 kJ/mol
T1 = 0.041599307

Atom XYZ coordinates (angstrom)
Cl    0.016938    -0.196007    0.094305
O    1.685025    0.120645    -0.136441
O    -1.850056    0.24132    -0.081649
H    1.898282    0.822552    0.492069
""",
)

entry(
    index = 107,
    label = "C2H3Cl3 + H <=> ClH-2 + C2H3Cl2-3",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(4.09068e+08,'cm^3/(mol*s)'), n=1.78337, Ea=(14.8929,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.12645, dn = +|- 0.0156438, dEa = +|- 0.0851327 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: CC(Cl)(Cl)Cl + [H] <=> Cl + C[C](Cl)Cl
barrier = 19.951966 kJ/mol
T1 = 0.015668503

Atom XYZ coordinates (angstrom)
Cl    1.79745    -0.003794    -0.076364
Cl    -0.763808    1.449725    -0.377562
Cl    -0.770557    -1.44492    -0.378123
C    -0.195876    0.000669    1.839476
C    -0.062406    0.000618    0.34012
H    -1.252514    0.003128    2.103463
H    0.279957    -0.890554    2.242304
H    0.284173    0.889488    2.242616
H    3.542415    -0.00862    -0.37388
""",
)

entry(
    index = 108,
    label = "Cl2 + C2Cl2F3 <=> C2Cl3F3 + Cl",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(157205,'cm^3/(mol*s)'), n=1.58787, Ea=(12.7432,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.03148, dn = +|- 0.00407213, dEa = +|- 0.0221604 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: [Cl][Cl] + FC(F)(F)[C](Cl)Cl <=> FC(F)(F)C(Cl)(Cl)Cl + [Cl]
barrier = 14.742386 kJ/mol

Atom XYZ coordinates (angstrom)
Cl    -0.280524    1.902671    -1.180685
Cl    -0.227026    1.496199    1.690562
Cl    1.908778    -0.031127    -0.011955
Cl    3.602477    -1.289022    -0.339095
F    -0.754987    -1.31403    0.928491
F    -0.78365    -1.016155    -1.20703
F    -2.302496    -0.119785    0.027341
C    -0.153277    0.814374    0.12766
C    -1.009293    -0.443324    -0.035387
""",
)

entry(
    index = 109,
    label = "C3H6ClF + H <=> ClH-2 + C3H6F",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.43171e+07,'cm^3/(mol*s)'), n=1.86762, Ea=(24.8767,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.17323, dn = +|- 0.0209897, dEa = +|- 0.114225 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: CC(C)(F)Cl + [H] <=> Cl + C[C](C)F
barrier = 30.964217 kJ/mol
T1 = 0.016634163

Atom XYZ coordinates (angstrom)
Cl    1.687365    -0.875007    0.123844
F    0.034114    -0.020935    -1.763968
C    -1.100365    -0.871426    0.101742
C    0.078686    1.401682    0.0976
C    0.015547    -0.008828    -0.406098
H    -2.052067    -0.431848    -0.204548
H    -1.019456    -1.872366    -0.315375
H    -1.065574    -0.929003    1.187019
H    0.147124    1.409523    1.182777
H    0.943048    1.910792    -0.32204
H    -0.829147    1.925666    -0.209089
H    3.160625    -1.63825    0.528135
""",
)

entry(
    index = 110,
    label = "CCl2F2 + CH2F <=> CH2ClF + CClF2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(42039.7,'cm^3/(mol*s)'), n=1.85566, Ea=(53.38,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.03586, dn = +|- 0.00462834, dEa = +|- 0.0251873 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: [CH2]F + FC(F)(Cl)Cl <=> FCCl + F[C](F)Cl
barrier = 57.750031 kJ/mol

Atom XYZ coordinates (angstrom)
Cl    -0.828327    -0.219606    -0.111209
Cl    2.060439    -0.286239    -1.239924
F    1.440246    0.817337    0.965245
F    1.396178    -1.330228    0.981471
F    -3.392979    -1.206156    0.453645
C    1.159487    -0.257153    0.253835
C    -2.926923    -0.22094    -0.31098
H    -3.04697    -0.421433    -1.368361
H    -3.190874    0.759381    0.065128
""",
)

entry(
    index = 111,
    label = "CCl4 + C3H6F <=> C3H6ClF + CCl3-2",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(392.269,'cm^3/(mol*s)'), n=3.09159, Ea=(19.1047,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.05261, dn = +|- 0.00673662, dEa = +|- 0.0366604 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: C[C](C)F + ClC(Cl)(Cl)Cl <=> CC(C)(F)Cl + Cl[C](Cl)Cl
barrier = 22.080695 kJ/mol

Atom XYZ coordinates (angstrom)
Cl    0.568613    0.02905    0.048504
Cl    -1.940899    -1.484334    -0.736829
Cl    -1.919739    1.394965    -1.022197
Cl    -2.028997    0.202982    1.611957
F    3.022911    0.156075    1.452514
C    3.145449    1.249481    -0.625617
C    3.132228    -1.326784    -0.36914
C    -1.447841    0.036292    -0.026762
C    2.77708    0.02634    0.136701
H    2.705496    2.130221    -0.162633
H    2.796201    1.169915    -1.652385
H    4.234626    1.360157    -0.628345
H    2.68406    -2.09446    0.258101
H    4.220244    -1.446804    -0.349145
H    2.782563    -1.447756    -1.391714
""",
)

entry(
    index = 112,
    label = "C2H3Cl3 + CH2F <=> CH2ClF + C2H3Cl2-3",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(1711.01,'cm^3/(mol*s)'), n=2.91943, Ea=(32.8682,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.02247, dn = +|- 0.00291925, dEa = +|- 0.0158864 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: CC(Cl)(Cl)Cl + [CH2]F <=> FCCl + C[C](Cl)Cl
barrier = 37.379801 kJ/mol
T1 = 0.017321057

Atom XYZ coordinates (angstrom)
Cl    1.038022    -0.258003    -0.10266
Cl    -1.738238    -1.482661    0.013704
Cl    -1.492295    1.31722    -0.683118
F    3.773645    -0.300401    0.698349
C    -0.945841    0.392173    1.809714
C    3.153953    -0.532632    -0.45904
C    -0.912468    0.027109    0.354668
H    -0.366708    1.299686    1.965663
H    -1.977538    0.56006    2.119887
H    -0.517843    -0.419737    2.393589
H    3.188817    -1.573785    -0.75227
H    3.347707    0.232257    -1.199717
""",
)

entry(
    index = 113,
    label = "C4H8Cl2 + H <=> ClH-2 + C4H8Cl",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.40202e+07,'cm^3/(mol*s)'), n=1.96824, Ea=(30.999,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.21985, dn = +|- 0.0261093, dEa = +|- 0.142086 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: CC(C)(Cl)CCl + [H] <=> Cl + [CH2]C(C)(C)Cl
barrier = 37.383335 kJ/mol

Atom XYZ coordinates (angstrom)
Cl    -1.219768    -0.916891    -1.714031
Cl    1.803453    -0.318716    1.502634
C    -0.433334    -0.141439    -0.248763
C    -0.110499    1.295955    -0.611172
C    -1.416945    -0.23876    0.902206
C    0.800665    -0.983023    -0.037061
H    0.356422    1.786199    0.243104
H    -1.023055    1.829832    -0.86928
H    0.572323    1.338636    -1.458349
H    -1.65577    -1.278233    1.121827
H    -0.978421    0.217418    1.789756
H    -2.336598    0.287002    0.652767
H    0.579404    -2.009884    0.23161
H    1.513849    -0.912018    -0.850632
H    2.66461    0.237247    2.810497
""",
)

entry(
    index = 114,
    label = "CClFO + H <=> ClH-2 + CFO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.20663e+07,'cm^3/(mol*s)'), n=1.89167, Ea=(38.2202,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.2004, dn = +|- 0.0239977, dEa = +|- 0.130594 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ODC(F)Cl + [H] <=> Cl + OD[C]F
barrier = 44.351890 kJ/mol
T1 = 0.021920194

Atom XYZ coordinates (angstrom)
Cl    1.182951    0.232341    0.004814
F    -1.28268    1.13516    -0.029783
O    -1.224941    -1.073177    0.018136
C    -0.691932    -0.039213    -0.000881
H    2.798161    0.546242    0.00776
""",
)

entry(
    index = 115,
    label = "CBrClF2 + CH3 <=> CH3Cl-2 + CBrF2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7798.37,'cm^3/(mol*s)'), n=2.71484, Ea=(54.7433,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.08762, dn = +|- 0.0110347, dEa = +|- 0.0600505 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: FC(F)(Cl)Br + [CH3] <=> CCl + F[C](F)Br
barrier = 60.897073 kJ/mol

Atom XYZ coordinates (angstrom)
Br    1.353616    -0.556944    -0.81365
Cl    -1.717795    0.026915    0.023022
F    0.504483    0.834375    1.333723
F    0.193399    1.859184    -0.523421
C    0.174483    0.679829    0.066337
C    -3.77691    -0.476761    0.089985
H    -3.965658    -0.521174    1.152604
H    -4.230653    0.351307    -0.43459
H    -3.782216    -1.423984    -0.429825
""",
)

entry(
    index = 116,
    label = "C2H5ClO-2 + HO <=> ClHO-2 + C2H5O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(42257.6,'cm^3/(mol*s)'), n=2.34082, Ea=(-4.97939,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.06796, dn = +|- 0.00863823, dEa = +|- 0.0470089 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: CCOCl + [OH] <=> OCl + CC[O]
barrier = 0.159970 kJ/mol
T1 = 0.032827551

Atom XYZ coordinates (angstrom)
Cl    -1.391035    1.625157    -2.75456
O    -2.707826    3.062703    -3.230719
O    -0.999817    0.17558    -1.942498
C    -2.159013    0.634169    0.159906
C    -0.841498    0.377983    -0.539016
H    -2.000222    0.717299    1.234688
H    -2.85345    -0.182964    -0.029199
H    -2.605582    1.563708    -0.192711
H    -0.131054    1.189697    -0.367519
H    -0.390301    -0.556408    -0.201522
H    -3.308527    2.580309    -3.818
""",
)

entry(
    index = 117,
    label = "C2Cl3F3 + CH3 <=> CH3Cl-2 + C2Cl2F3",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(50240.7,'cm^3/(mol*s)'), n=2.76768, Ea=(43.3895,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.07192, dn = +|- 0.00912462, dEa = +|- 0.0496558 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: FC(F)(F)C(Cl)(Cl)Cl + [CH3] <=> CCl + FC(F)(F)[C](Cl)Cl
barrier = 49.559476 kJ/mol

Atom XYZ coordinates (angstrom)
Cl    -1.629172    -0.109635    0.198952
Cl    0.894121    -1.634569    -0.536973
Cl    0.779895    -0.307836    2.040471
F    0.524948    1.130707    -1.556313
F    2.227512    1.077714    -0.241654
F    0.44063    2.115792    0.357722
C    0.896086    1.047357    -0.284677
C    0.360173    -0.240966    0.354731
C    -3.776306    0.118155    -0.012496
H    -3.832732    1.008424    -0.620399
H    -4.071991    0.22101    1.020771
H    -4.030671    -0.812686    -0.496822
""",
)

entry(
    index = 118,
    label = "BrCl + O <=> ClO-3 + Br",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.94992e+09,'cm^3/(mol*s)'), n=1.08089, Ea=(23.1505,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.03267, dn = +|- 0.00422331, dEa = +|- 0.0229831 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ClBr + [O] <=> [O]Cl + [Br]
barrier = 24.363058 kJ/mol

Atom XYZ coordinates (angstrom)
Br    2.063243    -0.170723    0.0
Cl    -0.093023    0.354618    -0.0
O    -1.970219    -0.183894    -0.0
""",
)

entry(
    index = 119,
    label = "ClHO-2 + CCl2F <=> CCl3F + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(29.9305,'cm^3/(mol*s)'), n=3.20569, Ea=(2.40489,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.05906, dn = +|- 0.00753912, dEa = +|- 0.0410276 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: OCl + F[C](Cl)Cl <=> FC(Cl)(Cl)Cl + [OH]
barrier = 5.886113 kJ/mol
T1 = 0.023520434

Atom XYZ coordinates (angstrom)
Cl    1.435796    -0.228456    -0.052133
Cl    -1.409223    -1.359771    -0.520671
Cl    -1.153347    1.530116    -0.224396
F    -0.800061    -0.160113    1.62592
O    3.211613    -0.314024    0.232985
C    -0.680004    -0.039673    0.319998
H    3.413506    0.571913    0.562038
""",
)

entry(
    index = 120,
    label = "CH2ClF + H <=> ClH-2 + CH2F",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.89542e+07,'cm^3/(mol*s)'), n=1.98915, Ea=(34.4709,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.23012, dn = +|- 0.0272103, dEa = +|- 0.148078 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: [H] + FCCl <=> Cl + [CH2]F
barrier = 41.488630 kJ/mol
T1 = 0.019607182

Atom XYZ coordinates (angstrom)
Cl    -1.061663    0.136736    0.335723
F    1.517979    -0.515623    -0.004991
C    0.793722    0.612445    0.045183
H    0.801627    1.125705    -0.909632
H    1.063527    1.213084    0.906352
H    -2.624536    -0.331016    0.583469
""",
)

entry(
    index = 121,
    label = "ClO-3 + C4H7Cl2 <=> C4H7Cl3 + O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(148.664,'cm^3/(mol*s)'), n=2.72935, Ea=(30.3973,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.08925, dn = +|- 0.0112317, dEa = +|- 0.0611226 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: [O]Cl + CC(C)[C](Cl)Cl <=> CC(C)C(Cl)(Cl)Cl + [O]
barrier = 34.040012 kJ/mol
T1 = 0.025755872000000003

Atom XYZ coordinates (angstrom)
Cl    -1.767282    0.089242    0.100697
Cl    0.325322    -1.8338    -0.918662
Cl    0.829453    -0.522834    1.605666
O    -3.343389    0.932673    0.063636
C    0.933577    0.834583    -0.791931
C    2.418516    0.57234    -1.061852
C    0.74758    2.16172    -0.063355
C    0.310328    -0.32629    -0.044048
H    0.39949    0.868574    -1.744412
H    2.828071    1.40389    -1.633574
H    2.572443    -0.344283    -1.627027
H    2.967709    0.502537    -0.122571
H    -0.299774    2.368182    0.145782
H    1.137792    2.964004    -0.687949
H    1.299851    2.16667    0.875938
""",
)

entry(
    index = 122,
    label = "ClHO-2 + H <=> ClH-2 + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.60971e+09,'cm^3/(mol*s)'), n=1.63953, Ea=(0.451671,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.04093, dn = +|- 0.00527044, dEa = +|- 0.0286816 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: OCl + [H] <=> Cl + [OH]
barrier = 3.374597 kJ/mol
T1 = 0.017025019

Atom XYZ coordinates (angstrom)
Cl    0.419679    0.021016    -0.073654
O    -1.28336    -0.110654    0.023155
H    2.341582    0.446247    -0.399747
H    -1.571541    0.786334    0.232281
""",
)

entry(
    index = 123,
    label = "CH2Cl + H <=> ClH-2 + CH2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.27707e+07,'cm^3/(mol*s)'), n=1.90015, Ea=(55.422,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.18223, dn = +|- 0.0219933, dEa = +|- 0.119687 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: [CH2]Cl + [H] <=> Cl + [CH2]
barrier = 62.852116 kJ/mol
T1 = 0.026023767000000003

Atom XYZ coordinates (angstrom)
Cl    0.990307    -0.174327    -0.010849
C    -0.877286    0.137094    0.065523
H    -1.163789    1.16973    0.158829
H    -1.490472    -0.689779    -0.246632
H    2.538343    -0.45543    0.029951
""",
)

entry(
    index = 124,
    label = "CCl3F + H <=> ClH-2 + CCl2F",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(3.61734e+08,'cm^3/(mol*s)'), n=1.77539, Ea=(16.5288,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.12921, dn = +|- 0.0159646, dEa = +|- 0.0868786 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: FC(Cl)(Cl)Cl + [H] <=> Cl + F[C](Cl)Cl
barrier = 21.778541 kJ/mol
T1 = 0.016539771

Atom XYZ coordinates (angstrom)
Cl    1.711036    -4.3e-05    0.029227
Cl    -0.845133    1.452814    -0.373083
Cl    -0.845189    -1.452772    -0.373104
F    -0.334619    -3e-06    1.630617
C    -0.153467    2e-06    0.316181
H    3.472668    -0.000122    -0.046465
""",
)

entry(
    index = 125,
    label = "Cl2 + CCl3-2 <=> CCl4 + Cl",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(527483,'cm^3/(mol*s)'), n=1.61124, Ea=(8.26744,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.03932, dn = +|- 0.00506701, dEa = +|- 0.0275745 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: [Cl][Cl] + Cl[C](Cl)Cl <=> ClC(Cl)(Cl)Cl + [Cl]
barrier = 10.165227 kJ/mol
T1 = 0.021332165

Atom XYZ coordinates (angstrom)
Cl    -1.222937    -0.438688    -1.720853
Cl    -1.271967    -1.284445    1.045901
Cl    -1.364386    1.531516    0.393604
Cl    1.31888    0.023038    -0.087826
Cl    3.414567    0.215932    0.450044
C    -0.874257    -0.047354    -0.080871
""",
)

entry(
    index = 126,
    label = "C3H7ClO + H <=> ClH-2 + C3H7O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.07671e+08,'cm^3/(mol*s)'), n=1.76176, Ea=(19.0677,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.11701, dn = +|- 0.0145377, dEa = +|- 0.0791138 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: [H] + CC(C)(O)Cl <=> Cl + C[C](C)O
barrier = 24.318581 kJ/mol
T1 = 0.017187035

Atom XYZ coordinates (angstrom)
Cl    1.462788    0.024235    0.011333
O    -0.885453    0.125793    1.395188
C    -0.529025    0.043    0.076765
C    -0.960701    -1.285966    -0.473606
C    -0.915276    1.248372    -0.741547
H    -0.593167    -1.415079    -1.488225
H    -2.052286    -1.324387    -0.477567
H    -0.582534    -2.088864    0.154391
H    -2.005012    1.323502    -0.758827
H    -0.545937    1.155478    -1.759722
H    -0.503281    2.158727    -0.306519
H    -0.651835    0.992728    1.74359
H    3.226395    0.020947    -0.022183
""",
)

entry(
    index = 127,
    label = "ClO-3 + CHCl2 <=> CHCl3 + O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(139886,'cm^3/(mol*s)'), n=1.59647, Ea=(38.7235,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.04113, dn = +|- 0.00529593, dEa = +|- 0.0288202 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: [O]Cl + Cl[CH]Cl <=> ClC(Cl)Cl + [O]
barrier = 42.464767 kJ/mol
T1 = 0.030896451000000002

Atom XYZ coordinates (angstrom)
Cl    1.370271    -0.116785    -0.085942
Cl    -1.488538    -1.247019    -0.170226
Cl    -1.152513    1.640813    -0.024876
O    3.130113    -0.322099    -0.072437
C    -0.642765    0.087202    0.515005
H    -0.562554    0.023755    1.590157
""",
)

entry(
    index = 128,
    label = "CCl2F2 + CF3 <=> CClF3 + CClF2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(501.469,'cm^3/(mol*s)'), n=3.18369, Ea=(43.5336,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.07137, dn = +|- 0.00905686, dEa = +|- 0.0492871 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: FC(F)(Cl)Cl + F[C](F)F <=> FC(F)(F)Cl + F[C](F)Cl
barrier = 45.878355 kJ/mol
T1 = 0.01758757

Atom XYZ coordinates (angstrom)
Cl    -0.180386    -0.054231    -0.001288
Cl    2.588647    0.743714    1.077158
F    2.066294    -1.548535    0.110801
F    2.169179    0.041181    -1.329412
F    -2.746401    -1.144284    0.062685
F    -2.632158    0.652011    -1.125721
F    -2.630654    0.781471    1.02743
C    1.819361    -0.274416    -0.101607
C    -2.263522    0.071123    -0.010938
""",
)

entry(
    index = 129,
    label = "C4H8Cl2-2 + H <=> ClH-2 + C4H8Cl-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3.79057e+07,'cm^3/(mol*s)'), n=1.91362, Ea=(32.053,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.1966, dn = +|- 0.0235806, dEa = +|- 0.128325 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: CC(C)C(Cl)Cl + [H] <=> Cl + CC(C)[CH]Cl
barrier = 38.437294 kJ/mol

Atom XYZ coordinates (angstrom)
Cl    0.035651    1.679522    0.22657
Cl    1.880087    -0.643089    -0.240034
C    -0.934871    -0.857199    -0.241421
C    -0.99989    -1.15795    1.250307
C    -2.283815    -0.363179    -0.767407
C    0.149185    0.133422    -0.608964
H    -0.666979    -1.77213    -0.776647
H    -1.740244    -1.935439    1.434641
H    -1.296367    -0.269508    1.807668
H    -0.039014    -1.499846    1.630754
H    -2.586659    0.545714    -0.247539
H    -3.045793    -1.123069    -0.596798
H    -2.246846    -0.151782    -1.836394
H    0.210373    0.332396    -1.672578
H    3.379386    -1.404282    0.049304
""",
)

entry(
    index = 130,
    label = "CHCl2F + H <=> ClH-2 + CHClF",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(8.05711e+07,'cm^3/(mol*s)'), n=1.90639, Ea=(25.324,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.1942, dn = +|- 0.0233173, dEa = +|- 0.126892 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: FC(Cl)Cl + [H] <=> Cl + F[CH]Cl
barrier = 31.734523 kJ/mol
T1 = 0.018009426999999998

Atom XYZ coordinates (angstrom)
Cl    -1.405891    -0.687128    -0.110651
Cl    1.552177    -0.19692    -0.02167
F    -0.344167    1.622513    -0.185084
C    -0.19019    0.444359    0.416875
H    -0.199068    0.550568    1.495197
H    3.147635    -0.630484    -0.429156
""",
)

entry(
    index = 131,
    label = "CH3Cl-2 + C2H2Cl-2 <=> C2H2Cl2 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(22.9292,'cm^3/(mol*s)'), n=3.44579, Ea=(51.9809,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.14485, dn = +|- 0.0177725, dEa = +|- 0.0967172 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: CD[C]Cl + CCl <=> CDC(Cl)Cl + [CH3]
barrier = 56.588208 kJ/mol
T1 = 0.019029073

Atom XYZ coordinates (angstrom)
Cl    -1.11048    0.052724    0.003555
Cl    1.852523    -0.899441    -0.000803
C    -3.128727    -0.284766    0.005933
C    1.237201    1.744496    0.001892
C    0.865948    0.486329    0.001424
H    -3.466206    0.19169    -0.904048
H    -3.19732    -1.363848    0.005128
H    -3.463829    0.190215    0.917563
H    0.490086    2.524789    0.003394
H    2.285369    2.015638    0.000791
""",
)

entry(
    index = 132,
    label = "ClHO-2 + CBrF2 <=> CBrClF2 + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(33.4555,'cm^3/(mol*s)'), n=3.14313, Ea=(3.09149,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.03965, dn = +|- 0.00510901, dEa = +|- 0.027803 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: OCl + F[C](F)Br <=> FC(F)(Cl)Br + [OH]
barrier = 6.391329 kJ/mol

Atom XYZ coordinates (angstrom)
Br    1.529213    -0.622957    0.009885
Cl    -1.778289    -0.317985    -0.022076
F    0.198943    1.472451    1.087976
F    0.216253    1.490394    -1.056547
O    -3.511772    -0.622147    0.002841
C    0.192181    0.729903    0.010223
H    -3.826354    -0.164783    -0.787409
""",
)

entry(
    index = 133,
    label = "CH3Cl-2 + C4H9-3 <=> C4H9Cl-3 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.946418,'cm^3/(mol*s)'), n=3.44684, Ea=(54.354,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.16615, dn = +|- 0.0201936, dEa = +|- 0.109893 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: CCl + C[C](C)C <=> [CH3] + CC(C)(C)Cl
barrier = 60.235275 kJ/mol
T1 = 0.016450925

Atom XYZ coordinates (angstrom)
Cl    1.01695    0.096571    -0.009779
C    -1.076717    0.229273    -0.004851
C    -1.419368    0.40621    1.447477
C    -1.518507    -1.079868    -0.595547
C    -1.360155    1.4291    -0.863931
C    3.139821    -0.037814    -0.014943
H    -2.506934    0.486613    1.557346
H    -1.081225    -0.444132    2.038177
H    -0.97033    1.313096    1.850317
H    -2.613386    -1.108936    -0.637109
H    -1.137782    -1.203247    -1.608561
H    -1.180153    -1.919423    0.010276
H    -0.911514    2.328606    -0.444437
H    -2.443347    1.585073    -0.924753
H    -0.981048    1.287675    -1.875193
H    3.315758    -1.012729    -0.44816
H    3.430229    0.801085    -0.632205
H    3.386847    0.053002    1.033783
""",
)

entry(
    index = 134,
    label = "C3H6Cl2-2 + C2H5-2 <=> C2H5Cl + C3H6Cl-5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1777.36,'cm^3/(mol*s)'), n=1.98145, Ea=(45.3308,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.00453, dn = +|- 0.000594188, dEa = +|- 0.00323355 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: CC(Cl)CCl + C[CH2] <=> C[CH]CCl + CCCl
barrier = 50.260154 kJ/mol
T1 = 0.016012918

Atom XYZ coordinates (angstrom)
Cl    -1.192761    -0.215545    0.300293
Cl    3.281736    -0.470134    -0.384641
C    -3.876873    0.682218    -0.429614
C    -3.27474    -0.597406    0.049634
C    0.932159    1.735989    0.302537
C    1.4764    -0.627158    -0.47599
C    0.827943    0.260748    0.530291
H    -4.954542    0.564146    -0.58059
H    -3.727326    1.481369    0.295089
H    -3.439112    0.990709    -1.37797
H    -3.532931    -0.911016    1.053249
H    -3.23518    -1.41318    -0.661211
H    0.321431    2.284535    1.0166
H    0.604636    1.991912    -0.705808
H    1.970664    2.058439    0.415655
H    1.198158    -0.35208    -1.489675
H    1.256273    -1.674359    -0.300366
H    0.987178    -0.058828    1.554446
""",
)

entry(
    index = 135,
    label = "CHCl3 + CF3 <=> CClF3 + CHCl2",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(254.115,'cm^3/(mol*s)'), n=3.26664, Ea=(32.948,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.08832, dn = +|- 0.0111199, dEa = +|- 0.0605141 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ClC(Cl)Cl + F[C](F)F <=> FC(F)(F)Cl + Cl[CH]Cl
barrier = 35.676052 kJ/mol
T1 = 0.017933884

Atom XYZ coordinates (angstrom)
Cl    -0.305203    -0.003599    0.237577
Cl    2.316813    -1.495547    -0.149183
Cl    2.334115    1.408867    -0.29961
F    -2.773723    1.152533    -0.493642
F    -2.942309    -0.126576    1.235819
F    -2.764655    -0.991927    -0.732843
C    1.688916    -0.003609    0.468708
C    -2.419318    0.008832    0.040457
H    1.789008    0.051441    1.54331
""",
)

entry(
    index = 136,
    label = "CHClO-2 + CH3 <=> CH3Cl-2 + CHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(10511.2,'cm^3/(mol*s)'), n=2.86655, Ea=(69.1023,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.05768, dn = +|- 0.00736773, dEa = +|- 0.0400949 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ODCCl + [CH3] <=> CCl + [CH]DO
barrier = 75.573214 kJ/mol
T1 = 0.024458228999999998

Atom XYZ coordinates (angstrom)
Cl    -0.384909    -0.059397    0.258754
O    2.279123    0.479937    -0.624778
C    -2.463562    -0.38433    0.192403
C    1.638799    0.256765    0.323324
H    1.977431    0.177605    1.372009
H    -2.720241    -0.558606    1.227982
H    -2.838248    0.540129    -0.224414
H    -2.551641    -1.246374    -0.454025
""",
)

entry(
    index = 137,
    label = "ClHO2 + Br <=> BrCl + HO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.05994e+07,'cm^3/(mol*s)'), n=1.63822, Ea=(6.54919,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.05092, dn = +|- 0.00652481, dEa = +|- 0.0355078 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: OOCl + [Br] <=> [O]O + ClBr
barrier = 7.605412 kJ/mol

Atom XYZ coordinates (angstrom)
Br    -1.663754    -0.237303    0.095479
Cl    0.633605    0.455642    -0.220434
O    3.04426    -0.561463    -0.182369
O    2.357357    0.511839    0.326991
H    3.077949    -1.178774    0.563277
""",
)

entry(
    index = 138,
    label = "C3H6Cl2-3 + CH3 <=> CH3Cl-2 + C3H6Cl-6",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.17087e+06,'cm^3/(mol*s)'), n=1.80738, Ea=(58.6546,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.06923, dn = +|- 0.00879494, dEa = +|- 0.0478617 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: CC(C)(Cl)Cl + [CH3] <=> CCl + C[C](C)Cl
barrier = 64.634435 kJ/mol

Atom XYZ coordinates (angstrom)
Cl    -1.215269    -0.015807    0.093322
Cl    1.586327    1.195227    0.333157
C    1.134287    -1.027741    -1.141086
C    1.00057    -1.22146    1.398943
C    -3.333934    0.326306    0.011563
C    0.805176    -0.381003    0.171838
H    0.889741    -0.368284    -1.970304
H    0.568115    -1.953101    -1.2409
H    2.201837    -1.259027    -1.177528
H    0.43446    -2.146733    1.297991
H    0.665529    -0.693072    2.288239
H    2.060292    -1.464051    1.511255
H    -3.611157    -0.174567    -0.904549
H    -3.381773    1.405266    -0.010155
H    -3.675436    -0.140493    0.923942
""",
)

entry(
    index = 139,
    label = "ClO-3 + CH2Br <=> CH2BrCl + O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(593.349,'cm^3/(mol*s)'), n=2.23642, Ea=(20.3579,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.4724, dn = +|- 0.0508304, dEa = +|- 0.276617 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: [O]Cl + [CH2]Br <=> ClCBr + [O]
barrier = 34.091768 kJ/mol

Atom XYZ coordinates (angstrom)
Br    1.802448    0.056371    0.021684
Cl    -1.457239    -0.114545    0.003772
O    -3.090383    -0.676937    0.006649
C    0.285541    1.154075    -0.004503
H    0.150196    1.714818    0.908452
H    0.161347    1.686241    -0.935985
""",
)

entry(
    index = 140,
    label = "C2HCl3 + H <=> ClH-2 + C2HCl2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.26882e+08,'cm^3/(mol*s)'), n=1.93859, Ea=(41.8928,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.19974, dn = +|- 0.0239251, dEa = +|- 0.130199 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ClCDC(Cl)Cl + [H] <=> Cl + [CH]DC(Cl)Cl
barrier = 47.569180 kJ/mol
T1 = 0.017261095

Atom XYZ coordinates (angstrom)
Cl    2.298537    -0.435887    0.144975
Cl    -2.142285    -0.685416    -0.114455
Cl    -0.312177    1.562263    0.07137
C    0.487916    -1.002686    0.018086
C    -0.502939    -0.140442    -0.003036
H    0.392358    -2.074916    -0.021874
H    3.734266    0.146269    0.370309
""",
)

entry(
    index = 141,
    label = "CBrClF2 + H <=> ClH-2 + CBrF2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.1139e+07,'cm^3/(mol*s)'), n=1.83301, Ea=(31.4394,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.17183, dn = +|- 0.0208329, dEa = +|- 0.113372 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: FC(F)(Cl)Br + [H] <=> Cl + F[C](F)Br
barrier = 37.400949 kJ/mol

Atom XYZ coordinates (angstrom)
Br    1.192666    -0.495865    -0.008743
Cl    -1.948443    -0.513357    0.008682
F    -0.457314    1.344711    -1.067931
F    -0.445403    1.340804    1.07542
C    -0.403853    0.575014    0.002081
H    -3.491339    -1.282836    0.015925
""",
)

# entry(
#     index = 142,
#     label = "C2H4ClF + H <=> ClH-2 + C2H4F",
#     degeneracy = 1.0,
#     kinetics = Arrhenius(A=(2.73733e+09,'cm^3/(mol*s)'), n=1.22923, Ea=(108.382,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.16026, dn = +|- 0.0195293, dEa = +|- 0.106278 kJ/mol"""),
#     rank = 3,
#     shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
#     longDesc = 
# """
# Training reaction from kinetics library: autotst/Cl_Abstraction
# Original entry: [H] + CC(F)Cl <=> Cl + C[CH]F
# barrier = 114.430561 kJ/mol
# T1 = 0.033177956

# Atom XYZ coordinates (angstrom)
# Cl    0.699747    -1.874376    0.09308
# F    -0.28965    1.622652    -0.040109
# C    1.42179    0.507454    1.446951
# C    0.739659    0.167747    0.164167
# H    2.367891    -0.024697    1.517791
# H    1.612338    1.578701    1.458589
# H    0.801555    0.243059    2.299304
# H    1.257727    0.332704    -0.76435
# H    -0.360245    -0.048064    0.116605
# """,
# )
# Wrong TS!

entry(
    index = 143,
    label = "C2Cl6 + H <=> ClH-2 + C2Cl5",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(8.08853e+08,'cm^3/(mol*s)'), n=1.77494, Ea=(25.9088,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.1342, dn = +|- 0.016544, dEa = +|- 0.0900316 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ClC(Cl)(Cl)C(Cl)(Cl)Cl + [H] <=> Cl + Cl[C](Cl)C(Cl)(Cl)Cl
barrier = 31.068722 kJ/mol

Atom XYZ coordinates (angstrom)
Cl    1.42392    1.581824    -0.114336
Cl    1.225343    -0.806914    1.594517
Cl    1.25446    -1.119949    -1.270782
Cl    -1.393387    0.702138    -1.497987
Cl    -1.42254    1.015402    1.369765
Cl    -1.609819    -1.618048    0.204398
C    0.679346    -0.144485    0.066701
C    -0.878116    -0.010651    0.036249
H    1.984372    3.26673    -0.292449
""",
)

entry(
    index = 144,
    label = "C3H7Cl + H <=> ClH-2 + C3H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.63387e+07,'cm^3/(mol*s)'), n=1.93893, Ea=(26.132,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.19472, dn = +|- 0.0233736, dEa = +|- 0.127198 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: CC(C)Cl + [H] <=> Cl + C[CH]C
barrier = 32.379591 kJ/mol
T1 = 0.016777833

Atom XYZ coordinates (angstrom)
Cl    -1.318384    0.018188    0.242554
C    0.627394    0.021743    0.523098
C    1.154697    -1.24493    -0.091699
C    1.148932    1.294551    -0.083903
H    0.676484    0.018501    1.60803
H    2.235097    -1.3026    0.066898
H    0.694302    -2.125501    0.350967
H    0.967756    -1.254444    -1.165447
H    0.684696    2.170296    0.364293
H    2.229092    1.356047    0.074888
H    0.961759    1.3099    -1.157542
H    -2.975913    0.014842    -0.024896
""",
)

entry(
    index = 145,
    label = "ClH-2 + C2H-2 <=> C2HCl + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(96.4471,'cm^3/(mol*s)'), n=3.30977, Ea=(43.0639,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.05805, dn = +|- 0.00741294, dEa = +|- 0.0403409 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: Cl + [C]#C <=> C#CCl + [H]
barrier = 52.573826 kJ/mol
T1 = 0.023871892999999998

Atom XYZ coordinates (angstrom)
Cl    1.052303    0.021119    -8e-06
C    -2.013824    0.068664    5e-06
C    -0.820021    -0.04746    -3e-06
H    -3.076054    0.126741    1.1e-05
H    2.387123    0.643448    -1.5e-05
""",
)

entry(
    index = 146,
    label = "CH3Cl-2 + C3H7-3 <=> C3H7Cl + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(11.2051,'cm^3/(mol*s)'), n=3.28274, Ea=(60.5556,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.09782, dn = +|- 0.0122608, dEa = +|- 0.0667227 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: C[CH]C + CCl <=> CC(C)Cl + [CH3]
barrier = 66.731756 kJ/mol
T1 = 0.017267075

Atom XYZ coordinates (angstrom)
Cl    -0.826315    -0.000743    -0.054627
C    1.731032    1.270407    0.265937
C    1.730105    -1.274939    0.261242
C    -2.903932    -0.000625    0.295689
C    1.242248    -0.000942    -0.35766
H    1.262471    2.143367    -0.184164
H    2.81488    1.357753    0.135406
H    1.521665    1.276274    1.336185
H    1.520706    -1.284615    1.331455
H    1.26093    -2.145892    -0.192096
H    2.813893    -1.362579    0.130413
H    -3.056925    -0.913388    0.854099
H    -3.056387    0.910675    0.856631
H    -3.318997    0.000888    -0.702386
H    1.252558    0.001056    -1.442759
""",
)

entry(
    index = 147,
    label = "ClHO-2 + CH2Br <=> CH2BrCl + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(215.683,'cm^3/(mol*s)'), n=2.88303, Ea=(8.79962,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.05291, dn = +|- 0.00677335, dEa = +|- 0.0368603 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: OCl + [CH2]Br <=> [OH] + ClCBr
barrier = 14.815020 kJ/mol

Atom XYZ coordinates (angstrom)
Br    1.52444    -0.30728    -0.025041
Cl    -1.7582    0.076348    0.029912
O    -3.506591    -0.295088    0.026262
C    0.254232    1.054467    0.027306
H    0.19011    1.630587    -0.882203
H    0.201403    1.570446    0.973119
H    -3.777068    -0.018683    -0.858148
""",
)

entry(
    index = 148,
    label = "ClHO-2 + CH3 <=> CH3Cl-2 + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(31486.4,'cm^3/(mol*s)'), n=2.84194, Ea=(0.83855,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.06429, dn = +|- 0.00818648, dEa = +|- 0.0445505 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: OCl + [CH3] <=> [OH] + CCl
barrier = 6.703957 kJ/mol
T1 = 0.022682789

Atom XYZ coordinates (angstrom)
Cl    -0.137377    -0.052503    -0.160952
O    -1.936215    0.031376    -0.218026
C    2.102812    0.089315    0.042243
H    2.337615    -0.843047    -0.447586
H    2.290931    0.999279    -0.504748
H    2.199264    0.124999    1.11557
H    -2.112034    0.871943    0.222743
""",
)

entry(
    index = 149,
    label = "C2HCl5 + H <=> ClH-2 + C2HCl4",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(2.68715e+08,'cm^3/(mol*s)'), n=1.79312, Ea=(25.6023,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.1424, dn = +|- 0.0174907, dEa = +|- 0.095184 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ClC(Cl)C(Cl)(Cl)Cl + [H] <=> Cl + Cl[C](Cl)C(Cl)Cl
barrier = 30.761761 kJ/mol

Atom XYZ coordinates (angstrom)
Cl    -2.120333    -0.884733    0.410658
Cl    -1.159699    1.831545    0.066077
Cl    1.922047    0.848355    0.229941
Cl    0.265965    -0.402962    -1.884921
Cl    0.946205    -1.906188    0.495403
C    -0.732876    0.201761    0.595015
C    0.494519    -0.336373    -0.154803
H    -0.486947    0.246382    1.650452
H    3.182424    2.048284    0.634568
""",
)

entry(
    index = 150,
    label = "ClO-3 + CBrF2 <=> CBrClF2 + O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(54795.5,'cm^3/(mol*s)'), n=1.74792, Ea=(26.4334,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.08754, dn = +|- 0.0110254, dEa = +|- 0.06 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: [O]Cl + F[C](F)Br <=> FC(F)(Cl)Br + [O]
barrier = 28.902692 kJ/mol

Atom XYZ coordinates (angstrom)
Br    1.713162    -0.510933    -0.036893
Cl    -1.544037    -0.369172    -0.0102
F    0.234908    1.513219    -1.048733
F    0.250089    1.45941    1.095963
O    -3.242368    -0.685998    -0.00465
C    0.267447    0.732937    0.004544
""",
)

entry(
    index = 151,
    label = "C2Cl4 + H <=> ClH-2 + C2Cl3",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(6.55379e+08,'cm^3/(mol*s)'), n=1.8839, Ea=(30.3745,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.19202, dn = +|- 0.0230769, dEa = +|- 0.125584 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ClC(Cl)DC(Cl)Cl + [H] <=> Cl + Cl[C]DC(Cl)Cl
barrier = 35.960566 kJ/mol
T1 = 0.016553109

Atom XYZ coordinates (angstrom)
Cl    -1.943505    -0.834776    0.426657
Cl    -0.952358    1.958109    -0.017365
Cl    1.101089    -1.809751    0.118089
Cl    2.071163    0.887295    -0.312458
C    -0.505912    0.328385    0.101604
C    0.727138    -0.142238    -0.014985
H    -3.011375    -2.01444    0.703563
""",
)

entry(
    index = 152,
    label = "C6H12Cl2-2 + H <=> ClH-2 + C6H12Cl-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.29536e+08,'cm^3/(mol*s)'), n=1.81809, Ea=(20.9771,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.14741, dn = +|- 0.018066, dEa = +|- 0.0983146 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: [H] + CC(C)(Cl)C(C)(C)Cl <=> Cl + C[C](C)C(C)(C)Cl
barrier = 25.931699 kJ/mol

Atom XYZ coordinates (angstrom)
Cl    -2.187594    -0.319961    -0.015246
Cl    2.236528    0.383543    0.003321
C    -0.455625    0.624934    -0.006113
C    0.612699    -0.486309    -0.005678
C    -0.503465    1.46361    1.251671
C    -0.494382    1.471297    -1.259036
C    0.592324    -1.35622    1.242148
C    0.601807    -1.347999    -1.259305
H    -0.665545    0.860194    2.140747
H    -1.314571    2.185076    1.177896
H    0.437012    2.006799    1.360281
H    0.447017    2.014767    -1.357782
H    -1.305743    2.192603    -1.186521
H    -0.650499    0.873352    -2.152863
H    -0.362758    -1.875993    1.31022
H    1.390057    -2.093383    1.177111
H    0.746052    -0.771439    2.145023
H    -0.352928    -1.866876    -1.338304
H    0.762887    -0.757357    -2.15707
H    1.398707    -2.085937    -1.192841
H    -3.717044    -1.151887    -0.028466
""",
)

entry(
    index = 153,
    label = "C4H6Cl4 + H <=> ClH-2 + C4H6Cl3",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(2.4415e+08,'cm^3/(mol*s)'), n=1.79753, Ea=(26.3422,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.14204, dn = +|- 0.0174498, dEa = +|- 0.094961 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: CC(C)(Cl)C(Cl)(Cl)Cl + [H] <=> Cl + CC(C)(Cl)[C](Cl)Cl
barrier = 31.560616 kJ/mol

Atom XYZ coordinates (angstrom)
Cl    -2.128001    -0.646517    0.417009
Cl    0.701019    4.3e-05    1.849371
Cl    1.717335    1.059151    -0.628485
Cl    0.80601    -1.735226    -0.52351
C    -0.937176    0.49383    -0.320142
C    -1.239074    1.888417    0.218257
C    -1.121936    0.444623    -1.831044
C    0.478453    0.0285    0.104317
H    -1.167696    1.918345    1.301943
H    -2.251888    2.157304    -0.074
H    -0.545367    2.610412    -0.210143
H    -2.145452    0.734182    -2.058955
H    -0.945651    -0.554232    -2.220079
H    -0.443594    1.145683    -2.31421
H    0.962422    -3.383886    -1.155262
""",
)

entry(
    index = 154,
    label = "ClHO-2 + CCl3-2 <=> CCl4 + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(40.2363,'cm^3/(mol*s)'), n=3.27282, Ea=(14.8511,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.08142, dn = +|- 0.0102844, dEa = +|- 0.0559671 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: OCl + Cl[C](Cl)Cl <=> ClC(Cl)(Cl)Cl + [OH]
barrier = 18.933259 kJ/mol
T1 = 0.025925438

Atom XYZ coordinates (angstrom)
Cl    -1.500343    -0.247047    -0.098673
Cl    1.20867    -1.52872    -0.364821
Cl    0.98688    0.710621    1.458049
Cl    0.924413    1.161395    -1.398491
O    -3.295856    0.126766    -0.072882
C    0.583815    0.06706    -0.100697
H    -3.407001    0.522583    0.802464
""",
)

entry(
    index = 155,
    label = "CH2BrCl + CHF2 <=> CHClF2 + CH2Br",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(35.1368,'cm^3/(mol*s)'), n=3.29448, Ea=(55.696,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.09572, dn = +|- 0.0120098, dEa = +|- 0.065357 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ClCBr + F[CH]F <=> [CH2]Br + FC(F)Cl
barrier = 59.792643 kJ/mol

Atom XYZ coordinates (angstrom)
Br    2.131198    0.94345    -1.291002
Cl    -0.789557    0.496424    0.05618
F    -3.484347    1.119153    0.280203
F    -3.046275    -0.933424    0.808725
C    1.174683    0.984954    0.340154
C    -2.812894    0.033632    -0.060731
H    1.521141    0.221164    1.020974
H    1.122445    1.986364    0.741813
H    -2.982728    -0.267771    -1.090516
""",
)

entry(
    index = 156,
    label = "Cl2 + O <=> ClO-3 + Cl",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.61204e+10,'cm^3/(mol*s)'), n=1.07817, Ea=(13.1778,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.03017, dn = +|- 0.003905, dEa = +|- 0.0212509 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: [Cl][Cl] + [O] <=> [O]Cl + [Cl]
barrier = 14.454558 kJ/mol
T1 = 0.040862565

Atom XYZ coordinates (angstrom)
Cl    1.966202    -0.153429    0.0
Cl    -0.042429    0.328761    -0.0
O    -1.923774    -0.175332    -0.0
""",
)

entry(
    index = 157,
    label = "C3H5Cl + H <=> ClH-2 + C3H5-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.55028e+07,'cm^3/(mol*s)'), n=1.93983, Ea=(41.02,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.20506, dn = +|- 0.024506, dEa = +|- 0.133361 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: [H] + CDC(C)Cl <=> Cl + CD[C]C
barrier = 47.101558 kJ/mol
T1 = 0.017644546

Atom XYZ coordinates (angstrom)
Cl    1.278544    -0.149152    -0.229556
C    -1.328533    -1.239704    -0.001015
C    -0.634278    0.06686    0.021806
C    -1.07554    1.292719    0.176565
H    -2.400046    -1.092572    0.141123
H    -0.949965    -1.887984    0.789241
H    -1.161413    -1.744981    -0.952257
H    -2.136784    1.466125    0.320455
H    -0.414475    2.147193    0.166099
H    2.8503    -0.325917    -0.432417
""",
)

entry(
    index = 158,
    label = "ClO-3 + C2H5-2 <=> C2H5Cl + O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3426.83,'cm^3/(mol*s)'), n=2.42175, Ea=(16.643,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.01473, dn = +|- 0.00192116, dEa = +|- 0.0104549 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: C[CH2] + [O]Cl <=> CCCl + [O]
barrier = 22.319351 kJ/mol
T1 = 0.028853285

Atom XYZ coordinates (angstrom)
Cl    0.77279    -0.153563    -0.05305
O    2.441385    0.385939    0.041959
C    -2.092398    0.668211    0.028832
C    -1.377869    -0.623983    -0.144312
H    -3.174034    0.498397    -0.007782
H    -1.859931    1.123502    0.989691
H    -1.839248    1.369896    -0.763716
H    -1.396714    -1.329679    0.675875
H    -1.375174    -1.076216    -1.127442
""",
)

entry(
    index = 159,
    label = "CH3Cl-2 + C3H6-2 <=> C3H6Cl-4 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(97.9469,'cm^3/(mol*s)'), n=3.46572, Ea=(44.1586,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.16079, dn = +|- 0.0195886, dEa = +|- 0.1066 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: CCl + C[C]C <=> [CH3] + C[C](C)Cl
barrier = 48.499909 kJ/mol
T1 = 0.020187561

Atom XYZ coordinates (angstrom)
Cl    0.798088    0.031561    -0.100834
C    -1.814703    -0.915014    -1.04079
C    -1.821013    0.777479    0.9903
C    -1.243154    0.16783    -0.220615
C    2.853138    0.031555    -0.094768
H    -2.866572    -0.711547    -1.263282
H    -1.764695    -1.8809    -0.522807
H    -1.27813    -1.02062    -1.983055
H    -2.873007    1.029996    0.826363
H    -1.288088    1.686752    1.266224
H    -1.772267    0.093844    1.847044
H    3.112251    -0.929197    -0.518648
H    3.118105    0.878882    -0.712349
H    3.107169    0.143265    0.95064
""",
)

entry(
    index = 160,
    label = "CCl4 + C2H3-2 <=> C2H3Cl-2 + CCl3-2",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(6041.93,'cm^3/(mol*s)'), n=3.07958, Ea=(21.8162,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.03865, dn = +|- 0.00498173, dEa = +|- 0.0271104 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ClC(Cl)(Cl)Cl + [CH]DC <=> CDCCl + Cl[C](Cl)Cl
barrier = 25.499224 kJ/mol

Atom XYZ coordinates (angstrom)
Cl    1.000576    0.356613    0.048669
Cl    -1.30827    -1.446625    0.632781
Cl    -1.686649    1.414243    0.813781
Cl    -1.360849    0.159277    -1.770554
C    3.186926    0.581443    0.163063
C    3.895343    -0.469243    -0.132844
C    -0.92284    0.110297    -0.07397
H    3.386274    1.595835    0.467666
H    4.981332    -0.433376    -0.098444
H    3.433661    -1.406384    -0.420547
""",
)

entry(
    index = 161,
    label = "C2H3Cl3-3 + H <=> ClH-2 + C2H3Cl2-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.48225e+07,'cm^3/(mol*s)'), n=1.97737, Ea=(24.4828,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.21245, dn = +|- 0.0253094, dEa = +|- 0.137733 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ClCC(Cl)Cl + [H] <=> Cl + [CH2]C(Cl)Cl
barrier = 31.064315 kJ/mol
T1 = 0.016032279

Atom XYZ coordinates (angstrom)
Cl    -2.293429    -0.374691    -0.232595
Cl    0.450362    1.603915    -0.181275
Cl    2.081008    -0.779151    0.274805
C    -0.461386    -0.929059    -0.516894
C    0.431335    -0.088507    0.344229
H    -0.451014    -1.970187    -0.214974
H    -0.277235    -0.793644    -1.576584
H    0.130084    -0.100839    1.385004
H    -3.862749    0.098881    0.011821
""",
)

entry(
    index = 162,
    label = "ClHO-2 + C2H2Cl-2 <=> C2H2Cl2 + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(330.289,'cm^3/(mol*s)'), n=3.11442, Ea=(-2.15891,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.03179, dn = +|- 0.00411109, dEa = +|- 0.0223724 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: OCl + CD[C]Cl <=> CDC(Cl)Cl + [OH]
barrier = 1.048483 kJ/mol

Atom XYZ coordinates (angstrom)
Cl    1.912635    -0.824689    0.019563
Cl    -1.274932    -0.1069    -0.08553
O    -3.007897    -0.276288    0.093799
C    1.137981    1.814158    0.048731
C    0.921572    0.526565    0.020452
H    2.147596    2.209615    0.062506
H    0.302841    2.500118    0.050526
H    -3.10287    -0.596577    0.999207
""",
)

entry(
    index = 163,
    label = "CClFO + CF3 <=> CClF3 + CFO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2891.19,'cm^3/(mol*s)'), n=2.26603, Ea=(69.0476,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.09898, dn = +|- 0.0124002, dEa = +|- 0.0674815 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ODC(F)Cl + F[C](F)F <=> FC(F)(F)Cl + OD[C]F
barrier = 71.397745 kJ/mol

Atom XYZ coordinates (angstrom)
Cl    -0.31924    -0.046577    0.06996
F    2.182437    -1.070749    -0.438807
F    2.088089    0.05893    1.395482
F    2.129707    1.083571    -0.500922
F    -2.758275    1.033781    -0.499639
O    -2.995175    -0.992088    0.36802
C    1.723885    0.013234    0.137412
C    -2.341032    -0.102381    0.00954
""",
)

entry(
    index = 164,
    label = "C2H2Cl4-2 + CH3 <=> CH3Cl-2 + C2H2Cl3-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(624500,'cm^3/(mol*s)'), n=1.78944, Ea=(30.2399,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.06376, dn = +|- 0.00812075, dEa = +|- 0.0441928 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ClCC(Cl)(Cl)Cl + [CH3] <=> CCl + ClC[C](Cl)Cl
barrier = 36.244952 kJ/mol
T1 = 0.016356877

Atom XYZ coordinates (angstrom)
Cl    2.649329    -0.864721    0.5618
Cl    -1.751071    -0.222443    0.091073
Cl    0.565829    0.375503    -1.774854
Cl    0.485167    1.704305    0.797503
C    0.869184    -0.978862    0.564995
C    -3.882127    -0.698387    0.270017
C    0.211821    0.216561    -0.073224
H    0.543474    -1.052574    1.597704
H    0.593172    -1.871562    0.012805
H    -4.239594    0.178911    0.787597
H    -4.156448    -0.790225    -0.76999
H    -3.844802    -1.613495    0.841514
""",
)

entry(
    index = 165,
    label = "C2H4ClF-2 + H <=> ClH-2 + C2H4F-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.12149e+07,'cm^3/(mol*s)'), n=2.00716, Ea=(29.5304,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.22536, dn = +|- 0.0267011, dEa = +|- 0.145306 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: FCCCl + [H] <=> Cl + [CH2]CF
barrier = 36.262390 kJ/mol
T1 = 0.017410185

Atom XYZ coordinates (angstrom)
Cl    -1.348627    -0.299465    0.0185
F    1.776238    -0.808425    -0.265309
C    1.364782    0.324979    0.402604
C    0.153346    0.902493    -0.254841
H    2.18479    1.048502    0.367995
H    1.165311    0.056405    1.44033
H    0.244064    0.974749    -1.333206
H    -0.167256    1.834468    0.198352
H    -2.600382    -1.347749    0.257517
""",
)

entry(
    index = 166,
    label = "CH2Cl2 + CF3 <=> CClF3 + CH2Cl-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(169.146,'cm^3/(mol*s)'), n=3.38543, Ea=(44.8483,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.12139, dn = +|- 0.0150517, dEa = +|- 0.0819108 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ClCCl + F[C](F)F <=> FC(F)(F)Cl + [CH2]Cl
barrier = 48.125749 kJ/mol
T1 = 0.018450604

Atom XYZ coordinates (angstrom)
Cl    0.259469    -0.304857    0.030327
Cl    3.066804    -0.306609    -1.277973
F    -1.964052    0.96757    -1.060409
F    -2.45153    -0.921567    -0.141468
F    -2.064895    0.80733    1.087878
C    2.228921    -0.81658    0.143482
C    -1.752989    0.185414    -0.02689
H    2.183427    -1.892867    0.228195
H    2.55571    -0.283769    1.024949
""",
)

entry(
    index = 167,
    label = "ClO-3 + CFO <=> CClFO + O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(589857,'cm^3/(mol*s)'), n=1.65372, Ea=(28.2843,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.05345, dn = +|- 0.00684134, dEa = +|- 0.0372303 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: [O]Cl + OD[C]F <=> ODC(F)Cl + [O]
barrier = 31.609122 kJ/mol
T1 = 0.032374957999999995

Atom XYZ coordinates (angstrom)
Cl    -0.925062    0.106177    -0.090626
F    1.588676    -1.160332    -0.001394
O    1.854229    1.040729    0.145429
O    -2.569007    -0.071411    0.314408
C    1.201119    0.091025    0.007543
""",
)

entry(
    index = 168,
    label = "C4H7Cl + H <=> ClH-2 + C4H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.42968e+07,'cm^3/(mol*s)'), n=1.88465, Ea=(46.2174,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.16471, dn = +|- 0.0200323, dEa = +|- 0.109015 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: [H] + CC(C)DCCl <=> Cl + [CH]DC(C)C
barrier = 51.600902 kJ/mol
T1 = 0.016782997

Atom XYZ coordinates (angstrom)
Cl    2.571894    -0.040677    -0.712582
C    -0.317907    1.31096    -0.080153
C    -1.448391    -0.886784    0.518379
C    -0.19466    -0.174371    0.076879
C    0.902307    -0.868645    -0.140016
H    -1.095422    1.542036    -0.810979
H    -0.626745    1.758316    0.8667
H    0.612915    1.769281    -0.399255
H    -2.250525    -0.709327    -0.200594
H    -1.781447    -0.493023    1.4806
H    -1.297516    -1.959602    0.61432
H    1.054273    -1.932942    -0.045025
H    3.871222    0.684779    -1.168273
""",
)

entry(
    index = 169,
    label = "CCl2O + H <=> ClH-2 + CClO",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.34563e+08,'cm^3/(mol*s)'), n=1.83026, Ea=(24.9557,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.1627, dn = +|- 0.0198054, dEa = +|- 0.10778 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ODC(Cl)Cl + [H] <=> Cl + OD[C]Cl
barrier = 30.787342 kJ/mol
T1 = 0.021802742000000003

Atom XYZ coordinates (angstrom)
Cl    -1.434336    -0.233709    0.368495
Cl    1.49405    -0.615505    -0.093715
O    0.349762    1.723063    -0.115485
C    0.225798    0.573988    0.011815
H    -2.997782    -0.897597    0.69577
""",
)

entry(
    index = 170,
    label = "C2Cl3F3 + H <=> ClH-2 + C2Cl2F3",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(3.93247e+08,'cm^3/(mol*s)'), n=1.7963, Ea=(27.6198,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.14261, dn = +|- 0.0175146, dEa = +|- 0.0953139 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: FC(F)(F)C(Cl)(Cl)Cl + [H] <=> Cl + FC(F)(F)[C](Cl)Cl
barrier = 32.787577 kJ/mol

Atom XYZ coordinates (angstrom)
Cl    1.620102    0.98316    0.005498
Cl    0.461737    -1.337843    -1.428088
Cl    0.460483    -1.317735    1.470158
F    -2.052492    -0.527675    0.014414
F    -1.182467    1.11312    -1.073383
F    -1.18338    1.128079    1.080049
C    -1.061182    0.356798    0.008691
C    0.302343    -0.36686    0.014299
H    2.745702    2.345314    -0.003444
""",
)

entry(
    index = 171,
    label = "CCl2F2 + CH3 <=> CH3Cl-2 + CClF2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(12306.9,'cm^3/(mol*s)'), n=2.71255, Ea=(51.3353,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.08845, dn = +|- 0.011135, dEa = +|- 0.0605964 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: FC(F)(Cl)Cl + [CH3] <=> CCl + F[C](F)Cl
barrier = 57.555877 kJ/mol
T1 = 0.018008747

Atom XYZ coordinates (angstrom)
Cl    -1.241003    0.076208    -0.004536
Cl    1.633812    -1.069539    0.010473
F    1.000682    1.153519    1.068719
F    1.006539    1.140098    -1.078908
C    0.736207    0.42826    -0.001334
C    -3.34615    -0.12237    -0.009566
H    -3.625431    0.386335    0.901588
H    -3.464724    -1.196324    -0.003684
H    -3.620139    0.375722    -0.928158
""",
)

entry(
    index = 172,
    label = "C2H5ClO-2 + O <=> ClO-3 + C2H5O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.5379e+08,'cm^3/(mol*s)'), n=1.59378, Ea=(-0.151855,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.02238, dn = +|- 0.00290798, dEa = +|- 0.0158251 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: CCOCl + [O] <=> [O]Cl + CC[O]
barrier = 1.620486 kJ/mol
T1 = 0.035668974

Atom XYZ coordinates (angstrom)
Cl    -0.948894    -0.432167    0.040348
O    0.633907    -1.00498    -0.298403
O    -2.352024    0.876723    -0.049221
C    1.63383    -0.272878    0.406614
C    1.841304    1.115237    -0.159805
H    2.527791    -0.886169    0.282919
H    1.381707    -0.240914    1.469312
H    2.658397    1.612454    0.362109
H    0.94212    1.719238    -0.039778
H    2.084637    1.059012    -1.219508
""",
)

entry(
    index = 173,
    label = "CH2Cl2 + CH2Br <=> CH2BrCl + CH2Cl-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(4096.87,'cm^3/(mol*s)'), n=2.00995, Ea=(72.76,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.00552, dn = +|- 0.000723727, dEa = +|- 0.0039385 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ClCCl + [CH2]Br <=> [CH2]Cl + ClCBr
barrier = 78.580656 kJ/mol

Atom XYZ coordinates (angstrom)
Br    -2.307929    0.541087    0.293357
Cl    0.930446    0.097363    0.182063
Cl    4.03721    -0.244846    0.32738
C    -0.936255    -0.739435    0.505381
C    2.817139    0.887264    -0.140653
H    -0.864245    -1.08222    1.527003
H    -0.984386    -1.505937    -0.253831
H    2.810215    1.064932    -1.206172
H    2.80618    1.762917    0.49189
""",
)

entry(
    index = 174,
    label = "C2Cl6 + CH3 <=> CH3Cl-2 + C2Cl5",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(61254.6,'cm^3/(mol*s)'), n=2.77509, Ea=(40.8245,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.06745, dn = +|- 0.00857493, dEa = +|- 0.0466644 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ClC(Cl)(Cl)C(Cl)(Cl)Cl + [CH3] <=> CCl + Cl[C](Cl)C(Cl)(Cl)Cl
barrier = 47.003943 kJ/mol

Atom XYZ coordinates (angstrom)
Cl    -1.866852    0.066996    -0.134335
Cl    0.433044    1.134092    -1.76542
Cl    0.196926    1.957093    0.987092
Cl    2.623465    -0.153708    0.316621
Cl    0.425478    -1.110556    1.925262
Cl    0.661331    -1.934424    -0.82948
C    0.05316    0.631457    -0.138292
C    0.898174    -0.592434    0.300133
C    -3.937801    -0.624526    -0.106685
H    -3.801797    -1.667702    0.13491
H    -4.235246    -0.397135    -1.11919
H    -4.346064    0.003026    0.671016
""",
)

entry(
    index = 175,
    label = "CHCl3 + CH2Cl-2 <=> CH2Cl2 + CHCl2",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(5143.18,'cm^3/(mol*s)'), n=1.9068, Ea=(48.9097,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.03458, dn = +|- 0.00446603, dEa = +|- 0.024304 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ClC(Cl)Cl + [CH2]Cl <=> Cl[CH]Cl + ClCCl
barrier = 54.695678 kJ/mol
T1 = 0.018555911

Atom XYZ coordinates (angstrom)
Cl    0.423253    -0.334555    0.36964
Cl    3.39914    0.185612    1.283314
Cl    -2.428247    -1.220128    1.108683
Cl    -2.096713    0.661979    -1.085924
C    2.477503    -0.835434    0.247099
C    -1.561365    0.14368    0.479873
H    2.458993    -1.863634    0.576927
H    2.671127    -0.657278    -0.800334
H    -1.548602    0.962872    1.184341
""",
)

entry(
    index = 176,
    label = "CH2Cl2 + C2H3-2 <=> C2H3Cl-2 + CH2Cl-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(709.333,'cm^3/(mol*s)'), n=3.20018, Ea=(34.7131,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.06789, dn = +|- 0.00863027, dEa = +|- 0.0469656 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ClCCl + [CH]DC <=> [CH2]Cl + CDCCl
barrier = 39.286425 kJ/mol
T1 = 0.01905928

Atom XYZ coordinates (angstrom)
Cl    2.292618    -0.670539    0.074301
Cl    -0.517394    0.557663    -0.150214
C    1.449564    0.817411    -0.249184
C    -3.047109    -0.951582    -0.067939
C    -2.601226    0.274833    -0.065436
H    1.619328    1.148791    -1.263942
H    1.654742    1.555388    0.513517
H    -2.375513    -1.800472    -0.113053
H    -4.113416    -1.154608    -0.023588
H    -3.087207    1.237175    -0.025927
""",
)

entry(
    index = 177,
    label = "C3H6Cl2 + CH2F <=> CH2ClF + C3H6Cl-7",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(671.175,'cm^3/(mol*s)'), n=3.00594, Ea=(48.0169,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.00595, dn = +|- 0.00077967, dEa = +|- 0.00424294 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: CCC(Cl)Cl + [CH2]F <=> CC[CH]Cl + FCCl
barrier = 52.889307 kJ/mol
T1 = 0.017282298

Atom XYZ coordinates (angstrom)
Cl    -0.784498    -0.465679    -0.258811
Cl    2.189766    -1.103119    0.189192
F    -3.504899    0.134876    0.126362
C    1.258925    1.446899    0.446309
C    0.42828    2.588045    -0.127523
C    -2.824436    -0.996389    -0.094991
C    1.162511    0.195285    -0.373885
H    0.95621    1.216492    1.469117
H    2.314703    1.732211    0.485627
H    0.576094    3.49334    0.458709
H    -0.632001    2.343099    -0.118674
H    0.720111    2.803197    -1.15617
H    -2.829019    -1.653807    0.765272
H    -3.040562    -1.421904    -1.066844
H    1.273721    0.313887    -1.445283
""",
)

entry(
    index = 178,
    label = "CH2BrCl + CH3 <=> CH3Cl-2 + CH2Br",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3005.42,'cm^3/(mol*s)'), n=2.90586, Ea=(66.3756,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.039, dn = +|- 0.00502588, dEa = +|- 0.0273506 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: [CH3] + ClCBr <=> CCl + [CH2]Br
barrier = 73.432878 kJ/mol

Atom XYZ coordinates (angstrom)
Br    -1.746891    0.533816    -1.122391
Cl    1.252952    0.043402    0.02523
C    -0.44575    1.160285    0.105477
C    3.045604    -1.05856    0.009135
H    -0.781913    1.035932    1.124375
H    -0.108727    2.151961    -0.158389
H    3.789355    -0.301031    -0.192414
H    2.872491    -1.763344    -0.791559
H    3.072899    -1.482723    1.002593
""",
)

entry(
    index = 179,
    label = "ClHO-2 + C2H3ClF <=> C2H3Cl2F + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(25.9217,'cm^3/(mol*s)'), n=3.15405, Ea=(-2.33293,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.04401, dn = +|- 0.00565879, dEa = +|- 0.0307949 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: OCl + C[C](F)Cl <=> CC(F)(Cl)Cl + [OH]
barrier = 0.690833 kJ/mol

Atom XYZ coordinates (angstrom)
Cl    1.664721    -1.070656    -0.12618
Cl    -1.336541    -0.157774    -0.100408
F    0.889834    0.81917    1.371694
O    -3.134647    -0.245163    -0.09303
C    0.999781    1.484286    -0.893282
C    0.800925    0.406714    0.113542
H    0.79636    1.101776    -1.889135
H    2.031559    1.840239    -0.841956
H    0.320092    2.30332    -0.668171
H    -3.334878    -0.197969    0.850471
""",
)

entry(
    index = 180,
    label = "C2H4Cl2O + CH3 <=> CH3Cl-2 + C2H4ClO-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(8323.64,'cm^3/(mol*s)'), n=2.75776, Ea=(53.3391,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.08108, dn = +|- 0.0102422, dEa = +|- 0.0557376 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: CC(O)(Cl)Cl + [CH3] <=> CCl + C[C](O)Cl
barrier = 59.665358 kJ/mol

Atom XYZ coordinates (angstrom)
Cl    -1.292238    0.122046    0.096829
Cl    1.514304    -1.077789    0.138601
O    0.947434    1.159681    1.366325
C    0.722481    0.520278    0.200747
C    1.052169    1.377034    -0.979618
C    -3.430518    -0.226451    0.03053
H    2.118241    1.608556    -0.968187
H    0.80114    0.857911    -1.8995
H    0.480037    2.2999    -0.908881
H    -3.685933    0.152864    -0.947981
H    -3.777609    0.359215    0.869061
H    -3.479455    -1.298899    0.149109
H    0.701281    0.590179    2.105046
""",
)

entry(
    index = 181,
    label = "C2H2Cl2 + H <=> ClH-2 + C2H2Cl-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.10586e+08,'cm^3/(mol*s)'), n=1.9091, Ea=(36.7923,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.20433, dn = +|- 0.0244261, dEa = +|- 0.132926 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: CDC(Cl)Cl + [H] <=> Cl + CD[C]Cl
barrier = 42.919777 kJ/mol
T1 = 0.018130297

Atom XYZ coordinates (angstrom)
Cl    0.601877    2.161916    -0.22416
Cl    1.421264    -0.735886    -0.202984
C    -1.192028    0.177529    0.182675
C    0.043306    0.560908    -0.044188
H    -1.423515    -0.872717    0.278409
H    -1.984493    0.907443    0.274962
H    2.485316    -1.942948    -0.307001
""",
)

entry(
    index = 182,
    label = "ClO-3 + H <=> ClH-2 + O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.99623e+09,'cm^3/(mol*s)'), n=1.20842, Ea=(11.801,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.08452, dn = +|- 0.0106595, dEa = +|- 0.0580086 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: [O]Cl + [H] <=> Cl + [O]
barrier = 15.543406 kJ/mol
T1 = 0.038035604

Atom XYZ coordinates (angstrom)
Cl    -0.080145    0.188152    0.0
O    -1.673196    -0.09001    0.0
H    1.753441    -0.098142    0.0
""",
)

entry(
    index = 183,
    label = "CH3Cl-2 + H <=> ClH-2 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.59764e+07,'cm^3/(mol*s)'), n=2.07537, Ea=(33.054,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.25697, dn = +|- 0.0300472, dEa = +|- 0.163516 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: CCl + [H] <=> Cl + [CH3]
barrier = 39.899528 kJ/mol
T1 = 0.020526098

Atom XYZ coordinates (angstrom)
Cl    -0.601279    -0.183737    -0.000182
C    1.340324    -0.049523    -0.00068
H    1.551614    0.991765    -0.205693
H    1.669707    -0.717972    -0.785311
H    1.645762    -0.363851    0.988702
H    -2.226765    -0.296149    0.000235
""",
)

entry(
    index = 184,
    label = "CH3ClO-2 + H <=> ClH-2 + CH3O-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.8207e+07,'cm^3/(mol*s)'), n=1.91432, Ea=(26.9905,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.18749, dn = +|- 0.0225768, dEa = +|- 0.122862 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: OCCl + [H] <=> Cl + [CH2]O
barrier = 33.632310 kJ/mol
T1 = 0.020455006

Atom XYZ coordinates (angstrom)
Cl    -1.024665    -0.218182    0.001929
O    1.726144    -0.411981    0.116075
C    0.784934    0.55332    -0.046152
H    0.791389    1.227031    0.80047
H    0.785038    1.05032    -1.011773
H    1.762808    -0.974746    -0.663344
H    -2.579538    -0.910389    0.0451
""",
)

entry(
    index = 185,
    label = "ClHO-2 + CHCl2 <=> CHCl3 + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(71.5617,'cm^3/(mol*s)'), n=3.06916, Ea=(6.22331,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.01411, dn = +|- 0.00184138, dEa = +|- 0.0100207 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: OCl + Cl[CH]Cl <=> ClC(Cl)Cl + [OH]
barrier = 10.626284 kJ/mol
T1 = 0.025200557000000002

Atom XYZ coordinates (angstrom)
Cl    1.129001    -1.636096    0.046697
Cl    1.54616    1.217261    -0.337419
Cl    -1.355555    0.307305    0.175633
O    -3.166752    0.258825    0.244014
C    0.754747    -0.03206    0.53354
H    0.780863    0.108066    1.603979
H    -3.354575    -0.65646    -0.00195
""",
)

entry(
    index = 186,
    label = "ClO-3 + C2H3-2 <=> C2H3Cl-2 + O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2855.47,'cm^3/(mol*s)'), n=2.56268, Ea=(6.09476,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.02474, dn = +|- 0.00321021, dEa = +|- 0.0174698 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: [O]Cl + [CH]DC <=> CDCCl + [O]
barrier = 11.000927 kJ/mol
T1 = 0.031873768999999996

Atom XYZ coordinates (angstrom)
Cl    1.741388    -0.28185    0.167273
O    3.381629    -0.662667    0.229415
C    -0.3326    1.887735    -0.240883
C    -0.263089    0.612443    0.007597
H    0.557261    2.492818    -0.365653
H    -1.296221    2.382374    -0.330284
H    -0.961183    -0.193521    0.170161
""",
)

entry(
    index = 187,
    label = "CH3Cl-2 + CH2-2 <=> CH2Cl + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(175826,'cm^3/(mol*s)'), n=2.33022, Ea=(53.7341,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.10284, dn = +|- 0.0128601, dEa = +|- 0.0699841 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: CCl + [CH2] <=> [CH3] + [CH2]Cl
barrier = 59.329051 kJ/mol
T1 = 0.023618762999999997

Atom XYZ coordinates (angstrom)
Cl    0.238789    0.022019    -0.03759
C    -1.775703    -0.144114    0.138695
C    2.251854    0.174712    -0.10942
H    -1.97469    -1.180573    -0.097754
H    -2.158186    0.560659    -0.587207
H    -1.973506    0.124283    1.167559
H    2.764797    -0.740369    -0.349259
H    2.626645    1.183283    -0.125125
""",
)

entry(
    index = 188,
    label = "CH2Cl2 + H <=> ClH-2 + CH2Cl-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(5.76038e+07,'cm^3/(mol*s)'), n=1.94327, Ea=(26.4699,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.20116, dn = +|- 0.02408, dEa = +|- 0.131043 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ClCCl + [H] <=> Cl + [CH2]Cl
barrier = 33.058989 kJ/mol
T1 = 0.018678341

Atom XYZ coordinates (angstrom)
Cl    -1.478639    0.004653    0.311708
Cl    1.504546    -0.329197    -0.07193
C    0.225842    0.84886    0.062692
H    0.125983    1.409369    -0.856385
H    0.363141    1.461164    0.943076
H    -3.017445    -0.640106    0.532064
""",
)

entry(
    index = 189,
    label = "C2H4Cl2-2 + H <=> ClH-2 + C2H4Cl-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(5.70062e+07,'cm^3/(mol*s)'), n=1.97907, Ea=(27.5456,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.21617, dn = +|- 0.0257118, dEa = +|- 0.139922 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ClCCCl + [H] <=> Cl + [CH2]CCl
barrier = 34.012843 kJ/mol
T1 = 0.016917271

Atom XYZ coordinates (angstrom)
Cl    2.105399    -0.019457    0.32378
Cl    -2.286616    0.026171    -0.274601
C    0.29803    0.659602    0.089126
C    -0.592378    -0.534854    -0.053642
H    0.110739    1.24318    0.982725
H    0.354219    1.275039    -0.800998
H    -0.575795    -1.158501    0.834133
H    -0.335827    -1.127123    -0.92585
H    3.65654    -0.581709    0.520402
""",
)

entry(
    index = 190,
    label = "C3H6ClF + CH2F <=> CH2ClF + C3H6F",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(14873.4,'cm^3/(mol*s)'), n=1.93367, Ea=(56.6062,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.02492, dn = +|- 0.00323348, dEa = +|- 0.0175965 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: [CH2]F + CC(C)(F)Cl <=> FCCl + C[C](C)F
barrier = 60.991438 kJ/mol
T1 = 0.017697626

Atom XYZ coordinates (angstrom)
Cl    -0.576057    0.222694    0.087241
F    1.738796    -0.383326    1.434337
F    -3.183085    -0.116181    -0.915353
C    1.455566    -0.247506    0.115378
C    2.14908    0.943839    -0.458868
C    1.566672    -1.556978    -0.593294
C    -2.645383    0.632016    0.058543
H    1.925649    1.83018    0.131064
H    3.229658    0.774683    -0.448274
H    1.82582    1.105011    -1.484779
H    0.963666    -2.309319    -0.089598
H    2.611112    -1.881621    -0.594723
H    1.225258    -1.455021    -1.620942
H    -2.684054    1.689401    -0.17217
H    -2.968974    0.315277    1.042139
""",
)

entry(
    index = 191,
    label = "ClHO-2 + C2Cl2F3 <=> C2Cl3F3 + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(11.9048,'cm^3/(mol*s)'), n=3.22184, Ea=(21.2228,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.06411, dn = +|- 0.0081644, dEa = +|- 0.0444304 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: OCl + FC(F)(F)[C](Cl)Cl <=> FC(F)(F)C(Cl)(Cl)Cl + [OH]
barrier = 25.211353 kJ/mol

Atom XYZ coordinates (angstrom)
Cl    -1.693534    -0.423041    -0.26448
Cl    0.602211    -1.301673    1.626882
Cl    1.02523    -1.472143    -1.238482
F    0.610893    1.45782    -1.0991
F    0.263402    1.584566    1.024261
F    2.185753    0.961323    0.281308
O    -3.342624    0.294132    -0.462517
C    0.871308    0.891317    0.069547
C    0.404578    -0.565397    0.083946
H    -3.524476    0.647543    0.419066
""",
)

entry(
    index = 192,
    label = "C4H6Cl3F + H <=> ClH-2 + C4H6Cl2F",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(1.40841e+08,'cm^3/(mol*s)'), n=1.75719, Ea=(11.0326,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.114, dn = +|- 0.0141836, dEa = +|- 0.0771868 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: CC(C)(F)C(Cl)(Cl)Cl + [H] <=> Cl + CC(C)(F)[C](Cl)Cl
barrier = 16.147129 kJ/mol
T1 = 0.014874051000000001

Atom XYZ coordinates (angstrom)
Cl    0.863863    1.067897    -1.354359
Cl    0.862766    0.9142    1.512579
Cl    1.197693    -1.568451    -0.057938
F    -1.761781    1.157147    0.087359
C    -1.201805    -0.113725    0.019126
C    -1.67688    -0.886533    1.235418
C    -1.676084    -0.751458    -1.273403
C    0.330373    0.128994    0.032697
H    -2.762327    -0.949719    1.185029
H    -1.398534    -0.378419    2.154385
H    -1.265295    -1.892972    1.239095
H    -1.263468    -1.751221    -1.385481
H    -2.761469    -0.820807    -1.230303
H    -1.398211    -0.146958    -2.132194
H    1.912099    -3.182921    -0.144245
""",
)

entry(
    index = 193,
    label = "C4H9Cl-2 + H <=> ClH-2 + C4H9-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.78004e+07,'cm^3/(mol*s)'), n=1.9284, Ea=(27.5148,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.19651, dn = +|- 0.0235708, dEa = +|- 0.128271 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: CCC(C)Cl + [H] <=> Cl + C[CH]CC
barrier = 33.609516 kJ/mol
T1 = 0.015759256

Atom XYZ coordinates (angstrom)
Cl    -1.744742    -0.339962    0.104159
C    1.015982    -0.74984    0.272889
C    2.474625    -0.450938    -0.076663
C    0.193663    1.670142    0.194165
C    0.075154    0.264791    -0.328482
H    0.746485    -1.742342    -0.088091
H    0.882983    -0.755556    1.356696
H    3.124716    -1.239018    0.30062
H    2.613601    -0.390422    -1.156995
H    2.80577    0.490673    0.359676
H    -0.592367    2.306736    -0.206232
H    0.130644    1.679142    1.282655
H    1.156588    2.095752    -0.098416
H    0.056992    0.219525    -1.414949
H    -3.296339    -0.852041    0.486945
""",
)

entry(
    index = 194,
    label = "ClO-3 + CCl3-2 <=> CCl4 + O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(56787.5,'cm^3/(mol*s)'), n=1.80944, Ea=(49.22,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.11315, dn = +|- 0.0140832, dEa = +|- 0.0766405 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: [O]Cl + Cl[C](Cl)Cl <=> ClC(Cl)(Cl)Cl + [O]
barrier = 52.430802 kJ/mol
T1 = 0.030132528

Atom XYZ coordinates (angstrom)
Cl    1.505307    -0.328918    0.197888
Cl    -1.149517    -1.315927    -0.862365
Cl    -0.643452    1.532699    -0.965058
Cl    -1.123977    0.239223    1.580003
O    3.284662    -0.136968    0.056895
C    -0.515482    0.073799    -0.037459
""",
)

entry(
    index = 195,
    label = "CCl4 + CH3 <=> CH3Cl-2 + CCl3-2",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(114819,'cm^3/(mol*s)'), n=2.77954, Ea=(26.778,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.06565, dn = +|- 0.00835344, dEa = +|- 0.0454591 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ClC(Cl)(Cl)Cl + [CH3] <=> CCl + Cl[C](Cl)Cl
barrier = 32.898137 kJ/mol
T1 = 0.016935741

Atom XYZ coordinates (angstrom)
Cl    1.382621    0.036307    -0.029533
Cl    -1.154756    -0.596433    1.476975
Cl    -1.117848    1.710312    -0.267023
Cl    -1.121347    -0.953552    -1.392585
C    -0.611769    0.050073    -0.054437
C    3.57569    0.020085    -0.003511
H    3.762031    0.056028    1.059061
H    3.773358    -0.918308    -0.498912
H    3.787676    0.918098    -0.563589
""",
)

entry(
    index = 196,
    label = "CCl2F2 + C2H5-2 <=> C2H5Cl + CClF2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(16870.5,'cm^3/(mol*s)'), n=1.82185, Ea=(41.7134,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.04151, dn = +|- 0.00534405, dEa = +|- 0.0290821 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: C[CH2] + FC(F)(Cl)Cl <=> CCCl + F[C](F)Cl
barrier = 46.555927 kJ/mol
T1 = 0.017216601

Atom XYZ coordinates (angstrom)
Cl    0.775192    0.552234    -0.137931
Cl    -2.078271    1.770409    0.078681
F    -1.555401    -0.356859    -1.213372
F    -1.475517    -0.551376    0.924272
C    3.398264    -0.51562    0.564953
C    2.894556    0.678463    -0.173272
C    -1.224773    0.254977    -0.091004
H    4.492671    -0.505178    0.585003
H    3.045341    -0.520298    1.594803
H    3.081804    -1.43914    0.083217
H    3.057142    0.698889    -1.243453
H    3.020871    1.641415    0.305477
""",
)

entry(
    index = 197,
    label = "C2H3Cl3 + CF3 <=> CClF3 + C2H3Cl2-3",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(507.899,'cm^3/(mol*s)'), n=3.21727, Ea=(37.6247,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.07457, dn = +|- 0.00944874, dEa = +|- 0.0514197 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: CC(Cl)(Cl)Cl + F[C](F)F <=> FC(F)(F)Cl + C[C](Cl)Cl
barrier = 39.894755 kJ/mol

Atom XYZ coordinates (angstrom)
Cl    -0.539572    0.08692    0.077929
Cl    1.988123    1.719293    -0.132467
Cl    2.123113    -1.12369    -0.65857
F    -3.091224    1.23754    -0.420832
F    -3.189782    -0.397306    0.98457
F    -2.959442    -0.798907    -1.12343
C    1.659049    -0.13208    1.825822
C    1.451887    0.128908    0.362271
C    -2.672288    0.025738    -0.145074
H    1.244884    -1.104809    2.081086
H    2.727337    -0.122001    2.043542
H    1.16251    0.643483    2.404471
""",
)

entry(
    index = 198,
    label = "Cl2 + CCl2F <=> CCl3F + Cl",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(40289.7,'cm^3/(mol*s)'), n=2.57076, Ea=(1.63465,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.02715, dn = +|- 0.00351889, dEa = +|- 0.0191496 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: [Cl][Cl] + F[C](Cl)Cl <=> FC(Cl)(Cl)Cl + [Cl]
barrier = 3.144070 kJ/mol

Atom XYZ coordinates (angstrom)
Cl    -1.596896    1.53317    -0.358224
Cl    -1.719586    -1.382738    -0.3987
Cl    1.150705    -0.046288    -0.133528
Cl    3.272777    -0.136871    -0.088571
F    -1.103117    0.024195    1.613726
C    -1.073128    0.041137    0.302892
""",
)

entry(
    index = 199,
    label = "CH3Cl-2 + CHF2 <=> CHClF2 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(23.7629,'cm^3/(mol*s)'), n=3.44894, Ea=(60.7232,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.14391, dn = +|- 0.0176643, dEa = +|- 0.0961285 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: F[CH]F + CCl <=> FC(F)Cl + [CH3]
barrier = 65.602888 kJ/mol
T1 = 0.019329607

Atom XYZ coordinates (angstrom)
Cl    -0.722774    -0.027834    0.044296
F    1.832748    -0.881818    -0.508403
F    1.736676    1.203566    0.065202
C    1.298872    -0.015845    0.339501
C    -2.765814    -0.011461    -0.359642
H    1.459718    -0.293878    1.377247
H    -2.944261    1.009377    -0.66676
H    -3.20271    -0.288249    0.589644
H    -2.864113    -0.749833    -1.142852
""",
)

entry(
    index = 200,
    label = "C3H4Cl2-2 + H <=> ClH-2 + C3H4Cl-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.77168e+07,'cm^3/(mol*s)'), n=1.89866, Ea=(45.4348,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.1726, dn = +|- 0.0209191, dEa = +|- 0.113841 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: CC(Cl)DCCl + [H] <=> Cl + [CH]DC(C)Cl
barrier = 51.274040 kJ/mol
T1 = 0.016825516999999998

Atom XYZ coordinates (angstrom)
Cl    0.878483    -1.327979    -0.128981
Cl    -2.02966    0.168519    -0.183262
C    2.154132    1.069481    0.001911
C    0.81357    0.40843    -0.070542
C    -0.330652    1.054992    -0.090037
H    2.043912    2.151292    0.035835
H    2.750996    0.796643    -0.86823
H    2.686325    0.734848    0.892205
H    -0.451857    2.126335    -0.056872
H    -3.31274    -0.702474    -0.259
""",
)

entry(
    index = 201,
    label = "ClO-3 + C3H6Cl-6 <=> C3H6Cl2-3 + O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(495.128,'cm^3/(mol*s)'), n=2.66142, Ea=(17.7217,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.07389, dn = +|- 0.00936614, dEa = +|- 0.0509702 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: C[C](C)Cl + [O]Cl <=> CC(C)(Cl)Cl + [O]
barrier = 22.011471 kJ/mol

Atom XYZ coordinates (angstrom)
Cl    0.837845    -1.066609    -0.467891
Cl    -1.788047    -0.799308    1.151144
O    -3.443659    -1.235045    1.646184
C    -0.349418    1.352417    -0.184472
C    0.775181    0.302454    1.870775
C    0.08609    0.128908    0.555124
H    -0.95138    1.09218    -1.051773
H    0.533409    1.901513    -0.524058
H    -0.929673    1.992693    0.478035
H    1.750898    0.768447    1.704396
H    0.927761    -0.654198    2.364665
H    0.181704    0.951656    2.512811
""",
)

entry(
    index = 202,
    label = "CH2BrCl + H <=> ClH-2 + CH2Br",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.68653e+07,'cm^3/(mol*s)'), n=1.9768, Ea=(34.9034,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.22377, dn = +|- 0.0265308, dEa = +|- 0.14438 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ClCBr + [H] <=> Cl + [CH2]Br
barrier = 41.547961 kJ/mol

Atom XYZ coordinates (angstrom)
Br    1.089823    -0.227929    -0.005593
Cl    -2.068964    -0.031578    0.040767
C    -0.418715    0.935696    0.008712
H    -0.445182    1.515803    -0.902692
H    -0.417737    1.529089    0.911914
H    -3.60544    -0.706096    0.066977
""",
)

entry(
    index = 203,
    label = "C3H5Cl-2 + H <=> ClH-2 + C3H5-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.32043e+07,'cm^3/(mol*s)'), n=1.91844, Ea=(22.9782,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.18321, dn = +|- 0.0221019, dEa = +|- 0.120278 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: CDCCCl + [H] <=> Cl + [CH2]CDC
barrier = 28.947173 kJ/mol
T1 = 0.017183398

Atom XYZ coordinates (angstrom)
Cl    1.498896    -0.124945    -0.069554
C    -1.224048    0.125353    0.447677
C    -0.154914    0.87809    -0.221849
C    -2.204153    -0.483364    -0.210062
H    -1.175824    0.07075    1.529051
H    0.109518    1.815052    0.254563
H    -0.29294    0.986766    -1.291698
H    -2.260201    -0.447604    -1.291129
H    -2.978551    -1.030378    0.308902
H    3.03709    -0.925171    -0.026315
""",
)

entry(
    index = 204,
    label = "CHCl3O + CH3 <=> CH3Cl-2 + CHCl2O-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(658020,'cm^3/(mol*s)'), n=1.76817, Ea=(33.1442,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.07097, dn = +|- 0.00900825, dEa = +|- 0.0490226 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: OC(Cl)(Cl)Cl + [CH3] <=> O[C](Cl)Cl + CCl
barrier = 39.157397 kJ/mol
T1 = 0.01786892

Atom XYZ coordinates (angstrom)
Cl    -1.314173    -1.500984    -0.334728
Cl    -1.270586    1.407356    -0.514093
Cl    1.334006    -0.033173    0.060067
O    -0.905974    0.001579    1.658486
C    -0.666997    -0.02991    0.337317
C    3.516932    -0.034632    -0.142055
H    3.653572    -0.848269    -0.838333
H    3.688206    0.960072    -0.525202
H    3.822821    -0.218163    0.876884
H    -0.491156    0.79007    2.032928
""",
)

entry(
    index = 205,
    label = "C2H5Cl + H <=> ClH-2 + C2H5-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.32804e+07,'cm^3/(mol*s)'), n=1.99427, Ea=(30.0451,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.21837, dn = +|- 0.0259499, dEa = +|- 0.141218 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: CCCl + [H] <=> Cl + C[CH2]
barrier = 36.650117 kJ/mol
T1 = 0.01822329

Atom XYZ coordinates (angstrom)
Cl    -1.030477    0.344056    7e-06
C    1.788051    0.416292    -2e-06
C    0.683925    -0.599552    4e-06
H    2.755593    -0.091961    -3e-06
H    1.736158    1.04932    -0.883924
H    1.736163    1.049325    0.883917
H    0.624207    -1.205751    -0.896877
H    0.624212    -1.205746    0.896888
H    -2.467882    1.159418    1.1e-05
""",
)

entry(
    index = 206,
    label = "C2H3Cl2F + CH2F <=> CH2ClF + C2H3ClF",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(487.731,'cm^3/(mol*s)'), n=2.90704, Ea=(45.368,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.0256, dn = +|- 0.00332084, dEa = +|- 0.0180719 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: CC(F)(Cl)Cl + [CH2]F <=> FCCl + C[C](F)Cl
barrier = 49.947253 kJ/mol
T1 = 0.017840754

Atom XYZ coordinates (angstrom)
Cl    -0.916662    -0.195918    0.085565
Cl    2.013383    -0.878201    -0.511731
F    -3.639367    0.262229    -0.509033
F    1.302352    0.620618    1.407539
C    1.099384    1.692566    -0.678127
C    -2.978212    -0.722667    0.104986
C    1.025854    0.427442    0.112877
H    0.804659    1.500795    -1.705794
H    2.1213    2.073868    -0.654509
H    0.425142    2.422217    -0.233934
H    -2.981362    -1.642639    -0.465757
H    -3.193793    -0.769061    1.164777
""",
)

entry(
    index = 207,
    label = "ClO-3 + C2Cl2F3 <=> C2Cl3F3 + O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8906.58,'cm^3/(mol*s)'), n=1.76738, Ea=(47.3671,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.09783, dn = +|- 0.0122621, dEa = +|- 0.0667299 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: [O]Cl + FC(F)(F)[C](Cl)Cl <=> FC(F)(F)C(Cl)(Cl)Cl + [O]
barrier = 50.697775 kJ/mol

Atom XYZ coordinates (angstrom)
Cl    1.700999    0.055221    -0.366525
Cl    -0.694984    -1.808985    -0.674482
Cl    -0.057876    -0.804424    1.97439
F    -0.583483    1.818163    0.695339
F    -1.056529    1.071978    -1.270255
F    -2.314435    0.570605    0.404212
O    3.018796    1.019265    -1.04885
C    -1.055845    0.778208    0.022469
C    -0.202751    -0.466102    0.28939
""",
)

entry(
    index = 208,
    label = "CBrClF2 + CClF2 <=> CCl2F2 + CBrF2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(44.8911,'cm^3/(mol*s)'), n=3.19144, Ea=(56.5628,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.07553, dn = +|- 0.0095659, dEa = +|- 0.0520573 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: FC(F)(Cl)Br + F[C](F)Cl <=> FC(F)(Cl)Cl + F[C](F)Br
barrier = 58.778284 kJ/mol

Atom XYZ coordinates (angstrom)
Br    -2.474797    0.915689    -0.272811
Cl    0.528027    -0.290578    -0.001301
Cl    3.138305    1.40248    0.065737
F    -1.673518    -1.555944    -0.997518
F    -1.75187    -1.274302    1.126331
F    3.001383    -0.899031    -1.010007
F    2.944648    -0.896439    1.137353
C    -1.481127    -0.697308    -0.022377
C    2.590441    -0.24452    0.052854
""",
)

entry(
    index = 209,
    label = "C2Cl2F4 + CF3 <=> CClF3 + C2ClF4",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(342.596,'cm^3/(mol*s)'), n=3.19295, Ea=(56.9806,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.07498, dn = +|- 0.00949875, dEa = +|- 0.0516918 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: FC(F)(Cl)C(F)(F)Cl + F[C](F)F <=> FC(F)(F)Cl + F[C](F)C(F)(F)Cl
barrier = 59.200487 kJ/mol

Atom XYZ coordinates (angstrom)
Cl    -0.965355    -0.259457    0.054366
Cl    3.54516    0.158709    -0.074969
F    1.1961    -1.592336    -0.929903
F    1.236273    -1.359345    1.220491
F    1.529663    1.345114    0.92169
F    1.489933    1.111783    -1.228549
F    -3.147302    1.448409    0.127377
F    -3.500281    -0.311399    -1.068292
F    -3.533048    -0.445703    1.083752
C    1.001077    -0.763942    0.072181
C    1.814486    0.523214    -0.08252
C    -2.995156    0.149918    0.048641
""",
)

entry(
    index = 210,
    label = "ClO-3 + C2H4ClO-2 <=> C2H4Cl2O + O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(548.19,'cm^3/(mol*s)'), n=2.65512, Ea=(13.3747,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.06186, dn = +|- 0.00788543, dEa = +|- 0.0429122 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: [O]Cl + C[C](O)Cl <=> CC(O)(Cl)Cl + [O]
barrier = 16.968819 kJ/mol
T1 = 0.026707022

Atom XYZ coordinates (angstrom)
Cl    -1.424681    -0.187237    0.119942
Cl    1.524122    -1.013334    -0.279431
O    0.887723    0.992904    1.260934
O    -3.167549    -0.637143    0.088931
C    0.651219    0.477306    0.05128
C    0.683122    1.487581    -1.04508
H    0.358278    1.037382    -1.977808
H    1.702747    1.862638    -1.154541
H    0.021932    2.3104    -0.781816
H    0.898465    0.298238    1.931963
""",
)

entry(
    index = 211,
    label = "C3H6BrCl + CH2F <=> CH2ClF + C3H6Br",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(463.85,'cm^3/(mol*s)'), n=2.94202, Ea=(52.8466,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.02218, dn = +|- 0.00288177, dEa = +|- 0.0156825 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: [CH2]F + CC(C)(Cl)Br <=> FCCl + C[C](C)Br
barrier = 57.440599 kJ/mol

Atom XYZ coordinates (angstrom)
Br    1.730377    -0.68793    0.092983
Cl    -1.426119    -0.181651    0.143413
F    -4.236602    0.099932    0.331563
C    0.416281    0.726816    0.056571
C    0.426577    1.455678    -1.254623
C    0.485877    1.577164    1.290477
C    -3.414227    -0.950474    0.235651
H    1.376259    1.982192    -1.375902
H    -0.384373    2.184478    -1.264261
H    0.297755    0.769114    -2.087799
H    -0.326162    2.304508    1.268941
H    1.438478    2.11167    1.316153
H    0.398398    0.973311    2.190379
H    -3.391039    -1.541103    1.142589
H    -3.508361    -1.463351    -0.713017
""",
)

entry(
    index = 212,
    label = "C2H2Cl4-2 + H <=> ClH-2 + C2H2Cl3-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(1.77982e+08,'cm^3/(mol*s)'), n=1.76709, Ea=(10.499,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.11548, dn = +|- 0.0143582, dEa = +|- 0.0781367 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ClCC(Cl)(Cl)Cl + [H] <=> Cl + ClC[C](Cl)Cl
barrier = 15.281374 kJ/mol
T1 = 0.015074688999999999

Atom XYZ coordinates (angstrom)
Cl    2.441329    0.03685    0.32653
Cl    -1.877601    0.371402    1.008223
Cl    -0.321114    -1.640416    -0.503114
Cl    -0.237365    1.132913    -1.333585
C    0.828978    0.294728    1.025014
C    -0.281797    0.029866    0.028542
H    0.764586    1.327184    1.354343
H    0.712977    -0.381771    1.866121
H    -3.339819    0.711171    1.984366
""",
)

entry(
    index = 213,
    label = "C4H9Cl + H <=> ClH-2 + C4H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.94625e+07,'cm^3/(mol*s)'), n=1.97883, Ea=(27.4378,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.2094, dn = +|- 0.0249787, dEa = +|- 0.135933 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: [H] + CC(C)CCl <=> Cl + [CH2]C(C)C
barrier = 33.575944 kJ/mol
T1 = 0.015712426

Atom XYZ coordinates (angstrom)
Cl    1.886554    0.050789    -0.049199
C    -0.958818    0.077972    -0.305801
C    -1.049889    1.504001    0.223602
C    -2.286474    -0.660588    -0.107827
C    0.129877    -0.708587    0.378034
H    -0.734096    0.10642    -1.374781
H    -1.273816    1.495469    1.292905
H    -1.846358    2.050395    -0.28112
H    -0.115726    2.042911    0.075789
H    -2.246664    -1.673414    -0.508506
H    -2.534904    -0.723049    0.953525
H    -3.093973    -0.126683    -0.609295
H    0.227283    -1.731522    0.028788
H    0.095498    -0.655041    1.463314
H    3.345215    0.721114    -0.418463
""",
)

entry(
    index = 214,
    label = "ClO-3 + C3H6Cl-7 <=> C3H6Cl2 + O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(107105,'cm^3/(mol*s)'), n=1.56368, Ea=(20.9671,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.02665, dn = +|- 0.00345482, dEa = +|- 0.018801 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: [O]Cl + CC[CH]Cl <=> CCC(Cl)Cl + [O]
barrier = 24.606227 kJ/mol

Atom XYZ coordinates (angstrom)
Cl    -1.537204    -0.411525    0.262542
Cl    1.426263    -1.110764    -0.460345
O    -3.26011    -0.246123    -0.078844
C    0.843329    1.3069    0.71245
C    0.693742    1.989134    -0.64037
C    0.576603    -0.163506    0.709207
H    1.861041    1.449935    1.094078
H    0.165979    1.749792    1.444488
H    1.39905    1.58442    -1.363792
H    -0.314263    1.853165    -1.029365
H    0.882593    3.05619    -0.541721
H    0.539528    -0.671033    1.664968
""",
)

entry(
    index = 215,
    label = "ClHO-2 + CClO <=> CCl2O + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(102.465,'cm^3/(mol*s)'), n=3.10435, Ea=(3.67657,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.0233, dn = +|- 0.00302642, dEa = +|- 0.0164696 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: OCl + OD[C]Cl <=> ODC(Cl)Cl + [OH]
barrier = 7.663227 kJ/mol
T1 = 0.025475837999999997

Atom XYZ coordinates (angstrom)
Cl    -1.176125    -0.068859    0.0693
Cl    1.912149    -0.760539    0.037845
O    1.139509    1.75854    -0.077964
O    -2.943233    -0.335688    0.122544
C    0.862459    0.640508    -0.012956
H    -3.297114    0.562419    0.082317
""",
)

entry(
    index = 216,
    label = "ClO-3 + CClO <=> CCl2O + O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(776813,'cm^3/(mol*s)'), n=1.65286, Ea=(37.9191,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.05343, dn = +|- 0.00683791, dEa = +|- 0.0372116 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: [O]Cl + OD[C]Cl <=> ODC(Cl)Cl + [O]
barrier = 41.355622 kJ/mol
T1 = 0.031952397

Atom XYZ coordinates (angstrom)
Cl    1.189549    0.025711    -0.002035
Cl    -1.811285    -0.853522    -0.073499
O    -1.143936    1.677727    0.132652
O    2.875611    -0.424732    0.27771
C    -0.826958    0.571082    0.029209
""",
)

entry(
    index = 217,
    label = "C4H8Cl2-3 + H <=> ClH-2 + C4H8Cl-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.53542e+07,'cm^3/(mol*s)'), n=1.81573, Ea=(12.8846,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.14111, dn = +|- 0.0173427, dEa = +|- 0.0943781 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: [H] + CC(C)(Cl)CCl <=> Cl + C[C](C)CCl
barrier = 18.101580 kJ/mol
T1 = 0.015130415

Atom XYZ coordinates (angstrom)
Cl    -2.11161    -0.398446    0.020375
Cl    2.301384    -0.409703    -0.020948
C    -0.312229    0.386861    0.010315
C    -0.233222    1.213352    -1.248193
C    -0.209477    1.191428    1.28125
C    0.554462    -0.850877    -0.008559
H    -0.384175    0.597565    -2.133589
H    0.75392    1.67633    -1.310322
H    -0.985387    1.999855    -1.233409
H    -0.343757    0.560334    2.158517
H    0.778678    1.653534    1.332795
H    -0.961753    1.977855    1.294276
H    0.377175    -1.441794    -0.901723
H    0.393705    -1.45734    0.877282
H    -3.710049    -1.057745    0.031731
""",
)

entry(
    index = 218,
    label = "CH3Cl-2 + CF3 <=> CClF3 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(29.1371,'cm^3/(mol*s)'), n=3.55919, Ea=(55.3669,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.17656, dn = +|- 0.0213618, dEa = +|- 0.11625 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: CCl + F[C](F)F <=> FC(F)(F)Cl + [CH3]
barrier = 59.358428 kJ/mol
T1 = 0.018343731999999998

Atom XYZ coordinates (angstrom)
Cl    -0.982854    -0.075592    -0.001743
F    1.462855    0.399409    1.167587
F    1.456862    0.767069    -0.956027
F    1.494252    -1.255559    -0.212702
C    -3.054096    -0.115144    -0.003029
C    1.043248    -0.037675    -0.000553
H    -3.30362    0.462377    -0.881868
H    -3.302624    0.350041    0.940351
H    -3.272954    -1.171559    -0.068029
""",
)

entry(
    index = 219,
    label = "C2H2Cl4-3 + H <=> ClH-2 + C2H2Cl3-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.47298e+07,'cm^3/(mol*s)'), n=1.98737, Ea=(21.4492,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.21404, dn = +|- 0.0254819, dEa = +|- 0.138672 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ClCC(Cl)(Cl)Cl + [H] <=> Cl + [CH2]C(Cl)(Cl)Cl
barrier = 27.635182 kJ/mol
T1 = 0.015459279

Atom XYZ coordinates (angstrom)
Cl    -2.269657    0.116426    -0.211086
Cl    2.087012    -0.107959    -1.020283
Cl    0.584075    1.512044    0.853601
Cl    0.465232    -1.381367    1.015149
C    -0.559547    -0.002703    -1.081156
C    0.567247    0.006941    -0.080246
H    -0.586927    -0.939285    -1.626404
H    -0.51258    0.866325    -1.727552
H    -3.721234    0.219221    0.583562
""",
)

entry(
    index = 220,
    label = "CCl2F2 + H <=> ClH-2 + CClF2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.6836e+08,'cm^3/(mol*s)'), n=1.82792, Ea=(23.5253,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.16478, dn = +|- 0.0200399, dEa = +|- 0.109056 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: FC(F)(Cl)Cl + [H] <=> Cl + F[C](F)Cl
barrier = 29.295341 kJ/mol
T1 = 0.017129057

Atom XYZ coordinates (angstrom)
Cl    1.320336    -0.740436    0.002235
Cl    -1.67814    -0.664697    -0.022257
F    -0.211743    1.088112    1.079438
F    -0.19373    1.108226    -1.066122
C    -0.241649    0.331    -0.00086
H    2.840865    -1.534039    0.007625
""",
)

entry(
    index = 221,
    label = "C3H5Cl3-3 + C3H6F <=> C3H6ClF + C3H5Cl2-4",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(20.0857,'cm^3/(mol*s)'), n=3.1208, Ea=(30.7921,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.05731, dn = +|- 0.00732099, dEa = +|- 0.0398406 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: C[C](C)F + CCC(Cl)(Cl)Cl <=> CC(C)(F)Cl + CC[C](Cl)Cl
barrier = 33.891036 kJ/mol

Atom XYZ coordinates (angstrom)
Cl    -0.862315    0.074264    0.112822
Cl    1.695355    -1.579904    -0.081013
Cl    1.687589    1.081548    -1.228274
F    -3.299087    0.623239    1.401851
C    1.571118    0.665395    1.467845
C    3.076181    0.765477    1.689835
C    1.187464    0.087394    0.12955
C    -3.413318    -1.340146    0.11273
C    -3.420352    1.031862    -0.91074
C    -3.038622    0.099075    0.185256
H    1.108933    0.033012    2.226453
H    1.104216    1.648834    1.529949
H    3.538939    1.406263    0.941048
H    3.543681    -0.216586    1.640547
H    3.274235    1.189742    2.672794
H    -3.066696    -1.769088    -0.824646
H    -2.97066    -1.887656    0.942192
H    -4.502317    -1.436886    0.167015
H    -3.073902    0.645912    -1.866682
H    -2.98219    2.013139    -0.740949
H    -4.509933    1.132319    -0.941492
""",
)

entry(
    index = 222,
    label = "C4H7Cl3-2 + H <=> ClH-2 + C4H7Cl2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.09185e+08,'cm^3/(mol*s)'), n=1.80526, Ea=(10.9209,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.13101, dn = +|- 0.0161739, dEa = +|- 0.0880175 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: [H] + CC(C)(Cl)C(Cl)Cl <=> Cl + C[C](C)C(Cl)Cl
barrier = 16.029105 kJ/mol
T1 = 0.014583618000000001

Atom XYZ coordinates (angstrom)
Cl    2.212923    0.219363    -0.34755
Cl    -2.117958    -0.642728    -0.289121
Cl    -0.629549    1.831282    0.050313
C    0.559539    -0.65756    0.196189
C    0.517493    -0.612727    1.702144
C    0.663517    -2.059006    -0.365602
C    -0.522809    0.149811    -0.505901
H    0.576125    0.406922    2.073608
H    -0.417356    -1.060221    2.047477
H    1.348187    -1.187098    2.107281
H    -0.188513    -2.652842    -0.033533
H    1.577277    -2.527008    -0.005511
H    0.681908    -2.050026    -1.45481
H    -0.342957    0.181401    -1.574398
H    3.685565    0.999737    -0.831823
""",
)

entry(
    index = 223,
    label = "ClHO-2 + CH2-2 <=> CH2Cl + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5191.64,'cm^3/(mol*s)'), n=2.99789, Ea=(-4.01602,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.01347, dn = +|- 0.0017573, dEa = +|- 0.00956317 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: OCl + [CH2] <=> [OH] + [CH2]Cl
barrier = 1.124784 kJ/mol
T1 = 0.02241839

Atom XYZ coordinates (angstrom)
Cl    0.086961    -0.015188    -0.096626
O    1.842691    -0.01428    -0.065725
C    -2.164648    0.122753    0.221495
H    -2.51862    -0.890034    0.300069
H    -2.518166    0.977567    -0.327369
H    2.052693    0.875208    0.244029
""",
)

entry(
    index = 224,
    label = "C2HCl3-2 + H <=> ClH-2 + C2HCl2-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3.48816e+10,'cm^3/(mol*s)'), n=0.915521, Ea=(32.3349,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.20696, dn = +|- 0.0247136, dEa = +|- 0.13449 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ClCDC(Cl)Cl + [H] <=> Cl + Cl[C]DCCl
barrier = 37.310596 kJ/mol
T1 = 0.01714546

Atom XYZ coordinates (angstrom)
Cl    -2.597934    0.689175    -0.540295
Cl    -0.121899    1.794093    1.337425
Cl    1.571864    -0.487268    0.319872
C    -1.041176    -0.033254    -0.435147
C    -0.076306    0.436317    0.329595
H    -0.895673    -0.912179    -1.042642
H    2.995837    -1.248318    0.186895
""",
)

entry(
    index = 225,
    label = "ClO-3 + C2H3Cl2-3 <=> C2H3Cl3 + O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(27169,'cm^3/(mol*s)'), n=1.73665, Ea=(32.5895,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.09322, dn = +|- 0.0117101, dEa = +|- 0.0637258 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: C[C](Cl)Cl + [O]Cl <=> CC(Cl)(Cl)Cl + [O]
barrier = 36.017103 kJ/mol
T1 = 0.028688517

Atom XYZ coordinates (angstrom)
Cl    1.208169    1.439556    -0.425798
Cl    1.193198    -1.45526    -0.430315
Cl    -1.479399    0.005739    -0.221138
O    -3.263948    0.012694    -0.113285
C    0.600861    -0.008216    1.797647
C    0.573058    -0.005749    0.301635
H    1.6363    -0.014103    2.141233
H    0.101202    0.883411    2.16971
H    0.091997    -0.89578    2.166933
""",
)

entry(
    index = 226,
    label = "CCl3F + CH3 <=> CH3Cl-2 + CCl2F",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(68627.7,'cm^3/(mol*s)'), n=2.75, Ea=(38.2043,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.07535, dn = +|- 0.00954405, dEa = +|- 0.0519383 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: FC(Cl)(Cl)Cl + [CH3] <=> CCl + F[C](Cl)Cl
barrier = 44.344827 kJ/mol
T1 = 0.017563541999999998

Atom XYZ coordinates (angstrom)
Cl    1.350583    -0.030072    0.117774
Cl    -1.24091    -1.553501    0.636327
Cl    -1.310669    0.730965    -1.164522
F    -0.870871    0.852774    1.323711
C    -0.638115    0.049178    0.2953
C    3.504673    -0.013036    0.056479
H    3.728208    -1.049678    0.260402
H    3.737885    0.689331    0.842691
H    3.682094    0.324751    -0.953794
""",
)

entry(
    index = 227,
    label = "CHClF2 + H <=> ClH-2 + CHF2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.44569e+07,'cm^3/(mol*s)'), n=1.89428, Ea=(34.0612,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.19222, dn = +|- 0.0230989, dEa = +|- 0.125703 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: FC(F)Cl + [H] <=> Cl + F[CH]F
barrier = 40.669308 kJ/mol
T1 = 0.018670472

Atom XYZ coordinates (angstrom)
Cl    -1.177427    0.121155    -0.251072
F    1.28372    1.095199    -0.076379
F    1.196269    -1.061699    -0.186373
C    0.646628    0.016185    0.35172
H    0.618922    -0.037993    1.436265
H    -2.719457    0.214376    -0.864501
""",
)

entry(
    index = 228,
    label = "CCl4 + C2H5-2 <=> C2H5Cl + CCl3-2",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(35918.6,'cm^3/(mol*s)'), n=1.86068, Ea=(15.7996,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.03121, dn = +|- 0.00403747, dEa = +|- 0.0219718 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ClC(Cl)(Cl)Cl + C[CH2] <=> CCCl + Cl[C](Cl)Cl
barrier = 20.773072 kJ/mol
T1 = 0.01611881

Atom XYZ coordinates (angstrom)
Cl    0.87678    0.095384    0.399893
Cl    -1.754071    1.573465    0.641144
Cl    -1.290774    -0.053126    -1.705532
Cl    -1.765132    -1.310866    0.855781
C    3.652903    0.013185    -0.627659
C    -1.091118    0.07515    0.028104
C    3.056483    0.112706    0.732019
H    4.746013    0.015191    -0.556582
H    3.359276    0.856447    -1.250555
H    3.35424    -0.908866    -1.123568
H    3.12525    1.062117    1.245978
H    3.119782    -0.753821    1.376525
""",
)

entry(
    index = 229,
    label = "C2H3ClO-2 + H <=> ClH-2 + C2H3O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.88575e+07,'cm^3/(mol*s)'), n=1.80771, Ea=(26.9997,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.14779, dn = +|- 0.0181094, dEa = +|- 0.0985506 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: [H] + CC(DO)Cl <=> Cl + C[C]DO
barrier = 32.806892 kJ/mol
T1 = 0.022076992

Atom XYZ coordinates (angstrom)
Cl    1.243489    -0.093095    0.374805
O    -1.055136    1.314364    -0.054893
C    -1.394301    -1.085667    0.013419
C    -0.669319    0.218411    0.060371
H    -1.23193    -1.606145    0.955412
H    -0.962584    -1.693353    -0.779657
H    -2.452684    -0.907867    -0.159835
H    2.914739    -0.36618    0.656035
""",
)

entry(
    index = 230,
    label = "ClO-3 + C3H7-4 <=> C3H7Cl-2 + O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1756.62,'cm^3/(mol*s)'), n=2.4222, Ea=(13.549,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.0153, dn = +|- 0.00199532, dEa = +|- 0.0108585 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: [CH2]CC + [O]Cl <=> CCCCl + [O]
barrier = 18.809279 kJ/mol
T1 = 0.026566981

Atom XYZ coordinates (angstrom)
Cl    1.19341    -0.221889    0.053184
O    2.71892    0.599232    -0.218491
C    -1.772097    -0.201855    -0.431865
C    -1.93723    1.166732    0.216055
C    -0.825583    -1.093874    0.292492
H    -1.454967    -0.102929    -1.471643
H    -2.742191    -0.716035    -0.461872
H    -2.272177    1.067014    1.249144
H    -2.671482    1.765005    -0.320298
H    -0.991688    1.707024    0.217291
H    -0.596132    -2.056786    -0.145315
H    -0.851039    -1.081116    1.376006
""",
)

entry(
    index = 231,
    label = "C2H4Cl2 + H <=> ClH-2 + C2H4Cl-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(9.19835e+07,'cm^3/(mol*s)'), n=1.91565, Ea=(22.4696,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.18781, dn = +|- 0.0226118, dEa = +|- 0.123052 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: CC(Cl)Cl + [H] <=> Cl + C[CH]Cl
barrier = 28.600879 kJ/mol
T1 = 0.016980118

Atom XYZ coordinates (angstrom)
Cl    1.627157    -0.218124    -0.074805
Cl    -1.335616    -0.695911    -0.158216
C    -0.284795    1.810026    -0.122817
C    -0.117629    0.427189    0.432285
H    -0.23158    1.787934    -1.209452
H    0.502331    2.456377    0.261573
H    -1.254972    2.208784    0.17552
H    -0.09003    0.364813    1.512737
H    3.208899    -0.701557    -0.499307
""",
)

entry(
    index = 232,
    label = "ClHO-2 + C2H4F-2 <=> C2H4ClF-2 + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(108.085,'cm^3/(mol*s)'), n=2.9324, Ea=(-0.871087,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.03187, dn = +|- 0.00412164, dEa = +|- 0.0224298 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: OCl + [CH2]CF <=> FCCCl + [OH]
barrier = 4.152614 kJ/mol

Atom XYZ coordinates (angstrom)
Cl    -1.057948    0.273885    0.074014
F    1.968733    -1.116227    0.256593
O    -2.602947    -0.580109    -0.271545
C    1.912053    0.119813    -0.351349
C    1.036054    1.032993    0.416063
H    2.933273    0.517933    -0.388807
H    1.552034    -0.014223    -1.37256
H    1.059704    0.949781    1.493706
H    0.879954    2.021401    0.005788
H    -2.402194    -1.479113    0.017936
""",
)

entry(
    index = 233,
    label = "C2H3Cl2F + CH3 <=> CH3Cl-2 + C2H3ClF",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(36814.2,'cm^3/(mol*s)'), n=2.76105, Ea=(50.9567,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.07689, dn = +|- 0.00973286, dEa = +|- 0.0529659 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: [CH3] + CC(F)(Cl)Cl <=> CCl + C[C](F)Cl
barrier = 57.034834 kJ/mol
T1 = 0.017615605

Atom XYZ coordinates (angstrom)
Cl    -1.293856    0.291056    -0.384625
Cl    0.709386    1.858881    -2.094694
F    1.128388    -0.507639    -1.283138
C    1.333812    1.073176    0.446234
C    0.657442    0.656127    -0.819513
C    -3.317817    -0.209998    0.082499
H    1.218991    0.278841    1.181123
H    2.393719    1.241966    0.250242
H    0.881628    1.986869    0.820804
H    -3.243711    -0.531548    1.11114
H    -3.82179    0.731513    -0.080962
H    -3.527908    -0.986651    -0.63824
""",
)

entry(
    index = 234,
    label = "CHClO-2 + H <=> ClH-2 + CHO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.40657e+07,'cm^3/(mol*s)'), n=1.94769, Ea=(32.2937,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.20796, dn = +|- 0.0248225, dEa = +|- 0.135083 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ODCCl + [H] <=> Cl + [CH]DO
barrier = 39.127745 kJ/mol
T1 = 0.024994403

Atom XYZ coordinates (angstrom)
Cl    -0.839971    -0.352227    -0.001977
O    1.905368    -0.26564    0.053573
C    0.94804    0.396109    0.003039
H    0.869269    1.491512    -0.046263
H    -2.389837    -1.002695    -0.00837
""",
)

entry(
    index = 235,
    label = "CCl3F + C2H5-2 <=> C2H5Cl + CCl2F",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(957.392,'cm^3/(mol*s)'), n=2.84493, Ea=(27.8664,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.03472, dn = +|- 0.00448469, dEa = +|- 0.0244055 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: C[CH2] + FC(Cl)(Cl)Cl <=> CCCl + F[C](Cl)Cl
barrier = 32.916576 kJ/mol
T1 = 0.016742518

Atom XYZ coordinates (angstrom)
Cl    0.821633    -0.31263    0.03436
Cl    -1.441141    1.74159    0.19182
Cl    -2.009119    -0.851378    -1.003452
F    -1.467929    -0.461065    1.437554
C    3.581666    0.6831    0.163213
C    -1.149212    0.019588    0.24299
C    2.958268    -0.65185    -0.057345
H    4.672594    0.59511    0.126456
H    3.278832    1.392241    -0.605368
H    3.31298    1.087849    1.137489
H    3.013953    -1.070165    -1.053984
H    3.049651    -1.382138    0.73595
""",
)

entry(
    index = 236,
    label = "CHCl3 + H <=> ClH-2 + CHCl2",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(2.28397e+08,'cm^3/(mol*s)'), n=1.83137, Ea=(18.749,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.14773, dn = +|- 0.0181028, dEa = +|- 0.098515 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ClC(Cl)Cl + [H] <=> Cl + Cl[CH]Cl
barrier = 24.365130 kJ/mol
T1 = 0.017033816

Atom XYZ coordinates (angstrom)
Cl    1.694702    -0.054964    0.168072
Cl    -0.775192    1.593619    -0.08079
Cl    -0.985701    -1.305483    -0.194091
C    -0.167335    0.066965    0.509992
H    -0.249428    0.030856    1.586908
H    3.417057    -0.168091    -0.067533
""",
)

entry(
    index = 237,
    label = "C2H5ClO-2 + H <=> ClH-2 + C2H5O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.43758e+09,'cm^3/(mol*s)'), n=1.62878, Ea=(-0.698534,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.02963, dn = +|- 0.0038365, dEa = +|- 0.0208781 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST ccsd(t)-f12/cc-pvdz-f12//M062X-D3/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: CCOCl + [H] <=> Cl + CC[O]
barrier = 1.960658 kJ/mol
T1 = 0.014966806000000001

Atom XYZ coordinates (angstrom)
Cl    -1.344141    -0.013531    0.18836
O    -0.013741    -0.980151    -0.287716
C    1.703753    0.760741    -0.109092
C    1.186064    -0.579004    0.365934
H    1.014129    1.560508    0.15697
H    1.832804    0.7549    -1.190317
H    2.665903    0.971824    0.35723
H    1.036182    -0.59384    1.447957
H    1.877848    -1.3819    0.10378
H    -2.706474    1.389037    0.676178
""",
)

entry(
    index = 238,
    label = "CH2BrCl + CClF2 <=> CCl2F2 + CH2Br",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.12823,'cm^3/(mol*s)'), n=3.42232, Ea=(62.1671,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.13483, dn = +|- 0.0166171, dEa = +|- 0.0904299 kJ/mol"""),
    rank = 3,
    shortDesc = """AutoTST m062x/jun-cc-pVTZ""",
    longDesc = 
"""
Training reaction from kinetics library: autotst/Cl_Abstraction
Original entry: ClCBr + F[C](F)Cl <=> [CH2]Br + FC(F)(Cl)Cl
barrier = 65.470393 kJ/mol

Atom XYZ coordinates (angstrom)
Br    2.793146    0.874747    -1.280728
Cl    -0.087146    0.409606    0.167582
Cl    -2.611393    -0.653399    -1.308703
F    -2.002122    -1.315988    1.069956
F    -2.717783    0.696639    0.844094
C    -2.01352    -0.262711    0.278405
C    1.849482    1.141467    0.326045
H    2.24985    0.551037    1.13673
H    1.678721    2.188206    0.529933
""",
)

