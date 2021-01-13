#!/usr/bin/env python
# encoding: utf-8

name = "Disproportionation-Y/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 6,
    label = "Y_rad_birad_trirad_quadrad;XH_Rrad_birad",
    kinetics = ArrheniusEP(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (2000, 'cal/mol'),
        Tmin = (300, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""From NIST CH2F2 model for CHFCCF3_r423 + H_r1 <=> F_p41 + C#CC(F)(F)F_p23""",
)
