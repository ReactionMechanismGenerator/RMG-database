#!/usr/bin/env python
# encoding: utf-8

name = "N-S_interactions"
shortDesc = u"N-S_interactions"
longDesc =u"""
This library includes important nitrogen-sulfur interactions
Prepared by Alon Grinberg Dana

Reference legend:
[Marshall2004] A. Goumri, D.D. Shao, P. Marshall, J. Chem. Phys., 2004, 121, 9999, doi: 10.1063/1.1806419
[Marshall2012] K.M. Thompson, Y. Gao, P. Marshall, Int. J. Chem. Kin., 2012, 44(1), 90-99, doi: 10.1002/kin.20612
[Palmer1977] H. Freund, H.B. Palmer, Int. J. Chem. Kin., 1977, 9(6), 887-905, doi: 10.1002/kin.550090605
[Pilling2002a] M.A. Blitz, K.W. McKee, M.J. Pilling, J. Phys. Chem. A, 2002, 106(36), 8406-8410, doi: 10.1021/jp025508y
[Roth1996b] D. Woiki, P. Roth, Symposium (International) on Combustion, 1996, 26(1), 583-588, doi: 10.1016/S0082-0784(96)80263-3
"""

entry(
    index = 1,
    label = "NS + NO2 <=> N2 + SO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.55e+13, 'cm^3/(mol*s)'), n=-1.10, Ea=(0, 'cal/mol'), T0=(295, 'K')),
    shortDesc = u"""[Pilling2002a]""",
    longDesc =
u"""
Part of the "SOx-NOx" direct interactions subset
calculations done at the BD-(T)//B3LYP/6-31G++ level of theory
""",
)

entry(
    index = 2,
    label = "NO2 + SO2 <=> NO + SO3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.31e+12, 'cm^3/(mol*s)'), n=0, Ea=(53700, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(700, 'K'), Tmax=(2000, 'K')),
    shortDesc = u"""[Palmer1977]""",
    longDesc =
u"""
Part of the "SOx-NOx" direct interactions subset
T range: 700-2000 K
Shock tube measurement
Also given by [doi: 10.1016/S0010-2180(71)80077-9] for 700-1200 K
""",
)

entry(
    index = 3,
    label = "NO2 + S <=> SO + NO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.14e+13, 'cm^3/(mol*s)'), n=0, Ea=(-980, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(292, 'K'), Tmax=(656, 'K')),
    shortDesc = u"""[Marshall2012]""",
    longDesc =
u"""
Part of the "SOx-NOx" direct interactions subset
T range: 292-656 K
Experimentally measured, and PES verified using QCISD/6-311G(d,p)
""",
)

entry(
    index = 4,
    label = "S + NO <=> SNO",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.3e+14, 'cm^3/(mol*s)'), n=0.24, Ea=(0, 'cal/mol'), T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(800, 'K')),
        arrheniusLow = Arrhenius(A=(2.25e+15, 'cm^6/(mol^2*s)'), n=0, Ea=(-1868, 'cal/mol'), T0=(300, 'K'), Tmin=(300, 'K'), Tmax=(800, 'K')),
        alpha=0.22, T3=(7445, 'K'), T1=(1e-30, 'K'), efficiencies={}),
    shortDesc = u"""[Marshall2004]""",
    longDesc =
u"""
Part of the "SOx-NOx" direct interactions subset
T range: 300-800 K
Experimentally measured, and PES verified using CBS-QB3
Added as a training reaction to Birad_R_Recombination
""",
)

entry(
    index = 5,
    label = "S + NO <=> SO + N",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.08e+14, 'cm^3/(mol*s)'), n=0, Ea=(40100, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(2420, 'K'), Tmax=(3870, 'K')),
    shortDesc = u"""[Roth1996b]""",
    longDesc =
u"""
Part of the "SOx-NOx" direct interactions subset
T range: 2420-3870 K
Shock tube
The overall rate "S + NO <=> products" was determined, and the branching ratio for SO + N products is 80%-95%.
A branching ratio of 90% was ASSUMED here.
""",
)

entry(
    index = 6,
    label = "S + NO <=> NS + O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e+13, 'cm^3/(mol*s)'), n=0, Ea=(40100, 'cal/mol'), T0=(1, 'K'),
                         Tmin=(2420, 'K'), Tmax=(3870, 'K')),
    shortDesc = u"""[Roth1996b]""",
    longDesc =
u"""
Part of the "SOx-NOx" direct interactions subset
T range: 2420-3870 K
Shock tube
The overall rate "S + NO <=> products" was determined, and the branching ratio for NS + O products is 5%-20%.
A branching ratio of 10% was ASSUMED here.
""",
)
