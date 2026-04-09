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
        A = (2.68E30, 'cm^4/(mol^2*s)'),
        n = 0.0,
        alpha = 0.636,
        E0 = (85.5, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
This BEP is created from a mixture of data in literature taken from the following papers: 

Gomez-Díaz and Lopez
https://pubs.acs.org/doi/10.1021/jp1093349

Deng et al.
https://pubs.rsc.org/en/content/articlelanding/2014/ra/c3ra46544f

kreitz et. al
https://doi.org/10.1021/acscatal.2c03378

and the current manuscript in progress by Badger et al. looking at the effects
of NO on the light out curves for hydrocarbons.
"""
)
