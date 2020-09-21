#!/usr/bin/env python
# encoding: utf-8

name = "API_Intra_R_Add_Endocyclic/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 809,
    label = "Rn;multiplebond_intra;radadd_intra",
    kinetics = ArrheniusEP(
        A = (1e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
)

