#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_Beta/rules"
shortDesc = u""
longDesc = u"""
"""

entry(
    index = 29,
    label = "Adsorbate1;Adsorbate2",
    kinetics = SurfaceArrheniusBEP(
        A = (3.048e17, 'm^2/(mol*s)'),
        n = 0.,
        alpha = 0.54,
        E0 = (20.9850987, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 29 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

E0 is Ea

A factor from paper / surface site density of Cu
8.971e12 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 3.048e17 m^2/(mol*s)
"""
)