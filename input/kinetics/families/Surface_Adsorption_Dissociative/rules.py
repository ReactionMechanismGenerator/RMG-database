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
        alpha =0.0,
        E0 = (41.8, 'kJ/mol'),
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
        A = 0.1,
        n = 0,
        alpha =0.0,
        E0 = (3.8, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""H2 dissociative adsorption""",
    longDesc = u"""
Careful, this is not a real BEP relation since alpha=0. These are values for H2 adsorption on Ni(111) from 
de Carvalho et al. "Modeling and Reduced Rate expression of the Water gas shift reaction on Nickel", Industrial & Engineering Chemistry Research, 2018, 57, 10269-10280, DOI:10.1021/acs.iecr.8b01957.
Dissocivative H2 adsorption is slightly activated on most metals. 
"""
)

entry(
    index = 3,
    label = "CH4;VacantSite1;VacantSite2",
    kinetics = StickingCoefficientBEP(
        A = 0.5,
        n = 0,
        alpha =0.72,
        E0 = (92.6, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""CH4 dissociative adsorption""",
    longDesc = u"""
BEP relation for all metals from Wang et al. "Universal transition state scaling relations for (de)hydrogenation over transition metals", Physical chemistry chemical physics, 2011, 13, 20760-20765, DOI:10.1039/c1cp20547a.
"""
)

entry(
    index = 4,
    label = "C2H6;VacantSite1;VacantSite2",
    kinetics = StickingCoefficientBEP(
        A = 0.5,
        n = 0,
        alpha =0.86,
        E0 = (72.4, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""CH4 dissociative adsorption""",
    longDesc = u"""
BEP relation for all metals (but only steps) from Wang et al. "Universal transition state scaling relations for (de)hydrogenation over transition metals", Physical chemistry chemical physics, 2011, 13, 20760-20765, DOI:10.1039/c1cp20547a.
"""
)

entry(
    index = 5,
    label = "C3H8;VacantSite1;VacantSite2",
    kinetics = StickingCoefficientBEP(
        A = 0.5,
        n = 0,
        alpha =0.76,
        E0 = (107.1, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""CH4 dissociative adsorption""",
    longDesc = u"""
BEP relation for all metals (but only steps) from Wang et al. "Universal transition state scaling relations for (de)hydrogenation over transition metals", Physical chemistry chemical physics, 2011, 13, 20760-20765, DOI:10.1039/c1cp20547a.
"""
)
