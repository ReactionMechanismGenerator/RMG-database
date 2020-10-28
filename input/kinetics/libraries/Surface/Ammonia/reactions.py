#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia"
shortDesc = u""
longDesc = u"""
Based primarily on "Modeling ammonia oxidation over a Pt (533) surface"
https://doi.org/10.1016/j.susc.2011.08.014
"""

entry(
    index = 1,
    label = "N_Pt + N_Pt <=> N2 + Pt + Pt",
    kinetics = SurfaceArrhenius(
        A=(1.2082e+16, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (85.0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
"Kinetics of ammonia oxidation on stepped platinum surfacesII. Simulation results"
Surface Science 576 (2005) 131–144
""",
    metal = "Pt" ,
)

entry(
    index = 2,
    label = "N_Pt + O_Pt <=> NO_Pt + Pt",
    kinetics = SurfaceArrhenius(
        A=(8.05477e+19, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (85.0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 11 in "Modeling ammonia oxidation over a Pt (533) surface"
https://doi.org/10.1016/j.susc.2011.08.014
""",
    metal = "Pt" ,
)

entry(
    index = 3,
    label = "NO_Pt + N_Pt <=> N2O + Pt + Pt",
    kinetics = SurfaceArrhenius(
        A=(4.43012e+18, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (101.0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
A factor from Reaction 13a in "Modeling ammonia oxidation over a Pt (533) surface"
https://doi.org/10.1016/j.susc.2011.08.014

Ea from "N2O formation and dissociation during ammonia combustion: A combined DFT and experimental study"
https://doi.org/10.1016/j.proci.2016.05.004
""",
    metal = "Pt" ,
)

entry(
    index = 4,
    label = "N2O + Pt <=> N2 + O_Pt",
    kinetics = SurfaceArrhenius(
        A=(1.0e18, 'm^2/(mol*s)'),
        n = 0.,
        Ea=(147.0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Ea from "N2O formation and dissociation during ammonia combustion: A combined DFT and experimental study"
https://doi.org/10.1016/j.proci.2016.05.004

A factor made up
""",
    metal = "Pt" ,
)

entry(
    index = 5,
    label = "NO_Pt + NO_Pt <=> N2O + O_Pt + Pt",
    kinetics = SurfaceArrhenius(
        A=(1.0e18, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (241.0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Ea from "NO pairing and transformation to N2O on Cu (111) and Pt (111) from first principles"
A. Bogicevic, K.C. Hass, Surf. Sci. 506 (2002) L237-L242.

A factor made up
""",
    metal = "Pt" ,
)

# entry(
#     index = 6,
#     label = "NO_Pt + N_Pt <=> N2O + Pt + Pt",
#     kinetics = SurfaceArrhenius(
#         A=(1.0e18, 'm^2/(mol*s)'),
#         n = 0.,
#         Ea = (48.0, 'kJ/mol'),
#         Tmin = (298, 'K'),
#         Tmax = (2000, 'K'),
#     ),
#     shortDesc = u"""Default""",
#     longDesc = u"""
# Ea from "N2O formation and dissociation during ammonia combustion: A combined DFT and experimental study"
# https://doi.org/10.1016/j.proci.2016.05.004

# A factor made up
# """,
#    metal = "Pt" ,
# )

entry(
    index = 7,
    label = "N2O_Pt <=> N2O + Pt",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(1e13, '1/s'),
        n = 0.,
        Ea = (29.0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""N2O Dissociation""",
    longDesc = u"""
    Ea from
    "N2O formation and dissociation during ammonia combustion: A combined DFT and experimental study"
    https://doi.org/10.1016/j.proci.2016.05.004

    A made up
    """,
    metal = "Pt" ,
)
