#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Abstraction_vdW/rules"
shortDesc = u""
longDesc = u"""
A vdW double bonded species dissociatively adsorbing to the surface with double
bonds.
"""

entry(
    index = 1,
    label = "AdsorbateVdW;Adsorbate1",
    kinetics = SurfaceArrheniusBEP(
        A = (1.0e13, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.5,
        E0 = (0, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""Made up"""
)

# entry(
#     index = 2,
#     label = "O-H;O=*",
#     kinetics = SurfaceArrheniusBEP(
#         A = (1e13, 'm^2/(mol*s)'),
#         n = 0,
#         alpha = 0.65,
#         E0 = (2.3060548, 'kcal/mol'),
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     rank = 1,
#     shortDesc = u"""Default""",
#     longDesc = u"""
# Reaction 17 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
# and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d
#
# E0 is Ea_fwd - deltaE and A is made up
# """
# )