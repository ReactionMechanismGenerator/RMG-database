#!/usr/bin/env python
# encoding: utf-8

name = "amine_COH_HCN/rules"
shortDesc = u""
longDesc = u"""

"""

entry(
    index=0,
    label="amine_COH;HCN",
    kinetics=ArrheniusEP(A=(5e+10, 'cm^3/(mol*s)'), n=0, alpha=0, E0=(0, 'kcal/mol')),
    rank=0,
    shortDesc=u"""Default""",
)
