#!/usr/bin/env python
# encoding: utf-8

name = "hemiacetal_hydrolysis/rules"
shortDesc = u""
longDesc = u"""

"""

entry(
    index=0,
    label="hemiacetal",
    kinetics=ArrheniusEP(A=(3e+10, 's^-1'), n=0, alpha=0, E0=(0, 'kcal/mol')),
    rank=0,
    shortDesc=u"""Default""",
)
