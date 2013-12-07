#!/usr/bin/env python
# encoding: utf-8

name = "intra_NO2_ONO_conversion/rules"
shortDesc = u""
longDesc = u"""

"""
recommended = True

entry(
    index = 1,
    label = "RNO2",
    group1 = 
"""
1 *1 Cs 0 {2,S}
2 *2 N5d 0 {1,S} {3,S} {4,D}
3 *3 Os 0 {2,S}
4    Od 0 {2,D}
""",
    kinetics = ArrheniusEP(
        A = (2.76e+14, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (67.0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 0,
    shortDesc = u"",
    longDesc = 
u"""

""",
    history = [
        (""),
    ],
)