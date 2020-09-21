#!/usr/bin/env python
# encoding: utf-8

name = "API_Intra_RH_Add_Endocyclic/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 807,
    label = "Rn;multiplebond_intra;radadd_intra",
    kinetics = ArrheniusEP(
        A = (1e+10, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    longDesc = 
u"""
To make this family possible, rate parameters of head node groups are estimated from typical threshold amounts of 
A (10^9 - 10^13 s^-1) and E0 (5-50 kcal/mol) in unimolecular gas-phase reactions. 
Definitely better kinetic parameters are needed to fill this database.
""",
)

