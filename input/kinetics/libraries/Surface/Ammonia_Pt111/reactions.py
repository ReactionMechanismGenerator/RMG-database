#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_Pt111"
shortDesc = u""
longDesc = u"""
Based primarily on 
"Ammonia Dissociation on Pt(100), Pt(111), and Pt(211): A Comparative Density Functional Theory Study"
W. K. Offermans, A. P. J. Jansen, R. A. van Santen, G. Novell-Leruth, J. M. Ricart, and J. Pérez-Ramírez
The Journal of Physical Chemistry C 2007 111 (47), 17551-17557
https://doi.org/10.1021/jp073083f
"""

#The unit of Pre Factor is [Hz]!
#Kinetic parameters at 300 K for the dissociation of NHx, Ea is zero point energy corrected
entry(
    index = 1,
    label = " NH3_X + X <=> NH2_X + H_X ",
    kinetics = SurfaceArrhenius(
        A=(8.6E11, 'm^2/(mol*s)'), #The value is for NH3_X(rot/vib), for NH3_X(vib), A=5.6E11
        n = 0.0,
        Ea = (93, 'kJ/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Ammonia Dissociation on Pt(100), Pt(111), and Pt(211): A Comparative Density Functional Theory Study
""",
    metal = "Pt" ,
)

entry(
    index = 2,
    label = " NH2_X + X <=> NH_X + H_X ",
    kinetics = SurfaceArrhenius(
        A=(5E12, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (110, 'kJ/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Ammonia Dissociation on Pt(100), Pt(111), and Pt(211): A Comparative Density Functional Theory Study
""",
    metal = "Pt" ,
)

entry(
    index = 3,
    label = " NH_X + X <=> N_X + H_X ",
    kinetics = SurfaceArrhenius(
        A=(7.2E12, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (118, 'kJ/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Ammonia Dissociation on Pt(100), Pt(111), and Pt(211): A Comparative Density Functional Theory Study
""",
    metal = "Pt" ,
)

#Kinetic parameters at 300 K of the oxidation of NHx by Oads
entry(
    index = 4,
    label = " NH3_X +O_X <=> NH2_X + OH_X ",
    kinetics = SurfaceArrhenius(
        A=(1.2E12, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (42, 'kJ/mol'),    
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Ammonia Dissociation on Pt(100), Pt(111), and Pt(211): A Comparative Density Functional Theory Study
""",
    metal = "Pt" ,
)

entry(
    index = 5,
    label = " NH2_X +O_X <=> NH_X + OH_X ",
    kinetics = SurfaceArrhenius(
        A=(6.1E12, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (87, 'kJ/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Ammonia Dissociation on Pt(100), Pt(111), and Pt(211): A Comparative Density Functional Theory Study
""",
    metal = "Pt" ,
)

entry(
    index = 6,
    label = " NH_X +O_X <=> N_X + OH_X ",
    kinetics = SurfaceArrhenius(
        A=(7.6E12, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (84, 'kJ/mol'), 
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Ammonia Dissociation on Pt(100), Pt(111), and Pt(211): A Comparative Density Functional Theory Study
""",
    metal = "Pt" ,
)

#Kinetic parameters at 300 K of the oxidation of NHx by OHads
entry(
    index = 7,
    label = " NH3_X + OH_X <=> NH2_X + H2O_X  ",
    kinetics = SurfaceArrhenius(
        A=(1.6E11, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (73, 'kJ/mol'),   
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Ammonia Dissociation on Pt(100), Pt(111), and Pt(211): A Comparative Density Functional Theory Study
""",
    metal = "Pt" ,
)

entry(
    index = 8,
    label = " NH2_X + OH_X <=> NH_X + H2O_X  ",
    kinetics = SurfaceArrhenius(
        A=(3.5E12, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (22, 'kJ/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Ammonia Dissociation on Pt(100), Pt(111), and Pt(211): A Comparative Density Functional Theory Study
""",
    metal = "Pt" ,
)

entry(
    index = 9,
    label = " NH_X + OH_X <=> N_X + H2O_X  ",
    kinetics = SurfaceArrhenius(
        A=(5.1E11, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (35, 'kJ/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Ammonia Dissociation on Pt(100), Pt(111), and Pt(211): A Comparative Density Functional Theory Study
""",
    metal = "Pt" , ,
)

