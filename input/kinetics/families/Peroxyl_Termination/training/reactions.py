#!/usr/bin/env python
# encoding: utf-8

name = "Peroxyl_Termination/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label = "CH3O2 + CH3O2-2 <=> CH2O + O2 + CH4O",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (2e+11, 'cm^3/(mol*s)'),
        n = -0.55,
        Ea = (-1600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Training reaction from kinetics library: Klippenstein_Glarborg2016""",
    longDesc =
u"""
Taken from entry CH3OO + CH3OO <=> CH3OH + CH2O + O2
which is based on experimental data from Baulch et al. in JPCRD (2005)
(https://doi.org/10.1063/1.1748524).
""",
)

entry(
    index = 2,
    label = "C2H5O2 + C2H5O2-2 <=> C2H4O + O2 + C2H6O",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(4.3e+09, 'cm^3/(mol*s)'), n=0, Ea=(-850, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Training reaction from kinetics library: Klippenstein_Glarborg2016""",
    longDesc =
u"""
Taken from entry CH3CH2OO + CH3CH2OO <=> CH3CHO + CH3CH2OH + O2
which is based on a fitted expression combining rates from Fenter et al. in J. Phys. Chem. 1993
(https://doi.org/10.1021/j100116a016) with a branching ratio from Lightfoot et al.
in Atmos. Environ. A 1992 (https://doi.org/10.1016/0960-1686(92)90423-I).
""",
)

entry(
    index = 3,
    label = "CH3O2 + C2H3O3 <=> CH2O + O2 + C2H4O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.2e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Experimental rate from Atkinson et al. (2006)""",
    longDesc =
u"""
Based on the experimental rates from Atkinson et al. in Atmos. Chem. Phys. (2006)
(https://doi.org/10.5194/acp-6-3625-2006).
""",
)
