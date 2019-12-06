#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_Abstraction_vdW/rules"
shortDesc = u""
longDesc = u"""
Adsorbtion of a vdw species to the surface with a surface species."""

entry(
    index = 43,
    label = "AdsorbateVdW;Adsorbate1",
    kinetics = SurfaceArrheniusBEP(
        A = (5.43e11, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.42,
        E0 = (9.68543017, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 43 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

E0 is Ea
"""
)