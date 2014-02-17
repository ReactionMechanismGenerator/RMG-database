#!/usr/bin/env python
# encoding: utf-8

name = "1,4_Cyclic_birad_scission/rules"
shortDesc = u""
longDesc = u"""

"""
recommended = True

entry(
    index = 1,
    label = "RJJ",
    group1 = "OR{R5JJ, R6JJ, R7JJ}",
    kinetics = ArrheniusEP(
        A = (10000000000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""AG Vandeputte estimate (should be fast)""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Feb 10 21:39:02 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> added this entry by importing the old RMG database."""),
    ],
)

