#!/usr/bin/env python
# encoding: utf-8

name = "methanoate_hydrolysis/rules"
shortDesc = u""
longDesc = u"""

"""

entry(
    index=0,
    label="methanoate;H2O",
    kinetics=Arrhenius(A=(2.07329e-08, 'cm^3/(mol*s)'), n=5.04178, Ea=(166.415, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(290, 'K'), Tmax=(2000, 'K')),
    rank=0,
    shortDesc=u"""Default""",
)
