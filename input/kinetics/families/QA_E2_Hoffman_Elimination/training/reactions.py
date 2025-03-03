#!/usr/bin/env python
# encoding: utf-8


name = "QA_E2_Hoffman_Elimination"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
 
 #THE KINETIC DATA IS NOT RELEVANT! UPDATE CORRECT PARAMETERS

entry(
    index = 0,
    label = "", 
    degeneracy = 1,
    kinetics = Arrhenius(A=(184.076, 's^-1'), n=3.49639, Ea=(4.64e+1, 'kJ/mol'),
        T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2600, 'K'),
        comment = 'Fitted to 51 data points; dA = *|/ 2.33413, dn = +|- 0.105743, dEa = +|- 0.801565 kJ/mol'),
    rank = 3, # means that the data is calculated using high-level theoretical methods
    shortDesc = u"""CCSD(T)-F12a/aug-cc-pVTZ//wB97x-D3/6-311++G(3df,3pd)""",
    longDesc =
u"""
Calculated by alongd (xq1343)
opt, freq: wB97x-D3/6-311++G(3df,3pd)
sp: CCSD(T)-F12a/aug-cc-pVTZ
rotors: B3LYP/6-311++G(3df,3pd)
""",
)
