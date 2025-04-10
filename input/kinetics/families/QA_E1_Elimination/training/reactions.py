#!/usr/bin/env python
# encoding: utf-8


name = "QA_E1_Elimination"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
 
 #THE KINETIC DATA IS NOT RELEVANT! UPDATE CORRECT PARAMETERS

entry(
    index = 0,
    label = "R-CHR-CR2-NR2-CH3 + OH <=> CR2CR2 + NR2-CH3 + H2O", 
    degeneracy = 1,
    kinetics = Arrhenius(A=(184.076, 'cm^3/(mol*s)'), n=3.49639, Ea=(52.767, 'kJ/mol'),
        T0=(1, 'K'), Tmin=(270, 'K'), Tmax=(600, 'K')),
    rank = 3, # means that the data is calculated using high-level theoretical methods
    shortDesc = u""" wb97xd/def2tzvp // dlpno-ccsd(t)/def2tzvpd  (L1-CC)""",
    longDesc =
u"""
Calculated by alongd (xq1343)
opt, freq: wB97x-D3/6-311++G(3df,3pd)
sp: CCSD(T)-F12a/aug-cc-pVTZ
rotors: B3LYP/6-311++G(3df,3pd)
"""
)
