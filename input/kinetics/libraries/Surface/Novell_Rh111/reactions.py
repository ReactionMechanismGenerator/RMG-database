#!/usr/bin/env python
# encoding: utf-8

name = "Novell_Rh111"
shortDesc = u""
longDesc = u"""
This library is built to import training reactions, based on:
"Ammonia Dehydrogenation over Platinum-Group Metal Surfaces. Structure, Stability, and Reactivity of Adsorbed NHx Species"
Gerard Novell-Leruth et al. J. Phys. Chem. C 2007, 111, 2, 860–868
https://doi.org/10.1021/jp064742b
"""

entry(
    index = 1,
    label = "NH3_X + X <=> NH2_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (1.31E23, 'cm^2/(mol*s)'), 
        n = -0.791,
        Ea = (100000, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""
"Ammonia Dehydrogenation over Platinum-Group Metal Surfaces. Structure, Stability, and Reactivity of Adsorbed NHx Species"
Gerard Novell-Leruth et al. J. Phys. Chem. C 2007, 111, 2, 860–868
https://doi.org/10.1021/jp064742b

This reaction used RMG's surface site density of Rh111 = 2.656E-9(mol/cm^2) to calculate the A factor.
The modified Arrhenius parameter is calculated from TABLE 4.
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 2,
    label = "NH2_X + X <=> NH_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (1.23E19, 'cm^2/(mol*s)'), 
        n = 0.902,
        Ea = (84000, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"Ammonia Dehydrogenation over Platinum-Group Metal Surfaces. Structure, Stability, and Reactivity of Adsorbed NHx Species"
Gerard Novell-Leruth et al. J. Phys. Chem. C 2007, 111, 2, 860–868
https://doi.org/10.1021/jp064742b

This reaction used RMG's surface site density of Rh111 = 2.656E-9(mol/cm^2) to calculate the A factor.
The modified Arrhenius parameter is calculated from TABLE 4.
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 3,
    label = "NH_X + X <=> N_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (1.1E19, 'cm^2/(mol*s)'), 
        n = 0.965,
        Ea = (98000, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"Ammonia Dehydrogenation over Platinum-Group Metal Surfaces. Structure, Stability, and Reactivity of Adsorbed NHx Species"
Gerard Novell-Leruth et al. J. Phys. Chem. C 2007, 111, 2, 860–868
https://doi.org/10.1021/jp064742b

This reaction used RMG's surface site density of Rh111 = 2.656E-9(mol/cm^2) to calculate the A factor.
The modified Arrhenius parameter is calculated from TABLE 4.
""",
    metal = "Rh",
    facet = "111",
)