#!/usr/bin/env python
# encoding: utf-8

name = "intra_H_migration/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 614,
    label = "RnH;Y_rad_out;XH_out",
    kinetics = ArrheniusEP(
        A = (1e+10, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""default""",
)

entry(
    index = 615,
    label = "R2H_S;C_rad_out_single;Cs_H_out",
    kinetics = ArrheniusEP(
        A = (5.48e+08, 's^-1'),
        n = 1.62,
        alpha = 0,
        E0 = (38.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
[5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. C7H15

Checked by Paul Green.
""",
)
