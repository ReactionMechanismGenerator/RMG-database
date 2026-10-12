#!/usr/bin/env python
# encoding: utf-8

name = "Bjarne_Ni"
shortDesc = u""
longDesc = u"""
test surface mechanism: based upon Bjarne Kreitz's work:
"Quantifying the Impact of Parametric Uncertainty on Automatic Mechanism Generation for CO2 Hydrogenation on Ni(111)"
Bjarne Kreitz et al
ACS Catalysis, 2021, 1, 10, 1656–1673
"""

entry(
    index = 1,
    label = "CHX + Ni <=> CX + HX",
    kinetics = SurfaceArrhenius(
        A=(8.75E17, 'm^2/(mol*s)'),
        n = 0,
        Ea=(122500, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""Default""",
	metal = "Ni",
)

entry(
    index = 2,
    label = "CH2X + Ni <=> CHX + HX",
    kinetics = SurfaceArrhenius(
        A=(4.26E17, 'm^2/(mol*s)'),
        n = 0,
        Ea=(18900, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""Default""",
	metal = "Ni",
)

entry(
    index = 3,
    label = "CH3X + Ni <=> CH2X + HX",
    kinetics = SurfaceArrhenius(
        A=(6.1E17, 'm^2/(mol*s)'),
        n = 0,
        Ea=(55600, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""Default""",
	metal = "Ni",
)

entry(
    index = 4,
    label = "CH2X + CX <=> CHX + CHX",
    kinetics = SurfaceArrhenius(
        A=(2.33E17, 'm^2/(mol*s)'),
        n = 0,
        Ea=(66000, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""Default""",
	metal = "Ni",
)

entry(
    index = 5,
    label = "CH3X + CX <=> CH2X + CHX",
    kinetics = SurfaceArrhenius(
        A=(6.13E17, 'm^2/(mol*s)'),
        n = 0,
        Ea=(82900, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""Default""",
	metal = "Ni",
)

