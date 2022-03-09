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
    index = 1,
    label = "C2H4N2O2 <=> C2H4N2O2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.00957e+13,'s^-1'), n=-0.120785, Ea=(192.666,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.17679, dn = +|- 0.0216006, dEa = +|- 0.111384 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: r001085 <=> p001088
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 2,
    label = "C2H3N3 <=> C2H3N3-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(7.84027e+10,'s^-1'), n=1.31782, Ea=(406.92,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.44696, dn = +|- 0.0490241, dEa = +|- 0.252794 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: r001235 <=> p001235
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 3,
    label = "C2H3NO2 <=> C2H3NO2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.90422e+13,'s^-1'), n=-0.320329, Ea=(105.293,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.07354, dn = +|- 0.00941532, dEa = +|- 0.0485503 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: r001958 <=> p001958
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 4,
    label = "C2H2N2O <=> C2H2N2O-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.49787e+11,'s^-1'), n=1.24936, Ea=(321.691,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.43847, dn = +|- 0.0482433, dEa = +|- 0.248768 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: r002774 <=> p002774
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 5,
    label = "C3H4N2 <=> C3H4N2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.07396e+11,'s^-1'), n=1.18751, Ea=(440.095,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.3651, dn = +|- 0.0412969, dEa = +|- 0.212948 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: r004142 <=> p004142
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 6,
    label = "C2H2N2O-3 <=> C2H2N2O-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.23202e+11,'s^-1'), n=0.959257, Ea=(243.463,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.29772, dn = +|- 0.0345798, dEa = +|- 0.178312 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: r004202 <=> p002774
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 7,
    label = "C3H3NO <=> C3H3NO-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.42792e+11,'s^-1'), n=1.12171, Ea=(360.677,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.35846, dn = +|- 0.0406495, dEa = +|- 0.20961 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: r005763 <=> p005763
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 8,
    label = "C4H3N3 <=> C4H3N3-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.04681e+10,'s^-1'), n=1.21369, Ea=(447.107,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.36962, dn = +|- 0.0417358, dEa = +|- 0.215211 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: r007269 <=> p007269
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 9,
    label = "C4H4N2O <=> C4H4N2O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.61854e+10,'s^-1'), n=0.947053, Ea=(380.965,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.24984, dn = +|- 0.0295922, dEa = +|- 0.152593 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: r011506 <=> p011506
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

