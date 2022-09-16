#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_to_Bidentate/rules"
shortDesc = u""
longDesc = u"""
"""

entry(
    index = 1,
    label = "Combined;VacantSite1;VacantSite2",
    kinetics = SurfaceArrheniusBEP(
        A = (5.726E21, 'm^4/(mol^2*s)'), 
        n = 0.0,  
        alpha = 0.0824, 
        E0 = (12.11, 'kcal/mol'), 
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
A and n factors are from the average rates of training reactions 1-3, and alpha and E0 are BEP
parameters from training reactions 1-3 (in the Surface_Dissociation_to_Bidentate 
forward direction).
The A factor has been divided by 2.33 here to account for the average degeneracy of the training reactions.
"""
)
