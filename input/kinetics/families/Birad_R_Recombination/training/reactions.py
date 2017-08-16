#!/usr/bin/env python
# encoding: utf-8

name = "Birad_R_Recombination/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
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
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: SOxNOx""",
    longDesc = 
u"""
Part of the "NOx" subset
T range: 500-3000 K
calculations done at the B3LYP/6-311D(d,p)//B3LYP/6-311D(d,p) level of theory
D. Chakraborty, C.C. Hsu, M.C. Lin, J. Chem. Phys., 1998, 109, 8887, doi: 10.1063/1.477560
k3a, p. 8893
No stabilization at low pressures, only K3a_inf is given (k3a_low = 0)
""",
)

entry(
    index = 1,
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
    referenceType = "<type 'NoneType'>",
    rank = 2,
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: Y_rad;Oa
""",
)

entry(
    index = 2,
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
    referenceType = "<type 'NoneType'>",
    rank = 2,
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: Y_rad;Sa
""",
)

entry(
    index = 3,
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
    referenceType = "<type 'NoneType'>",
    rank = 2,
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: Y_rad;N_R_birad
""",
)

