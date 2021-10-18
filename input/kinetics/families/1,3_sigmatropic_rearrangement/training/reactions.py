#!/usr/bin/env python
# encoding: utf-8

name = "1,3_sigmatropic_rearrangement/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "C2H4O <=> C2H4O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(100000,'s^-1'), n=2, Ea=(209.2,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 0,
    shortDesc = """A. G. Vandeputte, general rate""",
    longDesc = 
"""
Converted to training reaction from rate rule: R_ROSR;R1_doublebond;R2_doublebond;R_O
""",
)

entry(
    index = 1,
    label = "C4H8O <=> C4H8O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(205000,'s^-1'), n=2.37, Ea=(204.179,'kJ/mol'), T0=(1,'K'), Tmin=(600,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc = """A. G. Vandeputte, CBS-QB3, HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: R_ROR;R1_doublebond_CH2;R2_doublebond_CsC;R_O_H
""",
)

entry(
    index = 2,
    label = "C2H4O <=> C2H4O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7040,'s^-1'), n=2.66, Ea=(204.179,'kJ/mol'), T0=(1,'K'), Tmin=(600,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc = """A. G. Vandeputte, BMK/cbsb7, HO""",
    longDesc = 
"""
Converted to training reaction from rate rule: R_ROR;R1_doublebond_CH2;R2_doublebond_H;R_O_H
""",
)

entry(
    index = 3,
    label = "CH2OS <=> CH2OS-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(52,'s^-1'), n=3.26, Ea=(83.5545,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """calculated by CAC, CCSD(T)/vtz f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: R_ROR;R1_doublebond_S;R2_doublebond_H;R_O_H
""",
)

entry(
    index = 4,
    label = "C2H4OS <=> C2H4OS-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(104,'s^-1'), n=3.21, Ea=(82.0482,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """calculated by CAC, CCSD(T)/vtz f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: R_ROR;R1_doublebond_S;R2_doublebond_CH3;R_O_H
""",
)

entry(
    index = 5,
    label = "C3H6OS <=> C3H6OS-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(87.5,'s^-1'), n=3.23, Ea=(82.0482,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 6,
    shortDesc = """calculated by CAC, CCSD(T)/vtz f12""",
    longDesc = 
"""
Converted to training reaction from rate rule: R_ROR;R1_doublebond_S;R2_doublebond_CH2CH3;R_O_H
""",
)

entry(
    index = 6,
    label = "C3H6O <=> C3H6O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7040,'s^-1'), n=2.66, Ea=(351.456,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 11,
    shortDesc = """W.H. Green estimate
                   A,n from R_ROR;R1_doublebond_CH2;R2_doublebond_H;R_O_H
                   Ea = C-C BDE""",
    longDesc = 
"""
Converted to training reaction from rate rule: R_ROR;R1_doublebond_CH2;R2_doublebond_H;R_O_C
""",
)

entry(
    index = 7,
    label = "C2H4N2O2 <=> C2H4N2O2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.00067e+12,'s^-1'), n=0.391729, Ea=(94.5147,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.18377, dn = +|- 0.0223852, dEa = +|- 0.11543 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Calculated by Kevin Spiekermann
Reaction indices that correspond to the raw QM log files from the kinetics dataset from Spiekermann et al.: r001084 <=> p001084_0
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12/cc-pVDZ-F12
Species have no rotatable bonds and any rings are planar (either aromatic or 3-membered)
""",
)

entry(
    index = 8,
    label = "C2H4N2O2-3 <=> C2H4N2O2-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.07407e-11,'s^-1'), n=6.82872, Ea=(71.4835,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 77.9277, dn = +|- 0.577969, dEa = +|- 2.98031 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Calculated by Kevin Spiekermann
Reaction indices that correspond to the raw QM log files from the kinetics dataset from Spiekermann et al.: r001085 <=> p001085_0
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12/cc-pVDZ-F12
Species have no rotatable bonds and any rings are planar (either aromatic or 3-membered)
""",
)

entry(
    index = 9,
    label = "C2H4N2O2-5 <=> C2H4N2O2-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.20077e-11,'s^-1'), n=7.05311, Ea=(80.7907,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 97.3371, dn = +|- 0.607479, dEa = +|- 3.13248 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Calculated by Kevin Spiekermann
Reaction indices that correspond to the raw QM log files from the kinetics dataset from Spiekermann et al.: r001089 <=> p001089_0
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12/cc-pVDZ-F12
Species have no rotatable bonds and any rings are planar (either aromatic or 3-membered)
""",
)

