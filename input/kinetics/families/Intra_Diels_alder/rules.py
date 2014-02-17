#!/usr/bin/env python
# encoding: utf-8

name = "Intra_Diels_alder/rules"
shortDesc = u""
longDesc = u"""

"""
recommended = True

entry(
    index = 1,
    label = "cyclohexene",
    group1 = "OR{cyclohexene_1inring, cyclohexene_2inring, cyclohexene_3inring, cyclohexene_4inring}",
    kinetics = ArrheniusEP(
        A = (12400000000.0, 's^-1'),
        n = 1.27,
        alpha = 0,
        E0 = (65.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""A. G. Vandeputte, value for ring opening JP10=""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Feb 10 21:39:02 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> added this entry by importing the old RMG database."""),
    ],
)

