#!/usr/bin/env python
# encoding: utf-8

name = "amine_COH_HCN/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index=0,
    label="iC3H6NHCH2OH + HCN <=> iC3H6NHCH2CN + H2O",
    degeneracy=1.0,
    # kinetics=Arrhenius(A=(283.024, 'cm^3/(mol*s)'), n=2.54221, Ea=(232.434, 'kJ/mol'),
    #                    T0=(1, 'K'), Tmin=(250, 'K'), Tmax=(500, 'K')),
    kinetics=Arrhenius(A=(1e10, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(250, 'K'), Tmax=(500, 'K')),
    rank=5,
    longDesc=
    u"""
    Calculated at CBS-QB3 + PCM water
    """,
)
