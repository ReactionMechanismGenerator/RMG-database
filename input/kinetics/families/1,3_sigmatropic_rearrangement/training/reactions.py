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

entry(
    index = 12,
    label = "C3H2BrF3 <=> C3H2BrF3-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5058e+11,'s^-1'), n=0.533491, Ea=(191.066,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.20251, dn = +|- 0.0242278, dEa = +|- 0.131847 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 190.947 kJ/mol

F    1.142374    1.421228    0.222554
Br    0.2998    -1.605588    1.808404
F    1.456428    -0.394382    -0.864311
F    -1.495381    1.139496    0.19698
C    0.623179    0.355554    -0.24947
C    -0.75609    0.170015    -0.333055
C    -1.230603    -1.082411    -0.525959
H    -0.591708    -1.846995    -0.93513
H    -2.272469    -1.300136    -0.341214
""",
)

entry(
    index = 13,
    label = "C3H2F4 <=> C3H2F4-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.11883e+10,'s^-1'), n=0.811585, Ea=(262.426,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.30388, dn = +|- 0.0348607, dEa = +|- 0.18971 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 264.035 kJ/mol

F    -1.409595    -0.339058    0.651867
F    0.031141    1.950039    0.295275
F    -0.713349    0.215038    -1.287548
F    1.050515    -0.733828    1.595137
C    -0.402184    -0.015656    -0.064327
C    0.910623    -0.232565    0.357283
C    1.654059    0.843553    -0.050262
H    1.589195    1.206386    -1.0617
H    2.466716    1.19485    0.571355
""",
)

entry(
    index = 14,
    label = "C3H2ClF3 <=> C3H2ClF3-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.69656e+11,'s^-1'), n=0.593389, Ea=(209.675,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2500,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.22321, dn = +|- 0.0264708, dEa = +|- 0.144053 kJ/mol"""),
    rank = 7,
    shortDesc = """M062X-D3/jun-cc-pVTZ RRHO""",
    longDesc = 
"""
Calculated with Gaussian 16 using M062X with D3 dispersion and jun-cc-pVTZ basis set
barrier = 209.649 kJ/mol

F    1.142199    1.390146    0.27194
Cl    0.26597    -1.535971    1.658129
F    1.459617    -0.40383    -0.845094
F    -1.499556    1.14815    0.173539
C    0.621457    0.342527    -0.234896
C    -0.757234    0.174741    -0.348122
C    -1.218927    -1.089509    -0.498158
H    -0.582957    -1.855179    -0.908855
H    -2.255039    -1.314295    -0.289684
""",
)

