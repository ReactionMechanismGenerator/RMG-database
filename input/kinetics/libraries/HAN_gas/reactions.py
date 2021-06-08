#!/usr/bin/env python
# encoding: utf-8

name = "HAN"
shortDesc = u""
longDesc = u"""
Reactions pertinent to the decomposition of HAN from
Izato, Y., Shiota, K., & Miyake, A. (n.d.). 
A detailed kinetics model for the decomposition of aqueous hydroxylammonium nitrate. 
212–221.

"""

entry(
    index = 1,
    label = "HAN <=> NH2OH + HNO3",
    kinetics = Arrhenius(
        A = (7.32e10, '1/s'),
        n = 0.49,
        Ea=(17.492, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Ammonium Nitrate thermal decomp""",
    longDesc = u"""
R1 in paper
    """,
)

# entry(
#     index = 2,
#     label = "NH2OH + HNO3 <=> HAN",
#     kinetics = Arrhenius(
#         A = (1e12, 'cm^3/(mol*s)'),
#         n = 0,
#         Ea=(0.0, 'kcal/mol'),
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     shortDesc = u"""Ammonium Nitrate Adsorption decomposition""",
#     longDesc = u"""
    
#     """,

# )
