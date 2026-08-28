#!/usr/bin/env python
# encoding: utf-8

name = "Birad_R_Recombination/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "NH + NO2_r <=> HNNO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.42e+16,'cm^3/(mol*s)'), n=-0.75, Ea=(1226,'cal/mol'), T0=(1,'K')),
    rank = 5,
    shortDesc = """Training reaction from kinetics library: primaryNitrogenLibrary""",
    longDesc = 
"""
T range: 500-3000 K
calculations done at the B3LYP/6-311D(d,p)//B3LYP/6-311D(d,p) level of theory
D. Chakraborty, C.C. Hsu, M.C. Lin, J. Chem. Phys., 1998, 109, 8887, doi: 10.1063/1.477560
k3a, p. 8893
No stabilization at low pressures, only K3a_inf is given (k3a_low = 0)
""",
)

entry(
    index = 1,
    label = "S + NO <=> SNO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.3e+14,'cm^3/(mol*s)'), n=0.24, Ea=(0,'cal/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(800,'K')),
    rank = 1,
    shortDesc = """Training reaction from kinetics library: N-S_interactions""",
    longDesc = 
"""
A. Goumri, D.D. Shao, P. Marshall, J. Chem. Phys., 2004, 121, 9999, doi: 10.1063/1.1806419
Experimentally measured, and PES verified using CBS-QB3
Originally a Troe expression was given, only k_inf is taken here
kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.3e+14, 'cm^3/(mol*s)'), n=0.24, Ea=(0, 'cal/mol'), T0=(1, 'K'), Tmin = (300, 'K'), Tmax = (800, 'K')),
        arrheniusLow = Arrhenius(A=(2.25e+15, 'cm^6/(mol^2*s)'), n=0, Ea=(-1868, 'cal/mol'), T0=(1, 'K'), Tmin = (300, 'K'), Tmax = (800, 'K')),
        alpha=1, T3=(1e-30, 'K'), T1=(1e+30, 'K'), efficiencies={}),
""",
)

entry(
    index = 2,
    label = "NO2_p <=> NO + O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.98e+14,'s^-1'), n=0, Ea=(71700,'cal/mol'), T0=(1,'K'), Tmin=(1350,'K'), Tmax=(2100,'K')),
    rank = 1,
    shortDesc = """Training reaction from kinetics library: primarySulfurLibrary""",
    longDesc = 
"""
T range: 1350-2100 K
M. Rohrig, E.L. Petersen, D.F. Davidson, R.K. Hanson, Int. J. Chem. Kin., 1997, 29(7), 483-493, doi: 10.1002/(SICI)1097-4601(1997)29:7<483::AID-KIN2>3.0.CO;2-Q
Shock tube measurement
Originally a Troe expression was given, only k_inf is taken here
""",
)

entry(
    index = 3,
    label = "CH3CH2OO = CH3CH2O + O",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.98e+15,'s^-1'), n=-0.09, Ea=(61600,'cal/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K')),
    rank = 5,
    shortDesc = """CBS-Q//B3LYP/6-31G(d,p) calculation""",
    longDesc = 
"""
From Detailed Kinetics and Thermochemistry of C2H5+O2:  Reaction Kinetics of the 
Chemically-Activated and Stabilized CH3CH2OO Adduct
J. Phys. Chem. A 2002, 106,7276-7293
Sheng, Bozzelli, Dean and Chang
'enthalpy
calculated at the CBS-Q//B3LYP/6-31G(d,p) and entropy and
heat capacity values from frequencies and structures at B3LYP/
6-31G(d,p) level of theory'
""",
)

entry(
    index = 4,
    label = "H + O <=> HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 5,
    longDesc = 
"""
Converted to training reaction from rate rule: Y_rad;O_birad
""",
)

entry(
    index = 5,
    label = "H + S <=> HS",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 5,
    longDesc = 
"""
Converted to training reaction from rate rule: Y_rad;S_birad
""",
)

entry(
    index = 6,
    label = "H + NH <=> H2N",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13,'cm^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K')),
    rank = 5,
    longDesc = 
"""
Converted to training reaction from rate rule: Y_rad;N_R_birad
""",
)

