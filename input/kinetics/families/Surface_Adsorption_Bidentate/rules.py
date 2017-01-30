#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_Bidentate/rules"
shortDesc = u""
longDesc = u"""
Adsorption of an unsaturated gas-phase species forming a single adsorbate that is bound to two sites (di-sigma)
"""
entry(
    index = 1,
    label = "Adsorbate;VacantSite1;VacantSite2",
    kinetics = StickingCoefficientBEP(
        A = 0.1,
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""Made up"""
)



