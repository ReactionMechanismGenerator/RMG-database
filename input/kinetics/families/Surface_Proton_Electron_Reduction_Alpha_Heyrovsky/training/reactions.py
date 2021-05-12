#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Proton_Electron_Reduction_Alpha/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label = "CX + H3O <=> CHX_p + H2O",
    degeneracy = 1,
    kinetics = SurfaceChargeTransfer(
        alpha = 0.06, # charge transfer coeff
        A = (2.5e10, 'm^3/(mol*s)'), # pre-exponential factor estimate 10^11 s^-1 * 2.5e5 m^2/mol / 1000 m^3/mol H+
        n = 0, # temperature coeff
        V0 = (-0.5, 'V'), # reference potential
        Ea = (0.13, 'eV/molecule'), # activation energy
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        electrons = -1, # electron stochiometric coeff 
    ),
    shortDesc = u"""https://doi.org/10.1016/j.cattod.2018.03.048""",
    longDesc = u"""Heyrovsky""",
    metal = "Pt",
    facet = "111",
    site = "",
    rank = 5,
)

entry(
    index = 2,
    label = "CHX + H3O <=> CH2X_p + H2O",
    degeneracy = 1,
    kinetics = SurfaceChargeTransfer(
        alpha = 0.05, # charge transfer coeff
        A = (2.5e10, 'm^3/(mol*s)'), # pre-exponential factor estimate 10^11 s^-1 * 2.5e5 m^2/mol / 1000 m^3/mol H+
        n = 0, # temperature coeff
        V0 = (-0.5, 'V'), # reference potential
        Ea = (0.53, 'eV/molecule'), # activation energy
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        electrons = -1, # electron stochiometric coeff 
    ),
    shortDesc = u"""https://doi.org/10.1016/j.cattod.2018.03.048""",
    longDesc = u"""Heyrovsky""",
    metal = "Pt",
    facet = "111",
    site = "",
    rank = 5,
)

entry(
    index = 3,
    label = "NX + H3O <=> HNX_p + H2O",
    degeneracy = 1,
    kinetics = SurfaceChargeTransfer(
        alpha = 0.07, # charge transfer coeff
        A = (2.5e10, 'm^3/(mol*s)'), # pre-exponential factor estimate 10^11 s^-1 * 2.5e5 m^2/mol / 1000 m^3/mol H+
        n = 0, # temperature coeff
        V0 = (-0.5, 'V'), # reference potential
        Ea = (0.09, 'eV/molecule'), # activation energy
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        electrons = -1, # electron stochiometric coeff 
    ),
    shortDesc = u"""https://doi.org/10.1016/j.cattod.2018.03.048""",
    longDesc = u"""Heyrovsky""",
    metal = "Pt",
    facet = "111",
    site = "",
    rank = 5,
)


entry(
    index = 4,
    label = "HNX + H3O <=> H2NX + H2O",
    degeneracy = 1,
    kinetics = SurfaceChargeTransfer(
        alpha = 0.64, # charge transfer coeff
        A = (2.5e10, 'm^3/(mol*s)'), # pre-exponential factor estimate 10^11 s^-1 * 2.5e5 m^2/mol / 1000 m^3/mol H+
        n = 0, # temperature coeff
        V0 = (-0.5, 'V'), # reference potential
        Ea = (0.43, 'eV/molecule'), # activation energy
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        electrons = -1, # electron stochiometric coeff 
    ),
    shortDesc = u"""https://doi.org/10.1016/j.cattod.2018.03.048""",
    longDesc = u"""Heyrovsky""",
    metal = "Pt",
    facet = "111",
    site = "",
    rank = 5,
)

entry(
    index = 5,
    label = "OX + H3O <=> HOX + H2O",
    degeneracy = 1,
    kinetics = SurfaceChargeTransfer(
        alpha = 0.02, # charge transfer coeff
        A = (2.5e10, 'm^3/(mol*s)'), # pre-exponential factor estimate 10^11 s^-1 * 2.5e5 m^2/mol / 1000 m^3/mol H+
        n = 0, # temperature coeff
        V0 = (-0.5, 'V'), # reference potential
        Ea = (0.03, 'eV/molecule'), # activation energy
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        electrons = -1, # electron stochiometric coeff 
    ),
    shortDesc = u"""https://doi.org/10.1016/j.cattod.2018.03.048""",
    longDesc = u"""Heyrovsky""",
    metal = "Pt",
    facet = "111",
    site = "",
    rank = 5,
)
