#!/usr/bin/env python
# encoding: utf-8

name = "Deutschmann2006"
shortDesc = u""
longDesc = u"""
reaction supplied by sandia 
3x3x1 k-point mesh calculations. 
H* + H2CO -> H2 + HCO*, at 298.15K 
forward free energy barrier = 1.537 eV, 
reverse free energy barrier = 0.849, 
overall reaction energy = 0.688 eV. 
forward rate constant = 6.456258e-14 /s, 
a reverse rate constant = 2.7710160e-2 /s, 
and an equilibrium constant = 2.3299245e-12. 

This was calculated by representing the H2CO and H2 as vdW adsorbates, 
i.e. their lateral translation was represented as an ideal gas with a reference area equal to the area per Cu atom on the Cu(111) surface, and their rotations were represented as rigid rotors. All other species were treated solely as harmonic oscillators.
"""

entry(
    index = 1,
    label = "H* + H2CO* -> H2* + HCO*",
    kinetics = SurfaceArrhenius(
        A = 1.599845633664351e+17,
        n = 0,
        Ea=(1.537, 'eV'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
    calculations: 
    kf = 6.456258e-14/(2.943e-9*100**2) = 2.1937675840978593e-09 m^3/mol/s
    Ea = 1.537*9.6e4 = 147,552 J/mol
    A = 2.1937675840978593e-09/(exp(-147,552/(8.3145*298))) = 1.599845633664351e+17
    """,
	metal = "Cu",
    facet="111"
)
