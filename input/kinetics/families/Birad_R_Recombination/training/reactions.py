#!/usr/bin/env python
# encoding: utf-8

name = "Birad_R_Recombination/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "NH + NO2_r <=> HNNO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.42e+16, 'cm^3/(mol*s)'),
        n = -0.75,
        Ea = (1226, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: primaryNitrogenLibrary""",
    longDesc = 
u"""
T range: 500-3000 K
calculations done at the B3LYP/6-311D(d,p)//B3LYP/6-311D(d,p) level of theory
D. Chakraborty, C.C. Hsu, M.C. Lin, J. Chem. Phys., 1998, 109, 8887, doi: 10.1063/1.477560
k3a, p. 8893
No stabilization at low pressures, only K3a_inf is given (k3a_low = 0)
""",
)

entry(
    index = 2,
    label = "NO2_p <=> NO + O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.98e+14, 's^-1'),
        n = 0,
        Ea = (71700, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (1350, 'K'),
        Tmax = (2100, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Training reaction from kinetics library: primarySulfurLibrary""",
    longDesc = 
u"""
T range: 1350-2100 K
M. Rohrig, E.L. Petersen, D.F. Davidson, R.K. Hanson, Int. J. Chem. Kin., 1997, 29(7), 483-493, doi: 10.1002/(SICI)1097-4601(1997)29:7<483::AID-KIN2>3.0.CO;2-Q
Shock tube measurement
Originally a Troe expression was given, only k_inf is taken here
""",
)

entry(
    index = 4,
    label = "H + O <=> HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    longDesc = 
u"""
Converted to training reaction from rate rule: Y_rad;O_birad
""",
)

entry(
    index = 5,
    label = "H + S <=> HS",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    longDesc = 
u"""
Converted to training reaction from rate rule: Y_rad;S_birad
""",
)

entry(
    index = 6,
    label = "H + NH <=> H2N",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    longDesc = 
u"""
Converted to training reaction from rate rule: Y_rad;N_R_birad
""",
)

