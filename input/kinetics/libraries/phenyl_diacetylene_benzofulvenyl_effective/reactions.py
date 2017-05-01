#!/usr/bin/env python
# encoding: utf-8

name = "phenyl_diacetylene_benzofulvenyl_effective"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "i2_trans <=> i3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.813e+11, 's^-1'), n=0.685, Ea=(58.342, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Effective rate from i2 of phenyl+diacetylene PES directly to benzofulvenyl. Effective rate is determined by the rate-limiting 
step, which is trans to cis-isomerization of i2. The subsequent ring closure step is at least 3 orders of magnitude faster, 
and is therefore neglected in effected rate.
""",
)

