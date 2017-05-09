#!/usr/bin/env python
# encoding: utf-8

name = "2015_Wang_K_C6H9"
shortDesc = u""
longDesc = u"""
Only includes Methyl + CPD TST rate on C6H9 PES from CBS-QB3 calculations of:

Wang, K.; Villano, S. M.; Dean, A. M., Reactions of allylic radicals that impact molecular weight growth kinetics. 
Phys. Chem. Chem. Phys. 2015, 17, 6255-6273.

This reaction is critical to converting CPD to Benzene in the presence of methyl radical.
"""
entry(
    index = 1,
    label = "Well_5 <=> CH3 + CPD",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.89e+14, 's^-1'), n=0, Ea=(38.9, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

