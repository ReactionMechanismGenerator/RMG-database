#!/usr/bin/env python
# encoding: utf-8

name = "Intra_Retro_Diels_alder_bicyclic/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "cyclohexene",
    kinetics = ArrheniusEP(
        A = (1.24e+10, 's^-1'),
        n = 1.27,
        alpha = 0,
        E0 = (65.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""A. G. Vandeputte, value for ring opening JP10=""",
)

