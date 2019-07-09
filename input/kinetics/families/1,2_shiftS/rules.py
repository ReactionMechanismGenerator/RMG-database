#!/usr/bin/env python
# encoding: utf-8

name = "1,2_shiftS/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "XSYJ;YJ-S2s;C-S2s",
    kinetics = ArrheniusEP(
        A = (1e+08, 's^-1'),
        n = 2,
        alpha = 0,
        E0 = (40, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

