#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_Ru_MgAl2O2"
shortDesc = u""
longDesc = u"""
Based primarily on "Surface Science Based Microkinetic Analysis of Ammonia Synthesis
over Ruthenium Catalysts"
https://doi.org/10.1006/jcat.2000.2857
"""

entry(
    index = 1,
    label = " N2 + X + X <=>  N_X + N_X ",
    kinetics = StickingCoefficient(
        A=2.0689E-2,  #A=2.8X10^4 (bar^-1)(s^-1)
        n = 0.,
        Ea = (33, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface science based microkinetic analysis of ammonia synthesis over ruthenium catalysts"
Dahl S., Sehested J., Jacobsen C.J.H., Tornqvist E., Chorkendorff I.
(2000)  Journal of Catalysis,  192  (2) , pp. 391-399
""",
    metal = "Ru" ,
)

#Reverse reaction of index = 1, reconsider the value of A
#entry(
#    index = 2,
#    label = " N_X + N_X  <=> X + X + N2 ",
#    kinetics = SurfaceArrhenius(
#        A=(5.4506E27, 'm^2/(mol*s)'), #A=2.9x10^12 (s^-1)
#        n = 0,
#        Ea = (145, 'kJ/mol'),  
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""
#"Surface science based microkinetic analysis of ammonia synthesis over ruthenium catalysts"
#Dahl S., Sehested J., Jacobsen C.J.H., Tornqvist E., Chorkendorff I.
#(2000)  Journal of Catalysis,  192  (2) , pp. 391-399
#""",
#    metal = "Ru" ,
#)

entry(
    index = 3,
    label = " H2 + X + X <=> H_X + H_X ",
    kinetics = SurfaceArrhenius(  #Check it's StickingCoefficient or SurfaceArrhenius
        A=(1.9531E-12,'m^2/(mol*s)'), #A=1.2x10^-5(bar^-1) 
        n = 0.,
        Ea = (-82, 'kJ/mol'), # Negative value??
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface science based microkinetic analysis of ammonia synthesis over ruthenium catalysts"
Dahl S., Sehested J., Jacobsen C.J.H., Tornqvist E., Chorkendorff I.
(2000)  Journal of Catalysis,  192  (2) , pp. 391-399
""",
    metal = "Ru" ,
)


entry(
    index = 4,
    label = " NH3_X <=>  X + NH3  ",
    kinetics = SurfaceArrhenius(
        A=(8.5653E15,'m^2/(mol*s)'),# 1.8866E5, 8.5653E15 this value of A can't run, rmgpy.exceptions.ReactionError: Couldn't find the adsorbate!
          #2.8x10^7bar very different from Ru catalyst...?
        n = 0.,
        Ea = (106, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface science based microkinetic analysis of ammonia synthesis over ruthenium catalysts"
Dahl S., Sehested J., Jacobsen C.J.H., Tornqvist E., Chorkendorff I.
(2000)  Journal of Catalysis,  192  (2) , pp. 391-399
""",
    metal = "Ru" ,
)

entry(
    index = 5,
    label = " N_X + H_X <=> NH_X + X ",
    kinetics = SurfaceArrhenius(
        A=(1.0645E-3, 'm^2/(mol*s)'), #A=5.3x10^-2 (no unit show) very different from Ru catalyst...?
        n = 0.,
        Ea = (-18, 'kJ/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface science based microkinetic analysis of ammonia synthesis over ruthenium catalysts"
Dahl S., Sehested J., Jacobsen C.J.H., Tornqvist E., Chorkendorff I.
(2000)  Journal of Catalysis,  192  (2) , pp. 391-399
""",
    metal = "Ru" ,
)

entry(
    index = 6,
    label = " NH_X + H_X <=> NH2_X + X ",
    kinetics = SurfaceArrhenius(
        A=(0.82, 'm^2/(mol*s)'),  #no unit
        n = 0,
        Ea = (20, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface science based microkinetic analysis of ammonia synthesis over ruthenium catalysts"
Dahl S., Sehested J., Jacobsen C.J.H., Tornqvist E., Chorkendorff I.
(2000)  Journal of Catalysis,  192  (2) , pp. 391-399
""",
    metal = "Ru" ,
)

entry(
    index = 7,
    label = " NH2_X + H_X <=> NH3_X + X ",
    kinetics = SurfaceArrhenius(
        A=(0.26, 'm^2/(mol*s)'), #no unit
        n = 0,
        Ea = (20, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface science based microkinetic analysis of ammonia synthesis over ruthenium catalysts"
Dahl S., Sehested J., Jacobsen C.J.H., Tornqvist E., Chorkendorff I.
(2000)  Journal of Catalysis,  192  (2) , pp. 391-399
""",
    metal = "Ru" ,
)

