#!/usr/bin/env python
# encoding: utf-8

name = "hemiaminal_to_amine+aldehyde/rules"
shortDesc = u""
longDesc = u"""
"""

entry(
    index=0,
    label="hemiaminal",
    kinetics=ArrheniusEP(A=(1e+11, 's^-1'), n=0, alpha=0, E0=(0, 'cal/mol')),
    rank=0,
    shortDesc=u"""Default""",
)
