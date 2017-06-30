#!/usr/bin/env python
# encoding: utf-8

name = "intra_NO2_ONO_conversion/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "RNO2",
    kinetics = ArrheniusEP(
        A = (2.76e+14, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
        comment = '\n\nDegeneracy not recalculated\n\nConverted to training reaction from rate rule: RNO2',
    ),
    rank = 0,
    longDesc = 
u"""
Degeneracy not recalculated

Converted to training reaction from rate rule: RNO2
""",
)

