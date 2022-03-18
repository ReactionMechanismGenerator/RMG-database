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
Training reaction from kinetics library: 20220318_ketoenol_tmp
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

