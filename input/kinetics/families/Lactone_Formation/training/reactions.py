#!/usr/bin/env python
# encoding: utf-8

name = "Lactone_Formation/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "C2HF3O2 <=> C2F2O2 + FH",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(9.57e+11,'s^-1'), n=0.34, Ea=(53059.3,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CF3C(O)OH <=> c_F2COC(O)+HF
""",
)

entry(
    index = 1,
    label = "C3HF5O2 <=> C3F4O2 + FH",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(8.93e+10,'s^-1'), n=0.59, Ea=(56742.3,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C2F5C(O)OH <=> CF3-c_FCOC(O)+HF
""",
)

entry(
    index = 2,
    label = "C4HF7O2 <=> C4F6O2 + FH",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.06e+10,'s^-1'), n=0.85, Ea=(55739.6,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C3F7C(O)OH <=> C2F5-c_FCOC(O)+HF
""",
)

entry(
    index = 3,
    label = "C5HF9O2 <=> C5F8O2 + FH",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(7.32e+07,'s^-1'), n=1.61, Ea=(55284,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C4F9C(O)OH <=> C3F7-c_FCOC(O)+HF
""",
)

entry(
    index = 4,
    label = "C2H3FO2 <=> C2H2O2 + FH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.35e+11,'s^-1'), n=0.49, Ea=(50380.5,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CH2FC(O)OH <=> c_H2COC(O)+HF
""",
)

entry(
    index = 5,
    label = "C3H5FO2 <=> C3H4O2 + FH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.78e+10,'s^-1'), n=0.58, Ea=(45034.9,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CH3CFHC(O)OH <=> CH3-c_HCOC(O)+HF
""",
)

entry(
    index = 6,
    label = "C2H4O2 <=> C2H2O2 + H2",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(11800,'s^-1'), n=2.77, Ea=(97016.4,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CH3C(O)OH <=> c_H2COC(O)+H2
""",
)

entry(
    index = 7,
    label = "C3H6O2 <=> C3H4O2 + H2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(136000,'s^-1'), n=2.37, Ea=(89515.2,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C2H5C(O)OH <=> CH3-c_HCOC(O)+H2
""",
)

entry(
    index = 8,
    label = "C4H8O2 <=> C4H6O2 + H2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(52800,'s^-1'), n=2.44, Ea=(88012.6,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C3H7C(O)OH <=> C2H5-c_HCOC(O)+H2
""",
)

entry(
    index = 9,
    label = "C4HF7O3 <=> C4F6O3 + FH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.8e+12,'s^-1'), n=0.42, Ea=(48368.1,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CF3OCF(CF3)C(O)OH <=> CF3O-c_(CF3)COC(O)+HF
""",
)

entry(
    index = 10,
    label = "C5HF9O3 <=> C5F8O3 + FH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.51e+14,'s^-1'), n=-0.2, Ea=(56198.9,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C2F5OCF(CF3)C(O)OH <=> C2F5O-c_(CF3)COC(O)+HF
""",
)

entry(
    index = 11,
    label = "C6HF11O3 <=> C6F10O3 + FH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.78e+15,'s^-1'), n=-0.84, Ea=(49834.2,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C3F7OCF(CF3)C(O)OH <=> C3F7O-c_(CF3)COC(O)+HF
""",
)

entry(
    index = 12,
    label = "C4H8O3 <=> C4H6O3 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.37e+06,'s^-1'), n=1.62, Ea=(64042,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: CH3OCH(CH3)C(O)OH <=> CH3O-c_(CH3)COC(O)+H2
""",
)

entry(
    index = 13,
    label = "C5H10O3 <=> C5H8O3 + H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.17e+07,'s^-1'), n=1.55, Ea=(63678.9,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C2H5OCH(CH3)C(O)OH <=> C2H5O-c_(CH3)COC(O)+H2
""",
)

entry(
    index = 14,
    label = "C6HF11O2 <=> C6F10O2 + FH",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(6.7e+10,'s^-1'), n=0.7, Ea=(55450.5,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C5F11C(O)OH <=> C4F9-c_FCOC(O)+HF
""",
)

entry(
    index = 15,
    label = "C7HF13O2 <=> C7F12O2 + FH",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.09e+11,'s^-1'), n=0.55, Ea=(55585.8,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C6F13C(O)OH <=> C5F11-c_FCOC(O)+HF
""",
)

entry(
    index = 16,
    label = "C8HF15O2 <=> C8F14O2 + FH",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3.18e+10,'s^-1'), n=0.8, Ea=(55701.8,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL
Original entry: C7F15C(O)OH <=> C6F13-c_FCOC(O)+HF
""",
)

