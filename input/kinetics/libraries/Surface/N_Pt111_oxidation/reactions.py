#!/usr/bin/env python
# encoding: utf-8

name = "N_Pt111_oxidation"
shortDesc = u""
longDesc = u"""
Based primarily on DMa, Hanyu; Schneider, William F. (2019)
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
ACS Publications. Journal contribution. 
https://doi.org/10.1021/acscatal.8b04251.s001 
"""

#Author Imaginary prefactors of the reactions at 300K

entry(
    index = 8,
    label = " N_X + N_X  <=>  N2 + X + X ",
    kinetics = SurfaceArrhenius(
        A=(9.2E12, 'm^2/(mol*s)'), #9.2x10^12 (1/s)
        n = 0.0,
        Ea = (243.99, 'kJ/mol'), #2.53eV
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
    index = 9,
    label = " N_X + O_X  <=>  NO_X + X ",
    kinetics = SurfaceArrhenius(
        A=(8.3E12, 'm^2/(mol*s)'), #8.3x10^12 (1/s)
        n = 0.0,
        Ea = (213.13, 'kJ/mol'), #2.21eV
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
    index = 10,
    label = " NO_X   <=>  NO + X ",
    kinetics = SurfaceArrhenius(
        A=(1.3E17, 'm^2/(mol*s)'), #1.3x10^17 (1/s)
        n = 0.0,
        Ea = (184.20, 'kJ/mol'), #1.91eV
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
    index = 11,
    label = " N_X + NO_X   <=>  N2O_X +X ",
    kinetics = SurfaceArrhenius(
        A=(4.3E12, 'm^2/(mol*s)'), #4.3x10^12 (1/s)
        n = 0.0,
        Ea = (164.91, 'kJ/mol'), #1.71eV
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
    index = 12,
    label = " N2O_X <=>  N2O + X ",
    kinetics = SurfaceArrhenius(
        A=(1.4E16, 'm^2/(mol*s)'), #1.4x10^16 (1/s)
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