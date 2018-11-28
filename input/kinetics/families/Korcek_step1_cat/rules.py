#!/usr/bin/env python
# encoding: utf-8

name = "Korcek_step1_cat/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "RCH(OOH)CH2C(O)R';R''C(O)OH",
    kinetics = ArrheniusEP(
        A = (6.3e5, 'cm^3/mol/s'),
        n = 0.0,
        alpha = 0,
        E0 = (-1.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (800, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Rate from Jalan et al. (JACS, 2013) for the case where R=R'=R''=H""",
)

