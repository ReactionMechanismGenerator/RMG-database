#!/usr/bin/env python
# encoding: utf-8

name = "hemiaminal_hydrolysis/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 0,
    label = "CCCCN(C)CO <=> CH2O + CCCCNC",
    degeneracy = 1.0,
    kinetics=Arrhenius(A=(1e+13, 's^-1'), n=2.0, Ea=(60, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(275, 'K'), Tmax=(350, 'K')),
    rank = 1,
    longDesc =
"""
est.
Ea is high on purpose to avoid endothermicity correction
this rate is 9.5E+07 at 313 K
""",
)
