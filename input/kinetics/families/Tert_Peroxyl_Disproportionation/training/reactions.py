#!/usr/bin/env python
# encoding: utf-8

name = "Tert_Peroxyl_Disproportionation/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 1,
    label = "Me3COOrad + Me3COOrad <=> Me3COrad + Me3COrad + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.48e9, 'm^3/(mol*s)'), n=0.0, Ea=(35.6, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""Experimental rate at 303 K in methylcyclohexane solvent""",
    longDesc =
u"""
WJ Maguire, RC Pink. Trans Faraday Soc 64:1097-1105, 1967
""",
)

entry(
    index = 2,
    label = "Me/cyclohexaneOOrad + Me/cyclohexaneOOrad <=> Me/cyclohexaneOrad + Me/cyclohexaneOrad + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.40e5, 'm^3/(mol*s)'), n=0.0, Ea=(25.2, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""Experimental rate at 187-263 K in methylcyclohexane solvent""",
    longDesc =
u"""
LA Tavadyan, MV Musaelyan, VA Mardoyan. Khim Fiz 10:511-515, 1991
""",
)
