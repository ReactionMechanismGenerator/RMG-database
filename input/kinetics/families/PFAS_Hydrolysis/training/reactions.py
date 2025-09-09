#!/usr/bin/env python
# encoding: utf-8

name = "PFAS_Hydrolysis/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "CF2O + H2O <=> FH + CHFO2",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(0.242,'cm^3/(mol*s)'), n=3.33, Ea=(35135.3,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/PFAS_Hydrolysis/
Original entry: CF2O+H2O <=> FC(O)OH+HF
""",
)

entry(
    index = 1,
    label = "CF4 + H2O <=> FH + CHF3O",
    degeneracy = 8.0,
    kinetics = Arrhenius(A=(48.9,'cm^3/(mol*s)'), n=3.22, Ea=(86268,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/PFAS_Hydrolysis/
Original entry: CF4+H2O <=> CF3OH+HF
""",
)

entry(
    index = 2,
    label = "C2F4O + H2O <=> FH + C2HF3O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(0.0257,'cm^3/(mol*s)'), n=3.6, Ea=(30432.1,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/PFAS_Hydrolysis/
Original entry: CF3CFO+H2O <=> CF3C(O)OH+HF
""",
)

entry(
    index = 3,
    label = "C2F6 + H2O <=> FH + C2HF5O",
    degeneracy = 12.0,
    kinetics = Arrhenius(A=(2.98,'cm^3/(mol*s)'), n=3.36, Ea=(80307.6,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/PFAS_Hydrolysis/
Original entry: C2F6+H2O <=> C2F5OH+HF
""",
)

entry(
    index = 4,
    label = "C3F6O + H2O <=> FH + C3HF5O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(0.00923,'cm^3/(mol*s)'), n=3.71, Ea=(30829.4,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/PFAS_Hydrolysis/
Original entry: C2F5CFO+H2O <=> C2F5C(O)OH+HF
""",
)

entry(
    index = 5,
    label = "C3F8 + H2O <=> FH + C3HF7O",
    degeneracy = 12.0,
    kinetics = Arrhenius(A=(0.0677,'cm^3/(mol*s)'), n=3.77, Ea=(79908.1,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/PFAS_Hydrolysis/
Original entry: C3F8+H2O <=> C3F7OH+HF
""",
)

entry(
    index = 6,
    label = "C4F8O + H2O <=> FH + C4HF7O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(0.00267,'cm^3/(mol*s)'), n=3.86, Ea=(31139.6,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/PFAS_Hydrolysis/
Original entry: C3F7CFO+H2O <=> C3F7C(O)OH+HF
""",
)

entry(
    index = 7,
    label = "CHFO + H2O <=> FH + CH2O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(0.861,'cm^3/(mol*s)'), n=3.26, Ea=(31335.5,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/PFAS_Hydrolysis/
Original entry: CFHO+H2O <=> HC(O)OH+HF
""",
)

entry(
    index = 8,
    label = "C2H3FO + H2O <=> FH + C2H4O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(0.68,'cm^3/(mol*s)'), n=3.28, Ea=(30890.2,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/PFAS_Hydrolysis/
Original entry: CH3CFO+H2O <=> CH3C(O)OH+HF
""",
)

entry(
    index = 9,
    label = "CH2O + H2O <=> H2 + CH2O2",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(6.43e-07,'cm^3/(mol*s)'), n=5.03, Ea=(58456.6,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/PFAS_Hydrolysis/
Original entry: CH2O+H2O <=> HC(O)OH+H2
""",
)

entry(
    index = 10,
    label = "C2H4O + H2O <=> H2 + C2H4O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(8.54e-07,'cm^3/(mol*s)'), n=4.97, Ea=(58650.2,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/PFAS_Hydrolysis/
Original entry: CH3CHO+H2O <=> CH3C(O)OH+H2
""",
)

entry(
    index = 11,
    label = "C3H6O + H2O <=> H2 + C3H6O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(5.12e-07,'cm^3/(mol*s)'), n=5.03, Ea=(57674.4,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/PFAS_Hydrolysis/
Original entry: C2H5CHO+H2O <=> C2H5C(O)OH+H2
""",
)

entry(
    index = 12,
    label = "CH3F + H2O <=> FH + CH4O",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(10.3,'cm^3/(mol*s)'), n=3.42, Ea=(65515.4,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/PFAS_Hydrolysis/
Original entry: CH3F+H2O <=> CH3OH+HF
""",
)

entry(
    index = 13,
    label = "C2H5F + H2O <=> FH + C2H6O",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(5.99,'cm^3/(mol*s)'), n=3.24, Ea=(61755.8,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/PFAS_Hydrolysis/
Original entry: C2H5F+H2O <=> C2H5OH+HF
""",
)

entry(
    index = 14,
    label = "C3H7F + H2O <=> FH + C3H8O",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.46,'cm^3/(mol*s)'), n=3.33, Ea=(61435.6,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/PFAS_Hydrolysis/
Original entry: C3H7F+H2O <=> C3H7OH+HF
""",
)

entry(
    index = 15,
    label = "CH4 + H2O <=> H2 + CH4O",
    degeneracy = 8.0,
    kinetics = Arrhenius(A=(0.000523,'cm^3/(mol*s)'), n=4.85, Ea=(112002,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/PFAS_Hydrolysis/
Original entry: CH4+H2O <=> CH3OH+H2
""",
)

entry(
    index = 16,
    label = "C2H6 + H2O <=> H2 + C2H6O",
    degeneracy = 12.0,
    kinetics = Arrhenius(A=(0.000297,'cm^3/(mol*s)'), n=4.79, Ea=(107719,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/PFAS_Hydrolysis/
Original entry: C2H6+H2O <=> C2H5OH+H2
""",
)

entry(
    index = 17,
    label = "C3H8 + H2O <=> H2 + C3H8O",
    degeneracy = 12.0,
    kinetics = Arrhenius(A=(1.46e-05,'cm^3/(mol*s)'), n=4.98, Ea=(107230,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/PFAS_Hydrolysis/
Original entry: C3H8+H2O <=> C3H7OH+H2
""",
)

entry(
    index = 18,
    label = "C5F10O + H2O <=> FH + C5HF9O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(0.00448,'cm^3/(mol*s)'), n=3.8, Ea=(33069.2,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/PFAS_Hydrolysis/
Original entry: C4F9CFO+H2O <=> C4F9C(O)OH+HF
""",
)

entry(
    index = 19,
    label = "C6F12O + H2O <=> FH + C6HF11O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(0.00187,'cm^3/(mol*s)'), n=3.88, Ea=(33037.8,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/PFAS_Hydrolysis/
Original entry: C5F11CFO+H2O <=> C5F11C(O)OH+HF
""",
)

entry(
    index = 20,
    label = "C7F14O + H2O <=> FH + C7HF13O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(0.00509,'cm^3/(mol*s)'), n=3.78, Ea=(33513.6,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/PFAS_Hydrolysis/
Original entry: C6F13CFO+H2O <=> C6F13C(O)OH+HF
""",
)

