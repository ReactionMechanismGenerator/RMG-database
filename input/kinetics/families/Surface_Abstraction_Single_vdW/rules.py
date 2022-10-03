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
        A = (4.18e17, 'm^2/(mol*s)'),
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
