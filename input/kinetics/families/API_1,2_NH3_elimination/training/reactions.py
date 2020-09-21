#!/usr/bin/env python
# encoding: utf-8

name = "1,2_NH3_elimination/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "N4 <=> NH3 + NH2NHN_p",
    degeneracy = 2,
    kinetics = Arrhenius(A=(1.31e+12, 's^-1'), n=0.78, Ea=(173.6, 'kJ/mol'),
        T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K'),
        comment = 'Fitted to 51 data points; dA = *|/ 2.33413, dn = +|- 0.105743, dEa = +|- 0.801565 kJ/mol'),
    rank = 3,
    shortDesc = u"""CCSD(T)-F12a/aug-cc-pVTZ//wB97x-D3/6-311++G(3df,3pd)""",
    longDesc =
u"""
Calculated by alongd (xq1343)
opt, freq: wB97x-D3/6-311++G(3df,3pd)
sp: CCSD(T)-F12a/aug-cc-pVTZ
rotors: B3LYP/6-311++G(3df,3pd)
""",
)

entry(
    index = 2,
    label = "N4c <=> NH3 + NH2NNH",
    degeneracy = 2,
    kinetics = Arrhenius(A=(2.30e+13, 's^-1'), n=0.42, Ea=(37.1, 'kJ/mol'),
        T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K'),
        comment = 'Fitted to 51 data points; dA = *|/ 1.173, dn = +|- 0.0199062, dEa = +|- 0.150895 kJ/mol'),
    rank = 3,
    shortDesc = u"""CCSD(T)-F12a/aug-cc-pVTZ//wB97x-D3/6-311++G(3df,3pd)""",
    longDesc =
u"""
Calculated by alongd (xq1344)
opt, freq: wB97x-D3/6-311++G(3df,3pd)
sp: CCSD(T)-F12a/aug-cc-pVTZ
rotors: B3LYP/6-311++G(3df,3pd)
""",
)

entry(
    index = 3,
    label = "NH2NHN_r <=> NH3 + N2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.17e+08, 's^-1'), n=3.54, Ea=(48.2, 'kJ/mol'),
        T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K'),
        comment = 'Fitted to 51 data points; dA = *|/ 2.36471, dn = +|- 0.107367, dEa = +|- 0.813875 kJ/mol'),
    rank = 3,
    shortDesc = u"""CCSD(T)-F12a/aug-cc-pVTZ//wB97x-D3/6-311++G(3df,3pd)""",
    longDesc =
u"""
Calculated by alongd (xq1444)
opt, freq: wB97x-D3/6-311++G(3df,3pd)
sp: CCSD(T)-F12a/aug-cc-pVTZ
rotors: B3LYP/6-311++G(3df,3pd)
""",
)

entry(
    index = 4,
    label = "N3 <=> H2NN(S) + NH3",
    degeneracy = 2,
    kinetics = Arrhenius(A=(2.26e+08, 's^-1'), n=1.68, Ea=(171.3, 'kJ/mol'),
        T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(3000, 'K'),
        comment = 'Fitted to 51 data points; dA = *|/ 1.13644, dn = +|- 0.0159552, dEa = +|- 0.120945 kJ/mol'),
    rank = 3,
    shortDesc = u"""CCSD(T)-F12a/aug-cc-pVTZ//wB97x-D3/6-311++G(3df,3pd)""",
    longDesc =
u"""
Calculated by alongd (xq1457)
opt, freq: wB97x-D3/6-311++G(3df,3pd)
sp: CCSD(T)-F12a/aug-cc-pVTZ
rotors: B3LYP/6-311++G(3df,3pd)
""",
)
