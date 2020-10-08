#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_Pt_oxidation"
shortDesc = u""
longDesc = u"""
Based primarily on "Modeling ammonia oxidation over a Pt (533) surface"
10.1016/j.susc.2011.08.014
"""
#need to find binding energy of Pt 533 surface!!
entry(
    index = 1,
    label = " NH3_X <=> NH3 + X ",
    kinetics = SurfaceArrhenius(
        A=(2E10, 'm^2/(mol*s)'), #104.122E20    2x10^10 (1/s)
        n = 0.0,
        Ea = (69, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
M. Rafti, J.L. Vicente, A. Albesa, A. Scheibe, R. Imbihl
"Modeling ammonia oxidation over a Pt (533) surface"
Surf. Sci., 606 (1–2) (2012), pp. 12-20, 10.1016/j.susc.2011.08.014
"""
)

entry(
    index = 2,
    label = " NH3_X +O_X <=> NH2_X + OH_X ",
    kinetics = SurfaceArrhenius(
        A=(3.7E11, 'm^2/(mol*s)'), #3.7x10^11 (1/s)
        n = 0.0,
        Ea = (55, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
M. Rafti, J.L. Vicente, A. Albesa, A. Scheibe, R. Imbihl
"Modeling ammonia oxidation over a Pt (533) surface"
Surf. Sci., 606 (1–2) (2012), pp. 12-20, 10.1016/j.susc.2011.08.014
"""
)

#Reverse reactino of index= 2
#entry(
#    index = 3,
#    label = " NH2_X + OH_X <=> NH3_X + O_X  ",
#    kinetics = SurfaceArrhenius(
#        A=(3E11, 'm^2/(mol*s)'), #3x10^11 (1/s)
#        n = 0.0,
#        Ea = (22, 'kJ/mol'),
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""
#M. Rafti, J.L. Vicente, A. Albesa, A. Scheibe, R. Imbihl
#"Modeling ammonia oxidation over a Pt (533) surface"
#Surf. Sci., 606 (1–2) (2012), pp. 12-20, 10.1016/j.susc.2011.08.014
#"""
#)

entry(
    index = 4,
    label = " NH2_X +O_X <=> NH_X + OH_X ",
    kinetics = SurfaceArrhenius(
        A=(6.1E12, 'm^2/(mol*s)'), #6.1x10^12 (1/s)
        n = 0.0,
        Ea = (87, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
M. Rafti, J.L. Vicente, A. Albesa, A. Scheibe, R. Imbihl
"Modeling ammonia oxidation over a Pt (533) surface"
Surf. Sci., 606 (1–2) (2012), pp. 12-20, 10.1016/j.susc.2011.08.014
"""
)

#entry(
#    index = 5,
#    label = " NH_X + OH_X <=> NH2_X +O_X ",
#    kinetics = SurfaceArrhenius(
#        A=(3E11, 'm^2/(mol*s)'), #3x10^11 (1/s)
#        n = 0.0,
#        Ea = (128, 'kJ/mol'),
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""
#M. Rafti, J.L. Vicente, A. Albesa, A. Scheibe, R. Imbihl
#"Modeling ammonia oxidation over a Pt (533) surface"
#Surf. Sci., 606 (1–2) (2012), pp. 12-20, 10.1016/j.susc.2011.08.014
#"""
#)

entry(
    index = 6,
    label = " NH_X +O_X <=> N_X + OH_X ",
    kinetics = SurfaceArrhenius(
        A=(1E13, 'm^2/(mol*s)'), #1x10^13 (1/s)
        n = 0.0,
        Ea = (84, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
M. Rafti, J.L. Vicente, A. Albesa, A. Scheibe, R. Imbihl
"Modeling ammonia oxidation over a Pt (533) surface"
Surf. Sci., 606 (1–2) (2012), pp. 12-20, 10.1016/j.susc.2011.08.014
"""
)

#Reverse reaction of index= 6
#entry(
#    index = 7,
#    label = " N_X + OH_X <=> NH_X +O_X  ",
#    kinetics = SurfaceArrhenius(
#        A=(8.368E22, 'm^2/(mol*s)'), #3x10^11 (1/s)
#        n = 0.0,
#        Ea = (57, 'kJ/mol'),
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""
#M. Rafti, J.L. Vicente, A. Albesa, A. Scheibe, R. Imbihl
#"Modeling ammonia oxidation over a Pt (533) surface"
#Surf. Sci., 606 (1–2) (2012), pp. 12-20, 10.1016/j.susc.2011.08.014
#"""
#)

entry(
    index = 8,
    label = " NH3_X + OH_X <=> NH2_X + H2O + X  ",
    kinetics = SurfaceArrhenius(
        A=(2.697E28, 'm^2/(mol*s)'), #3.9x10^12 (1/s)
        n = 0.0,
        Ea = (73, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
M. Rafti, J.L. Vicente, A. Albesa, A. Scheibe, R. Imbihl
"Modeling ammonia oxidation over a Pt (533) surface"
Surf. Sci., 606 (1–2) (2012), pp. 12-20, 10.1016/j.susc.2011.08.014
"""
)

entry(
    index = 9,
    label = " NH2_X + OH_X <=> NH_X + H2O + X  ",
    kinetics = SurfaceArrhenius(
        A=(3.4E12, 'm^2/(mol*s)'), #3.4x10^12 (1/s)
        n = 0.0,
        Ea = (22, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
M. Rafti, J.L. Vicente, A. Albesa, A. Scheibe, R. Imbihl
"Modeling ammonia oxidation over a Pt (533) surface"
Surf. Sci., 606 (1–2) (2012), pp. 12-20, 10.1016/j.susc.2011.08.014
"""
)

entry(
    index = 10,
    label = " NH_X + OH_X <=> N_X + H2O + X  ",
    kinetics = SurfaceArrhenius(
        A=(5.1E11, 'm^2/(mol*s)'), #5.1x10^11 (1/s)
        n = 0.0,
        Ea = (22, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
M. Rafti, J.L. Vicente, A. Albesa, A. Scheibe, R. Imbihl
"Modeling ammonia oxidation over a Pt (533) surface"
Surf. Sci., 606 (1–2) (2012), pp. 12-20, 10.1016/j.susc.2011.08.014
"""
)

entry(
    index = 11,
    label = " N_X + N_X  <=> X + X + N2 ",
    kinetics = SurfaceArrhenius(
        A=(7.550E24, 'm^2/(mol*s)'), #2x10^11 (1/s)
        n = 0.0,
        Ea = (100, 'kJ/mol'), 
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
M. Rafti, J.L. Vicente, A. Albesa, A. Scheibe, R. Imbihl
"Modeling ammonia oxidation over a Pt (533) surface"
Surf. Sci., 606 (1–2) (2012), pp. 12-20, 10.1016/j.susc.2011.08.014
"""
)

entry(
    index = 12,
    label = " N_X + O_X  <=> NO_X + X ",
    kinetics = SurfaceArrhenius(
        A=(2E15, 'm^2/(mol*s)'), #2x10^15 (1/s)
        n = 0.0,
        Ea = (85, 'kJ/mol'), 
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
M. Rafti, J.L. Vicente, A. Albesa, A. Scheibe, R. Imbihl
"Modeling ammonia oxidation over a Pt (533) surface"
Surf. Sci., 606 (1–2) (2012), pp. 12-20, 10.1016/j.susc.2011.08.014
"""
)

#Reverse reaction of index=13
#entry(
#    index = 13,
#    label = " NO_X + X <=> N_X + O_X  ",
#    kinetics = SurfaceArrhenius(
#        A=(2E15, 'm^2/(mol*s)'), #2x10^15 (1/s)
#        n = 0.0,
#        Ea = (100, 'kJ/mol'), 
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""Default""",
#    longDesc = u"""
#M. Rafti, J.L. Vicente, A. Albesa, A. Scheibe, R. Imbihl
#"Modeling ammonia oxidation over a Pt (533) surface"
#Surf. Sci., 606 (1–2) (2012), pp. 12-20, 10.1016/j.susc.2011.08.014
#"""
#)

entry(
    index = 14,
    label = " NO_X <=> NO + X ",
    kinetics = SurfaceArrhenius(
        A=(8E14, 'm^2/(mol*s)'), #8x10^14 (1/s) 
        n = 0.,
        Ea = (163, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
M. Rafti, J.L. Vicente, A. Albesa, A. Scheibe, R. Imbihl
"Modeling ammonia oxidation over a Pt (533) surface"
Surf. Sci., 606 (1–2) (2012), pp. 12-20, 10.1016/j.susc.2011.08.014
"""
)

entry(
    index = 15,
    label = " NO_X + N_X  <=> N2O + X + X ",
    kinetics = SurfaceArrhenius(
        A=(1.1E14, 'm^2/(mol*s)'), #1.1x10^14 (1/s)
        n = 0.0,
        Ea = (155, 'kJ/mol'), 
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Default""",
    longDesc = u"""
M. Rafti, J.L. Vicente, A. Albesa, A. Scheibe, R. Imbihl
"Modeling ammonia oxidation over a Pt (533) surface"
Surf. Sci., 606 (1–2) (2012), pp. 12-20, 10.1016/j.susc.2011.08.014
"""
)

