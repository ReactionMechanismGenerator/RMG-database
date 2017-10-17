#!/usr/bin/env python
# encoding: utf-8

name = "C2H4+O_Klipp2017"
shortDesc = u"C2H4 + O surface with product branching"
longDesc = u"""
The reaction of atomic oxygen with ethylene is a fundamental oxidation step in combustion.

Decomposition of the initial adduct via spin-allowed reaction channels on the triplet surface competes
with intersystem crossing (ISC) and a set of spin-forbidden reaction channels on the ground-state singlet
surface. This library describes product branching ratios based on the following publication:

X. Li, A.W. Jasper, J. Zádor, J.A. Miller, S.J. Klippenstein,
Theoretical kinetics of O + C2H4,
Proceedings of the Combustion Institute 36 (2017) 219–227
http://dx.doi.org/10.1016/j.proci.2016.06.053

Several different methods were used:
CCSDT(Q)/cc-pVDZ//CCSD(T)/cc-pVTZ
For barrierless reactions on the spin allowed surface CASPT2(2e,2o)/cc-pVTZ was used.
For reaction with barriers on the spin allowed surface CCSD(T)/CBS//B2PLYPD3/cc-pVTZ was used.
The total ISC rate was calculated using Landau–Zener statistical theory
non-statistical “prompt” branching in the dynamics immediately following ISC was predicted using
direct classical trajectories and the CASPT2(2e,2o)/cc-pVDZ surface.

Pressure dependence in the product branching fractions and the potential formation of stabilized products were
considered, but results show that rates are pressure-independent (with < 10% variations in the branching fractions)
up to 20 bar at 300 K and up to 200 bar at 1000 K.

Channels which account for less than 1% of the products are given in this library a low rate: 1e7 cm^3/(mol*s)
(since reactions 1a, 1b, 1c, 1e, 1f are all in the 1e10-1e13 cm^3/(mol*s) range at the 300-2500 K range)

The manuscript mentioned an additional reaction e' which wasn't included in this library, C2H4 + O <=> CH2(S) + CH2O,
since its rate wasn't discussed.

Library written by alongd
"""

entry(
    index = 1,
    label = "C2H4 + O <=> CH3 + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.319e+13,'cm^3/(mol*s)'), n=-1.717, Ea=(2893,'cal/mol'), T0=(298,'K'), Tmin=(300,'K'), Tmax=(2500,'K')),
    longDesc = u"""Reaction 1a""",
)

entry(
    index = 2,
    label = "C2H4 + O <=> CH3CO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.485e+11,'cm^3/(mol*s)'), n=-0.4843, Ea=(1958,'cal/mol'), T0=(298,'K'), Tmin=(300,'K'), Tmax=(2500,'K')),
    longDesc = u"""Reaction 1b""",
)

entry(
    index = 3,
    label = "C2H4 + O <=> CH2CHO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.022e+12,'cm^3/(mol*s)'), n=0.9475, Ea=(1724,'cal/mol'), T0=(298,'K'), Tmin=(300,'K'), Tmax=(2500,'K')),
    longDesc = u"""Reaction 1c""",
)

entry(
    index = 4,
    label = "C2H4 + O <=> C2H3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+7,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(298,'K'), Tmin=(300,'K'), Tmax=(2500,'K')),
    longDesc = u"""Reaction 1d""",
)

entry(
    index = 5,
    label = "C2H4 + O <=> CH2 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.868e+11,'cm^3/(mol*s)'), n=1.991, Ea=(2860,'cal/mol'), T0=(298,'K'), Tmin=(300,'K'), Tmax=(2500,'K')),
    longDesc = u"""Reaction 1e""",
)

entry(
    index = 6,
    label = "C2H4 + O <=> CH2CO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.315e+12,'cm^3/(mol*s)'), n=-1.831, Ea=(3180,'cal/mol'), T0=(298,'K'), Tmin=(300,'K'), Tmax=(2500,'K')),
    longDesc = u"""Reaction 1f""",
)

entry(
    index = 7,
    label = "C2H4 + O <=> CH4 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+7,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(298,'K'), Tmin=(300,'K'), Tmax=(2500,'K')),
    longDesc = u"""Reaction 1g""",
)

entry(
    index = 8,
    label = "C2H4 + O <=> C2H2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+7,'cm^3/(mol*s)'), n=0, Ea=(0,'cal/mol'), T0=(298,'K'), Tmin=(300,'K'), Tmax=(2500,'K')),
    longDesc = u"""Reaction 1h""",
)
