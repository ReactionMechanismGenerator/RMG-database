#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Proton__Reduction_Beta/rules"
shortDesc = u""
longDesc = u"""
Surface adsorption of a single radical forming a single bond to the surface site
"""

# entry(
#     index = 0,
#     label = "Adsorbate;Proton",
#     kinetics = SurfaceChargeTransfer(
#         alpha = 0.25,
#         A = (2.5e10, 'm^3/(mol*s)'), # pre-exponential factor estimate 10^11 s^-1 * 2.5e5 m^2/mol / 1000 m^3/mol H+
#         n = 0, # temperature coeff, 0 default
#         V0 = None, # Reference potential
#         Ea = (100, 'kJ/mol'), # activation energy at the reversible potential
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#         electrons = -1, # electron stochiometric coeff
#     ),
#     rank = 0,
#     shortDesc = u"""Default""",
#     longDesc = u""""""
# )

entry(
    index = 1,
    label = "COX;Proton",
    kinetics = SurfaceChargeTransfer(
        alpha = 0.25,
        A = (2.5e10, 'm^3/(mol*s)'), # pre-exponential factor estimate 10^11 s^-1 * 2.5e5 m^2/mol / 1000 m^3/mol H+
        n = 0, # temperature coeff, 0 default
        V0 = None, # Reference potential
        Ea = (40, 'kJ/mol'), # activation energy at the reversible potential
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        electrons = -1, # electron stochiometric coeff
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u""""""
)

entry(
    index = 2,
    label = "OCX;Proton",
    kinetics = SurfaceChargeTransfer(
        alpha = 0.25,
        A = (2.5e10, 'm^3/(mol*s)'), # pre-exponential factor estimate 10^11 s^-1 * 2.5e5 m^2/mol / 1000 m^3/mol H+
        n = 0, # temperature coeff, 0 default
        V0 = None, # Reference potential
        Ea = (20, 'kJ/mol'), # activation energy at the reversible potential
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        electrons = -1, # electron stochiometric coeff
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u""""""
)

entry(
    index = 3,
    label = "OOX;Proton",
    kinetics = SurfaceChargeTransfer(
        alpha = 0.25,
        A = (2.5e10, 'm^3/(mol*s)'), # pre-exponential factor estimate 10^11 s^-1 * 2.5e5 m^2/mol / 1000 m^3/mol H+
        n = 0, # temperature coeff, 0 default
        V0 = None, # Reference potential
        Ea = (10, 'kJ/mol'), # activation energy at the reversible potential
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        electrons = -1, # electron stochiometric coeff
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u""""""
)

entry(
    index = 4,
    label = "CCX;Proton",
    kinetics = SurfaceChargeTransfer(
        alpha = 0.25,
        A = (2.5e10, 'm^3/(mol*s)'), # pre-exponential factor estimate 10^11 s^-1 * 2.5e5 m^2/mol / 1000 m^3/mol H+
        n = 0, # temperature coeff, 0 default
        V0 = None, # Reference potential
        Ea = (40, 'kJ/mol'), # activation energy at the reversible potential
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        electrons = -1, # electron stochiometric coeff
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u""""""
)

entry(
    index = 5,
    label = "NNX;Proton",
    kinetics = SurfaceChargeTransfer(
        alpha = 0.25,
        A = (2.5e10, 'm^3/(mol*s)'), # pre-exponential factor estimate 10^11 s^-1 * 2.5e5 m^2/mol / 1000 m^3/mol H+
        n = 0, # temperature coeff, 0 default
        V0 = None, # Reference potential
        Ea = (10, 'kJ/mol'), # 
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        electrons = -1, # electron stochiometric coeff
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u""""""
)

entry(
    index = 6,
    label = "NOX;Proton",
    kinetics = SurfaceChargeTransfer(
        alpha = 0.25,
        A = (2.5e10, 'm^3/(mol*s)'), # pre-exponential factor estimate 10^11 s^-1 * 2.5e5 m^2/mol / 1000 m^3/mol H+
        n = 0, # temperature coeff, 0 default
        V0 = None, # Reference potential
        Ea = (20, 'kJ/mol'), # 
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        electrons = -1, # electron stochiometric coeff
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u""""""
)

entry(
    index = 7,
    label = "ONX;Proton",
    kinetics = SurfaceChargeTransfer(
        alpha = 0.25,
        A = (2.5e10, 'm^3/(mol*s)'), # pre-exponential factor estimate 10^11 s^-1 * 2.5e5 m^2/mol / 1000 m^3/mol H+
        n = 0, # temperature coeff, 0 default
        V0 = None, # Reference potential
        Ea = (20, 'kJ/mol'), # 
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        electrons = -1, # electron stochiometric coeff
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u""""""
)