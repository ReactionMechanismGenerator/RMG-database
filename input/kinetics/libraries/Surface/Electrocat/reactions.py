#!/usr/bin/env python
# encoding: utf-8

name = "Electrocat"
shortDesc = u""
longDesc = u"""
"""

entry(
    index = 1,
    label = "H + e + X <=> HX",
    kinetics = SurfaceChargeTransfer(
        A = (2.5e14, 'm^3/(mol*s)'), # pre-exponential factor estimate 10^11 s^-1 * 2.5e5 m^2/mol / 1000 m^3/mol H+
        V0 = (0.0, 'V'), # reference potential
        Ea = (87, 'kJ/mol'), # activation energy
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        ne = -1, # electron stochiometric coeff 
    ),
    shortDesc = u"""Default""",
    longDesc = u"""R1""",
	metal = "Cu",
    facet = "111", 
)

# entry(
#     index = 2,
#     label = "H + H + e + e <=> H2",
#     kinetics = SurfaceChargeTransfer(
#         A = (1e15, 'm^6/(mol*s)'),
#         V0 = (0.0, 'V'), # reference potential
#         Ea = (0.0, 'eV/molecule'), # activation energy
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#         ne = -1, # electron stochiometric coeff 
#     ),
#     shortDesc = u"""Default""",
#     longDesc = u"""R1""",
# 	metal = "Pt",
# )