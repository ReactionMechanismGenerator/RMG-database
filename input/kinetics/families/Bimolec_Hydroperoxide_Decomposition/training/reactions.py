#!/usr/bin/env python
# encoding: utf-8

name = "Bimolec_Hydroperoxide_Decomposition/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 1,
    label = "HOOH + HOOH <=> HOOrad + HOrad + H2O",
    degeneracy = 4,
    kinetics = Arrhenius(A=(6.918e6, 'm^3/(mol*s)'), n=0.0, Ea=(121.7, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""Experimental rate at 393-413K in cyclohexanol solvent""",
    longDesc =
u"""
ET Denisov, VV Kharitonov. Kinet Katal 5:781-786, 1964
""",
)

entry(
    index = 2,
    label = "Me3COOH + Me3COOH <=> Me3COOrad + Me3COrad + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.096e5, 'm^3/(mol*s)'), n=0.0, Ea=(96.1, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""Experimental rate at 333-363K in heptane solvent""",
    longDesc =
u"""
ET Denisov, TG Denisova. Kinet Catal 34:173-179, 1993
""",
)

entry(
    index = 3,
    label = "EtMe2COOH + EtMe2COOH <=> EtMe2COOrad + EtMe2COrad + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.31e4, 'm^3/(mol*s)'), n=0.0, Ea=(100.0, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""Experimental rate at 333-363K in 2-methylbutane solvent""",
    longDesc =
u"""
TG Degtyareva, VM Solyanikov, ET Denisov. Neftekhimiya 12:854-861, 1972
""",
)

entry(
    index = 4,
    label = "Me/MecychexOOH + Me/MecychexOOH <=> Me/MecychexOOrad + Me/MecychexOrad + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.512e8, 'm^3/(mol*s)'), n=0.0, Ea=(120, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""Experimental rate at 333-353K in benzene solvent""",
    longDesc =
u"""
AV Tobolsky, RE Mesrobian, Organic Peroxides: Their Chemistry, Decomposition and Role in Polymerization.
New York: Interscience, 1954.
""",
)
