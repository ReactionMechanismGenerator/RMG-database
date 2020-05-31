#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia"
shortDesc = u""
longDesc = u"""
Based on "Modeling ammonia oxidation over a Pt (533) surface"
https://doi.org/10.1016/j.susc.2011.08.014
"""

entry(
    index = 1,
    label = "N_Pt + N_Pt <=> N2 + Pt + Pt",
    kinetics = SurfaceArrhenius(
        A=(4.966e+16, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (100.0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 10 in "Modeling ammonia oxidation over a Pt (533) surface"
https://doi.org/10.1016/j.susc.2011.08.014

A factor from paper / surface site density of Pt
2e11 1/s / 2.483e-05 mol/m^2 = 4.966e+16 m^2/(mol*s)
"""
)

entry(
    index = 2,
    label = "N_Pt + O_Pt <=> NO_Pt + Pt",
    kinetics = SurfaceArrhenius(
        A=(4.966e+20, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (85.0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 11 in "Modeling ammonia oxidation over a Pt (533) surface"
https://doi.org/10.1016/j.susc.2011.08.014

A factor from paper / surface site density of Pt
2e15 1/s / 2.483e-05 mol/m^2 = 4.966e+16 m^2/(mol*s)
"""
)

entry(
    index = 3,
    label = "NO_Pt + N_Pt <=> N2O + Pt + Pt",
    kinetics = SurfaceArrhenius(
        A=(2.7313e+19, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (101.0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
A factor from Reaction 13a in "Modeling ammonia oxidation over a Pt (533) surface"
https://doi.org/10.1016/j.susc.2011.08.014

A factor from paper / surface site density of Pt
1.1e14 1/s / 2.483e-05 mol/m^2 = 2.7313e+19 m^2/(mol*s)

Ea from "N2O formation and dissociation during ammonia combustion: A combined DFT and experimental study"
https://doi.org/10.1016/j.proci.2016.05.004
"""
)

entry(
    index = 4,
    label = "N2O + Pt111 <=> N2 + O_Pt111",
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
"""
)

entry(
    index = 5,
    label = "NO_Pt111 + NO_Pt111 <=> N2O + O_Pt111",
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
"""
)

# entry(
#     index = 6,
#     label = "NO_Pt100 + N_Pt100 <=> N2O + Pt100 + Pt100",
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
# """
# )

entry(
    index = 7,
    label = "N2O_Pt100 <=> N2O + Pt100",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(1e13, '1/s'),
        n = 0.,
        Ea = (29.0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""N2O Dissociation""",
    longDesc = u"""
    Ea from
    "N2O formation and dissociation during ammonia combustion: A combined DFT and experimental study"
    https://doi.org/10.1016/j.proci.2016.05.004

    A made up
    """
)
