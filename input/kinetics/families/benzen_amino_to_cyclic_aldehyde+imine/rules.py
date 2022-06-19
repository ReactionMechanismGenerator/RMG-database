#!/usr/bin/env python
# encoding: utf-8

name = "benzen_amino_to_cyclic_aldehyde+imine/rules"
shortDesc = u""
longDesc = u"""

"""

entry(
    index=0,
    label="benzen_amino",
    kinetics=ArrheniusEP(A=(6e+20, 's^-1'), n=0, alpha=0, E0=(40000, 'cal/mol')),
    rank=0,
    shortDesc=u"""Default""",
)
