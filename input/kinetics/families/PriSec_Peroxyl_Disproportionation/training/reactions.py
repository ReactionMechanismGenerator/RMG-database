#!/usr/bin/env python
# encoding: utf-8

name = "PriSec_Peroxyl_Disproportionation/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 1,
    label = "CH3OOrad + CH3OOrad <=> CH2O + CH3OH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.0e5, 'm^3/(mol*s)'), n=-0.55, Ea=(6.6944, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""From Glarborg library""",
    longDesc =
u"""

""",
)

entry(
    index = 2,
    label = "BuCH2OOrad + BuCH2OOrad <=> BuCHO + BuCH2OH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.0e6, 'm^3/(mol*s)'), n=0.0, Ea=(9.1, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""Experimental rate at 253-303 K""",
    longDesc =
u"""
SL Khursan, RL Safiullin, SYu Serenko. Khim Fiz 9:375-379, 1990
""",
)

entry(
    index = 3,
    label = "BuMeCHOOrad + BuMeCHOOrad <=> BuMeCO + BuMeCHOH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.88e4, 'm^3/(mol*s)'), n=0.0, Ea=(8.4, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""""",
    longDesc =
u"""
SI Maslennikov, AI Nikolaev, VD Komissarov. Kinet Katal 20:326-329, 1979
""",
)

entry(
    index = 4,
    label = "PrMeCHOOrad + PrMeCHOOrad <=> PrMeCO + PrMeCHOH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.0e4, 'm^3/(mol*s)'), n=0.0, Ea=(6.9, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""""",
    longDesc =
u"""
SL Khursan, RL Safiullin, SYu Serenko. Khim Fiz 9:375-379, 1990
""",
)

entry(
    index = 5,
    label = "EtMeCHOOrad + EtMeCHOOrad <=> EtMeCO + EtMeCHOH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.0e6, 'm^3/(mol*s)'), n=0.0, Ea=(11.3, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""""",
    longDesc =
u"""
JA Howard, JE Bennett. Can J Chem 50:2374-2377, 1972
""",
)

entry(
    index = 6,
    label = "Me2CHOOrad + Me2CHOOrad <=> Me2CO + Me2CHOH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.0e6, 'm^3/(mol*s)'), n=0.0, Ea=(20.0, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""""",
    longDesc =
u"""
JE Bennett. J Chem Soc Faraday Trans 1, 83:1805-1813, 1987
""",
)
