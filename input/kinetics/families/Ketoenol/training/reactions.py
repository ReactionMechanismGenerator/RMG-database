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
    kinetics = Arrhenius(A=(5.58698e-10,'s^-1'), n=6.27942, Ea=(73.9697,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 105.212, dn = +|- 0.617802, dEa = +|- 3.18571 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p001085 <=> r001085
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 7,
    label = "C2H4N2O2-3 <=> C2H4N2O2-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.24893e-09,'s^-1'), n=6.18216, Ea=(82.1219,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 110.839, dn = +|- 0.624715, dEa = +|- 3.22135 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p001089 <=> r001085
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 8,
    label = "C3H3NO <=> C3H3NO-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.02789e-13,'s^-1'), n=7.48219, Ea=(75.5303,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 172.661, dn = +|- 0.68353, dEa = +|- 3.52464 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p003183 <=> r003183
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 9,
    label = "C3H6N2O <=> C3H6N2O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.68509e-11,'s^-1'), n=6.88807, Ea=(73.4794,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 117.433, dn = +|- 0.632383, dEa = +|- 3.26089 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p003454 <=> r003454
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 10,
    label = "C2H5N3O <=> C2H5N3O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.95577e-10,'s^-1'), n=6.41822, Ea=(70.956,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 97.9173, dn = +|- 0.608267, dEa = +|- 3.13654 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p004749 <=> r004749
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 11,
    label = "C2H3NO2 <=> C2H3NO2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.36022e-11,'s^-1'), n=6.62861, Ea=(72.851,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 88.4737, dn = +|- 0.59481, dEa = +|- 3.06715 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p005032 <=> p001958
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 12,
    label = "C2H4N2O2-5 <=> C2H4N2O2-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.30511e-12,'s^-1'), n=7.26372, Ea=(77.7584,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 210.811, dn = +|- 0.710019, dEa = +|- 3.66123 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p005432 <=> r005432
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 13,
    label = "C2H4N2O <=> C2H4N2O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.10725e-11,'s^-1'), n=6.76455, Ea=(75.3833,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 107.635, dn = +|- 0.620823, dEa = +|- 3.20129 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p005588 <=> r005588
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 14,
    label = "CH4N2O <=> CH4N2O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.08033e-09,'s^-1'), n=6.26751, Ea=(72.9112,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 71.0635, dn = +|- 0.565734, dEa = +|- 2.91722 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p005826 <=> r005826
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 15,
    label = "C2H3N3O <=> C2H3N3O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.50659e-18,'s^-1'), n=8.75863, Ea=(114.547,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 530.44, dn = +|- 0.832458, dEa = +|- 4.29259 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: r000017 <=> p000017
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 16,
    label = "C3H3NO2 <=> C3H3NO2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.95366e-14,'s^-1'), n=7.77475, Ea=(152.142,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 337.834, dn = +|- 0.772595, dEa = +|- 3.9839 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: r000314 <=> p000314
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 17,
    label = "C2H3N3O-3 <=> C2H3N3O-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.52338e-22,'s^-1'), n=10.05, Ea=(150.418,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 865.769, dn = +|- 0.897465, dEa = +|- 4.6278 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: r000399 <=> p000401
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 18,
    label = "C3H7NO <=> C3H7NO-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.27692e-54,'s^-1'), n=19.1913, Ea=(180.189,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 21678.5, dn = +|- 1.32479, dEa = +|- 6.83129 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: r000842 <=> p000842
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 19,
    label = "CHN3O2 <=> CHN3O2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.02819e-14,'s^-1'), n=7.71417, Ea=(180.621,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 199.221, dn = +|- 0.702516, dEa = +|- 3.62254 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: r002513 <=> p002513
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 20,
    label = "CH2N4O <=> CH2N4O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.03103e-17,'s^-1'), n=8.43292, Ea=(153.029,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 354.367, dn = +|- 0.778935, dEa = +|- 4.01659 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: r004006 <=> p004006
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 21,
    label = "CH2N4O-3 <=> CH2N4O-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.58562e-24,'s^-1'), n=10.6226, Ea=(173.215,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1192.35, dn = +|- 0.939933, dEa = +|- 4.84679 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: r004006 <=> p004007
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 22,
    label = "C3H4N2O <=> C3H4N2O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.02325e-17,'s^-1'), n=8.65259, Ea=(104.52,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 465.629, dn = +|- 0.815167, dEa = +|- 4.20342 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: r004295 <=> p004295
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 23,
    label = "C2H2N2O2 <=> C2H2N2O2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.62343e-20,'s^-1'), n=9.5285, Ea=(156.362,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 787.027, dn = +|- 0.884812, dEa = +|- 4.56255 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: r004717 <=> p004717
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 24,
    label = "C2H2N2O2-3 <=> C2H2N2O2-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.87223e-13,'s^-1'), n=7.30388, Ea=(159.322,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 138.752, dn = +|- 0.654518, dEa = +|- 3.37504 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: r004717 <=> p004719
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 25,
    label = "C2H3N3O-5 <=> C2H3N3O-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.18952e-19,'s^-1'), n=9.32392, Ea=(161.52,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 641.618, dn = +|- 0.857707, dEa = +|- 4.42279 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: r005102 <=> p005102
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 26,
    label = "C3H4N2O-3 <=> C3H4N2O-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.23784e-18,'s^-1'), n=8.74837, Ea=(143.184,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 474.17, dn = +|- 0.817578, dEa = +|- 4.21586 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: r005546 <=> p005546
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 27,
    label = "C3H3N3O <=> C3H3N3O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.03729e-10,'s^-1'), n=6.68631, Ea=(102.806,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 132.44, dn = +|- 0.64834, dEa = +|- 3.34318 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: r007945 <=> p007945
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 28,
    label = "C4H6N2O <=> C4H6N2O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.57404e-19,'s^-1'), n=9.1193, Ea=(135.561,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 579.205, dn = +|- 0.844128, dEa = +|- 4.35277 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: r008828 <=> p008828
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 29,
    label = "C4H5NO2 <=> C4H5NO2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.23245e-20,'s^-1'), n=9.38178, Ea=(107.208,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 667.354, dn = +|- 0.862926, dEa = +|- 4.4497 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: r009513 <=> p009513
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 30,
    label = "C4H6N2O-3 <=> C4H6N2O-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.14825e-17,'s^-1'), n=8.45574, Ea=(104.82,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 419.583, dn = +|- 0.80135, dEa = +|- 4.13218 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: r010419 <=> p010419
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 31,
    label = "C2H4N4O <=> C2H4N4O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.00746e-18,'s^-1'), n=8.75254, Ea=(115.264,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 546.354, dn = +|- 0.836381, dEa = +|- 4.31281 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: r011443 <=> p011443
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 32,
    label = "C3H5N3O <=> C3H5N3O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.10787e-17,'s^-1'), n=8.57309, Ea=(108.743,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 474.691, dn = +|- 0.817724, dEa = +|- 4.21661 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: r011937 <=> p011937
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 33,
    label = "C3H6N2O-3 <=> C3H6N2O-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.2546e-11,'s^-1'), n=6.85152, Ea=(77.9947,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 107.804, dn = +|- 0.621031, dEa = +|- 3.20236 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p000049 <=> r000049
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 34,
    label = "C3H4O2 <=> C3H4O2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.69794e-26,'s^-1'), n=10.9363, Ea=(125.211,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1447.77, dn = +|- 0.965688, dEa = +|- 4.97959 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p000208 <=> r000208
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 35,
    label = "C4H5NO <=> C4H5NO-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.03652e-10,'s^-1'), n=6.72069, Ea=(82.5831,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 138.327, dn = +|- 0.654111, dEa = +|- 3.37294 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p000634 <=> r000634
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 36,
    label = "C5H6O <=> C5H6O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.42334e-31,'s^-1'), n=12.8324, Ea=(120.373,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 3626.22, dn = +|- 1.08752, dEa = +|- 5.60782 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p000721 <=> r000721
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 37,
    label = "C5H6O-3 <=> C5H6O-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.34803e-38,'s^-1'), n=14.7488, Ea=(110.291,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 7501.31, dn = +|- 1.18397, dEa = +|- 6.10517 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p000726 <=> r000721
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 38,
    label = "C4H5NO-3 <=> C4H5NO-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.84947e-45,'s^-1'), n=16.5411, Ea=(129.059,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 13981.8, dn = +|- 1.26659, dEa = +|- 6.53122 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p000744 <=> r000744
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 39,
    label = "C3H7NO2 <=> C3H7NO2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.80609e-12,'s^-1'), n=7.13985, Ea=(64.5475,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 98.3219, dn = +|- 0.608814, dEa = +|- 3.13937 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p000813 <=> r000813
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 40,
    label = "C4H6O2 <=> C4H6O2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.66974e-32,'s^-1'), n=12.7337, Ea=(112.625,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 3067.51, dn = +|- 1.06532, dEa = +|- 5.49333 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p001050 <=> r001050
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 41,
    label = "C4H8O-3 <=> C4H8O-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.22009e-49,'s^-1'), n=17.8112, Ea=(124.163,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 16475.9, dn = +|- 1.28837, dEa = +|- 6.64353 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p001147 <=> r001147
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 42,
    label = "C2H3NO2-3 <=> C2H3NO2-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.03997e-16,'s^-1'), n=8.33012, Ea=(78.2703,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 324.839, dn = +|- 0.76739, dEa = +|- 3.95706 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p001169 <=> r001169
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 43,
    label = "C4H9NO <=> C4H9NO-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.06473e-10,'s^-1'), n=6.60955, Ea=(80.838,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 135.547, dn = +|- 0.651418, dEa = +|- 3.35905 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p001357 <=> r001357
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 44,
    label = "C5H8O <=> C5H8O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.41171e-33,'s^-1'), n=13.3174, Ea=(105.78,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 3720.31, dn = +|- 1.09092, dEa = +|- 5.62535 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p001387 <=> r001387
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 45,
    label = "C5H8O-3 <=> C5H8O-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.84389e-11,'s^-1'), n=6.70227, Ea=(141.395,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 198.059, dn = +|- 0.70174, dEa = +|- 3.61854 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p001388 <=> r001387
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 46,
    label = "C3H5NO2 <=> C3H5NO2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.42686e-33,'s^-1'), n=13.1831, Ea=(126.309,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 3814.42, dn = +|- 1.09423, dEa = +|- 5.64244 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p001614 <=> r001614
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 47,
    label = "C3H5NO2-3 <=> C3H5NO2-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.51726e-18,'s^-1'), n=8.84109, Ea=(138.906,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 333.788, dn = +|- 0.770996, dEa = +|- 3.97566 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p001615 <=> r001614
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 48,
    label = "C3H5NO2-5 <=> C3H5NO2-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.40998e-13,'s^-1'), n=7.50448, Ea=(76.2627,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 184.62, dn = +|- 0.692416, dEa = +|- 3.57046 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p001627 <=> r001627
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 49,
    label = "C4H7NO <=> C4H7NO-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.65781e-21,'s^-1'), n=9.63784, Ea=(120.135,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 817.928, dn = +|- 0.889922, dEa = +|- 4.5889 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p002203 <=> r002203
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 50,
    label = "C4H7NO-3 <=> C4H7NO-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.59344e-34,'s^-1'), n=13.552, Ea=(109.766,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 4513.65, dn = +|- 1.11657, dEa = +|- 5.75761 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p002204 <=> r002203
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 51,
    label = "C4H7NO-5 <=> C4H7NO-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.03926e-10,'s^-1'), n=6.64444, Ea=(82.2627,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 148.108, dn = +|- 0.663176, dEa = +|- 3.41968 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p002312 <=> r002312
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 52,
    label = "C2H5NO2 <=> C2H5NO2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.51923e-11,'s^-1'), n=6.9247, Ea=(66.5174,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 99.4801, dn = +|- 0.610368, dEa = +|- 3.14738 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p002594 <=> r002594
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 53,
    label = "C4H6O <=> C4H6O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.16654e-24,'s^-1'), n=10.6408, Ea=(128.297,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1671.79, dn = +|- 0.984779, dEa = +|- 5.07803 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p002675 <=> r002675
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 54,
    label = "C4H5NO-5 <=> C4H5NO-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.12859e-53,'s^-1'), n=18.9999, Ea=(126.793,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 19011.4, dn = +|- 1.30737, dEa = +|- 6.74147 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p002689 <=> r002689
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 55,
    label = "C3H4O2-3 <=> C3H4O2-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.07484e-44,'s^-1'), n=16.5795, Ea=(142.735,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 21235.6, dn = +|- 1.32205, dEa = +|- 6.81717 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p002760 <=> r002760
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 56,
    label = "C4H6O2-3 <=> C4H6O2-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.47848e-14,'s^-1'), n=7.46671, Ea=(127.454,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 187.906, dn = +|- 0.694757, dEa = +|- 3.58253 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p002801 <=> r002801
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 57,
    label = "C4H4O <=> C4H4O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.92778e-40,'s^-1'), n=15.2017, Ea=(113.63,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 8229.85, dn = +|- 1.19627, dEa = +|- 6.16859 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p002874 <=> r002874
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 58,
    label = "C4H6O2-5 <=> C4H6O2-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.57345e-42,'s^-1'), n=16.0376, Ea=(138.173,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 20557.6, dn = +|- 1.31774, dEa = +|- 6.79497 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p002881 <=> r002881
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 59,
    label = "C3H4N2O-5 <=> C3H4N2O-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.3825e-13,'s^-1'), n=7.5932, Ea=(75.6216,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 171.089, dn = +|- 0.682317, dEa = +|- 3.51838 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p003070 <=> r003070
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 60,
    label = "C3H4O3 <=> C3H4O3-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.80714e-28,'s^-1'), n=11.6116, Ea=(140.422,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1748.44, dn = +|- 0.990727, dEa = +|- 5.10871 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p003195 <=> r003195
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 61,
    label = "C3H3NO-3 <=> C3H3NO-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.93747e-32,'s^-1'), n=12.864, Ea=(134.379,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 3910.61, dn = +|- 1.09754, dEa = +|- 5.65948 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p003323 <=> r003323
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 62,
    label = "C2H6N2O <=> C2H6N2O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.757e-07,'s^-1'), n=6.00798, Ea=(69.774,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 63.7085, dn = +|- 0.551237, dEa = +|- 2.84246 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p003344 <=> r003344
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 63,
    label = "C2H6N2O-3 <=> C2H6N2O-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.33821e-07,'s^-1'), n=5.68082, Ea=(75.8132,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 64.0288, dn = +|- 0.551902, dEa = +|- 2.84589 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p003346 <=> r003344
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 64,
    label = "C2H4O <=> C2H4O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.20593e-38,'s^-1'), n=14.7335, Ea=(119.026,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 7706.9, dn = +|- 1.18756, dEa = +|- 6.12367 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p003348 <=> r003348
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 65,
    label = "C3H5NO2-7 <=> C3H5NO2-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.81779e-10,'s^-1'), n=6.57871, Ea=(74.9502,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 79.2848, dn = +|- 0.58026, dEa = +|- 2.99212 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p003431 <=> r003431
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 66,
    label = "C4H7NO-7 <=> C4H7NO-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.32223e-12,'s^-1'), n=7.33725, Ea=(69.6232,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 115.77, dn = +|- 0.63049, dEa = +|- 3.25114 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p003437 <=> r003437
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 67,
    label = "C4H7NO-9 <=> C4H7NO-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.0332916,'s^-1'), n=3.98637, Ea=(105.771,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 12.7338, dn = +|- 0.337598, dEa = +|- 1.74083 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p003440 <=> r003437
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 68,
    label = "C5H6O-5 <=> C5H6O-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.06626e-37,'s^-1'), n=14.5413, Ea=(112.927,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 6576.73, dn = +|- 1.16652, dEa = +|- 6.01517 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p003718 <=> r003718
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 69,
    label = "C3H4N2O-7 <=> C3H4N2O-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.42858e-10,'s^-1'), n=6.4885, Ea=(88.6777,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 126.543, dn = +|- 0.642297, dEa = +|- 3.31202 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p003937 <=> r003937
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 70,
    label = "C4H9NO-3 <=> C4H9NO-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.48783e-11,'s^-1'), n=6.87686, Ea=(77.6406,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 144.417, dn = +|- 0.659829, dEa = +|- 3.40242 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p003958 <=> r003958
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 71,
    label = "C5H6O-7 <=> C5H6O-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.49793e-42,'s^-1'), n=15.9135, Ea=(134.508,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 10202, dn = +|- 1.22477, dEa = +|- 6.31557 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p004414 <=> r004414
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 72,
    label = "C5H6O-9 <=> C5H6O-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.00696e-46,'s^-1'), n=17.0834, Ea=(126.242,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 15132.4, dn = +|- 1.27709, dEa = +|- 6.58533 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p004467 <=> r004467
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 73,
    label = "C4H5NO-7 <=> C4H5NO-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.97955e-36,'s^-1'), n=14.0901, Ea=(149.791,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 6721.17, dn = +|- 1.1694, dEa = +|- 6.03003 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p004505 <=> r004505
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 74,
    label = "C4H7NO-11 <=> C4H7NO-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.56099e-43,'s^-1'), n=15.9484, Ea=(111.981,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 8672.61, dn = +|- 1.20322, dEa = +|- 6.20445 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p004547 <=> r004547
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 75,
    label = "C2H3N3O-7 <=> C2H3N3O-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.15125e-17,'s^-1'), n=8.71952, Ea=(109.961,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 548.261, dn = +|- 0.836843, dEa = +|- 4.3152 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p004625 <=> p000017
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 76,
    label = "C3H3NO-5 <=> C3H3NO-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.74964e-45,'s^-1'), n=16.6685, Ea=(116.975,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 11919.2, dn = +|- 1.24542, dEa = +|- 6.42201 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p004643 <=> r004643
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 77,
    label = "C3H7NO-3 <=> C3H7NO-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.92786e-16,'s^-1'), n=8.20829, Ea=(93.7874,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 339.338, dn = +|- 0.773184, dEa = +|- 3.98694 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p004778 <=> r004778
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 78,
    label = "C4H9NO-5 <=> C4H9NO-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.5544e-16,'s^-1'), n=8.25988, Ea=(88.0644,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 253.098, dn = +|- 0.734277, dEa = +|- 3.78631 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p004794 <=> r004794
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 79,
    label = "C4H6O2-7 <=> C4H6O2-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.04433e-53,'s^-1'), n=19.1929, Ea=(152.81,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 34234.4, dn = +|- 1.38541, dEa = +|- 7.14392 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p004852 <=> r004852
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 80,
    label = "C3H7NO2-3 <=> C3H7NO2-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.85036e-08,'s^-1'), n=5.86332, Ea=(65.6947,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 52.4027, dn = +|- 0.525314, dEa = +|- 2.70879 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p005118 <=> r005118
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 81,
    label = "C2H2N2O2-5 <=> C2H2N2O2-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.9201e-20,'s^-1'), n=9.47072, Ea=(116.615,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 723.084, dn = +|- 0.873568, dEa = +|- 4.50457 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p005148 <=> r005148
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 82,
    label = "C3H6O <=> C3H6O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.12867e-34,'s^-1'), n=13.5809, Ea=(114.48,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 4959.64, dn = +|- 1.12907, dEa = +|- 5.82208 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p005196 <=> r005196
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 83,
    label = "C3H8N2O <=> C3H8N2O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.39095e-06,'s^-1'), n=5.24031, Ea=(67.2473,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 46.2739, dn = +|- 0.50881, dEa = +|- 2.62369 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p005308 <=> r005308
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 84,
    label = "C4H6O2-9 <=> C4H6O2-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.55896e-23,'s^-1'), n=10.1131, Ea=(126.084,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1260.86, dn = +|- 0.947347, dEa = +|- 4.88502 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p005356 <=> r005356
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 85,
    label = "C3H5NO <=> C3H5NO-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.8149e-27,'s^-1'), n=11.304, Ea=(126.826,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1929.78, dn = +|- 1.00382, dEa = +|- 5.17623 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p005491 <=> r005491
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 86,
    label = "C4H7NO-13 <=> C4H7NO-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.49665e-24,'s^-1'), n=10.5562, Ea=(120.825,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1215.89, dn = +|- 0.942528, dEa = +|- 4.86017 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p005998 <=> r005998
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 87,
    label = "C4H7NO-15 <=> C4H7NO-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.33301e-26,'s^-1'), n=11.129, Ea=(116.406,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1558.75, dn = +|- 0.975489, dEa = +|- 5.03013 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p006089 <=> r006089
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 88,
    label = "C5H8O-5 <=> C5H8O-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.38708e-30,'s^-1'), n=12.1418, Ea=(114.989,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 2972.53, dn = +|- 1.06114, dEa = +|- 5.47181 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p006263 <=> r006263
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 89,
    label = "C3H3NO2-3 <=> C3H3NO2-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.83088e-20,'s^-1'), n=9.42661, Ea=(108.576,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 712.966, dn = +|- 0.871698, dEa = +|- 4.49493 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p006320 <=> r006320
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 90,
    label = "C4H8O3 <=> C4H8O3-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.76964e-27,'s^-1'), n=11.3857, Ea=(99.7486,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 2247.38, dn = +|- 1.02404, dEa = +|- 5.28047 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p006396 <=> r006396
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 91,
    label = "C4H5NO2-3 <=> C4H5NO2-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.77862e-15,'s^-1'), n=8.01018, Ea=(145.434,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 308.012, dn = +|- 0.760332, dEa = +|- 3.92067 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p006798 <=> r006798
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 92,
    label = "C3H5N3O-3 <=> C3H5N3O-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.18792e-17,'s^-1'), n=8.63308, Ea=(112.872,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 509.177, dn = +|- 0.82703, dEa = +|- 4.2646 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p007773 <=> r007773
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 93,
    label = "C3H5N3O-5 <=> C3H5N3O-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.19581e-17,'s^-1'), n=8.72753, Ea=(108.255,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 535.86, dn = +|- 0.833807, dEa = +|- 4.29955 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p007777 <=> r007773
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 94,
    label = "C6H8O <=> C6H8O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.63468e-47,'s^-1'), n=17.3183, Ea=(128.068,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 13506, dn = +|- 1.262, dEa = +|- 6.50753 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p009289 <=> r009289
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 95,
    label = "C5H3NO <=> C5H3NO-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.00799e-42,'s^-1'), n=15.8601, Ea=(125.554,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 10206.4, dn = +|- 1.22483, dEa = +|- 6.31587 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p009379 <=> r009379
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 96,
    label = "C5H6O2 <=> C5H6O2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.21191e-35,'s^-1'), n=13.8299, Ea=(127.361,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 5392.23, dn = +|- 1.14017, dEa = +|- 5.8793 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p009772 <=> r009772
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 97,
    label = "C4H4O3 <=> C4H4O3-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.10569e-41,'s^-1'), n=15.9357, Ea=(145.27,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 17910.8, dn = +|- 1.29945, dEa = +|- 6.70066 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p009945 <=> r009945
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 98,
    label = "C4H8N2O <=> C4H8N2O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.83728e-12,'s^-1'), n=7.25327, Ea=(73.9748,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 146.099, dn = +|- 0.661365, dEa = +|- 3.41034 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p010345 <=> r010345
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 99,
    label = "C4H7NO2 <=> C4H7NO2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.42405e-12,'s^-1'), n=7.19519, Ea=(76.6476,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 150.32, dn = +|- 0.665144, dEa = +|- 3.42983 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p010564 <=> r010564
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 100,
    label = "C2H3N3O2 <=> C2H3N3O2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.43945e-20,'s^-1'), n=9.41864, Ea=(117.984,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 692.603, dn = +|- 0.867853, dEa = +|- 4.4751 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p011399 <=> r011399
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

