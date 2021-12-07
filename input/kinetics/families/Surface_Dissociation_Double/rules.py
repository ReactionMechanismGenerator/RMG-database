#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_Double/rules"
shortDesc = u""
longDesc = u"""
"""
entry(
    index = 1,
    label = "Combined;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (3.2e17, 'm^2/(mol*s)'),
        n = 0,
        alpha =0.84,
        E0 = (185.1, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
E0 and alpha are taken from:
"Universal Brønsted-Evans-Polanyi Relations for C–C, C–O, C–N, N–O, N–N, and O–O Dissociation Reactions" by Wang, ..., Norskov/ Catal. Lett (2011) 141:370-373, DOI: 10.1007/s10562-010-0477-y
(actual value for E0 was 1.92 eV.)
Pre-exponential coefficient is calculated from 1e13 s^-1 (standard guess from transition state theory) divided by 3.16e-9 mol cm^-2 (Kreitz et al. 2021, DOI: 10.1021/jacsau.1c00276)
    """
)

entry(
    index = 2,
    label = "C=O;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (3.2e17, 'm^2/(mol*s)'),
        n = 0,
        alpha =1.05,
        E0 = (116.65, 'kJ/mol'),
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
