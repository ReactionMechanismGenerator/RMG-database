#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_Rh211_oxidation"
shortDesc = u""
longDesc = u"""
Based primarily on "DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
https://doi.org/10.1016/j.jcat.2020.01.029
"""
entry(
    index = 1,
    label = "O2 + X + X <=> O_X + O_X",
    kinetics = SurfaceArrhenius(
        A=(1.00E13, 'cm^5/(mol^2*s)'),
        n = 0,
        Ea=(0, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
	metal = "Rh",
)

entry(
    index = 2,
    label = " NH3_X +O_X <=> NH2_X + OH_X ",
    kinetics = SurfaceArrhenius(
        A=(7.96E12, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (62.66, 'kJ/mol'),   
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Rh" ,
)

entry(
    index = 3,
    label = " NH2_X +O_X <=> NH_X + OH_X ",
    kinetics = SurfaceArrhenius(
        A=(1.04E13, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (143.63, 'kJ/mol'),   
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Rh" ,
)

entry(
    index = 4,
    label = " NH_X +O_X <=> N_X + OH_X ",
    kinetics = SurfaceArrhenius(
        A=(1.04E13, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (60.73, 'kJ/mol'),   
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Rh" ,
)

entry(
    index = 5,
    label = " NH3_X + OH_X <=> NH2_X + H2O_X  ",
    kinetics = SurfaceArrhenius(
        A=(8.36E12, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (91.58, 'kJ/mol'),   
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Rh" ,
)

entry(
    index = 6,
    label = " NH2_X + OH_X <=> NH_X + H2O_X  ",
    kinetics = SurfaceArrhenius(
        A=(1.04E13, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (97.36, 'kJ/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Rh" ,
)

entry(
    index = 7,
    label = " NH_X + OH_X <=> N_X + H2O_X  ",
    kinetics = SurfaceArrhenius(
        A=(1.04E13, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (85.79, 'kJ/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Rh" ,
)

entry(
    index = 8,
    label = " N_X + N_X  <=>  N2 + X + X ",
    kinetics = SurfaceArrhenius(
        A=(1.01E13, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (169.66, 'kJ/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Rh" ,
)

entry(
    index = 9,
    label = " N_X + O_X  <=>  NO_X + X ",
    kinetics = SurfaceArrhenius(
        A=(1.02E13, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (166.76, 'kJ/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Rh" ,
)

entry(
    index = 10,
    label = " N_X + NO_X   <=>  N2O_X + X ",
    kinetics = SurfaceArrhenius(
        A=(9.91E12, 'cm^2/(mol*s)'),  
        n = 0.0,
        Ea = (211.11, 'kJ/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Rh" ,
)

entry(
    index = 11,
    label = " NH3_X + X <=> NH2_X + H_X ",
    kinetics = SurfaceArrhenius(
        A=(1.03E13, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (88.68, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Rh" ,
)

entry(
    index = 12,
    label = " NH2_X + X <=> NH_X + H_X ",
    kinetics = SurfaceArrhenius(
        A=(1.04E13, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (117.60, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Rh" ,
)

entry(
    index = 13,
    label = " NH_X + X <=> N_X + H_X ",
    kinetics = SurfaceArrhenius(
        A=(1.04E13, 'cm^2/(mol*s)'), 
        n = 0.0,
        Ea = (88.68, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Rh" ,
)
