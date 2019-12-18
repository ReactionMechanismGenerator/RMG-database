#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Addition_Dangling/rules"
shortDesc = u""
longDesc = u"""
Eley Rideal mechanism for a gas phase double or triple bonded species.
"""
entry(
    index = 29,
    label = "C=O;H-*",
    kinetics = SurfaceArrheniusBEP(
        A = (8.97112, 'm^2/(mol*s)'),
        n = 0.,
        alpha = 0.54,
        E0 = (20.9850987, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 29 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

E0 is Ea
"""
)