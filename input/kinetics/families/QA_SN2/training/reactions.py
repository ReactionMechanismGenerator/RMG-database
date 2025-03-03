#!/usr/bin/env python
# encoding: utf-8


name = "QA_Nucleophilic_Substitution/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
 
 #ONLY LAMBDA=0 IS DEFINED HERE!

entry(
    index = 0,
    label = "C6H5-CH2-N(CH3)3 + OH <=> C6H5-CH2-OH + N(CH3)3", #TMBA degradation, N charge is +1 in C6H5-CH2-N(CH3)3
    degeneracy = 1,
    kinetics = Arrhenius(A=(97.5001, 'cm^3/(mol*s)'), n=3.59734, Ea=(52.8018, 'kJ/mol'),
        T0=(1, 'K'), Tmin=(270, 'K'), Tmax=(600, 'K')),
    rank = 3, # means that the data is calculated using high-level theoretical methods
    shortDesc = u""" wb97xd/jul-cc-PVTZ // dlpno-ccsd(t)/def2tzvpd (L2D-CC)""",
    longDesc =
u"""
Calculated by alongd (xq1343)
opt, freq: wB97x-D3/6-311++G(3df,3pd)
sp: CCSD(T)-F12a/aug-cc-pVTZ
rotors: B3LYP/6-311++G(3df,3pd)
"""
)

