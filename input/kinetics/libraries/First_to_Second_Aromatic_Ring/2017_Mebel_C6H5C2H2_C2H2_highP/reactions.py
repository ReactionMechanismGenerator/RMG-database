#!/usr/bin/env python
# encoding: utf-8

name = "2017_Mebel_C6H5C2H2_C2H2_highP"
shortDesc = u"G3(MP2,C)//B3LYP/6-311G**"
longDesc = u"""
High-P limit rates calculated using MESS in:

Mebel, A. M.; Georgievskii, Y.; Jasper, A. W.; Klippenstein, S. J.,
Temperature- and pressure-dependent rate coefficients for the HACA pathways from benzene to naphthalene.
Proc. Combust. Inst. 2017, 36, 919-926.
"""
entry(
    index = 0,
    label = "W3 <=> P4 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.817e+11, 's^-1'), n=0.838, Ea=(38.356, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1,
    label = "W3 <=> W11",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.953e+11, 's^-1'), n=0.387, Ea=(32.996, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2,
    label = "W3 <=> W4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.076e+11, 's^-1'), n=0.228, Ea=(6.982, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 3,
    label = "W4 <=> P1 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.581e+10, 's^-1'), n=0.793, Ea=(14.523, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 4,
    label = "R2 + C2H2 <=> W3",
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

