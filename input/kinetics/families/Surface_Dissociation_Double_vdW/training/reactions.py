#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_Double_vdW/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 9,
    label = "CO* + O* <=> CO2* + Cu4",
    degeneracy = 2,
    kinetics = SurfaceArrhenius(
        A=(1.195e12, 'm^2/(mol*s)'),
        n = 0.,
        Ea=(14.9893562, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 9 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d
"""
)

entry(
    index = 35,
    label = "HCOOH* + Cu4 <=> HCOH* + O*",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(4.828e11, 'm^2/(mol*s)'),
        n = 0.,
        Ea=(57.65137, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 35 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d
"""
)
