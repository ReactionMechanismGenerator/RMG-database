#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Abstraction_vdW/rules"
shortDesc = u""
longDesc = u"""
A vdW double bonded species dissociatively adsorbing to the surface with double
bonds.
"""

entry(
    index = 1,
    label = "AdsorbateVdW;Adsorbate1",
    kinetics = SurfaceArrheniusBEP(
        A = (1.0e13, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.57,
        E0 = (15.62, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""source from http://dx.doi.org/10.1021/acs.jctc.6b00168""",
    longDesc = u"""adapted from table 3 in 'Effect of the Exchange-Correlation Potential on the Transferability of 
    Brønsted–Evans–Polanyi Relationships in Heterogeneous Catalysis'
    This is for H dissociationn, so it is more appropriate when another group is being abstracted to an empty site. nevertheless, we'll use it for
    this and the surface abstraction single vdw family in lieu of a better estimate. 
    """
)