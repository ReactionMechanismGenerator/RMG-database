#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Addition_Single_vdW/rules"
shortDesc = u""
longDesc = u"""
A single bonded surface species adding to a vdW double, triple, or quadruple bonded species and adsorbing to a surface.
"""

entry(
    index = 1,
    label = "AdsorbateVdW;Adsorbate1",
    kinetics = SurfaceArrheniusBEP(
        A = (1.0e17, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.5,
        E0 = (15.0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""Made up"""
)
