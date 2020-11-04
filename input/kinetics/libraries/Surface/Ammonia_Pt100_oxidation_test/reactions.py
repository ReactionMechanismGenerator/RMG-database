#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_Pt100_oxidation_test"
shortDesc = u""
longDesc = u"""
Based primarily on "Pt(100)-Catalyzed Ammonia Oxidation Studied by DFT: Mechanism and Microkinetics"
Gerard Novell-Leruth, Josep M. Ricart, and Javier Pérez-Ramírez
The Journal of Physical Chemistry C 2008 112 (35), 13554-13562
DOI: 10.1021/jp802489y
"""
#This paper contain other model such as O2,OH and H2O surface reaction, NOx surface reaction
#The pre-exponential factors were calculated at 500 K.
entry(
    index = 1,
    label = " NH3 + X <=> NH3_X ",
    kinetics = StickingCoefficient(
        A=2.3E3,                #2.3×10^3 Pa-1
        n = 0.0,
        Ea = (0, 'kJ/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
"Pt(100)-Catalyzed Ammonia Oxidation Studied by DFT: Mechanism and Microkinetics"
Gerard Novell-Leruth, Josep M. Ricart, and Javier Pérez-Ramírez
The Journal of Physical Chemistry C 2008 112 (35), 13554-13562
DOI: 10.1021/jp802489y
""",
    metal = "Pt" ,
)

entry(
    index = 2,
    label = " NH3_X +O_X <=> NH2_X + OH_X ",
    kinetics = SurfaceArrhenius(
        A=(1.5E11, 'm^2/(mol*s)'), #s^-1
        n = 0.0,
        Ea = (12, 'kJ/mol'),    
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
"Pt(100)-Catalyzed Ammonia Oxidation Studied by DFT: Mechanism and Microkinetics"
Gerard Novell-Leruth, Josep M. Ricart, and Javier Pérez-Ramírez
The Journal of Physical Chemistry C 2008 112 (35), 13554-13562
DOI: 10.1021/jp802489y
""",
    metal = "Pt" ,
)

entry(
    index = 3,
    label = " NH2_X +O_X <=> NH_X + OH_X ",
    kinetics = SurfaceArrhenius(
        A=(2.5E12, 'm^2/(mol*s)'), #s^-1
        n = 0.0,
        Ea = (0, 'kJ/mol'),   
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
"Pt(100)-Catalyzed Ammonia Oxidation Studied by DFT: Mechanism and Microkinetics"
Gerard Novell-Leruth, Josep M. Ricart, and Javier Pérez-Ramírez
The Journal of Physical Chemistry C 2008 112 (35), 13554-13562
DOI: 10.1021/jp802489y
""",
    metal = "Pt" ,
)

entry(
    index = 4,
    label = " NH_X +O_X <=> N_X + OH_X ",
    kinetics = SurfaceArrhenius(
        A=(2.1E12, 'm^2/(mol*s)'), #s^-1 #Similar to Pt211
        n = 0.0,
        Ea = (0, 'kJ/mol'),  #why 0
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
"Pt(100)-Catalyzed Ammonia Oxidation Studied by DFT: Mechanism and Microkinetics"
Gerard Novell-Leruth, Josep M. Ricart, and Javier Pérez-Ramírez
The Journal of Physical Chemistry C 2008 112 (35), 13554-13562
DOI: 10.1021/jp802489y
""",
    metal = "Pt" ,
)

entry(
    index = 5,
    label = " NH3_X + OH_X <=> NH2_X + H2O_X  ",
    kinetics = SurfaceArrhenius(
        A=(9.1E11, 'm^2/(mol*s)'), #s^-1
        n = 0.0,
        Ea = (59, 'kJ/mol'),   
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
"Pt(100)-Catalyzed Ammonia Oxidation Studied by DFT: Mechanism and Microkinetics"
Gerard Novell-Leruth, Josep M. Ricart, and Javier Pérez-Ramírez
The Journal of Physical Chemistry C 2008 112 (35), 13554-13562
DOI: 10.1021/jp802489y
""",
    metal = "Pt" ,
)

entry(
    index = 6,
    label = " NH2_X + OH_X <=> NH_X + H2O_X  ",
    kinetics = SurfaceArrhenius(
        A=(1.2E15, 'm^2/(mol*s)'), #s^-1
        n = 0.0,
        Ea = (83, 'kJ/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
"Pt(100)-Catalyzed Ammonia Oxidation Studied by DFT: Mechanism and Microkinetics"
Gerard Novell-Leruth, Josep M. Ricart, and Javier Pérez-Ramírez
The Journal of Physical Chemistry C 2008 112 (35), 13554-13562
DOI: 10.1021/jp802489y
""",
    metal = "Pt" ,
)

entry(
    index = 7,
    label = " NH_X + OH_X <=> N_X + H2O_X  ",
    kinetics = SurfaceArrhenius(
        A=(6.7E12, 'm^2/(mol*s)'), #s^-1
        n = 0.0,
        Ea = (30, 'kJ/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
"Pt(100)-Catalyzed Ammonia Oxidation Studied by DFT: Mechanism and Microkinetics"
Gerard Novell-Leruth, Josep M. Ricart, and Javier Pérez-Ramírez
The Journal of Physical Chemistry C 2008 112 (35), 13554-13562
DOI: 10.1021/jp802489y
""",
    metal = "Pt" ,
)

entry(
    index = 8,
    label = " N_X + N_X  <=>  N2 + X + X ",
    kinetics = SurfaceArrhenius(
        A=(2.4E12, 'm^2/(mol*s)'), #s^-1
        n = 0.0,
        Ea = (0, 'kJ/mol'), 
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
"Pt(100)-Catalyzed Ammonia Oxidation Studied by DFT: Mechanism and Microkinetics"
Gerard Novell-Leruth, Josep M. Ricart, and Javier Pérez-Ramírez
The Journal of Physical Chemistry C 2008 112 (35), 13554-13562
DOI: 10.1021/jp802489y
""",
    metal = "Pt" ,
)

entry(
    index = 9,
    label = " N_X + O_X  <=>  NO_X + X ",
    kinetics = SurfaceArrhenius(
        A=(2.4E12, 'm^2/(mol*s)'), #s^-1
        n = 0.0,
        Ea = (2, 'kJ/mol'), 
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
"Pt(100)-Catalyzed Ammonia Oxidation Studied by DFT: Mechanism and Microkinetics"
Gerard Novell-Leruth, Josep M. Ricart, and Javier Pérez-Ramírez
The Journal of Physical Chemistry C 2008 112 (35), 13554-13562
DOI: 10.1021/jp802489y
""",
    metal = "Pt" ,
)

entry(
    index = 10,
    label = " NO_X   <=>  NO + X ",
    kinetics = SurfaceArrhenius(
        A=(1.4E17, 'm^2/(mol*s)'), #s^-1
        n = 0.0,
        Ea = (209, 'kJ/mol'), #similar to Pt211
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
"Pt(100)-Catalyzed Ammonia Oxidation Studied by DFT: Mechanism and Microkinetics"
Gerard Novell-Leruth, Josep M. Ricart, and Javier Pérez-Ramírez
The Journal of Physical Chemistry C 2008 112 (35), 13554-13562
DOI: 10.1021/jp802489y
""",
    metal = "Pt" ,
)

entry(
    index = 11,
    label = " N_X + NO_X   <=>  N2O_X +X ",
    kinetics = SurfaceArrhenius(
        A=(2.9E12, 'm^2/(mol*s)'), #s^-1
        n = 0.0,
        Ea = (58, 'kJ/mol'), 
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
"Pt(100)-Catalyzed Ammonia Oxidation Studied by DFT: Mechanism and Microkinetics"
Gerard Novell-Leruth, Josep M. Ricart, and Javier Pérez-Ramírez
The Journal of Physical Chemistry C 2008 112 (35), 13554-13562
DOI: 10.1021/jp802489y
""",
    metal = "Pt" ,
)

entry(
    index = 12,
    label = " N2O_X <=>  N2O + X ",
    kinetics = SurfaceArrhenius(
        A=(4.5E16, 'm^2/(mol*s)'), #s^-1
        n = 0.0,
        Ea = (15, 'kJ/mol'),   
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
"Pt(100)-Catalyzed Ammonia Oxidation Studied by DFT: Mechanism and Microkinetics"
Gerard Novell-Leruth, Josep M. Ricart, and Javier Pérez-Ramírez
The Journal of Physical Chemistry C 2008 112 (35), 13554-13562
DOI: 10.1021/jp802489y
""",
    metal = "Pt" ,
)

entry(
    index = 13,
    label = " N2_X <=>  N2 + X ",
    kinetics = SurfaceArrhenius(
        A=(1.6E15, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (30, 'kJ/mol'), 
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
"Pt(100)-Catalyzed Ammonia Oxidation Studied by DFT: Mechanism and Microkinetics"
Gerard Novell-Leruth, Josep M. Ricart, and Javier Pérez-Ramírez
The Journal of Physical Chemistry C 2008 112 (35), 13554-13562
DOI: 10.1021/jp802489y
""",
    metal = "Pt" ,
)

entry(
    index = 14,
    label = " NH3_X + X  <=>  NH2_X + H_X ",
    kinetics = SurfaceArrhenius(
        A=(4.4E11, 'm^2/(mol*s)'), #s^-1
        n = 0.0,
        Ea = (90, 'kJ/mol'), 
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
"Pt(100)-Catalyzed Ammonia Oxidation Studied by DFT: Mechanism and Microkinetics"
Gerard Novell-Leruth, Josep M. Ricart, and Javier Pérez-Ramírez
The Journal of Physical Chemistry C 2008 112 (35), 13554-13562
DOI: 10.1021/jp802489y
""",
    metal = "Pt" ,
)

entry(
    index = 15,
    label = " NH2_X + X  <=>  NH_X + H_X ",
    kinetics = SurfaceArrhenius(
        A=(9.3E12, 'm^2/(mol*s)'), #s^-1
        n = 0.0,
        Ea = (107, 'kJ/mol'), 
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
"Pt(100)-Catalyzed Ammonia Oxidation Studied by DFT: Mechanism and Microkinetics"
Gerard Novell-Leruth, Josep M. Ricart, and Javier Pérez-Ramírez
The Journal of Physical Chemistry C 2008 112 (35), 13554-13562
DOI: 10.1021/jp802489y
""",
    metal = "Pt" ,
)

entry(
    index = 16,
    label = " NH_X + X  <=>  N_X + H_X ",
    kinetics = SurfaceArrhenius(
        A=(6.1E12, 'm^2/(mol*s)'), #s^-1
        n = 0.0,
        Ea = (64, 'kJ/mol'), 
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
"Pt(100)-Catalyzed Ammonia Oxidation Studied by DFT: Mechanism and Microkinetics"
Gerard Novell-Leruth, Josep M. Ricart, and Javier Pérez-Ramírez
The Journal of Physical Chemistry C 2008 112 (35), 13554-13562
DOI: 10.1021/jp802489y
""",
    metal = "Pt" ,
)