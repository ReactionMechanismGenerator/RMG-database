#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_Pt211_oxidation"
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
        A=2.9E16,                #2.9x10^16(1/s)
        n = 0.0,
        Ea = (0, 'kJ/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities.
"""
)

entry(
    index = 2,
    label = " NH3_X +O_X <=> NH2_X + OH_X ",
    kinetics = SurfaceArrhenius(
        A=(1E13, 'm^2/(mol*s)'), #1x10^13 (1/s)
        n = 0.0,
        Ea = (55.94, 'kJ/mol'),    #0.58eV
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities.
"""
)

entry(
    index = 3,
    label = " NH2_X +O_X <=> NH_X + OH_X ",
    kinetics = SurfaceArrhenius(
        A=(6E12, 'm^2/(mol*s)'), #6x10^12 (1/s)
        n = 0.0,
        Ea = (139.84, 'kJ/mol'),   #1.45eV
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities.
"""
)

entry(
    index = 4,
    label = " NH_X +O_X <=> N_X + OH_X ",
    kinetics = SurfaceArrhenius(
        A=(2.5E12, 'm^2/(mol*s)'), #2.5x10^12 (1/s)
        n = 0.0,
        Ea = (45.33, 'kJ/mol'),   #0.47eV
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities.
"""
)

entry(
    index = 5,
    label = " NH3_X + OH_X <=> NH2_X + H2O_X  ",
    kinetics = SurfaceArrhenius(
        A=(3.5E12, 'm^2/(mol*s)'), #3.5x10^12 (1/s)
        n = 0.0,
        Ea = (89.69, 'kJ/mol'),   #0.83eV
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities.
"""
)

entry(
    index = 6,
    label = " NH2_X + OH_X <=> NH_X + H2O_X  ",
    kinetics = SurfaceArrhenius(
        A=(8.7E11, 'm^2/(mol*s)'), #8.7x10^11 (1/s)
        n = 0.0,
        Ea = (76.19, 'kJ/mol'),  #0.79eV  #Ea is 4 times larger than Rh111_oxidation!
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities.
"""
)

entry(
    index = 7,
    label = " NH_X + OH_X <=> N_X + H2O_X  ",
    kinetics = SurfaceArrhenius(
        A=(6.8E11, 'm^2/(mol*s)'), #6.8x10^11 (1/s)
        n = 0.0,
        Ea = (81.01, 'kJ/mol'),  #0.84eV   #Ea almost 4 times larger than Rh111_oxidation!
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities.
"""
)

entry(
    index = 8,
    label = " N_X + N_X  <=>  N2 + X + X ",
    kinetics = SurfaceArrhenius(
        A=(5.3E12, 'm^2/(mol*s)'), #5.3x10^12 (1/s)
        n = 0.0,
        Ea = (113.80, 'kJ/mol'), #1.18eV
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities.
"""
)

entry(
    index = 9,
    label = " N_X + O_X  <=>  NO_X + X ",
    kinetics = SurfaceArrhenius(
        A=(9.6E11, 'm^2/(mol*s)'), #9.6x10^11 (1/s)
        n = 0.0,
        Ea = (140.80, 'kJ/mol'), #1.46eV
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities.
"""
)

entry(
    index = 10,
    label = " NO_X   <=>  NO + X ",
    kinetics = SurfaceArrhenius(
        A=(1.3E17, 'm^2/(mol*s)'), #1.3x10^17 (1/s)
        n = 0.0,
        Ea = (224.71, 'kJ/mol'), #2.33eV
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities.
"""
)

entry(
    index = 11,
    label = " N_X + NO_X   <=>  N2O_X +X ",
    kinetics = SurfaceArrhenius(
        A=(6.5E12, 'm^2/(mol*s)'), #6.5x10^12 (1/s)
        n = 0.0,
        Ea = (156.23, 'kJ/mol'), #1.62eV
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities.
"""
)

entry(
    index = 12,
    label = " N2O_X <=>  N2O + X ",
    kinetics = SurfaceArrhenius(
        A=(1.5E17, 'm^2/(mol*s)'), #1.5x10^17 (1/s)
        n = 0.0,
        Ea = (9.64, 'kJ/mol'),   #0.1eV
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities.
"""
)