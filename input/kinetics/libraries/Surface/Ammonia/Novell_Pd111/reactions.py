#!/usr/bin/env python
# encoding: utf-8

name = "Novell_Pd111"
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
        A = (2.78E17, 'cm^2/(mol*s)'), 
        n = 1.146,
        Ea = (104000, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""
"Ammonia Dehydrogenation over Platinum-Group Metal Surfaces. Structure, Stability, and Reactivity of Adsorbed NHx Species"
Gerard Novell-Leruth et al. J. Phys. Chem. C 2007, 111, 2, 860–868
https://doi.org/10.1021/jp064742b

This reaction used RMG's surface site density of Pd111 = 2.534E-09(mol/cm^2) to calculate the A factor.
The modified Arrhenius parameter is calculated from TABLE 4.
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 2,
    label = "NH2_X + X <=> NH_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (1.8E19, 'cm^2/(mol*s)'), 
        n = 0.783,
        Ea = (86000, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"Ammonia Dehydrogenation over Platinum-Group Metal Surfaces. Structure, Stability, and Reactivity of Adsorbed NHx Species"
Gerard Novell-Leruth et al. J. Phys. Chem. C 2007, 111, 2, 860–868
https://doi.org/10.1021/jp064742b

This reaction used RMG's surface site density of Pd111 = 2.534E-09(mol/cm^2) to calculate the A factor.
The modified Arrhenius parameter is calculated from TABLE 4.
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 3,
    label = "NH_X + X <=> N_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (8.14E17, 'cm^2/(mol*s)'), 
        n = 1.445,
        Ea = (113000, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
"Ammonia Dehydrogenation over Platinum-Group Metal Surfaces. Structure, Stability, and Reactivity of Adsorbed NHx Species"
Gerard Novell-Leruth et al. J. Phys. Chem. C 2007, 111, 2, 860–868
https://doi.org/10.1021/jp064742b

This reaction used RMG's surface site density of Pd111 = 2.534E-09(mol/cm^2) to calculate the A factor.
The modified Arrhenius parameter is calculated from TABLE 4.
""",
    metal = "Pd",
    facet = "111",
)