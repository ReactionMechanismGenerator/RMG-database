#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_H_ZSM5"
shortDesc = u""
longDesc = u"""
Based primarily on "Microkinetic Modeling of the fast Selective Catalytic Reduction 
of Nitrogen oxide with ammonia on H-ZSM5 based on first principles"
T.C. Brüggemann, D.G. Vlachos, F.J. Keil
J. Catal., 283 (2011), pp. 178-191
DOI: 10.1016/j.jcat.2011.08.009
"""
entry(
    index = 15,
    label = " NH3_X <=> NH3 + X ",
    kinetics = SurfaceArrhenius(
        A=(2.084E10, '1/s'), 
        n = 0.0,
        Ea = (32.00, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Pt" ,
)

entry(
    index = 19,
    label = " HNO_X <=> HNO + X ",
    kinetics = SurfaceArrhenius(
        A=(2.084E10, '1/s'), 
        n = 0.0,
        Ea = (14.71, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Pt" ,
)

entry(
    index = 20,
    label = " HNO2_X <=> HNO2 + X ",
    kinetics = SurfaceArrhenius(
        A=(2.084E10, '1/s'), 
        n = 0.0,
        Ea = (17.66, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Pt" ,
)

entry(
    index = 21,
    label = " HNO3_X <=> HNO3 + X ",
    kinetics = SurfaceArrhenius(
        A=(2.084E10, '1/s'), 
        n = 0.0,
        Ea = (19.52, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Pt" ,
)

entry(
    index = 22,
    label = " NH2OH_X <=> NH2OH + X ",
    kinetics = SurfaceArrhenius(
        A=(2.084E10, '1/s'), 
        n = 0.0,
        Ea = (35.68, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Pt" ,
)

entry(
    index = 23,
    label = " NH2NO_X <=> NH2NO + X ",
    kinetics = SurfaceArrhenius(
        A=(2.084E10, '1/s'), 
        n = 0.0,
        Ea = (25.43, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Pt" ,
)

entry(
    index = 24,
    label = " NH2NO2_X <=> NH2NO2 + X ",
    kinetics = SurfaceArrhenius(
        A=(2.084E10, '1/s'), 
        n = 0.0,
        Ea = (25.69, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Pt" ,
)

entry(
    index = 25,
    label = " NO2_X  <=> NO2 + X ",
    kinetics = SurfaceArrhenius(
        A = (2.084E10, '1/s'),
        n = 0,
        Ea=(8.24, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""R24 oxidation""",
    longDesc = u"""""",
    metal = 'Pt',
)

entry(
    index = 26,
    label = " NH3_X + NO2 <=> NH2OH_X + NO ",
    kinetics = SurfaceArrhenius(
        A = (1.599E7, '1/s'),
        n = 0,
        Ea=(39.13, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = 'Pt',
)

entry(
    index = 27,
    label = " HNO_X + NO2 <=> HNO2_X + NO ",
    kinetics = SurfaceArrhenius(
        A=(2.150E9, '1/s'), 
        n = 0.0,
        Ea = (6.23, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Pt" ,
)

entry(
    index = 28,
    label = " HNO3_X + NO <=> HNO2_X + NO2 ",
    kinetics = SurfaceArrhenius(
        A=(5.902E7, '1/s'), 
        n = 0.0,
        Ea = (21.46, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Pt" ,
)