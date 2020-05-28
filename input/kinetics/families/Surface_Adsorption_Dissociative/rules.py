#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_Dissociative/rules"
shortDesc = u""
longDesc = u"""
Dissociative adsorption of a gas-phase species forming two adsorbates, each with a single bond to a surface site
"""
entry(
    index = 1,
    label = "Adsorbate;VacantSite1;VacantSite2",
    kinetics = StickingCoefficientBEP(
        A = 0.01,
        n = 0,
        alpha = 0,
        E0 = (10, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""Made up"""
)

entry(
    index = 2,
    label = "H2;VacantSite1;VacantSite2",
    kinetics = StickingCoefficientBEP(
        A = 0.01,
        n = 0,
        alpha = 0,
        E0 = (0., 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""H2 dissociative adsorption""",
    longDesc = u"""
    Micro-kinetic modeling of NH3 decomposition on Ni and its application to solid oxide fuel cells
    Deutschmann et al
    doi: 10.1016/j.ces.2011.07.007

    E0 is the paper's Ea
    This is R1

    metal = 'Ni'
    """
)
