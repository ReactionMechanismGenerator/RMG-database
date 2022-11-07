#!/usr/bin/env python
# encoding: utf-8

name = "1,3_Insertion_CO2/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "H2 + CO2 <=> CH2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.51e+09,'cm^3/(mol*s)'), n=1.23, Ea=(309.198,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
"""
Degeneracy not recalculated

Converted to training reaction from rate rule: CO2_Cdd;H2
""",
)

entry(
    index = 1,
    label = "CH4 + CO2 <=> C2H4O2",
    degeneracy = 8.0,
    kinetics = Arrhenius(A=(36240,'cm^3/(mol*s)'), n=2.83, Ea=(331.373,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
"""
Converted to training reaction from rate rule: CO2_Cdd;C_methane
""",
)

entry(
    index = 2,
    label = "C2H6 + CO2 <=> C3H6O2",
    degeneracy = 12.0,
    kinetics = Arrhenius(A=(130800,'cm^3/(mol*s)'), n=2.56, Ea=(320.494,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
"""
Converted to training reaction from rate rule: CO2_Cdd;C_pri/NonDeC
""",
)

entry(
    index = 3,
    label = "C3H8 + CO2 <=> C4H8O2",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(424000,'cm^3/(mol*s)'), n=2.13, Ea=(322.168,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 5,
    shortDesc = """[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
"""
Converted to training reaction from rate rule: CO2_Cdd;C/H2/NonDeC
""",
)

entry(
    index = 4,
    label = "C3H8-2 + CO2 <=> C4H8O2-2",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(292,'cm^3/(mol*s)'), n=3.13, Ea=(493.712,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 10,
    shortDesc = """Aaron Vandeputte calculation for methylpropanate using BMK/CBSB7""",
    longDesc = 
"""
Converted to training reaction from rate rule: CO2_Od;C_methyl_C_pri
""",
)

entry(
    index = 5,
    label = "CH3N + CO2 <=> C2H3NO2",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(2.04107e-05,'cm^3/(mol*s)'), n=5.03741, Ea=(330.096,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.75369, dn = +|- 0.0745346, dEa = +|- 0.384339 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p001956_0 + p010048_1 <=> r001958
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 6,
    label = "C2H5N + CO2 <=> C3H5NO2",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(0.00462404,'cm^3/(mol*s)'), n=4.43694, Ea=(287.389,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.15053, dn = +|- 0.0186065, dEa = +|- 0.0959448 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p002395_0 + p010048_1 <=> r002395
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

entry(
    index = 7,
    label = "C3H9N + CO2 <=> C4H9NO2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(0.0798156,'cm^3/(mol*s)'), n=3.39053, Ea=(304.609,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), comment="""Fitted to 50 data points; dA = *|/ 1.33054, dn = +|- 0.0378939, dEa = +|- 0.195401 kJ/mol"""),
    rank = 4,
    shortDesc = """CCSD(T)-F12a/cc-pVDZ-F12//wB97X-D3/def2-TZVP""",
    longDesc = 
"""
Original entry: p010048_0 + p010048_1 <=> r010048
Calculated by Kevin Spiekermann
opt, freq: wB97X-D3/def2-TZVP
sp: CCSD(T)-F12a/cc-pVDZ-F12
All species include systematic conformer search and 1D rotor scans
""",
)

