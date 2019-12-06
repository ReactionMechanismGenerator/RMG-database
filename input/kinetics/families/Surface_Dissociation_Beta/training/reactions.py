#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_Beta/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 29,
    label = "HCO* + H* <=> HCOH* + Cu",
    degeneracy = 4,
    kinetics = SurfaceArrhenius(
        A = (8.97112, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (20.9850987, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 29 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/c s200055d
"""
)
