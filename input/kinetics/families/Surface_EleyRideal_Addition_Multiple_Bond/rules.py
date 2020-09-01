#!/usr/bin/env python
# encoding: utf-8

name = "Surface_EleyRideal_Addition_Multiple_Bond/rules"
shortDesc = u""
longDesc = u"""
Eley Rideal mechanism for a gas phase double or triple bonded species.
"""
entry(
    index = 1,
    label = "Adsorbate1;Gas",
    kinetics = StickingCoefficientBEP(
        A = 5e-6,
        n = 0,
        alpha = 0,
        E0 = (68.66, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""E0 is Ea from Xu et al. Doi:10.1021/acscatal.7b03205"""
)
