#!/usr/bin/env python
# encoding: utf-8

name = "HAN"
shortDesc = u""
longDesc = u"""
Reactions pertinent to the decomposition of HAN from
Izato, Y., Shiota, K., & Miyake, A. (n.d.). 
A detailed kinetics model for the decomposition of aqueous hydroxylammonium nitrate. 
212–221.

reaction for ammonium nitrate decomp
Feick, G., & Hainer, R. M. (1954). On the Thermal Decomposition of Ammonium Nitrate. 
Steady-state Reaction Temperatures and Reaction Rate. 
Journal of the American Chemical Society, 76(22), 
5860–5863. https://doi.org/10.1021/ja01651a096

"""

entry(
    index = 1,
    label = "HAN <=> NH2OH + HNO3",
    kinetics = Arrhenius(
        A = (7.32e10, '1/s'),
        n = 0.49,
        Ea=(40.492, 'kcal/mol'),
        # Ea=(17.492, 'kcal/mol'), changed to higher Ea because it is occurring too frequently (rate is too high at low T)
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""hydroxyl Ammonium Nitrate thermal decomp""",
    longDesc = u"""
R1 in paper
    """,
)

entry(
    index = 2,
    label = "NH4NO3 <=> N2O + H2O + H2O",
    kinetics = Arrhenius(
        A = (6.309573445e13, '1/s'),
        n = 0,
        Ea=(40.5, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Ammonium Nitrate decomposition""",
    longDesc = u"""
    from Feick paper, temp range is much lower though (only to 200C)
    """,

)
