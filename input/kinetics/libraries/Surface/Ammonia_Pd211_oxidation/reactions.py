#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_Pd211_oxidation"
shortDesc = u""
longDesc = u"""
Based primarily on "DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
https://doi.org/10.1016/j.jcat.2020.01.029
"""
entry(
    index = 1,
    label = "O2 + X + X <=> O_X + O_X",
    kinetics = SurfaceArrhenius(
        A=(1.02E13, 'cm^5/(mol^2*s)'),
        n = 0,
        Ea=(28.92, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
	metal = "Pd",
)

entry(
    index = 2,
    label = " NH3_X +O_X <=> NH2_X + OH_X ",
    kinetics = SurfaceArrhenius(
        A=(8.53E12, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (39.52, 'kJ/mol'),   
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Pd" ,
)

entry(
    index = 3,
    label = " NH2_X +O_X <=> NH_X + OH_X ",
    kinetics = SurfaceArrhenius(
        A=(1.04E13, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (104.11, 'kJ/mol'),   
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Pd" ,
)

entry(
    index = 4,
    label = " NH_X +O_X <=> N_X + OH_X ",
    kinetics = SurfaceArrhenius(
        A=(1.04E13, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (23.13, 'kJ/mol'),   
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Pd" ,
)

entry(
    index = 5,
    label = " NH3_X + OH_X <=> NH2_X + H2O_X  ",
    kinetics = SurfaceArrhenius(
        A=(8.93E12, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (70.37, 'kJ/mol'),   
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Pd" ,
)

entry(
    index = 6,
    label = " NH2_X + OH_X <=> NH_X + H2O_X  ",
    kinetics = SurfaceArrhenius(
        A=(1.04E13, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (73.26, 'kJ/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Pd" ,
)

entry(
    index = 7,
    label = " NH_X + OH_X <=> N_X + H2O_X  ",
    kinetics = SurfaceArrhenius(
        A=(1.04E13, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (41.45, 'kJ/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Pd" ,
)

entry(
    index = 8,
    label = " N_X + N_X  <=>  N2 + X + X ",
    kinetics = SurfaceArrhenius(
        A=(1.03E13, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (119.53, 'kJ/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""
""",
    metal = "Pd" ,
)

entry(
    index = 9,
    label = " N_X + O_X  <=>  NO_X + X ",
    kinetics = SurfaceArrhenius(
        A=(1.02E13, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (82.9, 'kJ/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Pd" ,
)

entry(
    index = 10,
    label = " N_X + NO_X   <=>  N2O_X + X ",
    kinetics = SurfaceArrhenius(
        A=(1.01E13, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (190.86, 'kJ/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Pd" ,
)

entry(
    index = 11,
    label = " NH3_X + X <=> NH2_X + H_X ",
    kinetics = SurfaceArrhenius(
        A=(1.04E13, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (97.36, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Pd" ,
)

entry(
    index = 12,
    label = " NH2_X + X <=> NH_X + H_X ",
    kinetics = SurfaceArrhenius(
        A=(1.03E13, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (152.30, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Pd" ,
)

entry(
    index = 13,
    label = " NH_X + X <=> N_X + H_X ",
    kinetics = SurfaceArrhenius(
        A=(1.04E13, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (118.57, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Pd" ,
)
