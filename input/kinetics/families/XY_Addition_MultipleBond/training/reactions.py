#!/usr/bin/env python
# encoding: utf-8

name = "XY-Addition_MultipleBond/training"
shortDesc = "Kinetics used to train group additivity values"
longDesc = """
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 0,
    label = "CH3-CHF2 <=> CH2CHF + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.94e+13,'s^-1'), n=0, Ea=(61900,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 1,
    label = "CH3-CF3 <=> CH2CF2 + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+14,'s^-1'), n=0, Ea=(68700,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 2,
    label = "CH2F-CH2F <=> CH2CHF + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+13,'s^-1'), n=0, Ea=(62900,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 3,
    label = "CH2F-CHF2 <=> CHFCHF[Z] + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.26e+14,'s^-1'), n=0, Ea=(69100,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 4,
    label = "CH2F-CHF2 <=> CH2CF2 + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'s^-1'), n=0, Ea=(65400,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 5,
    label = "CH2F-CF3 <=> CHFCF2 + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+11,'s^-1'), n=0, Ea=(62690,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST 2019 CH2F2 model""",
)

entry(
    index = 6,
    label = "CHF2-CHF2 <=> CHFCF2 + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'s^-1'), n=0, Ea=(69400,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 7,
    label = "CHF2-CF3 <=> CF2CF2 + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+13,'s^-1'), n=0, Ea=(71600,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """From NIST CH2F2 model""",
)

entry(
    index = 8,
    label = "C2H5F <=> C2H4 + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.63e+13,'s^-1'), n=0, Ea=(59900,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is CH3-CH2F <=> C2H4 + HF""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: CH3-CH2F <=> C2H4 + HF
""",
)

entry(
    index = 9,
    label = "C2H4F2 <=> CH2CHF + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.94e+13,'s^-1'), n=0, Ea=(61900,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is CH3-CHF2 <=> CH2:CHF + HF""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: CH3-CHF2 <=> CH2:CHF + HF
""",
)

entry(
    index = 10,
    label = "C2H3F3 <=> CH2CF2 + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+14,'s^-1'), n=0, Ea=(68700,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is CH3-CF3 <=> CH2:CF2 + HF""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: CH3-CF3 <=> CH2:CF2 + HF
""",
)

entry(
    index = 11,
    label = "C2H4F2-2 <=> C2H3F + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.5e+13,'s^-1'), n=0, Ea=(62900,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is CH2F-CH2F <=> CH2:CHF + HF""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: CH2F-CH2F <=> CH2:CHF + HF
""",
)

entry(
    index = 12,
    label = "C2H3F3-2 <=> CHFCHF[Z] + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.26e+14,'s^-1'), n=0, Ea=(69100,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is CH2F-CHF2 <=> CHF:CHF[Z] + HF""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: CH2F-CHF2 <=> CHF:CHF[Z] + HF
""",
)

entry(
    index = 13,
    label = "C2H3F3-3 <=> C2H2F2 + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'s^-1'), n=0, Ea=(65400,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is CH2F-CHF2 <=> CH2:CF2 + HF""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: CH2F-CHF2 <=> CH2:CF2 + HF
""",
)

entry(
    index = 14,
    label = "C2H2F4 <=> CHFCF2 + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.63e+13,'s^-1'), n=0, Ea=(70700,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is CH2F-CF3 <=> CHF:CF2 + HF""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: CH2F-CF3 <=> CHF:CF2 + HF
""",
)

entry(
    index = 15,
    label = "C2H2F4-2 <=> C2HF3 + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+13,'s^-1'), n=0, Ea=(69400,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is CHF2-CHF2 <=> CHF:CF2 + HF""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: CHF2-CHF2 <=> CHF:CF2 + HF
""",
)

entry(
    index = 16,
    label = "C2HF5 <=> CF2CF2 + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+13,'s^-1'), n=0, Ea=(71600,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is CHF2-CF3 <=> CF2:CF2 + HF""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: CHF2-CF3 <=> CF2:CF2 + HF
""",
)

entry(
    index = 17,
    label = "C2H5Br <=> C2H4 + BrH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.7e+13,'s^-1'), n=0, Ea=(53000,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is C2H5BR <=> C2H4 + HBR""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: C2H5BR <=> C2H4 + HBR
""",
)

entry(
    index = 18,
    label = "BrH + C3HF3 <=> C3H2BrF3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2e+12,'cm^3/(mol*s)'), n=0, Ea=(51390,'cal/mol'), T0=(1,'K')),
    rank = 3,
    shortDesc = """The chemkin file reaction is CF3CCH + HBR <=> BTP""",
    longDesc = 
"""
Training reaction from kinetics library: 2-BTP
Original entry: CF3CCH + HBR <=> BTP
""",
)

entry(
    index = 19,
    label = "C3H2F4 <=> C3HF3-2 + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3e+51,'s^-1'), n=-10.897, Ea=(102870,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is CHFCHCF3 <=> HF + CF3CCH""",
    longDesc = 
"""
Training reaction from kinetics library: NIST_Fluorine/reduced
Original entry: CHFCHCF3 <=> HF + CF3CCH
""",
)

entry(
    index = 20,
    label = "C3H2F4-2 <=> C3HF3 + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.1e+44,'s^-1'), n=-8.492, Ea=(99304,'cal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """The chemkin file reaction is CH2CFCF3 <=> CF3CCH + HF""",
    longDesc = 
"""
Training reaction from kinetics library: NIST_Fluorine/reduced
Original entry: CH2CFCF3 <=> CF3CCH + HF
""",
)

entry(
    index = 21,
    label = "CF3OH <=> CF2O + HF",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.94e+11,'s^-1'), n=0.45, Ea=(45.2,'kcal/mol'), T0=(1,'K')),
    rank = 10,
    shortDesc = """CF3OH Decomposition""",
    longDesc = 
"""
https://pubs.acs.org/doi/pdf/10.1021/jp709796n
""",
)


