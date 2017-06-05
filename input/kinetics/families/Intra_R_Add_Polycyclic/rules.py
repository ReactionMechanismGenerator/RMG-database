#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_Polycyclic/rules"
shortDesc = u""
longDesc = u"""
General comments go at the top of the file,

or in a section(s) titled 'General'

.. the ID must match those in the rateLibrary AS A STRING (ie. '2' is different from '02')
"""
entry(
    index = 1,
    label = "Rn_cyclic;multiplebond_intra;radadd_intra",
    kinetics = ArrheniusEP(
        A = (1e+09, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (20, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Guess""",
)
