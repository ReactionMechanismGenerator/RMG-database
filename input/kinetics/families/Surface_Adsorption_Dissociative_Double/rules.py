#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_Dissociation_Double/rules"
shortDesc = u""
longDesc = u"""
Dissociative adsorption of a gas-phase species forming two adsorbates, each with a double bond to a surface site
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
    label = "OO;VacantSite1;VacantSite2",
    kinetics = StickingCoefficientBEP(
        A = 4.36E-2,
        n = -0.206,
        E0=(1.5E3, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""O2 dissociative adsorption""",
    longDesc = u"""
    Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts
    Delgado et al
    Catalysts, 2015, 5, 871-904
    doi: 10.3390/catal5020871
    
    E0 is the paper's Ea
    This is R3
    
    metal = 'Ni'
    """
)
