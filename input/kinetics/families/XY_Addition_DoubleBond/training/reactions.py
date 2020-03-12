#!/usr/bin/env python
# encoding: utf-8

name = "XY-Addition_DoubleBond/training"
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

