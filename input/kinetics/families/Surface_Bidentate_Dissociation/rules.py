#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Bidentate_Dissociation/rules"
shortDesc = u""
longDesc = u"""
"""
entry(
    index = 1,
    label = "Combined",
    kinetics = SurfaceArrheniusBEP(
        A = (2.655E06, '1/s'),
        n = 1.675, 
        alpha = 0.821,
        E0 = (34.36, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
A and n factors are averages of training reactions 1-3 and the reverse direction of training reactions 4-7, 
and alpha and E0 are BEP parameters from training reactions 1-3 and the reverse of training reactions 4-7.
"""
)
