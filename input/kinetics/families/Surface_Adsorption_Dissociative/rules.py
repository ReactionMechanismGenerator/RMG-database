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
        A = 0.1,
        n = 0,
        alpha = 0.69,
        E0 = (107.9, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""Universal BEP relation for all metals from Wang et al. "Universal transition state scaling relations for (de)hydrogenation over transition metals", Physical chemistry chemical physics, 2011, 13, 20760-20765, DOI:10.1039/c1cp20547a."""
)

entry(
    index = 2,
    label = "H2;VacantSite1;VacantSite2",
    kinetics = StickingCoefficientBEP(
        A = 0.1,
        n = 0,
        alpha = 0,
        E0 = (3.8, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""H2 dissociative adsorption""",
    longDesc = u"""
    Parameters are from Carvalho et al. "Microkinetic Modeling and Reduced Rate Expression of the Water–Gas Shift Reaction on Nickel", Ind. Eng. Chem. Res. 2018, 57, 31, 10269-10280, DOI:10.1021/acs.iecr.8b01957. Metal is Ni(111). 
    """
)

entry(
    index = 3,
    label = "CH4;VacantSite1;VacantSite2",
    kinetics = StickingCoefficientBEP(
        A = 1.51,
        n = 0,
        alpha =0.0,
        E0 = (58.0, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""CH4 dissociative adsorption""",
    longDesc = u"""
Data from G.W. Cushing, J.K. Navin, S.B. Donald, L. Valdez, V. Johanek, I. Harrison "C-H Bond Activation of Light Alkanes on Pt(111): Dissociative Sticking Coefficients, Evans-Polanyi Relation, and Gas-Surface Energy Transfer" J. Phys. Chem. C, 2010, 114, 17222-17232, DOI:10.1021/jp105073.
A (6.04) divided by 4 because of surface degeneracy for CH4
"""
)

entry(
    index = 4,
    label = "C2H6;VacantSite1;VacantSite2",
    kinetics = StickingCoefficientBEP(
        A = 0.342,
        n = 0,
        alpha =0.0,
        E0 = (42.7, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""C2H6 dissociative adsorption""",
    longDesc = u"""
Data from G.W. Cushing, J.K. Navin, S.B. Donald, L. Valdez, V. Johanek, I. Harrison "C-H Bond Activation of Light Alkanes on Pt(111): Dissociative Sticking Coefficients, Evans-Polanyi Relation, and Gas-Surface Energy Transfer" J. Phys. Chem. C, 2010, 114, 17222-17232, DOI:10.1021/jp105073.
A (2.05) divided by 6 because of surface degeneracy for C2H6
"""
)

entry(
    index = 5,
    label = "C3H8;VacantSite1;VacantSite2",
    kinetics = StickingCoefficientBEP(
        A = 0.198,
        n = 0,
        alpha =0.0,
        E0 = (33.6, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""C3H8 dissociative adsorption""",
    longDesc = u"""
Data from G.W. Cushing, J.K. Navin, S.B. Donald, L. Valdez, V. Johanek, I. Harrison "C-H Bond Activation of Light Alkanes on Pt(111): Dissociative Sticking Coefficients, Evans-Polanyi Relation, and Gas-Surface Energy Transfer" J. Phys. Chem. C, 2010, 114, 17222-17232, DOI:10.1021/jp105073.
A (1.19) divided by 6 because of surface degeneracy for C3H8
"""
)

entry(
    index = 7,
    label = "C-H;VacantSite1;VacantSite2",
    kinetics = StickingCoefficientBEP(
        A = 0.1,
        n = 0,
        alpha = 0.69,
        E0 = (107.9, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""Universal BEP relation for all metals from Wang et al. "Universal transition state scaling relations for (de)hydrogenation over transition metals", Physical chemistry chemical physics, 2011, 13, 20760-20765, DOI:10.1039/c1cp20547a."""
)

entry(
    index = 7,
    label = "O-H;VacantSite1;VacantSite2",
    kinetics = StickingCoefficientBEP(
        A = 0.1,
        n = 0,
        alpha = 0.69,
        E0 = (107.9, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""Universal BEP relation for all metals from Wang et al. "Universal transition state scaling relations for (de)hydrogenation over transition metals", Physical chemistry chemical physics, 2011, 13, 20760-20765, DOI:10.1039/c1cp20547a."""
)

entry(
    index = 8,
    label = "CH3OH;VacantSite1;VacantSite2",
    kinetics = StickingCoefficientBEP(
        A = 0.033,
        n = 0,
        alpha =0.76,
        E0 = (107.1, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""CH3OH dissociative adsorption""",
    longDesc = u"""
BEP relation for all metals (but only steps) from Wang et al. "Universal transition state scaling relations for (de)hydrogenation over transition metals", Physical chemistry chemical physics, 2011, 13, 20760-20765, DOI:10.1039/c1cp20547a.
Divided by 3 because of surface degeneracy for CH3OH
"""
)

entry(
    index = 9,
    label = "C2H4;VacantSite1;VacantSite2",
    kinetics = StickingCoefficientBEP(
        A = 0.025,
        n = 0,
        alpha = 0.69,
        E0 = (107.9, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""Universal BEP relation for all metals from Wang et al. "Universal transition state scaling relations for (de)hydrogenation over transition metals", Physical chemistry chemical physics, 2011, 13, 20760-20765, DOI:10.1039/c1cp20547a.
Divided by 4 because of surface degeneracy for C2H4
"""
)

