#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Abstraction_Single_vdW/rules"
shortDesc = u""
longDesc = u"""
A vdW species splitting, adsorbing to the surface, and transferring a functional group to a single bonded surface species.
"""

entry(
    index = 1,
    label = "AdsorbateVdW1;Adsorbate1",
    kinetics = SurfaceArrheniusBEP(
        A = (1.0e13, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.5,
        E0 = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""Made up"""
)
