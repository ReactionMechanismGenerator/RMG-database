#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Abstraction/rules"
shortDesc = u""
longDesc = u"""
"""
entry(
    index = 1,
    label = "Abstracting;Donating",
    kinetics = SurfaceArrhenius(
        A = (1.0e13, 'm^2/(mol*s)'),
        n = 0,
        Ea=(10., 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
"Arrhenius preexponential values for surface recombination...reactions
are, in the SI system,... 10^13 - 10^14 m2/mol/s ...for bimolecular reactions"
from page 54 of "Silicon epitaxy"
Author:	Danilo Crippa; Daniel L Rode; Maurizio Masi
Publisher:	San Diego : Academic Press, 2001.
Series:	Semiconductors and semimetals, v. 72.

Ea made up.
    """
)

entry(
    index = 1,
    label = "Abstracting;R-H",
    kinetics = SurfaceArrhenius(
        A = (1.0e13, 'm^2/(mol*s)'),
        n = 0,
        Ea=(20., 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Made up""",
    longDesc = u"""
Totally made up by Richard to demonstrate how to define things in this file.
    """
)


