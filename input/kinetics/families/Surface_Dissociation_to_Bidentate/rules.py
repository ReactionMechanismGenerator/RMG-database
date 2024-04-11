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
        A = (1.41E22, 'm^4/(mol^2*s)'),
        n = 0.0,
        alpha = 0.87,
        E0 = (77.188, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
A and n factors are from the average rates of training reactions 1-2 and reverse of 3-4, and alpha and E0 are BEP
parameters from training reactions 1-2 and reverse of 3-4.

Details on the computational method to derive the rate constants for the BEP relation are provided in "Automatic mechanism generation involving 
kinetics of surface reactions with bidentate adsorbates" by B. Kreitz, K. Blöndal, K. Badger, R. H. West and C. F. Goldsmith, Digital Discovery, 2024, 3, 173
doi:10.1039/d3dd00184a
"""
)
