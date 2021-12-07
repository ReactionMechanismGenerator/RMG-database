#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_Beta_vdW/rules"
shortDesc = u""
longDesc = u"""
"""

entry(
    index = 1,
    label = "Combined;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (3.2e17, 'm^2/(mol*s)'),
        n = 0.,
        alpha =1.08,
        E0 = (110.56, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
Recreated BEP relation. Activation energies taken from Vogt et al. 2019 (see DOI: 10.1038/s41467-019-12858-3) and heats of formation from DFT calculations for Ni(111) performed by Bjarne Kreitz. For details on the DFT simulation and the results refer to Kreitz et al. 2021, DOI: 10.1021/jacsau.1c00276.
Pre-exponential coefficient is calculated from 1e13 s^-1 (standard guess from transition state theory) divided by 3.16e-9 mol cm^-2 (Kreitz et al. 2021, DOI: 10.1021/jacsau.1c00276)
"""
)