entry(
    index = 10,
    label = "C2H4N2O2-7 <=> C2H4N2O2-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.21561e-15,'s^-1'), n=8.08717, Ea=(70.5685,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 173.347, dn = +|- 0.684056, dEa = +|- 3.52735 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Calculated by Kevin Spiekermann
Reaction indices that correspond to the raw QM log files from the kinetics dataset from Spiekermann et al.: r001691 <=> p001691_0
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12/cc-pVDZ-F12
Species have no rotatable bonds and any rings are planar (either aromatic or 3-membered)
""",
)

entry(
    index = 11,
    label = "C2H2N2O <=> C2H2N2O-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.47167e+11,'s^-1'), n=1.27308, Ea=(321.43,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.45225, dn = +|- 0.0495084, dEa = +|- 0.255291 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Calculated by Kevin Spiekermann
Reaction indices that correspond to the raw QM log files from the kinetics dataset from Spiekermann et al.: r002774 <=> p002774_0
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12/cc-pVDZ-F12
Species have no rotatable bonds and any rings are planar (either aromatic or 3-membered)
""",
)

entry(
    index = 12,
    label = "C3H3NO <=> C3H3NO-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.48602e-15,'s^-1'), n=8.00071, Ea=(73.8737,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 162.648, dn = +|- 0.675603, dEa = +|- 3.48376 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Calculated by Kevin Spiekermann
Reaction indices that correspond to the raw QM log files from the kinetics dataset from Spiekermann et al.: r003183 <=> p003183_0
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12/cc-pVDZ-F12
Species have no rotatable bonds and any rings are planar (either aromatic or 3-membered)
""",
)

entry(
    index = 13,
    label = "C3H6N2O <=> C3H6N2O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.38421e-12,'s^-1'), n=7.22006, Ea=(74.0025,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 104.123, dn = +|- 0.616422, dEa = +|- 3.17859 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Calculated by Kevin Spiekermann
Reaction indices that correspond to the raw QM log files from the kinetics dataset from Spiekermann et al.: r003454 <=> p003454_0
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12/cc-pVDZ-F12
Species have no rotatable bonds and any rings are planar (either aromatic or 3-membered)
""",
)

entry(
    index = 14,
    label = "C2H5N3O <=> C2H5N3O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.61654e-11,'s^-1'), n=6.78703, Ea=(67.979,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 72.1251, dn = +|- 0.567701, dEa = +|- 2.92736 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Calculated by Kevin Spiekermann
Reaction indices that correspond to the raw QM log files from the kinetics dataset from Spiekermann et al.: r004749 <=> p004749_0
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12/cc-pVDZ-F12
Species have no rotatable bonds and any rings are planar (either aromatic or 3-membered)
""",
)

entry(
    index = 15,
    label = "C2H3NO2 <=> C2H3NO2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.29627e-12,'s^-1'), n=7.28519, Ea=(72.1644,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 108.246, dn = +|- 0.621573, dEa = +|- 3.20516 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Calculated by Kevin Spiekermann
Reaction indices that correspond to the raw QM log files from the kinetics dataset from Spiekermann et al.: r005032 <=> p005032_0
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12/cc-pVDZ-F12
Species have no rotatable bonds and any rings are planar (either aromatic or 3-membered)
""",
)

entry(
    index = 16,
    label = "C2H4N2O2-9 <=> C2H4N2O2-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.24517e-15,'s^-1'), n=8.2595, Ea=(75.0964,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 203.941, dn = +|- 0.705623, dEa = +|- 3.63856 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Calculated by Kevin Spiekermann
Reaction indices that correspond to the raw QM log files from the kinetics dataset from Spiekermann et al.: r005432 <=> p005432_0
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12/cc-pVDZ-F12
Species have no rotatable bonds and any rings are planar (either aromatic or 3-membered)
""",
)

entry(
    index = 17,
    label = "C2H4N2O <=> C2H4N2O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.35011e-13,'s^-1'), n=7.36802, Ea=(73.0838,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 115.182, dn = +|- 0.629815, dEa = +|- 3.24765 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Calculated by Kevin Spiekermann
Reaction indices that correspond to the raw QM log files from the kinetics dataset from Spiekermann et al.: r005588 <=> p005588_0
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12/cc-pVDZ-F12
Species have no rotatable bonds and any rings are planar (either aromatic or 3-membered)
""",
)

