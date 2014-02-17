#!/usr/bin/env python
# encoding: utf-8

name = "1,4_Linear_birad_scission/rules"
shortDesc = u""
longDesc = u"""

"""
recommended = True

entry(
    index = 1,
    label = "RJJ",
    group1 = 
"""
1 *1 R 1 {2,{S,D}}
2 *2 R 0 {1,{S,D}} {3,S}
3 *3 R 0 {2,S} {4,{S,D}}
4 *4 R 1 {3,{S,D}}
""",
    kinetics = ArrheniusEP(
        A = (5000000000000.0, 's^-1'),
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

