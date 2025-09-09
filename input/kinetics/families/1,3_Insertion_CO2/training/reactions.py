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

entry(
    index = 8,
    label = "C3HF5O2 <=> CO2 + C2HF5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.54e-42,'s^-1'), n=16.02, Ea=(42280.7,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C2F5C(O)OH <=> C2F5H+CO2
""",
)

entry(
    index = 9,
    label = "C4HF6O2 <=> CO2 + C3HF6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.44e-44,'s^-1'), n=16.52, Ea=(41072.8,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C3F6C(O)OH <=> C2F4CF2H+CO2
""",
)

entry(
    index = 10,
    label = "C4HF7O2 <=> CO2 + C3HF7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.18e-40,'s^-1'), n=15.66, Ea=(42257.3,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C3F7C(O)OH <=> C3F7H+CO2
""",
)

entry(
    index = 11,
    label = "C4HF7O3 <=> CO2 + C3HF7O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.99e-30,'s^-1'), n=12.69, Ea=(46973.6,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CF3OCF(CF3)C(O)OH <=> CF3OCFHCF3+CO2
""",
)

entry(
    index = 12,
    label = "C5HF9O2 <=> CO2 + C4HF9",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.93e-43,'s^-1'), n=16.39, Ea=(41420.4,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C4F9C(O)OH <=> C4F9H+CO2
""",
)

entry(
    index = 13,
    label = "C5HF9O3 <=> CO2 + C4HF9O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.77e-25,'s^-1'), n=11.12, Ea=(47765.6,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C2F5OCF(CF3)C(O)OH <=> C2F5OCFHCF3+CO2
""",
)

entry(
    index = 14,
    label = "C6HF11O3 <=> CO2 + C5HF11O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.14e-22,'s^-1'), n=10.39, Ea=(48295.9,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C3F7OCF(CF3)C(O)OH <=> C3F7OCFHCF3+CO2
""",
)

entry(
    index = 15,
    label = "CH2O2 <=> CO2 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.15e-48,'s^-1'), n=17.68, Ea=(34510.9,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: HC(O)OH <=> H2+CO2
""",
)

entry(
    index = 16,
    label = "C2H4O2 <=> CO2 + CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.6e-39,'s^-1'), n=15.17, Ea=(42623.1,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CH3C(O)OH <=> CH4+CO2
""",
)

entry(
    index = 17,
    label = "C3H5O2 <=> CO2 + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(340,'s^-1'), n=2.56, Ea=(20162.6,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C2H4C(O)OH <=> C2H5+CO2
""",
)

entry(
    index = 18,
    label = "C4H8O3 <=> CO2 + C3H8O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.39e-35,'s^-1'), n=13.62, Ea=(46555.1,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CH3OCH(CH3)C(O)OH <=> C2H5OCH3+CO2
""",
)

entry(
    index = 19,
    label = "C5H10O3 <=> CO2 + C4H10O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.39e-34,'s^-1'), n=13.36, Ea=(46864.2,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C2H5OCH(CH3)C(O)OH <=> C2H5OC2H5+CO2
""",
)

entry(
    index = 20,
    label = "C2HF3O2 <=> CO2 + CHF3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.19e-45,'s^-1'), n=17.11, Ea=(41536.3,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CF3C(O)OH <=> CF3H+CO2,""",
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CF3C(O)OH <=> CF3H+CO2
""",
)

entry(
    index = 21,
    label = "CHFO2 <=> CO2 + FH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(25300,'s^-1'), n=2.53, Ea=(28082.1,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: FC(O)OH <=> CO2+HF
""",
)

entry(
    index = 22,
    label = "C3HF4O2 <=> CO2 + C2HF4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(66.3,'s^-1'), n=2.87, Ea=(24236.8,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C2F4C(O)OH <=> CF2CF2H+CO2
""",
)

