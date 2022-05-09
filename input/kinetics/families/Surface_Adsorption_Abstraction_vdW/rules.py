#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_Abstraction_vdW/rules"
shortDesc = u""
longDesc = u"""
Adsorbtion of a vdw species to the surface with a surface species."""

entry(
    index = 1,
    label = "AdsorbateVdW;Adsorbate1",
    kinetics = SurfaceArrheniusBEP(
        A = (3.2e+17, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.42,
        E0 = (9.68543017, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
    Removing grabow rate and replacing with updated guess for uncertainty analysis. 
    A is 1e13 s^-1 (standard guess from transition state theory) 
    divided by 3.16e-9 mol cm^-2

    flagged for uncertainty perturbation
    """
)