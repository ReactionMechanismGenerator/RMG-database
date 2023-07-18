#!/usr/bin/env python
# encoding: utf-8

name = "H_abstraction_DMF_kinetics"
shortDesc = u"H_abstraction_DMF"
longDesc = u"""

"""
#RMG
#entry(
#    index = 1,
#    label = "H_rad + DMF <=> H2 + DMF_rad_on_methyl",
#    degeneracy = 1,
#   kinetics = Arrhenius(
#        A = (6100.68, 'cm^3/(mol*s)'),
#        n = 3.15,
#        Ea = (4.3166754302e+03, 'cal/mol'),
#        T0 = (1, 'K'),
#    ),
#)

#Tran 2017 CBS-QB3 300-2500K https://www.sciencedirect.com/science/article/pii/S0010218017301256#bib0047
#DMF+R1H=R1C6H7O+H2                1.55E+05     2.700    3434.0    !CBSQ-B3! Tran 2017 ~700-1200K

entry(
    index = 0,
    label = "H_rad + DMF <=> H2 + DMF_rad_on_methyl",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.55E+05, 'cm^3/(mol*s)'),
        n = 2.7,
        Ea = (3434.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1,
    label = "H_rad + DMF <=> H2 + DMF_rad_on_ring",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.73, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (6.1e+03, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

