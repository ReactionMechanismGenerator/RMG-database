#!/usr/bin/env python
# encoding: utf-8

name = "Cl_Abstraction/groups"
shortDesc = u"Abstraction of a Chlorine atom"
longDesc = u"""
"""


#entry(
#    index = 560,
#    label = "Cl2;C_Chloro",
#    kinetics = ArrheniusEP(
#        A = (9.13E-13, 'cm^3/(mol*s)'),
#        n = 0,
#        alpha = 0,
#        E0 = (5.01, 'kcal/mol'),
#        Tmin = (300, 'K'),
#        Tmax = (1500, 'K'),
#    ),
#    rank = 0,
#    shortDesc = u"""NIST""",
#)
#
#
#entry(
#    index = 561,
#    label = "Cl2;C_pri_rad",
#    kinetics = ArrheniusEP(
#        A = (4.62E-15, 'cm^3/(mol*s)'),
#        n = 3.07,
#        alpha = 0,
#        E0 = (-1.929, 'kcal/mol'),
#        Tmin = (300, 'K'),
#        Tmax = (1500, 'K'),
#    ),
#    rank = 0,
#    shortDesc = u"""NIST""",
#)


entry(
    index = 562,
    label = "Cl2;H_rad",
    kinetics = ArrheniusEP(
        A = (1.43E-10, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (1.172, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Baulch review via kinetics.NIST.gov 1981BAU/DUX """,
    longDesc = u"""
    NIST kinetics site 1981BAU/DUX (Baulch review)
    Cl2 + H. -> HCl + Cl
    T range 250-730 K
    """,
)


#entry(
#    index = 563,
#    label = "Cl2;C_methyl",
#    kinetics = ArrheniusEP(
#        A = (4.78E-12, 'cm^3/(mol*s)'),
#        n = 0,
#        alpha = 0,
#        E0 = (0.47, 'kcal/mol'),
#        Tmin = (300, 'K'),
#        Tmax = (1500, 'K'),
#    ),
#    rank = 0,
#    shortDesc = u"""Default""",
#)


entry(
    index = 563,
    label = "Cl2;OH_rad",
    kinetics = ArrheniusEP(
        A = (4.21E-13, 'cm^3/(mol*s)'),
        n =2.10,
        alpha = 0,
        E0 = (1.14, 'kcal/mol'),
        Tmin = (220, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""kinetics.nist.gov 2003WAN/LIU""",
    longDesc = u"""
    OH + Cl2 -> HOCl + Cl
    T range 220-2000 K
    Wang et al 2003, Ab initio calculations.
    Added by Fariba. See her thesis http://hdl.handle.net/2047/D20213055""",
)

entry(
    index = 5630,
    label = "Cl2;OCl_rad",
    kinetics = ArrheniusEP(
        A = (4.21E-13, 'cm^3/(mol*s)'),
        n =2.10,
        alpha = 0,
        E0 = (1.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Added by Fariba. See her thesis http://hdl.handle.net/2047/D20213055""",
)

entry(
    index = 564,
    label = "Cs_Cl;Cl_rad",
    kinetics = ArrheniusEP(
        A = (4.21E-13, 'cm^3/(mol*s)'),
        n =2.10,
        alpha = 0,
        E0 = (1.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Added by Fariba. See her thesis http://hdl.handle.net/2047/D20213055""",
)

entry(
    index = 565,
    label = "X_Cl;Cl_rad",
    kinetics = ArrheniusEP(
        A = (4.21E-13, 'cm^3/(mol*s)'),
        n =2.10,
        alpha = 0,
        E0 = (1.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Added by Fariba. See her thesis http://hdl.handle.net/2047/D20213055""",
)



entry(
    index = 566,
    label = "X_Cl;Cs_rad",
    kinetics = ArrheniusEP(
        A = (4.21E-13, 'cm^3/(mol*s)'),
        n =2.10,
        alpha = 0,
        E0 = (1.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Added by Fariba. See her thesis http://hdl.handle.net/2047/D20213055""",
)


entry(
    index = 567,
    label = "Cl2;Y_rad",
    kinetics = ArrheniusEP(
        A = (4.21E-13, 'cm^3/(mol*s)'),
        n =2.10,
        alpha = 0,
        E0 = (1.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Added by Fariba. See her thesis http://hdl.handle.net/2047/D20213055""",
)
entry(
    index = 568,
    label = "X_Cl;Y_rad",
    kinetics = ArrheniusEP(
        A = (4.21E-13, 'cm^3/(mol*s)'),
        n =2.10,
        alpha = 0,
        E0 = (1.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Added by Fariba. See her thesis http://hdl.handle.net/2047/D20213055""",
)


entry(
    index = 569,
    label = "Xrad_Cl;Y_rad",
    kinetics = ArrheniusEP(
        A = (4.21E-13, 'cm^3/(mol*s)'),
        n =2.10,
        alpha = 0,
        E0 = (1.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Added by Fariba. See her thesis http://hdl.handle.net/2047/D20213055""",
)



entry(
    index = 570,
    label = "Cl2;Y_1centerbirad",
    kinetics = ArrheniusEP(
        A = (4.21E-13, 'cm^3/(mol*s)'),
        n =2.10,
        alpha = 0,
        E0 = (1.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Added by Fariba. See her thesis http://hdl.handle.net/2047/D20213055""",
)

entry(
    index = 571,
    label = "X_Cl;Y_1centerbirad",
    kinetics = ArrheniusEP(
        A = (4.21E-13, 'cm^3/(mol*s)'),
        n =2.10,
        alpha = 0,
        E0 = (1.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Added by Fariba. See her thesis http://hdl.handle.net/2047/D20213055""",
)
entry(
    index = 572,
    label = "Cs_Cl;Y_1centerbirad",
    kinetics = ArrheniusEP(
        A = (4.21E-13, 'cm^3/(mol*s)'),
        n =2.10,
        alpha = 0,
        E0 = (1.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Added by Fariba. See her thesis http://hdl.handle.net/2047/D20213055""",
)
