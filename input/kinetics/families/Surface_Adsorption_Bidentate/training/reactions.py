#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_Bidentate/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label = "HCCH + X_3 + X_4 <=> HCCH_2X",
    kinetics = StickingCoefficient(
        A = 8.3E-1,
        n = 0,
        Ea = (0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Default""",
    longDesc = u"""
    Experimental value with single-crystal adsorption calorimetry (SCAC) for initial sticking probability:
    "Energetics and kinetics of the interaction of acetylene and ethylene with Pd{100} and Ni{100}"
    Vattuone et al
    Surface Science, 2000, 447, 1-14""",
	metal = "Pd",
)

entry(
    index = 2,
    label = "H2CCH2 + X_3 + X_4 <=> H2CCH2_2X",
    kinetics = StickingCoefficient(
        A = 6.9E-1,
        n = 0,
        Ea = (0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Default""",
    longDesc = u"""
    Experimental value with microcalorimetry for initial sticking probability:
    "Microcalorimetric study of ethylene adsorption at 300 K on Pt{100}-hex and Pt{100}-(11)"
    Yeo et al
    Journal of Molecular Catalysis A: Chemical, 1998, 131, 31-38""",
	metal = "Pt",
)

entry(
    index = 3,
    label = "H2CO + X_3 + X_4 <=> H2CO_2X",
    kinetics = StickingCoefficient(
        A = 2.0E-1,
        n = 0,
        Ea = (0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""Made up""",
	metal = "Pt",
)
