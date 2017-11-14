#!/usr/bin/env python
# encoding: utf-8

name = "2017_Mebel_C6H5_C2H2_highP"
shortDesc = u"G3(MP2,CC)//B3LYP"
longDesc = u"""
Phenyl radical + acetylene PES calculated using G3(MP2,CC)//B3LYP + TST. Taken from:

Mebel, A. M.; Georgievskii, Y.; Jasper, A. W.; Klippenstein, S. J., 
Temperature- and pressure-dependent rate coefficients for the HACA pathways from benzene to naphthalene. 
Proc. Combust. Inst. 2017, 36, 919-926.
"""
entry(
    index = 0,
    label = "W1 <=> P1 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.323e+10, 's^-1'), n=1.103, Ea=(38.251, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1,
    label = "W1 <=> W3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.445e+06, 's^-1'), n=1.735, Ea=(23.162, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2,
    label = "R1 + C2H2 <=> W1",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.954e+07, 'cm^3/(mol*s)'),
        n = 1.638,
        Ea = (3.448, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

