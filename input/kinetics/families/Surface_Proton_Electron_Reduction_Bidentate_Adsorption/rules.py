#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Proton_Electron_Reduction_Beta/rules"
shortDesc = u""
longDesc = u"""
Surface adsorption of a single radical forming a single bond to the surface site
"""

entry(
    index = 1,
    label = "Adsorbate1;Adsorbate2;Proton",
    kinetics = SurfaceChargeTransfer(
        alpha = 0.25,
        A = (2.5e15, 'm^5/(mol^2*s)'), # pre-exponential factor estimate 10^11 s^-1 * 2.5e5 m^2/mol / 1000 m^3/mol H+
        n = 0, # temperature coeff, 0 default
        V0 = None, # Reference potential
        Ea = (50, 'kJ/mol'), # activation energy at the reversible potential
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        electrons = -1, # electron stochiometric coeff
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u""""""
)
