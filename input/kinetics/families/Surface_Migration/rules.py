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
        A = (1.0e13, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (50, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""From Xu et al. Doi:10.1021/acscatal.7b03205 sort of,
    but mostly made up -E"""
)
