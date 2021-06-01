#!/usr/bin/env python
# encoding: utf-8

name = "Arevalo_Pt111"
shortDesc = u""
longDesc = u"""
This library is built to import training reactions, based on:
"First-principles study of nitric oxide oxidation on Pt(111) versus Pt overlayer on 3d transition metals"
Ryan Lacdao Arevalo, Mary Clare Sison Escaño, and Hideaki Kasai. J. Vac. Sci. Technol. A 33, 021402 (2015)
https://doi.org/10.1116/1.4903225
"""

entry(
    index = 1,
    label = "O2 + X + X <=> O_X + O_X",
    kinetics = StickingCoefficient(
        A = 0.1768,
        n = 0,
        Ea = (0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""O2 Surface_Adsorption_Dissociative""",
    longDesc = u"""
"First-principles study of nitric oxide oxidation on Pt(111) versus Pt overlayer on 3d transition metals"
Ryan Lacdao Arevalo, Mary Clare Sison Escaño, and Hideaki Kasai. J. Vac. Sci. Technol. A 33, 021402 (2015)
https://doi.org/10.1116/1.4903225

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = ((3.19E7 /bar) / s) * (2.483E-9 mol/cm2) * sqrt(2 * pi * 32 g/mol * molar gas constant * 298 kelvin)

This is R1 in Table 1
""",
	metal = "Pt",
    facet = "111",
)

entry(
    index = 2,
    label = "NO + X <=> NO_X",
    kinetics = StickingCoefficient(
        A = 1.4917E-6,
        n = 0,
        Ea = (0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""
"First-principles study of nitric oxide oxidation on Pt(111) versus Pt overlayer on 3d transition metals"
Ryan Lacdao Arevalo, Mary Clare Sison Escaño, and Hideaki Kasai. J. Vac. Sci. Technol. A 33, 021402 (2015)
https://doi.org/10.1116/1.4903225

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = ((2.78E2 /bar) / s) * (2.483E-9 mol/cm2) * sqrt(2 * pi * 30 g/mol * molar gas constant * 298 kelvin)

This is R3 in Table 1
""",
	metal = "Pt",
    facet = "111",
)

entry(
    index = 3,
    label = "NO_X + O_X <=> NO2_X + X",
    kinetics = SurfaceArrhenius(
        A = (1.776E22, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (115788, 'J/mol'),  
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"First-principles study of nitric oxide oxidation on Pt(111) versus Pt overlayer on 3d transition metals"
Ryan Lacdao Arevalo, Mary Clare Sison Escaño, and Hideaki Kasai. J. Vac. Sci. Technol. A 33, 021402 (2015)
https://doi.org/10.1116/1.4903225

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 300K) = 4.41E13(1/s)/2.483E-9(mol/cm^2) = 1.776E22 cm^2/(mol*s)
Ea = 1.2eV * 96490J/eV mol = 115788J/mol

This is R5 in Table 1
""",
	metal = "Pt",
    facet = "111",
)

entry(
    index = 4,
    label = "NO2 + X  <=> NO2_X",
    kinetics = StickingCoefficient(
        A = 1.4884E-6,
        n = 0,
        Ea = (0, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Adsorption_Single""",
    longDesc = u"""
"First-principles study of nitric oxide oxidation on Pt(111) versus Pt overlayer on 3d transition metals"
Ryan Lacdao Arevalo, Mary Clare Sison Escaño, and Hideaki Kasai. J. Vac. Sci. Technol. A 33, 021402 (2015)
https://doi.org/10.1116/1.4903225

This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = ((2.24E2 /bar) / s) * (2.483E-9 mol/cm2) * sqrt(2 * pi * 46 g/mol * molar gas constant * 298 kelvin)

This is R7 in Table 1
""",
	metal = "Pt",
    facet = "111",
)