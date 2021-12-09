#!/usr/bin/env python
# encoding: utf-8

name = "Ketoenol/training"
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
    label = "C2H4N2O2 <=> C2H4N2O2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.00037e+12,'s^-1'), n=0.391734, Ea=(94.5149,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.18377, dn = +|- 0.0223855, dEa = +|- 0.115431 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p001084 <=> r001084
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
Systematic conformer search was done with ACS
""",
)

entry(
    index = 7,
    label = "C2H4N2O2-3 <=> C2H4N2O2-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.26244e-13,'s^-1'), n=7.34559, Ea=(70.152,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 109.399, dn = +|- 0.62298, dEa = +|- 3.21241 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p001085 <=> r001084
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
Systematic conformer search was done with ACS
""",
)

entry(
    index = 8,
    label = "C2H4N2O2-5 <=> C2H4N2O2-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.63498e-12,'s^-1'), n=7.20509, Ea=(79.6963,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 110.489, dn = +|- 0.624295, dEa = +|- 3.21919 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p001089 <=> r001084
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
Systematic conformer search was done with ACS
""",
)

entry(
    index = 9,
    label = "C2H4N2O2-7 <=> C2H4N2O2-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.40253e-13,'s^-1'), n=7.701, Ea=(72.7924,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 138.963, dn = +|- 0.65472, dEa = +|- 3.37608 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p001691 <=> r001691
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
Systematic conformer search was done with ACS
""",
)

entry(
    index = 10,
    label = "C3H3NO <=> C3H3NO-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.48602e-15,'s^-1'), n=8.00071, Ea=(73.8737,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 162.648, dn = +|- 0.675603, dEa = +|- 3.48376 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p003183 <=> r003183
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
Systematic conformer search was done with ACS
""",
)

entry(
    index = 11,
    label = "C3H6N2O <=> C3H6N2O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.47903e-12,'s^-1'), n=7.22226, Ea=(73.9821,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 103.905, dn = +|- 0.616142, dEa = +|- 3.17715 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p003454 <=> r003454
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
Systematic conformer search was done with ACS
""",
)

entry(
    index = 12,
    label = "C2H5N3O <=> C2H5N3O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.70268e-12,'s^-1'), n=7.27027, Ea=(68.0463,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 100.019, dn = +|- 0.611086, dEa = +|- 3.15108 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p004749 <=> r004749
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
Systematic conformer search was done with ACS
""",
)

entry(
    index = 13,
    label = "C2H3NO2 <=> C2H3NO2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.18181e-12,'s^-1'), n=7.01339, Ea=(72.1949,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 88.831, dn = +|- 0.595345, dEa = +|- 3.06991 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p005032 <=> r005032
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
Systematic conformer search was done with ACS
""",
)

entry(
    index = 14,
    label = "C2H4N2O2-9 <=> C2H4N2O2-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.24517e-15,'s^-1'), n=8.2595, Ea=(75.0964,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 203.941, dn = +|- 0.705623, dEa = +|- 3.63856 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p005432 <=> r005432
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
Systematic conformer search was done with ACS
""",
)

entry(
    index = 15,
    label = "C2H4N2O <=> C2H4N2O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.13103e-12,'s^-1'), n=7.21352, Ea=(75.026,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 104.624, dn = +|- 0.617057, dEa = +|- 3.18187 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p005588 <=> r005588
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
Systematic conformer search was done with ACS
""",
)

entry(
    index = 16,
    label = "CH4N2O <=> CH4N2O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.67535e-10,'s^-1'), n=6.6431, Ea=(72.3053,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 68.373, dn = +|- 0.560612, dEa = +|- 2.89081 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p005826 <=> r005826
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
Systematic conformer search was done with ACS
""",
)

