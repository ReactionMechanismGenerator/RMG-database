#!/usr/bin/env python
# encoding: utf-8

name = "benzene_amino_to_cyclic_aldehyde_and_imine/rules"
shortDesc = u""
longDesc = u"""
"""

entry(
    index=0,
    label="benzen_amino",
    kinetics=ArrheniusEP(A=(6e+13, 's^-1'), n=0, alpha=0, E0=(40, 'kcal/mol')),
    rank=0,
    shortDesc=u"""Default""",
)

