#!/usr/bin/env python
# encoding: utf-8

name = "C6H4C2H_C2H2_highP"
shortDesc = u"C6H3C2H + C2H2 to form C10H7"
longDesc = u"""
Rate from V. V. Kislov et al., J. Chem. Theory Comput., 1(2005)
908-924. Also includes recombination of C10H7 with H to form napthalene -
Rate from L. B. Harding et al., J. Phys. Chem. A., 109(2005) 4646-4656
"""
entry(
    index = 1,
    label = "C6H4C2H + C2H2 <=> A12",
    degeneracy = 1,
    kinetics = Arrhenius(A=(13400, 'cm^3/(mol*s)'), n=2.499, Ea=(1283, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2,
    label = "A12 <=> C10H7-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.948e+11, 's^-1'), n=0.045, Ea=(5395, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 3,
    label = "C10H7-1 + H <=> C10H8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.87e+13, 'cm^3/(mol*s)'), n=0.13, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

