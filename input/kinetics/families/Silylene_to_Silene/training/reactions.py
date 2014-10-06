#!/usr/bin/env python
# encoding: utf-8

name = "Silylene_to_Silene/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 1,
    label = "H3SiSiH <=> Si2H4",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (7.9E12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5.3095, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1600, 'K'),
    ),
    reference = Article(
        authors = ["Dollet, A.", "de Persis, S."],
        title = "Pressure-dependent rate coefficients of chemical reactions involving Si2H4 isomerization from QRRK calculations",
        journal = "J. Anal. Apply. Pyrolysis",
        pages = """460-470""",
        year = "2007",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2007DOL/DEP460-470:1",
    ),
    longDesc = 
u"""
QRRK calculations for the Si2H4 isomerization. This is the high P limit. Rate parameters are corroborated in J. Phys. Chem. 91, 5765 (1987).""",
)

