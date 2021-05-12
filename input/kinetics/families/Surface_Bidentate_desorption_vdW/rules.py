#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Bidentate_desorption_vdW/rules"
shortDesc = u""
longDesc = u"""
Surface adsorption of a closed-shell gas-phase species forming a van der Waals bond to the surface site
"""
entry(
    index = 1,
    label = "Adsorbed",
    kinetics = SurfaceArrheniusBEP(
        A = (1e13, '1/s'),
        n = 0,
        alpha = 0,
        E0 = (0.0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
)
