#!/usr/bin/env python
# encoding: utf-8

name = "Surface"
shortDesc = u""
longDesc = u"""
test surface mechanism:
"""
entry(
    index = 1,
    label = "O2 + Ni + Ni <=> OX + OX",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.08E8, 'cm^5/(mol^2*s)'), n=0.294, Ea=(1500.0, 'J/mol'), T0=(1, 'K')),
    longDesc = 
u"""
dissociative adsorption of O2 on Nickel to yield 2 O*
""",
)