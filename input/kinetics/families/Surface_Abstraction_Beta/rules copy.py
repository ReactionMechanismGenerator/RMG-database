#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Abstraction_Beta/rules"
shortDesc = u""
longDesc = u"""
"""

entry(
    index = 1,
    label = "Combined;Adsorbate1",
    kinetics = SurfaceArrheniusBEP(
        A = (3.2e17, 'm^2/(mol*s)'),
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
From Table 7 includes beta and alpha position. Pre-exponential coefficient is calculated from 1e13 s^-1 (standard guess from transition state theory) divided by 3.16e-9 mol cm^-2 (Kreitz et al. 2021, DOI: 10.1021/jacsau.1c00276)
"""
)

entry(
    index = 2,
    label = "C-H;O",
    kinetics = SurfaceArrheniusBEP(
        A = (3.2e17, 'm^2/(mol*s)'),
        n = 0.,
        alpha =0.94,
        E0 = (129.3, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
BEP values from "Combined DFT, Microkinetic, and Experimental Study of Ethanol Steam Reforming on Pt", Sutton et al., The Journal of Physical Chemistry C, 2013, 117, 4691-4706, DOI:10.1021/jp312593u
From Table 7 includes beta and alpha position. Pre-exponential coefficient is calculated from 1e13 s^-1 (standard guess from transition state theory) divided by 3.16e-9 mol cm^-2 (Kreitz et al. 2021, DOI: 10.1021/jacsau.1c00276)
"""
)

entry(
    index = 3,
    label = "O-H;O",
    kinetics = SurfaceArrheniusBEP(
        A = (3.2e17, 'm^2/(mol*s)'),
        n = 0.,
        alpha =0.65,
        E0 = (15.4, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
BEP values from "Combined DFT, Microkinetic, and Experimental Study of Ethanol Steam Reforming on Pt", Sutton et al., The Journal of Physical Chemistry C, 2013, 117, 4691-4706, DOI:10.1021/jp312593u
From Table 7 includes beta and alpha position. Pre-exponential coefficient is calculated from 1e13 s^-1 (standard guess from transition state theory) divided by 3.16e-9 mol cm^-2 (Kreitz et al. 2021, DOI: 10.1021/jacsau.1c00276)
"""
)
