#!/usr/bin/env python
# encoding: utf-8

name = "2017_Mebel_C6H4C2H_C2H2_highP"
shortDesc = u"G3(MP2,CC)//B3LYP"
longDesc = u"""
Taken from high P calculations of:

Mebel, A. M.; Georgievskii, Y.; Jasper, A. W.; Klippenstein, S. J.,
Temperature- and pressure-dependent rate coefficients for the HACA pathways from benzene to naphthalene.
Proc. Combust. Inst. 2017, 36, 919-926.
"""
entry(
    index = 1,
    label = "W1 <=> W2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.926e+10, 's^-1'), n=0.198, Ea=(5.455, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2,
    label = "W1 <=> W3_6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.42e+11, 's^-1'), n=0.258, Ea=(3.797, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 3,
    label = "W2 <=> W4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.843e+08, 's^-1'), n=1.605, Ea=(56.952, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 4,
    label = "W3_6 <=> W5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(24735, 's^-1'), n=2.344, Ea=(38.798, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 5,
    label = "W3_6 <=> W7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(191.5, 's^-1'), n=3.05, Ea=(53.137, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 6,
    label = "R1 + C2H2 <=> W1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.068e+06, 'cm^3/(mol*s)'),
        n = 1.842,
        Ea = (3.272, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 7,
    label = "P1 + H <=> W1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.775e+09, 'cm^3/(mol*s)'),
        n = 1.414,
        Ea = (6.896, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 8,
    label = "P2 + H <=> W2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.586e+11, 'cm^3/(mol*s)'),
        n = 0.743,
        Ea = (0.228, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 9,
    label = "P2 + H <=> W4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.409e+12, 'cm^3/(mol*s)'),
        n = 0.597,
        Ea = (0.436, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 10,
    label = "P3 + H <=> W4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.179e+12, 'cm^3/(mol*s)'),
        n = 0.61,
        Ea = (0.09, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 11,
    label = "P4 + H <=> W5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.919e+13, 'cm^3/(mol*s)'),
        n = 0.168,
        Ea = (-0.002, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 12,
    label = "P5 + H <=> W7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.919e+13, 'cm^3/(mol*s)'),
        n = 0.168,
        Ea = (-0.002, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

