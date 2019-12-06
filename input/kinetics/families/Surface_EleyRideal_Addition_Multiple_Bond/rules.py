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

entry(
    index = 2,
    label = "*C;R=R",
    kinetics = StickingCoefficientBEP(
        A = 5e-2,
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

entry(
    index = 3,
    label = "*C12+;Gas",
    kinetics = StickingCoefficientBEP(
        A = 5e-3,
        n = 0,
        alpha = 0,
        E0 = (85., 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""Made up"""
)

entry(
    index = 4,
    label = "*C6;R=R",
    kinetics = StickingCoefficientBEP(
        A = 5e-2,
        n = 0,
        alpha = 0,
        E0 = (77.62, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""E0 is Ea from Xu et al. Doi:10.1021/acscatal.7b03205"""
)

entry(
    index = 5,
    label = "*C8;R=R",
    kinetics = StickingCoefficientBEP(
        A = 5e-2,
        n = 0,
        alpha = 0,
        E0 = (77.62, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""Same as *C6.  E0 is Ea from Xu et al. Doi:10.1021/acscatal.7b03205"""
)

entry(
    index = 6,
    label = "*H;R=R",
    kinetics = StickingCoefficientBEP(
        A = 5e-2,
        n = 0,
        alpha = 0,
        E0 = (68.66, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""Same as *C"""
)

entry(
    index = 7,
    label = "*C2;R=R",
    kinetics = StickingCoefficientBEP(
        A = 5e-2,
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

entry(
    index = 8,
    label = "*C4;R=R",
    kinetics = StickingCoefficientBEP(
        A = 5e-2,
        n = 0,
        alpha = 0,
        E0 = (68.34, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""E0 is Ea from Xu et al. Doi:10.1021/acscatal.7b03205"""
)
