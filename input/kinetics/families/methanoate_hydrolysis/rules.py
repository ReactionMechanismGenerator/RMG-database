#!/usr/bin/env python
# encoding: utf-8

name = "methanoate_hydrolysis/rules"
shortDesc = u""
longDesc = u"""

"""

entry(
    index=0,
    label="methanoate;H2O",
    kinetics=ArrheniusEP(A=(1e+3, 'cm^3/(mol*s)'), n=0, alpha=0, E0=(0, 'kcal/mol')),
    rank=0,
    shortDesc=u"""Default""",
)
