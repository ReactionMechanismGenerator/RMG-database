#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_vdW/rules"
shortDesc = u""
longDesc = u"""
"""

entry(
    index = 1,
    label = "Combined;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (3.2e17, 'm^2/(mol*s)'),
        n = 0,
        alpha =0.5801,
        E0 = (117.49, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
Based on C-OH dissociation from Table 2 of "Effects of errors in linear scaling relations and Bronsted-Evans-Polanyi relations on activity and selectivity maps" Jonathan E. Sutton, Dionisios G. Vlachos, Journal of Catalysis, 2016, 338, 273-283, DOI: 10.1016/j.jcat.2016.03.013.
Pre-exponential coefficient is calculated from 1e13 s^-1 (standard guess from transition state theory) divided by 3.16e-9 mol cm^-2 (Kreitz et al. 2021, DOI: 10.1021/jacsau.1c00276)
"""
)

entry(
    index = 2,
    label = "H2O;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (3.2e17, 'm^2/(mol*s)'),
        n = 0,
        alpha =0.51,
        E0 = (97.5, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
BEP relation for all metals and facets from Wang et al. "Universal transition state scaling relations for (de)hydrogenation over transition metals", Physical chemistry chemical physics, 2011, 13, 20760-20765, DOI:10.1039/c1cp20547a.
Technically this is a relation for dissociative adsorption.  
"""
)

entry(
    index = 3,
    label = "C-OH;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (3.2e17, 'm^2/(mol*s)'),
        n = 0,
        alpha =0.5801,
        E0 = (117.49, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
Based on C-OH dissociation from Table 2 of "Effects of errors in linear scaling relations and Bronsted-Evans-Polanyi relations on activity and selectivity maps" Jonathan E. Sutton, Dionisios G. Vlachos, Journal of Catalysis, 2016, 338, 273-283, DOI: 10.1016/j.jcat.2016.03.013.
Pre-exponential coefficient is calculated from 1e13 s^-1 (standard guess from transition state theory) divided by 3.16e-9 mol cm^-2 (Kreitz et al. 2021, DOI: 10.1021/jacsau.1c00276)
"""
)

entry(
    index = 4,
    label = "C-H;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (3.2e17, 'm^2/(mol*s)'),
        n = 0,
        alpha =0.5860,
        E0 = (75.64, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
Based on C-H dissociation from Table 2 of "Effects of errors in linear scaling relations and Bronsted-Evans-Polanyi relations on activity and selectivity maps" Jonathan E. Sutton, Dionisios G. Vlachos, Journal of Catalysis, 2016, 338, 273-283, DOI: 10.1016/j.jcat.2016.03.013.
Pre-exponential coefficient is calculated from 1e13 s^-1 (standard guess from transition state theory) divided by 3.16e-9 mol cm^-2 (Kreitz et al. 2021, DOI: 10.1021/jacsau.1c00276)
"""
)
