#!/usr/bin/env python
# encoding: utf-8

name = ""
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "biCPD_1 <=> biCPD_2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.11e+08, 's^-1'), n=1.6, Ea=(22.9, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
/intra H migrations in biCPD
""",
)

entry(
    index = 2,
    label = "biCPD_4 <=> biCPD_5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.14e+07, 's^-1'), n=1.81, Ea=(25.1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3,
    label = "biCPD_2 <=> biCPD_4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+08, 's^-1'), n=1.55, Ea=(19.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 4,
    label = "biCPD_2 <=> biCPD_3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.19e+07, 's^-1'), n=1.72, Ea=(24.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 5,
    label = "biCPD_5 <=> biCPD_6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.22e+07, 's^-1'), n=1.76, Ea=(25, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 6,
    label = "biCPD_3 <=> biCPD_5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.28e+08, 's^-1'), n=1.55, Ea=(20.1, 'kcal/mol'), T0=(1, 'K')),
)

