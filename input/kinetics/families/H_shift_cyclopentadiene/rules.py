#!/usr/bin/env python
# encoding: utf-8

name = "H_shift_cyclopentadiene/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "cyclopentadiene",
    kinetics = ArrheniusEP(
        A = (5.06e+07, 's^-1'),
        n = 1.74,
        alpha = 0,
        E0 = (24.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""AG Vandeputte, CBS-QB3""",
    longDesc = """Rate taken from H shift in ethyleneCPD""",
)

