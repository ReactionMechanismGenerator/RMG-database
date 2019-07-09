#!/usr/bin/env python
# encoding: utf-8

name = "Peroxyl_Disproportionation/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label = "CH3OCH2O2 + CH3OCH2O2 <=> CH3OCH2O + O2 + CH3OCH2O",
    degeneracy = 0.5,
    kinetics=Arrhenius(
        A = (1.547e+23, 'cm^3/(mol*s)'),
        n = -4.5,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: CurranPentane""",
    longDesc =
u"""
Taken from entry CH3OCH2O2 + CH3OCH2O2 <=> O2 + CH3OCH2O + CH3OCH2O
which is based on an Arrhenius fit of rate parameters in the NIST database
with a modified A-factor (scaled by 1/3). The NIST rates are obtained from experiment.

Because it is not evident how exactly this rate was obtained, a lower rank is assigned.
""",
)

entry(
    index = 2,
    label = "CH3O2 + CH3O2 <=> CH3O + O2 + CH3O",
    degeneracy = 0.5,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Training reaction from kinetics library: CurranPentane""",
    longDesc =
u"""
Taken from entry CH3O2 + CH3O2 <=> O2 + CH3O + CH3O
which is based on the experimental rate from Lightfoot et al. in J. Chem. Soc. Faraday Trans. (1991)
(https://doi.org/10.1039/FT9918703213) and was combined with the branching ratio from
Lightfoot et al. in J. Phys. Chem. (1990) (https://doi.org/10.1021/j100365a036) which is for a
different reaction, but was used due to its similarity to this one.
""",
)

entry(
    index = 3,
    label = "C2H5O2 + C2H5O2 <=> C2H5O + O2 + C2H5O",
    degeneracy = 0.5,
    kinetics = Arrhenius(
        A = (2.9e+11, 'cm^3/(mol*s)'),
        n = -0.27,
        Ea = (408, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Training reaction from kinetics library: Klippenstein_Glarborg2016""",
    longDesc =
u"""
Taken from entry CH3CH2OO + CH3CH2OO <=> CH3CH2O + CH3CH2O + O2
which is based on a fitted expression combining rates from Fenter et al. in J. Phys. Chem. 1993
(https://doi.org/10.1021/j100116a016) with a branching ratio from Lightfoot et al.
in Atmos. Environ. A 1992 (https://doi.org/10.1016/0960-1686(92)90423-I).
""",
)

entry(
    index = 4,
    label = "C2H3O3 + CH3O2 <=> C2H3O2 + O2 + CH3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.1e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
    rank = 1,
    shortDesc = u"""Training reaction from kinetics library: Klippenstein_Glarborg2016""",
    longDesc =
u"""
Taken from entry CH3C(O)OO + CH3OO <=> CH3C(O)O + CH3O + O2
which is based on the experimental rates from Atkinson et al. in Atmos. Chem. Phys. (2006)
(https://doi.org/10.5194/acp-6-3625-2006).
""",
)

entry(
    index = 5,
    label = "C2H3O3 + HO2 <=> C2H3O2 + O2 + OH",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.9e+11, 'cm^3/(mol*s)'), n=0, Ea=(-1950, 'cal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: Klippenstein_Glarborg2016""",
    longDesc =
u"""
Taken from entry CH3C(O)OO + HO2 <=> CH3C(O)O + OH + O2
which is based on the experimental rate from Gross et al. in J. Phys. Chem. (2014)
(https://doi.org/10.1021/jp412380z) with temperature-dependence from Atkinson et al.
in Atmos. Chem. Phys. (2006) (https://doi.org/10.5194/acp-6-3625-2006).
""",
)
