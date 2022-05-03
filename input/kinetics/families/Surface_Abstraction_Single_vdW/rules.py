#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Abstraction_Single_vdW/rules"
shortDesc = u""
longDesc = u"""
A vdW species splitting, adsorbing to the surface, 
and transferring a functional group to a single bonded surface species.
"""

entry(
    index = 1,
    label = "Donating;Abstracting",
    kinetics = SurfaceArrheniusBEP(
        A = (3.2e+17, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.5,
        E0 = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
    Updated for uncertainty analysis, 1e13 s^-1 (standard guess from transition state theory) divided by 3.16e-9 mol cm^-2
    flagged for uncertainty perturbation
    """
)
