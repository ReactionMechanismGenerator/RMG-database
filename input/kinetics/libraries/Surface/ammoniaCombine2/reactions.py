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
    label = "N_X + N_X <=> N2 + X + X",
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
"""
)

entry(
    index = 2,
    label = "N_X + O_X <=> NO_X + X",
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
"""
)

entry(
    index = 3,
    label = "NO_X + N_X <=> N2O + X + X",
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
"""
)

entry(
    index = 4,
    label = "N2O + X <=> N2 + O_X",
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
    label = "NO_X + NO_X <=> N2O + O_X + X",
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
#     label = "NO_X + N_X <=> N2O + X + X",
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
    label = "N2O_X <=> N2O + X",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(1e13, 'm^2/(mol*s)'),
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
    """
)

#https://github.com/rwest/RMG-database/commit/ac3072bc0a4779d17316a5b11ead94fb28c56aeb

entry(
    index = 8,
    label = "NH3 + X <=> NH3_X",
    kinetics = SurfaceArrhenius( #StickingCoefficient(
        A = (0.011, 'm^2/(mol*s)'),
        n = 0,
        Ea=(0, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""NH3 Surface Adsorption vdW""",
    longDesc = u"""
    Micro-kinetic modeling of NH3 decomposition on Ni and its application to solid oxide fuel cells
    Deutschmann et al
    doi: 10.1016/j.ces.2011.07.007
    This is R2
    metal = 'Ni'
    """
)


entry(
    index = 9,
    label = "NH4NO3 + X + X <=> N2O_X + H2O_X + H2O",
    kinetics = SurfaceArrhenius(  #StickingCoefficient(
        A = (1.0e-6, 'm^2/(mol*s)'),
        n = 0,
        Ea=(0, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Ammonium Nitrate Adsorption decomposition""",
    longDesc = u"""
Currently modeling this as one step, adsorbs and breaks down immediately.
The pathway is insipred by Inazu et al. 2004.  http://dx.doi.org/10.1016/j.cattod.2004.06.055
Hopefully the reverse is calculated correctly, with there being a gas phase product.
Assume N2O_X is vdw-adsorbed (because "weakly bound", and I can't figure out a Lewis structure with bonds).
For the rate, just copied Deutschmann's dissociative adsorption of N2 from above, i.e.
a fixed sticking coefficient of 1e-6.
    """
)

#https://github.com/mazeau/RMG-database/blob/surface_nitrogen_lib_broken/input/kinetics/libraries/Surface/Nitrogen/reactions.py

entry(
    index = 10,
    label = "NO_X + X <=> N_X + O_X",
    kinetics = SurfaceArrhenius(
        A = (5e20, 'cm^2/(mol*s)'),
        n = 0,
        Ea=(107.8, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""NO Dissociation""",
    longDesc = u"""
    Detailed surface reaction mechanism in a three-way catalyst
    Chatterjee, Deutschmann, Warnatz et al.
    doi: 10.1039/b101968f
    is supposedly only valid for a Pt/Rh ratio of 75%/25%
    This is R51
    metal = 'Pt'
    """
)