#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Addition_Single_vdW/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 11,
    label = "COOH* + Cu5 <=> CO2_2* + H*",
    degeneracy = 2,
    kinetics = SurfaceArrhenius(
        A = (2.3626e13, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (28.3644741, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 11 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d
"""
)

entry(
    index = 17,
    label = "CO2* + H* <=> HCOO* + Cu5",
    degeneracy = 2,
    kinetics = SurfaceArrhenius(
        A = (3.658e13, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (20.0626768, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 17 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d
"""
)

entry(
    index = 20,
    label = "HCOOH* + H* <=> CH3O2_2* + Cu5",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (6.244e14, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (23.9829699, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 20 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d
"""
)

entry(
    index = 23,
    label = "CH3O2* + Cu5 <=> CH2O* + OH*",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (1.001e13, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (17.0648055, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 23 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d
"""
)

entry(
    index = 24,
    label = "CH2O* + H* <=> CH3O* + Cu5",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (1.815e13, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (5.53453152, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 24 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d
"""
)

entry(
    index = 31,
    label = "CH2O_2* + H* <=> CH2OH* + Cu5",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (9.518e14, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (18.9096494, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 31 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d
"""
)
