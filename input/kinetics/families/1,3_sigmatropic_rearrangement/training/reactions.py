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
    kinetics = Arrhenius(A=(1.88231e+11,'s^-1'), n=0.661449, Ea=(208.054,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.1914, dn = +|- 0.0232376, dEa = +|- 0.119825 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: r001084 <=> p001086
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
Systematic conformer search was done with ACS
""",
)

entry(
    index = 2,
    label = "C2H4N2O2-3 <=> C2H4N2O2-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.57015e+11,'s^-1'), n=0.576299, Ea=(192.369,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.15438, dn = +|- 0.0190497, dEa = +|- 0.0982302 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: r001084 <=> p001088
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
Systematic conformer search was done with ACS
""",
)

entry(
    index = 3,
    label = "C2H3N3 <=> C2H3N3-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.23088e+11,'s^-1'), n=1.34775, Ea=(406.598,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.46535, dn = +|- 0.0507003, dEa = +|- 0.261437 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: r001235 <=> p001235
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
Systematic conformer search was done with ACS
""",
)

entry(
    index = 4,
    label = "C2H3NO2 <=> C2H3NO2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.38947e+11,'s^-1'), n=0.419069, Ea=(103.611,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.11238, dn = +|- 0.0141317, dEa = +|- 0.0728703 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: r001958 <=> p001958
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
Systematic conformer search was done with ACS
""",
)

entry(
    index = 5,
    label = "C2H2N2O <=> C2H2N2O-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.47172e+11,'s^-1'), n=1.27308, Ea=(321.43,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.45225, dn = +|- 0.0495083, dEa = +|- 0.25529 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: r002774 <=> p002774
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
Systematic conformer search was done with ACS
""",
)

entry(
    index = 6,
    label = "C3H4N2 <=> C3H4N2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.47516e+11,'s^-1'), n=1.23379, Ea=(439.575,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.38946, dn = +|- 0.0436439, dEa = +|- 0.225051 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: r004142 <=> p004142
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
Systematic conformer search was done with ACS
""",
)

entry(
    index = 7,
    label = "C2H2N2O-3 <=> C2H2N2O-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.0435e+11,'s^-1'), n=1.01704, Ea=(242.812,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.32691, dn = +|- 0.0375319, dEa = +|- 0.193534 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: r004202 <=> p002774
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
Systematic conformer search was done with ACS
""",
)

entry(
    index = 8,
    label = "C2H4N2O <=> C2H4N2O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.30252e+10,'s^-1'), n=0.837267, Ea=(238.019,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.22417, dn = +|- 0.0268381, dEa = +|- 0.138391 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: r005588 <=> p005593
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
Systematic conformer search was done with ACS
""",
)

entry(
    index = 9,
    label = "C3H3NO <=> C3H3NO-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6259e+11,'s^-1'), n=1.19107, Ea=(359.894,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.39462, dn = +|- 0.0441353, dEa = +|- 0.227585 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: r005763 <=> p005763
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
Systematic conformer search was done with ACS
""",
)

entry(
    index = 10,
    label = "C4H3N3 <=> C4H3N3-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.04679e+11,'s^-1'), n=1.26667, Ea=(446.512,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.39754, dn = +|- 0.0444136, dEa = +|- 0.22902 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: r007269 <=> p007269
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
Systematic conformer search was done with ACS
""",
)

entry(
    index = 11,
    label = "C4H4N2O <=> C4H4N2O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.1761e+10,'s^-1'), n=0.996245, Ea=(380.451,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.27748, dn = +|- 0.0324947, dEa = +|- 0.16756 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: r011506 <=> p011506
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
Systematic conformer search was done with ACS
""",
)

