#!/usr/bin/env python
# encoding: utf-8

name = "methanoate_hydrolysis/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label="BNX + H2O <=> P1 + P2",
    degeneracy=1.0,
    kinetics=Arrhenius(A=(2.07329e-08, 'cm^3/(mol*s)'), n=5.04178, Ea=(166.415, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(290, 'K'), Tmax=(2000, 'K'),
                       comment="""Fitted to 15 points; dA = *|/ 76.452, dn = +|- 0.574177, dEa = +|- 2.95278 kJ/mol"""),
    rank=5,
    shortDesc=u"""DFT""",
    longDesc=
    u"""
    xdeg1018b
    wb97xd/def2tzvp SMD water
    computed for a fragment CC(=O)OCCN, no rotors
    """,
)
