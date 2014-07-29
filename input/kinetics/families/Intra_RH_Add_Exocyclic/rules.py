#!/usr/bin/env python
# encoding: utf-8

name = "Intra_RH_Add_Exocyclic/rules"
shortDesc = u""
longDesc = u"""
"""
recommended = True

entry(
    index = 807,
    label = "Rn;multiplebond_intra;radadd_intra",
    group1 = "OR{R4, R5, R6, R7}",
    group2 = 
"""
1 *2  C 0 {2,{D,T}}
2 *3 {C,O} 0 {1,{D,T}}
""",
    group3 = 
"""
1 *1 R!H 0
""",
    kinetics = ArrheniusEP(
        A = (10000000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 0,
    shortDesc = u"""""",
    longDesc = 
u"""
To make this family possible, rate parameters of head node groups are estimated from typical threshold amounts of 
A (10^9 - 10^13 s^-1) and E0 (5-50 kcal/mol) in unimolecular gas-phase reactions. 
Definitely better kinetic parameters are needed to fill this database.
""",
    
)
