#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Migration/rules"
shortDesc = u""
longDesc = u"""
Surface species migrating where it binds to the surface
"""
entry(
    index = 1,
    label = "Adsorbate1",
    kinetics = SurfaceArrheniusBEP(
        A = (1.0e13, '1/s'),
        n = 0,
        alpha = 0,
        E0 = (100, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""From Xu et al. Doi:10.1021/acscatal.7b03205 sort of, made up the rest -E"""
)

entry(
    index = 2,
    label = "*nbutane",
    kinetics = SurfaceArrheniusBEP(
        A = (7.336e12, '1/s'),
        n = 0,
        alpha = 0,
        E0 = (59.33, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""n-butane migration from C1 to C2""",
    longDesc = u"""From Xu et al. Doi:10.1021/acscatal.7b03205

Given Ea = 59.33 kJ/mol, and fwd rate of 1.22e4/s:
A = 1.22e4/s / exp(-59.33 kJ/mol / R / 353 K) = 7.336e12/s
"""
)

entry(
    index = 3,
    label = "*nhexane",
    kinetics = SurfaceArrheniusBEP(
        A = (7.346e12, '1/s'),
        n = 0,
        alpha = 0,
        E0 = (58.93, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""n-hexane migration from C1 to C2""",
    longDesc = u"""From Xu et al. Doi:10.1021/acscatal.7b03205

Given Ea = 58.93 kJ/mol, and fwd rate of 1.40e4/s:
A = 1.40e4/s / exp(-58.93 kJ/mol / R / 353 K) = 7.346e12/s
"""
)

entry(
    index = 4,
    label = "*noctane",
    kinetics = SurfaceArrheniusBEP(
        A = (7.327e12, '1/s'),
        n = 0,
        alpha = 0,
        E0 = (63.31, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""n-octane migration from C1 to C2""",
    longDesc = u"""From Xu et al. Doi:10.1021/acscatal.7b03205

Given Ea = 63.31 kJ/mol, and fwd rate of 3.14e3/s:
A = 3.14e3/s / exp(-63.31 kJ/mol / R / 353 K) = 7.327e12/s
"""
)


entry(
    index = 5,
    label = "*C",
    kinetics = SurfaceArrheniusBEP(
        A = (7.336e12, '1/s'),
        n = 0,
        alpha = 0,
        E0 = (59.33, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""See *C4"""
)
