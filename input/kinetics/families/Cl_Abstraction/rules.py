
#!/usr/bin/env python
# encoding: utf-8

name = "Cl_Abstraction/groups"
shortDesc = u""
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
    rank = 0,
    shortDesc = u"""NIST""",
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
    label = "Cl2;O_pri_rad",
    kinetics = ArrheniusEP(
        A = (4.21E-13, 'cm^3/(mol*s)'),
        n =2.10,
        alpha = 0,
        E0 = (1.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
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
    rank = 0,
    shortDesc = u"""Default""",
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
    rank = 0,
    shortDesc = u"""Default""",
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
    rank = 0,
    shortDesc = u"""Default""",
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
    rank = 0,
    shortDesc = u"""Default""",
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
    rank = 0,
    shortDesc = u"""Default""",
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
    rank = 0,
    shortDesc = u"""Default""",
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
    rank = 0,
    shortDesc = u"""Default""",
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
    rank = 0,
    shortDesc = u"""Default""",
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
    rank = 0,
    shortDesc = u"""Default""",
)



