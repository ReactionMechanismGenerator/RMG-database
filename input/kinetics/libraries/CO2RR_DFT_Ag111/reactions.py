#!/usr/bin/env python
# encoding: utf-8

name = "CO2RR_DFT_Ag111"
shortDesc = u"Calculated by Manish Kumar Kothakonda at Northeastern University"
longDesc = u"""
Place holder for long description
"""


entry(
    index = 1,
    label = "CO2X + proton <=> CO2HX",
    degeneracy = 1,
    kinetics = SurfaceChargeTransfer(
        alpha = 0.62, # charge transfer coeff
        A = (2.5e10, 'm^3/(mol*s)'), # pre-exponential factor estimate 10^11 s^-1 * 2.5e5 m^2/mol / 1000 m^3/mol H+
        n = 0, # temperature coeff
        V0 = (-0.0, 'V'), # reference potential
        Ea = (0.75, 'eV/molecule'), # activation energy
        Tmin = (298, 'K'),
        Tmax = (3000, 'K'),
        electrons = 1, # electron stochiometric coeff
    ),
    shortDesc = u"""CO2RR_Ag111""",
    longDesc = u"""Calculated by Manish Kumar Kothakonda""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 2,
    label = "CO2X + proton <=> CHO2X",
    kinetics = SurfaceChargeTransfer(
        alpha = 0.46, # charge transfer coeff
        A = (2.5e10, 'm^3/(mol*s)'), # pre-exponential factor estimate 10^11 s^-1 * 2.5e5 m^2/mol / 1000 m^3/mol H+
        n = 0, # temperature coeff
        V0 = (-0.0, 'V'), # reference potential
        Ea = (1.25, 'eV/molecule'), # activation energy
        Tmin = (298, 'K'),
        Tmax = (3000, 'K'),
        electrons = 1, # electron stochiometric coeff
    ),
    shortDesc = u"""CO2RR_Ag111""",
    longDesc = u"""Calculated by Manish Kumar Kothakonda""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 3,
    label = "CO2HX + proton <=> OCX + H2O",
    kinetics = SurfaceChargeTransfer(
        alpha = 0.36, # charge transfer coeff
        A = (2.5e10, 'm^3/(mol*s)'), # pre-exponential factor estimate 10^11 s^-1 * 2.5e5 m^2/mol / 1000 m^3/mol H+
        n = 0, # temperature coeff
        V0 = (-0.0, 'V'), # reference potential
        Ea = (0.25, 'eV/molecule'), # activation energy
        Tmin = (298, 'K'),
        Tmax = (3000, 'K'),
        electrons = 1, # electron stochiometric coeff
    ),
    shortDesc = u"""CO2RR_Ag111""",
    longDesc = u"""Calculated by Manish Kumar Kothakonda""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 4,
    label = "CO2HX + proton <=> HCOOHX",
    kinetics = SurfaceChargeTransfer(
        alpha = 0.62, # charge transfer coeff
        A = (2.5e10, 'm^3/(mol*s)'), # pre-exponential factor estimate 10^11 s^-1 * 2.5e5 m^2/mol / 1000 m^3/mol H+
        n = 0, # temperature coeff
        V0 = (-0.0, 'V'), # reference potential
        Ea = (2.40, 'eV/molecule'), # activation energy
        Tmin = (298, 'K'),
        Tmax = (3000, 'K'),
        electrons = 1, # electron stochiometric coeff
    ),
    shortDesc = u"""CO2RR_Ag111""",
    longDesc = u"""Calculated by Manish Kumar Kothakonda""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 5,
    label = "CHO2X + proton <=> HCOOHX",
    kinetics = SurfaceChargeTransfer(
        alpha = 0.12, # charge transfer coeff
        A = (2.5e10, 'm^3/(mol*s)'), # pre-exponential factor estimate 10^11 s^-1 * 2.5e5 m^2/mol / 1000 m^3/mol H+
        n = 0, # temperature coeff
        V0 = (-0.0, 'V'), # reference potential
        Ea = (2.64, 'eV/molecule'), # activation energy
        Tmin = (298, 'K'),
        Tmax = (3000, 'K'),
        electrons = 1, # electron stochiometric coeff
    ),
    shortDesc = u"""CO2RR_Ag111""",
    longDesc = u"""Calculated by Manish Kumar Kothakonda""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 6,
    label = "OCX + proton <=> CHOX",
    kinetics = SurfaceChargeTransfer(
        alpha = 0.49, # charge transfer coeff
        A = (2.5e10, 'm^3/(mol*s)'), # pre-exponential factor estimate 10^11 s^-1 * 2.5e5 m^2/mol / 1000 m^3/mol H+
        n = 0, # temperature coeff
        V0 = (-0.0, 'V'), # reference potential
        Ea = (0.45, 'eV/molecule'), # activation energy
        Tmin = (298, 'K'),
        Tmax = (3000, 'K'),
        electrons = 1, # electron stochiometric coeff
    ),
    shortDesc = u"""CO2RR_Ag111""",
    longDesc = u"""Calculated by Manish Kumar Kothakonda""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 7,
    label = "CHOX + proton <=> XCHOH",
    kinetics = SurfaceChargeTransfer(
        alpha = 0.71, # charge transfer coeff
        A = (2.5e10, 'm^3/(mol*s)'), # pre-exponential factor estimate 10^11 s^-1 * 2.5e5 m^2/mol / 1000 m^3/mol H+
        n = 0, # temperature coeff
        V0 = (-0.0, 'V'), # reference potential
        Ea = (2.14, 'eV/molecule'), # activation energy
        Tmin = (298, 'K'),
        Tmax = (3000, 'K'),
        electrons = 1, # electron stochiometric coeff
    ),
    shortDesc = u"""CO2RR_Ag111""",
    longDesc = u"""Calculated by Manish Kumar Kothakonda""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 8,
    label = "CHOX + proton <=> CH2OX",
    kinetics = SurfaceChargeTransfer(
        alpha = 0.36, # charge transfer coeff
        A = (2.5e10, 'm^3/(mol*s)'), # pre-exponential factor estimate 10^11 s^-1 * 2.5e5 m^2/mol / 1000 m^3/mol H+
        n = 0, # temperature coeff
        V0 = (-0.0, 'V'), # reference potential
        Ea = (2.60, 'eV/molecule'), # activation energy
        Tmin = (298, 'K'),
        Tmax = (3000, 'K'),
        electrons = 1, # electron stochiometric coeff
    ),
    shortDesc = u"""CO2RR_Ag111""",
    longDesc = u"""Calculated by Manish Kumar Kothakonda""",
    metal = "Ag",
    facet = "111",
)

entry(
    index = 9,
    label = "XCH2OH + proton <=> XCH2 + H2O",
    kinetics = SurfaceChargeTransfer(
        alpha = 0.19, # charge transfer coeff
        A = (2.5e10, 'm^3/(mol*s)'), # pre-exponential factor estimate 10^11 s^-1 * 2.5e5 m^2/mol / 1000 m^3/mol H+
        n = 0, # temperature coeff
        V0 = (-0.0, 'V'), # reference potential
        Ea = (0.79, 'eV/molecule'), # activation energy
        Tmin = (298, 'K'),
        Tmax = (3000, 'K'),
        electrons = 1, # electron stochiometric coeff
    ),
    shortDesc = u"""CO2RR_Ag111""",
    longDesc = u"""Calculated by Manish Kumar Kothakonda""",
    metal = "Ag",
    facet = "111",
)
