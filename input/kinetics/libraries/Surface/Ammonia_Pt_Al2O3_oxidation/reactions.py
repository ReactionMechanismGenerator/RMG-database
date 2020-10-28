#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_Pt_Al2O3_oxidation"
shortDesc = u""
longDesc = u"""
Based primarily on Pritpal S. Dhillon, Michael P. Harold, Di Wang, Ashok Kumar, Saurabh Joshi,
Hydrothermal aging of Pt/Al2O3 monolith: 
Washcoat morphology degradation effects studied using ammonia and propylene oxidation,
Catalysis Today, Volume 320, 2019, Pages 20-29, ISSN 0920-5861,
https://doi.org/10.1016/j.cattod.2017.12.023.
"""
#Need to use  generatedSpeciesConstraints(allowSingletO2=True) in input.py

entry(
    index = 1,
    label = " NH3 + X <=> NH3_X ",
    kinetics = StickingCoefficient(
        A=1.25E1,                
        n = 0.0,
        Ea = (0, 'kJ/mol'),  #For the reverse rxn: A=2E4, Ea=106.16
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Hydrothermal aging of Pt/Al2O3 monolith: Washcoat morphology degradation effects studied using ammonia and propylene oxidation
""",
    metal = "Pt" ,
)

entry(
    index = 2,
    label = " O2 + X + X <=> O_X + O_X",
    kinetics = SurfaceArrhenius(
        A=(2.6E1, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (0, 'kJ/mol'),    
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Hydrothermal aging of Pt/Al2O3 monolith: Washcoat morphology degradation effects studied using ammonia and propylene oxidation
""",
    metal = "Pt" ,
)

#might delete this
entry(
    index = 3,
    label = " NH3_X + O_X <=> N_X + H2O + H_X ",
    kinetics = SurfaceArrhenius(
        A=(2.7E15, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (140.70, 'kJ/mol'),   
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Hydrothermal aging of Pt/Al2O3 monolith: Washcoat morphology degradation effects studied using ammonia and propylene oxidation
""",
    metal = "Pt" ,
)

entry(
    index = 4,
    label = " NO + X <=> NO_X ",
    kinetics = SurfaceArrhenius(
        A=(0.9E2, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (0, 'kJ/mol'),   
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Hydrothermal aging of Pt/Al2O3 monolith: Washcoat morphology degradation effects studied using ammonia and propylene oxidation
""",
    metal = "Pt" ,
)

entry(
    index = 5,
    label = " N_X + N_X  <=>  N2 + X + X ",
    kinetics = SurfaceArrhenius(
        A=(1.9E18, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (174, 'kJ/mol'), 
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Hydrothermal aging of Pt/Al2O3 monolith: Washcoat morphology degradation effects studied using ammonia and propylene oxidation
""",
    metal = "Pt" ,
)

entry(
    index = 6,
    label = " N_X + O_X  <=>  NO_X + X ",
    kinetics = SurfaceArrhenius(
        A=(2.2E12, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (120.32, 'kJ/mol'), 
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Hydrothermal aging of Pt/Al2O3 monolith: Washcoat morphology degradation effects studied using ammonia and propylene oxidation
""",
    metal = "Pt" ,
)

entry(
    index = 7,
    label = " N_X + NO_X   <=>  N2O + X + X ",
    kinetics = SurfaceArrhenius(
        A=(7.3E18, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (130.5, 'kJ/mol'), 
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Hydrothermal aging of Pt/Al2O3 monolith: Washcoat morphology degradation effects studied using ammonia and propylene oxidation
""",
    metal = "Pt" ,
)

entry(
    index = 8,
    label = " O_X + NO_X <=> NO2_X + X ",
    kinetics = SurfaceArrhenius(
        A=(6.4E13, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (103.4, 'kJ/mol'), 
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Hydrothermal aging of Pt/Al2O3 monolith: Washcoat morphology degradation effects studied using ammonia and propylene oxidation
""",
    metal = "Pt" ,
)

entry(
    index = 9,
    label = " NO2_X <=> NO2 + X ",
    kinetics = SurfaceArrhenius(
        A=(4E13, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (120, 'kJ/mol'), 
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
Hydrothermal aging of Pt/Al2O3 monolith: Washcoat morphology degradation effects studied using ammonia and propylene oxidation
""",
    metal = "Pt" ,
)