#!/usr/bin/env python
# encoding: utf-8

name = "Surface_vdW_to_Bidentate/rules"
shortDesc = u""
longDesc = u"""
"""
entry(
    index = 1,
    label = "Combined;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (1.0e15, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.0,
        E0 = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
    These values are made up.
    """
)
