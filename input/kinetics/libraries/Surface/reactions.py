#!/usr/bin/env python
# encoding: utf-8

name = "Surface"
shortDesc = u""
longDesc = u"""
test surface mechanism:
"""

entry(
    index = 1,
    label = "O2 + Ni + Ni <=> OX + OX",
    kinetics = StickingCoefficient(
        A = 0.1,
        n = 0,
        Ea=(0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""Made up"""
)



entry(
    index = 2,
    label = "CH4 + Ni + Ni <=> CH3X + HX",
    kinetics = StickingCoefficient(
        A = 0.1,
        n = 0,
        Ea=(0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""Made up"""
)