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
        n = 0.,
        alpha =0.94,
        E0 = (129.3, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u""" 
These numbers for the general BEP are from the abstraction reaction of C-H to O.
BEP values from "Combined DFT, Microkinetic, and Experimental Study of Ethanol Steam Reforming on Pt", Sutton et al., The Journal of Physical Chemistry C, 2013, 117, 4691-4706, DOI:10.1021/jp312593u
From Table 7 includes beta and alpha position. Pre-exponential coefficient is calculated from 1e13 s^-1 (standard guess from transition state theory) divided by 2.39e-9 mol cm^-2 (surface site density of Pt(111)
"""
)
