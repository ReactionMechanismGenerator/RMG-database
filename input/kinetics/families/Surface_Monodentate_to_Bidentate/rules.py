#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Monodentate_to_Bidentate/rules"
shortDesc = u""
longDesc = u"""
"""
entry(
    index = 1,
    label = "Monodentate;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (7.15e20, 'cm^2/(mol*s)'),
        n = 0.0,
        alpha = 0,
        E0 = (3, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
Pre-exponential value and E0 are from R6b in Table 2 of "Automatic mechanism generation involving 
kinetics of surface reactions with bidentate adsorbates"
Authors:  B. Kreitz, K. Blöndal, K. Badger, R. H. West and C. F. Goldsmith
doi:10.1039/d3dd00184a

The reaction R6b is
   *CHCH2 + *  -> *CH*CH2

Other monodentate to bidentate reactions in this publication were without reaction barriers.
"""
)



