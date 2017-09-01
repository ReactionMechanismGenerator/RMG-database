#!/usr/bin/env python
# encoding: utf-8

name = "Methyl_CPD_H_abs"
shortDesc = u"CBS-QB3"
longDesc = u"""
TST calculations using CBS-QB3.
"""
entry(
    index = 1,
    label = "1_methyl_CPD + H <=> 1_methyl_CPD_1_yl + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.707e+06, 'cm^3/(mol*s)'),
        n = 2.007,
        Ea = (4.132, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
CBS-QB3 calculations
""",
)

entry(
    index = 2,
    label = "2_methyl_CPD + H <=> 2_methyl_CPD_2_yl + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (930800, 'cm^3/(mol*s)'),
        n = 2.265,
        Ea = (3.244, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
CBS-QB3 calculations
""",
)

entry(
    index = 3,
    label = "5_methyl_CPD + H <=> 5_methyl_CPD_5_yl + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (418100, 'cm^3/(mol*s)'),
        n = 2.424,
        Ea = (7.318, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
CBS-QB3 calculations
""",
)

