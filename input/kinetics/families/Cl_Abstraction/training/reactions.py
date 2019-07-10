#!/usr/bin/env python
# encoding: utf-8

name = "Cl_Abstraction/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""

entry(
    index = 0,
    degeneracy = 2.0, # guess because there are 2 chlorines?
    label = "Cl2_r12 + H_r3 <=> HCl_p32 + Cl_p1",
    kinetics = Arrhenius(
        A = (1.43E-10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1.172, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (250, 'K'),
        Tmax = (730, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Baulch review via kinetics.NIST.gov 1981BAU/DUX """,
    longDesc = u"""
    NIST kinetics site 1981BAU/DUX (Baulch review)
    Cl2 + H. -> HCl + Cl
    T range 250-730 K
    """,
)
