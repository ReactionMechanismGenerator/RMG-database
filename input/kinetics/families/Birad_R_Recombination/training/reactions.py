#!/usr/bin/env python
# encoding: utf-8

name = "Birad_R_Recombination/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""

entry(
    index = 1,
    label = "NH + NO2_r <=> HNNO2",
    degeneracy = 2,
    kinetics = Arrhenius(A=(1.42e+16, 'cm^3/(mol*s)'), n=-0.75, Ea=(1226, 'cal/mol'), T0=(1, 'K')),
    rank = 3,
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
    label = "S + NO <=> SNO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+14, 'cm^3/(mol*s)'), n=0.24, Ea=(0, 'cal/mol'), T0=(1, 'K'), Tmin = (300, 'K'), Tmax = (800, 'K')),
    rank = 1,
    shortDesc = u"""Training reaction from kinetics library: N-S_interactions""",
    longDesc = 
u"""
A. Goumri, D.D. Shao, P. Marshall, J. Chem. Phys., 2004, 121, 9999, doi: 10.1063/1.1806419
Experimentally measured, and PES verified using CBS-QB3
Originally a Troe expression was given, only k_inf is taken here
kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.3e+14, 'cm^3/(mol*s)'), n=0.24, Ea=(0, 'cal/mol'), T0=(1, 'K'), Tmin = (300, 'K'), Tmax = (800, 'K')),
        arrheniusLow = Arrhenius(A=(2.25e+15, 'cm^6/(mol^2*s)'), n=0, Ea=(-1868, 'cal/mol'), T0=(1, 'K'), Tmin = (300, 'K'), Tmax = (800, 'K')),
        alpha=1, T3=(1e-30, 'K'), T1=(1e+30, 'K'), efficiencies={}),
""",
)

#This is commented out because currently GAV can't estimate the reverse rate
#which results in rates that are many orders of magnitude faster than they should
#be, when this is no longer a problem for these species, this can be uncommented
#entry(
#   index = 3,
#   label = "HSOO <=> HSO + O",
#   degeneracy = 1,
#   kinetics = Arrhenius(A=(2.01e+19, 's^-1'), n=-1.07, Ea=(28377, 'cal/mol'), T0=(1, 'K'), Tmin = (200, 'K'), Tmax = (2000, 'K')),
#   rank = 2,
#   shortDesc = u"""Training reaction from kinetics library: primarySulfurLibrary""",
#   longDesc =
#u"""
#T range: 200-2000 K
#A. Goumri, J-D.R. Rocha, D. Laakso, C.E. Smith, P. Marshall, J. Phys. Chem. A, 1999, 103(51), 11328-11335 doi: 10.1021/jp9924070
#Table 7 on p. 11333
#calculations done at the QCISD(T)/6-311+G(3df,2p)//MP2=FULL/6-31G(d) level of theory
#Originally a Troe expression was given, only k_inf is taken here
#""",
#)

entry(
   index = 4,
   label = "NO2_p <=> NO + O",
   degeneracy = 1,
   kinetics = Arrhenius(A=(3.98e+14, 's^-1'), n=0, Ea=(71700, 'cal/mol'), T0=(1, 'K'), Tmin = (1350, 'K'), Tmax = (2100, 'K')),
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
   index = 5,
   label = "CH3CH2OO = CH3CH2O + O",
   degeneracy = 1,
   kinetics = Arrhenius(A=(2.98e15, 's^-1'), n=-0.09, Ea=(61600, 'cal/mol'), T0=(1, 'K'), Tmin = (300, 'K'), Tmax = (2000, 'K')),
   rank = 3,
   shortDesc = u"""CBS-Q//B3LYP/6-31G(d,p) calculation""",
   longDesc =
u"""
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
