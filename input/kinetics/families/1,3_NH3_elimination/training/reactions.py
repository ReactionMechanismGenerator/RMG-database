#!/usr/bin/env python
# encoding: utf-8

name = "1,3_NH3_elimination/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "NH2NNH_r <=> NH3 + N2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.9e+09,'s^-1'), n=1.34, Ea=(142.2,'kJ/mol'), T0=(1,'K'), Tmin=(500,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """CCSD(T)-F12a/aug-cc-pVTZ//wB97x-D3/6-311++G(3df,3pd)""",
    longDesc = 
"""
Calculated by alongd (xq1445)
opt, freq: wB97x-D3/6-311++G(3df,3pd)
sp: CCSD(T)-F12a/aug-cc-pVTZ
rotors: B3LYP/6-311++G(3df,3pd)
Fitted to 51 data points; dA = *|/ 1.61639, dn = +|- 0.0584997, dEa = +|- 0.583637 kJ/mol
""",
)

entry(
    index = 1,
    label = "N3 <=> N2H2 + NH3",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(4.52e+08,'s^-1'), n=1.06, Ea=(221.9,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """CCSD(T)-F12a/aug-cc-pVTZ//wB97x-D3/6-311++G(3df,3pd)""",
    longDesc = 
"""
Calculated by alongd (xq1460)
opt, freq: wB97x-D3/6-311++G(3df,3pd)
sp: CCSD(T)-F12a/aug-cc-pVTZ
rotors: B3LYP/6-311++G(3df,3pd)
Fitted to 51 data points; dA = *|/ 1.22202, dn = +|- 0.0250126, dEa = +|- 0.189603 kJ/mol
""",
)

entry(
    index = 2,
    label = "N4 <=> NH2NNH_p + NH3",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(9.04e+09,'s^-1'), n=0.95, Ea=(207.4,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """CCSD(T)-F12a/aug-cc-pVTZ//wB97x-D3/6-311++G(3df,3pd)""",
    longDesc = 
"""
Calculated by alongd (xq1472)
opt, freq: wB97x-D3/6-311++G(3df,3pd)
sp: CCSD(T)-F12a/aug-cc-pVTZ
rotors: B3LYP/6-311++G(3df,3pd)
Fitted to 51 data points; dA = *|/ 3.06808, dn = +|- 0.139852, dEa = +|- 1.06012 kJ/mol
""",
)

entry(
    index = 3,
    label = "NCC <=> C2H4 + NH3",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(49000,'s^-1'), n=2.65, Ea=(65100,'cal/mol'), T0=(1,'K')),
    rank = 5,
    shortDesc = """CBS-QB3""",
    longDesc = 
"""
Alon Grinberg Dana, Beat Buesser, Shamel S. Merchant, William H. Green
Int. J. Chem. Kin. 2018, 50(4) 243-258
""",
)

