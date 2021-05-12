#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Proton_Electron_Reduction_Beta_vdW/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label = "CO2X + H <=> CO2HX",
    degeneracy = 1,
    kinetics = SurfaceChargeTransfer(
        alpha = 0.29, # charge transfer coeff
        A = (2.5e10, 'm^3/(mol*s)'), # pre-exponential factor estimate 10^11 s^-1 * 2.5e5 m^2/mol / 1000 m^3/mol H+
        n = 0, # temperature coeff
        V0 = (-0.19, 'V'), # reference potential
        Ea = (1.00, 'eV/molecule'), # activation energy
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        electrons = -1, # electron stochiometric coeff 
    ),
    shortDesc = u"""https://doi.org/10.1016/j.cattod.2017.01.050""",
    longDesc = u"""
""",
    metal = "Cu",
    facet = "111",
    site = "",
    rank = 5,
)

entry(
    index = 2,
    label = "CO2X + H <=> CO2HX",
    degeneracy = 1,
    kinetics = SurfaceChargeTransfer(
        alpha = 0.29, # charge transfer coeff
        A = (2.5e10, 'm^3/(mol*s)'), # pre-exponential factor estimate 10^11 s^-1 * 2.5e5 m^2/mol / 1000 m^3/mol H+
        n = 0, # temperature coeff
        V0 = (-0.50, 'V'), # reference potential
        Ea = (0.90, 'eV/molecule'), # activation energy
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        electrons = -1, # electron stochiometric coeff 
    ),
    shortDesc = u"""https://doi.org/10.1016/j.cattod.2017.01.050""",
    longDesc = u"""
""",
    metal = "Cu",
    facet = "111",
    site = "",
    rank = 5,
)

entry(
    index = 3,
    label = "N2X + H <=> HNNX",
    degeneracy = 1,
    kinetics = SurfaceChargeTransfer(
        A = (2.5e10, 'm^3/(mol*s)'), # pre-exponential factor estimate 10^11 s^-1 * 2.5e5 m^2/mol / 1000 m^3/mol H+
        n = 0, # temperature coeff
        V0 = (0.0, 'V'), # reference potential
        Ea = (1.46, 'eV/molecule'), # activation energy
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        electrons = -1, # electron stochiometric coeff 
    ),
    shortDesc = u"""https://pubs.rsc.org/en/content/getauthorversionpdf/c8cy01845f Table 1""",
    longDesc = u"""
""",
    metal = "Pt",
    facet = "111",
    site = "",
    rank = 5,
)
