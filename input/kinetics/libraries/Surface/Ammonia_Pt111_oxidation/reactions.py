#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_Pt111_oxidation"
shortDesc = u""
longDesc = u"""
Based primarily on DMa, Hanyu; Schneider, William F. (2019)
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
ACS Publications. Journal contribution. 
https://doi.org/10.1021/acscatal.8b04251.s001 
"""

#Author Imaginary prefactors of the reactions at 300K
entry(
    index = 1,
    label = " NH3 + X <=> NH3_X ",
    kinetics = StickingCoefficient(
        A=5.2E16,                #5.2x10^16(1/s)
        n = 0.0,
        Ea = (0, 'kJ/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities.
""",
    metal = "Pt" , 
)

entry(
    index = 2,
    label = " NH3_X +O_X <=> NH2_X + OH_X ",
    kinetics = SurfaceArrhenius(
        A=(8.4E12, 'm^2/(mol*s)'), #8.4x10^12 (1/s)
        n = 0.0,
        Ea = (67.51, 'kJ/mol'),    #0.7eV
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities.
""",
    metal = "Pt" ,
)

entry(
    index = 3,
    label = " NH2_X +O_X <=> NH_X + OH_X ",
    kinetics = SurfaceArrhenius(
        A=(4.2E12, 'm^2/(mol*s)'), #4.2x10^12 (1/s)
        n = 0.0,
        Ea = (78.12, 'kJ/mol'),   #0.81eV
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities.
""",
    metal = "Pt" ,
)

entry(
    index = 4,
    label = " NH_X +O_X <=> N_X + OH_X ",
    kinetics = SurfaceArrhenius(
        A=(3.8E12, 'm^2/(mol*s)'), #3.8x10^12 (1/s)
        n = 0.0,
        Ea = (154.30, 'kJ/mol'),   #1.6eV
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities.
""",
    metal = "Pt" ,
)

entry(
    index = 5,
    label = " NH3_X + OH_X <=> NH2_X + H2O_X  ",
    kinetics = SurfaceArrhenius(
        A=(3.2E12, 'm^2/(mol*s)'), #3.2x10^12 (1/s)
        n = 0.0,
        Ea = (33.75, 'kJ/mol'),   #0.35eV
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities.
""",
    metal = "Pt" ,
)

entry(
    index = 6,
    label = " NH2_X + OH_X <=> NH_X + H2O_X  ",
    kinetics = SurfaceArrhenius(
        A=(4.7E12, 'm^2/(mol*s)'), #4.7x10^12 (1/s)
        n = 0.0,
        Ea = (0.96, 'kJ/mol'),  #0.01
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities.
""",
    metal = "Pt" ,
)

entry(
    index = 7,
    label = " NH_X + OH_X <=> N_X + H2O_X  ",
    kinetics = SurfaceArrhenius(
        A=(1.2E12, 'm^2/(mol*s)'), #1.2x10^12 (1/s)
        n = 0.0,
        Ea = (39.54, 'kJ/mol'),  #0.41eV 
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities.
""",
    metal = "Pt" ,
)
