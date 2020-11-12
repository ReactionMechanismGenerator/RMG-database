#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_Fe_BEAzeolite"
shortDesc = u""
longDesc = u"""
Based primarily on 
"Kinetic Modelling of the Adsorption and Desorption of NH3 on Fe/BEA Zeolite"
https://doi.org/10.1515/zpch-2014-0607
"""
entry(
    index = 6,
    label = " NH3 + X <=> NH3_X ",
    kinetics = StickingCoefficient(
        A = 0.87,
        n = 0,
        Ea=(0, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R6""",
    longDesc = u"""
    Kinetic Modelling of the Adsorption and Desorption of NH3 on Fe/BEA Zeolite
    """,
    metal = "Fe",
)

#entry(
#    index = 15,
#    label = " NH3_X <=> NH3 + X ",
#    kinetics = SurfaceArrhenius(
#        A=(5E7, 'm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (84.9, 'kJ/mol'), #140.2-55.3, vary from 125 kJ/mol to 164kJ/mol in Lit?
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""Reverse of R6""",
#    longDesc = u"""
#    Kinetic Modelling of the Adsorption and Desorption of NH3 on Fe/BEA Zeolite
#    """,
#    metal = "Fe" ,
#)

#Non-neutral molecule encountered. Currently, RMG does not support ion chemistry
entry(
    index = 30,
    label = " NH3 + OH_X <=> NH4 + O_X ",
    kinetics =  SurfaceArrhenius(
        A=(0.87, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (0, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""R30""",
    longDesc = u"""
    Kinetic Modelling of the Adsorption and Desorption of NH3 on Fe/BEA Zeolite
    """,
    metal = "Fe" ,
)

#entry(
#    index = 31,
#    label = " NH4 + O_X <=> NH3 + OH_X ",
#    kinetics = SurfaceArrhenius(
#        A=(5E11, 'm^2/(mol*s)'),
#        n = 0.,
#        Ea = (104.9, 'kJ/mol'),  #109.6-4.7
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""Reverse of R30""",
#    longDesc = u"""
#Kinetic Modelling of the Adsorption and Desorption of NH3 on Fe/BEA Zeolite
#""",
#    metal = "Fe" ,
#)