#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Addition_Single_vdW/rules"
shortDesc = u""
longDesc = u"""
A single bonded surface species adding to a vdW double, triple, or quadruple bonded species and adsorbing to a surface.
"""

# entry(
#     index = 1,
#     label = "AdsorbateVdW;Adsorbate1",
#     kinetics = SurfaceArrheniusBEP(
#         A = (1.0e13, 'm^2/(mol*s)'),
#         n = 0,
#         alpha = 0.5,
#         E0 = (5, 'kcal/mol'),
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     rank = 5,
#     shortDesc = u"""Default""",
#     longDesc = u"""Made up"""
# )

entry(
    index = 2,
    label = "O=C=O;H",
    kinetics = SurfaceArrheniusBEP(
        A = (3.658e13, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.31,
        E0 = (20.0626768, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 17 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

E0 is Ea
"""
)

entry(
    index = 3,
    label = "O=C;H",
    kinetics = SurfaceArrheniusBEP(
        A = (1.815e13, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.37,
        E0 = (5.53453152, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 24 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

E0 is Ea
"""
)

entry(
    index = 4,
    label = "C=O;H",
    kinetics = SurfaceArrheniusBEP(
        A = (9.518e14, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.58,
        E0 = (18.9096494, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 31 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

E0 is Ea
"""
)