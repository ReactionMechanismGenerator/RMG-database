#!/usr/bin/env python
# encoding: utf-8

name = "2001_Tokmakov_H_Toluene_to_CH3_Benzene_high_P"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "C6H5CH3 + H <=> ipso-(C7H9)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.65e+06, 'cm^3/(mol*s)'),
        n = 2.063,
        Ea = (3.976, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2001 Tokmakov calculation using G2M(cc,MP2)//B3LYP/6-311++G(3df,2p)',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
From 2001 Tokmakov calculation using G2M(cc,MP2)//B3LYP/6-311++G(3df,2p)
""",
)

entry(
    index = 2,
    label = "ipso-(C7H9) <=> C6H6 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.831e+11, 's^-1'),
        n = 0.669,
        Ea = (19.862, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2001 Tokmakov calculation using G2M(cc,MP2)//B3LYP/6-311++G(3df,2p)',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
From 2001 Tokmakov calculation using G2M(cc,MP2)//B3LYP/6-311++G(3df,2p)
""",
)

