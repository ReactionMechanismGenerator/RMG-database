#!/usr/bin/env python
# encoding: utf-8

name = "Aromatics_high_pressure/C10H9-1"
shortDesc = u"Phenyl radical second acetylene addition, Bittner-Howard pathway"
longDesc = u"""
Temperature- and pressure-dependent rate coefficients for the HACA pathways from benzene to naphthalene
Alexander M. Mebel, Yuri Georgievskii, Ahren W. Jasper, Stephen J. Klippenstein
Proceedings of the Combustion Institute 36 (2017) 919–926

Calculated at the G3(MP2,CC)//B3LYP/6-311G** level of theory. TST rates are from the literature.
"""
duplicatesChecked=True
entry(
    index = 0,
    label = "W18 <=> P7 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.817e+11, 's^-1'), n=0.838, Ea=(38.356, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1,
    label = "W18 <=> W11",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.953e+11, 's^-1'), n=0.387, Ea=(32.996, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2,
    label = "W18 <=> W21",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.076e+11, 's^-1'), n=0.228, Ea=(6.982, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: 2016_Mebel_C6H5C2H2_C2H2_High_P
""",
)

entry(
    index = 3,
    label = "W21 <=> P1 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.581e+10, 's^-1'), n=0.793, Ea=(14.523, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 4,
    label = "R2 + C2H2 <=> W18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.081e+09, 'cm^3/(mol*s)'),
        n = 1.21,
        Ea = (6.756, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

