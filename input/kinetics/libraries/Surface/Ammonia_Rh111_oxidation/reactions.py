#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_Rh111_oxidation"
shortDesc = u""
longDesc = u"""
Based primarily on Popa, C.; van Santen, R.; Jansen, A. 
"Density-functional theory study of NHx oxidation and reverse reactions on the Rh (111) surface." 
J. Phys. Chem. C 2007, 111, 9839– 9852.
https://doi.org/10.1021/jp071072g
"""
# top + hcp -> bridge + top
entry(
    index = 1,
    label = " NH3_X +O_X <=> NH2_X + OH_X ",
    kinetics = SurfaceArrhenius(
        A=(1.7E11, 'm^2/(mol*s)'), #0.17x10^13 (1/s)
        n = 0.0,
        Ea = (92.58, 'kJ/mol'),   #0.96eV
        Tmin = (100, 'K'),
        Tmax = (1000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Density-functional theory study of NHx oxidation and reverse reactions on the Rh (111) surface.
""",
    metal = "Rh" ,
)

# brigde + fcc -> hcp + top
entry(
    index = 2,
    label = " NH2_X +O_X <=> NH_X + OH_X ",
    kinetics = SurfaceArrhenius(
        A=(1.67E13, 'm^2/(mol*s)'), #1.67x10^13 (1/s)
        n = 0.0,
        Ea = (71.37, 'kJ/mol'),   #0.96eV
        Tmin = (100, 'K'),
        Tmax = (1000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Density-functional theory study of NHx oxidation and reverse reactions on the Rh (111) surface.
""",
    metal = "Rh" ,
)

# hcp + hcp -> hcp + top
entry(
    index = 3,
    label = " NH_X +O_X <=> N_X + OH_X ",
    kinetics = SurfaceArrhenius(
        A=(2.21E13, 'm^2/(mol*s)'), #2.21x10^13 (1/s)
        n = 0.0,
        Ea = (84.87, 'kJ/mol'),   #0.88eV
        Tmin = (100, 'K'),
        Tmax = (1000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Density-functional theory study of NHx oxidation and reverse reactions on the Rh (111) surface.
""",
    metal = "Rh" ,
)

# top + top -> bridge + top
entry(
    index = 4,
    label = " NH3_X + OH_X <=> NH2_X + H2O_X  ",
    kinetics = SurfaceArrhenius(
        A=(1.93E12, 'm^2/(mol*s)'), #1.93x10^12 (1/s)
        n = 0.0,
        Ea = (23.15, 'kJ/mol'),   #0.24eV
        Tmin = (100, 'K'),
        Tmax = (1000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Density-functional theory study of NHx oxidation and reverse reactions on the Rh (111) surface.
""",
    metal = "Rh" ,
)

# bridge + top + hcp + top
entry(
    index = 5,
    label = " NH2_X + OH_X <=> NH_X + H2O_X  ",
    kinetics = SurfaceArrhenius(
        A=(3.98E12, 'm^2/(mol*s)'), #3.98x10^12 (1/s)
        n = 0.0,
        Ea = (13.50, 'kJ/mol'),  #0.14eV
        Tmin = (100, 'K'),
        Tmax = (1000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Density-functional theory study of NHx oxidation and reverse reactions on the Rh (111) surface.
""",
    metal = "Rh" ,
)

# hcp + top -> hcp + top
entry(
    index = 6,
    label = " NH_X + OH_X <=> N_X + H2O_X  ",
    kinetics = SurfaceArrhenius(
        A=(1.2E12, 'm^2/(mol*s)'), #1.2x10^12 (1/s)
        n = 0.0,
        Ea = (22.18, 'kJ/mol'),  #0.23eV
        Tmin = (100, 'K'),
        Tmax = (1000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Density-functional theory study of NHx oxidation and reverse reactions on the Rh (111) surface.
""",
    metal = "Rh" ,
)

# hcp + fcc -> top
entry(
    index = 7,
    label = " N_X + N_X  <=>  N2_X + X ",
    kinetics = SurfaceArrhenius(
        A=(4.48E13, 'm^2/(mol*s)'), #4.48x10^13 (1/s)
        n = 0.0,
        Ea = (147.55, 'kJ/mol'), 
        Tmin = (100, 'K'),
        Tmax = (1000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Density-functional theory study of NHx oxidation and reverse reactions on the Rh (111) surface.
""",
    metal = "Rh" ,
)