entry(
    index = 18,
    label = "CH4N2O <=> CH4N2O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.56778e-11,'s^-1'), n=7.05561, Ea=(68.9016,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 84.7858, dn = +|- 0.589161, dEa = +|- 3.03802 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Calculated by Kevin Spiekermann
Reaction indices that correspond to the raw QM log files from the kinetics dataset from Spiekermann et al.: r005826 <=> p005826_0
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12/cc-pVDZ-F12
Species have no rotatable bonds and any rings are planar (either aromatic or 3-membered)
""",
)

entry(
    index = 19,
    label = "C2H4N2O2-11 <=> C2H4N2O2-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.88124e+11,'s^-1'), n=0.620515, Ea=(129.787,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.21005, dn = +|- 0.0252993, dEa = +|- 0.130456 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Calculated by Kevin Spiekermann
Reaction indices that correspond to the raw QM log files from the kinetics dataset from Spiekermann et al.: r001086 <=> p001086_0
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12/cc-pVDZ-F12
Species have no rotatable bonds and any rings are planar (either aromatic or 3-membered)
""",
)

entry(
    index = 20,
    label = "C2H4N2O2-13 <=> C2H4N2O2-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.93892e+11,'s^-1'), n=0.308436, Ea=(89.6821,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.09084, dn = +|- 0.0115367, dEa = +|- 0.0594892 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Calculated by Kevin Spiekermann
Reaction indices that correspond to the raw QM log files from the kinetics dataset from Spiekermann et al.: r001088 <=> p001088_0
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12/cc-pVDZ-F12
Species have no rotatable bonds and any rings are planar (either aromatic or 3-membered)
""",
)

entry(
    index = 21,
    label = "C2H3NO2-3 <=> C2H3NO2-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.38956e+11,'s^-1'), n=0.419065, Ea=(103.611,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.11238, dn = +|- 0.0141314, dEa = +|- 0.0728687 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Calculated by Kevin Spiekermann
Reaction indices that correspond to the raw QM log files from the kinetics dataset from Spiekermann et al.: r001958 <=> p001958_0
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12/cc-pVDZ-F12
Species have no rotatable bonds and any rings are planar (either aromatic or 3-membered)
""",
)

entry(
    index = 22,
    label = "C2H2N2O-3 <=> C2H2N2O-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.0435e+11,'s^-1'), n=1.01704, Ea=(242.812,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.32691, dn = +|- 0.0375319, dEa = +|- 0.193534 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Calculated by Kevin Spiekermann
Reaction indices that correspond to the raw QM log files from the kinetics dataset from Spiekermann et al.: r004202 <=> p004202_0
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12/cc-pVDZ-F12
Species have no rotatable bonds and any rings are planar (either aromatic or 3-membered)
""",
)

entry(
    index = 23,
    label = "C2H3NO2-3 <=> C2H3NO2-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.65585e+11,'s^-1'), n=0.379761, Ea=(99.6869,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.1015, dn = +|- 0.0128273, dEa = +|- 0.0661441 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Calculated by Kevin Spiekermann
Reaction indices that correspond to the raw QM log files from the kinetics dataset from Spiekermann et al.: r005036 <=> p005036_0
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12/cc-pVDZ-F12
Species have no rotatable bonds and any rings are planar (either aromatic or 3-membered)
""",
)

entry(
    index = 24,
    label = "C2H4N2O-3 <=> C2H4N2O-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(9.71203e+09,'s^-1'), n=0.739985, Ea=(158.599,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.21759, dn = +|- 0.0261233, dEa = +|- 0.134705 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Calculated by Kevin Spiekermann
Reaction indices that correspond to the raw QM log files from the kinetics dataset from Spiekermann et al.: r005593 <=> p005593_0
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12/cc-pVDZ-F12
Species have no rotatable bonds and any rings are planar (either aromatic or 3-membered)
""",
)

entry(
    index = 25,
    label = "C3H3NO-3 <=> C3H3NO-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6259e+11,'s^-1'), n=1.19107, Ea=(359.894,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.39462, dn = +|- 0.0441353, dEa = +|- 0.227585 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Calculated by Kevin Spiekermann
Reaction indices that correspond to the raw QM log files from the kinetics dataset from Spiekermann et al.: r005763 <=> p005763_0
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12/cc-pVDZ-F12
Species have no rotatable bonds and any rings are planar (either aromatic or 3-membered)
""",
)

entry(
    index = 26,
    label = "C4H4N2O <=> C4H4N2O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.1761e+10,'s^-1'), n=0.996245, Ea=(380.451,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.27748, dn = +|- 0.0324947, dEa = +|- 0.16756 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Calculated by Kevin Spiekermann
Reaction indices that correspond to the raw QM log files from the kinetics dataset from Spiekermann et al.: r011506 <=> p011506_0
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12/cc-pVDZ-F12
Species have no rotatable bonds and any rings are planar (either aromatic or 3-membered)
""",
)

