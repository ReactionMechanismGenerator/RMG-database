#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Abstraction_Charge_Single/rules"
shortDesc = u""
longDesc = u"""
"""
entry(
    index = 1,
    label = "Abstracting;Donating",
    kinetics = SurfaceArrheniusBEP(
        A = (5.09e21, 'cm^2/(mol*s)'),
        n = 0,
        alpha = 0.768,
        E0 = (124, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""

""",
)
