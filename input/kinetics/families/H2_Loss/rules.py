#!/usr/bin/env python
# encoding: utf-8

name = "H2_Loss/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "Di-H-ene",
    kinetics = ArrheniusEP(
        A = (4.73e+9, 's^-1'),
        n = 0.797,
        alpha = 0,
        E0 = (17.176, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2200, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Based on V. V. Kislov, N. I. Islamova, A. M. Kolker, S. H. Lin, and A. M. Mebel;
Hydrogen Abstraction Acetylene Addition and Diels-Alder Mechanisms of PAH Formation: A Detailed Study Using First Principles Calculations; 
J. Chem. Theory Comput. 2005, 1, 908-924.""",
)

