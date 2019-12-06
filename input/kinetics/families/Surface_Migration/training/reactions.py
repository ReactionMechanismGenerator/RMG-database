#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Migration/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label = "*nbutane <=> *nbutane2",
    degeneracy = 4,
    kinetics = SurfaceArrhenius(
        A = (7.336e12, 's^-1'),
        n = 0.,
        Ea = (59.33, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""n-butane migration from C1 to C2""",
    longDesc = u"""
From Xu et al. Doi:10.1021/acscatal.7b03205

Given Ea = 59.33 kJ/mol, and fwd rate of 1.22e4/s:
A = 1.22e4/s / exp(-59.33 kJ/mol / R / 353 K) = 7.336e12/s
"""
)

entry(
    index = 2,
    label = "*nhexane <=> *nhexane2",
    degeneracy = 4,
    kinetics = SurfaceArrhenius(
        A = (7.346e12, 's^-1'),
        n = 0.,
        Ea = (58.93, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""n-hexane migration from C1 to C2""",
    longDesc = u"""
From Xu et al. Doi:10.1021/acscatal.7b03205

Given Ea = 58.93 kJ/mol, and fwd rate of 1.40e4/s:
A = 1.40e4/s / exp(-58.93 kJ/mol / R / 353 K) = 7.346e12/s
"""
)

entry(
    index = 3,
    label = "*noctane <=> *noctane2",
    degeneracy = 4,
    kinetics = SurfaceArrhenius(
        A = (7.327e12, 's^-1'),
        n = 0.,
        Ea = (63.31, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""n-octane migration from C1 to C2""",
    longDesc = u"""
From Xu et al. Doi:10.1021/acscatal.7b03205

Given Ea = 63.31 kJ/mol, and fwd rate of 3.14e3/s:
A = 3.14e3/s / exp(-63.31 kJ/mol / R / 353 K) = 7.327e12/s
"""
)
